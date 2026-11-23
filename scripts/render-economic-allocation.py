"""Render a qualitative allocation-and-feedback map for the economic RSI essay."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1] / 'docx/references/diagrams'
INK, MUTED, RULE, ACCENT = '#243c3b', '#536461', '#8c9c96', '#a55335'


def render(zh):
    def label(cn, en):
        return cn if zh else en

    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-labelledby="title desc">
<title id="title">{label('有限投入，怎样分配？', 'Where should finite resources go?')}</title>
<desc id="desc">{label('时间、注意力、身体精力和费用，支持亲自培养、借用模型以及支持与恢复。比较生活所得、能力发展和总成本，重新选择投入与分工。神经与身体、心理与选择、社会与制度共同影响这一安排。箭头表示关系。', 'Time, attention, bodily energy, and money support personal cultivation, model assistance, and support and recovery. Outcomes, developing capacities, and total costs inform revised allocation. Neural and bodily, psychological, and social conditions shape the arrangement. Arrows denote relationships.')}</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1L9 5L1 9" fill="none" stroke="{MUTED}" stroke-width="1.5"/></marker></defs>
<rect width="1200" height="800" rx="12" fill="#faf9f5"/>
<style>text{{font-family:Helvetica Neue,PingFang SC,sans-serif;fill:{INK}}}.sub{{fill:{MUTED};font-size:19px}}.title{{font-size:25px;font-weight:600}}.path{{fill:none;stroke:{MUTED};stroke-width:2;stroke-linejoin:round;marker-end:url(#arrow)}}</style>''']

    def text(x, y, value, size=20, weight=400, anchor='start', color=INK):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" style="fill:{color}">{escape(value)}</text>')

    def box(x, y, w, h, fill='white', stroke=RULE):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')

    text(52, 57, label('有限投入，怎样分配？', 'Where should finite resources go?'), 34, 600)
    text(52, 93, label('个人递归自改进 · 让选择投入的方法也能改善', 'Personal RSI · improve how investment is chosen'), 20, color=MUTED)
    box(52, 126, 1096, 66, '#eef2ec', '#c2cec5')
    text(600, 167, label('生活目的 · 当前能力 · 现实机会', 'Life purposes · current capabilities · real opportunities'), 24, 500, 'middle')

    text(70, 237, label('有限资源', 'Finite resources'), 23, 600)
    box(52, 262, 230, 328)
    resources = [('时间', 'Time'), ('注意力', 'Attention'), ('身体精力', 'Bodily energy'), ('费用', 'Money')]
    for i, pair in enumerate(resources):
        y = 312 + i * 66
        parts.append(f'<circle cx="82" cy="{y-7}" r="5" fill="{ACCENT}"/>')
        text(102, y, label(*pair), 23)
        if i < 3:
            parts.append(f'<path d="M74 {y+22}H260" stroke="#e1e5de"/>')

    text(600, 237, label('组合投入', 'Combine investments'), 23, 600, 'middle')
    rows = [
        (262, '亲自培养', 'Cultivate personally', '感知 · 判断 · 真实尝试', 'Perceive · judge · practice'),
        (382, '借用模型', 'Use model capabilities', '语言展开 · 生成 · 实现', 'Elaborate · generate · implement'),
        (502, '支持与恢复', 'Support and recovery', '环境维护 · 休息 · 返回', 'Maintain · rest · resume'),
    ]
    for y, cn, en, scn, sen in rows:
        box(418, y, 364, 88)
        text(600, y+35, label(cn, en), 25, 600, 'middle')
        text(600, y+65, label(scn, sen), 19, anchor='middle', color=MUTED)

    # Separate attachment points and rounded elbows keep each relation legible.
    for p in ['M282 306H418',
              'M282 426H418',
              'M282 546H418',
              'M782 306H834Q846 306 846 318V353Q846 365 858 365H918',
              'M782 426H918',
              'M782 546H834Q846 546 846 534V499Q846 487 858 487H918']:
        parts.append(f'<path class="path" d="{p}"/>')

    text(1033, 237, label('实际后果', 'Actual consequences'), 23, 600, 'middle')
    box(918, 300, 230, 252, '#f7eee6', ACCENT)
    for y, cn, en in [(353, '生活所得', 'Life gains'), (414, '能力发展', 'Capacity growth'), (475, '总成本', 'Total costs')]:
        text(1033, y, label(cn, en), 24, 500, 'middle')
    text(1033, 521, label('含监督与他人成本', 'Including costs to others'), 16, anchor='middle', color=MUTED)

    # Feedback changes the allocation, rather than implying replenishment of a budget.
    parts.append('<path class="path" d="M1033 552V648Q1033 660 1021 660H800"/>')
    box(400, 628, 400, 64, '#eef2ec', '#839b8d')
    text(600, 668, label('重选投入、分工与评价', 'Revise allocation and evaluation'), 23, 600, 'middle')
    parts.append('<path class="path" d="M400 660H364Q352 660 352 648V554A8 8 0 0 0 352 538V434A8 8 0 0 0 352 418V314A8 8 0 0 0 352 298V246Q352 234 364 234H475"/>')
    text(969, 631, label('经验返回', 'Experience returns'), 18, anchor='middle', color=MUTED)

    text(600, 744, label('神经与身体 · 心理与选择 · 社会与制度', 'Neural and bodily · psychological · social and institutional'), 21, 500, 'middle')
    text(600, 777, label('三种视角共同解释投入的条件与价值；各项资源分别比较。', 'Three perspectives on conditions and value; compare each resource on its own terms.'), 17, anchor='middle', color=MUTED)
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    for zh in (False, True):
        (ROOT / ('economic-allocation' + ('.zh-CN' if zh else '') + '.svg')).write_text(render(zh))
