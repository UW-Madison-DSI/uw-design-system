#!/bin/bash
# Open a generated UW-Slides presentation in the default browser.
# Usage: open-presentation.sh <path-to-html>

FILE="${1:?Usage: open-presentation.sh <path-to-html>}"

if [ ! -f "$FILE" ]; then
  echo "Error: File not found: $FILE"
  exit 1
fi

if [[ "$(uname)" == "Darwin" ]]; then
  open "$FILE"
elif command -v xdg-open &>/dev/null; then
  xdg-open "$FILE"
elif command -v wslview &>/dev/null; then
  wslview "$FILE"
else
  echo "Generated: $FILE"
  echo "Open this file in a web browser to view the presentation."
fi
