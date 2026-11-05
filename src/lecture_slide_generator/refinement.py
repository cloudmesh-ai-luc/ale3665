"""Conservative, instructor-approved edits for a source-labelled lecture outline.

All proposals are based on the *existing* outline. This module does not
have access to the original PDF text and cannot verify factual support.
"""
from __future__ import annotations

import re
from collections import Counter


def _norm(text: str) -> str:
    return ' '.join(re.findall(r'[a-z0-9]+', text.casefold()))


def _tokens(text: str) -> set[str]:
    stop = {'the', 'and', 'for', 'are', 'with', 'from', 'into', 'that', 'this', 'can', 'should', 'about'}
    return set(_norm(text).split()) - stop


def _score(a: dict, b: dict) -> float:
    left = _tokens(' '.join(a['points']))
    right = _tokens(' '.join(b['points']))
    return len(left & right) / len(left | right) if left and right else 0.0


def _unique_points(a: dict, b: dict) -> list[str]:
    points, used = [], set()
    for point in a['points'] + b['points']:
        key = _norm(point)
        if key and key not in used:
            points.append(point)
            used.add(key)
    return points


def _all_sources(slides: list[dict]) -> set[str]:
    return {sid for slide in slides for sid in slide['source_ids']}


def propose_refinements(plan: dict, title_proposals: dict[int, str] | None = None) -> list[dict]:
    """Return advisory edits; merge only if every point can be retained.

    Indices are zero-based *content slide* indices. Client must compare
    proposal's original snapshot before applying to avoid stale edits.
    """
    slides = plan['outline']
    suggestions = []
    for index, slide in enumerate(slides):
        if title_proposals and index in title_proposals:
            suggested = title_proposals[index].strip()
            if (3 <= len(suggested) <= 130 and suggested.casefold() != slide['title'].casefold()
                    and '\n' not in suggested):
                suggestions.append({
                    'id': f'title-{index}', 'kind': 'rename', 'index': index,
                    'original': {'title': slide['title'], 'points': slide['points']},
                    'suggested_title': suggested,
                    'reason': 'Suggested title based on the slide’s existing teaching points; verify its fit.'
                })
    for right in range(1, len(slides)):
        for left in range(right):
            a, b = slides[left], slides[right]
            similarity = _score(a, b)
            exact = [_norm(x) for x in a['points']] == [_norm(x) for x in b['points']]
            shared = len(set(_norm(x) for x in a['points']) & set(_norm(x) for x in b['points']))
            if not (exact or shared >= 2 or similarity >= 0.78):
                continue
            combined = _unique_points(a, b)
            resulting = [s for j, s in enumerate(slides) if j != right]
            covered = _all_sources(resulting) | set(b['source_ids'])
            originally = _all_sources(slides)
            allowed = len(combined) <= 4 and covered == originally
            if allowed:
                pages = {sid: list(pgs) for sid, pgs in a.get('source_pages', {}).items()}
                for sid, nums in b.get('source_pages', {}).items():
                    pages[sid] = sorted(set(pages.get(sid, []) + nums))
                suggestions.append({
                    'id': f'merge-{left}-{right}', 'kind': 'merge',
                    'index': left, 'remove_index': right,
                    'original': {'left': a, 'right': b},
                    'merged_slide': {
                        'title': a['title'], 'points': combined,
                        'source_ids': list(dict.fromkeys(a['source_ids'] + b['source_ids'])),
                        'source_pages': pages,
                    },
                    'reason': f'Possible overlap between slides {left+2} and {right+2}; merging retains all distinct listed points and sources. Review before accepting.',
                })
            else:
                suggestions.append({
                    'id': f'overlap-{left}-{right}', 'kind': 'review',
                    'index': right, 'original': {'left': a, 'right': b},
                    'reason': f'Slides {left+2} and {right+2} may overlap, but cannot be merged safely without dropping teaching points. Edit manually or reduce the slide count.',
                })
            break  # One candidate pairing per later slide
    return suggestions[:30]


def title_mismatch_indices(plan: dict) -> list[int]:
    """Locate slides mentioned by existing advisory title warnings."""
    found = set()
    for warning in plan.get('quality_warnings', []):
        for number in re.findall(r'\bSlide\s+(\d+):\s+title may not match', warning, re.I):
            index = int(number) - 2
            if 0 <= index < len(plan['outline']):
                found.add(index)
    return sorted(found)[:8]
