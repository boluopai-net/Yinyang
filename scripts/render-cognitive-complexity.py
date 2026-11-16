#!/usr/bin/env python3
"""Render the authored cognitive complexity diagram in both reader languages."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "skills/yinyang/references/diagrams"
data = json.loads((DIR / "cognitive-complexity.candidate.json").read_text())

def esc(value):
    return html.escape(value, quote=True)

for locale, d in data.items():
    suffix = ".zh-CN" if locale == "zh-CN" else ""
    def text(x, y, value, cls):
        return f'<text x="{x}" y="{y}" class="{cls}">{esc(value)}</text>'
    pieces = [f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc" viewBox="0 0 1100 760">
<title id="title">{esc(d['title'])}</title><desc id="desc">{esc(d['description'])}</desc>
<style>text{{font-family:"PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif}}.title{{font-size:38px;font-weight:600;fill:#223c3b}}.subtitle{{font-size:20px;fill:#657572}}.eyebrow{{font-size:16px;font-weight:700;letter-spacing:2px;fill:#9b5336}}.heading{{font-size:27px;font-weight:600;fill:#263f3d}}.body{{font-size:20px;fill:#405653}}.cardtitle{{font-size:18px;font-weight:700;letter-spacing:1px;fill:#9b5336}}.cardbody{{font-size:21px;fill:#263f3d}}.small{{font-size:18px;fill:#657572}}.return{{font-size:20px;font-weight:600;fill:#a15035}}</style>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M1 1L8 5L1 9" fill="none" stroke="#a15035" stroke-width="1.6"/></marker></defs>
<rect width="1100" height="760" rx="8" fill="#faf9f4"/><path d="M44 48H1056" stroke="#c8d2c8"/>
''', text(44, 99, d['title'], 'title'), text(45, 132, d['subtitle'], 'subtitle'),
'''<rect x="44" y="166" width="1012" height="115" rx="16" fill="#f5e9de"/><circle cx="81" cy="223" r="17" fill="#ac5c3e"/><path d="M81 214v11m0 6v1" stroke="#fffaf4" stroke-width="2.5" stroke-linecap="round"/>''',
text(113, 214, d['observation'][0], 'heading'), text(113, 249, d['observation'][1], 'body'),
'''<path d="M550 281V313" fill="none" stroke="#a15035" stroke-width="2" marker-end="url(#arrow)"/>''', text(44, 342, d['allocation'], 'eyebrow')]
    english_lines = [["Recognize when the", "meaning changes"], ["Bring the source into", "the reading place"], ["Align sources and", "track versions"]]
    for i, (label, body) in enumerate(d['choices']):
        x = 44 + i * 344
        pieces += [f'<rect x="{x}" y="359" width="324" height="112" rx="14" fill="#e9f0eb" stroke="#c7d8ce"/>',
                   text(x + 23, 394, label, 'cardtitle')]
        if locale == "en":
            pieces += [text(x + 23, 424 + n * 26, line, 'cardbody') for n, line in enumerate(english_lines[i])]
        else:
            pieces.append(text(x + 23, 435, body, 'cardbody'))
    pieces += ['''<path d="M550 471V502" fill="none" stroke="#a15035" stroke-width="2" marker-end="url(#arrow)"/>
<rect x="44" y="512" width="1012" height="112" rx="16" fill="#e1ece8" stroke="#bad0c6"/>''',
text(73, 556, d['test'][0], 'heading'), text(73, 592, d['test'][1], 'body'),
'''<path d="M950 624V664Q950 684 930 684H45Q25 684 25 664V350" fill="none" stroke="#a15035" stroke-width="2" marker-end="url(#arrow)"/>
<rect x="275" y="664" width="550" height="39" rx="9" fill="#faf9f4"/>''',
text(550, 690, d['return'], 'return').replace('<text ', '<text text-anchor="middle" '),
text(550, 738, d['retire'], 'small').replace('<text ', '<text text-anchor="middle" '), '</svg>']
    (DIR / f"cognitive-complexity{suffix}.svg").write_text(''.join(pieces))
