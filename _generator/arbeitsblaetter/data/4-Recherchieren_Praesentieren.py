from render import *

WS = {
'01_Recherchieren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die Funktionsweise einer Suchmaschine: Internet → Datenbank ← Suchanfrage → Trefferliste.',
    sections=[
    ('auftakt', [
        A('Nenne vier Suchmaschinen, darunter eine Kindersuchmaschine.', 1, 'z. B. Google, Bing, Ecosia, DuckDuckGo; Kindersuchmaschinen: fragFINN, Blinde Kuh, Helles Köpfchen'),
    ]),
    ('suchmaschine', [
        L('Eine Suchmaschine ist ein [[Programm]], das Informationen im Internet findet. Sie [[durchsucht]] ständig Webseiten und speichert die Inhalte sortiert in einer [[Datenbank]]. Welche Seiten oben stehen, hängt von den [[Suchbegriffen]], der [[Aktualität]] und der [[Beliebtheit]] einer Seite ab.'),
    ]),
    ('begriffe', [
        ZU('**M2** Ordne die Fachbegriffe zu.', ['Browser', 'URL', 'Suchbegriff', 'Trefferliste', 'Vorschautext'],
           ['Wort, das man in die Suchzeile eingibt', 'kurzer Ausschnitt einer Seite unter dem Treffer', 'Programm zur Darstellung von Webseiten', 'Adresse einer Webseite', 'alle Ergebnisse einer Suchanfrage'], loes=[3, 5, 1, 2, 4]),
    ]),
    ('m1', [
        A('**M1 Aufgabe 2:** Schreibe drei Tipps für Menschen, die noch nie im Internet recherchiert haben.', 3, 'genaue Suchbegriffe verwenden (Kaninchen statt Tier) // mehrere Ergebnisse vergleichen, nicht nur das erste // auf Werbung („Gesponsert“) achten; prüfen, wer die Seite gemacht hat und wie aktuell sie ist'),
    ]),
]),

'02_Suchoperatoren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere zu jedem Operator ein eigenes Beispiel.',
    sections=[
    ('praezise', [
        MC('Welche Suchanfrage liefert die genauesten Ergebnisse?', ['Bär', 'Tiere Wald Bär', '*Schwarzbär Verbreitungsgebiet', 'Bären und so']),
    ]),
    ('operatoren', [
        TAB('Ergänze die Tabelle der Operatoren.', ['Operator', 'Funktion', 'Beispiel'],
            [['„…“', '[[genaue Wortgruppe]]', '„Weltbevölkerung im Jahr 2040“'], ['-', '[[Wort ausschließen]]', '[[Jaguar -Auto]]'], ['site:', '[[nur auf einer Webseite suchen]]', '[[Mathematik site:beispielverlag.de]]'],
             ['OR', '[[das eine oder das andere]]', '[[Hund OR Katze]]'], ['filetype:', '[[nur bestimmte Dateitypen]]', '[[Zwergkaninchen filetype:pdf]]']], h=6.5, widths=[16, 40, 44]),
    ]),
    ('m4', [
        A('**M4:** Merle sucht „Welches Haustier ist das Beste?“. Der erste Treffer ist „Gesponsert“. Was bedeutet das, und wie sollte Merle vorgehen?', 2, '„Gesponsert“ bedeutet Werbung: Jemand hat dafür bezahlt, dass die Seite oben steht. Merle sollte mehrere seriöse Treffer vergleichen und genauere Suchbegriffe nutzen, z. B. „Haustier für Kinder“ Steckbrief.'),
    ]),
    ('m5', [
        GL('**M5** Verbessere die Suchanfragen mit Operatoren.', ['Hausaufgabenhilfe Bruchrechnen als PDF → [[Bruchrechnen Übungen filetype:pdf]]', 'Python, aber nicht die Schlange → [[Python -Schlange]]', 'genau der Satz Wer zuletzt lacht → [[„Wer zuletzt lacht“]]']),
    ]),
]),

'03_Praesentieren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege eine Tabelle an: Präsentationsmittel – Vorteil – Nachteil.',
    sections=[
    ('vorbereiten', [
        L('Eine gute Präsentation ist [[verständlich]], [[interessant]] und gut [[vorbereitet]]. Vorher klärt man Thema und Ziel, das [[Publikum]], die Anschaulichkeit, die [[Zeitplanung]] und die technische [[Ausstattung]].'),
    ]),
    ('mittel', [
        TAB('Nenne je einen Vorteil und einen Nachteil.', ['Präsentationsmittel', 'Vorteil', 'Nachteil'],
            [['Plakat', '[[bleibt hängen, kein Strom nötig]]', '[[wenig Platz, von hinten schlecht lesbar]]'], ['Präsentationssoftware', '[[Bilder, Videos, Diagramme möglich]]', '[[Technik kann ausfallen]]'], ['Anschauungsobjekt', '[[echt, zum Anfassen]]', '[[oft klein, nicht immer verfügbar]]']], h=7.5, widths=[28, 36, 36]),
    ]),
    ('m1', [
        ZU('**M1** Welches Präsentationsmittel wird genutzt?', ['Rollenspiel', 'Video', 'Anschauungsobjekt', 'Tafelbild', 'Plakat', 'Präsentationssoftware'],
           ['A Kinder spielen eine Szene', 'B Film über Fahrräder', 'C Modell des Herzens', 'D Diagramme an der Tafel', 'E „Der Baum“ mit Bildern', 'F Folien am Whiteboard'], loes=[1, 2, 3, 4, 5, 6]),
    ]),
]),

'04_Folien_gestalten': dict(skip=['uebungen'],
    heft_hint='Zeichne sieben kleine Rechtecke als Folien und beschrifte sie mit den Folientypen. Schreibe die Merksätze ab.',
    sections=[
    ('aufbau', [
        TAB('Ergänze die Folientypen in der richtigen Reihenfolge.', ['Nr.', 'Folientyp', 'Was steht darauf?'],
            [['1', '[[Titelfolie]]', '[[Titel, Name, Datum]]'], ['2', '[[Gliederungsfolie]]', '[[Überblick wie ein Inhaltsverzeichnis]]'], ['3', '[[Einleitungsfolie]]', '[[führt ins Thema ein, oft mit einer Frage]]'], ['4', '[[Inhaltsfolien]]', '[[Stichpunkte, Bilder, Diagramme]]'],
             ['5', '[[Abschlussfolie]]', '[[Zusammenfassung]]'], ['6', '[[Fragenfolie]]', '[[lädt zu Fragen und Feedback ein]]'], ['7', '[[Dankesfolie]]', '[[Verabschiedung]]']], h=6.5, widths=[8, 32, 60]),
    ]),
    ('layouts', [
        A('Wie fügt man eine neue Folie ein, und wozu dienen Layouts?', 2, '„Start“ → „Neue Folie“. Layouts geben Felder für Text und Bilder vor, sodass man nicht alles selbst gestalten muss; „Leer“ hat keine Felder.'),
    ]),
    ('m1', [
        BOX('**M1 Aufgabe 4:** Skizziere eine Inhaltsfolie mit dem Layout „Zwei Inhalte“ zu einem Thema deiner Wahl.', 34, loes='Titel oben; links Stichpunkte, rechts ein Bild'),
    ]),
]),

'05_Texte_Folien': dict(skip=['uebungen', 'check'],
    heft_hint='Schreibe die Merksätze ab und notiere die Merkzahl 7 · 6 · 18.',
    sections=[
    ('regeln', [
        L('Folientexte unterstützen den Vortrag: kurze [[Stichpunkte]] statt Fließtext, höchstens [[7]] Zeilen pro Folie, höchstens [[6]] Wörter pro Zeile und eine Schriftgröße von mindestens [[18]]–24 Pt.'),
    ]),
    ('formatieren', [
        A('Wie fügt man ein Textfeld ein und formatiert den Text?', 2, '„Einfügen“ → „Textfeld“ und ein Rechteck aufziehen. Text markieren und unter „Start“ Schriftgröße, fett, kursiv, Farbe oder Aufzählung wählen; Rechtsklick → „Text formatieren“ für Effekte.'),
    ]),
    ('barriere', [
        RF(['r|Dunkle Schrift auf hellem Hintergrund ist gut lesbar.', 'f|Wichtiges sollte man nur mit roter Farbe hervorheben.|Nicht nur über Farben unterscheiden, z. B. zusätzlich fett.', 'r|Ein Alternativtext beschreibt ein Bild für einen Screenreader.', 'f|Gelbe Schrift auf weißem Hintergrund hat einen starken Kontrast.|Der Kontrast ist zu schwach.']),
    ]),
    ('m1', [
        A('**M1:** Vergleiche die beiden Folien zu Fledermäusen. Welche ist besser gestaltet? Begründe.', 2, 'Die linke Folie: kurze Stichpunkte, wenige Zeilen, gut lesbar. Die rechte ist ein langer Fließtext, zu viele Wörter, das Publikum liest statt zuzuhören.'),
    ]),
]),

'06_Abbildungen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne ein Säulendiagramm zur Smartphone-Nutzung der drei Altersgruppen.',
    sections=[
    ('bilder', [
        A('Nenne zwei Gründe, Abbildungen in eine Präsentation einzufügen, und drei Arten von Abbildungen.', 2, 'Sie veranschaulichen, ziehen Aufmerksamkeit an und helfen beim Merken. // Bilder, Screenshots, Illustrationen (Formen, Symbole), Diagramme'),
    ]),
    ('anordnen', [
        TAB('Wie gelingt es?', ['Ich möchte …', 'So geht es'],
            [['ein Bild proportional vergrößern', '[[an der Ecke ziehen und Shift gedrückt halten]]'], ['ein Bild mittig setzen', '[[„Format“ → „Ausrichten“]]'], ['ein Bild hinter den Text legen', '[[„In den Hintergrund“]]']], h=7, widths=[38, 62]),
    ]),
    ('diagramm', [
        ZU('Welches Diagramm passt?', ['Säulen- oder Balkendiagramm', 'Kreisdiagramm'],
           ['Anteile der Schulwege an der ganzen Klasse', 'Smartphone-Nutzung der Altersgruppen vergleichen', 'Lieblingssportarten: Anzahl der Stimmen'], loes=[2, 1, 1]),
    ]),
]),

'07_Audio_Video': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere zwei Webseiten mit lizenzfreier Musik.',
    sections=[
    ('audio', [
        L('Audio einfügen: „[[Einfügen]]“ → „Audio“ → „Audio auf meinem PC“ oder „Audio [[aufnehmen]]“. Der Sound startet [[automatisch]] oder beim [[Klicken]].'),
    ]),
    ('probleme', [
        A('Nenne drei Probleme, die man beim Einfügen von Sounds vermeiden sollte.', 2, 'keine Musik ohne Nutzungsrechte // keine zu großen Dateien // angemessene Lautstärke, passend zu Thema und Stimmung'),
    ]),
    ('video', [
        L('Ein Video kürzt man über „[[Wiedergabe]]“ → „Video kürzen“. Der [[grüne]] Regler bestimmt den Anfang, der [[rote]] das Ende.'),
    ]),
    ('schritte', [
        A('Beschreibe in Schritten, wie man ein Video einfügt.', 2, '„Einfügen“ → „Medien“ → „Video“ → Speicherort wählen → „Einfügen“ → Größe am Rahmen anpassen.'),
    ]),
]),

'08_Urheberrecht': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere zu jeder Ausnahme beim Recht am eigenen Bild ein Beispiel.',
    sections=[
    ('urheber', [
        RF(['f|Was frei im Internet steht, darf ich verwenden.|Meist braucht man eine Erlaubnis des Urhebers.', 'r|Auch kleine Ausschnitte eines Liedes sind geschützt.', 'r|Wer das Urheberrecht verletzt, kann eine Geldstrafe bekommen.']),
    ]),
    ('bild', [
        TAB('Ausnahmen vom Recht am eigenen Bild', ['Ausnahme', 'Beispiel'],
            [['[[Beiwerk]]', 'Touristen klein vor dem Eiffelturm'], ['[[Versammlungen, große Veranstaltungen]]', '[[Konzert oder Demo ohne herausgehobene Einzelpersonen]]'], ['[[Bilder der Zeitgeschichte]]', '[[Politikerin im Parlament]]']], h=7, widths=[38, 62]),
    ]),
    ('ki', [
        A('**M2:** Nenne drei Anzeichen für ein KI-generiertes Bild und erkläre, was ein Deepfake ist.', 3, 'falsche Anzahl Finger, unmögliche Gegenstände (Würfel mit sieben Augen), fehlende Schatten oder krumme Linien. // Ein Deepfake ist eine mit KI erstellte Fälschung, die Personen in Situationen zeigt, die nie stattgefunden haben; damit werden falsche Informationen verbreitet.'),
    ]),
]),

'09_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Suchmaschine', 'URL', 'Operator', 'Alternativtext', 'Deepfake'],
           ['grenzt eine Suche ein', 'mit KI gefälschtes Video', 'Adresse einer Webseite', 'durchsucht und sortiert Webseiten', 'beschreibt ein Bild für Screenreader'], loes=[3, 5, 2, 1, 4]),
    ]),
    ('t1', [
        A('Welche Anfrage ist genauer: „Tiere im Wald“ oder „Ernährung Katze“ site:wwf.de? Begründe.', 1, 'Die zweite: genaue Wortgruppe in Anführungszeichen und auf eine Webseite beschränkt.'),
    ]),
    ('t2', [
        A('Nenne die sieben Folientypen in der richtigen Reihenfolge.', 1, 'Titel-, Gliederungs-, Einleitungs-, Inhalts-, Abschluss-, Fragen-, Dankesfolie'),
    ]),
    ('t3', [
        A('Freja möchte Umfrageergebnisse der Klasse zeigen. Welche Abbildung wählt sie?', 1, 'Ein Diagramm, z. B. Säulendiagramm (Anzahlen) oder Kreisdiagramm (Anteile).'),
    ]),
    ('t4', [
        A('Darfst du ein Video mit einem kurzen Ausschnitt eines bekannten Songs einfach posten? Begründe.', 1, 'Nein: Auch kleine Teile sind urheberrechtlich geschützt; man braucht eine Erlaubnis oder lizenzfreie Musik.'),
    ]),
]),
}
