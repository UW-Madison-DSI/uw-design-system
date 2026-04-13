# Accessibility Requirements

All generated presentations must meet WCAG 2.1 AA standards. UW-Madison requires accessibility compliance for all digital materials.

## Color Contrast

- Minimum **4.5:1** contrast ratio for normal text
- Minimum **3:1** for large text (18pt+ or 14pt+ bold)
- See the contrast ratio table in `brand-system.md` for precomputed values
- Test any custom color combinations before using them
- Never place red text on dark backgrounds (fails contrast)
- Never place light gray text on white backgrounds (fails contrast)

## Typography

- No text smaller than approximately 14px rendered size
- No all-capital-letter headings or body text
- Line height minimum 1.5 for body text, 1.2 for headings
- Sufficient spacing between list items

## Semantic HTML

- Use proper heading hierarchy: `<h1>` for title slide only, `<h2>` for slide headings, `<h3>` for sub-headings
- Use `<section>` for each slide
- Use `<ul>` / `<ol>` for lists (not just styled `<p>` tags)
- Use `<blockquote>` with `<cite>` for quotations
- Use `<table>` with `<thead>`, `<th scope="col">`, and `<th scope="row">` for data tables
- Use `<code>` and `<pre>` for code blocks

## ARIA and Landmarks

```html
<!-- Presentation container -->
<main class="presentation" role="main" aria-label="Slide presentation">

<!-- Progress bar -->
<div class="progress-bar" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">

<!-- Navigation -->
<nav class="nav-dots" aria-label="Slide navigation">
  <button class="nav-dot" aria-label="Go to slide 1" aria-current="step">
  <button class="nav-dot" aria-label="Go to slide 2">

<!-- Current slide -->
<section class="slide" aria-current="step">

<!-- Hidden elements -->
<div class="keyboard-hint" aria-hidden="true">
<div class="presenter-notes" aria-hidden="true">
```

## Keyboard Navigation

The SlidePresentation JS class must support:
- **Arrow keys** (Up/Down, Left/Right): Navigate between slides
- **Space / PageDown**: Next slide
- **PageUp**: Previous slide
- **Home**: First slide
- **End**: Last slide
- **Escape**: Return to first slide
- **N**: Toggle presenter notes

## Images

- Every `<img>` must have a descriptive `alt` attribute
- Decorative images use `alt=""` and `aria-hidden="true"`
- The W Crest logo SVG should have `aria-hidden="true"` (it's decorative branding, not content)

## Motion and Animation

```css
@media (prefers-reduced-motion: reduce) {
  .animate-in, .animate-fade, .animate-scale,
  .stagger > * {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

- All animations must respect `prefers-reduced-motion`
- No auto-playing animations or infinite loops
- Transitions should be subtle (max 0.8s duration)
- Never use animations that flash or strobe

## Focus Management

- Navigation dots must be focusable buttons (not divs)
- Keyboard focus should follow the current slide
- Skip-to-content patterns are not needed (the entire page is the presentation)

## Print Accessibility

- Print styles must:
  - Remove navigation UI (dots, progress bar, keyboard hint)
  - Make all animated content visible (opacity: 1, transform: none)
  - Add page breaks between slides
  - Ensure text is black on white for printing

## Content Accessibility (UW IT Guidelines)

Per UW-Madison Policy UW-519 and the [UW IT accessible presentations guide](https://it.wisc.edu/learn/make-it-accessible/accessible-online-and-in-person-presentations/), generated presentations must satisfy these *content* accessibility requirements in addition to the technical/markup requirements above.

### Plain Language and Acronyms

- **Spell out acronyms on first use**: write the full term followed by the abbreviation in parentheses, e.g., "Retrieval-Augmented Generation (RAG)"
- After first use, the acronym alone is fine
- Avoid jargon when a plain term works
- Define domain-specific terms in context when the audience may not know them
- This aids comprehension for non-experts and screen reader users alike

### Presenter Notes Describe Visuals

Every slide that contains a chart, diagram, image, code block, or non-trivial visual layout MUST have a `data-notes="..."` attribute on the `<section class="slide">` element describing the visual content.

The notes should let someone understand the slide without seeing it:
- **Charts**: describe the trend, key values, and the takeaway. Example: "Bar chart showing prescreen filtering reduces papers from 100,000 to about 30,000 before expensive retrieval, saving roughly 70% of LLM costs."
- **Images**: describe what is depicted and why it matters. Example: "Photo of a herd of dairy cows on a Wisconsin pasture, illustrating the agricultural focus of the dataset."
- **Diagrams**: describe the components and their relationships. Example: "Pipeline diagram showing four sequential stages: Ingestion to Research Agent to Model Agent to Review Agent, with arrows indicating data flow."
- **Code**: summarize what the code does in plain language. Example: "Python function that takes a paper ID and returns the extracted equation as a SymPy expression."

### Materials Independence

The presentation file should be self-explanatory enough that someone who cannot attend the live event can still understand it from the speaker notes. This is why descriptive presenter notes are a generation requirement, not optional.

When sharing materials in advance (recommended for accessibility), the recipient relies entirely on what's in the slide plus the notes.

### Reference

- **UW-Madison Digital Accessibility Policy**: UW-519
- **Center for User Experience** - Free accessibility evaluation and consultation: centerforux@wisc.edu
- **Delivery guidance**: see `references/delivery-guide.md` for accessible presentation delivery practices (microphone, pacing, describing visuals aloud, Q&A practices)
