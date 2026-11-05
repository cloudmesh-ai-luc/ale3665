"""Conservative checks for repeated slide concepts and teaching sequence.

No external model calls. All replacements come from previously extracted source concepts.
This module does not prove factual accuracy or validate source citations.
"""
from __future__ import annotations
import re
from collections import Counter

STOP = {'a','an','the','and','or','of','to','for','in','on','with','by','from','is','are',
        'this','that','as','what','how','why','about','using','used','based','can','should',
        'ai','artificial','intelligence','machine','learning','systems','system','concepts',
        'fundamentals','foundations','overview','introduction','understanding'}


def _words(text: str) -> set[str]:
    return {word for word in re.findall(r'[a-z0-9]+', text.lower()) if len(word) > 2 and word not in STOP}


def _content_words(slide: dict) -> set[str]:
    return _words(' '.join(slide.get('points', [])))


def _similarity(a: dict, b: dict) -> float:
    x, y = _content_words(a), _content_words(b)
    return len(x & y) / len(x | y) if x and y else 0.0


def _duplicate(a: dict, b: dict) -> bool:
    a_points = [p.strip().casefold() for p in a.get('points', [])]
    b_points = [p.strip().casefold() for p in b.get('points', [])]
    if a_points and a_points == b_points:
        return True
    if len(set(a_points) & set(b_points)) >= 2:
        return True
    return _similarity(a, b) >= 0.72


def _stage(slide: dict) -> int:
    """Best-effort pedagogical order, never a claim of validated prerequisites."""
    title = slide.get('title', '').casefold()
    if re.search(r'conclusion|summary|takeaway|discussion|recap', title):
        return 6
    if re.search(r'ethic|fairness|bias|privacy|risk|responsib|oversight|security|transparen', title):
        return 5
    if re.search(r'application|example|use.case|case.study|deployment|real.world', title):
        return 4
    if re.search(r'evaluat|testing|validation|training|data quality|workflow|overfitt', title):
        return 3
    if re.search(r'type|method|mechanism|supervised|unsupervised|reinforcement|algorithm|model', title):
        return 2
    if re.search(r'definition|introduction|foundation|prerequisite|what is|basics', title):
        return 0
    return 2


def _candidates(analyses: list[dict], source_ids: list[str]):
    for doc in analyses:
        if doc['source_id'] in source_ids:
            for concept in doc['concepts']:
                yield {'title': concept['title'],
                       'points': concept['points'][:4],
                       'source_ids': [doc['source_id']],
                       'source_pages': {doc['source_id']: concept['pages']}}


def review_outline(outline: list[dict], analyses: list[dict]) -> tuple[list[dict], list[str]]:
    """Replace clear repeated slides from unused extracted concepts; report limitations.

    Preserves every original source assignment when replacing a slide.  Multi-source
    slides are left for an instructor rather than fabricating cross-source support.
    """
    result = [dict(item) for item in outline]
    warnings: list[str] = []
    replacements = 0
    for idx, current in enumerate(result):
        if not any(_duplicate(current, previous) for previous in result[:idx]):
            continue
        ids = current.get('source_ids', [])
        if len(ids) != 1:
            warnings.append(f'Potential repeated material at slide {idx + 2}; review the multi-source slide.')
            continue
        choices = list(_candidates(analyses, ids))
        choice = next((c for c in choices if all(not _duplicate(c, s) for j, s in enumerate(result) if j != idx)), None)
        if choice is None:
            warnings.append(f'No distinct source-backed replacement found for slide {idx + 2}; consider fewer slides.')
        else:
            result[idx] = choice
            replacements += 1
    if replacements:
        warnings.append(f'Replaced {replacements} repeated slide(s) with different extracted source concepts; review the changes.')
    result.sort(key=_stage)
    for idx, slide in enumerate(result, start=2):
        distinctive_title = _words(slide.get('title', ''))
        if distinctive_title and not distinctive_title.intersection(_content_words(slide)):
            warnings.append(f'Slide {idx}: title may not match the teaching points — {slide["title"][:65]}')
    for idx in range(len(result)):
        for prev in range(idx):
            if _duplicate(result[idx], result[prev]):
                warnings.append(f'Slide {idx + 2} may repeat slide {prev + 2}; revise before exporting.')
                break
    return result, list(dict.fromkeys(warnings))
