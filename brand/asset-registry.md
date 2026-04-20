# Brand Asset Registry

This file catalogs all brand assets available for embedding in presentations. Assets live in `assets/` and are embedded as base64 data URIs to keep the HTML self-contained.

## How to Embed Assets

Read the file, convert to base64, and embed as a data URI:

**For SVG icons:**
```html
<!-- Read the SVG file and embed inline as <svg> markup -->
<svg class="slide-icon" ...>...</svg>
```

**For PNG images (elements, illustrations, textures):**
```html
<!-- Embed as base64 data URI in an <img> tag or CSS background -->
<img src="data:image/png;base64,..." class="decorative" aria-hidden="true" alt="">

<!-- Or as a CSS background -->
background-image: url('data:image/png;base64,...');
```

## Asset Selection Guidelines

- Read only the specific assets needed for the presentation (not all 211 icons)
- Pick 2-4 decorative elements per presentation, not more
- Icons should match the slide content contextually
- Use `aria-hidden="true"` and empty `alt=""` on all decorative images

---

## Icons (211 SVG icons)

**Path:** `assets/icons/icons-rgb-red_[name].svg`
**Format:** SVG, stroke-based, uses `#c5050c` stroke color
**Typical size:** 500 bytes - 3KB per icon
**Styling:** Override stroke color with CSS: `.slide-icon { stroke: #ffffff; }` for dark backgrounds

### Icon Categories

Pick icons that match your slide content. Here are the icons grouped by topic:

**Academic / Research:**
atom, beaker, book, brain, braille, calculator, chart, chart-03, chart-104, chemistry, classroom, computer, diploma, DNA, drawing, folder, graduation-gown, grad cap, idea, institution, lecture-hall, lightbulb, magnifying-glass, mircoscope, notepad, open-book, org-chart, paper, pencil, pillar, podium, technology, telescope

**Data / Analytics:**
chart, chart-03, chart-104, target, stop-watch, calculator, link, robotics, AI, 3D-cube

**Agriculture / Nature:**
acorn, barn, bee, bird, campfire, cat, climate-change, cow, deer, dog, fish, flamingo, flower, flower2, four-leaf-clover, fox, garden-tools, leaves, mallard, milk, plant, tree, tree2, trees, tulip, turtle, water-drop

**Campus Life:**
balloons, basketball, bike, bonfire, cafe, camp-randall, canoe, celebrate, celebration, chair, chazen-museum, club-banner, coffee, disco-ball, drum, emotions, fireworks, foam-finger, football, football-helmet, game-controller, headphones, hockey, ice-cream, kite, marching-band-hat, medal, megaphone, music-notes, party, pompoms, pontoon, popcorn, present, sailboat, sparklers, takeaway-coffee, tennis, theater, tickets, trumpet, vinyl-record, volleyball

**Campus Buildings:**
camp-randall, capitol, chazen-museum, institution, lecture-hall, neighborhood

**People / Community:**
accessibility, bunk-beds, connects, counseling-headset, dancer, emotions, handshake, hearing-aid, meditate, people, speech-bubbles, wheelchair

**Health / Science:**
atom, beaker, chemistry, DNA, first-aid, heart-organ, heartbeat, mircoscope, regenerative-medicine, stethoscope, syringe

**Business / Professional:**
award, briefcase, chart, check-box, crane, delivery, folder, give-money, handshake, hardhat, logistics, luggage, mail, money, newspaper, org-chart, phone, ribbon, security, toolbox

**Travel / Geography:**
automobile, bus, canoe, compass, hike-boot, luggage, map, map-destination, pinpoint, planet, road, sailboat, world, wisconsin

**Weather / Nature:**
cloud, moon-stars, partly-cloudy, rainy, rainbow, snow-flake, snowflake, snowflake2, sun, sunset-choppy-waves, sunset-smooth-water, tornado, umbrella, water-drop, waves, weather, weather-satellite, wind-turbine

**Food:**
apple, cake, cheese, chef-hat, coffee, fork-spoon, ice-cream, ice-cream-cone, ice-cream-cup, milk, pie, popcorn, pretzel, takeaway-coffee

**Communication:**
hashtag, link, loud-speaker, mail, megaphone, megaphone-celebration, microphone, newspaper, phone, quote, speech-bubbles, video-camera

**Sustainability:**
climate-change, recycle, solar-panel, water-drop, wind-turbine

---

## Graphic Elements (18 elements x 2 colors)

**Path (red):** `assets/elements/red/elements-rgb-red_[name].png`
**Path (white):** `assets/elements/white/elements_[name]-rgb-white.png`
**Format:** PNG with transparent background
**Size:** 2KB - 58KB per element

Note: Red and white files use different naming conventions (inherited from brand.wisc.edu download).

Use **red** elements on light backgrounds, **white** elements on dark/red backgrounds.

| Element | Best Used For | Size |
|---------|--------------|------|
| `mini-bars` | Signature brand accent (short bar + long bar) | 2KB |
| `container` | Framing content areas | 3KB |
| `dash-line` | Horizontal dividers, separators | 10KB |
| `short-wave` | Section accents, background decoration | 9KB |
| `long-wave` | Full-width decorative bands | 15KB |
| `lightning-bolt` | Energy, impact, call-to-action emphasis | 11KB |
| `W` | Hand-drawn W watermark on title/closing slides | 18KB |
| `scribble1` | Casual, hand-drawn accent | 16KB |
| `scribble2` | Casual, hand-drawn accent (variant) | 22KB |
| `long-scribble` | Extended hand-drawn underline or divider | 58KB |
| `asterisk-thin` | Marker, footnote indicator | 20KB |
| `asterisk-thick` | Bold marker, emphasis point | 23KB |
| `circled-asterisk` | Highlighted marker, key point indicator | 30KB |
| `explosion` | Attention, surprise, announcement emphasis | 37KB |
| `dash-circle-thin` | Encircling content, subtle framing | 30KB |
| `dash-circle-med` | Medium-weight circular frame | 31KB |
| `dash-circle-thick` | Bold circular frame | 28KB |
| `word-bubble-scribble` | Quote slides, testimonials, callouts | 25KB |

### Recommended Usage Per Slide Type

| Slide Type | Suggested Elements |
|-----------|-------------------|
| `title-slide` | `W` watermark (low opacity), `long-wave` bottom accent |
| `section-divider` | `short-wave` (white) as background accent, `explosion` for energy |
| `content` | None typically, or subtle `dash-line` separator |
| `quote` | `word-bubble-scribble` behind the quote |
| `closing` | `W` watermark, `mini-bars` accent |
| `event` presets | `explosion`, `lightning-bolt`, `asterisk-thick` for energy |

---

## Campus Illustrations (20 buildings)

**Path:** `assets/illustrations/illustrations-red_[name].png`
**Format:** PNG with transparent background, red line art
**Size:** 3KB - 8KB per illustration (very lightweight)

| Illustration | Landmark |
|-------------|----------|
| `Agricultural Hall` | College of Agricultural and Life Sciences |
| `Animals` | Animal/livestock motif |
| `Bascom` | Bascom Hall (main admin building, iconic) |
| `Camp Randall Arch` | Camp Randall Memorial Arch |
| `Capitol` | Wisconsin State Capitol |
| `Carillon Tower` | Carillon Tower |
| `Education` | Education Building |
| `Fieldhouse` | UW Fieldhouse |
| `Hamel Music Center` | Hamel Music Center |
| `Lady of the lake` | Lady of the Lake statue |
| `Memorial Union` | Memorial Union (Terrace) |
| `Monona Terrace` | Monona Terrace Convention Center |
| `Music Hall` | Music Hall |
| `Nancy Nicholas Hall` | Nancy Nicholas Hall |
| `Red Gym` | Red Gym / Armory |
| `Science Hall` | Science Hall |
| `Stock Pavilion` | Stock Pavilion |
| `Transportation` | Transportation motif |
| `Washburn Observatory` | Washburn Observatory |
| `Máquina Fountain` | Máquina Fountain |

### Recommended Usage

- **Title slides**: Place a campus building illustration at low opacity (10-15%) as a background watermark, or at full opacity in a corner
- **Closing slides**: Bascom Hall or Memorial Union as a branded sign-off element
- **Section dividers**: Subtle background illustration adds sense of place
- **Recruitment preset**: Use prominently to showcase campus

---

## Textures (5 patterns)

**Path:** `assets/textures/textures-rgb-red_[name].png`
**Format:** PNG, red on white
**Size:** 95KB - 145KB per texture

| Texture | Description | Best Used For |
|---------|-------------|--------------|
| `hand-drawn-dots` | Scattered dot pattern | Subtle background texture |
| `hand-drawn-grid` | Loose crosshatch grid | Academic/notebook feel |
| `ripple-large` | Wide wavy lines | Full-slide background accent |
| `ripple-medium` | Medium wavy lines | Section background |
| `ripple-small` | Tight wavy lines | Dense pattern overlay |

### Recommended Usage

- Apply as low-opacity (5-10%) CSS background overlays on section dividers or title slides
- Use `background-repeat: repeat` for textures that tile
- Use `mix-blend-mode: multiply` or `opacity: 0.08` to keep text readable
- White-on-red: for red background slides, use `background-blend-mode` or invert
