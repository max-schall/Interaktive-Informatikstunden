#!/usr/bin/env python3
"""Öffnet alle Stunden einer Reihe headless, blättert durch alle Stationen, klickt Buttons und meldet JS-Fehler.
Aufruf: test.py <ordner> [--shots] [--dark]"""
import sys, re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SHOTS = Path(__file__).resolve().parent / 'shots'


def run(folders, shots=False, dark=False, only=None):
    SHOTS.mkdir(exist_ok=True)
    bad = 0
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/chromium-browser', args=['--no-sandbox'])
        ctx = b.new_context(viewport={'width': 1366, 'height': 820}, color_scheme='dark' if dark else 'light')
        for folder in folders:
            for f in sorted((ROOT / folder).glob('*.html')):
                if only and only not in f.name:
                    continue
                errs = []
                pg = ctx.new_page()
                pg.on('pageerror', lambda e: errs.append('pageerror: ' + str(e)))
                pg.on('console', lambda m: errs.append('console: ' + m.text) if m.type == 'error' and 'fonts' not in m.text else None)
                pg.goto(f.as_uri())
                pg.wait_for_timeout(300)
                ids = pg.eval_on_selector_all('.station', 'els => els.map(e => e.id)')
                for sid in ids:
                    pg.evaluate(f"document.querySelector('[data-go=\"{sid}\"]') && document.querySelector('[data-go=\"{sid}\"]').click()")
                    pg.wait_for_timeout(250)
                    # alle sichtbaren Buttons der Station einmal anklicken (außer Links)
                    btns = pg.query_selector_all(f'#{sid} button:visible')
                    for bt in btns[:40]:
                        try:
                            if bt.is_visible() and bt.is_enabled():
                                bt.click(timeout=500)
                        except Exception:
                            pass
                    pg.wait_for_timeout(150)
                    if shots:
                        pg.evaluate(f"document.querySelector('[data-go=\"{sid}\"]') && document.querySelector('[data-go=\"{sid}\"]').click()")
                        pg.wait_for_timeout(400)
                        pg.screenshot(path=str(SHOTS / f'{folder}_{f.stem}_{sid}{"_d" if dark else ""}.png'), full_page=True)
                # horizontale Überbreite prüfen
                ow = pg.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
                if ow > 2:
                    errs.append(f'horizontal overflow {ow}px')
                status = 'OK ' if not errs else 'ERR'
                if errs:
                    bad += 1
                print(f'{status} {folder}/{f.name} ({len(ids)} Stationen)')
                for e in dict.fromkeys(errs):
                    print('    ', e[:300])
                pg.close()
        b.close()
    return bad


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    only = None
    for a in sys.argv[1:]:
        if a.startswith('--only='):
            only = a[7:]
    sys.exit(1 if run(args, '--shots' in sys.argv, '--dark' in sys.argv, only) else 0)
