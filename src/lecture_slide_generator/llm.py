
"""Generate lecture content using self-hosted Ollama."""

import json
import os
from urllib.request import Request, urlopen
from urllib.error import URLError


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://127.0.0.1:11434"
)
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")


def generate_lecture_content(
    topic: str,
    skill_level: str,
    slide_count: int,
) -> dict:
    """Request structured lecture content from Qwen."""

    prompt = f"""
You are an expert university lecturer and instructional designer.

Create a high-quality educational PowerPoint outline.

Topic: {topic}
Audience skill level: {skill_level}
Number of slides: {slide_count}

Requirements:
- Produce exactly {slide_count} slides.
- Slide 1 must be a title slide.
- Adapt vocabulary, explanations, and technical depth
  to the audience's skill level.
- Use clear, accurate educational content.
- Include meaningful concepts, not placeholder text.
- Use 3 to 5 concise bullet points per content slide.
- Include an introduction, core concepts, examples,
  and a conclusion where appropriate.
- Return only valid JSON.

Use this JSON structure:
{{
  "slides": [
    {{
      "title": "Slide title",
      "bullets": ["Point 1", "Point 2", "Point 3"]
    }}
  ]
}}
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.3
        }
    }

    request = Request(
        url=f"{OLLAMA_URL}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(request, timeout=180) as response:
            result = json.load(response)
    except (URLError, TimeoutError) as exc:
        raise RuntimeError(
            f"Could not communicate with Ollama: {exc}"
        ) from exc

    try:
        content = json.loads(result["response"])
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError(
            "Qwen returned an invalid JSON response."
        ) from exc

    slides = content.get("slides")
    if not isinstance(slides, list) or len(slides) != slide_count:
        raise ValueError("Qwen returned an unexpected slide count.")

    for slide in slides:
        if (
            not isinstance(slide, dict)
            or not isinstance(slide.get("title"), str)
            or not isinstance(slide.get("bullets"), list)
            or not all(
                isinstance(bullet, str)
                for bullet in slide["bullets"]
            )
        ):
            raise ValueError("Qwen returned an invalid slide structure.")

    return content
