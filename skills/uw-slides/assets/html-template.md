# HTML Template

This is the complete HTML boilerplate for every UW-Slides presentation. Claude reads this file during generation and uses it as the skeleton, filling in the marked placeholders.

## Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{PRESENTATION_TITLE}}</title>
  <link rel="icon" href="data:image/svg+xml,{{FAVICON_SVG_URI_ENCODED}}" type="image/svg+xml">

  <!-- UW Brand Fonts: primary from UW CDN, fallback to Google Fonts -->
  <link rel="preconnect" href="https://cdn.wisc.cloud" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://cdn.wisc.cloud/fonts/uw-rh/0.0.1/fonts.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;600;700&family=Red+Hat+Text:ital,wght@0,400;0,700;1,400&display=swap">

  <style>
    /* ===== CSS Custom Properties (from selected preset) ===== */
    :root {
      {{PRESET_CSS_VARIABLES}}
    }

    /* ===== Viewport Base CSS ===== */
    /* Paste the full contents of viewport-base.css here */
    {{VIEWPORT_BASE_CSS}}

    /* ===== Preset-Specific Styles ===== */
    {{PRESET_SPECIFIC_CSS}}

    /* ===== Slide-Type-Specific Styles ===== */
    {{SLIDE_TYPE_CSS}}
  </style>
</head>
<body>
  <!-- Progress Bar -->
  <div class="progress-bar" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">
    <div class="progress-fill"></div>
  </div>

  <!-- Navigation Dots -->
  <nav class="nav-dots" aria-label="Slide navigation">
    {{NAV_DOTS}}
    <!-- Example: <button class="nav-dot active" aria-label="Slide 1" data-slide="0"></button> -->
  </nav>

  <!-- Presentation Slides -->
  <main class="presentation" role="main" aria-label="Slide presentation">
    {{SLIDES}}
    <!--
      Each slide is a <section class="slide"> element.
      See slide-types.md for the HTML structure of each type.
    -->
  </main>

  <!-- Keyboard Hint (auto-hides after 5 seconds) -->
  <div class="keyboard-hint" aria-hidden="true">
    Use arrow keys or scroll to navigate
  </div>

  <!-- Presenter Notes Panel (toggle with N key) -->
  <div class="presenter-notes" aria-hidden="true"></div>

  <script>
    {{SLIDE_PRESENTATION_JS}}
  </script>
</body>
</html>
```

## SlidePresentation JavaScript Class

Paste this complete JS class into the `{{SLIDE_PRESENTATION_JS}}` placeholder. It provides all navigation and animation functionality.

```javascript
class SlidePresentation {
  constructor() {
    this.slides = document.querySelectorAll('.slide');
    this.dots = document.querySelectorAll('.nav-dot');
    this.progressFill = document.querySelector('.progress-fill');
    this.progressBar = document.querySelector('.progress-bar');
    this.keyboardHint = document.querySelector('.keyboard-hint');
    this.notesPanel = document.querySelector('.presenter-notes');
    this.currentSlide = 0;
    this.totalSlides = this.slides.length;
    this.isScrolling = false;
    this.notesVisible = false;

    this.init();
  }

  init() {
    this.setupIntersectionObserver();
    this.setupKeyboardNav();
    this.setupTouchNav();
    this.setupWheelNav();
    this.setupDotNav();
    this.setupHashNav();
    this.updateProgress();
    this.hideKeyboardHint();

    // Activate first slide animations
    requestAnimationFrame(() => {
      this.activateSlideAnimations(0);
    });
  }

  // --- Intersection Observer for scroll-triggered animations ---
  setupIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const index = Array.from(this.slides).indexOf(entry.target);
          this.currentSlide = index;
          this.updateProgress();
          this.updateDots();
          this.updateHash();
          this.activateSlideAnimations(index);
          this.updateNotes(index);
          entry.target.setAttribute('aria-current', 'step');
        } else {
          entry.target.removeAttribute('aria-current');
        }
      });
    }, {
      threshold: 0.5
    });

    this.slides.forEach(slide => observer.observe(slide));
  }

  // --- Activate animations within a slide ---
  activateSlideAnimations(index) {
    const slide = this.slides[index];
    if (!slide) return;

    const animatedElements = slide.querySelectorAll('.animate-in, .animate-fade, .animate-scale, .stagger');
    animatedElements.forEach(el => el.classList.add('visible'));
  }

  // --- Keyboard Navigation ---
  setupKeyboardNav() {
    document.addEventListener('keydown', (e) => {
      switch(e.key) {
        case 'ArrowDown':
        case 'ArrowRight':
        case ' ':
        case 'PageDown':
          e.preventDefault();
          this.goToSlide(this.currentSlide + 1);
          break;
        case 'ArrowUp':
        case 'ArrowLeft':
        case 'PageUp':
          e.preventDefault();
          this.goToSlide(this.currentSlide - 1);
          break;
        case 'Home':
          e.preventDefault();
          this.goToSlide(0);
          break;
        case 'End':
          e.preventDefault();
          this.goToSlide(this.totalSlides - 1);
          break;
        case 'Escape':
          e.preventDefault();
          this.goToSlide(0);
          break;
        case 'n':
        case 'N':
          this.toggleNotes();
          break;
      }
    });
  }

  // --- Touch / Swipe Navigation ---
  setupTouchNav() {
    let touchStartY = 0;
    let touchStartX = 0;

    document.addEventListener('touchstart', (e) => {
      touchStartY = e.touches[0].clientY;
      touchStartX = e.touches[0].clientX;
    }, { passive: true });

    document.addEventListener('touchend', (e) => {
      const touchEndY = e.changedTouches[0].clientY;
      const touchEndX = e.changedTouches[0].clientX;
      const diffY = touchStartY - touchEndY;
      const diffX = touchStartX - touchEndX;

      // Only handle vertical swipes (threshold 50px, and more vertical than horizontal)
      if (Math.abs(diffY) > 50 && Math.abs(diffY) > Math.abs(diffX)) {
        if (diffY > 0) {
          this.goToSlide(this.currentSlide + 1);
        } else {
          this.goToSlide(this.currentSlide - 1);
        }
      }
    }, { passive: true });
  }

  // --- Mouse Wheel Navigation (with debounce) ---
  setupWheelNav() {
    let wheelTimeout;
    document.addEventListener('wheel', (e) => {
      if (this.isScrolling) return;
      clearTimeout(wheelTimeout);

      wheelTimeout = setTimeout(() => {
        if (Math.abs(e.deltaY) > 30) {
          this.isScrolling = true;
          if (e.deltaY > 0) {
            this.goToSlide(this.currentSlide + 1);
          } else {
            this.goToSlide(this.currentSlide - 1);
          }
          setTimeout(() => { this.isScrolling = false; }, 800);
        }
      }, 50);
    }, { passive: true });
  }

  // --- Navigation Dot Click ---
  setupDotNav() {
    this.dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        this.goToSlide(index);
      });
    });
  }

  // --- Hash-Based Deep Linking ---
  setupHashNav() {
    const hash = window.location.hash;
    if (hash && hash.startsWith('#slide-')) {
      const slideNum = parseInt(hash.replace('#slide-', ''), 10) - 1;
      if (slideNum >= 0 && slideNum < this.totalSlides) {
        // Delay to allow page to render
        setTimeout(() => this.goToSlide(slideNum), 100);
      }
    }
  }

  // --- Navigate to Slide ---
  goToSlide(index) {
    if (index < 0 || index >= this.totalSlides) return;
    this.currentSlide = index;
    this.slides[index].scrollIntoView({ behavior: 'smooth' });
  }

  // --- Update Progress Bar ---
  updateProgress() {
    const progress = ((this.currentSlide + 1) / this.totalSlides) * 100;
    if (this.progressFill) {
      this.progressFill.style.width = `${progress}%`;
    }
    if (this.progressBar) {
      this.progressBar.setAttribute('aria-valuenow', Math.round(progress));
    }
  }

  // --- Update Navigation Dots ---
  updateDots() {
    this.dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === this.currentSlide);
      dot.setAttribute('aria-current', index === this.currentSlide ? 'step' : 'false');
    });
  }

  // --- Update URL Hash ---
  updateHash() {
    const newHash = `#slide-${this.currentSlide + 1}`;
    if (window.location.hash !== newHash) {
      history.replaceState(null, null, newHash);
    }
  }

  // --- Keyboard Hint Auto-Hide ---
  hideKeyboardHint() {
    if (this.keyboardHint) {
      setTimeout(() => {
        this.keyboardHint.style.transition = 'opacity 1s ease';
        this.keyboardHint.style.opacity = '0';
        setTimeout(() => { this.keyboardHint.style.display = 'none'; }, 1000);
      }, 5000);
    }
  }

  // --- Presenter Notes ---
  toggleNotes() {
    this.notesVisible = !this.notesVisible;
    if (this.notesPanel) {
      this.notesPanel.classList.toggle('visible', this.notesVisible);
      this.notesPanel.setAttribute('aria-hidden', !this.notesVisible);
    }
    if (this.notesVisible) {
      this.updateNotes(this.currentSlide);
    }
  }

  updateNotes(index) {
    if (!this.notesPanel || !this.notesVisible) return;
    const slide = this.slides[index];
    const notes = slide ? slide.dataset.notes : '';
    this.notesPanel.textContent = notes || '(No presenter notes for this slide)';
  }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  new SlidePresentation();
});
```

## Slide HTML Structure

Each slide follows this general pattern:

```html
<section class="slide {{SLIDE_TYPE_CLASS}}" data-notes="{{OPTIONAL_PRESENTER_NOTES}}">
  <!-- Optional: Logo (typically on title and closing slides) -->
  <div class="slide__logo">
    {{W_CREST_SVG_INLINE}}
  </div>

  <div class="slide-content animate-in">
    <!-- Slide-type-specific content goes here -->
    <!-- See slide-types.md for each type's structure -->
  </div>
</section>
```

## Logo Embedding

Read the SVG files from the `assets/` directory and embed them directly as inline `<svg>` markup:

- **Light backgrounds**: Use `uw-crest-color.svg` (full-color W Crest with gold gradient shield)
- **Dark backgrounds**: Use `uw-crest-1color.svg` (single stroke path, set fill to white via CSS or inline style)
- **Favicon**: Use `favicon-w.svg` (simple W on red square), URI-encode it for the `<link rel="icon">` tag

To make the 1-color crest white on dark backgrounds, add `style="fill: #ffffff"` to the root `<svg>` element, or wrap it in a container with `color: #fff` and ensure the SVG paths use `currentColor`.

## Navigation Dots Generation

Generate one dot button per slide:

```html
<button class="nav-dot" aria-label="Go to slide 1" data-slide="0"></button>
<button class="nav-dot" aria-label="Go to slide 2" data-slide="1"></button>
<!-- ... one per slide -->
```

The first dot should have the `active` class added.
