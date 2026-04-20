# UW-Madison Brand System

Official UW-Madison brand specifications for all branded digital materials. Sourced from the UW Style CSS (v5.3.0) and [brand.wisc.edu](https://brand.wisc.edu/) guidelines.

For the canonical token definitions (CSS custom properties, values, and mappings to UW Style CSS), see **[`tokens.md`](tokens.md)**.

## Color Palette

The brand palette is defined in `tokens.md` under "Colors > Brand Palette." The key rules for using those colors:

- **Badger Red (`--uw-red`) and White** are the foundation of all branded materials
- Secondary colors pair seamlessly with Badger Red and White
- Accent colors (yellow, gray-blue, blue) should be used in moderation
- Digital text requires minimum **4.5:1 contrast ratio** per WCAG standards
- Never place black text on a red background (fails contrast)
- Never modify the Badger Red value (`#c5050c`)
- Links use `--uw-link-blue` (`#036796`) on light backgrounds, white on dark backgrounds

See `tokens.md` for the full contrast ratio table with all pre-tested combinations.

## Typography

Font families, weights, loading strategy, and type scales (web and presentation) are defined in `tokens.md` under "Typography."

Key rules:

- **Red Hat Display** (geometric sans-serif): Headings, headlines, subheadings, large sizes. Carries brand personality. Weights: 400, 500, 600, 700.
- **Red Hat Text** (sans-serif): Body copy, paragraphs, UI text, small sizes. Optimized for legibility. Weights: 400, 400i, 700.
- **Arial**: Official fallback for both. Used when brand fonts are unavailable.
- Two type scales exist: one for web (`--uw-text-*`) and one for projected slides (`--uw-slide-*-size`). Use the appropriate scale for the output format.
- Per StratComm best practices, no text smaller than 24pt equivalent on projected slides.

## Logo Usage

### Available Variants

1. **Full-color W Crest** (`uw-crest-color.svg`): Gold gradient shield with black outline, red center, white W. Use on light backgrounds.
2. **1-color W Crest** (`uw-crest-1color.svg`): Single-color stroke version. On dark backgrounds, set the SVG fill to white.
3. **Favicon W** (`favicon-w.svg`): Simple white W on red square. Used for the HTML favicon only.

### Placement Rules

- **Position**: Upper-right corner of the slide (matching all official PPT templates)
- **Clear space**: Minimum buffer zone equal to the width of the W Crest on all sides
- **Size**: `clamp(40px, 5vw, 80px)` width, scales proportionally
- **When to show**: Always on title slide and closing slide. Optional on other slides.
- **Dark backgrounds**: Use the 1-color variant with `fill: #ffffff`
- **Light backgrounds**: Use the full-color variant

### Logo Don'ts

- Never adjust colors of the logo
- Never substitute fonts in the logo
- Never replace words or reconfigure elements
- Never combine with other logos into a single mark
- Never place on busy backgrounds that reduce readability
- Never display multiple W Crest logos on the same slide

## Brand Design Elements

### The Mini-Bar

The UW mini-bar is the signature design element. It appears as a small red bar above headings.

```css
.uw-mini-bar::before {
  content: "";
  display: block;
  background-color: #c5050c;
  width: 1.5em;
  height: 0.2em;
  margin-bottom: 0.375rem;
}
```

- Use above slide headings (h2, h3) on content slides
- On section dividers (red background), switch to white: `.uw-mini-bar-white`
- Center variant available: `.uw-mini-bar-center`

### The Red Bar / Stripe

A full-width or partial-width red bar used as a structural accent:
- As the top bar of the progress indicator
- As a bottom border on title slides
- As a vertical rule on data-driven layouts

### Graphic Elements (for reference, not embedded)

The `uw resources/` directory contains hand-drawn graphic elements in PNG format that match the brand's playful personality: hand-drawn W, waves, scribbles, dots, grid textures, explosion, lightning bolt, etc. These are available in red, black, and white. They can be referenced as external images when presenting from a known location, but are NOT embedded in self-contained HTML due to file size.

## Brand Voice (Content Guidance)

When generating slide content, the tone should be:

- **Passionate**: Bold and proud, never pretentious
- **Approachable**: Welcoming, genuine, relatable
- **Unconventional**: Creative and witty while professional
- **Catalytic**: Forward-thinking without boastfulness
- **Purposeful**: Active, concise, clear, no jargon
- **Tenacious**: Inspiring without hyperbole
- **Grounded**: Curious and intellectual without arrogance

Writing style: accessible to wide audiences, avoid jargon and acronyms, never pompous. Use "the University of Wisconsin-Madison" or "UW-Madison" (with en-dash).
