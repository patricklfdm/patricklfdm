#!/usr/bin/env python3
"""Generate self-contained SVG assets using only the Python standard library."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BG, SURFACE, CYAN, GREEN, WHITE, MUTED = '#0B1220', '#152337', '#7DD3FC', '#34D399', '#F8FAFC', '#B6C6D9'

def text(x, y, value, size=20, color=WHITE, weight=400, extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def line(x1, y1, x2, y2, color='#28445C', width=1):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none"/>'

def rect(x,y,w,h,fill=SURFACE,stroke='#28445C',r=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'

def node(x,y,active=False):
    c = GREEN if active else CYAN
    return f'<circle cx="{x}" cy="{y}" r="13" fill="{BG}" stroke="{c}" stroke-width="2"/><circle cx="{x}" cy="{y}" r="4" fill="{c}"/>'

def save(name, h, title, desc, body):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="{h}" viewBox="0 0 800 {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
<defs><linearGradient id="surface" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#152337"/><stop offset="1" stop-color="#0B1220"/></linearGradient></defs>
<rect width="800" height="{h}" rx="18" fill="url(#surface)"/>
<rect x="0.5" y="0.5" width="799" height="{h-1}" rx="18" fill="none" stroke="#28445C"/>
<g font-family="Arial, Helvetica, sans-serif">{body}</g>
</svg>
'''
    (ROOT / 'assets' / name).write_text(svg)

body = ''.join(line(x,0,x,360,'#1B2E43') for x in range(480,801,40))
body += ''.join(line(480,y,800,y,'#1B2E43') for y in range(40,361,40))
pts=[(570,75),(700,105),(620,180),(740,245),(550,290)]
for a,b in [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,4)]:
    body+=line(*pts[a],*pts[b],'#39617A',2)
body+=''.join(node(x,y,i==2) for i,(x,y) in enumerate(pts))
body+=text(36,123,'Patrick Li',62,WHITE,700)
body+=text(36,184,'Engineering Systems',33,WHITE,600)
body+=text(36,226,'That Scale.',33,WHITE,600)
body+=line(36,265,112,265,GREEN,3)
body+=text(36,309,'SEARCH  /  SYSTEMS  /  AI',20,MUTED,400,'letter-spacing="1.5"')
save('hero.svg',350,'Patrick Li — Engineering Systems That Scale.','Patrick Li. Search, systems, and AI. A restrained topology connects five distributed nodes.',body)

body=text(32,40,'01 / FEATURED SYSTEM',18,CYAN,600,'letter-spacing="1.4"')
body+=text(768,40,'PUBLIC SOURCE',17,GREEN,600,'text-anchor="end"')
body+=text(32,101,'General Search Engine',43,WHITE,700)
body+=text(32,143,'Retrieval. Durability. Replication.',24,MUTED)
body+=line(32,169,768,169)
body+=text(32,208,'JAVA 21',19,CYAN,600)
body+=text(213,208,'BM25',19,MUTED,600)
body+=text(375,208,'WAL',19,MUTED,600)
body+=text(546,208,'QUORUM',19,MUTED,600)
save('gse-card.svg',240,'General Search Engine','Public source. Java 21 search infrastructure: retrieval, durability, and replication.',body)

body=text(32,40,'02 / PRIVATE ENGINEERING',18,CYAN,600,'letter-spacing="1.4"')
body+=text(768,40,'PRIVATE SOURCE',17,MUTED,600,'text-anchor="end"')
body+=text(32,105,'Wayvia',48,WHITE,700)
body+=text(32,147,'AI-powered travel planning',27,MUTED)
body+=line(32,175,768,175)
body+=text(32,214,'REASON',19,CYAN,600)+line(132,207,195,207)
body+=text(219,214,'ORCHESTRATE',19,CYAN,600)+line(384,207,447,207)
body+=text(471,214,'PERSONALIZE',19,GREEN,600)
save('wayvia-card.svg',246,'Wayvia — AI-powered travel planning','Private source. AI engineering, workflow orchestration, and personalized travel planning.',body)

body=text(32,44,'GSE / CONCEPTUAL ARCHITECTURE',22,CYAN,600)
body+=text(32,80,'Search core with optional durability and replication',21,MUTED)
body+=rect(32,110,736,72)+text(56,155,'Typed filters + full-text queries + BM25',27,WHITE,600)
body+=line(400,182,400,216,CYAN,2)+text(420,207,'read',18,MUTED)
body+=rect(32,216,736,72)+text(56,262,'Immutable search snapshots',27,WHITE,600)
body+=line(400,288,400,326,GREEN,2)+text(420,315,'publish',18,MUTED)
body+=rect(32,326,736,72)+text(56,372,'Single writer / batched mutations',27,WHITE,600)
body+=line(400,398,400,436,GREEN,2)
body+=rect(32,436,736,94)+text(56,475,'OPTIONAL DURABILITY',18,CYAN,600)+text(56,508,'Write-ahead log + checkpoints + recovery',24)
body+=line(400,530,400,564,GREEN,2)
body+=rect(32,564,736,152)+text(56,601,'OPTIONAL REPLICATION / v5.1',18,CYAN,600)
body+=line(150,650,400,650)+line(400,650,650,650)
for x,label,active in [(150,'Voter 1',False),(400,'Leader / voter 2',True),(650,'Voter 3',False)]:
    body+=node(x,650,active)+text(x,690,label,19,MUTED,400,'text-anchor="middle"')
body+=text(32,755,'Fixed three-voter group · strong reads on the leader',22,MUTED)
body+=text(32,790,'Conceptual layers; not a complete protocol or deployment diagram.',18,MUTED)
save('gse-architecture.svg',822,'General Search Engine conceptual architecture','Queries read immutable snapshots; a single writer publishes updates. Optional WAL and checkpoints provide durability. Optional v5.1 replication uses a fixed three-voter group with a leader.',body)
print('Generated 4 SVG assets.')
