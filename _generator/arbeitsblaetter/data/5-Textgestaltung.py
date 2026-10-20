from render import *

WS = {
'01_Texte_eingeben': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die Tasten Strg, C, X und V mit den passenden Shortcuts.',
    sections=[
    ('auftakt', [
        SORT('Ordne die Begriffe der Mindmap den Oberbegriffen zu.', ['Texte eingeben', 'Textfluss', 'Zellen', 'Thesaurus', 'Texte kopieren', 'Bilder zuschneiden', 'Spalten', 'Fehlererkennung'],
             ['Texte erstellen', 'Texte mit Bildern', 'Tabellen', 'Texte verbessern'], loes=[['Texte eingeben', 'Texte kopieren'], ['Textfluss', 'Bilder zuschneiden'], ['Zellen', 'Spalten'], ['Thesaurus', 'Fehlererkennung']]),
    ]),
    ('grundlagen', [
        L('Texte bestehen aus [[Sätzen]], diese aus [[Wörtern]] und Satzzeichen. Mit der [[Enter]]-Taste beginnt ein neuer Absatz. Die Rücktaste löscht das Zeichen [[links]] vom Cursor, die Entf-Taste das Zeichen [[rechts]] davon.'),
        TAB('Ergänze die Funktionen der Menüsymbole.', ['Befehl', 'Funktion'],
            [['Öffnen', '[[öffnet eine zuvor erstellte Datei]]'], ['Speichern', '[[speichert die Datei; beim ersten Mal Name und Speicherort wählen]]'], ['Speichern unter', '[[speichert unter neuem Namen oder in anderem Ordner]]'], ['Neu', '[[öffnet eine neue, leere Datei]]']], h=7, widths=[24, 76]),
    ]),
    ('oberflaeche', [
        ZU('Ordne die Bereiche der Benutzeroberfläche zu.', ['Menüleiste', 'Symbolleiste', 'Cursor', 'Statusleiste'],
           ['zeigt Seitenzahl und Wörterzahl', 'Registerkarten wie „Start“ oder „Einfügen“', 'blinkender Strich an der Schreibposition', 'Schaltflächen wie fett und kursiv'], loes=[4, 1, 3, 2]),
    ]),
    ('kopieren', [
        A('Beschreibe, wie man ein Wort an eine andere Stelle verschiebt. Nenne den Unterschied zum Kopieren.', 3, 'Wort markieren → Rechtsklick → „Ausschneiden“ → an die neue Stelle klicken → Rechtsklick → „Einfügen“. // Beim Kopieren bleibt das Wort an der alten Stelle stehen, beim Ausschneiden verschwindet es dort.'),
    ]),
    ('m1', [
        TAB('**M1** Welche Shortcuts sind mit Strg möglich?', ['Taste', 'Shortcut', 'Befehl'],
            [['C', 'Strg + C', '[[kopieren]]'], ['V', '[[Strg + V]]', '[[einfügen]]'], ['X', '[[Strg + X]]', '[[ausschneiden]]'], ['N', '[[Strg + N]]', '[[neues Dokument]]']], h=6.5, widths=[14, 30, 56]),
    ]),
]),

'02_Textfelder_Bilder': dict(skip=['uebungen', 'vorlagen'],
    heft_hint='Schreibe die Merksätze ab und zeichne drei Textflussoptionen als kleine Skizzen (Linien = Text, Kasten = Bild).',
    sections=[
    ('textfeld', [
        A('Was ist ein Textfeld und wofür kann man es nutzen?', 2, 'Ein Textfeld ist ein Objekt, das man an einer beliebigen Stelle im Dokument platzieren kann („Einfügen“ → „Textfeld“), z. B. für eine Infobox.'),
    ]),
    ('bilder', [
        L('Zieht man an einer [[Ecke]] des Bildes, wird es gleichmäßig skaliert. Zieht man an einer [[Seite]], wird es verzerrt. Mit gedrückter [[Shift]]-Taste bleibt das Seitenverhältnis erhalten.'),
    ]),
    ('zuschneiden', [
        A('Beschreibe in Schritten, wie man ein Bild zuschneidet.', 2, 'Bild markieren → „Bildformat“ → „Zuschneiden“ → die schwarzen Markierungen auf den gewünschten Bereich ziehen → erneut „Zuschneiden“ klicken.'),
    ]),
    ('textfluss', [
        ZU('**M1** Ordne die Textflussoptionen zu.', ['Mit Text in Zeile', 'Quadrat', 'Oben und unten', 'Hinter dem Text', 'Vor dem Text'],
           ['Das Bild liegt über dem Text und verdeckt ihn.', 'Der Text fließt um das Bild herum.', 'Das Bild steht wie ein Buchstabe im Text.', 'Text steht nur über und unter dem Bild.', 'Das Bild liegt wie ein Hintergrund hinter dem Text.'], loes=[5, 2, 1, 3, 4]),
    ]),
]),

'03_Zeichen_formatieren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Schreibe den Namen deiner Schule fünfmal und markiere, wie du jede Zeile formatieren würdest.',
    sections=[
    ('formate', [
        A('Nenne sechs verschiedene Formatierungen für Zeichen.', 2, 'Schriftart, Schriftgröße, fett, kursiv, unterstrichen, durchgestrichen, hoch-/tiefgestellt, Schriftfarbe, Texthervorhebung'),
    ]),
    ('sinnvoll', [
        TAB('Wozu nutzt man welche Formatierung?', ['Formatierung', 'Einsatz'],
            [['fett', '[[zentrale Begriffe, wichtige Aussagen]]'], ['kursiv', '[[Fachbegriffe, Zitate, Gedanken]]'], ['hoch-/tiefgestellt', '[[Formeln wie 2³ oder CO₂]]'], ['Aufzählung', '[[Listen, z. B. Zutaten]]']], h=7, widths=[30, 70]),
    ]),
    ('markieren', [
        GL('Wie markierst du …?', ['ein Wort → [[Doppelklick]]', 'einen Absatz → [[Dreifachklick]]', 'den ganzen Text → [[Strg + A]]']),
    ]),
    ('m1', [
        A('**M1:** Nenne drei Fehler in der Formatierung des Textes „Der Wasserkreislauf“ und verbessere sie.', 3, 'Die Überschrift ist nur unterstrichen → groß und fett, eigene Zeile. // H²O: Die 2 muss tiefgestellt sein (H₂O); „oben“ darf nicht hochgestellt sein. // Drei verschiedene Schriftarten → eine einheitliche Schrift; die Phasen als Aufzählung.'),
    ]),
]),

'04_Shortcuts_Symbolleiste': dict(skip=['uebungen', 'ausprobieren'],
    heft_hint='Schreibe die Merksätze ab und notiere deine fünf wichtigsten Shortcuts.',
    sections=[
    ('shortcuts', [
        TAB('Ergänze die Shortcuts unter Windows.', ['Befehl', 'Windows', 'Mac'],
            [['speichern', '[[Strg + S]]', 'cmd + S'], ['rückgängig', '[[Strg + Z]]', 'cmd + Z'], ['suchen', '[[Strg + F]]', 'cmd + F'], ['drucken', '[[Strg + P]]', 'cmd + P'], ['Absatz zentrieren', '[[Strg + E]]', 'cmd + E']], h=6.5, widths=[34, 33, 33]),
        A('Warum funktionieren Shortcuts nicht überall gleich?', 1, 'Sie hängen vom Betriebssystem (Windows, macOS) und von der Software ab.'),
    ]),
    ('memory', [
        ZU('Ordne die Shortcuts zu.', ['Strg + C', 'Strg + X', 'Strg + V', 'Strg + N'], ['einfügen', 'neues Dokument', 'kopieren', 'ausschneiden'], loes=[3, 4, 1, 2]),
    ]),
    ('symbolleiste', [
        ZU('Ordne die Funktionen der Symbolleiste zu.', ['Sortieren', 'Alle anzeigen ¶', 'Texthervorhebungsfarbe', 'Einzug vergrößern', 'Rahmen'],
           ['hinterlegt Text farbig wie ein Textmarker', 'rückt den Text ein', 'ordnet Zeilen alphabetisch', 'zieht eine Linie um den Text', 'zeigt Absatzmarken und Leerzeichen'], loes=[3, 4, 1, 5, 2]),
    ]),
]),

'05_Objekte_Klassen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die Objektkarte für den ersten Buchstaben deines Vornamens.',
    sections=[
    ('auto', [
        L('Ein roter Sportwagen ist ein konkretes [[Objekt]] der [[Klasse]] „Auto“. Seine Eigenschaften wie Farbe oder Leistung heißen [[Attribute]], ihre Werte (rot, 250 PS) [[Attributwerte]].'),
    ]),
    ('zeichen', [
        BOX('Fülle eine Objektkarte für den Buchstaben **A** aus: Schriftart Arial, 14 Pt, fett, blau.', 30, loes='Kopfzeile „Zeichen1 : ZEICHEN“; darunter Schriftart = Arial, Schriftgröße = 14 Pt, Schriftstil = fett, Farbe = blau'),
    ]),
    ('aufbau', [
        GL('Ergänze den Aufbau eines Textdokuments.', ['DOKUMENT besteht aus [[ABSCHNITTEN]]', 'ABSCHNITT besteht aus [[ABSÄTZEN]] (oder Grafiken, Tabellen)', 'ABSATZ besteht aus [[ZEICHEN]]']),
    ]),
    ('m2', [
        A('**M2:** Text A ist fett in 9 Pt, Text B kursiv in 11 Pt. Ordne die Objektkarten „Zeichen1: Schriftstil = kursiv, 11 Pt“ und „Zeichen2: Schriftstil = fett, 9 Pt“ zu.', 1, 'Zeichen1 gehört zu Text B, Zeichen2 zu Text A.'),
    ]),
    ('m3', [
        A('**M3:** Beschreibe, was ein Objektdiagramm zeigt.', 2, 'Ein Objektdiagramm zeigt einzelne Objekte mit ihren Attributen und ihre Beziehungen („besteht aus“), z. B. Textdokument → Abschnitte → Absätze → Zeichen.'),
    ]),
]),

'06_Texte_ueberarbeiten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere zu drei Wörtern je drei Synonyme.',
    sections=[
    ('pruefung', [
        TAB('Rechtschreibprüfung', ['Markierung', 'Bedeutung'], [['rote Wellenlinie', '[[Rechtschreib- oder Tippfehler]]'], ['blaue Wellenlinie', '[[Grammatik- oder Satzbaufehler]]']], h=7, widths=[30, 70]),
        A('Wie korrigiert man ein markiertes Wort, und warum muss man trotzdem selbst Korrektur lesen?', 2, 'Rechtsklick auf das Wort → Vorschlag wählen → „Ändern“. // Die Prüfung ist nicht immer verlässlich: Manche Fehler erkennt sie nicht, manche richtigen Wörter markiert sie.'),
    ]),
    ('m1', [
        GL('**M1** Verbessere die Fehler.', ['Hocky-Spiel → [[Hockey-Spiel]]', 'Manschaften → [[Mannschaften]]', 'mit voler Kraft → [[mit voller Kraft]]', 'einem spieler → [[einem Spieler]]']),
    ]),
    ('thesaurus', [
        L('Ein [[Thesaurus]] findet Wörter mit ähnlicher Bedeutung, sogenannte [[Synonyme]]. So vermeidet man [[Wortwiederholungen]].'),
    ]),
    ('m2', [
        A('**M2:** Ersetze „gut“ dreimal durch passende Synonyme: „Das Essen war gut. Die Lieferzeit war nicht so gut. Die Nachspeise war gut.“', 2, 'Das Essen war lecker. Die Lieferzeit war nicht so kurz. Die Nachspeise war köstlich.'),
    ]),
]),

'07_Tabellen': dict(skip=['uebungen', 'einfuegen'],
    heft_hint='Schreibe die Merksätze ab und zeichne eine Tabelle mit 3 Spalten und 4 Zeilen. Markiere eine Zeile, eine Spalte und eine Zelle farbig.',
    sections=[
    ('aufbau', [
        L('Eine Tabelle besteht aus [[Zellen]]. Sie sind in [[Zeilen]] (waagerecht, von links nach rechts) und [[Spalten]] (senkrecht, von oben nach unten) angeordnet.'),
    ]),
    ('zellen', [
        A('Wie fügt man eine Tabelle ein, und wie springt man in die nächste Zelle?', 2, '„Einfügen“ → „Tabelle“ → Anzahl der Spalten und Zeilen wählen. Mit der Tab-Taste, den Pfeiltasten oder per Mausklick in die nächste Zelle.'),
    ]),
    ('m1', [
        TAB('**M1** Übertrage Malikas Stundenplan (Mo: Deutsch, Deutsch, Engl., Engl., Mathe, Mathe · Di: Mathe, Mathe, ILZ, ILZ, Mathe, ILZ · Mi: Engl., Engl., ILZ, ILZ, Sport, Sport).', ['Std.', 'Mo', 'Di', 'Mi'],
            [['1.', '[[Deutsch]]', '[[Mathe]]', '[[Engl.]]'], ['2.', '[[Deutsch]]', '[[Mathe]]', '[[Engl.]]'], ['3.', '[[Engl.]]', '[[ILZ]]', '[[ILZ]]'], ['4.', '[[Engl.]]', '[[ILZ]]', '[[ILZ]]'], ['5.', '[[Mathe]]', '[[Mathe]]', '[[Sport]]'], ['6.', '[[Mathe]]', '[[ILZ]]', '[[Sport]]']], h=6, widths=[10, 30, 30, 30]),
    ]),
]),

'08_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Shortcut', 'Textfluss', 'Attribut', 'Thesaurus', 'Zelle'],
           ['findet Synonyme', 'Kästchen einer Tabelle', 'Tastenkombination für einen Befehl', 'wie der Text um ein Bild fließt', 'Eigenschaft eines Objekts'], loes=[4, 5, 1, 2, 3]),
    ]),
    ('t1', [
        GL('Ergänze die Shortcuts.', ['kopieren: Strg + [[C]]', 'ausschneiden: Strg + [[X]]', 'einfügen: Strg + [[V]]']),
    ]),
    ('t2', [
        A('Beschreibe eine Situation, in der ein Bild hinter dem Text liegen soll.', 1, 'z. B. ein Hintergrundbild auf einer Einladungskarte oder ein blasses Logo als Wasserzeichen.'),
    ]),
    ('t3', [
        GL('Verbessere die Rechtschreibfehler.', ['in den schuhle → [[in die Schule]]', 'Zhause fergaßen → [[zu Hause vergessen]]', 'schnel zurük → [[schnell zurück]]']),
    ]),
    ('t4', [
        A('Beschreibe eine Situation, in der du eine Tabelle einfügen würdest. Begründe.', 1, 'z. B. ein Stundenplan: Tage und Stunden lassen sich in Spalten und Zeilen übersichtlich ablesen.'),
    ]),
]),
}
