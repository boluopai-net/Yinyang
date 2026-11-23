#!/usr/bin/env python3
"""Render the environment-to-assistance relationship in both reader languages."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "docs/references/diagrams"
data = json.loads((DIR / "cognitive-complexity.candidate.json").read_text())

def text(x, y, value, cls, center=False):
    anchor = ' text-anchor="middle"' if center else ''
    return f'<text x="{x}" y="{y}" class="{cls}"{anchor}>{html.escape(value)}</text>'

for locale, d in data.items():
    suffix = ".zh-CN" if locale == "zh-CN" else ""
    pieces = [f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 1200 820">
<title id="title">{html.escape(d['title'])}</title><desc id="desc">{html.escape(d['description'])}</desc>
<style>text{{font-family:"PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif}}.title{{font-size:36px;font-weight:600;fill:#223c3b}}.sub{{font-size:22px;fill:#576d67}}.label{{font-size:20px;font-weight:600;fill:#355a50}}.body{{font-size:23px;fill:#405653}}.focus{{font-size:27px;font-weight:600;fill:#804327}}.rule{{font-size:20px;font-weight:700;fill:#804327}}.result{{font-size:28px;font-weight:600;fill:#223c3b}}.return{{font-size:23px;font-weight:600;fill:#804327}}</style>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M1 1L8 5L1 9" fill="none" stroke="#a15035" stroke-width="1.6"/></marker></defs>
<rect width="1200" height="820" rx="10" fill="#faf9f4"/>
<rect x="34" y="148" width="1132" height="430" rx="20" fill="#f0f3ef" stroke="#c7d5cc"/>
''', text(52, 73, d['title'], 'title'), text(54, 114, d['subtitle'], 'sub')]
    for i, (label, first, second) in enumerate(d['sources']):
        x = 54 + 370 * i
        fill = "#f5e7dc" if i == 2 else "#ffffff"
        pieces += [f'<rect x="{x}" y="170" width="352" height="132" rx="14" fill="{fill}"/>',
                   text(x + 22, 207, label, 'label'),
                   text(x + 22, 245, first, 'body'),
                   text(x + 22, 277, second, 'body')]
    pieces += [''.join(f'<path d="M{x} 302V333" stroke="#a15035" stroke-width="2" marker-end="url(#arrow)"/>' for x in (230, 600, 970)),
               '<rect x="54" y="344" width="1092" height="112" rx="16" fill="#f5e7dc" stroke="#d7b8a4"/>',
               text(80, 391, d['focusTitle'], 'focus'),
               text(80, 431, d['focus'], 'sub'),
               text(600, 483, d['principlesTitle'], 'label', True)]
    for i, rule in enumerate(d['priorities']):
        x = 80 + 350 * i
        pieces += [f'<rect x="{x}" y="498" width="326" height="58" rx="10" fill="#ffffff"/>',
                   text(x + 163, 535, rule, 'rule', True)]
    pieces += ['<path d="M600 578V605" stroke="#a15035" stroke-width="2" marker-end="url(#arrow)"/>',
               '<rect x="34" y="617" width="1132" height="113" rx="16" fill="#e1ece8" stroke="#bad0c6"/>',
               text(600, 661, d['outcome'], 'result', True),
               text(600, 702, d['detail'], 'sub', True),
               text(600, 784, d['return'], 'return', True), '</svg>']
    (DIR / f"cognitive-complexity{suffix}.svg").write_text(''.join(pieces))
