# 08.09.2026

MSETCL **Asset Retirement, Scrap Declaration & Disposal Policy** — source documents and explainers built from them.

## Source documents

| File | What it is |
|---|---|
| `Policy.pdf` | The policy circular (13 pages, signed by Director (Operations)) |
| `MSA wardha new scrapping policy.pdf` | The 19-slide presentation of the same policy |
| `covering letter.pdf` | Covering letter from the Chief Engineer (Trans O&M), dated 02.12.2024 |

## Explainers (`docs/`)

| Document | Read it when | Markdown | HTML |
|---|---|---|---|
| **Flow charts** — the policy as 8 diagrammatic flow charts with document-trail and deadline tables | You want the process visually | [`docs/flowchart.md`](docs/flowchart.md) | [`docs/flowchart.html`](docs/flowchart.html) |
| **The Scrap Story** — from scratch, in plain language, with assumptions, examples and a 2-minute briefing script | You are new to the job, or you must explain it to your team | [`docs/story-guide.md`](docs/story-guide.md) | [`docs/story-guide.html`](docs/story-guide.html) |
| **The Finance Head at the Store** — responsibilities, verification points, how to verify, and formats F-1 to F-8 | You are the F&A officer handling the scrapping file | [`docs/finance-officer-guide.md`](docs/finance-officer-guide.md) | [`docs/finance-officer-guide.html`](docs/finance-officer-guide.html) |

- The **`.md`** files are the source of truth. GitHub renders them, **including the Mermaid diagrams**.
- The **`.html`** files are generated from the `.md` files — open them after cloning for a styled, scrollable, print-friendly version.

### Regenerating the HTML

```bash
python3 docs/build_html.py docs/flowchart.md docs/flowchart.html
python3 docs/build_html.py docs/story-guide.md docs/story-guide.html
python3 docs/build_html.py docs/finance-officer-guide.md docs/finance-officer-guide.html
```

Mermaid is loaded from `docs/vendor/mermaid.min.js` when present (offline use) and from the jsDelivr CDN otherwise; `docs/vendor/` is git-ignored, so a fresh clone uses the CDN.

## Known gap

Pages 14–15 of `Policy.pdf` — the table of **Competent Authority / financial powers under GO No. 1 (F&A)** — are a scanned image with no extractable text. Read it from the original PDF before signing any approval.
