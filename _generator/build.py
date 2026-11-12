#!/usr/bin/env python3
"""Baut die IT-Unterrichtsreihen aus src/<reihe>/*.html in den Zielordner.
Aufbau wie bei den Chemie-Präsentationen, aber mit eigenem Design (style.css) und eigener Bibliothek (lib.js).
Aufruf: build.py [<reihe> ...]   (ohne Argument: alle Reihen und die Startseite)"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from series import SERIES  # noqa: E402

FONTS = '<link rel="stylesheet" href="../fonts/fonts.css">'
LIGHT = ("--bg:#EEF2F1; --surface:#FFFFFF; --surface-2:#E3EAE9; --ink:#0E1A1C; --ink-2:#4A5B5E; --line:#C3CFCE; --grid:rgba(14,26,28,.10);\n"
         "  --edge:#0E1A1C; --edge-shadow:#0E1A1C; --accent:#0B7A80; --accent-ink:#FFFFFF; --good:#15803D; --bad:#B91C1C;\n"
         "  --e:#2459D6; --v:#B45309; --a:#BE185D; --k1:#6D28D9; --k2:#C2410C; --k3:#0369A1; --k4:#047857; --zl-a:#F7E9A8; --zl-b:#F1B35A;\n"
         "  --bar:#0B1416; --bar-2:#132226; --bar-line:#2A4046; --bar-ink:#DCE8E9; --bar-ink-2:#8FA7AB; --led:#3DF2C4;\n"
         "  --phone:#2B3438; --phone-scr:#CFE6EE; --phone-part:#55636A; --heft-line:rgba(11,122,128,.10);")
DARK = ("--bg:#091113; --surface:#101C1F; --surface-2:#172A2E; --ink:#E2EEEF; --ink-2:#9AB0B3; --line:#294046; --grid:rgba(226,238,239,.06);\n"
        "    --edge:#3C5A61; --edge-shadow:#000000; --accent:#2DD4BF; --accent-ink:#04201C; --good:#4ADE80; --bad:#F87171;\n"
        "    --e:#3B7BF6; --v:#D97706; --a:#DB2777; --k1:#8B5CF6; --k2:#EA580C; --k3:#0284C7; --k4:#059669; --zl-a:#E9D98F; --zl-b:#E3A04A;\n"
        "    --bar:#050B0C; --bar-2:#0E1A1C; --bar-line:#24383D; --bar-ink:#DCE8E9; --bar-ink-2:#8FA7AB; --led:#3DF2C4;\n"
        "    --phone:#3A464B; --phone-scr:#1E3A44; --phone-part:#6B7B82; --heft-line:rgba(45,212,191,.08);\n    color-scheme:dark;")


def palette_css(series=None):
    fonts = ('  --f-body:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;\n'
             '  --f-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Consolas,monospace;\n  font-size:clamp(16px, 0.75vw + 9px, 22px);\n')
    light, dark = LIGHT, DARK
    if series and 'accent' in series:
        # Kapitelfarbe: (hell, dunkel)
        la, da = series['accent']
        # Leisten sind immer dunkel: Leuchtfarbe (Stationen, Weiter-Button) ist die helle Kapitelfarbe
        light += f" --accent:{la}; --led:{da};"
        dark = dark.replace('color-scheme:dark;', f'--accent:{da}; --led:{da}; color-scheme:dark;')
    return (":root{\n  " + light + "\n" + fonts + "}\n"
            "@media (prefers-color-scheme: dark){\n  :root:not([data-theme=\"light\"]){\n    " + dark + "\n  }\n}\n"
            ":root[data-theme=\"dark\"]{\n    " + dark + "\n}\n")


META_RE = re.compile(r'^\s*<!--(.*?)-->', re.S)


def parse_lesson(path):
    txt = path.read_text(encoding='utf-8')
    m = META_RE.match(txt)
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    body = txt[m.end():]
    js = ''
    if '<script>' in body:
        i = body.index('<script>')
        js = body[i + 8:body.rindex('</script>')]
        body = body[:i]
    return meta, body.strip(), js


SEC_RE = re.compile(r'<section class="station" id="([^"]+)"([^>]*)>')
ATTR_RE = re.compile(r'data-([a-z]+)="([^"]*)"')


def build_lesson(series, idx, lessons, outdir, css, js):
    path, meta, body, ljs = lessons[idx]
    grade, subj = series['grade'], series.get('subject', 'Informatik')
    num = idx + 1
    secs = [(mm.group(1), dict(ATTR_RE.findall(mm.group(2)))) for mm in SEC_RE.finditer(body)]
    first = True

    def hide(mm):
        nonlocal first
        tag = mm.group(0)
        if first:
            first = False
            return tag
        return tag[:-1] + ' hidden>'
    body = SEC_RE.sub(hide, body)
    stations = [(i, a) for i, a in secs if 'yr' in a]
    tl = ['      <li><button class="tl-pill" data-go="start">Start</button></li>', '      <li class="sep" aria-hidden="true"></li>']
    for k, (sid, a) in enumerate(stations):
        cls = 'm' + (' first' if k == 0 else '') + (' last' if k == len(stations) - 1 else '')
        tl.append(f'      <li class="{cls}"><button class="tl-stop" data-go="{sid}"><span class="dot"><span class="num">{k + 1}</span></span><span class="yr">{a["yr"]}</span><span class="nm">{a.get("label", sid)}</span></button></li>')
    tl.append('      <li class="sep" aria-hidden="true"></li>')
    for sid, a in secs:
        if sid != 'start' and 'yr' not in a:
            tl.append(f'      <li><button class="tl-pill" data-go="{sid}">{a.get("label", sid)}</button></li>')
    prev = ['    <ol class="preview" aria-label="Stationen dieser Stunde">']
    for k, (sid, a) in enumerate(stations):
        prev.append(f'      <li><button data-go="{sid}"><span class="num">{k + 1:02d}</span><span class="y">{a["yr"]}</span><span class="n"><b>{a.get("title", a.get("label"))}</b><span>{a.get("sub", "")}</span></span></button></li>')
    prev.append('    </ol>')
    body = body.replace('<!--PREVIEW-->', '\n'.join(prev)).replace('{{N}}', str(num)).replace('{{K}}', str(grade))
    if idx + 1 < len(lessons):
        npath, nmeta = lessons[idx + 1][0], lessons[idx + 1][1]
        nxt = {'href': npath.name, 'label': f'Stunde {num + 1}: {nmeta["short"]}'}
        box = (f'<div class="next-lesson"><p><b>Nächste Stunde – {nmeta["title"]}:</b> {nmeta["q"]}</p>'
               f'<a class="btn primary" href="{npath.name}">Zu Stunde {num + 1} →</a></div>')
    else:
        nxt = {'href': '00_Uebersicht.html', 'label': 'Zur Übersicht'}
        box = '<div class="next-lesson"><p><b>Geschafft!</b> Das war die letzte Stunde dieser Reihe.</p><a class="btn primary" href="00_Uebersicht.html">Zur Übersicht der Reihe</a></div>'
    if 'id="uebungen"' in body:
        i = body.index('id="uebungen"')
        j = body.index('</section>', i)
        body = body[:j] + '  ' + box + '\n' + body[j:]
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{meta["title"]}</title>
{FONTS}
<style>
/* Layout: Konsolen-Leiste mit Stationen oben, eine Station pro Bildschirm, Blätter-Leiste unten – gebaut für Beamer & Presenter */
{palette_css(series)}{css}
</style>
</head>
<body data-next="{html.escape(json.dumps(nxt, ensure_ascii=False))}">
<div class="app">
<header class="top">
  <div class="brand"><b>{meta["short"]}</b><span>Stunde {num} · {subj} · Klasse {grade}</span></div>
  <nav class="tl-scroll" aria-label="Stationen der Stunde">
    <ol class="tl" id="tl">
{chr(10).join(tl)}
    </ol>
  </nav>
  <a class="icon-btn" href="../index.html#{gkey(series)}" title="Startseite: alle Reihen der Klassenstufe">⌂ Start</a>
  <a class="icon-btn" href="{path.stem}.pdf" target="_blank" rel="noopener" title="Arbeitsblatt zur Stunde (PDF)">Arbeitsblatt</a>
  <a class="icon-btn" href="00_Uebersicht.html" title="Zur Übersicht der Reihe">Übersicht</a>
  <button class="icon-btn" id="fs" title="Vollbild (F)">Vollbild</button>
</header>

<main id="stage">
{body}
</main>

<footer class="pager">
  <button class="btn" id="prev">←</button>
  <div class="mid"><span id="pos"></span><span class="keys"> · Pfeiltasten ← → oder Presenter</span></div>
  <button class="btn primary" id="next">→</button>
</footer>
</div>

<script>
(() => {{
{js}
/* ================================================================ */
/* ================= Inhalte dieser Stunde ================= */
{ljs}
startApp();
}})();
</script>
</body>
</html>
'''
    (outdir / path.name).write_text(page, encoding='utf-8')


def build_overview(series, lessons, outdir, css):
    grade, subj = series['grade'], series.get('subject', 'Informatik')
    items = []
    for k, (path, meta, body, _) in enumerate(lessons):
        facts = ''.join(f'<li>{f.strip()}</li>' for f in meta.get('facts', '').split('|') if f.strip())
        items.append(f'''    <li class="lesson">
      <div class="l-num">{k + 1:02d}</div>
      <div class="l-body">
        <p class="eyebrow">Stunde {k + 1} · {meta.get("time", "1 Unterrichtsstunde")}</p>
        <h2>{meta["title"]}</h2>
        <p class="l-q"><b>Leitfrage:</b> {meta["q"]}</p>
        <ul class="facts">{facts}</ul>
        <p class="l-int"><span class="tag info">Interaktiv</span> {meta.get("inter", "")}</p>
      </div>
      <div class="l-go"><a class="btn" href="{path.stem}.pdf" target="_blank" rel="noopener">Arbeitsblatt</a><a class="btn primary" href="{path.name}">Öffnen →</a></div>
    </li>''')
    links = ''.join(f'\n  <a class="icon-btn" href="{h}">{t}</a>' for h, t in series.get('links', []))
    notes = '\n'.join(f'    <div class="box"><span class="tag {c}">{t}</span>\n      <p>{p}</p></div>' for t, c, p in series['notes'])
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{series["name"]} – Übersicht</title>
{FONTS}
<style>
{palette_css(series)}{css}
</style>
</head>
<body>
<div class="app">
<header class="top">
  <div class="brand"><b>{series["name"]}</b><span>{subj} · Klasse {grade}</span></div>
  <span style="flex:1"></span>
  <a class="icon-btn" href="../index.html#{gkey(series)}">⌂ Start</a>{links}
  <a class="icon-btn" href="#hinweise">Hinweise für Lehrkräfte</a>
</header>
<main>
<section class="ov">
  <div class="ov-hero">
    <div>
      <p class="eyebrow">Kapitel {series["chapter"]} · {len(lessons)} Stunde{"n" if len(lessons) != 1 else ""} · interaktive Präsentationen</p>
      <h1>{series["h1"]}</h1>
      <p class="lead">{series["lead"]}</p>
    </div>
    <div class="ov-facts">
      <div class="meter"><span>Stunden</span><b>{len(lessons)}</b><small>Präsentation{"en" if len(lessons) != 1 else ""}</small></div>
      <div class="meter"><span>Umfang</span><b>≈ {series["ue"]}</b><small>Unterrichtsstunden</small></div>
      <div class="meter"><span>Thema</span><b>{series["bp"]}</b></div>
    </div>
  </div>
  <ol class="lessons">
{chr(10).join(items)}
  </ol>
  <div class="section-head mt" id="hinweise"><p class="eyebrow">Für Lehrkräfte</p><h2>Hinweise zum Einsatz</h2></div>
  <div class="takeaway">
    <div class="box"><span class="tag info">Bedienung</span>
      <p>Blättern mit den Pfeiltasten, Bild↑/Bild↓ oder einem Presenter. <b>F</b> schaltet den Vollbildmodus. Über die Leiste oben springt man direkt zu jeder Station. Stationen lassen sich direkt verlinken, z. B. <code>{lessons[0][0].name}#merke</code>.</p></div>
    <div class="box"><span class="tag info">Aufbau jeder Stunde</span>
      <p>Start mit Leitfrage → nummerierte Stationen (Einstieg, Erarbeitung, Aufgaben) → <b>Hefteintrag</b>, der Punkt für Punkt aufgedeckt wird → <b>Übungen</b> mit Prüfen-Knopf und Lösung. Zu jeder Stunde gibt es ein Arbeitsblatt (PDF) mit Platz für den Hefteintrag und ein Lösungsblatt.</p></div>
{notes}
    <div class="box"><span class="tag info">Technik</span>
      <p>Jede Datei ist eigenständig und funktioniert offline, auch vom USB-Stick. Die Schriften liegen im Ordner <code>fonts</code> neben den Reihen. Hell- und Dunkelmodus folgen der Systemeinstellung.</p></div>
  </div>
</section>
</main>
</div>
</body>
</html>
'''
    (outdir / '00_Uebersicht.html').write_text(page, encoding='utf-8')


def gkey(series):
    """Klassenstufe als Anker: '5/6' -> 'klasse-5-6'."""
    return 'klasse-' + series['grade'].replace('/', '-')


GRADE_INFO = {'5/6': 'Informationen, Computer, Algorithmen mit Scratch, Bilder, Präsentieren, Textverarbeitung und Kommunikation im Netz.',
              '7': 'Netze und Internet, Codierung, Verschlüsselung, Informatik und Gesellschaft, Algorithmen mit Scratch.',
              '8': 'Mikrocontroller, maschinelles Lernen, Programmieren mit JavaScript, Tabellen und Datenbanken.'}

INDEX_CSS = '''.kitap-sub{font-style:italic;font-size:clamp(1rem,1.6vw,1.3rem);color:var(--ink-2);margin:-.2em 0 1.2rem}
.hero h1 .cur{display:inline-block;width:.55em;height:.95em;background:var(--accent);vertical-align:-.12em;margin-left:.1em;animation:blink 1.1s steps(1) infinite}
@media (prefers-reduced-motion: reduce){.hero h1 .cur{animation:none}}
.crumbs{display:flex;flex-wrap:wrap;align-items:center;gap:.2rem;margin:2rem 0 1.2rem;padding:.5rem .8rem;background:var(--bar);color:var(--bar-ink-2);border-radius:4px;font-family:var(--f-mono);font-size:.85rem;scroll-margin-top:5rem}
.crumbs::before{content:"$ cd";color:var(--led);margin-right:.4rem;font-weight:600}
.crumbs a{color:var(--bar-ink);text-decoration:none;padding:.1rem .3rem;border-radius:3px}
.crumbs a:hover{background:var(--bar-2);color:var(--led)}
.crumbs [aria-current]{color:var(--led);padding:.1rem .3rem}
.crumbs .sep{opacity:.6}
.vh{font-size:1.35rem;margin:0 0 1rem}
.grades{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:1.2rem}
.grade{display:flex;flex-direction:column;gap:.3rem;padding:1.1rem 1.2rem 1rem;text-decoration:none;color:inherit;background:var(--surface);border:1.5px solid var(--edge);border-radius:6px;box-shadow:4px 4px 0 var(--edge-shadow);transition:transform .08s,box-shadow .08s}
.grade:hover,.grade:focus-visible{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--edge-shadow)}
.grade:active{transform:translate(2px,2px);box-shadow:1px 1px 0 var(--edge-shadow)}
.g-lbl{font-family:var(--f-mono);font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--ink-2)}
.g-num{font-family:var(--f-mono);font-weight:600;font-size:clamp(3rem,8vw,4.6rem);line-height:1;color:var(--accent)}
.g-num::before{content:">";opacity:.35;margin-right:.1em}
.g-meta{font-family:var(--f-mono);font-size:.82rem;font-weight:600}
.g-txt{font-size:.9rem;color:var(--ink-2)}
.g-leds{display:flex;gap:.3rem;margin-top:auto;padding-top:.6rem}
.g-leds i{flex:1;height:.5rem;border-radius:2px;background:var(--accent)}
.lesson .l-num{color:var(--accent)}
.lesson{border-left:8px solid var(--accent)}
.topic-head{display:flex;flex-wrap:wrap;gap:1rem 2rem;align-items:flex-end;justify-content:space-between;margin-bottom:1.2rem}
.topic-head h2{margin:0 0 .3rem}
.topic-head p{margin:0;color:var(--ink-2);max-width:64ch}
.topic-head .eyebrow{margin-bottom:.4rem}
.rows{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.55rem}
.rows li{display:flex;gap:.55rem}
.row{flex:1;display:flex;align-items:center;gap:1rem;text-decoration:none;color:inherit;background:var(--surface);border:1.5px solid var(--edge);border-radius:5px;box-shadow:3px 3px 0 var(--edge-shadow);padding:.65rem .9rem;min-width:0}
.row:hover,.ws:hover{background:var(--surface-2)}
.row .no{font-family:var(--f-mono);font-weight:600;background:var(--accent);color:var(--accent-ink);border-radius:3px;padding:.15rem .45rem;flex:none}
.row .rt{flex:1;min-width:0;display:flex;flex-direction:column}
.row .rt small{color:var(--ink-2);font-size:.85rem}
.row .go{font-family:var(--f-mono);font-size:.8rem;color:var(--accent);font-weight:600;flex:none}
.ws{flex:none;display:grid;place-items:center;width:3.2rem;font-family:var(--f-mono);font-weight:600;font-size:.8rem;text-decoration:none;color:var(--ink);background:var(--surface);border:1.5px solid var(--edge);border-radius:5px;box-shadow:3px 3px 0 var(--edge-shadow)}
.site-foot{margin-top:3rem;color:var(--ink-2);font-size:.82rem}
.site-foot a{color:inherit}
.site-foot a:hover{color:var(--accent)}
@media (max-width:600px){.row .go{display:none}.grade{display:grid;grid-template-columns:auto 1fr;column-gap:1rem;align-items:center}.g-num{grid-row:1/4;grid-column:1}.g-txt,.g-leds{grid-column:1/-1}}
'''

INDEX_JS = '''(() => {
  const views = [...document.querySelectorAll('.view')], crumbs = document.getElementById('crumbs'), home = document.getElementById('home');
  function show() {
    let h = decodeURIComponent(location.hash.slice(1));
    if (!views.some(v => v.dataset.view === h)) h = '';
    views.forEach(v => v.hidden = v.dataset.view !== h);
    home.hidden = !h;
    const parts = h ? h.split('/') : [];
    let out = parts.length ? '<a href="#">~/klassen</a>' : '<span aria-current="page">~/klassen</span>';
    parts.forEach((p, i) => {
      const key = parts.slice(0, i + 1).join('/'), name = T[key] || p;
      out += '<span class="sep">/</span>' + (i === parts.length - 1 ? `<span aria-current="page">${name}</span>` : `<a href="#${key}">${name}</a>`);
    });
    crumbs.innerHTML = out;
    document.title = (h ? T[h] + ' – ' : '') + 'KITAP – Informatik';
  }
  addEventListener('hashchange', () => { show(); if (location.hash) crumbs.scrollIntoView({block: 'start', behavior: 'smooth'}); });
  show();
})();'''


def build_index(css):
    """Startseite: Klassenstufe wählen → Reihe wählen → Stunde wählen (wie bei Chemie, Ansichten über #Anker)."""
    grades = {}
    for k, s in enumerate(SERIES):
        files = sorted((HERE / 'src' / s['folder']).glob('[0-9][0-9]_*.html'))
        if not files:
            continue
        s = dict(s, idx=k, lessons=[(f, parse_lesson(f)[0]) for f in files])
        grades.setdefault(s['grade'], []).append(s)
    tiles, views, scss_l, scss_d, titles = [], [], [], [], {}
    for g, ss in grades.items():
        gk = gkey(ss[0])
        titles[gk] = f'Klasse {g}'
        n = sum(len(s['lessons']) for s in ss)
        leds = ''.join(f'<i class="s{s["idx"]}" title="{html.escape(s["name"])}"></i>' for s in ss)
        tiles.append(f'''    <a class="grade" href="#{gk}">
      <span class="g-lbl">Klasse</span><span class="g-num">{g}</span>
      <span class="g-meta">{len(ss)} Reihen · {n} Stunden</span>
      <span class="g-txt">{GRADE_INFO.get(g, '')}</span>
      <span class="g-leds" aria-hidden="true">{leds}</span>
    </a>''')
        cards, sviews = [], []
        for s in ss:
            titles[f'{gk}/{s["folder"]}'] = s['name']
            scss_l.append(f'.s{s["idx"]}{{--accent:{s["accent"][0]}}}')
            scss_d.append(f'.s{s["idx"]}{{--accent:{s["accent"][1]}}}')
            ln = len(s['lessons'])
            cards.append(f'''      <li class="lesson s{s["idx"]}">
        <div class="l-num">{s["chapter"]}</div>
        <div class="l-body"><p class="eyebrow">Kapitel {s["chapter"]} · {ln} Stunde{"n" if ln != 1 else ""} · ≈ {s["ue"]} Unterrichtsstunden</p><h2>{s["name"]}</h2><p class="l-q">{s["lead"]}</p></div>
        <div class="l-go"><a class="btn primary" href="#{gk}/{s["folder"]}">Stunden →</a><a class="btn" href="{s["folder"]}/00_Uebersicht.html">Übersicht</a></div>
      </li>''')
            rows = []
            for k2, (f, m) in enumerate(s['lessons']):
                rows.append(f'''        <li><a class="row" href="{s["folder"]}/{f.name}"><span class="no">{k2 + 1:02d}</span><span class="rt"><b>{m["title"]}</b><small>{m.get("q", "")}</small></span><span class="go">öffnen →</span></a><a class="ws" href="{s["folder"]}/{f.stem}.pdf" target="_blank" rel="noopener" title="Arbeitsblatt (PDF)">AB</a></li>''')
            sviews.append(f'''  <section class="view s{s["idx"]}" data-view="{gk}/{s["folder"]}" hidden>
    <div class="topic-head">
      <div><p class="eyebrow">Klasse {g} · Kapitel {s["chapter"]}</p><h2>{s["name"]}</h2><p>{s["lead"]}</p></div>
      <a class="btn primary" href="{s["folder"]}/00_Uebersicht.html">Übersicht der Reihe →</a>
    </div>
    <ol class="rows">
{chr(10).join(rows)}
    </ol>
  </section>''')
        views.append(f'''  <section class="view" data-view="{gk}" hidden>
    <h2 class="vh">Klasse {g}: Reihe wählen</h2>
    <ol class="lessons">
{chr(10).join(cards)}
    </ol>
  </section>''')
        views += sviews
    kcss = (''.join(scss_l) + '\n@media (prefers-color-scheme: dark){' + ''.join(':root:not([data-theme="light"]) ' + x for x in scss_d) + '}\n'
            + ''.join(':root[data-theme="dark"] ' + x for x in scss_d) + '\n')
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>KITAP – Informatik</title>
<meta name="description" content="Interaktive Präsentationen mit Arbeitsblättern für den Informatikunterricht der Klassen 5 bis 8.">
<link rel="stylesheet" href="fonts/fonts.css">
<style>
{palette_css()}{css}
{kcss}{INDEX_CSS}</style>
</head>
<body>
<div class="app">
<header class="top"><div class="brand"><b>KITAP</b><span>Informatik · interaktiv</span></div><span style="flex:1"></span><a class="icon-btn" href="#" id="home" hidden>⌂ Klassen</a></header>
<main>
<section class="ov">
  <div class="hero">
    <p class="eyebrow">Interaktive Präsentationen · Klassen 5–8</p>
    <h1>KITAP<span class="cur" aria-hidden="true"></span></h1>
    <p class="kitap-sub">Klassenfertige Inhalte – Thematisch Aufbereitet und Präsentationsbereit</p>
    <p class="lead">Präsentationen für Informatik und Medienbildung. Jede Stunde mit Stationen, Aufgaben, Hefteintrag, Übungen und Arbeitsblatt. Wähle zuerst die Klassenstufe, dann die Reihe.</p>
  </div>
  <nav class="crumbs" aria-label="Navigation" id="crumbs"><span aria-current="page">~/klassen</span></nav>
  <section class="view" data-view="">
    <h2 class="vh">Klassenstufe wählen</h2>
    <div class="grades">
{chr(10).join(tiles)}
    </div>
  </section>
{chr(10).join(views)}
  <footer class="site-foot">KITAP · freie Unterrichtsmaterialien · <a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></footer>
</section>
</main>
</div>
<script>
const T = {json.dumps(titles, ensure_ascii=False)};
{INDEX_JS}
</script>
</body>
</html>
'''
    (ROOT / 'index.html').write_text(page, encoding='utf-8')


def main(only=None):
    css, js = (HERE / 'style.css').read_text(encoding='utf-8'), (HERE / 'lib.js').read_text(encoding='utf-8')
    for s in SERIES:
        if only and s['folder'] not in only:
            continue
        files = sorted((HERE / 'src' / s['folder']).glob('[0-9][0-9]_*.html'))
        if not files:
            continue
        lessons = [(p, *parse_lesson(p)) for p in files]
        out = ROOT / s['folder']
        out.mkdir(exist_ok=True)
        for i in range(len(lessons)):
            build_lesson(s, i, lessons, out, css, js)
        build_overview(s, lessons, out, css)
        print('gebaut:', s['folder'], len(lessons), 'Stunde(n)')
    build_index(css)


if __name__ == '__main__':
    main(sys.argv[1:] or None)
