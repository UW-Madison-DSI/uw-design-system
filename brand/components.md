# Component Catalog

UI components from the UW Style CSS framework (v5.3.0). Each component includes its class names, HTML structure, key styles, and accessibility requirements.

All token references use the canonical names from `tokens.md`. For the UW Style CSS variable names, see the mapping table in `tokens.md` under "UW Style CSS Mapping."

---

## Buttons

### Base: `.uw-button`

```html
<button class="uw-button">Label</button>
<a href="..." class="uw-button">Label</a>
```

| Property | Value |
|----------|-------|
| Font | `--uw-font-button` (Red Hat Text), weight 500, 1.0625rem |
| Padding | `--uw-space-sm` vertical, `--uw-space-md` horizontal |
| Background | `#036796` (`--uw-link-blue`) |
| Text color | `--uw-white` |
| Border | 2px solid `#036796` |
| Border radius | `--uw-radius-md` (0.5rem) |
| Shadow | `--uw-shadow-md` |
| Transition | all 0.25s ease-out |

**Hover/Focus:** background darkens to `#023d54`, border matches.

### Variants

| Class | Background | Text | Border | Use case |
|-------|-----------|------|--------|----------|
| `.uw-button` | `#036796` | white | `#036796` | Primary action |
| `.uw-button.uw-button-red` | `--uw-red` | white | `--uw-red` | Brand-emphasized action |
| `.uw-button.uw-button-reverse` | white | `#036796` | `#036796` | Secondary action |
| `.uw-button.uw-button-red-reverse` | white | `--uw-red` | `--uw-red` | Secondary brand action |
| `.uw-button.uw-button-transparent` | `rgba(0,0,0,0.5)` | white | white | Over images/dark backgrounds |
| `.uw-button.uw-button-expanded` | (inherits) | (inherits) | (inherits) | Full-width (display: block) |
| `.uw-button-cta` | (inherits) | (inherits) | (inherits) | Uppercase text transform |

All reverse variants swap foreground/background on hover.

**Accessibility:** Use `<button>` for actions, `<a class="uw-button">` for navigation. Never use `<div>` or `<span>` as buttons.

---

## Cards

### Base: `.uw-card`

```html
<div class="uw-card">
  <div class="uw-card-content">
    <img src="..." alt="Descriptive text">
    <div class="uw-card-copy">
      <h2>Card Title</h2>
      <p>Card description.</p>
    </div>
  </div>
</div>
```

| Property | Value |
|----------|-------|
| Layout | flex, responsive width (100% mobile, 33.333% at 500px+) |
| Padding | `clamp(1rem, 2.75vw, 1.55rem)` |
| Content background | `--uw-white` |
| Heading size | 1.375rem, weight 650 |
| Copy padding | 0 1rem 1rem |
| Line height (text) | 1.6 |

Cards use the flex parent to create responsive grid layouts. Wrap multiple `.uw-card` elements in a flex container.

**Accessibility:** Every card image needs descriptive `alt` text. Card headings should form a logical hierarchy with the page.

---

## Tables

### Base: `<table>`

```html
<table>
  <thead>
    <tr>
      <th scope="col">Column Header</th>
      <th scope="col">Column Header</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row"><a href="">Row Header</a></th>
      <td>Data</td>
    </tr>
  </tbody>
</table>
```

| Property | Value |
|----------|-------|
| Width | 100% |
| Border | 1px solid `#cfcfcf`, collapse: separate, spacing: 0 |
| Header background | `--uw-gray-lightest` (#f3f3f3) |
| Striped rows | even rows get `--uw-gray-lightest` background |
| Cell padding | `clamp(1rem, 2.75vw, 1.55rem)` |
| Font size | `--uw-text-base` (1.125rem) |
| Header weight | 700 |
| Link style | underline, thickness 0.05em, offset 0.125rem |

**Accessibility:** Use `scope="col"` on column headers, `scope="row"` on row headers. For complex tables, use `id`/`headers` attributes.

---

## Forms

### Structure

```html
<form>
  <fieldset>
    <legend>Group Label</legend>
    <div class="uw-input-row">
      <label for="field-id">Label:</label>
      <input type="text" id="field-id">
    </div>
  </fieldset>
  <input type="submit" value="Submit">
</form>
```

### Input Fields

Applies to: `input[type=text|email|password|search|number|tel|url|date|...]`, `select`, `textarea`.

| Property | Value |
|----------|-------|
| Padding | 0.5rem |
| Background | `--uw-white` |
| Border | 1px solid `#cfcfcf` |
| Border radius | `--uw-radius-sm` (4px) |
| Font | `--uw-font-body` (Red Hat Text) |
| Height | 2.5rem (text inputs and selects) |

### Fieldset

| Property | Value |
|----------|-------|
| Padding | 10px 25px |
| Border | 1px solid `#cfcfcf` |
| Border radius | `--uw-radius-sm` (4px) |
| Legend weight | 625 |

### States

- **Label:** `display: block`, weight 625 (400 inside fieldsets)
- **Disabled:** `cursor: not-allowed`
- **Focus:** default browser outline (no custom focus ring in framework)
- **Submit/Reset:** styled identically to `.uw-button`

**Accessibility:** Every input needs a `<label>` with matching `for`/`id`. Group related inputs in `<fieldset>` with `<legend>`. Use `aria-required="true"` for required fields. Use `aria-describedby` to link inputs to error messages.

---

## Header

### Structure

```html
<div class="uw-global-bar" role="navigation">
  <a class="uw-global-name-link" href="https://www.wisc.edu">
    University of Wisconsin-Madison
  </a>
</div>

<header id="branding" class="uw-header">
  <div class="uw-header-container">
    <div class="uw-header-crest">
      <a href="/"><img class="uw-crest-svg" src="uw-crest.svg" alt="UW-Madison home"></a>
    </div>
    <div class="uw-title-tagline">
      <div class="uw-site-title"><a href="/">Site Name</a></div>
      <div class="uw-site-tagline">Optional tagline</div>
    </div>
  </div>
</header>
```

### Global Bar

| Property | Value |
|----------|-------|
| Background | `--uw-red` (#c5050c) |
| Text color | `--uw-white` |
| Padding | 0.5rem horizontal-responsive |
| Font | `--uw-font-body`, 0.8125rem, weight 500, uppercase |

**Inverse variant:** `.uw-global-bar-inverse` flips to white background with `--uw-gray-dark` text and a bottom border.

### Header Bar

| Property | Value |
|----------|-------|
| Background | `--uw-white` |
| Padding | 1rem horizontal-responsive |
| Layout | flex, space-between, center-aligned |
| Max width | 75rem (at 640px+) |
| Crest width | 2.5rem |
| Site title | `--uw-font-heading`, `--uw-text-2xl`, weight 700, color `--uw-red` |
| Tagline | `--uw-font-heading`, 0.9375rem, weight 500, color `--uw-black` |

**Accessibility:** The global bar should have `role="navigation"`. The crest image needs alt text linking to the home page.

---

## Footer

### Structure

```html
<footer id="colophon" class="uw-footer">
  <div class="uw-footer-content">
    <div class="uw-logo">
      <a href="https://www.wisc.edu">
        <svg><use href="uw-icons.svg#uw-icon-crest-footer"></use></svg>
      </a>
    </div>
    <div class="uw-footer-menu">
      <h3 class="uw-footer-header">Section</h3>
      <ul><li><a href="">Link</a></li></ul>
    </div>
    <div class="uw-social-icons">
      <a href="" class="uw-social-icon" aria-label="Facebook">
        <svg>...</svg>
      </a>
    </div>
  </div>
  <div class="uw-copyright">
    <p>&copy; Board of Regents of the University of Wisconsin System</p>
  </div>
</footer>
```

| Property | Value |
|----------|-------|
| Background | `--uw-gray-dark` (#282728) |
| Text color | `#adadad` |
| Link color | `#adadad`, hover: `--uw-gray-lightest` with underline |
| Layout | flex-wrap, responsive columns (1 on mobile, 3 at 640px, 4 at 972px) |
| Max width | 1200px centered |
| Header font | `--uw-font-heading`, weight 700, 0.9rem (1.25rem at 972px+) |
| Logo SVG | 200px wide, fill `#adadad`, hover fill `--uw-gray-lightest` |
| Social icons | `#adadad` background, `--uw-radius-lg` border-radius, hover `--uw-gray-lightest` |

**Accessibility:** Social icon links need `aria-label` with the platform name. Footer should use `<footer>` landmark element.

---

## Navigation

### Breadcrumbs

```html
<nav class="uw-breadcrumbs" aria-label="Breadcrumbs">
  <ol>
    <li><a href="/"><span>Home</span></a></li>
    <li><a href="/section"><span>Section</span></a></li>
    <li><a href="" aria-current="page"><span>Current Page</span></a></li>
  </ol>
</nav>
```

| Property | Value |
|----------|-------|
| Font | `--uw-font-heading`, 0.875rem, weight 500 |
| Separator | 1px `#585758` line, skewed 20 degrees |
| Current page | `--uw-black` color (not a link) |
| Margin | responsive spacing |

**Accessibility:** Wrap in `<nav>` with `aria-label="Breadcrumbs"`. Mark current page with `aria-current="page"`.

### Pagination

```html
<nav class="uw-pagination" aria-label="Pagination">
  <ul class="uw-pagination-menu">
    <li><a href="">Previous</a></li>
    <li><a href="">1</a></li>
    <li><a href="" aria-current="page">2</a></li>
    <li><a href="">Next</a></li>
  </ul>
</nav>
```

| Property | Value |
|----------|-------|
| Background | `--uw-gray-lightest` |
| Link padding | 0.75rem 1rem |
| Border | 1px solid `rgb(217, 217, 217)` between items |
| Font size | 0.875rem |
| Hover | background `#036796`, color white |
| Disabled | `pointer-events: none`, color `#717171` |

**Accessibility:** Use `aria-current="page"` on the active page. Use `aria-disabled="true"` on disabled links.

### Mobile Menu

```html
<button class="uw-mobile-menu-button-bar">
  <span>Menu</span>
  <svg>...</svg>
</button>
```

| Property | Value |
|----------|-------|
| Background | `--uw-red` |
| Color | white |
| Font | 1rem, weight 450, uppercase |
| Hidden by default | `display: none`, shown via `.uw-is-visible` |

**Inverse variant:** `.uw-mobile-menu-button-bar-reversed` uses white background with dark text.

---

## Utility Classes

### Accessibility

| Class | Purpose |
|-------|---------|
| `.uw-sr-only` | Visually hidden, available to screen readers |
| `.uw-show-for-sr-only` | Same as above (alias) |
| `.uw-show-on-focus` | Hidden until focused (skip links) |

### Layout

| Class | Effect |
|-------|--------|
| `.uw-flex` | `display: flex` |
| `.uw-flex-reverse` | `flex-direction: row-reverse` |
| `.uw-gap` | `gap: 1rem` |
| `.uw-clearfix` | Clear floats |
| `.uw-row` | Flex container, max-width 75rem, centered |
| `.uw-row-narrow` | Same, max-width 50rem |
| `.uw-body` | Main content column (66.67% at 640px+) |
| `.uw-sidebar` | Sidebar column (33.33% at 640px+) |

### Spacing

Padding (`.uw-pad-{side}-{size}`) and margin (`.uw-mg-{side}-{size}`) utility classes.

**Sides:** (none) = all, `t` = top, `b` = bottom, `l` = left, `r` = right, `tb` = top + bottom

**Sizes:** `xs` (0.25rem), `s` (0.5rem), `m` (1rem), `l` (2rem), `xl` (4rem), `xxl` (8rem)

Larger sizes (`l`, `xl`, `xxl`) are halved below 640px for mobile.

### Text

| Class | Effect |
|-------|--------|
| `.uw-text-center` | Center-aligned text |
| `.uw-text-left` | Left-aligned text |
| `.uw-text-right` | Right-aligned text |
| `.uw-nowrap` | Prevent line wrapping |
| `.uw-double-size-text` | Larger body text (1.25rem, 1.375rem at 640px+) |
| `.uw-small-text` | 0.9rem |
| `.uw-smaller-text` | 0.8rem |
| `.uw-no-case-transform` | Remove text-transform |

### Background Colors

| Class | Color |
|-------|-------|
| `.uw-white-bg` | `--uw-white` |
| `.uw-light-gray-bg` | `--uw-gray-lightest` |
| `.uw-red-bg` | `--uw-red` (sets text to white) |

### Decorative

| Class | Effect |
|-------|--------|
| `.uw-mini-bar` | Red bar above element (signature UW accent) |
| `.uw-mini-bar-white` | White bar variant (for dark backgrounds) |
| `.uw-mini-bar-center` | Centered red bar |
| `.uw-mini-bar-white-center` | Centered white bar |
| `.uw-more-link` | Uppercase link with red caret icon |
