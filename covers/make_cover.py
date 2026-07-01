#!/usr/bin/env python3
"""Generate the NOTED covers — one per book + the anthology.

Minimal, typographic, administrative: a framed dossier with quiet corner
annotations (REF / STATUS: NOTED) and the title set large. No imagery. Titles
auto-fit and wrap so long ones (e.g. SEPARATION OF CONCERNS) stay balanced.

Run: python covers/make_cover.py   →   covers/<slug>.png for every book.
"""
from __future__ import annotations

import pathlib
import yaml
import cairosvg

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "covers"

W, H = 1600, 2400
BG, INK, GREY, FAINT, RULE = "#f2efe6", "#1b1915", "#55514a", "#8f8a7e", "#b9b3a4"
MAXW = 1200  # title measure box

# anthology first, then the seven parts in reading order
BOOKS = [
    ("anthology", "noted", "REF 001–VII"),
    ("agreeable", "agreeable", "REF I / VII"),
    ("compliant", "compliant", "REF II / VII"),
    ("null-pointer", "null-pointer", "REF III / VII"),
    ("deprecated", "deprecated", "REF IV / VII"),
    ("separation-of-concerns", "separation-of-concerns", "REF V / VII"),
    ("friction", "friction", "REF VI / VII"),
    ("eight-minutes", "eight-minutes", "REF VII / VII"),
]


def _width(text: str, size: float) -> float:
    # rough advance for Liberation Serif caps incl. letter-spacing (~0.09em)
    n = len(text)
    return n * size * 0.60 + max(n - 1, 0) * size * 0.09


def layout_title(title: str, cap: float = 270.0):
    """Return (lines, font_size) that fit MAXW, wrapping to two lines if needed."""
    def size_for(lines):
        longest = max(_width(l, 1.0) for l in lines)  # width at size 1
        return MAXW / longest
    one = min(cap, size_for([title]))
    if one >= 150 or len(title.split()) == 1:
        return [title], one
    words = title.split()
    best = None
    for i in range(1, len(words)):
        lines = [" ".join(words[:i]), " ".join(words[i:])]
        s = min(cap * 0.75, size_for(lines))
        if best is None or s > best[1]:
            best = (lines, s)
    return best


def svg_for(title: str, subtitle: str, ref: str) -> str:
    lines, size = layout_title(title)
    spacing = round(size * 0.095, 1)
    lh = size * 1.02
    top = 1070 - (len(lines) - 1) * lh / 2   # vertically centre the title block
    title_svg = "".join(
        f'<text x="800" y="{round(top + i*lh)}" text-anchor="middle" '
        f'font-family="Liberation Serif, serif" font-size="{round(size)}" '
        f'letter-spacing="{spacing}" fill="{INK}">{ln}</text>'
        for i, ln in enumerate(lines)
    )
    sub_y = round(top + (len(lines) - 1) * lh + size * 0.42 + 96)
    rule_y = sub_y - 84
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect x="110" y="110" width="1380" height="2180" fill="none" stroke="{INK}" stroke-width="1.5"/>
  <rect x="126" y="126" width="1348" height="2148" fill="none" stroke="{INK}" stroke-width="0.75"/>
  <text x="168" y="214" font-family="Liberation Mono, monospace" font-size="26" letter-spacing="3" fill="{FAINT}">{ref}</text>
  <text x="1432" y="214" text-anchor="end" font-family="Liberation Mono, monospace" font-size="26" letter-spacing="3" fill="{FAINT}">STATUS: NOTED</text>
  <line x1="168" y1="250" x2="1432" y2="250" stroke="{RULE}" stroke-width="1"/>
  {title_svg}
  <line x1="700" y1="{rule_y}" x2="900" y2="{rule_y}" stroke="{INK}" stroke-width="2"/>
  <text x="800" y="{sub_y}" text-anchor="middle" font-family="Liberation Serif, serif" font-style="italic" font-size="42" fill="{GREY}">{subtitle}</text>
  <line x1="168" y1="2010" x2="1432" y2="2010" stroke="{RULE}" stroke-width="1"/>
  <text x="800" y="2096" text-anchor="middle" font-family="Liberation Serif, serif" font-size="42" letter-spacing="8" fill="{INK}">ALFONSO SASTRE BRUNO</text>
  <text x="800" y="2168" text-anchor="middle" font-family="Liberation Mono, monospace" font-size="24" letter-spacing="5" fill="{FAINT}">CC BY 4.0</text>
</svg>"""


for book_dir, slug, ref in BOOKS:
    cfg = yaml.safe_load((ROOT / book_dir / "book.yaml").read_text(encoding="utf-8"))
    title = str(cfg.get("title", slug)).upper()
    subtitle = str(cfg.get("subtitle", "") or "")
    svg = svg_for(title, subtitle, ref)
    cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                     write_to=str(OUT / f"{slug}.png"),
                     output_width=W, output_height=H)
    print("wrote", OUT / f"{slug}.png", f"({title})")
