#!/usr/bin/env bash
#
# Build every book (and the anthology) into ./site/ — one folder per title, each
# with its HTML / EPUB / (PDF if available) — plus a generated index.html.
#
# The canonical source is the Markdown; everything under site/ is a build artifact
# (git-ignored). Run locally, or in CI (see .github/workflows/build.yml).
#
# Usage:  bash scripts/build-site.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
OUT="$ROOT/site"
rm -rf "$OUT"
mkdir -p "$OUT"

# The anthology first, then each standalone part in reading order.
BOOKS=(anthology agreeable compliant null-pointer deprecated separation-of-concerns friction eight-minutes)

# Build PDFs only if WeasyPrint (and its system libraries) are available.
PDF_OK=0
if python3 -c "import weasyprint" >/dev/null 2>&1; then
  PDF_OK=1
else
  echo "note: WeasyPrint not available — skipping PDF output."
fi

for b in "${BOOKS[@]}"; do
  [ -f "$ROOT/$b/book.yaml" ] || { echo "skip: $b (no book.yaml)"; continue; }
  echo "=== building $b ==="
  bookkit build -b "$ROOT/$b" -f html
  bookkit build -b "$ROOT/$b" -f epub
  if [ "$PDF_OK" = "1" ]; then
    bookkit build -b "$ROOT/$b" -f pdf || echo "warn: PDF build failed for $b"
  fi
  mkdir -p "$OUT/$b"
  cp "$ROOT/$b"/build/*.html "$OUT/$b"/ 2>/dev/null || true
  cp "$ROOT/$b"/build/*.epub "$OUT/$b"/ 2>/dev/null || true
  cp "$ROOT/$b"/build/*.pdf  "$OUT/$b"/ 2>/dev/null || true
done

python3 "$ROOT/scripts/gen-index.py" "$OUT" "${BOOKS[@]}"
echo "=== site built at $OUT ==="
