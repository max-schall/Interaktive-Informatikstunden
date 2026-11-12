from render import *

NS_TPL = ('<div class="tpl"><div class="bx" style="--c:#047857;height:7mm;flex:none;width:60mm">Anweisung</div><div class="bx" style="--c:#B45309;height:7mm;flex:none;width:60mm;text-align:center">Bedingung? ja | nein</div>'
          '<div class="bx" style="--c:#4338CA;height:7mm;flex:none;width:50mm">wiederhole …</div></div>')

WS = {
'01_Algorithmen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Schreibe einen Algorithmus zum Zähneputzen und prüfe die drei Bedingungen.',
    sections=[
    ('ablauf', [
        L('Ein einzelner Arbeitsschritt heißt [[Anweisung]]. Mehrere Anweisungen in einer festen Reihenfolge bilden eine [[Sequenz]] oder einen [[Ablauf]].'),
    ]),
    ('eigenschaften', [
        TAB('Welche Bedingung ist verletzt? Verbessere die Anweisung.', ['Anweisung', 'verletzte Bedingung', 'Verbesserung'],
            [['Gib etwas Mehl dazu.', '[[Eindeutigkeit]]', '[[Gib 200 g Mehl dazu.]]'], ['Rühre immer weiter.', '[[Endlichkeit]]', '[[Rühre 2 Minuten lang.]]'], ['Gib die Eier mit Schale dazu.', '[[Ausführbarkeit]]', '[[Schlage die Eier auf und gib sie dazu.]]']], h=8, widths=[34, 26, 40]),
    ]),
    ('roboter', [
        A('Übertrage das Händewaschen in eine Befehlsfolge im Imperativ. Beginne mit: „Drehe das Wasser auf.“', 4, 'Drehe das Wasser auf. Halte die Hände unter das Wasser. Halte eine Hand unter den Seifenspender. Drücke einmal. Verreibe die Seife 20 Sekunden. Spüle die Seife ab. Drehe das Wasser zu. Trockne die Hände ab.'),
    ]),
    ('m1', [
        A('**M1:** Schreibe den Algorithmus für den Roboter im Labyrinth (vor, links drehen, rechts drehen).', 2, 'Der Roboter schaut nach rechts: rechts drehen · 4× vor · links drehen · 6× vor'),
    ]),
]),

'02_Ablaufplan_Struktogramm': dict(skip=['uebungen'], heft_tpl=NS_TPL,
    heft_hint='Zeichne „Kaffee oder Tee“ einmal als Ablaufplan und einmal als Struktogramm. Schreibe dann die Merksätze ab.',
    sections=[
    ('ablaufplan', [
        A('Beschreibe den Ablaufplan „Milch finden“ für den Fall, dass die Milch nicht im Regal steht.', 2, 'Start → gehe zum Kühlregal → Milch da? nein → frage eine Mitarbeiterin → zurück zur Entscheidung → Milch da? ja → nimm die Milch → Ende.'),
    ]),
    ('symbole', [
        ZU('Ordne die Symbole zu.', ['abgerundetes Feld', 'Rechteck', 'Raute', 'Pfeil'], ['Leserichtung', 'Entscheidung', 'Start oder Ende', 'Anweisung'], loes=[4, 3, 1, 2]),
    ]),
    ('struktogramm', [
        BOX('Zeichne das Struktogramm: „Wenn die Ampel grün ist, gehe über die Straße, sonst warte.“', 30, loes='Kopfzeile „Ampel grün?“ mit Dreieck, links (ja) „gehe über die Straße“, rechts (nein) „warte“.'),
    ]),
    ('m1', [
        BOX('**M1:** Zeichne das Struktogramm „Kaffee oder Tee“.', 45, loes='Fülle Wasser in die Maschine · Verzweigung „Kaffeepulver vorhanden?“: ja → Lege Filter ein und fülle Pulver ein; Schalte die Maschine ein · nein → Mache einen Tee · danach: Trinke dein Getränk.'),
    ]),
]),

'03_Scratch': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne die Bühne mit Koordinatenkreuz und markiere (100 | 50) und (−200 | −100).',
    sections=[
    ('fenster', [
        ZU('Ordne die Bereiche des Scratch-Fensters zu.', ['Blockpalette', 'Skriptbereich', 'Bühne', 'Figurenliste'],
           ['alle Figuren des Projekts', 'Blöcke zu Skripten zusammenstecken', 'Codeblöcke der gewählten Kategorie', 'hier laufen die Programme ab'], loes=[4, 2, 1, 3]),
    ]),
    ('koordinaten', [
        L('Die Mitte der Bühne ist der Ursprung ([[0 | 0]]). Die x-Achse reicht von [[−240]] bis 240, die y-Achse von −180 bis [[180]].'),
    ]),
    ('bloecke', [
        SORT('Ordne die Blöcke den Kategorien zu.', ['gehe 10er Schritt', 'sage Hallo!', 'wiederhole 10 mal', '( ) + ( )', 'setze Punkte auf 0', 'drehe dich um 15 Grad', 'falls … dann'],
             ['Bewegung', 'Aussehen', 'Steuerung', 'Operatoren', 'Variablen'], h=14, loes=[['gehe 10er Schritt', 'drehe dich'], ['sage Hallo!'], ['wiederhole', 'falls … dann'], ['( ) + ( )'], ['setze Punkte']]),
    ]),
    ('erstes', [
        A('Beschreibe, was das Skript „Die Katze stellt sich vor“ macht.', 2, 'Die Katze springt nach links (−150 | 0), sagt „Hallo, ich bin Scratchy!“, gleitet zu einer zufälligen Position, sagt „Ich kann mich bewegen.“, springt in die Mitte und denkt „Fertig!“.'),
    ]),
    ('m1', [
        TAB('**M1:** Bringe die Projektphasen in die richtige Reihenfolge.', ['Testphase', 'Projektidee', 'Implementieren', 'Funktionen festlegen', 'Gliederung', 'Materialien festlegen'], [['[[6]]', '[[1]]', '[[5]]', '[[2]]', '[[4]]', '[[3]]']], h=6),
    ]),
]),

'04_Wiederholungen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne das Struktogramm für ein Sechseck.',
    sections=[
    ('zaehl', [
        TAB('Ergänze für regelmäßige Vielecke.', ['Figur', 'wiederhole … mal', 'drehe um … Grad'], [['Dreieck', '[[3]]', '[[120]]'], ['Quadrat', '4', '[[90]]'], ['Sechseck', '[[6]]', '[[60]]'], ['Achteck', '[[8]]', '[[45]]']], h=6),
    ]),
    ('vergleich', [
        A('Nenne zwei Vorteile von Schleifen.', 1, 'Programme werden kürzer und übersichtlicher; Änderungen müssen nur an einer Stelle gemacht werden.'),
    ]),
    ('endlos', [
        A('Erkläre den Unterschied zwischen einer Zählschleife und einer Endlosschleife.', 2, 'Die Zählschleife wiederholt eine feste Anzahl von Malen. Die Endlosschleife läuft immer weiter, bis das Programm gestoppt wird.'),
    ]),
    ('geschachtelt', [
        GL('Wie oft läuft der innere Block?', ['außen 6-mal, innen 4-mal: [[24]]-mal', 'außen 3-mal, innen 10-mal: [[30]]-mal']),
    ]),
    ('m1', [
        BOX('**M1:** Schreibe das Skript für eine Treppe mit 5 Stufen (Stufe 40 Schritte).', 30, loes='Wenn ⚑ angeklickt · wiederhole 5 mal: gehe 40er Schritt, drehe dich ↺ 90 Grad, gehe 40er Schritt, drehe dich ↻ 90 Grad'),
    ]),
]),

'05_Verzweigungen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Struktogramm „Freibad oder Buch“.',
    sections=[
    ('alltag', [
        SORT('Bedingte Anweisung oder Verzweigung mit Alternative?', ['Wenn es regnet, nimm einen Schirm.', 'Wenn es über 30 °C ist, gehe ins Freibad, sonst lies ein Buch.', 'Wenn die Ampel grün ist, gehe los.', 'Wenn die Antwort richtig ist, lobe, sonst nenne die Lösung.'],
             ['ohne Alternative', 'mit Alternative'], h=14, loes=[['Regen → Schirm', 'Ampel → los'], ['Freibad/Buch', 'richtig/Lösung']]),
    ]),
    ('ampel', [
        A('Erkläre, was die Katze bei roter Ampel macht und warum.', 1, 'Sie bleibt stehen: Die Bedingung „Ampel = Grün“ ist nicht erfüllt, die Anweisungen im falls-Block werden übersprungen.'),
    ]),
    ('sonst', [
        BOX('Zeichne das Struktogramm für das Rechenquiz (7 · 8).', 30, loes='frage „Was ist 7 · 8?“ · Verzweigung „Antwort = 56?“: ja → sage „Richtig!“, spiele Klang · nein → sage „Leider falsch …“'),
    ]),
    ('vergleich', [
        TAB('Welcher Zweig wird bei „Temperatur > 30“ ausgeführt?', ['Temperatur', '25', '30', '31', '40'], [['Zweig', '[[sonst]]', '[[sonst]]', '[[dann]]', '[[dann]]']], h=6),
    ]),
    ('m1', [
        TAB('**M1:** Was sagt die Katze?', ['Punkte', '35', '41', '50', '51'], [['Ausgabe', '[[üben]]', '[[knapp]]', '[[knapp]]', '[[bestanden]]']], h=6),
    ]),
]),

'06_Variablen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege die Trace-Tabelle für das Programm aus Station 2 an.',
    sections=[
    ('behaelter', [
        L('Eine Variable ist wie ein beschrifteter Behälter. Die Beschriftung ist der [[Name]], der Inhalt ist der [[Wert]]. Der Wert kann sich [[ändern]], der Name bleibt gleich.'),
    ]),
    ('trace', [
        TAB('Ergänze die Trace-Tabelle.', ['Anweisung', 'a', 'b'], [['setze a auf 3', '3', '–'], ['setze b auf 5', '[[3]]', '[[5]]'], ['ändere a um b', '[[8]]', '[[5]]'], ['ändere b um −2', '[[8]]', '[[3]]'], ['setze a auf b', '[[3]]', '[[3]]'], ['ändere a um 10', '[[13]]', '[[3]]']], h=6, widths=[50, 25, 25]),
    ]),
    ('punkte', [
        A('Erkläre, warum „setze Punkte auf 0“ am Anfang des Programms stehen muss.', 2, 'Sonst würde der alte Punktestand vom letzten Spiel weitergezählt. Die Variable wird zu Beginn initialisiert.'),
    ]),
    ('raten', [
        A('Beschreibe, welche Variablen das Zahlenraten-Spiel nutzt und wofür.', 2, '„Zahl“ speichert die Zufallszahl von 1 bis 20, „Versuche“ zählt, wie oft geraten wurde; die Antwort wird mit Zahl verglichen.'),
    ]),
    ('m1', [
        SORT('**M1:** Lokal oder global?', ['Lebenspunkte einer Figur', 'Spielstand', 'Größe der Katze', 'Level / Bühnenbild', 'verbleibende Zeit'], ['lokal', 'global'], h=14,
             loes=[['Lebenspunkte', 'Größe der Katze'], ['Spielstand', 'Level', 'Zeit']]),
    ]),
]),

'07_Abbruchbedingung': dict(skip=['uebungen'], heft_tpl=NS_TPL,
    heft_hint='Zeichne das Struktogramm „Nagel einschlagen“ mit Abbruchbedingung. Schreibe dann die Merksätze ab.',
    sections=[
    ('nagel', [
        L('Ist die Anzahl der Wiederholungen unbekannt, nutzt man eine Schleife mit [[Abbruchbedingung]]. Sie wird bei jedem [[Durchlauf]] geprüft. In Scratch: „wiederhole [[bis]] …“.'),
    ]),
    ('welche', [
        SORT('Welche Schleife passt?', ['20 Liegestütze', 'Treppe steigen bis oben', 'Quadrat zeichnen', 'Nudeln kochen, bis sie weich sind', 'Raten, bis die Zahl stimmt'], ['Zählschleife', 'Abbruchbedingung'], h=14,
             loes=[['Liegestütze', 'Quadrat'], ['Treppe', 'Nudeln', 'Raten']]),
    ]),
    ('rand', [
        A('Erkläre, warum das Programm „laufe bis zum Rand“ auch bei anderer Schrittweite funktioniert.', 2, 'Die Schleife zählt nicht, sondern prüft bei jedem Durchlauf, ob der Rand berührt wird. Die Anzahl der Durchläufe passt sich automatisch an.'),
    ]),
    ('jagd', [
        A('Nenne die Abbruchbedingung der Mäusejagd und was danach passiert.', 1, '„wird Mauszeiger berührt?“ – danach spielt die Katze einen Klang und sagt die Anzahl der Schritte.'),
    ]),
    ('m1', [
        TAB('**M1:** Vergleiche.', ['', 'kopfgesteuert', 'fußgesteuert'], [['Bedingung steht …', '[[oben, vor dem Durchlauf]]', '[[unten, nach dem Durchlauf]]'], ['mindestens …', '[[0 Durchläufe]]', '[[1 Durchlauf]]']], h=7),
    ]),
]),

'08_Spiel_Testen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege ein Testprotokoll mit fünf Testfällen für den Eintrittspreis an.',
    sections=[
    ('spiel', [
        A('Beschreibe, wie du „Fang die Katze“ schwieriger machen kannst.', 2, 'Die Wartezeit verkürzen, die Gleitzeit verkürzen, die Zeit (Runden) verringern, die Figur kleiner machen.'),
    ]),
    ('elemente', [
        ZU('Ordne die Spielelemente zu.', ['Variable Punkte', 'wiederhole bis Zeit = 0', 'gleite zu Zufallsposition', 'falls Mauszeiger berührt'],
           ['prüft, ob gefangen wurde', 'Spielschleife mit Abbruchbedingung', 'speichert den Spielstand', 'macht das Spiel unvorhersehbar'], loes=[4, 2, 3, 1]),
    ]),
    ('fehler', [
        SORT('Ordne die Fehlerarten zu.', ['Befehl falsch geschrieben', 'Division durch 0', 'Punkte werden abgezogen statt addiert', 'Endlosschleife', '< statt ≤'], ['Syntaxfehler', 'Laufzeitfehler', 'logischer Fehler'], h=14,
             loes=[['Befehl falsch geschrieben'], ['Division durch 0', 'Endlosschleife'], ['Punkte abgezogen', '< statt ≤']]),
    ]),
    ('m1', [
        TAB('**M1:** Testprotokoll für den Eintrittspreis.', ['Eingabe', 'erwartet', 'Ausgabe', 'ok?'], [['5', '[[0 €]]', '0 €', '[[ja]]'], ['6', '[[3 €]]', '0 €', '[[nein]]'], ['17', '[[3 €]]', '5 €', '[[nein]]'], ['18', '[[5 €]]', '5 €', '[[ja]]']], h=6),
        A('**M1:** Nenne die fehlerhaften Zeilen und verbessere sie.', 2, 'Zeile 3: alter < 6 statt alter <= 6. Zeile 5: alter <= 17 statt alter < 17.'),
    ]),
]),

'09_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Sequenz', 'Zählschleife', 'Abbruchbedingung', 'Variable', 'Grenzfall'],
           ['Testfall genau an einer Grenze', 'wiederhole n mal', 'Behälter mit Name und Wert', 'Anweisungen in fester Reihenfolge', 'wiederhole bis …'], loes=[5, 2, 4, 3, 1]),
    ]),
    ('t1', [
        A('**T1:** Nenne die drei Bedingungen an einen Algorithmus.', 1, 'Eindeutigkeit, Ausführbarkeit, Endlichkeit'),
    ]),
    ('t2', [
        GL('**T2:** Rechne.', ['Drehwinkel beim Fünfeck: [[72]]°', 'wiederhole 3 mal: wiederhole 4 mal: gehe 10er Schritt → [[120]] Schritte']),
    ]),
    ('t3', [
        GL('**T3:** Welchen Wert hat x am Ende?', ['setze x auf 12 · falls x > 10 dann ändere x um −3, sonst um 3 → x = [[9]]']),
    ]),
    ('t4', [
        A('**T4:** Erkläre den Unterschied zwischen einem Laufzeitfehler und einem logischen Fehler.', 2, 'Laufzeitfehler: Das Programm bricht während des Laufs ab oder hängt. Logischer Fehler: Es läuft, liefert aber falsche Ergebnisse.'),
    ]),
]),
}
