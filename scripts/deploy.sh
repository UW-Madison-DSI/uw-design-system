#!/bin/bash
# Deploy a UW-Slides HTML presentation to Vercel for sharing.
#
# Usage: deploy.sh <path-to-html> [project-name]
#
# Requires: Vercel CLI (npm i -g vercel)

HTML_FILE="${1:?Usage: deploy.sh <path-to-html> [project-name]}"
PROJECT_NAME="${2:-uw-slides}"

if [ ! -f "$HTML_FILE" ]; then
  echo "Error: File not found: $HTML_FILE"
  exit 1
fi

# Check for Vercel CLI
if ! command -v vercel &>/dev/null; then
  echo "Error: Vercel CLI is required."
  echo "Install with: npm i -g vercel"
  exit 1
fi

# Create a temporary directory for deployment
DEPLOY_DIR=$(mktemp -d)
cp "$HTML_FILE" "$DEPLOY_DIR/index.html"

echo "Deploying presentation to Vercel..."
echo "  Source: $HTML_FILE"
echo "  Project: $PROJECT_NAME"

cd "$DEPLOY_DIR"
vercel --name "$PROJECT_NAME" --yes --prod 2>&1

RESULT=$?

# Clean up
rm -rf "$DEPLOY_DIR"

if [ $RESULT -eq 0 ]; then
  echo ""
  echo "Deployment complete! Your presentation is live."
else
  echo "Deployment failed. Make sure you're logged in: vercel login"
  exit 1
fi
