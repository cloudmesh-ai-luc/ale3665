"""API endpoints for staged PDF lecture review and PowerPoint export."""
from __future__ import annotations

import logging
import re
from datetime import date
from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field, model_validator
from starlette.concurrency import run_in_threadpool

from .generator import generate_presentation
from .lecture_workflow import (
    MAX_FILES, MAX_FILE_BYTES, MAX_SLIDES, create_outline, produce_content
)

logger = logging.getLogger(__name__)
router = APIRouter()


class OutlineSlide(BaseModel):
    title: str = Field(min_length=1, max_length=130)
    points: list[str] = Field(min_length=1, max_length=4)
    source_ids: list[str] = Field(min_length=1)
    source_pages: dict[str, list[int]] = Field(default_factory=dict)


class Source(BaseModel):
    source_id: str
    filename: str


class Plan(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    skill_level: str
    sources: list[Source] = Field(min_length=1, max_length=MAX_FILES)
    quality_warnings: list[str] = Field(default_factory=list)
    outline: list[OutlineSlide] = Field(min_length=1, max_length=MAX_SLIDES - 1)

    @model_validator(mode='after')
    def verify(self):
        if self.skill_level not in {'beginner', 'intermediate', 'advanced'}:
            raise ValueError('Invalid skill level')
        allowed = {s.source_id for s in self.sources}
        if len(allowed) != len(self.sources):
            raise ValueError('Duplicate source IDs')
        used = set()
        for item in self.outline:
            if any(x not in allowed for x in item.source_ids):
                raise ValueError('Unknown source assigned to outline')
            used.update(item.source_ids)
        if used != allowed:
            raise ValueError('Every source must be assigned to at least one slide')
        return self


@router.get('/lecture-workspace', include_in_schema=False)
def workspace():
    return FileResponse(Path(__file__).with_name('lecture_workspace.html'), media_type='text/html')


@router.post('/api/lecture/outline')
async def outline_from_pdfs(
    files: list[UploadFile] = File(...),
    title: str = Form('Combined Lecture'),
    skill_level: str = Form('intermediate'),
    slide_count: int = Form(12),
):
    if not 1 <= len(files) <= MAX_FILES:
        raise HTTPException(422, f'Upload 1–{MAX_FILES} PDFs.')
    if not len(files) + 1 <= slide_count <= MAX_SLIDES:
        raise HTTPException(422, f'Choose {len(files) + 1}–{MAX_SLIDES} total slides for {len(files)} PDFs.')
    docs = []
    for file in files:
        try:
            data = await file.read(MAX_FILE_BYTES + 1)
        finally:
            await file.close()
        if len(data) > MAX_FILE_BYTES:
            raise HTTPException(413, f'{file.filename}: exceeds 10 MB.')
        docs.append((file.filename or 'lecture.pdf', data))
    try:
        result = await run_in_threadpool(create_outline, docs, title, skill_level, slide_count)
        return Plan.model_validate(result).model_dump()
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    except RuntimeError as exc:
        logger.exception('Qwen analysis failed')
        raise HTTPException(502, 'AI analysis failed. Check the Ollama service and server logs.') from exc


@router.post('/api/lecture/export')
async def export_plan(plan: Plan):
    try:
        content = await run_in_threadpool(produce_content, plan.model_dump())
        pptx = await run_in_threadpool(
            generate_presentation, plan.title, plan.skill_level,
            len(content['slides']), content
        )
        # Add source attributions below each slide using a separate, tiny
        # text box. These are traceability aids, not verified fact citations.
        from pptx import Presentation
        from pptx.util import Inches, Pt
        from pptx.dml.color import RGBColor
        pres = Presentation(pptx)
        source_map = {source.source_id: source.filename for source in plan.sources}
        for slide, outline_slide in zip(list(pres.slides)[1:], plan.outline):
            references = []
            for sid in outline_slide.source_ids:
                pages = outline_slide.source_pages.get(sid, [])
                p = ','.join(map(str, pages[:5]))
                references.append(f'{source_map[sid]}' + (f' p.{p}' if p else ''))
            box = slide.shapes.add_textbox(Inches(0.5), Inches(7.15), Inches(12.3), Inches(0.24))
            tf = box.text_frame
            tf.text = 'Source material: ' + ' | '.join(references)
            tf.paragraphs[0].font.size = Pt(9)
            tf.paragraphs[0].font.color.rgb = RGBColor(90, 102, 121)
        from io import BytesIO
        exported = BytesIO()
        pres.save(exported)
        exported.seek(0)
    except (ValueError, RuntimeError, OSError) as exc:
        logger.exception('PowerPoint export failed')
        raise HTTPException(502, 'Slide generation failed; inspect server logs.') from exc
    filename = re.sub(r'[^a-zA-Z0-9]+', '_', plan.title).strip('_')[:75] or 'Lecture'
    filename += '_' + date.today().isoformat() + '.pptx'
    return StreamingResponse(exported, media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation',
        headers={'Content-Disposition': f'attachment; filename="{filename}"'})
