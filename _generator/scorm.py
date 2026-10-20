#!/usr/bin/env python3
"""Packt Reihen-Ordner als SCORM-1.2-Paket (z. B. für itslearning).
Aufruf: python3 scorm.py [1-Informatiksysteme 2-Algorithmen ...]   (ohne Argumente: alle Reihen)
Ausgabe: ../_scorm/<reihe>_scorm.zip – die Quelldateien bleiben unverändert."""
import html, re, sys, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
OUT = BASE / '_scorm'
FONTS = BASE / 'fonts'
# Links in andere Reihen (../<reihe>/...) lassen sich im Paket nicht auflösen → Anker entfernen.
CROSS_LINK = re.compile(r'\s*<a\b[^>]*href="\.\./[^"]*"[^>]*>.*?</a>', re.S)

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
    <resource identifier="res1" type="webcontent" adlcp:scormtype="sco" href="00_Uebersicht.html">
{files}
    </resource>
  </resources>
</manifest>
'''


def pack(folder):
    pages = sorted(folder.glob('*.html'))
    if not (folder / '00_Uebersicht.html').exists():
        print(f'übersprungen (keine 00_Uebersicht.html): {folder.name}')
        return
    m = re.search(r'<title>(.*?)</title>', (folder / '00_Uebersicht.html').read_text(encoding='utf-8'), re.S)
    title = html.escape(html.unescape(m.group(1)).replace(' – Übersicht', '').strip() if m else folder.name)
    ident = 'informatik_' + re.sub(r'[^A-Za-z0-9_]', '_', folder.name)
    fonts = sorted(f for f in FONTS.iterdir() if f.is_file())
    # Arbeitsblätter (ohne Lösungen) für den Button „Arbeitsblatt“
    sheets = [p.with_suffix('.pdf') for p in pages if p.with_suffix('.pdf').exists()]
    files = '\n'.join(f'      <file href="{html.escape(n)}"/>' for n in [p.name for p in pages + sheets] + [f'fonts/{f.name}' for f in fonts])
    OUT.mkdir(exist_ok=True)
    target = OUT / f'{folder.name}_scorm.zip'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('imsmanifest.xml', MANIFEST.format(ident=ident, title=title, files=files))
        for p in pages:
            # Schriften liegen im Paket unter fonts/ statt ../fonts/
            z.writestr(p.name, CROSS_LINK.sub('', p.read_text(encoding='utf-8')).replace('href="../fonts/', 'href="fonts/'))
        for f in sheets:
            z.write(f, f.name)
        for f in fonts:
            z.write(f, f'fonts/{f.name}')
    print(f'{target.relative_to(BASE)}  ({len(pages)} Seiten)')


def main(names):
    folders = [BASE / n for n in names] if names else sorted(
        d for d in BASE.iterdir() if d.is_dir() and d.name[0].isdigit())
    for f in folders:
        pack(f)


if __name__ == '__main__':
    main(sys.argv[1:])
