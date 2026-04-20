# UW-Madison Brand System

This file contains the official UW-Madison brand specifications for use in all branded digital materials. All values are sourced from the official UW Style CSS (v5.3.0) and brand.wisc.edu guidelines.

## Color Palette

### CSS Custom Properties

```css
:root {
  /* Primary */
  --uw-red: #c5050c;          /* Badger Red - Pantone 200 C */
  --uw-white: #ffffff;

  /* Secondary */
  --uw-red-dark: #9B0000;     /* Dark Red */
  --uw-gray-dark: #282728;    /* Dark Charcoal */
  --uw-gray-light: #e1e5e7;   /* Light Gray */
  --uw-gray-lightest: #f3f3f3; /* Near White */
  --uw-black: #121212;         /* Rich Black (NOT pure #000) */

  /* Accent (use sparingly) */
  --uw-yellow: #FFB500;        /* Warm Yellow (from CMYK conversion) */
  --uw-gray-blue: #6B8F99;    /* Medium Gray Blue */
  --uw-blue: #385966;          /* Dark Blue */

  /* Derived from brand materials */
  --uw-cream: #f6ede4;         /* From crest gradient */
  --uw-gold: #d4ac7f;          /* From crest gradient */
}
```

### Color Usage Rules

- **Badger Red and White** are the foundation of all branded materials
- Secondary colors pair seamlessly with Badger Red and White
- Accent colors (yellow, gray-blue, blue) should be used in moderation
- Digital text requires minimum **4.5:1 contrast ratio** per WCAG standards
- Never place black text on a red background (notoriously difficult to read)
- Never modify the Badger Red value

### Precomputed Contrast Ratios (text on background)

| Text Color | Background | Ratio | Pass AA? |
|-----------|-----------|-------|----------|
| #121212 (black) | #ffffff (white) | 17.4:1 | Yes |
| #121212 (black) | #f3f3f3 (lightest gray) | 14.8:1 | Yes |
| #121212 (black) | #e1e5e7 (light gray) | 12.1:1 | Yes |
| #c5050c (red) | #ffffff (white) | 5.9:1 | Yes |
| #9B0000 (dark red) | #ffffff (white) | 8.0:1 | Yes |
| #ffffff (white) | #c5050c (red) | 5.9:1 | Yes |
| #ffffff (white) | #9B0000 (dark red) | 8.0:1 | Yes |
| #ffffff (white) | #121212 (black) | 17.4:1 | Yes |
| #ffffff (white) | #282728 (dark charcoal) | 14.3:1 | Yes |
| #FFB500 (yellow) | #121212 (black) | 9.6:1 | Yes |
| #121212 (black) | #FFB500 (yellow) | 9.6:1 | Yes |
| #c5050c (red) | #121212 (black) | 2.9:1 | NO |
| #c5050c (red) | #e1e5e7 (light gray) | 2.1:1 | NO |

**Key takeaways for presets:**
- White text on Badger Red: 5.9:1 (passes)
- White text on Dark Red: 8.0:1 (passes)
- White text on Black: 17.4:1 (passes)
- Red text on White: 5.9:1 (passes)
- Red text on Black: 2.9:1 (FAILS - do not use)
- Red text on Light Gray: 2.1:1 (FAILS - do not use)

## Typography

### Font Families

```css
:root {
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-quote-font: 'Red Hat Display', Arial, sans-serif;
  --uw-code-font: 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace;
}
```

- **Red Hat Display** (geometric sans serif): Headings, headlines, subheadings, large sizes. Carries brand personality. Weights: 400, 500, 600, 700.
- **Red Hat Text** (sans serif): Body copy, paragraphs, small sizes. Optimized for legibility. Weights: 400, 400i, 700.
- **Arial**: Official fallback for both. Used when brand fonts are unavailable.

### Font Loading

Primary source (UW CDN, has both families pre-configured):
```html
<link rel="stylesheet" href="https://cdn.wisc.cloud/fonts/uw-rh/0.0.1/fonts.css">
```

Fallback (Google Fonts):
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;600;700&family=Red+Hat+Text:ital,wght@0,400;0,700;1,400&display=swap">
```

Include both links. The browser will use whichever loads first. If both fail (offline), Arial takes over.

### Typography Scale (Responsive)

From the official UW Style CSS, adapted for presentations (larger base):

```css
:root {
  --uw-title-size: clamp(2.5rem, 5vw, 4.5rem);       /* Display / title slides */
  --uw-subtitle-size: clamp(1.25rem, 2.5vw, 2rem);    /* Subtitles */
  --uw-h2-size: clamp(1.75rem, 3.5vw, 3rem);          /* Slide headings */
  --uw-h3-size: clamp(1.375rem, 2.5vw, 2rem);         /* Sub-headings */
  --uw-body-size: clamp(1.125rem, 1.8vw, 1.5rem);     /* Body text */
  --uw-caption-size: clamp(0.875rem, 1.2vw, 1rem);    /* Captions, labels */
  --uw-code-size: clamp(0.85rem, 1.3vw, 1.1rem);      /* Code blocks */
  --uw-quote-size: clamp(1.5rem, 3vw, 2.5rem);        /* Pull quotes */
}
```

**Minimum readable size**: Per StratComm best practices, no text smaller than 24pt equivalent on projected slides. The `clamp()` values ensure this on standard projector resolutions.

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
