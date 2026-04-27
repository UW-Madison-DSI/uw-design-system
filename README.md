# DSI Skills

The University of Wisconsin-Madison is a public R1 research university. Its visual identity is built on Badger Red (#c5050c), the Red Hat type family, the W Crest, and a set of hand-drawn illustrative elements that give the brand a distinctive, approachable personality. This repo codifies that identity as a structured design system: tokens, components, accessibility rules, and curated assets, all derived from the official [brand.wisc.edu](https://brand.wisc.edu/) guidelines and the UW Style CSS framework (v5.3.0). It is designed to be consumed by humans, AI tools, and code generators alike.

## Start Here

If you want to understand the system quickly, read these three files in order:

1. **[`brand/tokens.md`](brand/tokens.md)** - Every color, font, size, spacing, shadow, and breakpoint in the system. This is the single source of truth for all design values.
2. **[`brand/components.md`](brand/components.md)** - Buttons, cards, tables, forms, navigation, header, footer, and utility classes extracted from the UW Style CSS framework. Shows how tokens become UI.
3. **[`brand/brand-system.md`](brand/brand-system.md)** - Logo usage rules, link styling, and brand voice. The qualitative rules that tokens alone don't capture.

## Where Things Live

```
brand/                          Design system (the core of this repo)
  tokens.md                     Colors, typography, spacing, radius, shadows,
                                breakpoints, animation, chart palette, theme
                                tokens, UW Style CSS variable mapping
  components.md                 UI component catalog (from UW Style CSS)
  brand-system.md               Logo rules, link usage, brand voice and tone
  accessibility.md              WCAG 2.1 AA requirements (UW Policy UW-519)
  asset-registry.md             Curated asset catalog with categories and sizing
  resource-guide.md             Full index of brand.wisc.edu downloads
  assets/                       Ready-to-embed brand assets
    uw-crest-color.svg            Full-color W Crest (light backgrounds)
    uw-crest-1color.svg           1-color W Crest (dark backgrounds)
    favicon-w.svg                 Browser tab favicon
    icons/                        211 hand-drawn SVG icons
    elements/                     36 decorative PNGs (18 red + 18 white)
    illustrations/                20 campus building line drawings (PNG)
    textures/                     5 background texture patterns (PNG)
  fonts/                        Red Hat Display + Text woff2 files (OFL license)
  web-template/                 Official UW Style v5.3.0 (upstream, do not modify)

skills/uw-slides/               UW-branded HTML slide generator
  SKILL.md                        Orchestration and generation rules
  references/                     Presets, slide types, best practices
  assets/                         HTML template, base CSS
  scripts/                        Build/export utilities (PDF, deploy, PPTX import)

skills/dsi-deploy/              DSI infrastructure deployment assessor
  SKILL.md                        Assessment and artifact generation rules
  references/                     Compose/Dockerfile patterns, checklists

commands/                       Claude Code slash command entry points
.claude-plugin/                 Plugin registration for Claude Code
_source-materials/              Raw brand.wisc.edu downloads (gitignored, ~659MB)
```

## Design Principles

These principles are derived from the UW-Madison brand guidelines and govern decisions throughout the system.

**Badger Red is sacred.** The value `#c5050c` is never modified, approximated, or replaced. It is the primary accent in every context. Dark Red (`#9B0000`) is the only acceptable darkened variant, and it is a separate defined token.

**Accessibility is not optional.** All output must meet WCAG 2.1 AA (UW Policy UW-519). This means 4.5:1 contrast for normal text, 3:1 for large text, semantic HTML, keyboard operability, and respect for `prefers-reduced-motion`. The contrast ratio table in `tokens.md` pre-validates every brand color pairing.

**Two fonts, no exceptions.** Red Hat Display for headings, Red Hat Text for body. Arial is the fallback, not a design choice. No other typefaces enter the system.

**Light by default, dark when intentional.** The default theme is white backgrounds with dark text. Dark themes (black or red backgrounds) exist for specific contexts (executive presentations, event branding) and have their own semantic token overrides in `tokens.md`.

**Hand-drawn elements are the personality.** Icons, illustrations, and decorative elements use a loose, hand-drawn style that distinguishes UW from other institutional brands. They are used sparingly (2-3 per surface) and always as decoration (`aria-hidden="true"`), never as the sole carrier of meaning.

**One source of truth per fact.** Design values live in `tokens.md`. Logo rules live in `brand-system.md`. Accessibility requirements live in `accessibility.md`. Other files cross-reference rather than duplicate.

## Token Naming

All tokens use the convention `--uw-{category}-{name}` in kebab-case:

```
--uw-red              color
--uw-font-heading     typography
--uw-space-md         spacing
--uw-radius-md        border radius
--uw-shadow-sm        elevation
--uw-bp-lg            breakpoint
--uw-bg-primary       semantic/theme
```

The upstream UW Style CSS uses camelCase (`--uwRed`, `--uwDisplayFont`). The mapping between the two conventions is documented in `tokens.md` under "UW Style CSS Mapping." Do not modify the upstream CSS; use the mapping to translate.

## Design System Boundary

Everything in `brand/` is the design system. It defines the UW-Madison brand identity independent of any output format.

Everything outside `brand/` consumes the design system but is not part of it. The `skills/uw-slides/` directory, for example, adds presentation-specific layout (viewport locking, slide types, style presets) that should not be generalized to other contexts. The `_source-materials/` directory (gitignored) contains the raw ~659MB download from brand.wisc.edu; the curated subset lives in `brand/assets/`.

When extracting brand rules for a new tool or context, start from `brand/` and ignore everything else.

---

## UW-Slides Skill

The first tool built on this design system. It generates self-contained HTML slide presentations that are brand-compliant by default.

### Quick Start

```
/uw-slides A 10-slide lecture on machine learning fundamentals for CS undergrads
```

### What It Produces

A single `.html` file containing all CSS, JS, and SVG inline. Works offline (fonts fall back to Arial). Opens in any browser.

### Presets

| Preset | Best For |
|--------|----------|
| `lecture` | Teaching, courses, classroom |
| `research` | Thesis defense, research talks, academic conferences |
| `conference` | Keynotes, invited talks, high-impact presentations |
| `department` | Department overviews, reports, committee updates |
| `recruitment` | Admissions, student outreach, open houses |
| `data-driven` | Metrics, dashboards, performance reviews |
| `executive` | Board meetings, leadership, donor events |
| `event` | Celebrations, announcements, homecoming, commencement |

### Controls

| Action | Input |
|--------|-------|
| Next slide | Arrow Down, Arrow Right, Space, Scroll, Swipe Up |
| Previous slide | Arrow Up, Arrow Left, Page Up, Swipe Down |
| First / Last slide | Home / End |
| Toggle presenter notes | N |
| Print | Ctrl+P |
| Jump to slide | Click nav dot, or add `#slide-3` to URL |

### Other Modes

```
/uw-slides Convert my-talk.pptx to branded HTML slides
```

```
/uw-slides Build a brief intro deck for the project at /path/to/my/project
```

### Export and Deploy

| Feature | Command | Requires |
|---------|---------|----------|
| PDF export | `./skills/uw-slides/scripts/export-pdf.sh presentation.html` | Playwright |
| Web deploy | `./skills/uw-slides/scripts/deploy.sh presentation.html my-talk` | Vercel CLI |
| PowerPoint import | (automatic when given a .pptx file) | `python-pptx` |

## Installation

### As a Claude Code plugin

```
/install /path/to/this/repo
```

### With the plugin-dir flag

```bash
claude --plugin-dir /path/to/this/repo
```

### Clone to the default location

```bash
git clone <repo-url> ~/.claude/skills/dsi-skills
```

## Source

All brand assets from [brand.wisc.edu/resources](https://brand.wisc.edu/resources/), downloaded April 9, 2026. UW Style CSS framework v5.3.0 maintained by University Marketing.

## Credits

- Brand guidelines and assets: [UW-Madison Brand](https://brand.wisc.edu/)
- Presentation best practices: UW-Madison Strategic Communications
- Slide architecture inspired by: [frontend-slides](https://github.com/zarazhangrui/frontend-slides) by zarazhangrui
