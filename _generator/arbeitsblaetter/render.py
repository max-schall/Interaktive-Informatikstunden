#!/usr/bin/env python3
"""Erzeugt Arbeitsblätter (max. 2 Seiten A4) zu den HTML-Präsentationen (IT, Aufbau wie bei Chemie).
Erzeugt zu jedem Blatt zusätzlich <stem>_Lösung.pdf.
Aufruf: render.py <reihe> [<stem> ...]   (Daten in data/<reihe>.py, dict WS)
        render.py --alle                 (alle Reihen in data/)"""
import html, importlib.util, re, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import quote
import segno
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
# Projektordner: zwei Ebenen über _generator/arbeitsblaetter/
ROOT = HERE.parents[1]
BUILD = Path(tempfile.mkdtemp(prefix='arbeitsblaetter_'))
sys.path.insert(0, str(HERE.parent))
from series import SERIES  # noqa: E402
SER = {s['folder']: s for s in SERIES}
FAECH = 'Informatik'
ACCENT = TINT = ''  # je Reihe in run() gesetzt (Kapitelfarbe)


def tint(hexcol, t=.88):
    h = hexcol.lstrip('#'); c = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
    return '#' + ''.join(f'{round(v + (255 - v) * t):02X}' for v in c)
# Adresse der veröffentlichten Präsentationen (z. B. GitHub Pages). Leer = kein QR-Code auf dem Blatt.
PAGES = 'https://max-schall.github.io/Interaktive-Informatikstunden/'
FONTS = '<link rel="stylesheet" href="' + (ROOT / 'fonts' / 'fonts.css').as_uri() + '">'


def esc(s):
    return html.escape(s, quote=False)


def gaps(s, sol=False):
    """[[Antwort]] -> Lücke (Arbeitsblatt) bzw. eingetragene Antwort (Lösung); **x** -> fett."""
    def g(m):
        if sol:
            return f'<span class="fill">{m.group(1)}</span>'
        w = max(2.2, len(m.group(1)) * 0.62 + 1.2)
        return f'<span class="gap" style="width:{w:.1f}em"></span>'
    s = esc(s)
    s = re.sub(r'\[\[(.*?)\]\]', g, s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s


def qr(series, stem):
    """QR-Code (SVG) zur Präsentation auf GitHub Pages."""
    if not PAGES:
        return ''
    url = PAGES + quote(f'{series}/{stem}.html')
    return segno.make(url, error='m').svg_inline(border=0, omitsize=True, dark='#111')


def lines(n):
    return f'<div class="lines" data-max="{n + 3}">' + '<div class="ln"></div>' * n + '</div>' if n else ''


def ans(loes):
    """Lösungstext; mehrere Absätze mit ' // ' trennen."""
    if not loes:
        return '<div class="ans miss">(individuelle Lösung)</div>'
    return '<div class="ans">' + '<br>'.join(gaps(x, True) for x in loes.split(' // ')) + '</div>'


# ---------- Aufgabentypen ----------
# Jeder Typ liefert ('A'|'I', Aufgabentext, HTML Arbeitsblatt, HTML Lösung).
def A(text, n=2, loes=''):
    """Offene Frage mit n Schreiblinien."""
    return ('A', text, lines(n), ans(loes))


def L(text, intro='Ergänze die Lücken.'):
    """Lückentext mit [[Lösung]]."""
    return ('A', intro, f'<p class="cloze">{gaps(text)}</p>', f'<p class="cloze">{gaps(text, True)}</p>')


def TAB(text, head, rows, h=8, widths=None):
    """Tabelle; Zellen [[Lösung]] bleiben auf dem Arbeitsblatt leer, '' bleibt immer leer."""
    cols = ''
    if widths:
        cols = '<colgroup>' + ''.join(f'<col style="width:{w}%">' for w in widths) + '</colgroup>'
    th = ''.join(f'<th>{gaps(c)}</th>' for c in head)

    def build(sol):
        trs = ''
        for r in rows:
            tds = ''
            for c in r:
                m = re.fullmatch(r'\[\[(.*)\]\]', c)
                if c == '' or m:
                    inner = f'<span class="fill">{gaps(m.group(1))}</span>' if (sol and m) else ''
                    tds += f'<td class="blank" style="height:{h}mm">{inner}</td>'
                else:
                    tds += f'<td>{gaps(c, sol)}</td>'
            trs += f'<tr>{tds}</tr>'
        return f'<table class="t">{cols}<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>'
    return ('A', text, build(False), build(True))


def MC(text, opts, cols=2):
    """Ankreuzaufgabe; richtige Optionen beginnen mit '*'."""
    def build(sol):
        li = ''
        for o in opts:
            ok = o.startswith('*')
            cb = '<span class="cb x">✗</span>' if (sol and ok) else '<span class="cb"></span>'
            li += f'<li>{cb}{gaps(o.lstrip("*"))}</li>'
        return f'<ul class="mc" style="columns:{cols}">{li}</ul>'
    return ('A', text, build(False), build(True))


def RF(statements, text='Richtig oder falsch? Kreuze an und verbessere falsche Aussagen.', fix=True):
    """Aussagen als 'r|Text' oder 'f|Text|Verbesserung'."""
    def build(sol):
        trs = ''
        for st in statements:
            parts = st.split('|')
            rf, t = parts[0], parts[1]
            corr = parts[2] if len(parts) > 2 else ''
            mark = lambda k: '<span class="cb x">✗</span>' if (sol and rf == k) else '<span class="cb"></span>'
            extra = f'<br><span class="fill">→ {gaps(corr)}</span>' if (sol and corr) else ''
            trs += f'<tr><td>{gaps(t)}{extra}</td><td class="c">{mark("r")}</td><td class="c">{mark("f")}</td></tr>'
        out = f'<table class="t rf"><colgroup><col><col style="width:9mm"><col style="width:9mm"></colgroup><thead><tr><th>Aussage</th><th>r</th><th>f</th></tr></thead><tbody>{trs}</tbody></table>'
        if fix and not sol:
            out += lines(1)
        return out
    return ('A', text, build(False), build(True))


def BOX(text, h=35, label='', n=0, loes=''):
    """Zeichen- oder Skizzenfeld (Höhe in mm), optional mit n Schreiblinien darunter."""
    lab = f'<span class="boxlab">{esc(label)}</span>' if label else ''
    return ('A', text, f'<div class="box" style="height:{h}mm">{lab}</div>' + lines(n), ans(loes))


def BOXES(text, labels, h=32, n=0, loes=None):
    """Mehrere Zeichenfelder nebeneinander; loes = Liste (je Feld) oder Text."""
    bx = ''.join(f'<div class="box" style="height:{h}mm"><span class="boxlab">{esc(l)}</span></div>' for l in labels)
    if isinstance(loes, list):
        sb = ''.join(f'<div class="box sol"><span class="boxlab">{esc(l)}</span>{ans(x)}</div>' for l, x in zip(labels, loes))
        sol = f'<div class="boxes">{sb}</div>'
    else:
        sol = ans(loes or '')
    return ('A', text, f'<div class="boxes">{bx}</div>' + lines(n), sol)


def GL(text, eqs):
    """Gleichungen/Formeln ergänzen; je Zeile ein String mit [[…]]."""
    return ('A', text, '<ol class="eqs">' + ''.join(f'<li>{gaps(e)}</li>' for e in eqs) + '</ol>',
            '<ol class="eqs">' + ''.join(f'<li>{gaps(e, True)}</li>' for e in eqs) + '</ol>')


def ZU(text, left, right, loes=()):
    """Zuordnung: links nummeriert, rechts mit Buchstaben; loes = Nummer je rechtem Eintrag."""
    def build(sol):
        rows = ''
        for i in range(max(len(left), len(right))):
            l = f'<span class="num">{i + 1}</span> {gaps(left[i])}' if i < len(left) else ''
            box = f'<span class="cb sq x">{loes[i]}</span>' if (sol and i < len(loes)) else '<span class="cb sq"></span>'
            r = f'<div class="zr">{box}<span class="num">{chr(65 + i)}</span><span>{gaps(right[i])}</span></div>' if i < len(right) else ''
            rows += f'<tr><td>{l}</td><td>{r}</td></tr>'
        return f'<table class="zu">{rows}</table>'
    return ('A', text + ' Trage die passende Nummer in das Kästchen ein.', build(False), build(True))


def INFO(text):
    """Kurzer Hinweis-/Materialkasten ohne Aufgabennummer."""
    return ('I', text, '', '')


def SORT(text, items, cats, h=22, loes=None):
    """Begriffe in Kategorien sortieren; loes = Liste von Listen je Kategorie."""
    words = ' · '.join(gaps(i) for i in items)
    bx = ''.join(f'<div class="box" style="height:{h}mm"><span class="boxlab">{esc(c)}</span></div>' for c in cats)
    sb = ''.join(f'<div class="box sol"><span class="boxlab">{esc(c)}</span><div class="ans">{esc(", ".join(x))}</div></div>'
                 for c, x in zip(cats, loes or [[] for _ in cats]))
    return ('A', text, f'<p class="words">{words}</p><div class="boxes">{bx}</div>', f'<div class="boxes">{sb}</div>')


# ---------- Präsentation lesen ----------
def tx(el):
    return re.sub(r'\s+', ' ', el.get_text(' ', strip=True)).replace(' .', '.').replace(' ,', ',').replace('( ', '(').replace(' )', ')') if el else ''


KEEP = {'b', 'i', 'sub', 'sup', 'br', 'ol', 'ul', 'li', 'p', 'table', 'thead', 'tbody', 'tr', 'th', 'td'}


def clean(el):
    """Nur einfache Text-Tags behalten, alles andere auspacken bzw. entfernen."""
    for x in el.find_all(['svg', 'canvas', 'button', 'script', 'style']):
        x.decompose()
    for x in el.select('.controls, .heft-title, .tag'):
        x.decompose()
    for x in el.find_all(True):
        if x.name not in KEEP:
            x.unwrap()
        else:
            x.attrs = {}
    return re.sub(r'\s+', ' ', el.decode_contents()).strip()


def heft_html(m):
    out = ''
    h = m.select_one('.heft')
    if h:
        out += clean(BeautifulSoup(str(h), 'html.parser'))
    for b in m.select('.stack .box'):
        c = clean(BeautifulSoup(str(b), 'html.parser'))
        if BeautifulSoup(c, 'html.parser').get_text(strip=True):
            out += f'<div class="hbox">{c}</div>'
    return out


def read_pres(path):
    src = path.read_text(encoding='utf-8')
    soup = BeautifulSoup(src, 'html.parser')
    info = {'stations': {}, 'order': []}
    start = soup.select_one('section#start')
    info['eyebrow'] = tx(start.select_one('.eyebrow'))
    info['title'] = tx(soup.title) or tx(start.find('h1'))
    ov = path.parent / '00_Uebersicht.html'
    info['series'] = re.sub(r'\s*–\s*Übersicht$', '', tx(BeautifulSoup(ov.read_text(encoding='utf-8'), 'html.parser').title)) if ov.exists() else ''
    leit = ''
    for tz in start.select('.teaser'):
        if 'Leitfrage' in tx(tz.select_one('.tag')):
            leit = tx(tz.find('p'))
    info['leitfrage'] = leit
    for s in soup.select('section.station'):
        sid = s.get('id')
        if sid == 'start':
            continue
        info['order'].append(sid)
        info['stations'][sid] = {'label': s.get('data-label'), 'h2': tx(s.find('h2')),
                                 'eyebrow': tx(s.select_one('.eyebrow'))}
    m = soup.select_one('section#merke')
    if m:
        info['heft'] = tx(m.select_one('.heft-title h3')) or tx(m.find('h3'))
        notes = [tx(p) for p in m.select('.stack .note')]
        info['heft_hint'] = ' '.join(n for n in notes if n)
        info['heft_html'] = heft_html(m)
    info['ichkann'] = [html.unescape(t).replace("\\'", "'") for t in re.findall(r"\{t:\s*'((?:[^'\\]|\\.)*)',\s*href", src)]
    if not info['ichkann']:
        info['ichkann'] = ['Ich kann ' + html.unescape(t) for t in re.findall(r"\['([^']+)',\s*'\d\d_\w+\.html#[\w-]+'", src)]
    return info


CSS = r'''
@page { size: A4; margin: 0 }
* { box-sizing: border-box }
html, body { margin: 0; padding: 0 }
body { font-family: "Atkinson Hyperlegible", "Noto Sans", "DejaVu Sans", sans-serif; font-size: 10.2pt; line-height: 1.38; color: #1b1b1b;
       -webkit-print-color-adjust: exact; print-color-adjust: exact }
.page { width: 210mm; height: 297mm; padding: 11mm 13mm 9mm 15mm; display: flex; flex-direction: column; overflow: hidden;
        page-break-after: always; position: relative }
#p2 { page-break-after: auto }
#src { display: none }
.top { display: flex; justify-content: space-between; align-items: flex-end; gap: 5mm; border-bottom: 2.2pt solid var(--ac);
       padding-bottom: 1.6mm; font-size: 8.6pt; color: #444 }
.top .meta b { color: var(--ac); letter-spacing: .02em }
.top .name { display: flex; gap: 5mm }
.top .meta { white-space: nowrap }
.top .name { white-space: nowrap }
.top .name span { display: inline-block; border-bottom: .6pt solid #555; min-width: 30mm; height: 4.5mm }
.top .name span.d { min-width: 20mm }
.head { display: flex; align-items: flex-start; gap: 4mm }
.head .ht { flex: 1 1 auto; min-width: 0 }
.qr { flex: none; margin-top: 3.2mm }
.qr svg { display: block; width: 15mm; height: 15mm }
h1 { font-family: "IBM Plex Mono", "DejaVu Sans Mono", monospace; font-weight: 600; font-size: 18pt; letter-spacing: -.01em; margin: 3.2mm 0 1.2mm; color: #111; line-height: 1.15 }
.leit { background: var(--tint); border-left: 2.4mm solid var(--ac); padding: 1.6mm 3mm; margin: 0 0 1.5mm; font-size: 10pt }
.leit b { color: var(--ac) }
.flow { flex: 1 1 auto; min-height: 0; overflow: hidden }
.sec { display: flex; align-items: baseline; gap: 2.2mm; margin: 3.4mm 0 0.8mm; border-bottom: .6pt solid var(--ac); padding-bottom: .5mm;
       break-after: avoid }
.sec .n { background: #0E1A1C; color: #fff; font-family: "IBM Plex Mono", monospace; font-weight: 600; font-size: 8.5pt; border-radius: .6mm; padding: .2mm 1.8mm }
.sec .h { font-family: "IBM Plex Mono", monospace; font-weight: 600; font-size: 11pt; color: #0E1A1C }
.sec .h::before { content: "// "; color: var(--ac) }
.sec .s { font-size: 8.4pt; color: #666; margin-left: auto }
.task { display: grid; grid-template-columns: 7mm 1fr; margin: 1.6mm 0 0 }
.task .no { font-weight: 700; color: var(--ac) }
.task .q > p:first-child { margin: 0 }
.info { margin: 1.4mm 0 0 7mm; padding: 1.2mm 2.5mm; background: #f4f4f4; border-radius: 1mm; font-size: 9.3pt }
.ln { height: 8mm; border-bottom: .5pt solid #8a8a8a }
.hl .ln { border-color: #b0b0b0 }
.gap { display: inline-block; border-bottom: .7pt solid #333; height: 1.05em; vertical-align: -0.25em; margin: 0 .5mm }
.cloze { line-height: 2.05; margin: .5mm 0 0 }
table.t { border-collapse: collapse; width: 100%; margin-top: 1.2mm; font-size: 9.4pt }
table.t th, table.t td { border: .6pt solid #777; padding: .8mm 1.6mm; text-align: left; vertical-align: middle }
table.t th { background: var(--tint) }
table.t td.c { text-align: center }
table.zu { width: 100%; border-collapse: collapse; margin-top: 1mm; font-size: 9.6pt }
table.zu td { padding: .9mm 1.5mm; vertical-align: top; width: 50% }
.zr { display: flex; align-items: flex-start; gap: 1mm }
.zr .cb.sq { flex: none; vertical-align: 0 }
.num { display: inline-block; min-width: 4.2mm; font-weight: 700; color: var(--ac) }
.cb { display: inline-block; width: 3.4mm; height: 3.4mm; border: .7pt solid #333; border-radius: .5mm; vertical-align: -0.5mm; margin-right: 1.8mm }
.cb.sq { width: 5mm; height: 5mm; vertical-align: -1.3mm }
ul.mc { list-style: none; padding: 0; margin: 1mm 0 0; column-gap: 6mm }
ul.mc li { break-inside: avoid; margin: .7mm 0 }
ol.eqs { margin: .5mm 0 0; padding-left: 5mm; line-height: 2.1 }
.box { border: .7pt solid #888; border-radius: 1.2mm; margin-top: 1.2mm; position: relative }
.boxes { display: flex; gap: 3mm }
.boxes .box { flex: 1 }
.boxlab { position: absolute; top: .8mm; left: 1.8mm; font-size: 8pt; color: #555 }
.words { margin: 1mm 0 0; padding: 1.2mm 2.5mm; border: .6pt dashed #888; border-radius: 1mm; font-size: 9.6pt }
.heft { flex: 1 1 auto; display: flex; flex-direction: column; border: 1.2pt solid #0E1A1C; border-radius: 1.5mm; margin-top: 3mm; min-height: 0; box-shadow: 1.2mm 1.2mm 0 #0E1A1C }
.heft .hh { background: #0E1A1C; color: #fff; font-family: "IBM Plex Mono", monospace; padding: 1.4mm 3mm; display: flex; justify-content: space-between; align-items: baseline;
            border-radius: 1.4mm 1.4mm 0 0 }
.heft .hh b { font-size: 11.4pt }
.heft .hh span { font-size: 8.4pt; opacity: .95 }
.heft .hint { font-size: 8.8pt; color: #333; padding: 1.2mm 3mm 0 }
.heft .hl { flex: 1 1 auto; margin: 0 3mm 2mm; overflow: hidden; min-height: 0 }
.p2top { display: flex; justify-content: space-between; font-size: 8.4pt; color: #555; border-bottom: .8pt solid var(--ac); padding-bottom: 1mm }
.tpl { display: flex; align-items: stretch; gap: 2mm; margin: 2.5mm 3mm .5mm }
.tpl .bx { flex: 1; border: 1pt solid var(--c); border-top-width: 2.4mm; border-radius: 1mm; height: 17mm; padding: .8mm 1.6mm; font-family: "IBM Plex Mono", monospace; font-size: 8pt; font-weight: 600; color: var(--c) }
.tpl .ar { align-self: center; font-size: 15pt; color: #555 }
.foot { position: absolute; bottom: 4mm; right: 13mm; font-size: 7.6pt; color: #888 }
.ichkann { width: 100%; border-collapse: collapse; font-size: 9.4pt; margin-top: 1mm }
.ichkann td, .ichkann th { border: .6pt solid #888; padding: .9mm 1.6mm }
.ichkann th { background: var(--tint); font-size: 8.6pt }
.ichkann .c { width: 13mm; text-align: center }
.ichkann th { text-align: left }
'''

JS = r'''
(function(){
  const src = document.getElementById('src'), f1 = document.querySelector('#p1 .flow'), f2 = document.querySelector('#p2 .flow');
  const blocks = Array.from(src.children);
  let target = f1, ok = true;
  for (let i = 0; i < blocks.length; i++) {
    const b = blocks[i];
    target.appendChild(b);
    if (target.scrollHeight > target.clientHeight + 1) {
      if (target === f1) {
        f1.removeChild(b);
        // Abschnittsüberschrift nicht allein am Seitenende stehen lassen
        const last = f1.lastElementChild;
        if (last && last.classList.contains('sec')) { f1.removeChild(last); f2.appendChild(last); }
        target = f2; f2.appendChild(b);
      }
    }
  }
  // Restplatz auf Seite 1 als zusätzliche Schreiblinien verteilen
  const restOf = () => { const lb = f1.lastElementChild; return (f1.getBoundingClientRect().bottom - (lb ? lb.getBoundingClientRect().bottom : 0)) / 3.7795; };
  const ls = Array.from(f1.querySelectorAll('.task .lines'));
  for (let k = 0; ls.length && restOf() >= 9 && k < 60; k++) {
    const l = ls[k % ls.length];
    if (l.children.length < +l.dataset.max) l.insertAdjacentHTML('beforeend', '<div class="ln"></div>');
  }
  const bx = Array.from(f1.querySelectorAll('.task .box'));
  if (bx.length && restOf() >= 6) { const b = bx[bx.length - 1]; b.style.height = (b.getBoundingClientRect().height / 3.7795 + restOf() - 3) + 'mm'; }
  // Restplatz auf Tabellen mit leeren Zellen (Schreibfelder) verteilen
  const tabs = Array.from(f1.querySelectorAll('.task table.t')).filter(t => t.querySelector('td.blank'));
  if (tabs.length && restOf() >= 8) {
    const rows = tabs.flatMap(t => Array.from(t.querySelectorAll('tbody tr')).filter(r => r.querySelector('td.blank')));
    const extra = Math.min(12, (restOf() - 4) / rows.length);
    const hs = rows.map(r => r.getBoundingClientRect().height / 3.7795);
    rows.forEach((r, i) => { r.style.height = (hs[i] + extra) + 'mm'; });
  }
  f2.style.flex = '0 0 auto';
  const heft = document.querySelector('.heft .hl');
  const mm = heft.getBoundingClientRect().height / 3.7795;
  heft.innerHTML = '<div class="ln"></div>'.repeat(Math.floor(mm / 8));
  const lastb = f1.lastElementChild;
  const rest = (f1.getBoundingClientRect().bottom - (lastb ? lastb.getBoundingClientRect().bottom : 0)) / 3.7795;
  const p2 = document.getElementById('p2');
  const over = p2.scrollHeight > p2.clientHeight + 1;
  document.body.setAttribute('data-heft', mm.toFixed(0));
  document.body.setAttribute('data-p1', rest.toFixed(0));
  document.body.setAttribute('data-over', over ? '1' : '0');
})();
'''


def task_blocks(ws, info, sol):
    blocks, no, secno = [], 0, 0
    for sid, tasks in ws['sections']:
        st = info['stations'][sid]
        secno += 1
        head = st['h2']
        if sid == 'uebungen' and 'Ich kann' not in head:
            head = 'Üben: ' + head
        sub = st['eyebrow'].split('·', 1)[-1].strip() if '·' in st['eyebrow'] else ''
        blocks.append(f'<div class="sec"><span class="n">{secno}</span><span class="h">{esc(head)}</span><span class="s">{esc(sub)}</span></div>')
        for kind, text, body, body_sol in tasks:
            if kind == 'I':
                blocks.append(f'<div class="info">{gaps(text)}</div>')
                continue
            no += 1
            blocks.append(f'<div class="task"><span class="no">{no}</span><div class="q"><p>{gaps(text)}</p>{body_sol if sol else body}</div></div>')
    return blocks, secno


def header_info(series, ws, info):
    info = dict(info)
    for k in ('eyebrow', 'leitfrage', 'title'):
        if k in ws:
            info[k] = ws[k]
    grade = SER[series]['grade']
    sname = info['series'] or info['eyebrow'].split('·', 1)[-1].strip()
    m = re.search(r'Stunde \d+', info['eyebrow'])
    return info, grade, sname, (m.group(0) if m else '')


SOL_CSS = r'''
@page { size: A4; margin: 11mm 13mm 10mm 15mm }
.solpage { display: block }
.solpage h1 { margin-top: 2.5mm }
.badge { background: var(--sol); color: #fff; font-weight: 700; padding: .4mm 2.4mm; border-radius: 1mm; letter-spacing: .04em }
.task, .info, .sec, .grp, table, .hbox, li { break-inside: avoid }
.sec { break-after: avoid }
.fill { color: var(--sol); font-weight: 600; border-bottom: .7pt solid #333; padding: 0 1mm }
td .fill, .ans .fill, .rf .fill { border-bottom: 0; padding: 0 }
.ans { color: var(--sol); margin: .8mm 0 0; padding: 1.2mm 2.5mm; border-left: 1mm solid var(--sol); background: #FBF1F0; font-size: 9.8pt }
.ans.miss { color: #888; border-color: #bbb; background: #f4f4f4 }
.cb.x { color: var(--sol); font-weight: 700; text-align: center; line-height: 3.2mm; font-size: 9pt; border-color: var(--sol) }
.cb.sq.x { line-height: 4.8mm }
.box.sol { height: auto; min-height: 12mm; padding-top: 5mm }
.box.sol .ans { border-left: 0; background: none; padding: 0 2mm 1mm }
.heftsol { border: 1.2pt solid var(--ac); border-radius: 2mm; margin-top: 4mm; break-inside: avoid }
.heftsol .hh { break-after: avoid }
.heftsol .hh { background: var(--ac); color: #fff; padding: 1.4mm 3mm; border-radius: 1.4mm 1.4mm 0 0; font-weight: 700; font-size: 11.4pt }
.heftsol .hb { padding: 1.5mm 4mm 2.5mm; font-size: 9.8pt }
.heftsol ol { padding-left: 5mm; margin: 1mm 0 }
.heftsol li { margin: .8mm 0 }
.heftsol table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 1.5mm 0 }
.heftsol th, .heftsol td { border: .6pt solid #888; padding: .7mm 1.4mm; text-align: left }
.heftsol th { background: var(--tint) }
.hbox { margin-top: 1.5mm; padding: 1mm 2.5mm; background: #f4f4f4; border-radius: 1mm }
.hbox p { margin: .5mm 0 }
'''


def build_solution_html(series, stem, ws, info):
    info, grade, sname, stunde = header_info(series, ws, info)
    blocks, _ = task_blocks(ws, info, sol=True)
    merged = []
    for b in blocks:
        if merged and merged[-1].startswith('<div class="sec">'):
            merged[-1] = '<div class="grp">' + merged[-1] + b + '</div>'
        else:
            merged.append(b)
    heft = ''
    content = ws.get('heft_loes') or info.get('heft_html', '')
    if content and not ws.get('ichkann'):
        heft_t = ws.get('heft_title') or info.get('heft') or info['title']
        heft = f'<div class="heftsol"><div class="hh">Heftaufschrieb: {esc(heft_t)}</div><div class="hb">{content}</div></div>'
    leit = f'<div class="leit"><b>Leitfrage:</b> {esc(info["leitfrage"])}</div>' if info['leitfrage'] else ''
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{esc(info["title"])} – Lösung</title>{FONTS}
<style>:root{{--ac:{ACCENT};--tint:{TINT};--sol:#B3261E}}{CSS}{SOL_CSS}</style></head><body>
<div class="solpage">
  <div class="top"><div class="meta"><b>{FAECH.upper()} · KLASSE {grade}</b> · {esc(sname)}{' · ' + esc(stunde) if stunde else ''}</div>
  <div><span class="badge">LÖSUNG</span></div></div>
  <h1>{esc(info["title"])}</h1>{leit}
  {"".join(merged)}{heft}
</div></body></html>'''


def build_html(series, stem, ws, info):
    info, grade, sname, stunde = header_info(series, ws, info)
    blocks, secno = task_blocks(ws, info, sol=False)
    if ws.get('ichkann') and info['ichkann']:
        rows = ''.join(f'<tr><td>{esc(t)}</td><td class="c">☺</td><td class="c">😐</td><td class="c">☹</td></tr>' for t in info['ichkann'])
        secno += 1
        blocks.append(f'<div class="sec"><span class="n">{secno}</span><span class="h">Ich kann …</span><span class="s">Selbsteinschätzung</span></div>')
        blocks.append('<div><div class="info" style="margin-left:0">Kreuze ehrlich an. Bei ☹ wiederholst du die passende Stunde.</div>'
                      f'<table class="ichkann"><thead><tr><th>Ich kann …</th><th class="c">sicher</th><th class="c">teils</th><th class="c">noch nicht</th></tr></thead><tbody>{rows}</tbody></table></div>')
    # Abschnittsüberschrift immer mit dem ersten Element zusammenhalten
    merged = []
    for b in blocks:
        if merged and merged[-1].startswith('<div class="sec">') and merged[-1].endswith('</div>') and merged[-1].count('class="sec"') == 1 and not merged[-1].startswith('<div class="grp">'):
            merged[-1] = '<div class="grp">' + merged[-1] + b + '</div>'
        else:
            merged.append(b)
    blocks = merged
    heft_t = ws.get('heft_title') or info.get('heft') or info['title']
    heft_label = ws.get('heft_label', 'Heftaufschrieb')
    hint = ws.get('heft_hint', info.get('heft_hint', ''))
    hint_html = f'<div class="hint">✎ {gaps(hint)}</div>' if hint else ''
    leit = f'<div class="leit"><b>Leitfrage:</b> {esc(info["leitfrage"])}</div>' if info['leitfrage'] else ''
    acc, tint = ACCENT, TINT
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{esc(info["title"])} – Arbeitsblatt</title>{FONTS}
<style>:root{{--ac:{acc};--tint:{tint}}}{CSS}</style></head><body>
<div class="page" id="p1">
  <div class="top"><div class="meta"><b>{FAECH.upper()} · KLASSE {grade}</b> · {esc(sname)}{' · ' + esc(stunde) if stunde else ''}</div>
  <div class="name">Name <span></span> Datum <span class="d"></span></div></div>
  <div class="head"><div class="ht"><h1>{esc(info["title"])}</h1>{leit}</div>
  {f'<div class="qr">{qr(series, stem)}</div>' if PAGES else ''}</div>
  <div class="flow"></div><div class="foot">Arbeitsblatt zu {esc(stem)}.html · Seite 1/2</div>
</div>
<div class="page" id="p2">
  <div class="p2top"><span>{esc(info["title"])}</span><span>{FAECH} · Klasse {grade}</span></div>
  <div class="flow"></div>
  <div class="heft"><div class="hh"><b>{esc(heft_label)}: {esc(heft_t)}</b><span>{esc(ws.get("heft_sub", "aus der Präsentation übernehmen"))}</span></div>{hint_html}{ws.get("heft_tpl", "")}<div class="hl"></div></div>
  <div class="foot">Arbeitsblatt zu {esc(stem)}.html · Seite 2/2</div>
</div>
<div id="src">{"".join(blocks)}</div>
<script>{JS}</script></body></html>'''


def check(info, ws, stem):
    covered = [s for s, _ in ws['sections']]
    need = [s for s in info['order'] if s != 'merke' and s not in ws.get('skip', [])]
    if ws.get('ichkann'):
        need = [s for s in need if not (info['stations'][s]['label'] or '').startswith('Ich kann')]
    miss = [s for s in need if s not in covered]
    bad = [s for s in covered if s not in info['stations']]
    for s, tasks in ws['sections']:
        if not tasks:
            print(f'  ! {stem}: Abschnitt {s} ohne Aufgaben')
    if miss or bad:
        print(f'  ! {stem}: fehlende Abschnitte {miss}, unbekannte {bad}')


def run(series, stems):
    global ACCENT, TINT
    ACCENT = SER[series]['accent'][0]; TINT = tint(ACCENT)
    spec = importlib.util.spec_from_file_location('d', HERE / 'data' / f'{series}.py')
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    for stem, ws in mod.WS.items():
        if stems and stem not in stems:
            continue
        info = read_pres(ROOT / series / f'{stem}.html')
        check(info, ws, stem)
        hp = BUILD / f'{series}__{stem}.html'
        hp.write_text(build_html(series, stem, ws, info), encoding='utf-8')
        pdf = ROOT / series / f'{stem}.pdf'
        common = ['chromium-browser', '--headless', '--disable-gpu', '--no-sandbox', '--virtual-time-budget=3000']
        subprocess.run(common + ['--no-pdf-header-footer', f'--print-to-pdf={pdf}', hp.as_uri()],
                       capture_output=True, check=True)
        dom = subprocess.run(common + ['--dump-dom', hp.as_uri()], capture_output=True, text=True).stdout
        m = re.search(r'data-heft="(\d+)" data-p1="(-?\d+)" data-over="(\d)"', dom)
        heft, p1, over = (m.groups() if m else ('?', '?', '?'))
        flag = '  <-- PRÜFEN' if over != '0' or (heft != '?' and int(heft) < 60) else ''
        print(f'{series}/{stem}.pdf  Heft {heft} mm  Restplatz S.1 {p1} mm  Überlauf {over}{flag}')
        sh = BUILD / f'{series}__{stem}_Loesung.html'
        shtml = build_solution_html(series, stem, ws, info)
        sh.write_text(shtml, encoding='utf-8')
        spdf = ROOT / series / f'{stem}_Lösung.pdf'
        subprocess.run(common + ['--no-pdf-header-footer', f'--print-to-pdf={spdf}', sh.as_uri()], capture_output=True, check=True)
        miss = shtml.count('ans miss')
        if miss:
            print(f'  ! {stem}: {miss} Aufgabe(n) ohne Lösungstext')


if __name__ == '__main__':
    if sys.argv[1:] == ['--alle']:
        for d in sorted((HERE / 'data').glob('*.py')):
            run(d.stem, [])
    else:
        run(sys.argv[1], sys.argv[2:])
