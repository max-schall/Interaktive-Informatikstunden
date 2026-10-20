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
  <a class="icon-btn" href="../index.html" title="Startseite: alle Reihen">⌂ Start</a>
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
  <a class="icon-btn" href="../index.html">⌂ Start</a>{links}
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
      <div class="meter"><span>Thema</span><b>{series["bp"]}</b><small>im Schulbuch</small></div>
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
      <p>Start mit Leitfrage → nummerierte Stationen (Einstieg, Erarbeitung, Buchaufgaben) → <b>Hefteintrag</b>, der Punkt für Punkt aufgedeckt wird → <b>Übungen</b> mit Prüfen-Knopf und Lösung. Zu jeder Stunde gibt es ein Arbeitsblatt (PDF) mit Platz für den Hefteintrag und ein Lösungsblatt.</p></div>
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


def build_index(css):
    cards = []
    for s in SERIES:
        src = HERE / 'src' / s['folder']
        n = len(list(src.glob('[0-9][0-9]_*.html')))
        if not n:
            continue
        cards.append(f'''    <li class="lesson k{s["chapter"]}">
      <div class="l-num">{s["chapter"]}</div>
      <div class="l-body"><p class="eyebrow">Kapitel {s["chapter"]} · Klasse {s["grade"]} · {n} Stunde{"n" if n != 1 else ""}</p><h2>{s["name"]}</h2><p class="l-q">{s["lead"]}</p></div>
      <div class="l-go"><a class="btn primary" href="{s["folder"]}/00_Uebersicht.html">Zur Reihe →</a></div>
    </li>''')
    # jede Kapitelkarte in ihrer Kapitelfarbe (hell / dunkel)
    lt = ''.join(f'.lesson.k{s["chapter"]}{{--accent:{s["accent"][0]}}}' for s in SERIES)
    dk = ''.join(f'.lesson.k{s["chapter"]}{{--accent:{s["accent"][1]}}}' for s in SERIES)
    kcss = (lt + '\n.lesson .l-num{color:var(--accent)}\n'
            + '@media (prefers-color-scheme: dark){' + dk.replace('.lesson', ':root:not([data-theme="light"]) .lesson') + '}\n'
            + dk.replace('.lesson', ':root[data-theme="dark"] .lesson') + '\n')
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>KITAP – Informatik</title>
<link rel="stylesheet" href="fonts/fonts.css">
<style>
{palette_css()}{css}
{kcss}.kitap-sub{{font-style:italic;font-size:clamp(1rem,1.6vw,1.3rem);color:var(--ink-2);margin:-.2em 0 1.2rem}}
.site-foot{{margin-top:3rem;color:var(--ink-2);font-size:.82rem}}
.site-foot a{{color:inherit}}
.site-foot a:hover{{color:var(--accent)}}
</style>
</head>
<body>
<div class="app">
<header class="top"><div class="brand"><b>KITAP</b><span>Informatik · interaktiv</span></div><span style="flex:1"></span></header>
<main>
<section class="ov">
  <p class="eyebrow">Interaktive Präsentationen</p>
  <h1>KITAP</h1>
  <p class="kitap-sub">Klassenfertige Inhalte – Thematisch Aufbereitet und Präsentationsbereit</p>
  <p class="lead">Präsentationen für Informatik und Medienbildung (Klasse 5/6). Jede Stunde mit Stationen, Buchaufgaben, Hefteintrag, Übungen und Arbeitsblatt.</p>
  <ol class="lessons">
{chr(10).join(cards)}
  </ol>
  <footer class="site-foot">KITAP · freie Unterrichtsmaterialien · <a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></footer>
</section>
</main>
</div>
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
