# Accessibility Requirements

All UW-Madison digital materials must meet **WCAG 2.1 AA** standards. This is required by UW-Madison Digital Accessibility Policy **UW-519** and applies to web pages, presentations, documents, and any other digital output.

Reference: [UW-Madison Digital Accessibility](https://accessible.wisc.edu/) | [Center for User Experience](mailto:centerforux@wisc.edu) (free evaluation and consultation)

---

## Color Contrast

- Minimum **4.5:1** contrast ratio for normal text (under 18pt or under 14pt bold)
- Minimum **3:1** for large text (18pt+ or 14pt+ bold)
- Minimum **3:1** for UI components and graphical objects (borders, icons, form controls)
- See the precomputed contrast ratio table in `tokens.md` (under Colors > Contrast Ratios) for UW brand color pairings
- Test any custom color combinations before using them
- Never place red text on dark backgrounds (fails contrast)
- Never place light gray text on white backgrounds (fails contrast)
- Never rely on color alone to convey meaning (add text labels, patterns, or icons)

## Typography

- No text smaller than 16px for body content on the web; 14px absolute minimum for any text
- No all-capital-letter headings or body text
- Line height minimum 1.5 for body text, 1.2 for headings
- Paragraph spacing at least 1.5x the font size
- Letter spacing at least 0.12em for body text is recommended
- Sufficient spacing between list items for readability

## Semantic HTML

### Headings

- Use one `<h1>` per page (the page title)
- Maintain proper heading hierarchy: `<h1>` then `<h2>` then `<h3>`, never skip levels
- Headings should describe the content that follows

### Content elements

- Use `<p>` for paragraphs, not `<div>` or `<br>` chains
- Use `<ul>` / `<ol>` for lists (not styled `<p>` or `<div>` tags)
- Use `<blockquote>` with `<cite>` for quotations
- Use `<table>` with `<thead>`, `<th scope="col">`, and `<th scope="row">` for data tables
- Use `<code>` and `<pre>` for code blocks
- Use `<em>` and `<strong>` for emphasis (not `<i>` and `<b>` unless purely stylistic)
- Use `<time datetime="...">` for dates

### Page structure

- Use `<header>`, `<nav>`, `<main>`, `<aside>`, `<footer>` landmark elements
- Use `<section>` with headings for distinct content regions
- Use `<article>` for self-contained content (blog posts, cards, news items)

## Navigation and Links

- Every page must have a **skip to main content** link as the first focusable element
- Link text must be descriptive: "Read the accessibility policy" not "click here"
- Links that open in a new window must indicate this (e.g., with text or an icon with `aria-label`)
- Navigation menus must be inside `<nav>` elements with descriptive `aria-label` attributes
- Breadcrumbs use `<nav aria-label="Breadcrumbs">` with an `<ol>` list
- The current page in navigation should be marked with `aria-current="page"`
- Pagination and multi-step flows must indicate current position

## Keyboard Navigation

- All interactive elements must be reachable and operable via keyboard alone
- Tab order must follow the visual reading order
- Focus must be visible on all interactive elements (never `outline: none` without a replacement)
- No keyboard traps: the user must be able to Tab away from any component
- Custom interactive components need appropriate keyboard handlers (Enter, Space, Escape, Arrow keys as applicable)
- Modal dialogs must trap focus while open and return focus to the trigger on close

## Focus Management

- Focus indicators must have at least **3:1** contrast against adjacent colors
- When content updates dynamically (modals, tab panels, accordions), move focus to the new content
- After closing a dialog or popover, return focus to the element that opened it
- Never use `tabindex` values greater than 0

## Images and Media

### Images

- Every `<img>` must have an `alt` attribute
- Informative images: `alt` describes what the image conveys in context
- Decorative images: use `alt=""` and `aria-hidden="true"`
- Complex images (charts, diagrams): provide a longer description via `aria-describedby` or adjacent text
- SVG logos and brand marks used as decoration: `aria-hidden="true"`

### Video and audio

- Pre-recorded video must have synchronized captions
- Pre-recorded audio must have a transcript
- Live video should have live captions when feasible
- Video players must be keyboard-operable
- No media auto-plays with sound

## Forms and Inputs

- Every input must have a visible `<label>` element associated via `for`/`id`
- Group related inputs with `<fieldset>` and `<legend>`
- Required fields must be indicated (not by color alone)
- Error messages must be associated with their input via `aria-describedby` or `aria-errormessage`
- Error messages must describe the problem and how to fix it
- Use `autocomplete` attributes for common fields (name, email, address, etc.)
- Custom controls (toggles, date pickers, comboboxes) must follow [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)

## ARIA

Use ARIA only when native HTML semantics are insufficient. Prefer semantic HTML first.

### Common patterns

```html
<!-- Landmark with label -->
<nav aria-label="Main Menu">

<!-- Live region for dynamic updates -->
<div role="status" aria-live="polite">3 results found</div>

<!-- Expandable section -->
<button aria-expanded="false" aria-controls="panel-1">Section title</button>
<div id="panel-1" hidden>...</div>

<!-- Tab interface -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="tab-panel-1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="tab-panel-2">Tab 2</button>
</div>
<div role="tabpanel" id="tab-panel-1">...</div>

<!-- Modal dialog -->
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm action</h2>
</div>

<!-- Loading state -->
<button aria-busy="true" aria-disabled="true">Saving...</button>
```

### Rules

- Never use ARIA roles that contradict the native element semantics
- If you use `role`, ensure all required ARIA properties are set
- `aria-label` and `aria-labelledby` override visible text for screen readers; use carefully
- `aria-hidden="true"` removes elements from the accessibility tree entirely; never hide focusable elements this way

## Motion and Animation

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- All animations must respect `prefers-reduced-motion`
- No auto-playing animations or infinite loops
- Transitions should be subtle (max 0.8s duration)
- Never use animations that flash or strobe (three flashes per second threshold)
- Parallax and motion effects must have a reduced-motion alternative

## Responsive Design

- Content must be readable at 200% zoom without horizontal scrolling
- Touch targets must be at least 44x44 CSS pixels
- Content must reflow into a single column at 320px width
- Do not disable pinch-to-zoom (`user-scalable=no` or `maximum-scale=1`)

## Print Accessibility

- Print styles should remove navigation UI, backgrounds, and non-essential visuals
- Ensure text is dark on a light background for readability
- Expand abbreviated URLs so printed links are usable
- Add page breaks at logical content boundaries

## Content Accessibility (UW IT Guidelines)

These content requirements apply to all digital materials, not just code.

### Plain language and acronyms

- **Spell out acronyms on first use**: write the full term followed by the abbreviation in parentheses, e.g., "Retrieval-Augmented Generation (RAG)"
- After first use, the acronym alone is fine
- Avoid jargon when a plain term works
- Define domain-specific terms in context when the audience may not know them
- Write at a reading level appropriate for the audience

### Document structure

- Use headings to organize content, not for visual styling
- Keep paragraphs short and focused on one idea
- Use lists for sets of related items
- Front-load important information (inverted pyramid)

### Materials independence

- Digital materials should be self-explanatory enough that someone who cannot attend a live event can still understand them
- When sharing materials in advance (recommended), the recipient relies entirely on the document itself

---

## Presentation-Specific Requirements

These apply when generating slide presentations (in addition to all requirements above).

### Slide structure

- `<h1>` for the title slide only, `<h2>` for slide headings, `<h3>` for sub-headings
- Use `<section>` for each slide
- Mark the current slide with `aria-current="step"`

### ARIA for presentations

```html
<!-- Presentation container -->
<main class="presentation" role="main" aria-label="Slide presentation">

<!-- Progress bar -->
<div class="progress-bar" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">

<!-- Navigation dots -->
<nav class="nav-dots" aria-label="Slide navigation">
  <button class="nav-dot" aria-label="Go to slide 1" aria-current="step">
  <button class="nav-dot" aria-label="Go to slide 2">

<!-- Hidden elements -->
<div class="keyboard-hint" aria-hidden="true">
<div class="presenter-notes" aria-hidden="true">
```

### Keyboard navigation (slides)

- **Arrow keys** (Up/Down, Left/Right): Navigate between slides
- **Space / PageDown**: Next slide
- **PageUp**: Previous slide
- **Home**: First slide
- **End**: Last slide
- **Escape**: Return to first slide
- **N**: Toggle presenter notes

### Presenter notes describe visuals

Every slide with a chart, diagram, image, code block, or non-trivial visual layout MUST have a `data-notes` attribute describing the visual content so someone can understand the slide without seeing it:

- **Charts**: describe the trend, key values, and the takeaway
- **Images**: describe what is depicted and why it matters
- **Diagrams**: describe the components and their relationships
- **Code**: summarize what the code does in plain language

### Print (slides)

- Remove navigation UI (dots, progress bar, keyboard hint)
- Make all animated content visible (`opacity: 1`, `transform: none`)
- Add page breaks between slides
- Ensure text is black on white for printing

---

## UW-Madison Resources

- **Digital Accessibility Policy**: [UW-519](https://policy.wisc.edu/library/UW-519)
- **Center for User Experience**: Free accessibility evaluation and consultation, centerforux@wisc.edu
- **McBurney Disability Resource Center**: Student accommodation services
- **Cultural Linguistics Services**: Translation and interpretation
- **UW IT Accessibility Guide**: [it.wisc.edu/learn/make-it-accessible](https://it.wisc.edu/learn/make-it-accessible/)
