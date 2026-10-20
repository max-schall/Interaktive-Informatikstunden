# Interaktive IT-Stunden

Interaktive HTML-Präsentationen für den Informatikunterricht – gleicher Aufbau wie die Chemie-Präsentationen, eigenes Design.

- `index.html` – Startseite mit allen Reihen
- `<Klasse>-<Reihe>/00_Uebersicht.html` – Übersicht der Reihe mit Hinweisen für Lehrkräfte
- `<Klasse>-<Reihe>/01_….html` – Präsentation (eigenständig, offline lauffähig)
- `<Klasse>-<Reihe>/01_….pdf` / `01_…_Lösung.pdf` – Arbeitsblatt und Lösung
- `fonts/` – Schriften (müssen neben den Reihen liegen)
- `_generator/` – Quellen und Skripte

## Bauen

    cd _generator
    python3 build.py                                    # Präsentationen, Übersichten, Startseite
    cd arbeitsblaetter && python3 render.py 7-Informatiksysteme   # Arbeitsblätter (PDF)

Die Inhalte einer Stunde stehen in `_generator/src/<Reihe>/NN_Name.html` (Kopfkommentar mit Metadaten, Stationen als
`<section class="station">`, Skript am Ende). Design: `_generator/style.css`, Bausteine: `_generator/lib.js`,
Reihen: `_generator/series.py`. Die Aufgabentypen der Arbeitsblätter sind in `_generator/arbeitsblaetter/README.md` beschrieben.

## Online

Die Präsentationen sind über GitHub Pages erreichbar:
https://max-schall.github.io/Interaktive-Informatikstunden/

Die Arbeitsblätter enthalten einen QR-Code zur jeweiligen Präsentation (Adresse in `_generator/arbeitsblaetter/render.py`, `PAGES`).
