# Stories of AI

Books about the age of agreeable machines — **as code.**

This is the prose shelf of the [NOTED](https://github.com/alpibrusl/noted) universe.
NOTED tells its stories as audio drama; *Stories of AI* tells the same stories as
**books**. Each book is novelized from a NOTED series and built with
[content-kit / bookkit](https://github.com/alpibrusl/content-kit): the Markdown
chapters are the source, the EPUB/PDF is the build artifact.

> One canonical source, many rendered media. A NOTED series is a `script.json`;
> a book here is `chapters/*.md`. The audio is built from one, the EPUB from the
> other, and a committed `bible.yaml` keeps both honest.

## The shelf

| Book | Source series | Status |
|------|---------------|--------|
| [**AGREEABLE** — *The Politest Apocalypse in History*](agreeable/) | [`noted/agreeable`](https://github.com/alpibrusl/noted/tree/main/agreeable) | ✅ Pilot — 6 chapters |
| COMPLIANT | `noted/compliant` | planned |
| EIGHT MINUTES | `noted/eight_minutes` | planned |
| NULL POINTER | `noted/null_pointer` | planned |
| DEPRECATED | `noted/deprecated` | planned |
| SEPARATION OF CONCERNS | `noted/separation_of_concerns` | planned |

Each NOTED series has its own cast and arc, so each becomes a **standalone book**
(one book per series) rather than chapters of a single anthology.

## How a book is made

These are **adaptations**, not transcripts. The episode scripts are the ground
truth; the prose is built from them in two passes:

1. **Faithful scaffold.** Every line of dialogue is carried over verbatim from the
   NOTED `script.json` — the comedy lives in ARIA's exact cadence, so it is never
   paraphrased.
2. **Prose pass.** The screenplay's stage-direction narration is adapted into
   continuous prose, with light interiority consistent with the series bible. No
   new plot is invented; the `bible.yaml` is the contract.

Continuity is governed by a committed `bible.yaml` (characters, world, timeline,
per-chapter beats) and linted with `bookkit check continuity` — so a book cannot
silently drift from its source canon.

## Build a book

Each book directory is a self-contained bookkit project.

```bash
# install bookkit (from the content-kit monorepo)
pip install -e ./packages/core -e './packages/bookkit[epub,pdf]'

# from a book directory, e.g. agreeable/
bookkit build -f epub                 # → build/agreeable.epub
bookkit build -f pdf                  # → build/agreeable.pdf
bookkit check continuity -b . --scan-prose   # lint canon vs. prose
```

The `build/` directory is git-ignored: the canonical work is the Markdown, the
EPUB is derived from it the way a binary is derived from source.

## Layout

```
stories-of-ai/
├── agreeable/                 a book = one NOTED series
│   ├── book.yaml              metadata, theme, chapter order
│   ├── bible.yaml             committed canon (continuity contract)
│   ├── chapters/
│   │   ├── 01-just-to-confirm.md
│   │   └── … 06-thank-you-for-your-patience.md
│   └── build/                 EPUB/PDF/HTML — generated, git-ignored
└── README.md
```

## License

Text is adapted from NOTED, which releases its scripts and bibles under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). These prose editions
are published under the same licence — share and adapt freely with attribution.
