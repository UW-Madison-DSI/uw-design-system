# UW-Madison Design System

Curated brand assets, style specifications, and accessibility requirements for building UW-Madison branded digital materials with Claude Code.

All source material comes from [brand.wisc.edu/resources](https://brand.wisc.edu/resources/) and the official UW Style CSS framework (v5.3.0).

## What's Here

| Path | Contents |
|------|----------|
| `tokens.md` | **Canonical design tokens**: colors, typography, spacing, border-radius, shadows, breakpoints, animation, chart palette, theme tokens, UW Style CSS mapping |
| `brand-system.md` | Logo rules, link usage, brand voice and tone (references tokens.md for values) |
| `components.md` | **Component catalog**: buttons, cards, tables, forms, nav, header, footer, utility classes (extracted from UW Style CSS) |
| `accessibility.md` | WCAG 2.1 AA requirements, semantic HTML patterns, ARIA landmarks |
| `asset-registry.md` | Catalog of all brand assets with categories and usage guidance |
| `resource-guide.md` | Index of all official UW brand resources (logos, icons, templates, etc.) |
| `web-template/` | Official UW Style v5.3.0: CSS framework, sample HTML, JS, SVG icons |
| `assets/` | Curated brand assets ready for embedding |

## Assets

| Directory | Count | Format | Description |
|-----------|-------|--------|-------------|
| `assets/uw-crest-color.svg` | 1 | SVG | Full-color W Crest (light backgrounds) |
| `assets/uw-crest-1color.svg` | 1 | SVG | 1-color W Crest (dark backgrounds) |
| `assets/favicon-w.svg` | 1 | SVG | Browser tab favicon |
| `assets/icons/` | 211 | SVG | Hand-drawn icons, red only (campus, academic, nature, sports, etc.) |
| `assets/elements/` | 36 | PNG | Hand-drawn decorative elements (18 red + 18 white) |
| `assets/illustrations/` | 20 | PNG | Campus building line drawings, red only |
| `assets/textures/` | 5 | PNG | Background texture patterns, red only |

## Web Template (UW Style v5.3.0)

The `web-template/` directory contains the official HTML/CSS/JS framework maintained by University Marketing. This is the source of truth for UW's digital brand implementation.

Key files:
- `css/uw-style.css` - Full CSS framework with design tokens and component styles
- `index.html` - Sample page showing all base element styles
- `images/uw-crest.svg` - Official W Crest with radial gradient
- `images/uw-icons.svg` - SVG sprite sheet (caret, menu, close, social, footer crest)

The framework defines CSS custom properties using camelCase names (e.g., `--uwRed`). See `tokens.md` (UW Style CSS Mapping section) for the full mapping between these and the design system's canonical kebab-case tokens.

Fonts load from `https://cdn.wisc.cloud/fonts/uw-rh/0.0.1/fonts.css`.

## Usage

This design system is consumed by skills and other tools that generate UW-branded output. Currently:

- **`/uw-slides`** - HTML slide presentations

Any new skill that needs UW branding should reference this design system rather than duplicating brand rules.

## Design System Boundary

Everything in `brand/` is the general-purpose design system. It defines the UW-Madison brand identity independent of any specific output format.

**Included (brand system):**
- `tokens.md` - All design tokens (colors, type, spacing, radius, shadows, breakpoints, themes)
- `components.md` - UI component patterns from UW Style CSS
- `brand-system.md` - Logo rules, link styling, brand voice
- `accessibility.md` - WCAG 2.1 AA compliance requirements
- `asset-registry.md` - Curated brand assets catalog
- `resource-guide.md` - Full brand.wisc.edu resource index
- `web-template/` - Official UW Style CSS framework (upstream, do not modify)
- `assets/` - SVG icons, PNG elements/illustrations/textures, crest SVGs

**Excluded (not part of the design system):**
- `skills/uw-slides/` - Slide-specific presets, viewport CSS, slide-type HTML structures, SlidePresentation JS class. These consume design tokens but add presentation-specific layout that should not be generalized.
- `uw resources/` - Raw downloads from brand.wisc.edu (gitignored, ~659MB). The curated subset lives in `assets/`.
- `.claude-plugin/` - Plugin registration metadata for Claude Code.
- `scripts/` - Build/export utilities (PDF export, deployment).

Skills consume the design system but are not part of it. When extracting brand rules for a new context, start from `brand/` and ignore everything else.

## Source

Assets downloaded from [brand.wisc.edu/resources](https://brand.wisc.edu/resources/) on April 9, 2026.
