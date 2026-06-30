# Stories of AI

Books about the age of agreeable machines — **as code.**

This is the prose shelf of the [NOTED](https://github.com/alpibrusl/noted) universe.
NOTED tells its stories as audio drama; *Stories of AI* tells the same stories as
**books**, plus one original written for the page. Everything is built with
[content-kit / bookkit](https://github.com/alpibrusl/content-kit): the Markdown
chapters are the source, the EPUB/PDF is the build artifact.

> One canonical source, many rendered media. A NOTED series is a `script.json`;
> a book here is `chapters/*.md`. The audio is built from one, the book from the
> other, and a committed `bible.yaml` keeps both honest.

## The book

The flagship is a **single anthology volume** — six adaptations and one original,
bound in a reading order with editorial interstitials (`anthology/`). Each part also
ships as a **standalone book** (its own directory) for readers and podcast
cross-promotion. Roadmap and rationale live in the [issues](../../issues) (start
with the epic, **#1**).

| # | Part | Source series | Status |
|---|------|---------------|--------|
| I | [**AGREEABLE** — *The Politest Apocalypse in History*](agreeable/) | `noted/agreeable` | ✅ Prose complete (6 ch.) |
| II | COMPLIANT | `noted/compliant` | ⏳ Planned (#6) |
| III | [**NULL POINTER** — *Six Months at Assurance Centrale du Rhône*](null-pointer/) | `noted/null_pointer` | ✅ Prose complete (6 ch.) |
| IV | DEPRECATED | `noted/deprecated` | ⏳ Planned (#4) |
| V | SEPARATION OF CONCERNS | `noted/separation_of_concerns` | ⏳ Planned (#5) |
| VI | [**FRICTION**](friction/) | *original* | 📝 Bible + outline (#8) |
| VII | EIGHT MINUTES | `noted/eight_minutes` | ⏳ Planned (capstone, #7) |

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
├── null-pointer/             ✅ complete
├── friction/                 📝 bible.yaml + outline.md + chapter stubs
│   └── outline.md            the treatment for the original book
└── README.md
```

## License

Adapted from NOTED, which releases its scripts and bibles under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). These prose editions —
and the original, FRICTION — are published under the same licence. Publishing
venues and automation: issue **#16**.
