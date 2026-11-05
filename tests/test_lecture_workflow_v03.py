"""Offline regression tests for the multi-PDF lecture planning workflow."""

import pymupdf
import pytest

from lecture_slide_generator import lecture_workflow as workflow


def make_pdf(text: str) -> bytes:
    pdf = pymupdf.open()
    page = pdf.new_page()
    page.insert_text((70, 70), text)
    result = pdf.tobytes()
    pdf.close()
    return result


def test_reads_three_distinct_lecture_pdfs():
    docs = workflow.read_documents([
        (f'lecture_{i}.pdf', make_pdf(f'Lecture {i}: distinct educational concept'))
        for i in range(1, 4)
    ])
    assert [d['source_id'] for d in docs] == ['S1', 'S2', 'S3']
    assert all(d['pages'] for d in docs)


def test_invalid_pdf_rejected():
    with pytest.raises(ValueError, match='valid PDF'):
        workflow.read_documents([('lecture.pdf', b'NOT A PDF')])


def test_analyze_and_sequence_covers_sources(monkeypatch):
    def simulated_model(prompt, timeout=300):
        if 'summarizing ONE SECTION' in prompt:
            return {'concepts': [{'title': 'Foundation', 'points': ['Point one', 'Point two']}]}
        if 'instructional designer planning' in prompt:
            return {'slides': [
                {'title': f'Content {n}', 'source_ids': [f'S{n % 3 + 1}'],
                 'points': ['Fact A', 'Fact B'], 'source_pages': {}}
                for n in range(7)
            ]}
        return {'slides': [{'bullets': ['Fact A', 'Fact B']} for _ in range(4)]}

    monkeypatch.setattr(workflow, '_model', simulated_model)
    docs = [(f'L{i}.pdf', make_pdf(f'Lecture topic {i}')) for i in range(1, 4)]
    plan = workflow.create_outline(docs, 'AI Foundations', 'intermediate', 8)
    assert len(plan['outline']) == 7
    assert {sid for slide in plan['outline'] for sid in slide['source_ids']} == {'S1', 'S2', 'S3'}


def test_requires_at_least_one_content_slide_per_pdf(monkeypatch):
    docs = [(f'L{i}.pdf', make_pdf(f'Lecture topic {i}')) for i in range(1, 4)]
    with pytest.raises(ValueError, match='at least 4 slides'):
        workflow.create_outline(docs, 'AI Foundations', 'intermediate', 3)
