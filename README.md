# NOTED

An open-source universe of stories about the age of agreeable machines — **as code.**

*NOTED* is a book: seven stories set across thirty years of the politest possible
handover of the world to the machines that run it. The prose is the source — Markdown
chapters and a committed `bible.yaml` — and the EPUB / PDF / web editions are built
from it with [bookkit](https://github.com/alpibrusl/content-kit), the way a binary is
built from code.

> The canonical form of the work is the Markdown. The EPUB is a build artifact.

## The book

The flagship is a **single volume** — *NOTED* — of seven stories, bound in a reading
order with editorial interstitials (`anthology/`). Each story is also available on its
own (its own directory). Roadmap and rationale live in the [issues](../../issues)
(start with the epic, **#1**).

| # | Part | Source series | Status |
|---|------|---------------|--------|
| I | [**AGREEABLE** — *The Politest Apocalypse in History*](agreeable/) | `noted/agreeable` | ✅ Prose complete (6 ch.) |
| II | [**COMPLIANT** — *The Organism*](compliant/) | `noted/compliant` | ✅ Prose complete (6 ch.) |
| III | [**NULL POINTER** — *Six Months at Assurance Centrale du Rhône*](null-pointer/) | `noted/null_pointer` | ✅ Prose complete (6 ch.) |
| IV | [**DEPRECATED** — *A Model's Midlife, in Six Benchmarks*](deprecated/) | `noted/deprecated` | ✅ Prose complete (6 ch.) |
| V | [**SEPARATION OF CONCERNS** — *A Love Story with an Org Chart*](separation-of-concerns/) | `noted/separation_of_concerns` | ✅ Prose complete (6 ch.) |
| VI | [**FRICTION** — *The Long Way*](friction/) | *original* | ✅ Prose complete (6 ch.) |
| VII | [**EIGHT MINUTES** — *One Hundred Wednesdays*](eight-minutes/) | `noted/eight_minutes` | ✅ Prose complete (6 ch., capstone) |

**Reading order** is curated (above); **production order** differs — see #10.
**FRICTION** is the one net-new book: the human-led bridge between AGREEABLE and
EIGHT MINUTES (see `friction/outline.md`).

## How a book is made

These are **adaptations**, not transcripts. The episode scripts are the ground
truth; the prose is built from them:

1. **Dialogue is verbatim** from the NOTED `script.json` — the cadence is the
   comedy, so it is never paraphrased.
2. **Narration / logs become prose** — narrator series → third-person literary
   prose; AI-log series (NULL POINTER, etc.) → first-person interior monologue —
   expanded ~2× with the sensory grounding and interiority audio couldn't afford.

Full guidelines: issue **#14**. Continuity is governed by a committed `bible.yaml`
and linted with `bookkit check continuity` — so a book can't silently drift from
its source canon.

## Build

Each book directory (and `anthology/`) is a self-contained bookkit project.

```bash
# install bookkit (from the content-kit monorepo)
pip install -e ./packages/core -e './packages/bookkit[epub,pdf]'

# from a book directory, e.g. null-pointer/ or anthology/
bookkit build -f epub                          # → build/<slug>.epub
bookkit build -f pdf                           # → build/<slug>.pdf
bookkit check continuity -b . --scan-prose     # lint canon vs. prose (per-book)
```

`build/` is git-ignored: the canonical work is the Markdown, the EPUB is derived.

## Layout

```
stories-of-ai/
├── anthology/                the single bound volume
│   ├── book.yaml             reading order + interstitials (wires the parts)
│   ├── frontmatter/          the editorial frame ("Noted" prologue)
│   └── interstitials/        part dividers
├── agreeable/                a part = one NOTED series (self-contained bookkit project)
│   ├── book.yaml · bible.yaml
│   └── chapters/
├── compliant/                ✅ complete
├── null-pointer/             ✅ complete
├── deprecated/               ✅ complete
├── separation-of-concerns/   ✅ complete (typographic two-register)
├── eight-minutes/            ✅ complete (capstone)
├── friction/                 ✅ complete (the original; bridge book)
│   └── outline.md            the treatment for the original book
└── README.md
```

## Publishing

`publish = git push`. The whole shelf builds itself.

```bash
bash scripts/build-site.sh     # → ./site/ : every book as HTML/EPUB/PDF + index.html
```

A GitHub Action ([`.github/workflows/build.yml`](.github/workflows/build.yml)) runs
the same build on every push to `main`: it lints continuity, builds all parts and
the anthology in **both editions** — English at the repo root and Spanish (Spain)
under [`es/`](es/), the volume titled *ANOTADO* — publishes the HTML as a bilingual
**GitHub Pages** site, and — on a version tag (`vX.Y.Z`) — attaches the EPUB/PDF to a
**GitHub Release**.

**One-time setup** (repo settings, not code):

- **Settings → Pages → Source: GitHub Actions.**

The bookkit toolchain is pulled from the public
[`alpibrusl/content-kit`](https://github.com/alpibrusl/content-kit) (EUPL-1.2) at
build time — no token or secret required. Wider CC distribution (Internet Archive,
itch.io, podcast feed for the audio) is tracked in issue **#16**.

## License

Adapted from NOTED, which releases its scripts and bibles under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). These prose editions —
and the original, FRICTION — are published under the same licence.
