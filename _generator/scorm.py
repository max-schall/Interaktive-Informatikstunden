#!/usr/bin/env python3
"""Packt die Präsentationen und Arbeitsblätter als SCORM-1.2-Paket (z. B. für itslearning).
Aufruf: python3 scorm.py                                  → ein Paket mit allen Reihen (Start: index.html)
        python3 scorm.py 1-Informatiksysteme 2-Algorithmen → je Reihe ein eigenes Paket
Ausgabe: ../_scorm/*.zip – die Quelldateien bleiben unverändert.
Im Paket steht neben jedem Button „Arbeitsblatt“ zusätzlich ein Button „Lösungsblatt“."""
import html, re, sys, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
OUT = BASE / '_scorm'
FONTS = BASE / 'fonts'
# Links in andere Reihen (../<reihe>/...) lassen sich im Einzelpaket nicht auflösen → Anker entfernen.
CROSS_LINK = re.compile(r'\s*<a\b[^>]*href="\.\./[^"]*"[^>]*>.*?</a>', re.S)
# Button „Arbeitsblatt“ (Kopfleiste der Präsentation und Liste in der Übersicht)
SHEET_BTN = re.compile(r'<a class="(icon-btn|btn)" href="([^"/]+)\.pdf"([^>]*)>Arbeitsblatt</a>')

MANIFEST = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{ident}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd http://www.imsglobal.org/xsd/imsmd_rootv1p2p1 imsmd_rootv1p2p1.xsd http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>1.2</schemaversion>
  </metadata>
  <organizations default="org">
    <organization identifier="org">
      <title>{title}</title>
      <item identifier="item1" identifierref="res1">
        <title>{title}</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="res1" type="webcontent" adlcp:scormtype="sco" href="{start}">
{files}
    </resource>
  </resources>
</manifest>
'''


def add_solution_buttons(text, folder):
    """Ergänzt hinter jedem Button „Arbeitsblatt“ einen Button „Lösungsblatt“, sofern das Lösungsblatt existiert."""
    def repl(m):
        cls, stem, attrs = m.groups()
        if not (folder / f'{stem}_Lösung.pdf').exists():
            return m.group(0)
        attrs = attrs.replace('Arbeitsblatt zur Stunde', 'Lösungsblatt zur Stunde')
        return f'{m.group(0)}<a class="{cls}" href="{stem}_Lösung.pdf"{attrs}>Lösungsblatt</a>' if cls == 'btn' else \
            f'{m.group(0)}\n  <a class="{cls}" href="{stem}_Lösung.pdf"{attrs}>Lösungsblatt</a>'
    return SHEET_BTN.sub(repl, text)


def series_files(folder):
    """HTML-Seiten und PDFs (Arbeitsblatt + Lösung) einer Reihe."""
    pages = sorted(folder.glob('*.html'))
    pdfs = sorted(folder.glob('*.pdf'))
    return pages, pdfs


def write(target, ident, title, start, entries):
    """entries: Liste (Pfad im Paket, Quelle Path | str-Inhalt)."""
    files = '\n'.join(f'      <file href="{html.escape(n)}"/>' for n, _ in entries)
    OUT.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('imsmanifest.xml', MANIFEST.format(ident=ident, title=html.escape(title), start=start, files=files))
        for name, src in entries:
            if isinstance(src, str):
                z.writestr(name, src)
            else:
                z.write(src, name)
    print(f'{target.relative_to(BASE)}  ({len(entries)} Dateien, {target.stat().st_size / 1e6:.1f} MB)')


def series_folders():
    return sorted(d for d in BASE.iterdir() if d.is_dir() and d.name[0].isdigit())


def pack_all():
    """Ein Paket mit Startseite, allen Reihen, Schriften, Impressum und Datenschutz – Ordnerstruktur wie online."""
    entries = []
    for name in ('index.html', 'impressum.html', 'datenschutz.html'):
        if (BASE / name).exists():
            entries.append((name, (BASE / name).read_text(encoding='utf-8')))
    for folder in series_folders():
        pages, pdfs = series_files(folder)
        for p in pages:
            entries.append((f'{folder.name}/{p.name}', add_solution_buttons(p.read_text(encoding='utf-8'), folder)))
        entries += [(f'{folder.name}/{f.name}', f) for f in pdfs]
    entries += [(f'fonts/{f.name}', f) for f in sorted(FONTS.iterdir()) if f.is_file()]
    write(OUT / 'Informatik_alle_Reihen_scorm.zip', 'informatik_alle_reihen',
          'Interaktive Informatikstunden', 'index.html', entries)


def pack(folder):
    if not (folder / '00_Uebersicht.html').exists():
        print(f'übersprungen (keine 00_Uebersicht.html): {folder.name}')
        return
    m = re.search(r'<title>(.*?)</title>', (folder / '00_Uebersicht.html').read_text(encoding='utf-8'), re.S)
    title = html.unescape(m.group(1)).replace(' – Übersicht', '').strip() if m else folder.name
    ident = 'informatik_' + re.sub(r'[^A-Za-z0-9_]', '_', folder.name)
    pages, pdfs = series_files(folder)
    entries = []
    for p in pages:
        text = add_solution_buttons(p.read_text(encoding='utf-8'), folder)
        # Schriften liegen im Paket unter fonts/ statt ../fonts/
        entries.append((p.name, CROSS_LINK.sub('', text).replace('href="../fonts/', 'href="fonts/')))
    entries += [(f.name, f) for f in pdfs]
    entries += [(f'fonts/{f.name}', f) for f in sorted(FONTS.iterdir()) if f.is_file()]
    write(OUT / f'{folder.name}_scorm.zip', ident, title, '00_Uebersicht.html', entries)


def main(names):
    if not names:
        pack_all()
        return
    for n in names:
        pack(BASE / n)


if __name__ == '__main__':
    main(sys.argv[1:])
