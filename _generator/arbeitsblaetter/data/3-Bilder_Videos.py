from render import *

GRID8 = ('<table class="t" style="margin:2.5mm 3mm .5mm;width:auto;border-collapse:collapse">' + ('<tr>' + '<td style="width:6mm;height:6mm;padding:0"></td>' * 8 + '</tr>') * 8 + '</table>')

WS = {
'01_Pixel_Rastergrafiken': dict(skip=['uebungen'], heft_tpl=GRID8,
    heft_hint='Male ein eigenes 8 · 8-Bild in das Raster und schreibe den Binärcode daneben. Schreibe dann die Merksätze ab.',
    sections=[
    ('pixel', [
        L('Digitale Bilder bestehen aus [[Pixeln]]. Jedes Pixel hat eine [[Farbe]] und eine [[Position]]. Je mehr Pixel ein Bild hat, desto höher ist seine [[Auflösung]].'),
    ]),
    ('sw', [
        BOXES('**A** Zeichne ein Schwarz-Weiß-Muster und schreibe die Binärcodierung daneben (schwarz = 0, weiß = 1).', ['Muster (8 · 8)', 'Binärcode'], 46,
              loes=['individuelles Muster', 'je Zeile 8 Ziffern; schwarze Kästchen = 0, weiße = 1']),
    ]),
    ('farbtiefe', [
        TAB('Ergänze die Tabelle zur Farbtiefe.', ['Farbtiefe', 'mögliche Farben', 'Beispiel'],
            [['1 Bit', '[[2]]', '[[Schwarz-Weiß-Bild]]'], ['8 Bit', '[[256]]', '[[Graustufenbild]]'], ['24 Bit', '[[über 16 Millionen]]', '[[Farbfoto (RGB)]]']], h=6.5, widths=[22, 34, 44]),
    ]),
    ('m2', [
        TAB('**M2** Ergänze die Dateiformate.', ['Format', 'Eigenschaft', 'Informationsverlust?'],
            [['JPEG', '[[spart Speicherplatz]]', '[[ja]]'], ['PNG', '[[Logos, durchsichtige Ebenen]]', '[[nein]]'], ['GIF', '[[Animationen aus Einzelbildern]]', '[[nein]]'], ['TIFF', '[[hohe Qualität, viel Speicher]]', '[[nein]]']], h=6.5, widths=[18, 52, 30]),
        A('**M2 Aufgabe 3:** Rico braucht ein Logo mit durchsichtigem Hintergrund. Wähle begründet ein Format.', 1, 'PNG: für Logos geeignet, unterstützt durchsichtige Ebenen, ohne Verlust.'),
    ]),
]),

'02_Komprimieren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Codiere „AAAABBBBBBCC“ und „0000011100“ mit der Lauflängencodierung.',
    sections=[
    ('kompression', [
        L('Bei der [[Datenkompression]] werden Datenmengen verkleinert. Komprimierte Daten brauchen [[weniger]] Speicher und lassen sich [[schneller]] übertragen, die Qualität kann aber [[sinken]].'),
    ]),
    ('verlust', [
        TAB('Vergleiche die beiden Arten der Kompression.', ['', 'verlustbehaftet', 'verlustfrei'],
            [['Was passiert?', '[[Informationen gehen verloren]]', '[[alle Informationen bleiben erhalten]]'], ['Beispiel', '[[Fotos (JPEG), Videos, Musik]]', '[[Text in E-Mails, Lauflängencodierung]]']], h=7, widths=[22, 39, 39]),
        A('**M1 Aufgabe 3:** Gibt es Bilder, die nicht für eine (verlustbehaftete) Kompression geeignet sind? Begründe.', 2, 'Ja, z. B. Röntgenbilder, Pläne oder Bilder mit kleinem Text: Hier dürfen keine Details verloren gehen.'),
    ]),
    ('rle', [
        GL('**A** Codiere mit der Lauflängencodierung.', ['AAAAABBCCCD → [[5A2B3C1D]]', '1111 1100 0011 1111 1000 0000 → [[61 40 71 70]]', 'XXXYYYYZ → [[3X4Y1Z]]']),
    ]),
    ('m2', [
        TAB('**M2** Komprimiere die Bitfolgen.', ['Bitfolge', 'Lauflängencode'],
            [['1100011', '[[21 30 21]]'], ['1000001', '[[11 50 11]]'], ['1010101', '[[11 10 11 10 11 10 11]]'], ['1001001', '[[11 20 11 20 11]]'], ['0000000', '[[70]]']], h=6, widths=[40, 60]),
    ]),
    ('m3', [
        BOX('**M3 Aufgabe 3:** Zeichne das Herz in ein 8 · 8-Raster (je 2 · 2 Pixel werden zu einem).', 42, loes='Herzform mit 8 · 8 Pixeln: oben zwei Bögen, unten Spitze in der Mitte.'),
    ]),
]),

'03_Farben_RGB': dict(skip=['uebungen'],
    heft_hint='Zeichne die beiden Farbkreise (CMY und RGB) farbig und schreibe die Merksätze ab.',
    sections=[
    ('mischen', [
        TAB('**A/B** Vergleiche die Farbmischungen.', ['', 'subtraktiv', 'additiv'],
            [['Grundfarben', '[[Cyan, Magenta, Yellow (CMY)]]', '[[Rot, Grün, Blau (RGB)]]'], ['alle gemischt', '[[Schwarz]]', '[[Weiß]]'], ['Einsatz', '[[Malen, Drucken]]', '[[Bildschirme]]']], h=7, widths=[24, 38, 38]),
    ]),
    ('rgb', [
        GL('Welche Farbe ergibt sich?', ['(255, 0, 0) = [[Rot]]', '(255, 255, 0) = [[Gelb]]', '(0, 0, 0) = [[Schwarz]]', '(255, 255, 255) = [[Weiß]]']),
        A('**M1 Aufgabe 1:** Erkläre, warum ein RGB-Bild drei Werte für ein Pixel codiert.', 2, 'Jede Bildschirmfarbe wird aus Rot, Grün und Blau gemischt; für jede Grundfarbe wird ein Helligkeitswert von 0 bis 255 gespeichert.'),
    ]),
    ('grau', [
        L('Im Graustufen-Modell hat jedes Pixel einen Helligkeitswert zwischen [[0]] (Schwarz) und [[255]] (Weiß).'),
        BOX('**M2 Aufgabe 3:** Male das Graustufenbild aus der Präsentation farbig an.', 40, loes='individuell gefärbte Version der Figur'),
    ]),
]),

'04_Bilder_bearbeiten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege eine Tabelle an: Einstellung – Wirkung – Beispiel.',
    sections=[
    ('editor', [
        TAB('Beschreibe die Einstellungen.', ['Einstellung', 'Was verändert sie?'],
            [['Helligkeit', '[[Bild wirkt heller oder dunkler]]'], ['Kontrast', '[[Unterschied zwischen hellen und dunklen Bereichen]]'], ['Sättigung', '[[wie stark die Farben leuchten]]']], h=7, widths=[24, 76]),
        A('Nenne drei Grundfunktionen der Bildbearbeitung am Smartphone.', 1, 'zuschneiden, drehen, spiegeln'),
    ]),
    ('filter', [
        TAB('**M1** Ordne den Filtern eine Stimmung zu.', ['Filter', 'Stimmung'], [['A warm, hell', '[[fröhlich]]'], ['B dunkel, kühl', '[[geheimnisvoll, spannend]]'], ['C schwarz-weiß', '[[ernst, traurig]]'], ['D bräunlich, verblasst', '[[nostalgisch]]']], h=6, widths=[40, 60]),
        A('**M1 Aufgabe 3:** Stelle Vermutungen an, warum die Filter in B und D genutzt wurden.', 2, 'B wirkt wie eine Nacht in der Großstadt: geheimnisvoll, spannend. D wirkt wie ein altes Foto: nostalgisch.'),
    ]),
    ('computer', [
        A('Nenne drei Wege, Bilder vom Smartphone auf den Computer zu übertragen.', 1, 'Kabel, Bluetooth, Clouddienst'),
        A('Nenne zwei Dinge, die ein Programm wie GIMP besser kann als das Smartphone.', 1, 'Bereiche auswählen und freistellen, mit dem Pinsel malen, Texte einfügen, Bilder übereinanderlegen'),
    ]),
]),

'05_Bildmanipulation': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere zu jedem Werkzeug ein Beispiel.',
    sections=[
    ('alltag', [
        L('Wird ein Foto so stark bearbeitet, dass es die Realität verfälscht, spricht man von [[Bildmanipulation]]. Das Foto ist dann nicht mehr [[authentisch]].'),
        A('Erkläre, warum manipulierte Bilder gefährlich sein können.', 2, 'Sie wirken echt, zeigen aber Situationen, die nie passiert sind. Damit kann man Menschen mobben oder Fehlinformationen verbreiten.'),
    ]),
    ('m2', [
        TAB('**M2 Aufgaben 1–2:** Ordne zu.', ['Bild', 'Grund für die Bearbeitung', 'Wirklichkeit'],
            [['A Wanderweg', '[[lebendige Farben]]', '[[leicht geändert]]'], ['B Astronaut und Mond', '[[Fantasywelt]]', '[[falsch]]'], ['C Porträt', '[[makelloses Hautbild]]', '[[leicht geändert]]'], ['D Explosion', '[[spannende Szene]]', '[[falsch]]']], h=6, widths=[30, 40, 30]),
        A('**M2 Aufgabe 3:** Beschreibe eine Situation, in der eine Bildbearbeitung negative Auswirkungen haben kann.', 2, 'z. B. ein montiertes peinliches Foto einer Mitschülerin in der Klassengruppe (Cybermobbing); Werbefotos mit unrealistischem Schönheitsideal.'),
    ]),
    ('werkzeuge', [
        ZU('Ordne die Werkzeuge ihren Funktionen zu.', ['Lasso', 'Magnet-Werkzeug', 'Zauberstab', 'Klon-Werkzeug'],
           ['wählt Bereiche mit gleicher Farbe aus', 'kopiert Bildbereiche an eine andere Stelle', 'Bereich frei abstecken', 'Linie legt sich an die Kanten eines Objekts'], loes=[3, 4, 1, 2]),
    ]),
    ('freistellen', [
        A('**M1 Aufgabe 2:** Notiere in Stichpunkten, wie du den roten Hintergrund entfernst und ersetzt.', 3, 'Zauberstab wählen, in den roten Hintergrund klicken; Auswahl löschen; neue Ebene darunter mit Farbe oder Bild füllen; als PNG speichern.'),
    ]),
]),

'06_Erklaervideos': dict(skip=['uebungen'],
    heft_hint='Übertrage die Übersicht der fünf Erklärvideo-Arten (Merkmale, Einsatz, Vor- und Nachteile).',
    sections=[
    ('arten', [
        TAB('Ergänze die Übersicht.', ['Art', 'Merkmale', 'Einsatz', 'Vor-/Nachteile'],
            [['Animationsvideo', '[[bewegte Grafiken]]', '[[komplizierte Vorgänge]]', '[[ansprechend, aber teuer]]'], ['Realfilm', '[[echte Menschen, Gegenstände]]', '[[Experimente, Interviews]]', '[[lebensnah, schwer nachzubearbeiten]]'],
             ['Screencast', '[[Bildschirmaufnahme]]', '[[Software-Tutorials]]', '[[einfach, wenig abwechslungsreich]]'], ['Whiteboard-Film', '[[Zeichnungen im Zeitraffer]]', '[[Unterrichtsinhalte]]', '[[übersichtlich, gute Planung nötig]]'],
             ['Stop-Motion', '[[Einzelbilder]]', '[[Geschichten, Abläufe]]', '[[kreativ, sehr zeitaufwendig]]']], h=8, widths=[20, 26, 26, 28]),
    ]),
    ('stopmotion', [
        A('Erkläre, wie ein Stop-Motion-Film entsteht.', 1, 'Man fotografiert viele Einzelbilder, bei denen sich die Figuren jeweils ein kleines Stück bewegen, und setzt sie zu einem Film zusammen.'),
    ]),
    ('m1', [
        TAB('**M1 Aufgabe 4:** Welche Filmart bietet sich an?', ['Inhalt', 'Filmart'],
            [['Interview führen', '[[Realfilm]]'], ['Bogenschießen erklären', '[[Realfilm]]'], ['Wachstum einer Bohnenpflanze', '[[Stop-Motion (Zeitraffer)]]'], ['Bau einer Pyramide im alten Ägypten', '[[Animationsvideo]]']], h=6, widths=[60, 40]),
        A('**M1 Aufgabe 5:** Erkläre, was man bei Realfilmen beachten sollte.', 2, 'Sie sind aufwendig und schwer nachzubearbeiten. Bei Personen gilt das Recht am eigenen Bild: vor der Veröffentlichung Einwilligung einholen.'),
    ]),
]),

'07_Videoproduktion': dict(skip=['uebungen'],
    heft_hint='Schreibe die Checkliste in drei Spalten (vorher – während – nachher) und die Lizenz-Zeichen ab.',
    sections=[
    ('checkliste', [
        SORT('Ordne die Schritte den Phasen zu.', ['Storyboard erarbeiten', 'deutlich sprechen', 'Video sicher speichern', 'Akku prüfen', 'Nebengeräusche vermeiden', 'Szenen schneiden'],
             ['vor der Aufnahme', 'während der Aufnahme', 'nach der Aufnahme'], h=14,
             loes=[['Storyboard erarbeiten', 'Akku prüfen'], ['deutlich sprechen', 'Nebengeräusche vermeiden'], ['Video sicher speichern', 'Szenen schneiden']]),
    ]),
    ('format', [
        A('Wann nutzt man das Querformat, wann das Hochformat?', 1, 'Querformat: mehrere Personen, Landschaften, Übersicht. Hochformat: einzelne Personen und Details.'),
    ]),
    ('m1', [
        A('**M1:** Nenne zwei typische Probleme beim Videodreh und gib je einen Tipp.', 2, 'zu dunkel → für Licht sorgen; Gegenlicht → Sonne im Rücken der Kamera; Personen laufen ins Bild → Drehort absperren, Probeszene'),
    ]),
    ('rechte', [
        ZU('Ordne die Lizenz-Zeichen zu.', ['CC', 'BY (Person)', 'NC (Dollar durchgestrichen)', 'ND (=)', '©'],
           ['darf kopiert, aber nicht bearbeitet werden', 'frei verwendbar', 'nicht ohne Erlaubnis verwendbar', 'mit Namensnennung verwendbar', 'verwendbar, wenn kein Geld verdient wird'], loes=[4, 1, 5, 2, 3]),
    ]),
    ('m2', [
        A('**M2:** Darf Lukas das Video vom Schulfest einfach auf YouTube stellen? Begründe.', 2, 'Nein: Seine Mitschüler sind deutlich erkennbar. Er braucht ihre (bzw. der Eltern) schriftliche Erlaubnis (Recht am eigenen Bild).'),
    ]),
]),

'08_Podcast': dict(skip=['uebungen'], heft_label='Skript', heft_title='Mein Podcast-Skript', heft_sub='Thema, Abschnitte, Audio',
    heft_hint='Schreibe hier das Skript für euren Podcast: Eröffnung (Intro), Wie heißt das Tier? Wo lebt es? Was frisst es? Besonderheit? Abschluss (Outro).',
    sections=[
    ('schritte', [
        A('Nenne die sieben Schritte zum eigenen Podcast in der richtigen Reihenfolge.', 2, 'Thema wählen → recherchieren → Aufnahme vorbereiten (Skript) → Ton aufnehmen → schneiden → Musik hinterlegen → als MP3 speichern'),
    ]),
    ('skript', [
        A('Erkläre, wozu man ein Skript braucht.', 1, 'Man spricht sicher und flüssig und vergisst nichts Wesentliches.'),
    ]),
    ('projekt', [
        TAB('Sammle Informationen für deinen Tier-Podcast.', ['Frage', 'Notizen'], [['Wie heißt das Tier?', ''], ['Wo lebt es?', ''], ['Was frisst es?', ''], ['Besonderheit?', '']], h=7, widths=[30, 70]),
    ]),
    ('bewertung', [
        INFO('Bewertet eure Podcasts mit dem Bewertungsbogen in der Präsentation.'),
    ]),
]),

'09_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Pixel', 'Farbtiefe', 'Lauflängencodierung', 'Sättigung', 'Screencast'],
           ['wie stark Farben leuchten', 'Bildschirmaufnahme für Tutorials', 'kleinster Bildpunkt', 'verlustfreie Kompression', 'Bits pro Pixel'], loes=[4, 5, 1, 3, 2]),
    ]),
    ('t1', [
        A('Bei welchem Dateiformat gehen beim Speichern Informationen verloren? Welches nutzt du für eine Animation?', 1, 'JPEG verliert Informationen; für Animationen GIF.'),
    ]),
    ('t2', [
        GL('Codiere bzw. decodiere.', ['0000111 → [[40 31]]', '21 30 21 → [[1100011]]']),
    ]),
    ('t3', [
        A('Beschreibe das RGB-Modell und wo es eingesetzt wird.', 1, 'Drei Werte (Rot, Grün, Blau) von 0 bis 255 pro Pixel; additive Mischung bei Bildschirmen.'),
    ]),
    ('t4', [
        A('Welche Erklärfilm-Art nutzt du für ein Tutorial zu einem Bildbearbeitungsprogramm? Begründe.', 1, 'Screencast: zeigt den Bildschirm, einfach zu erstellen.'),
    ]),
]),
}
