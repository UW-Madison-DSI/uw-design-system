#!/bin/bash
# Export a UW-Slides HTML presentation to PDF using Playwright.
# Each slide becomes one page in the PDF.
#
# Usage: export-pdf.sh <path-to-html> [output-pdf-path]
#
# Requires: npx playwright (or playwright installed globally)

HTML_FILE="${1:?Usage: export-pdf.sh <path-to-html> [output-pdf-path]}"
PDF_FILE="${2:-${HTML_FILE%.html}.pdf}"

if [ ! -f "$HTML_FILE" ]; then
  echo "Error: File not found: $HTML_FILE"
  exit 1
fi

# Convert to absolute path
HTML_FILE="$(cd "$(dirname "$HTML_FILE")" && pwd)/$(basename "$HTML_FILE")"
PDF_FILE="$(cd "$(dirname "$PDF_FILE")" 2>/dev/null && pwd)/$(basename "$PDF_FILE")" 2>/dev/null || PDF_FILE="$(pwd)/$(basename "$PDF_FILE")"

# Check for Playwright
if ! command -v npx &>/dev/null; then
  echo "Error: npx is required. Install Node.js first."
  exit 1
fi

echo "Exporting presentation to PDF..."
echo "  Input:  $HTML_FILE"
echo "  Output: $PDF_FILE"

# Use a Node.js script with Playwright to generate the PDF
node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.goto('file://${HTML_FILE}', { waitUntil: 'networkidle' });

  // Wait for fonts to load
  await page.waitForTimeout(2000);

  // Get the number of slides
  const slideCount = await page.evaluate(() => document.querySelectorAll('.slide').length);
  console.log('Found ' + slideCount + ' slides');

  // Generate PDF with print styles
  await page.pdf({
    path: '${PDF_FILE}',
    width: '1920px',
    height: '1080px',
    printBackground: true,
    preferCSSPageSize: false,
  });

  await browser.close();
  console.log('PDF exported successfully: ${PDF_FILE}');
})().catch(err => {
  console.error('Export failed:', err.message);
  console.error('Make sure Playwright is installed: npx playwright install chromium');
  process.exit(1);
});
" 2>&1

if [ $? -eq 0 ]; then
  echo "Done! PDF saved to: $PDF_FILE"
else
  echo ""
  echo "If Playwright is not installed, run:"
  echo "  npm install playwright"
  echo "  npx playwright install chromium"
  exit 1
fi
