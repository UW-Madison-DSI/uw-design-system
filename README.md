# UW-Madison Design System + Skills

A Claude Code plugin with a curated UW-Madison design system and skills that use it to generate branded digital materials.

## Overview

The **design system** (`brand/`) contains official UW-Madison brand assets, style specifications, the UW Style web template, and accessibility requirements. It is the shared foundation for any skill that produces UW-branded output.

The first skill built on this system is **`/uw-slides`**, which generates self-contained HTML slide presentations. More skills can be added to produce other branded materials (web pages, reports, emails, etc.) using the same design system.

### Design System

- Official color palette, typography, and logo usage rules from [brand.wisc.edu](https://brand.wisc.edu/)
- UW Style v5.3.0 web template (CSS framework, sample HTML, SVG icons)
- 211 hand-drawn SVG icons, decorative elements, campus illustrations, and textures
- WCAG 2.1 AA accessibility requirements
- See [`brand/README.md`](brand/README.md) for details

### UW-Slides Skill

- **Self-contained output** - one `.html` file, works anywhere, works offline (fonts fall back to Arial)
- **8 style presets** tailored to university use cases (lecture, research, conference, and more)
- **10 slide types** covering academic needs (title, content, two-column, data chart, code, quote, image, references, section divider, closing)
- **Brand-compliant by default** - colors, fonts, logos, and design elements all follow official guidelines
- **Accessible** - keyboard navigation, touch/swipe, screen reader support, reduced motion, 4.5:1 contrast ratios
- **PowerPoint import** - extract content from `.pptx` files and regenerate as branded HTML
- **PDF export** - convert to PDF via Playwright for sharing or printing
- **Web deployment** - deploy to Vercel with a single command
- **Presenter notes** - hidden notes per slide, toggled with the N key

## Installation

### Option 1: Install as a Claude Code plugin

From any project where you want to use the skill:

```
/install /path/to/skills
```

### Option 2: Reference the plugin directory

```bash
claude --plugin-dir /path/to/skills
```

### Option 3: Clone to the default skills location

```bash
git clone <repo-url> ~/.claude/skills/uw-slides
```

### Optional dependencies

These are only needed if you use the corresponding features:

| Feature | Install Command |
|---------|----------------|
| PowerPoint import | `pip install python-pptx` |
| PDF export | `npm install playwright && npx playwright install chromium` |
| Web deployment | `npm i -g vercel` |

## Usage

Invoke the skill with `/uw-slides` followed by a description of what you want.

### Create a presentation from a topic

```
/uw-slides A 10-slide lecture on machine learning fundamentals for CS undergrads
```

### Provide an outline

```
/uw-slides Create slides from this outline:
1. Introduction to CRISPR
2. How Cas9 finds its target
3. Applications in agriculture
4. Ethical considerations
5. What's next
```

### Specify a preset

```
/uw-slides Research defense on protein folding, use the research preset
```

### Convert a PowerPoint file

```
/uw-slides Convert my-talk.pptx to branded HTML slides
```

### Point to existing content

```
/uw-slides Build a brief intro deck for the project at /path/to/my/project
```

The skill will read your project's README and source files to understand what it does, then generate an appropriate presentation.

## Style Presets

Each preset defines colors, layout, logo variant, and visual signature while staying within UW brand guidelines. If you don't specify a preset, the skill will choose one based on your content and audience.

| Preset | Best For | Visual Style |
|--------|----------|--------------|
| `lecture` | Teaching, courses, classroom | Clean white, red mini-bars, generous spacing |
| `research` | Thesis defense, research talks | White with dark red accents, slide numbers, data-friendly |
| `conference` | Keynotes, invited talks | Bold red headings, strong brand presence |
| `department` | Department overviews, reports | White with gray-blue accent, card-based layouts |
| `recruitment` | Admissions, student outreach | Photo-forward with red overlays, high energy |
| `data-driven` | Metrics, dashboards, reviews | Light gray background, chart color palette, tight layout |
| `executive` | Board meetings, leadership, donors | Dark theme (#121212), premium feel, red + white accents |
| `event` | Celebrations, announcements | Badger Red background, white text, yellow accent |

## Presentation Controls

Once the HTML file is open in a browser:

| Action | Input |
|--------|-------|
| Next slide | Arrow Down, Arrow Right, Space, Scroll Down, Swipe Up |
| Previous slide | Arrow Up, Arrow Left, Page Up, Swipe Down |
| First slide | Home or Escape |
| Last slide | End |
| Toggle presenter notes | N |
| Print / save as PDF | Ctrl+P (clean print styles applied automatically) |
| Jump to slide | Click a navigation dot on the right edge |
| Deep link | Add `#slide-3` to the URL to link directly to slide 3 |

## How It Works

The skill uses a **progressive disclosure architecture**. The main orchestration file (`SKILL.md`) is kept lean at around 300 lines and tells Claude which reference files to load at each stage. This keeps context usage efficient.

### Workflow

1. **Content understanding** - Claude analyzes your request, asks clarifying questions if needed (topic, audience, length, preset)
2. **Preset selection** - picks the right visual style for your use case
3. **Generation** - reads the HTML template, base CSS, preset CSS, slide type specs, and SVG logos, then assembles a complete HTML file
4. **Delivery** - writes the file and opens it in your browser

### What gets generated

A single HTML file containing:
- Font links to the [UW CDN](https://cdn.wisc.cloud) (primary) and Google Fonts (fallback)
- All CSS inlined in one `<style>` block (viewport system, preset theme, slide-type styles)
- The official W Crest logo as inline SVG markup
- A `SlidePresentation` JavaScript class handling navigation, animations, and accessibility
- Semantic HTML with proper ARIA attributes

### Content rules (enforced automatically)

These follow the [StratComm presentation best practices](https://brand.wisc.edu/resources/):
- Title slides: max 8-word title, max 15-word subtitle
- Content slides: max 5 bullets, each max 12 words
- One idea per slide; if content overflows, it splits across slides
- Minimum 24pt-equivalent text size
- No all-caps headings
- Every slide fits in one viewport (no scrolling)

## Export and Deploy

### Export to PDF

Requires Playwright:

```bash
./scripts/export-pdf.sh path/to/presentation.html
```

Produces a PDF with one page per slide at 1920x1080 resolution.

### Deploy to Vercel

Requires the Vercel CLI:

```bash
./scripts/deploy.sh path/to/presentation.html my-talk
```

Deploys the presentation as a static site and returns a shareable URL.

## Project Structure

```
.claude-plugin/
  plugin.json                          # Plugin manifest (name, version, description)
brand/                                 # UW-Madison Design System (shared)
  README.md                            # Design system documentation
  brand-system.md                      # Colors, typography, logo rules, voice
  accessibility.md                     # WCAG 2.1 AA requirements, ARIA patterns
  asset-registry.md                    # Catalog of all brand assets
  resource-guide.md                    # Index of official UW brand resources
  web-template/                        # Official UW Style v5.3.0
    index.html                         # Sample page with all base element styles
    css/uw-style.css                   # Full CSS framework with design tokens
    js/_uw-style.min.js                # Header, menus, search JS
    images/                            # Crest SVG, icon sprite sheet, favicons
  assets/
    uw-crest-color.svg                 # Full-color W Crest (light backgrounds)
    uw-crest-1color.svg                # 1-color W Crest (dark backgrounds)
    favicon-w.svg                      # W favicon for browser tab
    icons/                             # 211 hand-drawn SVG icons
    elements/                          # Decorative hand-drawn elements (PNG)
    illustrations/                     # Campus building line drawings (PNG)
    textures/                          # Background texture patterns (PNG)
commands/
  uw-slides.md                         # /uw-slides slash command entry point
skills/uw-slides/                      # Slide generation skill
  SKILL.md                             # Main orchestration file
  references/
    style-presets.md                   # CSS definitions for all 8 presets
    slide-types.md                     # HTML structure + rules for 10 slide types
    best-practices.md                  # StratComm presentation guidelines
    delivery-guide.md                  # Accessible delivery practices
  assets/
    html-template.md                   # HTML boilerplate + SlidePresentation JS class
    viewport-base.css                  # Base CSS: viewport lock, scroll-snap, animations
scripts/
  open-presentation.sh                 # Open HTML in default browser
  extract-pptx.py                      # Extract content from PowerPoint files
  export-pdf.sh                        # Export to PDF via Playwright
  deploy.sh                            # Deploy to Vercel
uw resources/                          # Raw UW brand downloads (gitignored, not part of plugin)
```

## Brand Compliance

All generated presentations adhere to these rules from the [UW-Madison brand guidelines](https://brand.wisc.edu/):

- **Colors** - Badger Red `#c5050c` as primary accent; official secondary palette (`#9B0000`, `#e1e5e7`, `#121212`); accent colors used sparingly
- **Typography** - Red Hat Display for headings, Red Hat Text for body, loaded from the official UW font CDN (`cdn.wisc.cloud`)
- **Logo** - Official W Crest SVG embedded inline; positioned upper-right per brand templates; full-color on light, white on dark backgrounds; clear space maintained
- **Mini-bar** - The signature red bar element (`#c5050c`, 1.5em wide, 0.2em tall) appears above slide headings, matching the official `uw-style.css` implementation
- **Accessibility** - 4.5:1 minimum contrast ratio, keyboard navigation, `prefers-reduced-motion` support, semantic HTML, ARIA landmarks
- **Content** - Per StratComm guidelines: concise titles, limited text per slide, no all-caps, no distracting transitions

## Credits

- Brand guidelines and assets: [UW-Madison Brand](https://brand.wisc.edu/)
- Presentation best practices: UW-Madison Strategic Communications
- Presentation architecture inspired by: [frontend-slides](https://github.com/zarazhangrui/frontend-slides) by zarazhangrui
