# UW-Madison Design System

Curated brand assets, style specifications, and accessibility requirements for building UW-Madison branded digital materials with Claude Code.

All source material comes from [brand.wisc.edu/resources](https://brand.wisc.edu/resources/) and the official UW Style CSS framework (v5.3.0).

## What's Here

| Path | Contents |
|------|----------|
| `brand-system.md` | Color palette, typography, logo rules, voice and tone |
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
| `assets/icons/` | 211 | SVG | Hand-drawn icons (campus, academic, nature, sports, etc.) |
| `assets/elements/` | 18 | PNG | Hand-drawn decorative elements in red and white |
| `assets/illustrations/` | 20 | PNG | Campus building line drawings |
| `assets/textures/` | 8 | PNG | Background texture patterns |

## Web Template (UW Style v5.3.0)

The `web-template/` directory contains the official HTML/CSS/JS framework maintained by University Marketing. This is the source of truth for UW's digital brand implementation.

Key files:
- `css/uw-style.css` - Full CSS framework with design tokens and component styles
- `index.html` - Sample page showing all base element styles
- `images/uw-crest.svg` - Official W Crest with radial gradient
- `images/uw-icons.svg` - SVG sprite sheet (caret, menu, close, social, footer crest)

CSS design tokens (from `:root`):
```css
--uwRed: #c5050c;
--uwRedDark: #9B0000;
--uwGrayDark: #282728;
--uwGrayLight: #e1e5e7;
--uwGrayLightest: #f3f3f3;
--uwWhite: #ffffff;
--uwBlack: #121212;
--uwDisplayFont: Red Hat Display, sans-serif;
--uwTextFont: Red Hat Text, sans-serif;
```

Fonts load from `https://cdn.wisc.cloud/fonts/uw-rh/0.0.1/fonts.css`.

## Usage

This design system is consumed by skills and other tools that generate UW-branded output. Currently:

- **`/uw-slides`** - HTML slide presentations

Any new skill that needs UW branding should reference this design system rather than duplicating brand rules.

## Source

Assets downloaded from [brand.wisc.edu/resources](https://brand.wisc.edu/resources/) on April 9, 2026.
