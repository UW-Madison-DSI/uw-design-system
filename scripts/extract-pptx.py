#!/usr/bin/env python3
"""Extract slide content from a PowerPoint (.pptx) file.

Outputs structured text that can be used to generate an HTML presentation.
Extracts slide titles, body text, speaker notes, image descriptions, and
basic layout information.

Usage:
    python extract-pptx.py <path-to-pptx> [--output <path-to-txt>]

Requires:
    pip install python-pptx
"""

import argparse
import sys
from pathlib import Path

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
except ImportError:
    print("Error: python-pptx is required. Install with: pip install python-pptx")
    sys.exit(1)


def extract_text_from_shape(shape) -> str:
    """Extract all text from a shape's text frame."""
    if not shape.has_text_frame:
        return ""
    paragraphs = []
    for paragraph in shape.text_frame.paragraphs:
        text = paragraph.text.strip()
        if text:
            paragraphs.append(text)
    return "\n".join(paragraphs)


def get_shape_type_hint(shape) -> str:
    """Determine the likely purpose of a shape based on its properties."""
    if shape.has_table:
        return "table"
    if shape.has_chart:
        return "chart"
    if hasattr(shape, "image"):
        return "image"
    if shape.has_text_frame:
        for paragraph in shape.text_frame.paragraphs:
            if paragraph.level > 0:
                return "bullet-list"
        return "text"
    return "other"


def extract_table(shape) -> str:
    """Extract table data as formatted text."""
    table = shape.table
    rows = []
    for row in table.rows:
        cells = [cell.text.strip() for cell in row.cells]
        rows.append(" | ".join(cells))
    if rows:
        # Add a separator after the header row
        header = rows[0]
        separator = " | ".join(["---"] * len(rows[0].split(" | ")))
        return "\n".join([header, separator] + rows[1:])
    return ""


def extract_slide(slide, slide_number: int) -> dict:
    """Extract all content from a single slide."""
    result = {
        "number": slide_number,
        "title": "",
        "content": [],
        "notes": "",
        "images": [],
        "tables": [],
        "layout": slide.slide_layout.name if slide.slide_layout else "unknown",
    }

    # Extract title
    if slide.shapes.title:
        result["title"] = slide.shapes.title.text.strip()

    # Extract content from all shapes
    for shape in slide.shapes:
        # Skip the title shape (already extracted)
        if shape == slide.shapes.title:
            continue

        shape_type = get_shape_type_hint(shape)

        if shape_type == "table":
            result["tables"].append(extract_table(shape))
        elif shape_type == "image":
            alt_text = shape.name or "Image"
            result["images"].append(alt_text)
        elif shape_type in ("text", "bullet-list"):
            text = extract_text_from_shape(shape)
            if text:
                result["content"].append(text)

    # Extract speaker notes
    if slide.has_notes_slide:
        notes_text = slide.notes_slide.notes_text_frame.text.strip()
        if notes_text:
            result["notes"] = notes_text

    return result


def format_output(slides: list[dict]) -> str:
    """Format extracted slides as readable structured text."""
    output_lines = []
    output_lines.append("=" * 60)
    output_lines.append("EXTRACTED POWERPOINT CONTENT")
    output_lines.append(f"Total slides: {len(slides)}")
    output_lines.append("=" * 60)
    output_lines.append("")

    for slide in slides:
        output_lines.append(f"--- Slide {slide['number']} ---")
        output_lines.append(f"Layout: {slide['layout']}")

        if slide["title"]:
            output_lines.append(f"Title: {slide['title']}")

        if slide["content"]:
            output_lines.append("Content:")
            for block in slide["content"]:
                for line in block.split("\n"):
                    output_lines.append(f"  - {line}")

        if slide["tables"]:
            output_lines.append("Tables:")
            for table in slide["tables"]:
                output_lines.append(table)

        if slide["images"]:
            output_lines.append("Images:")
            for img in slide["images"]:
                output_lines.append(f"  [Image: {img}]")

        if slide["notes"]:
            output_lines.append(f"Speaker Notes: {slide['notes']}")

        output_lines.append("")

    return "\n".join(output_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Extract content from a PowerPoint file for HTML presentation generation."
    )
    parser.add_argument("pptx_path", type=str, help="Path to the .pptx file")
    parser.add_argument(
        "--output", "-o", type=str, default=None,
        help="Output file path (default: prints to stdout)"
    )
    args = parser.parse_args()

    pptx_path = Path(args.pptx_path)
    if not pptx_path.exists():
        print(f"Error: File not found: {pptx_path}")
        sys.exit(1)

    if not pptx_path.suffix.lower() == ".pptx":
        print(f"Warning: File does not have .pptx extension: {pptx_path}")

    prs = Presentation(str(pptx_path))
    slides = []
    for i, slide in enumerate(prs.slides, 1):
        slides.append(extract_slide(slide, i))

    output = format_output(slides)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(output)
        print(f"Extracted content written to: {output_path}")
    else:
        print(output)


if __name__ == "__main__":
    main()
