# Design Tokens

Single source of truth for all UW-Madison design tokens. Every color, font, size, spacing, and animation value used across the design system is defined here.

Naming convention: `--uw-{category}-{name}` (kebab-case, `uw` prefix).

**Context suffixes:** Most tokens are universal (no suffix). When web pages and presentations need different values for the same role, the token is split with a `-web` or `-slide` suffix. Examples: `--uw-font-quote-web` vs `--uw-font-quote-slide`, `--uw-border-color-web` vs `--uw-border-color-slide`. Unsuffixed tokens apply everywhere.

---

## Colors

### Brand Palette

These are fixed values from the official UW-Madison brand guidelines. Never modify them.

```css
:root {
  /* Primary */
  --uw-red: #c5050c;              /* Badger Red (Pantone 200 C) */
  --uw-white: #ffffff;

  /* Secondary */
  --uw-red-dark: #9B0000;         /* Dark Red */
  --uw-gray-dark: #282728;        /* Dark Charcoal */
  --uw-gray-light: #e1e5e7;       /* Light Gray */
  --uw-gray-lightest: #f3f3f3;    /* Near White */
  --uw-black: #121212;            /* Rich Black (NOT pure #000) */

  /* Accent (use sparingly) */
  --uw-yellow: #FFB500;           /* Warm Yellow */
  --uw-gray-blue: #6B8F99;        /* Medium Gray Blue */
  --uw-blue: #385966;             /* Dark Blue */
  --uw-link-blue: #036796;        /* Link text on light backgrounds */

  /* Extended */
  --uw-dark-blue-black: #1a1a2e;      /* Code block backgrounds, executive preset surfaces */

  /* Derived (from crest artwork, not for general use) */
  --uw-cream: #f6ede4;            /* Crest shield gradient */
  --uw-gold: #d4ac7f;             /* Crest shield gradient */
}
```

### Contrast Ratios

Pre-tested combinations against WCAG 2.1 AA (4.5:1 for normal text, 3:1 for large text).

| Text | Background | Ratio | AA normal | AA large |
|------|-----------|-------|-----------|----------|
| `--uw-black` #121212 | `--uw-white` #ffffff | 17.4:1 | Pass | Pass |
| `--uw-black` #121212 | `--uw-gray-lightest` #f3f3f3 | 14.8:1 | Pass | Pass |
| `--uw-black` #121212 | `--uw-gray-light` #e1e5e7 | 12.1:1 | Pass | Pass |
| `--uw-red` #c5050c | `--uw-white` #ffffff | 5.9:1 | Pass | Pass |
| `--uw-red-dark` #9B0000 | `--uw-white` #ffffff | 8.0:1 | Pass | Pass |
| `--uw-white` #ffffff | `--uw-red` #c5050c | 5.9:1 | Pass | Pass |
| `--uw-white` #ffffff | `--uw-red-dark` #9B0000 | 8.0:1 | Pass | Pass |
| `--uw-white` #ffffff | `--uw-black` #121212 | 17.4:1 | Pass | Pass |
| `--uw-white` #ffffff | `--uw-gray-dark` #282728 | 14.3:1 | Pass | Pass |
| `--uw-yellow` #FFB500 | `--uw-black` #121212 | 9.6:1 | Pass | Pass |
| `--uw-black` #121212 | `--uw-yellow` #FFB500 | 9.6:1 | Pass | Pass |
| `--uw-link-blue` #036796 | `--uw-white` #ffffff | 5.5:1 | Pass | Pass |
| `--uw-link-blue` #036796 | `--uw-gray-lightest` #f3f3f3 | 4.7:1 | Pass | Pass |
| `--uw-red` #c5050c | `--uw-black` #121212 | 2.9:1 | **Fail** | **Fail** |
| `--uw-red` #c5050c | `--uw-gray-light` #e1e5e7 | 2.1:1 | **Fail** | **Fail** |
| `--uw-gray-blue` #6B8F99 | `--uw-white` #ffffff | 3.4:1 | **Fail** | Pass |

### Chart Palette

Six sequential colors for data visualizations. Use in order; all pass AA contrast on white backgrounds except where noted.

```css
:root {
  --uw-chart-1: #c5050c;          /* Badger Red */
  --uw-chart-2: #385966;          /* Blue */
  --uw-chart-3: #6B8F99;          /* Gray Blue (large text/fills only on white) */
  --uw-chart-4: #FFB500;          /* Yellow (large text/fills only on white) */
  --uw-chart-5: #9B0000;          /* Dark Red */
  --uw-chart-6: #282728;          /* Dark Charcoal */
}
```

---

## Typography

### Font Families

```css
:root {
  --uw-font-heading: 'Red Hat Display', Arial, sans-serif;
  --uw-font-body: 'Red Hat Text', Arial, sans-serif;
  --uw-font-quote-web: 'Red Hat Text', Arial, sans-serif;
  --uw-font-quote-slide: 'Red Hat Display', Arial, sans-serif;
  --uw-font-code: 'SFMono-Regular', 'Consolas', 'Liberation Mono', 'Menlo', monospace;
  --uw-font-button: 'Red Hat Text', Arial, sans-serif;
  --uw-font-caption: 'Red Hat Text', Arial, sans-serif;
}
```

**Red Hat Display** (geometric sans-serif): Headings, headlines, large sizes. Weights: 400, 500, 600, 700.
**Red Hat Text** (sans-serif): Body, UI, small sizes. Optimized for legibility. Weights: 400, 400i, 700.
**Arial**: Official fallback. Used when brand fonts are unavailable.

### Font Loading

Primary (UW CDN, has both families pre-configured):
```html
<link rel="stylesheet" href="https://cdn.wisc.cloud/fonts/uw-rh/0.0.1/fonts.css">
```

Fallback (Google Fonts):
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;600;700&family=Red+Hat+Text:ital,wght@0,400;0,700;1,400&display=swap">
```

Include both links. The browser uses whichever loads first. If both fail (offline), Arial takes over.

### Type Scale (Web)

For web pages, dashboards, and general UI. Values from UW Style v5.3.0.

```css
:root {
  --uw-text-3xl: clamp(1.75rem, 1.75rem + (1vw - 0.388rem) * 2.069, 2.5rem);
  --uw-text-2xl: clamp(1.5rem, 1.5rem + (1vw - 0.388rem) * 1.379, 2rem);
  --uw-text-xl: clamp(1.375rem, 1.375rem + (1vw - 0.388rem) * 0.345, 1.5rem);
  --uw-text-lg: 1.25rem;
  --uw-text-base: 1.125rem;
  --uw-text-sm: 1rem;
}
```

### Type Scale (Presentations)

Larger scale for projected slides. Values tuned for 1920x1080 projection.

```css
:root {
  --uw-slide-title-size: clamp(2.5rem, 5vw, 4.5rem);
  --uw-slide-subtitle-size: clamp(1.25rem, 2.5vw, 2rem);
  --uw-slide-h2-size: clamp(1.75rem, 3.5vw, 3rem);
  --uw-slide-h3-size: clamp(1.375rem, 2.5vw, 2rem);
  --uw-slide-body-size: clamp(1.125rem, 1.8vw, 1.5rem);
  --uw-slide-caption-size: clamp(0.875rem, 1.2vw, 1rem);
  --uw-slide-code-size: clamp(0.85rem, 1.3vw, 1.1rem);
  --uw-slide-quote-size: clamp(1.5rem, 3vw, 2.5rem);
}
```

---

## Spacing

### Responsive Scale (default)

Fluid spacing that adapts to viewport. Use for presentations and responsive layouts.

```css
:root {
  --uw-space-xs: clamp(0.25rem, 0.5vw, 0.5rem);
  --uw-space-sm: clamp(0.5rem, 1.5vw, 0.75rem);
  --uw-space-md: clamp(1rem, 2.5vw, 1.25rem);
  --uw-space-lg: clamp(1.5rem, 3vw, 2rem);
  --uw-space-xl: clamp(2rem, 4vw, 3rem);
  --uw-space-2xl: clamp(2.5rem, 5vw, 5rem);
}
```

### Fixed Scale (UW Style utility classes)

Fixed spacing from UW Style CSS utility classes (`.uw-pad-*`, `.uw-mg-*`). Use for web pages and components where fixed values are appropriate.

| Token | Value | Utility suffix |
|-------|-------|---------------|
| `--uw-space-fixed-xs` | `0.25rem` (4px) | `-xs` |
| `--uw-space-fixed-sm` | `0.5rem` (8px) | `-s` |
| `--uw-space-fixed-md` | `1rem` (16px) | `-m` |
| `--uw-space-fixed-lg` | `2rem` (32px) | `-l` |
| `--uw-space-fixed-xl` | `4rem` (64px) | `-xl` |
| `--uw-space-fixed-2xl` | `8rem` (128px) | `-xxl` |

---

## Border Radius

Values extracted from UW Style CSS v5.3.0 component styles.

```css
:root {
  --uw-radius-sm: 4px;               /* Form inputs, small elements */
  --uw-radius-md: 0.5rem;            /* Buttons, cards, containers (most common) */
  --uw-radius-lg: 1.05rem;           /* Social icons, featured elements */
  --uw-radius-pill: 9999px;          /* Pill-shaped buttons, tags */
  --uw-radius-circle: 50%;           /* Avatars, round icons */
}
```

---

## Shadows

```css
:root {
  --uw-shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);                    /* Subtle lift */
  --uw-shadow-md: 2px 2px 6px 0 rgba(0, 0, 0, 0.25);              /* Cards, dropdowns, buttons */
}
```

UW Style uses only two shadow levels. Prefer `--uw-shadow-sm` for hover states and `--uw-shadow-md` for persistent elevation (cards, dropdowns).

---

## Layout

```css
:root {
  --uw-slide-padding: clamp(2rem, 4vw, 4rem);
  --uw-content-max-width: 72rem;           /* Max width for web content */
  --uw-content-narrow-width: 48rem;        /* Narrow content column */
}
```

### Breakpoints

From UW Style CSS media queries. Values are in `em` (the framework convention).

```css
:root {
  --uw-bp-sm: 37.5em;               /* 600px - Small tablets, large phones */
  --uw-bp-md: 56.25em;              /* 900px - Tablets, small desktops */
  --uw-bp-lg: 64em;                 /* 1024px - Desktops */
  --uw-bp-xl: 75em;                 /* 1200px - Wide desktops, max-width cap */
}
```

Additional breakpoints used sparingly: `17.5em` (280px, very small), `31.25em` (500px), `40em` (640px), `60.75em` (972px).

---

## Animation

```css
:root {
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);     /* Primary easing (ease-out expo) */
  --uw-duration-fast: 0.2s;
  --uw-duration-normal: 0.6s;
  --uw-duration-slow: 0.8s;
}
```

All animations must respect `prefers-reduced-motion: reduce`. See `accessibility.md`.

---

## Theme Tokens (Semantic)

These map the brand palette to semantic roles. Default values assume a light theme. Dark theme values are provided for presets, dark mode, or any context with a dark background.

### Light Theme (default)

```css
:root {
  /* Backgrounds */
  --uw-bg-primary: #ffffff;
  --uw-bg-secondary: #f3f3f3;

  /* Text */
  --uw-text-primary: #121212;
  --uw-text-secondary: #4a4a4a;

  /* Headings */
  --uw-heading-color: #121212;

  /* Accents */
  --uw-accent: #c5050c;
  --uw-accent-secondary: #9B0000;

  /* Surfaces */
  --uw-card-bg: #f3f3f3;

  /* Borders */
  --uw-border-color-web: #cfcfcf;       /* Matches UW Style CSS form/table borders */
  --uw-border-color-slide: #e1e5e7;     /* Brand palette gray-light */

  /* Links */
  --uw-link: #036796;
}
```

### Dark Theme

Override these tokens when using a dark background (e.g., `--uw-bg-primary: #121212` or `--uw-bg-primary: #c5050c`).

```css
[data-theme="dark"], .uw-theme-dark {
  --uw-bg-primary: #121212;
  --uw-bg-secondary: #282728;

  --uw-text-primary: #ffffff;
  --uw-text-secondary: rgba(255, 255, 255, 0.85);

  --uw-heading-color: #ffffff;

  --uw-accent: #FFB500;
  --uw-accent-secondary: #c5050c;

  --uw-card-bg: #282728;

  --uw-border-color-web: rgba(255, 255, 255, 0.2);
  --uw-border-color-slide: rgba(255, 255, 255, 0.2);

  --uw-link: #ffffff;
}
```

Slide presets that use dark backgrounds (conference, executive, event) apply these overrides automatically. See `skills/uw-slides/references/style-presets.md` for all preset definitions.

### Links

Link styling tokens and behavior. The base color is `--uw-link-blue` (#036796) from the brand palette.

```css
:root {
  --uw-link: var(--uw-link-blue);             /* Default link color */
  --uw-link-hover: var(--uw-link-blue);       /* Hover: same color, add underline */
  --uw-link-visited: var(--uw-link-blue);     /* No distinct visited color */
  --uw-link-underline-offset: 0.125rem;
  --uw-link-underline-thickness: 0.05em;
}
```

UW Style CSS link behavior: links have no underline by default, gain underline on hover. The color does not change between states. In dark theme / dark backgrounds, links use `#ffffff` instead. See `brand-system.md` for link usage rules.

---

## Mini-Bar

The UW signature design element: a small colored bar above headings.

```css
.uw-mini-bar::before {
  content: "";
  display: block;
  background-color: var(--uw-accent, #c5050c);
  width: 1.5em;
  height: 0.2em;
  margin-bottom: 0.375rem;
}
```

Variants: `.uw-mini-bar-white` (white bar for dark/red backgrounds), `.uw-mini-bar-center` (centered).

---

## UW Style CSS Mapping

The official UW Style framework (v5.3.0, in `web-template/css/uw-style.css`) uses camelCase token names. This table maps them to the design system's canonical kebab-case names.

**Do not modify `uw-style.css`.** It is the upstream framework maintained by University Marketing. When consuming it in a project alongside design system tokens, use the mapping below to translate.

### Colors

| Design System (canonical) | UW Style CSS | Value |
|--------------------------|-------------|-------|
| `--uw-red` | `--uwRed` | `#c5050c` |
| `--uw-red-dark` | `--uwRedDark` | `#9B0000` |
| `--uw-gray-dark` | `--uwGrayDark` | `#282728` |
| `--uw-gray-light` | `--uwGrayLight` | `#e1e5e7` |
| `--uw-gray-lightest` | `--uwGrayLightest` | `#f3f3f3` |
| `--uw-white` | `--uwWhite` | `#ffffff` |
| `--uw-black` | `--uwBlack` | `#121212` |
| `--uw-link-blue` | *(hardcoded `a { color: #036796 }`)* | `#036796` |
| `--uw-yellow` | *(not defined)* | `#FFB500` |
| `--uw-gray-blue` | *(not defined)* | `#6B8F99` |
| `--uw-blue` | *(not defined)* | `#385966` |

### Typography

| Design System (canonical) | UW Style CSS | Value |
|--------------------------|-------------|-------|
| `--uw-font-heading` | `--uwDisplayFont` | `Red Hat Display, sans-serif` |
| `--uw-font-body` | `--uwTextFont` | `Red Hat Text, sans-serif` |
| `--uw-font-button` | `--uwButtonFont` | `Red Hat Text, sans-serif` |
| `--uw-font-caption` | `--uwCaptionFont` | `Red Hat Text, sans-serif` |
| `--uw-font-quote-web` | `--uwBlockquoteFont` | `Red Hat Text, sans-serif` |
| `--uw-font-quote-slide` | *(presentation-only)* | `Red Hat Display, sans-serif` |
| *(not applicable)* | `--uwSiteTitleFont` | `Red Hat Display, sans-serif` |
| *(not applicable)* | `--uwSiteTaglineFont` | `Red Hat Display, sans-serif` |
| *(not applicable)* | `--uwCopyFont` | `Red Hat Text, sans-serif` |

Note: UW Style defines more granular font tokens (site title, tagline, copy) that all resolve to the same two families. The design system consolidates these into role-based tokens.

### Type Scale

| Design System (canonical) | UW Style CSS | Min | Max |
|--------------------------|-------------|-----|-----|
| `--uw-text-3xl` | `--uwFontSize3XL` | 1.75rem | 2.5rem |
| `--uw-text-2xl` | `--uwFontSize2XL` | 1.5rem | 2rem |
| `--uw-text-xl` | `--uwFontSizeXL` | 1.375rem | 1.5rem |
| `--uw-text-lg` | `--uwFontSizeMedium` | 1.25rem | 1.25rem |
| `--uw-text-base` | `--uwFontSizeBase` | 1.125rem | 1.125rem |
| `--uw-text-sm` | `--uwFontSizeSmall` | 1rem | 1rem |

### Spacing

| Design System (canonical) | UW Style CSS | Min | Max |
|--------------------------|-------------|-----|-----|
| `--uw-space-sm` | `--uwSpacingSmall` | 0.5rem | 0.75rem |
| `--uw-space-md` | `--uwSpacingMedium` | 1rem | 1.25rem |

UW Style defines only two spacing tokens. The design system extends the scale with xs, lg, xl, and 2xl. See "Fixed Scale" under Spacing for the utility class values.

### Border Radius

| Design System (canonical) | UW Style CSS | Value |
|--------------------------|-------------|-------|
| `--uw-radius-sm` | *(hardcoded on form inputs)* | `4px` |
| `--uw-radius-md` | *(hardcoded on buttons, cards)* | `0.5rem` |
| `--uw-radius-lg` | *(hardcoded on social icons)* | `1.05rem` |

UW Style does not use CSS custom properties for border-radius; values are hardcoded per component.

### Shadows

| Design System (canonical) | UW Style CSS | Value |
|--------------------------|-------------|-------|
| `--uw-shadow-sm` | *(hardcoded)* | `0 2px 4px rgba(0,0,0,0.1)` |
| `--uw-shadow-md` | *(hardcoded)* | `2px 2px 6px 0 rgba(0,0,0,0.25)` |

### Breakpoints

| Design System (canonical) | UW Style CSS | Value |
|--------------------------|-------------|-------|
| `--uw-bp-sm` | `@media (min-width: 37.5em)` | `37.5em` (600px) |
| `--uw-bp-md` | `@media (min-width: 56.25em)` | `56.25em` (900px) |
| `--uw-bp-lg` | `@media (min-width: 64em)` | `64em` (1024px) |
| `--uw-bp-xl` | `@media (min-width: 75em)` | `75em` (1200px) |

UW Style uses `em` units for breakpoints in media queries (not CSS custom properties).

---

## Token Migration Notes

### For skills referencing `brand-system.md` tokens

The old token names used in `brand-system.md` mapped directly:

| Old name | New canonical name |
|----------|-------------------|
| `--uw-heading-font` | `--uw-font-heading` |
| `--uw-body-font` | `--uw-font-body` |
| `--uw-quote-font` | `--uw-font-quote-slide` (presentations) or `--uw-font-quote-web` (web) |
| `--uw-code-font` | `--uw-font-code` |
| `--uw-title-size` | `--uw-slide-title-size` |
| `--uw-subtitle-size` | `--uw-slide-subtitle-size` |
| `--uw-h2-size` | `--uw-slide-h2-size` |
| `--uw-h3-size` | `--uw-slide-h3-size` |
| `--uw-body-size` | `--uw-slide-body-size` |
| `--uw-caption-size` | `--uw-slide-caption-size` |
| `--uw-code-size` | `--uw-slide-code-size` |
| `--uw-quote-size` | `--uw-slide-quote-size` |

Color tokens (`--uw-red`, `--uw-black`, etc.) are unchanged.
Theme tokens (`--uw-bg-primary`, `--uw-accent`, etc.) are unchanged.
