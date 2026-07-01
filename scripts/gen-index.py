#!/usr/bin/env python3
"""Generate site/index.html — a simple landing page linking every built book.

Reads each book's book.yaml for its title/subtitle and lists the HTML / EPUB / PDF
that build-site.sh produced under site/<slug>/. Pure stdlib + pyyaml (already a
bookkit dependency). Usage: gen-index.py <site_dir> <slug> [<slug> ...]
"""
from __future__ import annotations

import html
import sys
from pathlib import Path

import yaml

SITE = Path(sys.argv[1])
SLUGS = sys.argv[2:]
ROOT = Path(__file__).resolve().parent.parent


def book_meta(slug: str) -> dict:
    cfg = ROOT / slug / "book.yaml"
    data = yaml.safe_load(cfg.read_text(encoding="utf-8")) if cfg.exists() else {}
    return data or {}


def links(slug: str) -> list[str]:
    read = "Leer online" if slug.startswith("es/") else "Read online"
    out = []
    for ext, label in (("html", read), ("epub", "EPUB"), ("pdf", "PDF")):
        hits = sorted((SITE / slug).glob(f"*.{ext}"))
        if hits:
            href = f"{slug}/{hits[0].name}"
            out.append(f'<a href="{html.escape(href)}">{label}</a>')
    return out


def row_for(slug: str) -> str | None:
    if not (SITE / slug).is_dir():
        return None
    meta = book_meta(slug)
    title = html.escape(str(meta.get("title", slug)))
    subtitle = html.escape(str(meta.get("subtitle", "") or ""))
    featured = " featured" if slug in ("anthology", "es/anthology") else ""
    sub_html = f'<p class="sub">{subtitle}</p>' if subtitle else ""
    link_html = " · ".join(links(slug)) or "<em>not built</em>"
    return (
        f'<li class="book{featured}">'
        f"<h2>{title}</h2>{sub_html}"
        f'<p class="links">{link_html}</p></li>'
    )


en_rows = [r for slug in SLUGS if not slug.startswith("es/") and (r := row_for(slug))]
es_rows = [r for slug in SLUGS if slug.startswith("es/") and (r := row_for(slug))]

sections = [f'<ul>\n{chr(10).join(en_rows)}\n</ul>']
if es_rows:
    sections.append(
        '<h2 class="lang">Español (España)</h2>'
        f'<ul>\n{chr(10).join(es_rows)}\n</ul>'
    )
body_sections = "\n".join(sections)
n_books = len(en_rows) + len(es_rows)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NOTED</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 46rem;
         margin: 0 auto; padding: 3rem 1.25rem 5rem; line-height: 1.5; }}
  header p {{ color: #666; }}
  ul {{ list-style: none; padding: 0; }}
  .book {{ border-top: 1px solid #ccc; padding: 1.3rem 0; }}
  .book h2 {{ margin: 0; font-size: 1.3rem; }}
  .book.featured h2 {{ font-size: 1.7rem; }}
  h2.lang {{ margin: 2.5rem 0 0; font-size: 1rem; letter-spacing: .12em;
             text-transform: uppercase; color: #888;
             font-family: -apple-system, system-ui, sans-serif; }}
  .sub {{ margin: .2rem 0 .4rem; color: #777; font-style: italic; }}
  .links a {{ text-decoration: none; border-bottom: 1px solid currentColor; }}
  .links {{ font-family: -apple-system, system-ui, sans-serif; font-size: .9rem; }}
  footer {{ margin-top: 3rem; color: #888; font-size: .85rem;
            font-family: -apple-system, system-ui, sans-serif; }}
</style>
</head>
<body>
<header>
  <h1>NOTED</h1>
  <p>An open-source universe of stories about the age of agreeable machines.
     Also available in Spanish, as <em>ANOTADO</em>.</p>
</header>
{body_sections}
<footer>
  <p>The flagship is the single anthology volume; each story is also available on its
     own. Read online, or download the EPUB or PDF. Licensed <a
     href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> — share and
     adapt freely, with attribution.</p>
</footer>
</body>
</html>
"""

(SITE / "index.html").write_text(page, encoding="utf-8")
print(f"wrote {SITE / 'index.html'} ({n_books} books)")
