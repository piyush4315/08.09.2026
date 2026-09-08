#!/usr/bin/env python3
"""Render docs/flowchart.md into a self-contained docs/flowchart.html.

The markdown file is the source of truth; this script only wraps it in a
styled page and turns ```mermaid blocks into live diagrams (Mermaid is
vendored in docs/vendor/mermaid.min.js, with a CDN fallback).

Usage:  python3 docs/build_html.py
"""

import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MD = HERE / "flowchart.md"
OUT = HERE / "flowchart.html"


def inline(text: str) -> str:
    """Very small markdown inline formatter (bold, italic, code, br)."""
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    # Mermaid labels / policy text intentionally use HTML entities such as &amp;
    text = text.replace("&amp;lt;", "&lt;").replace("&amp;gt;", "&gt;").replace("&amp;amp;", "&amp;")
    return text


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "section"


def convert(md: str) -> str:
    lines = md.split("\n")
    out, i = [], 0
    n = len(lines)

    def flush_list(items, ordered):
        tag = "ol" if ordered else "ul"
        body = "".join(f"<li>{inline(x)}</li>" for x in items)
        out.append(f"<{tag}>{body}</{tag}>")

    while i < n:
        line = lines[i]

        # fenced code block
        if line.startswith("```"):
            lang = line[3:].strip()
            i += 1
            code = []
            while i < n and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            if lang == "mermaid":
                out.append('<div class="diagram"><pre class="mermaid">\n'
                           + "\n".join(code)
                           + "\n</pre></div>")
            else:
                out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            if level == 1:
                out.append(f'<h1 id="{slug(text)}">{inline(text)}</h1>')
            else:
                out.append(f'<h{level} id="{slug(text)}">{inline(text)}</h{level}>')
            i += 1
            continue

        if not line.strip():
            i += 1
            continue

        if re.match(r"^\s*(---|\*\*\*)\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # blockquote
        if line.startswith(">"):
            buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>")
            continue

        # table
        if line.strip().startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "".join(f"<th>{inline(c)}</th>" for c in header)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in rows
            )
            out.append(f'<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>')
            continue

        # lists
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            items = []
            while i < n and re.match(r"^\s*[-*]\s+(.*)$", lines[i]):
                items.append(re.match(r"^\s*[-*]\s+(.*)$", lines[i]).group(1))
                i += 1
            flush_list(items, ordered=False)
            continue

        m = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if m:
            items = []
            while i < n and re.match(r"^\s*\d+[.)]\s+(.*)$", lines[i]):
                items.append(re.match(r"^\s*\d+[.)]\s+(.*)$", lines[i]).group(1))
                i += 1
            flush_list(items, ordered=True)
            continue

        # paragraph
        buf = []
        while i < n and lines[i].strip() and not re.match(
            r"^\s*(#{1,6}\s|```|>|[-*]\s|\d+[.)]\s|\|)", lines[i]
        ):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>")

    return "\n".join(out)


CSS = """
:root{
  --ink:#1a2330; --muted:#5a6b7f; --line:#dde4ec; --bg:#f6f8fb; --card:#ffffff;
  --accent:#1565c0; --accent2:#6a1b9a;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
.wrap{max-width:1180px; margin:0 auto; padding:32px 24px 96px}
header.hero{
  background:linear-gradient(135deg,#0d47a1 0%,#1565c0 45%,#6a1b9a 100%);
  color:#fff; padding:44px 24px 38px; border-radius:0 0 18px 18px;
  box-shadow:0 8px 30px rgba(21,101,192,.25);
}
header.hero .inner{max-width:1180px; margin:0 auto}
header.hero h1{margin:0 0 8px; font-size:30px; letter-spacing:.2px}
header.hero p{margin:0; opacity:.93; font-size:16px}
header.hero .chips{margin-top:18px; display:flex; flex-wrap:wrap; gap:8px}
header.hero .chip{
  background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.28);
  padding:5px 12px; border-radius:999px; font-size:13px;
}
nav.toc{
  position:sticky; top:0; z-index:20; background:rgba(255,255,255,.96);
  backdrop-filter:blur(6px); border-bottom:1px solid var(--line);
}
nav.toc .inner{max-width:1180px; margin:0 auto; padding:10px 24px; display:flex; gap:6px; flex-wrap:wrap}
nav.toc a{
  font-size:13px; color:var(--muted); text-decoration:none; padding:4px 10px;
  border-radius:999px; border:1px solid transparent; white-space:nowrap;
}
nav.toc a:hover{background:#eef3fa; color:var(--accent); border-color:#cfe0f5}
h1{font-size:30px; margin:8px 0 6px}
h2{
  font-size:22px; margin:44px 0 14px; padding:14px 18px; background:var(--card);
  border-left:5px solid var(--accent); border-radius:8px; box-shadow:0 1px 3px rgba(16,32,64,.07);
}
h3{font-size:18px; margin:26px 0 8px; color:var(--accent)}
p{margin:10px 0}
blockquote{
  margin:16px 0; padding:14px 18px; background:#eef3fa; border-left:5px solid var(--accent2);
  border-radius:8px; color:#2b3a4d;
}
.diagram{
  background:var(--card); border:1px solid var(--line); border-radius:12px;
  padding:18px 12px; margin:18px 0 22px; overflow-x:auto;
  box-shadow:0 2px 10px rgba(16,32,64,.06);
}
pre.mermaid{margin:0; text-align:center; background:transparent}
pre.mermaid svg{max-width:100%; height:auto}
table{border-collapse:collapse; width:100%; margin:16px 0; background:var(--card);
  border-radius:10px; overflow:hidden; box-shadow:0 1px 3px rgba(16,32,64,.07); font-size:14.5px}
th{background:#eef3fa; text-align:left; padding:11px 13px; font-size:13px;
  text-transform:uppercase; letter-spacing:.04em; color:#3b4d63; border-bottom:2px solid var(--line)}
td{padding:10px 13px; border-bottom:1px solid var(--line); vertical-align:top}
tr:last-child td{border-bottom:none}
ul,ol{margin:10px 0 10px 6px; padding-left:22px}
li{margin:5px 0}
code{background:#eef3fa; padding:1px 6px; border-radius:5px; font-size:14px; color:#0d47a1}
hr{border:none; border-top:1px solid var(--line); margin:34px 0}
footer{max-width:1180px; margin:0 auto; padding:0 24px 40px; color:var(--muted); font-size:13px}
@media print{
  body{background:#fff}
  nav.toc{display:none}
  .diagram{break-inside:avoid; box-shadow:none}
  h2{box-shadow:none}
}
"""

JS = """
const start = () => {
  mermaid.initialize({
    startOnLoad: true,
    securityLevel: 'loose',
    theme: 'base',
    flowchart: { curve: 'basis', useMaxWidth: true, htmlLabels: true, nodeSpacing: 34, rankSpacing: 46 },
    themeVariables: {
      fontFamily: '-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif',
      fontSize: '15px', primaryColor: '#eef4fb', primaryBorderColor: '#90b4dd',
      primaryTextColor: '#1a2330', lineColor: '#7d90a6', secondaryColor: '#f4f0f8',
      tertiaryColor: '#f7f9fc', edgeLabelBackground: '#ffffff'
    }
  });
  mermaid.run({ querySelector: 'pre.mermaid' });
};
if (window.mermaid) { start(); } else { document.addEventListener('DOMContentLoaded', start); }
"""


def build_toc(md: str) -> str:
    items = []
    for line in md.split("\n"):
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1))
            label = re.sub(r"^\d+\.\s*", "", title)
            items.append(f'<a href="#{slug(title)}">{html.escape(label)}</a>')
    return "\n".join(items)


def main() -> None:
    md = MD.read_text(encoding="utf8")
    body = convert(md)
    toc = build_toc(md)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MSETCL Asset Retirement, Scrap Declaration &amp; Disposal Policy — Flow Charts</title>
<style>{CSS}</style>
</head>
<body>
<header class="hero">
  <div class="inner">
    <h1>MSETCL — Asset Retirement, Scrap Declaration &amp; Disposal Policy</h1>
    <p>The complete policy, explained as flow charts. Built from <code>Policy.pdf</code> and
       <code>MSA wardha new scrapping policy.pdf</code> in this repository.</p>
    <div class="chips">
      <span class="chip">Part 1 — Asset Retirement</span>
      <span class="chip">Part 2 — Scrap Declaration &amp; Disposal</span>
      <span class="chip">CLARC → ZSC → CO R&amp;D → Competent Authority → MSTC</span>
      <span class="chip">6 flow charts + responsibility &amp; timeline tables</span>
    </div>
  </div>
</header>

<nav class="toc"><div class="inner">
{toc}
</div></nav>

<main class="wrap">
{body}
</main>

<footer>
  Generated by <code>docs/build_html.py</code> from <code>docs/flowchart.md</code>.
  Mermaid is loaded from <code>docs/vendor/mermaid.min.js</code> (offline) with a CDN fallback.
</footer>

<script src="vendor/mermaid.min.js"></script>
<script>
if (!window.mermaid) {{
  document.write('<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"><\\/script>');
}}
</script>
<script>{JS}</script>
</body>
</html>
"""
    OUT.write_text(page, encoding="utf8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
