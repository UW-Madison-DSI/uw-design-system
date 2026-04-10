# Slide Types

Ten slide types for UW-Madison presentations. Each defines its HTML structure, CSS classes, content density limits, and recommended animation.

---

## 1. `title-slide`

The opening slide. Sets the tone, identifies the presentation, and establishes brand presence.

### HTML Structure
```html
<section class="slide slide--title" data-notes="">
  <div class="slide__logo">
    <!-- Inline W Crest SVG (full-color or 1-color depending on preset) -->
  </div>
  <div class="slide-content animate-in">
    <h1 class="slide-title uw-mini-bar">Presentation Title</h1>
    <p class="slide-subtitle">Subtitle or description line</p>
    <div class="slide-meta">
      <p class="slide-author">Author Name</p>
      <p class="slide-date">Department or Affiliation | Date</p>
    </div>
  </div>
</section>
```

### Content Limits
- Title: max 8 words
- Subtitle: max 15 words
- Author + affiliation: 1-2 lines
- Date: 1 line

### CSS
```css
.slide--title .slide-content {
  justify-content: center;
  align-items: flex-start;
}
.slide-meta {
  margin-top: clamp(1.5rem, 3vw, 3rem);
}
.slide-author {
  font-family: var(--uw-heading-font);
  font-weight: 600;
  font-size: var(--uw-body-size);
}
.slide-date {
  font-size: var(--uw-caption-size);
  color: var(--uw-text-secondary);
}
```

### Animation
`animate-in` on `.slide-content` (fade + slide up)

---

## 2. `section-divider`

A visual break between major sections. Bold, simple, high-impact.

### HTML Structure
```html
<section class="slide slide--divider" data-notes="">
  <div class="slide-content animate-fade">
    <h2 class="slide-heading uw-mini-bar-white">Section Title</h2>
    <p class="slide-subtitle">Optional brief description</p>
  </div>
</section>
```

### Content Limits
- Heading: max 5 words
- Subtitle: max 10 words (optional)

### CSS
```css
.slide--divider {
  background-color: var(--uw-accent, #c5050c);
  color: #ffffff;
}
.slide--divider .slide-content {
  justify-content: center;
  align-items: flex-start;
}
.slide--divider .slide-heading {
  font-size: var(--uw-title-size);
  color: #ffffff;
}
.slide--divider .slide-subtitle {
  color: rgba(255, 255, 255, 0.85);
}
```

### Animation
`animate-fade` (simple fade in, no movement)

---

## 3. `content`

The workhorse slide. Heading plus bullet points, short paragraphs, or a brief explanation.

### HTML Structure (bullets)
```html
<section class="slide slide--content" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">Slide Heading</h2>
    <ul class="stagger">
      <li>First point, kept concise</li>
      <li>Second point with key detail</li>
      <li>Third point</li>
      <li>Fourth point</li>
      <li>Fifth point (maximum)</li>
    </ul>
  </div>
</section>
```

### HTML Structure (paragraphs)
```html
<section class="slide slide--content" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">Slide Heading</h2>
    <div class="stagger">
      <p>First paragraph, two to three sentences maximum.</p>
      <p>Second paragraph if needed. Keep it brief.</p>
    </div>
  </div>
</section>
```

### Content Limits
- Heading: 1 line
- Bullets: max 5 items, each max 12 words
- Paragraphs: max 2, each max 3 sentences
- If content exceeds limits, SPLIT into multiple slides

### Animation
`animate-in` on heading, `stagger` on the list/paragraphs

---

## 4. `two-column`

Side-by-side layout for comparisons, text+image, or parallel points.

### HTML Structure
```html
<section class="slide slide--two-column" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">Comparison Heading</h2>
    <div class="two-column stagger">
      <div class="column">
        <h3>Column A Title</h3>
        <ul>
          <li>Point one</li>
          <li>Point two</li>
          <li>Point three</li>
        </ul>
      </div>
      <div class="column">
        <h3>Column B Title</h3>
        <ul>
          <li>Point one</li>
          <li>Point two</li>
          <li>Point three</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

### Content Limits
- Heading: 1 line
- Per column: max 4 items or 1 short paragraph
- Column titles: max 3 words each
- Use `two-column-60-40` or `two-column-40-60` for text+image layouts

### Animation
`animate-in` on heading, `stagger` on the two-column container

---

## 5. `data-chart`

For bar charts, simple line representations, or styled tables. Uses CSS/SVG for charts (no external libraries).

### HTML Structure (bar chart)
```html
<section class="slide slide--data" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">Chart Title</h2>
    <div class="chart-container animate-scale">
      <div class="bar" style="height: 80%; background: var(--uw-chart-1);">
        <span class="bar-value">80%</span>
        <span class="bar-label">Label A</span>
      </div>
      <div class="bar" style="height: 60%; background: var(--uw-chart-2);">
        <span class="bar-value">60%</span>
        <span class="bar-label">Label B</span>
      </div>
      <!-- max 6 bars -->
    </div>
    <p class="caption animate-in">Source: Data source attribution</p>
  </div>
</section>
```

### HTML Structure (table)
```html
<section class="slide slide--data" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">Table Title</h2>
    <div class="animate-in">
      <table>
        <thead>
          <tr>
            <th>Category</th>
            <th>Value A</th>
            <th>Value B</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>Row 1</td><td>123</td><td>456</td></tr>
          <!-- max 6 rows -->
        </tbody>
      </table>
    </div>
    <p class="caption animate-in">Source attribution</p>
  </div>
</section>
```

### Content Limits
- Heading: 1 line
- Bar chart: max 6 bars
- Table: max 4 columns, max 6 rows
- Caption/source: 1 line
- Annotations: max 2 lines below chart

### Chart Colors
Use the preset's chart palette: `--uw-chart-1` through `--uw-chart-6`. Default: Red, Blue, Gray-Blue, Yellow, Dark Red, Charcoal.

### Animation
`animate-in` on heading, `animate-scale` on chart container

---

## 6. `quote`

A pull quote with attribution. Uses decorative oversized quotation mark.

### HTML Structure
```html
<section class="slide slide--quote" data-notes="">
  <div class="slide-content animate-in">
    <blockquote>
      The quote text goes here. Keep it to three lines maximum for readability.
      <cite>Speaker Name, Title or Context</cite>
    </blockquote>
  </div>
</section>
```

### Content Limits
- Quote: max 3 lines (roughly 30 words)
- Attribution: 1 line (name + title/context)
- No heading above the quote (the quote IS the content)

### CSS
The `blockquote::before` pseudo-element provides the oversized red quotation mark. See `viewport-base.css`.

### Animation
`animate-in` on `.slide-content`

---

## 7. `image-feature`

A slide dominated by an image, with optional text overlay or side panel.

### HTML Structure (image with text overlay)
```html
<section class="slide slide--image" style="background-image: url('IMAGE_URL'); background-size: cover; background-position: center;" data-notes="">
  <div class="image-overlay"></div>
  <div class="slide-content animate-in" style="position: relative; z-index: 2;">
    <h2 class="slide-heading">Heading Over Image</h2>
    <p>Brief description or caption</p>
  </div>
</section>
```

### HTML Structure (image beside text)
```html
<section class="slide slide--image-split" data-notes="">
  <div class="slide-content">
    <div class="two-column-40-60">
      <div class="column stagger">
        <h2 class="slide-heading uw-mini-bar">Heading</h2>
        <p>Description text alongside the image.</p>
      </div>
      <div class="column animate-fade">
        <img src="IMAGE_URL" alt="Descriptive alt text">
      </div>
    </div>
  </div>
</section>
```

### Content Limits
- Heading: max 6 words
- Description: max 2 sentences
- Image: 1 per slide
- Always include descriptive alt text

### CSS
```css
.slide--image {
  padding: 0;
}
.image-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7));
  z-index: 1;
}
.slide--image .slide-content {
  color: #ffffff;
  padding: var(--uw-slide-padding);
  justify-content: flex-end;
}
.slide--image .slide-heading {
  color: #ffffff;
}
```

For the `recruitment` preset, use a red gradient overlay instead:
```css
.image-overlay {
  background: linear-gradient(to bottom, rgba(197,5,12,0.7), rgba(155,0,0,0.85));
}
```

### Animation
`animate-in` or `animate-fade`

---

## 8. `code`

A slide showing code with syntax highlighting on a dark background.

### HTML Structure
```html
<section class="slide slide--code" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">Code Example Title</h2>
    <pre class="animate-in"><code>def hello_world():
    """A simple example."""
    print("On, Wisconsin!")
    return True</code></pre>
  </div>
</section>
```

### Content Limits
- Heading: 1 line
- Code: max 15 lines
- No additional text below (if explanation needed, put on a separate content slide)

### Syntax Highlighting
Use inline `<span>` elements with color classes for basic highlighting:
```css
.token-keyword { color: #c5050c; }     /* Red for keywords */
.token-string { color: #FFB500; }      /* Yellow for strings */
.token-comment { color: #6B8F99; }     /* Gray-blue for comments */
.token-function { color: #e0e0e0; }    /* Light for function names */
.token-number { color: #9B0000; }      /* Dark red for numbers */
```

### Animation
`animate-in` on heading and `<pre>` block

---

## 9. `references`

For citations, bibliography, and source attribution. Smaller text, efficient layout.

### HTML Structure
```html
<section class="slide slide--references" data-notes="">
  <div class="slide-content">
    <h2 class="slide-heading uw-mini-bar animate-in">References</h2>
    <div class="references-list stagger">
      <ol>
        <li>Author, A. (2024). Title of work. <em>Journal Name</em>, 12(3), 45-67.</li>
        <li>Author, B., & Author, C. (2023). Another title. Publisher.</li>
        <!-- Continue as needed -->
      </ol>
    </div>
  </div>
</section>
```

### Content Limits
- Up to 8 references per slide (split across multiple slides if more)
- For long lists, use a two-column layout:
```html
<div class="references-list two-column">
  <ol><!-- first half --></ol>
  <ol start="5"><!-- second half --></ol>
</div>
```

### CSS
```css
.slide--references .references-list {
  font-size: var(--uw-caption-size);
  line-height: 1.6;
}
.slide--references ol {
  list-style: decimal;
  padding-left: 2em;
}
.slide--references li {
  font-size: var(--uw-caption-size);
  margin-bottom: 0.5em;
}
```

### Animation
`stagger` on the references list

---

## 10. `closing`

The final slide. Thank you, questions, or contact information. Re-establishes brand with the logo.

### HTML Structure
```html
<section class="slide slide--closing" data-notes="">
  <div class="slide__logo">
    <!-- Inline W Crest SVG -->
  </div>
  <div class="slide-content animate-in">
    <h2 class="slide-title uw-mini-bar-center">Thank You</h2>
    <div class="closing-contact">
      <p class="slide-author">Author Name</p>
      <p>email@wisc.edu</p>
      <p>Department of Example Studies</p>
      <p>University of Wisconsin-Madison</p>
    </div>
  </div>
</section>
```

### Content Limits
- Main text: "Thank You", "Questions?", or similar (max 3 words)
- Contact info: 3-5 lines
- Optional: QR code placeholder area

### CSS
```css
.slide--closing .slide-content {
  justify-content: center;
  align-items: center;
  text-align: center;
}
.closing-contact {
  margin-top: clamp(1.5rem, 3vw, 3rem);
  font-size: var(--uw-body-size);
}
.closing-contact p {
  margin-bottom: 0.25em;
}
```

### Animation
`animate-in` on `.slide-content`

---

## General Rules for All Slide Types

1. **Every slide must fit in 100vh without scrolling.** If content overflows, split it.
2. **Minimum font size**: No text smaller than `clamp(0.875rem, 1.2vw, 1rem)` (approximately 14px minimum, 16px typical).
3. **Alt text**: Every `<img>` must have descriptive `alt` text.
4. **Heading hierarchy**: Title slides use `<h1>`, all other slides use `<h2>` for their main heading, `<h3>` for sub-headings.
5. **No all-caps**: Use title case or sentence case for headings (per accessibility and StratComm guidelines).
6. **Presenter notes**: Add `data-notes="..."` to any `<section class="slide">` for speaker notes (toggled with N key).
7. **Semantic HTML**: Use `<section>`, `<h2>`, `<ul>`, `<blockquote>`, `<table>`, `<cite>` appropriately.

---

## Decorative Brand Elements

Brand assets from `assets/brand/` can be embedded to add visual personality. See `references/asset-registry.md` for the full catalog. All decorative images use `aria-hidden="true"` and `alt=""`.

### Embedding Method

Read the asset file and embed as a base64 data URI:
```html
<img src="data:image/png;base64,{BASE64_DATA}" class="decorative" aria-hidden="true" alt="">
```

For SVG icons, embed as inline `<svg>` markup (read the file, paste the SVG content).

### CSS for Decorative Elements

```css
/* Base decorative positioning */
.decorative {
  position: absolute;
  pointer-events: none;
  z-index: 0;
}
.slide-content { position: relative; z-index: 1; }

/* Watermark (e.g., hand-drawn W or campus illustration) */
.decorative--watermark {
  position: absolute;
  bottom: 5%;
  right: 5%;
  width: clamp(120px, 20vw, 250px);
  opacity: 0.07;
}

/* Corner accent (e.g., wave, scribble) */
.decorative--corner-br {
  position: absolute;
  bottom: 0;
  right: 0;
  width: clamp(150px, 25vw, 350px);
  opacity: 0.12;
}
.decorative--corner-tl {
  position: absolute;
  top: 0;
  left: 0;
  width: clamp(150px, 25vw, 350px);
  opacity: 0.12;
}

/* Background texture overlay */
.decorative--texture {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.05;
  mix-blend-mode: multiply;
}

/* Inline icon next to text (in cards, list items) */
.slide-icon {
  width: 2em;
  height: 2em;
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
}
.slide-icon--large {
  width: 3em;
  height: 3em;
}

/* Icon + text card layout */
.icon-card {
  display: flex;
  align-items: flex-start;
  gap: 1em;
}
.icon-card .slide-icon {
  margin-top: 0.2em;
}

/* Campus illustration as section background */
.decorative--illustration {
  position: absolute;
  bottom: 8%;
  right: 5%;
  width: clamp(180px, 25vw, 350px);
  opacity: 0.1;
}

/* For dark/red background slides, use white element variants */
.slide--divider .decorative { opacity: 0.15; }
```

### Decoration Rules Per Slide Type

| Slide Type | Recommended Decorations |
|-----------|------------------------|
| `title-slide` | Hand-drawn W watermark (bottom-right, 7% opacity) OR campus illustration. Optional: long-wave accent at bottom edge. |
| `section-divider` | White wave or scribble element (corner, 15% opacity). Optional: texture overlay at 5%. |
| `content` | Contextual SVG icons in card layouts (icon-card class). No background decorations to keep focus on text. |
| `two-column` | Optional: small icon at the top of each column to visually label them. |
| `data-chart` | Minimal decoration. Optional: subtle texture on the chart container background. |
| `quote` | Word-bubble-scribble element behind the quote (10% opacity). Or oversized decorative quotation mark only (no extra element). |
| `image-feature` | No additional decoration (the image IS the decoration). |
| `code` | No decoration. |
| `references` | No decoration. |
| `closing` | Hand-drawn W watermark (centered, 7% opacity behind content) OR campus illustration (Bascom Hall is the default). |

### Icon Usage in Content Slides

When a content slide uses cards or a feature grid, add contextually relevant SVG icons:

```html
<div class="card-grid stagger">
  <div class="card icon-card">
    <svg class="slide-icon"><!-- inline SVG from assets/brand/icons/ --></svg>
    <div>
      <h3>Feature Title</h3>
      <p>Brief description of the feature.</p>
    </div>
  </div>
  <!-- more cards -->
</div>
```

Choose icons that match the card content. See the categorized icon list in `references/asset-registry.md`.

### Decoration Budget

To keep presentations clean and professional:
- **Max 2-3 decorative elements per slide** (not counting the logo)
- **Max 1 texture overlay per presentation** (use on one section divider, not all)
- **Max 4 unique icons per presentation** (reuse is fine)
- **Watermarks should never exceed 10% opacity** on light backgrounds, 15% on dark
- Decorations must never compete with content for attention
