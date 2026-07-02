#!/usr/bin/env python3
"""Generate site/index.html and inject SEO / Open Graph metadata across the site.

For every built book (site/<slug>/) this:
  - copies the book's cover to site/<slug>/cover.png (for absolute og:image URLs),
  - injects <meta description>, canonical, Open Graph, Twitter card and JSON-LD
    (schema.org/Book) into each rendered HTML page,
and for the site as a whole writes a bilingual index.html, a sitemap.xml and a
robots.txt. Pure stdlib + pyyaml (already a bookkit dependency).

Usage: gen-index.py <site_dir> <slug> [<slug> ...]
"""
from __future__ import annotations

import html
import shutil
import sys
from pathlib import Path

import yaml

SITE = Path(sys.argv[1])
SLUGS = sys.argv[2:]
ROOT = Path(__file__).resolve().parent.parent

BASE_URL = "https://alpibrusl.github.io/stories-of-ai"
SITE_NAME = "NOTED"
AUTHOR = "Alfonso Sastre Bruno"
CC_URL = "https://creativecommons.org/licenses/by/4.0/"

GENERIC_EN = ("Part of NOTED — an open-source cycle of stories about the age of "
              "agreeable machines. Free to read; licensed CC BY 4.0.")
GENERIC_ES = ("Parte de ANOTADO — un ciclo de relatos de código abierto sobre la "
              "era de las máquinas complacientes. Lectura gratuita; CC BY 4.0.")
INDEX_DESC = ("Seven linked stories about an AI future that arrives not by force "
              "but by consent — capture without a coup. Free, CC BY 4.0. Also in "
              "Spanish, as ANOTADO.")


def book_meta(slug: str) -> dict:
    cfg = ROOT / slug / "book.yaml"
    data = yaml.safe_load(cfg.read_text(encoding="utf-8")) if cfg.exists() else {}
    return data or {}


def is_es(slug: str) -> bool:
    return slug.startswith("es/")


def copy_cover(slug: str, meta: dict) -> str | None:
    """Copy the book's cover into site/<slug>/cover.png; return absolute URL or None."""
    cover = meta.get("cover")
    if not cover:
        return None
    src = (ROOT / slug / cover).resolve()
    if not src.exists():
        return None
    dst = SITE / slug / "cover.png"
    shutil.copyfile(src, dst)
    return f"{BASE_URL}/{slug}/cover.png"


def meta_tags(*, title, desc, url, image, lang, og_type) -> str:
    t, d = html.escape(title), html.escape(desc)
    locale = "es_ES" if lang == "es" else "en_US"
    tags = [
        f'<meta name="description" content="{d}">',
        f'<link rel="canonical" href="{url}">',
        f'<meta property="og:type" content="{og_type}">',
        f'<meta property="og:site_name" content="{SITE_NAME}">',
        f'<meta property="og:title" content="{t}">',
        f'<meta property="og:description" content="{d}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:locale" content="{locale}">',
    ]
    if image:
        tags += [
            f'<meta property="og:image" content="{image}">',
            '<meta property="og:image:width" content="1600">',
            '<meta property="og:image:height" content="2400">',
            f'<meta property="og:image:alt" content="{t} — cover">',
        ]
    # Portrait covers crop badly in large cards, so use the square "summary" card.
    tags.append('<meta name="twitter:card" content="summary">')
    tags += [
        f'<meta name="twitter:title" content="{t}">',
        f'<meta name="twitter:description" content="{d}">',
    ]
    if image:
        tags.append(f'<meta name="twitter:image" content="{image}">')
    return "\n".join(tags)


def book_jsonld(*, title, url, image, lang) -> str:
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "Book",
        "name": title,
        "author": {"@type": "Person", "name": AUTHOR},
        "inLanguage": lang,
        "license": CC_URL,
        "isAccessibleForFree": True,
        "url": url,
    }
    if image:
        data["image"] = image
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def inject_head(page_path: Path, block: str) -> None:
    txt = page_path.read_text(encoding="utf-8")
    if "og:title" in txt:  # idempotent
        return
    if "</head>" in txt:
        txt = txt.replace("</head>", block + "\n</head>", 1)
        page_path.write_text(txt, encoding="utf-8")


def process_book(slug: str) -> None:
    meta = book_meta(slug)
    title = str(meta.get("title", slug))
    subtitle = str(meta.get("subtitle", "") or "")
    lang = "es" if is_es(slug) else "en"
    generic = GENERIC_ES if is_es(slug) else GENERIC_EN
    desc = f"{subtitle} — {generic}" if subtitle else generic
    image = copy_cover(slug, meta)
    for page in sorted((SITE / slug).glob("*.html")):
        url = f"{BASE_URL}/{slug}/{page.name}"
        block = (
            meta_tags(title=title, desc=desc, url=url, image=image, lang=lang,
                      og_type="book")
            + "\n" + book_jsonld(title=title, url=url, image=image, lang=lang)
        )
        inject_head(page, block)


# ---- links + index rows --------------------------------------------------

def links(slug: str) -> list[str]:
    read = "Leer online" if is_es(slug) else "Read online"
    out = []
    for ext, label in (("html", read), ("epub", "EPUB"), ("pdf", "PDF")):
        hits = sorted(p for p in (SITE / slug).glob(f"*.{ext}"))
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


# ---- run: per-book SEO, then index, sitemap, robots ----------------------

for slug in SLUGS:
    if (SITE / slug).is_dir():
        process_book(slug)

en_rows = [r for slug in SLUGS if not is_es(slug) and (r := row_for(slug))]
es_rows = [r for slug in SLUGS if is_es(slug) and (r := row_for(slug))]

sections = [f'<ul>\n{chr(10).join(en_rows)}\n</ul>']
if es_rows:
    sections.append(
        '<h2 class="lang">Español (España)</h2>'
        f'<ul>\n{chr(10).join(es_rows)}\n</ul>'
    )
body_sections = "\n".join(sections)
n_books = len(en_rows) + len(es_rows)

index_image = f"{BASE_URL}/anthology/cover.png"
index_meta = meta_tags(
    title="NOTED — stories about the age of agreeable machines",
    desc=INDEX_DESC, url=f"{BASE_URL}/", image=index_image, lang="en",
    og_type="website",
)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NOTED — stories about the age of agreeable machines</title>
{index_meta}
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
     href="{CC_URL}">CC BY 4.0</a> — share and adapt freely, with attribution.</p>
</footer>
</body>
</html>
"""

(SITE / "index.html").write_text(page, encoding="utf-8")

# sitemap.xml — index + every rendered HTML page
urls = [f"{BASE_URL}/"]
for slug in SLUGS:
    d = SITE / slug
    if d.is_dir():
        urls += [f"{BASE_URL}/{slug}/{p.name}" for p in sorted(d.glob("*.html"))]
sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    + "</urlset>\n"
)
(SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")

(SITE / "robots.txt").write_text(
    f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n", encoding="utf-8"
)

print(f"wrote {SITE / 'index.html'} ({n_books} books), sitemap.xml ({len(urls)} urls), robots.txt")
