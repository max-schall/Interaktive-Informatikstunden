from render import *

# Vorgedruckte binäre Stellenwerttafel im Hefteintrag
PV_TPL = ('<table class="t" style="margin:2.5mm 3mm .5mm;width:auto"><tr>' + ''.join(f'<th style="width:11mm;text-align:center">{v}</th>' for v in [128, 64, 32, 16, 8, 4, 2, 1])
          + '</tr><tr>' + '<td style="height:7mm"></td>' * 8 + '</tr></table>')
FLOW_TPL = ('<div class="tpl"><div class="bx" style="--c:#C2410C;height:9mm;border-radius:5mm;text-align:center">Start</div><span class="ar">→</span>'
            '<div class="bx" style="--c:#2459D6;height:9mm">Anweisung</div><span class="ar">→</span><div class="bx" style="--c:#2459D6;height:9mm">Anweisung</div><span class="ar">→</span>'
            '<div class="bx" style="--c:#555;height:9mm;border-radius:5mm;text-align:center">Stopp</div></div>')

WS = {
'01_Binaersystem': dict(skip=['uebungen'], heft_tpl=PV_TPL,
    heft_hint='Trage die Zahl 28 in die Stellenwerttafel ein. Schreibe dann die Merksätze ab.',
    sections=[
    ('auftakt', [
        A('**A** Nenne drei Situationen, in denen Barcodes oder andere Codes gescannt werden.', 1, 'Supermarktkasse, Paketdienst, Bibliotheksausweis, Bordkarte, Konzertticket, Pfandautomat'),
        A('**C** Stelle Vermutungen an, ob man eine Anleitung für die Lösung eines Zauberwürfels erstellen kann.', 1, 'Ja: Es gibt Lösungsanleitungen mit festen Zugfolgen – ein Algorithmus.'),
    ]),
    ('binaer', [
        L('Computer arbeiten nur mit den Ziffern [[0]] und [[1]]. Eine solche Stelle heißt [[Bit]]. Im Binärsystem haben die Stellen die Werte 1, [[2]], [[4]], [[8]], [[16]] …'),
    ]),
    ('umrechnen', [
        GL('Rechne die Dualzahlen in Dezimalzahlen um (Aufgabe A).', ['1111₂ = 8 + 4 + 2 + 1 = [[15]]', '11100₂ = [[16 + 8 + 4]] = [[28]]', '101₂ = [[4 + 1]] = [[5]]']),
        BOX('Rechne die Dezimalzahl 162 mit dem Divisionsverfahren in eine Dualzahl um (M2 Aufgabe 3).', 34,
            loes='162:2=81 R0 · 81:2=40 R1 · 40:2=20 R0 · 20:2=10 R0 · 10:2=5 R0 · 5:2=2 R1 · 2:2=1 R0 · 1:2=0 R1 → von unten nach oben: 10100010₂'),
    ]),
    ('m1', [
        TAB('**M1** Schreibe die Dualzahlen der Lampenreihen auf und rechne um.', ['Lampen (64 32 16 8 4 2 1)', 'Dualzahl', 'Dezimalzahl'],
            [['○ ○ ● ○ ● ● ●', '10111₂', '23'], ['● ○ ○ ● ○ ● ○', '[[1001010₂]]', '[[74]]'], ['○ ○ ● ○ ○ ○ ●', '[[10001₂]]', '[[17]]'],
             ['○ ● ● ● ○ ● ○', '[[111010₂]]', '[[58]]'], ['○ ● ○ ○ ● ○ ●', '[[100101₂]]', '[[37]]']], h=6, widths=[42, 30, 28]),
        A('**M1 Aufgabe 3:** Welche LEDs müssen für 40, 33 und 17 leuchten?', 1, '40 = 32 + 8 → 0101000 · 33 = 32 + 1 → 0100001 · 17 = 16 + 1 → 0010001'),
    ]),
    ('m2', [
        A('**M2 Aufgabe 1:** Stelle die Bitfolge 10101001 als Dezimalzahl dar.', 1, '128 + 32 + 8 + 1 = 169'),
    ]),
]),

'02_Bits_Bytes': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die Einheiten-Treppe: Bit → Byte → KB → MB → GB → TB.',
    sections=[
    ('speichern', [
        L('Beim Speichern wird ein Dokument in einen [[Binärcode]] aus Nullen und Einsen übersetzt. Die kleinste Informationseinheit ist das [[Bit]].'),
    ]),
    ('bytes', [
        L('[[8]] Bit ergeben 1 Byte. Mit einem Byte gibt es 2⁸ = [[256]] Kombinationen. Der Buchstabe A wird als [[01000001]] codiert.'),
    ]),
    ('einheiten', [
        A('**A** Beschreibe den Unterschied zwischen Bits und Bytes.', 2, 'Ein Bit ist die kleinste Einheit (0 oder 1), ein Byte besteht aus 8 Bit. Speichergrößen gibt man in Byte an, Übertragungsgeschwindigkeiten in Bit pro Sekunde.'),
        GL('**B** Rechne um.', ['2 TB = [[2000]] GB', '5 B = [[40]] Bit', '2 MB = [[2 000 000]] B', '3000 MB = [[3]] GB']),
    ]),
    ('uebertragen', [
        L('Speichergrößen von Festplatten werden in [[Bytes]] angegeben. Datenübertragungen werden in [[Bit]] pro Sekunde angegeben.'),
    ]),
    ('m1', [
        TAB('**M1 Aufgabe 1:** Vergleiche die drei Handyverträge.', ['Angebot', 'Preis', 'Datenvolumen', 'Geschwindigkeit'],
            [['Telefonie All 100 GB', '5,99 €', '[[100 GB]]', '[[16 Mbit/s]]'], ['LTE All 5 + 3 GB', '9,99 €', '[[8 GB]]', '[[50 Mbit/s]]'], ['LTE All 50 GB', '24,99 €', '[[50 GB]]', '[[50 Mbit/s]]']], h=6, widths=[34, 18, 24, 24]),
        A('**M1 Aufgabe 2:** Gib Sebastian, der gerne streamt, eine Empfehlung.', 2, 'Streaming braucht viel Datenvolumen: Er sollte auf großes Datenvolumen und ausreichende Geschwindigkeit achten, z. B. 100 GB mit 16 Mbit/s.'),
        BOX('**M1 Aufgabe 3:** Ermittle die Downloadzeit eines 12 GB großen Films bei 50 Mbit/s.', 24, loes='12 GB = 12 000 MB = 96 000 Mbit; 96 000 : 50 = 1920 s = 32 Minuten'),
    ]),
]),

'03_Codierung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Schreibe deinen Namen in Brailleschrift und im Morsealphabet.',
    sections=[
    ('codieren', [
        A('**A** Nenne Möglichkeiten, Daten zu codieren, und beschreibe sie kurz.', 2, 'Andere Schrift (Kyrillisch), Binärcode (0 und 1), Brailleschrift (Punktmuster), Morsealphabet (kurze und lange Signale), Barcode, QR-Code'),
    ]),
    ('braille', [
        L('Die Blindenschrift wurde von [[Louis Braille]] entwickelt. Jeder Buchstabe besteht aus [[6]] Punkten, die man mit den Fingerspitzen [[ertasten]] kann.'),
    ]),
    ('morse', [
        A('**M1 Aufgabe 1:** Übersetze: • • • / − − − / • • •', 1, 'SOS'),
        GL('**M1 Aufgabe 2:** Schreibe im Morsealphabet.', ['Hund: [[•••• / ••− / −• / −••]]', 'Katze: [[−•− / •− / − / −−•• / •]]']),
        A('**M1 Aufgabe 3:** Erkläre die Vorteile des Morsecodes.', 2, 'Nachrichten kamen in Minuten statt Tagen an; der Code funktioniert mit Strom, Licht, Ton oder Klopfzeichen, auch in Notfällen.'),
    ]),
    ('verbraucher', [
        TAB('Entschlüssele den Erzeugercode **1-DE-0812345**.', ['Teil', 'Bedeutung'], [['1', '[[Freilandhaltung]]'], ['DE', '[[Deutschland]]'], ['08…', '[[Bundesland Baden-Württemberg, Betrieb und Stall]]']], h=6, widths=[20, 80]),
        A('**M2 Aufgabe 3:** Welche Städte sind codiert? M XY 549; F GH 4536; L C 542', 1, 'München, Frankfurt am Main, Leipzig'),
    ]),
    ('maschinen', [
        A('Beschreibe, was beim Einscannen eines Barcodes an der Kasse passiert.', 2, 'Der Scanner liest die Striche, der Computer decodiert sie in einen Binärcode, interpretiert die Daten und verbucht Bezeichnung und Preis des Artikels.'),
    ]),
    ('qr', [
        ZU('**M3 Aufgabe 2:** Ordne die Bereiche des QR-Codes ihren Aufgaben zu.', ['Positionsmarkierungen', 'Synchronisationslinien', 'Ausrichtungsmarkierung', 'Datenfeld'],
           ['zeigen dem Scanner die Größe des Datenfeldes', 'enthält die Daten, jede Zelle 1 Bit', 'zeigen dem Scanner die Ausrichtung des Codes', 'zusätzliche Orientierung bei großen QR-Codes'], loes=[2, 4, 1, 3]),
        A('**M3 Aufgabe 4:** Begründe, warum ein QR-Code mehr Daten speichern kann als ein EAN-Barcode.', 1, 'Der QR-Code ist zweidimensional (Zeilen und Spalten aus Zellen), der Barcode nur eine Reihe von Strichen mit 13 Ziffern.'),
    ]),
]),

'04_Algorithmen_Alltag': dict(skip=['uebungen'], heft_tpl=FLOW_TPL,
    heft_hint='Schreibe die Merksätze ab und ergänze darunter einen Algorithmus für eine Tätigkeit deiner Wahl.',
    sections=[
    ('anweisungen', [
        L('Ein einzelner Arbeitsschritt heißt [[Anweisung]]. Hintereinander ausgeführte Anweisungen nennt man [[Ablauf]] oder [[Sequenz]].'),
        A('Nummeriere die Pfannkuchen-Schritte: Teig in die Pfanne geben · Eier aufschlagen · Öl erhitzen · Pfannkuchen wenden · Teig vermengen', 1, '1 Eier aufschlagen, 2 Teig vermengen, 3 Öl erhitzen, 4 Teig in die Pfanne geben, 5 Pfannkuchen wenden'),
    ]),
    ('eigenschaften', [
        TAB('**A** Nenne und beschreibe die Bedingungen eines Algorithmus.', ['Bedingung', 'Beschreibung'],
            [['[[Eindeutigkeit]]', '[[Anweisungen sind klar beschrieben, Reihenfolge ist festgelegt]]'], ['[[Ausführbarkeit]]', '[[jede Anweisung ist sinnvoll und ausführbar]]'], ['[[Endlichkeit]]', '[[der Ablauf hat ein klar formuliertes Ende]]']], h=7, widths=[28, 72]),
    ]),
    ('m1', [
        A('**M1 Aufgabe 2:** Schreibe das Händewaschen als Befehlsfolge. Beginne mit: „Halte eine Hand unter den Seifenspender.“', 3,
          'Halte eine Hand unter den Seifenspender. Halte die Hände unter das Wasser. Verreibe die Seife gründlich. Spüle die Seife ab. Trockne die Hände ab.'),
        A('**M1 Aufgabe 4:** Können einige Anweisungen vertauscht werden?', 1, 'Seife nehmen und Hände anfeuchten ja; Abspülen und Abtrocknen nicht.'),
    ]),
    ('m2', [
        A('**M2:** Erstelle eine Ablaufbeschreibung für den Fluchtweg aus deinem Klassenzimmer.', 3, 'individuell, Anweisungen im Imperativ mit genauen Angaben (links/rechts, wie weit), Ende am Sammelplatz'),
    ]),
]),

'05_Algorithmen_darstellen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne einen Ablaufplan mit Start, drei Anweisungen und Stopp.',
    sections=[
    ('beschreiben', [
        L('Damit ein Computer einen Algorithmus ausführen kann, wird er in eine [[Programmiersprache]] übersetzt. So entsteht ein [[Programm]]. Ein Algorithmus überführt eine Eingabe ([[Problem]]) in eine Ausgabe ([[Lösung]]).'),
    ]),
    ('ablaufplan', [
        BOX('**A** Erstelle einen Ablaufplan zu einer Tätigkeit, die du jeden Tag machst.', 52, loes='individuell; Start → Anweisungen im Imperativ → Stopp, verbunden mit Pfeilen'),
    ]),
    ('m1', [
        A('**M1 Aufgabe 1:** Bringe die Geschichte in die richtige Reihenfolge: Er kauft ein Bahnticket. · In der Hauptstadt trifft er den Wesir. · Irving will in die Hauptstadt reisen. · Irving fährt mit der Bahn los.', 1,
          'Irving will in die Hauptstadt reisen. → Er kauft ein Bahnticket. → Irving fährt mit der Bahn los. → In der Hauptstadt trifft er den Wesir.'),
    ]),
    ('m2', [
        A('**M2:** „Biege ein paar Schritte danach rechts ab. Bei den Konserven oder dem Mehl stehen die Nudeln.“ Begründe, warum diese Anweisungen nicht eindeutig sind, und verbessere sie.', 3,
          '„Ein paar Schritte“ und „Konserven oder Mehl“ sind ungenau. Besser: „Gehe 5 Schritte geradeaus. Biege rechts in Gang 3 ab. Nimm die Nudeln aus dem zweiten Regal links.“'),
    ]),
    ('m3', [
        BOX('**M3:** Stelle die Anweisungssequenz für den Traktor im Labyrinth als Ablaufplan dar.', 40,
            loes='Start → Fahre 2 Felder → Drehe rechts → Fahre 2 Felder → Drehe rechts → Fahre 2 Felder → Drehe links → Fahre 2 Felder → Drehe links → Fahre 4 Felder → Drehe links → Fahre 4 Felder → Drehe rechts → Fahre 2 Felder → Drehe rechts → Fahre 6 Felder → Stopp'),
    ]),
]),

'06_Scratch_Umgebung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die Bühne mit Koordinatenkreuz und den vier Randpunkten.',
    sections=[
    ('fenster', [
        ZU('Ordne die Bereiche des Scratch-Fensters ihren Aufgaben zu.', ['Codebereich', 'Skriptbereich', 'Bühne', 'Figurenliste', 'Registerkarten'],
           ['hier läuft das Programm ab', 'Wechsel zwischen Code, Kostümen und Klängen', 'listet alle Codeblöcke auf', 'hier steckt man die Blöcke zusammen', 'hier wählt man Figuren aus'], loes=[3, 5, 1, 4, 2]),
        A('**A** Beschreibe, was eine visuelle Programmiersprache ist.', 2, 'Man programmiert mit grafischen Blöcken, die wie Puzzleteile zusammengesteckt werden, statt Code zu tippen.'),
    ]),
    ('buehne', [
        L('Die Mitte der Bühne ist der Ursprung ([[0]]|[[0]]). Die x-Werte reichen von [[−240]] bis [[240]], die y-Werte von [[−180]] bis [[180]].'),
        BOX('Zeichne ein Koordinatensystem der Bühne. Markiere die Katze bei (100|−50) und einen Ball bei (−200|150).', 45, loes='Katze rechts unterhalb der Mitte, Ball links oben nahe dem Rand.'),
    ]),
    ('figuren', [
        TAB('**M1 Aufgabe 2:** Beschreibe die Auswirkungen, wenn du die Attribute veränderst.', ['Attribut', 'Auswirkung'],
            [['Größe', '[[Figur wird größer oder kleiner (100 = normal)]]'], ['Richtung', '[[Figur dreht sich (90 = rechts, 0 = oben)]]'], ['Sichtbarkeit', '[[Figur wird gezeigt oder versteckt]]'], ['Position', '[[Figur steht an anderer Stelle (x, y)]]']], h=7, widths=[24, 76]),
    ]),
]),

'07_Wiederholungen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne die drei Schleifenblöcke mit je einem Alltagsbeispiel.',
    sections=[
    ('schleifen', [
        L('Ein anderes Wort für Wiederholung ist [[Schleife]]. Damit lässt sich eine [[Sequenz]] von Anweisungen wiederholen.'),
    ]),
    ('zaehl', [
        A('Beschreibe, was das Programm „wiederhole 4 mal: gehe 100 er Schritt, drehe dich um 90 Grad“ macht.', 1, 'Die Figur zeichnet bzw. läuft ein Quadrat ab.'),
        A('Wie musst du das Programm ändern, damit ein Dreieck entsteht?', 1, 'wiederhole 3 mal, drehe dich um 120 Grad'),
    ]),
    ('endlos', [
        A('Erkläre, was eine Endlosschleife ist und wie sie meist entsteht.', 2, 'Die Anweisungen werden unendlich oft wiederholt. Manchmal ist das gewollt, meist entsteht sie durch einen Programmierfehler und muss gestoppt werden.'),
    ]),
    ('bedingung', [
        A('**A** Nenne den Unterschied zwischen einer Endloswiederholung und einer Wiederholung mit Bedingung.', 2, 'Die Endlosschleife hört nie auf; die Wiederholung mit Bedingung endet, sobald die Bedingung wahr ist.'),
    ]),
    ('m2', [
        BOX('**M2 Aufgabe 1:** Erstelle einen Ablaufplan zum Nagel-Einschlagen.', 42, loes='Start → Nimm den Nagel → Richte ihn aus → Nimm den Hammer → Schlage leicht ein → Nimm die Hand weg → ◇ Nagel versenkt? nein → Schlage auf den Nagel (zurück zur Frage) / ja → Stopp'),
        A('**M2 Aufgabe 2:** Welche Art von Wiederholung ist das? Begründe.', 1, 'Wiederholung mit Bedingung: Man schlägt, bis der Nagel versenkt ist; die Anzahl ist vorher nicht bekannt.'),
    ]),
]),

'08_Bedingungen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne einen Ablaufplan mit Verzweigung (Raute mit ja/nein).',
    sections=[
    ('ampel', [
        L('Ist eine [[Bedingung]] mit einer Anweisung verknüpft, spricht man von einer [[bedingten Anweisung]]. In Scratch nutzt man den Block „falls … [[dann]]“.'),
    ]),
    ('verzweigung', [
        A('**B** Beschreibe den Unterschied zwischen einer bedingten Anweisung und einer Verzweigung.', 2, 'Bei der bedingten Anweisung passiert nur etwas, wenn die Bedingung erfüllt ist. Bei der Verzweigung gibt es zusätzlich eine Alternative („sonst“).'),
    ]),
    ('mathe', [
        A('Die Katze fragt „Wie viel ist 1+1?“. Beschreibe, was bei der Antwort „2“ und bei der Antwort „3“ passiert.', 1, 'Bei „2“ ist die Bedingung erfüllt: „Mathe-Profi!“. Bei „3“ nicht: „Nochmal üben!“'),
    ]),
    ('m1', [
        TAB('**M1 Aufgaben 1–2:** Ordne zu und nenne die Bedingung.', ['Satz', 'bedingte Anweisung oder Verzweigung?', 'Bedingung'],
            [['A: Freibad ab 30 °C', '[[bedingte Anweisung]]', '[[über 30 °C]]'], ['B: Einkaufswagen oder -korb', '[[Verzweigung]]', '[[Einkaufschip vorhanden]]'], ['C: Aufstehen beim Wecker', '[[bedingte Anweisung]]', '[[Wecker klingelt]]']], h=7, widths=[34, 36, 30]),
    ]),
    ('m2', [
        A('**M2 Aufgabe 1:** Formuliere für das Navi eine passende Bedingung.', 1, 'Falls auf der L 311 Stau ist, dann fahre über die K 47, sonst über die L 311.'),
    ]),
]),

'09_Sequenzen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Skript aus M1 farbig ab.',
    sections=[
    ('bloecke', [
        A('**A** Beschreibe die Rollen von Codebereich und Skriptbereich.', 2, 'Der Codebereich listet alle Blöcke nach Kategorien auf. Im Skriptbereich werden sie zu einem Programm (Skript) zusammengesteckt.'),
        TAB('**M1 Aufgabe 1:** Ordne die Codeblöcke den Kategorien zu.', ['Codeblock', 'Kategorie'],
            [['Wenn ⚑ angeklickt wird', '[[Ereignisse]]'], ['gleite in 1 Sek. zu Zufallsposition', '[[Bewegung]]'], ['warte 1 Sekunden', '[[Steuerung]]'], ['spiele Klang Miau', '[[Klang]]'], ['sage Hallo! für 2 Sekunden', '[[Aussehen]]']], h=6, widths=[55, 45]),
    ]),
    ('sequenz', [
        L('Untereinander gesteckte Blöcke bilden eine [[Sequenz]]. Sie beginnt mit einem [[Startblock]] aus der Kategorie „Ereignisse“. Die Blöcke laufen von [[oben]] nach [[unten]] ab.'),
    ]),
    ('m1', [
        TAB('**M1 Aufgabe 3:** Verändere Werte und dokumentiere deine Beobachtungen.', ['Block', 'Wert vorher', 'Wert nachher', 'Beobachtung'],
            [['gleite in … Sek.', '1', '', ''], ['warte … Sekunden', '1', '', ''], ['sage … für … Sekunden', 'Hallo!, 2', '', '']], h=7, widths=[30, 18, 18, 34]),
        BOX('Schreibe ein eigenes Skript aus einem Startblock und vier Anweisungen. Notiere neben jedem Block die Kategorie.', 50, loes='individuell, z. B. Wenn ⚑ angeklickt (Ereignisse) – gehe 50 (Bewegung) – wechsle zum nächsten Kostüm (Aussehen) – spiele Klang Miau (Klang) – sage Tschüss! (Aussehen)'),
    ]),
]),

'10_Projekte': dict(skip=['uebungen'], heft_label='Projektplan', heft_title='Mein Scratch-Projekt', heft_sub='Idee, Figuren, Ablaufplan',
    heft_hint='Plane hier dein Projekt: Idee, Figuren und Bühnenbild, Ablaufplan, verwendete Bausteine (Schleife, Bedingung).',
    sections=[
    ('phasen', [
        A('Nenne die Phasen eines Projekts in der richtigen Reihenfolge.', 1, 'Idee → Ablaufplan → Programmieren → Testen → Verbessern → Präsentieren'),
    ]),
    ('fangen', [
        A('Nenne die Bausteine, die im Fangspiel stecken, und beschreibe ihre Aufgabe.', 2, 'Endlosschleife (Katze läuft immer weiter), Bewegung und „pralle vom Rand ab“, bedingte Anweisung „falls Mauszeiger berührt“ (Katze ruft „Erwischt!“).'),
    ]),
    ('quiz-proj', [
        A('Beschreibe, wie die Quiz-Katze prüft, ob deine Antwort richtig ist.', 1, 'Mit einer Verzweigung: falls Antwort = richtige Lösung, dann „Richtig!“, sonst „Leider falsch“.'),
    ]),
    ('ideen', [
        A('Wähle eine Projektidee und nenne die Bausteine, die du brauchst.', 1, 'individuell, z. B. Quiz: Frage, Verzweigung, Variable'),
    ]),
    ('check', [
        INFO('Nutze die Checkliste in der Präsentation, bevor du dein Projekt vorstellst.'),
    ]),
]),

'11_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Bit', 'Byte', 'Algorithmus', 'Schleife', 'Verzweigung'],
           ['Wiederholung von Anweisungen', 'falls … dann … sonst', '8 Bit', 'kleinste Informationseinheit', 'eindeutige, ausführbare, endliche Handlungsanweisung'], loes=[4, 5, 3, 1, 2]),
    ]),
    ('t1', [
        GL('Rechne um.', ['1010₂ = [[10]]', '25 = [[11001₂]]', '3 GB = [[3000]] MB', '4 Byte = [[32]] Bit']),
    ]),
    ('t2', [
        A('Übersetze: − • − / • − / • • • / • • • / •', 1, 'KASSE'),
    ]),
    ('t3', [
        A('Prüfe: „Nimm etwas Wasser. Koche es irgendwann. Gieße den Tee auf und warte.“', 2, 'Nicht eindeutig („etwas“, „irgendwann“), ausführbar ja, nicht endlich („warte“ – wie lange?).'),
    ]),
    ('t4', [
        A('Wie musst du „wiederhole 4 mal: gehe 100, drehe 90°“ ändern, damit ein Dreieck entsteht?', 1, 'wiederhole 3 mal, drehe 120°'),
    ]),
]),
}
