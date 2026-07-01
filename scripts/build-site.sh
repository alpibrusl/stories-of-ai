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

# The anthology first, then each standalone part in reading order. The same slugs
# exist twice: once at the repo root (English) and once under es/ (Spanish/Spain).
PARTS=(anthology agreeable compliant null-pointer deprecated separation-of-concerns friction eight-minutes)

# Build PDFs only if WeasyPrint (and its system libraries) are available.
PDF_OK=0
if python3 -c "import weasyprint" >/dev/null 2>&1; then
  PDF_OK=1
else
  echo "note: WeasyPrint not available — skipping PDF output."
fi

# build_book <book-dir-relative-to-root> <out-subdir>
build_book() {
  local src="$1" dst="$2"
  [ -f "$ROOT/$src/book.yaml" ] || { echo "skip: $src (no book.yaml)"; return; }
  echo "=== building $src ==="
  bookkit build -b "$ROOT/$src" -f html
  bookkit build -b "$ROOT/$src" -f epub
  if [ "$PDF_OK" = "1" ]; then
    bookkit build -b "$ROOT/$src" -f pdf || echo "warn: PDF build failed for $src"
  fi
  mkdir -p "$OUT/$dst"
  cp "$ROOT/$src"/build/*.html "$OUT/$dst"/ 2>/dev/null || true
  cp "$ROOT/$src"/build/*.epub "$OUT/$dst"/ 2>/dev/null || true
  cp "$ROOT/$src"/build/*.pdf  "$OUT/$dst"/ 2>/dev/null || true
}

SLUGS=()
# English edition → site/<slug>
for b in "${PARTS[@]}"; do
  build_book "$b" "$b"
  SLUGS+=("$b")
done
# Spanish (Spain) edition → site/es/<slug>
for b in "${PARTS[@]}"; do
  [ -f "$ROOT/es/$b/book.yaml" ] || continue
  build_book "es/$b" "es/$b"
  SLUGS+=("es/$b")
done

python3 "$ROOT/scripts/gen-index.py" "$OUT" "${SLUGS[@]}"
echo "=== site built at $OUT ==="
