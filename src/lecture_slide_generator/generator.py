from datetime import date
from io import BytesIO

from pptx import Presentation
from pptx.util import Inches, Pt


def generate_presentation(
    topic: str,
    skill_level: str = "beginner",
    slide_count: int = 5,
    content: dict | None = None,
) -> BytesIO:
    """Generate a lecture presentation using structured AI content."""

    if content is None:
        raise ValueError("AI-generated lecture content is required.")

    slides_data = content.get("slides", [])

    if len(slides_data) != slide_count:
        raise ValueError("The generated slide count is incorrect.")

    presentation = Presentation()
    presentation.slide_width = Inches(13.333)
    presentation.slide_height = Inches(7.5)

    # Title slide
    title_slide = presentation.slides.add_slide(
        presentation.slide_layouts[0]
    )

    title_slide.shapes.title.text = topic

    title_slide.placeholders[1].text = (
        "Educational Lecture\n"
        f"Level: {skill_level.title()}\n"
        f"Created: {date.today().isoformat()}"
    )

    # AI-generated content slides
    for slide_data in slides_data[1:]:
        slide = presentation.slides.add_slide(
            presentation.slide_layouts[1]
        )

        slide.shapes.title.text = slide_data["title"]
        text_frame = slide.placeholders[1].text_frame
        text_frame.clear()

        for index, bullet in enumerate(slide_data["bullets"]):
            paragraph = (
                text_frame.paragraphs[0]
                if index == 0
                else text_frame.add_paragraph()
            )

            paragraph.text = bullet
            paragraph.level = 0
            paragraph.font.size = Pt(19)
            paragraph.space_after = Pt(12)

    output = BytesIO()
    presentation.save(output)
    output.seek(0)

    return output
