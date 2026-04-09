# Style Presets

Eight UW-Madison branded presets. Each defines CSS custom property overrides, layout treatment, and visual signature. All presets share the brand fonts and base color palette from `brand-system.md`.

---

## Preset: `lecture`

### Design Intent
Clean, high-readability, classroom-appropriate. Optimized for projection in lecture halls. Maximum legibility with minimal visual distraction.

### CSS Variables
```css
:root {
  --uw-bg-primary: #ffffff;
  --uw-bg-secondary: #f3f3f3;
  --uw-text-primary: #121212;
  --uw-text-secondary: #4a4a4a;
  --uw-heading-color: #121212;
  --uw-accent: #c5050c;
  --uw-accent-secondary: #9B0000;
  --uw-card-bg: #f3f3f3;
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(2.5rem, 5vw, 5rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
6px solid bar across top of every slide via the progress bar. Mini-bar above all slide headings.

### Logo
Full-color W Crest, upper-right, on title and closing slides only.

### Slide Backgrounds
- Title: White with a subtle `#f3f3f3` bottom 20% gradient
- Content: Pure white
- Section dividers: Badger Red `#c5050c` background, white text
- Closing: White

### Signature Elements
- Large, generously spaced typography
- Red bullet markers on lists
- Clean card backgrounds for grouped content

---

## Preset: `research`

### Design Intent
Structured, scholarly, data-friendly. Suited for thesis defenses, research group presentations, and academic conferences. Slightly more formal than `lecture`.

### CSS Variables
```css
:root {
  --uw-bg-primary: #ffffff;
  --uw-bg-secondary: #f7f8f9;
  --uw-text-primary: #121212;
  --uw-text-secondary: #555555;
  --uw-heading-color: #121212;
  --uw-accent: #9B0000;
  --uw-accent-secondary: #c5050c;
  --uw-card-bg: #f7f8f9;
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(2.5rem, 5vw, 5rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
Thin 3px dark red (`#9B0000`) line at the top of each slide. Mini-bar above headings uses dark red.

### Logo
Full-color W Crest on title slide. Omitted on content slides to maximize space for data.

### Slide Backgrounds
- Title: White with a thin dark red horizontal rule below the title
- Content: White or very subtle off-white `#f7f8f9`
- Section dividers: Dark red `#9B0000` background, white text
- Data slides: `#f7f8f9` to reduce glare on projected charts

### Signature Elements
- Slightly smaller title sizes to fit longer academic titles
- Numbered slide references in bottom-left corner
- Table-friendly layouts with brand-colored headers
- Two-column default for literature review / methods comparison

---

## Preset: `conference`

### Design Intent
Bold, confident, stage-ready. For keynotes, invited talks, and conference presentations. High visual impact with strong brand presence.

### CSS Variables
```css
:root {
  --uw-bg-primary: #ffffff;
  --uw-bg-secondary: #f3f3f3;
  --uw-text-primary: #121212;
  --uw-text-secondary: #333333;
  --uw-heading-color: #c5050c;
  --uw-accent: #c5050c;
  --uw-accent-secondary: #9B0000;
  --uw-card-bg: #f3f3f3;
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(3rem, 5vw, 5rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
Bold 8px red stripe across the top of the title slide. 4px on other slides. Section dividers use a full-width red background.

### Logo
Full-color W Crest on title slide and closing slide.

### Slide Backgrounds
- Title: White with large bold red heading text
- Content: White with generous padding
- Section dividers: Full Badger Red background, large white text
- Closing: White with centered red mini-bar

### Signature Elements
- Headings in Badger Red (not black) for strong brand presence
- Larger title sizes than other presets
- Bold red section dividers that fill the entire slide
- Wider spacing between elements

---

## Preset: `department`

### Design Intent
Professional, balanced, informational. For department overviews, annual reports, committee presentations. Approachable and organized.

### CSS Variables
```css
:root {
  --uw-bg-primary: #ffffff;
  --uw-bg-secondary: #f3f3f3;
  --uw-text-primary: #121212;
  --uw-text-secondary: #4a4a4a;
  --uw-heading-color: #282728;
  --uw-accent: #c5050c;
  --uw-accent-secondary: #6B8F99;
  --uw-card-bg: #f3f3f3;
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(2.5rem, 4vw, 4rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
Standard mini-bar above headings. A thin gray-blue (`#6B8F99`) accent line appears as a left border on card elements.

### Logo
Full-color W Crest on title and closing slides.

### Slide Backgrounds
- Title: White
- Content: White
- Section dividers: Gray-blue `#6B8F99` background, white text (a softer alternative)
- Cards/features: `#f3f3f3` with gray-blue left border

### Signature Elements
- Gray-blue accent complements the red
- Card-based layouts for organized information
- Two-column layouts for team/org structures
- Subtle, professional color usage

---

## Preset: `recruitment`

### Design Intent
Energetic, aspirational, photo-forward. For admissions events, student recruiting, open houses. Showcases campus life and UW spirit.

### CSS Variables
```css
:root {
  --uw-bg-primary: #ffffff;
  --uw-bg-secondary: #f3f3f3;
  --uw-text-primary: #121212;
  --uw-text-secondary: #333333;
  --uw-heading-color: #121212;
  --uw-accent: #c5050c;
  --uw-accent-secondary: #FFB500;
  --uw-card-bg: rgba(197, 5, 12, 0.9);
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(2rem, 4vw, 4rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
Bold red strip/banner overlaying images with white text inside (similar to the digital signage style).

### Logo
Full-color W Crest on white slides. White 1-color crest on image/red slides.

### Slide Backgrounds
- Title: Full-bleed photo with semi-transparent red overlay + white text (like the campus screen designs)
- Content: White with accent imagery
- Section dividers: Photo background with red overlay
- Closing: Badger Red with white text

### Signature Elements
- Photo-forward with red overlay text banners (matching the "Snow Days / Lunch Trays / Badger Ways" signage style)
- Yellow accent for call-to-action elements
- High-energy, bold typography
- Image-feature slides are the default content type
- For image slides: use CSS gradient overlay `linear-gradient(rgba(197,5,12,0.85), rgba(155,0,0,0.9))` over background images

---

## Preset: `data-driven`

### Design Intent
Clean, analytical, metrics-focused. For data presentations, dashboards, performance reviews. Maximizes space for charts and tables.

### CSS Variables
```css
:root {
  --uw-bg-primary: #f3f3f3;
  --uw-bg-secondary: #ffffff;
  --uw-text-primary: #121212;
  --uw-text-secondary: #555555;
  --uw-heading-color: #121212;
  --uw-accent: #c5050c;
  --uw-accent-secondary: #385966;
  --uw-card-bg: #ffffff;
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(2rem, 4vw, 3.5rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Chart Color Palette
```css
:root {
  --uw-chart-1: #c5050c;  /* Badger Red */
  --uw-chart-2: #385966;  /* Blue */
  --uw-chart-3: #6B8F99;  /* Gray Blue */
  --uw-chart-4: #FFB500;  /* Yellow */
  --uw-chart-5: #9B0000;  /* Dark Red */
  --uw-chart-6: #282728;  /* Dark Charcoal */
}
```

### Red Bar
Thin 3px red vertical rule on the left side of chart/data areas (matching the official data-driven PPT template).

### Logo
Full-color W Crest upper-right on title slide only. Omitted elsewhere to maximize data space.

### Slide Backgrounds
- Title: Light gray `#f3f3f3`
- Content/data: Light gray with white cards for chart containers
- Section dividers: Badger Red
- Tables: White background with red header row

### Signature Elements
- Light gray base background (reduces eye strain for data-heavy content)
- White card containers for charts and tables
- Red vertical rule accent on the left side of data areas
- Tighter padding to maximize chart space
- Brand-colored chart palette (red, blue, gray-blue, yellow, dark red, charcoal)

---

## Preset: `executive`

### Design Intent
Premium, polished, authoritative. For leadership presentations, board meetings, donor events. Dark theme conveys gravitas.

### CSS Variables
```css
:root {
  --uw-bg-primary: #121212;
  --uw-bg-secondary: #1a1a2e;
  --uw-text-primary: #ffffff;
  --uw-text-secondary: #cccccc;
  --uw-heading-color: #ffffff;
  --uw-accent: #c5050c;
  --uw-accent-secondary: #FFB500;
  --uw-card-bg: rgba(255, 255, 255, 0.08);
  --uw-gray-light: #333333;
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(3rem, 5vw, 5rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
Red mini-bar above headings on dark background. Progress bar in red.

### Logo
**1-color W Crest in white** (`uw-crest-1color.svg` with `fill: #ffffff`). Shown on title and closing slides.

### Slide Backgrounds
- Title: Rich black `#121212`
- Content: Rich black or very dark blue-black `#1a1a2e`
- Section dividers: Badger Red `#c5050c` (the one splash of full color)
- Cards: Semi-transparent white `rgba(255,255,255,0.08)`

### Signature Elements
- Dark theme with white text and red accents
- Subtle card backgrounds with glass-like transparency
- Yellow accent for key metrics or highlights
- Generous spacing for premium feel
- Red section dividers provide visual relief from the dark palette

### Special CSS
```css
/* Override bullet color for dark backgrounds */
.slide ul li::before {
  background-color: #c5050c;
}
/* Override table header for dark theme */
.slide th {
  background-color: #c5050c;
  color: #ffffff;
}
.slide td {
  border-bottom-color: #333333;
}
/* Override nav dots for dark theme */
.nav-dot {
  background: #333333;
}
```

---

## Preset: `event`

### Design Intent
Celebratory, vibrant, spirited. For event announcements, ceremonies, homecoming, commencement, and campus celebrations. Uses bold red as the primary background.

### CSS Variables
```css
:root {
  --uw-bg-primary: #c5050c;
  --uw-bg-secondary: #9B0000;
  --uw-text-primary: #ffffff;
  --uw-text-secondary: #ffe0e0;
  --uw-heading-color: #ffffff;
  --uw-accent: #FFB500;
  --uw-accent-secondary: #ffffff;
  --uw-card-bg: rgba(255, 255, 255, 0.15);
  --uw-heading-font: 'Red Hat Display', Arial, sans-serif;
  --uw-body-font: 'Red Hat Text', Arial, sans-serif;
  --uw-slide-padding: clamp(2.5rem, 5vw, 5rem);
  --uw-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Red Bar
White mini-bar above headings (since background is red). Yellow accent bar on special callout slides.

### Logo
**1-color W Crest in white** on red background. Shown on title and closing slides.

### Slide Backgrounds
- Title: Badger Red `#c5050c` with white text
- Content: Badger Red with white text
- Section dividers: Dark Red `#9B0000` or White (for contrast relief)
- Callout/highlight slides: White background with red text (alternating for visual variety)

### Signature Elements
- Bold red-as-background throughout (like the "Go get it, Badgers!" signage)
- Yellow accent for dates, CTAs, and key details
- White text throughout
- Alternating white slides for visual relief every 3-4 slides
- High-energy, celebration-forward

### Special CSS
```css
/* White bullets on red background */
.slide ul li::before {
  background-color: #ffffff;
}
/* Override mini-bar to white */
.uw-mini-bar::before {
  background-color: #ffffff;
}
/* Yellow highlight class */
.highlight {
  color: #FFB500;
  font-weight: 700;
}
/* Override nav dots for red theme */
.nav-dot {
  background: rgba(255, 255, 255, 0.4);
}
.nav-dot.active, .nav-dot:hover {
  background: #ffffff;
}
/* Alternating white slides */
.slide--light {
  background-color: #ffffff;
  color: #121212;
}
.slide--light .slide-heading,
.slide--light h2 { color: #c5050c; }
.slide--light .uw-mini-bar::before { background-color: #c5050c; }
.slide--light ul li::before { background-color: #c5050c; }
```
