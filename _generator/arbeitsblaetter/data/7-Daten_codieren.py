from render import *

# Vorgedruckte binäre Stellenwerttafel im Hefteintrag
PV_TPL = ('<table class="t" style="margin:2.5mm 3mm .5mm;width:auto"><tr>' + ''.join(f'<th style="width:11mm;text-align:center">{v}</th>' for v in [128, 64, 32, 16, 8, 4, 2, 1])
          + '</tr><tr>' + '<td style="height:7mm"></td>' * 8 + '</tr></table>')
NEUMANN_TPL = ('<div class="tpl"><div class="bx" style="--c:#4338CA;height:9mm;text-align:center">Steuerwerk</div><div class="bx" style="--c:#4338CA;height:9mm;text-align:center">Rechenwerk</div>'
               '<span class="ar">⇄</span><div class="bx" style="--c:#B45309;height:9mm;text-align:center">Speicher</div><span class="ar">⇄</span><div class="bx" style="--c:#BE185D;height:9mm;text-align:center">Ein-/Ausgabe</div></div>')

WS = {
'01_Codes_Binaersystem': dict(skip=['uebungen'], heft_tpl=PV_TPL,
    heft_hint='Trage die Zahl 28 in die Stellenwerttafel ein. Schreibe dann die Merksätze ab.',
    sections=[
    ('codes', [
        L('Beim [[Codieren]] wird jedes Zeichen nach einer festen Vorschrift in ein anderes Zeichen umgewandelt. Der Morsecode nutzt kurze und lange [[Signale]], die Brailleschrift [[Punkte]], die man ertasten kann.'),
        SORT('Wer soll den Code lesen?', ['Brailleschrift', 'EAN-Barcode', 'Kyrillische Schrift', 'Pfandcode', 'Erzeugercode auf Eiern', 'Binärcode'], ['bestimmte Menschen', 'Maschinen'], h=14,
             loes=[['Brailleschrift', 'Kyrillische Schrift', 'Erzeugercode'], ['EAN-Barcode', 'Pfandcode', 'Binärcode']]),
    ]),
    ('binaer', [
        GL('Rechne die Dualzahlen in Dezimalzahlen um.', ['11100₂ = 16 + 8 + 4 = [[28]]', '1111₂ = [[8 + 4 + 2 + 1]] = [[15]]', '10101001₂ = [[128 + 32 + 8 + 1]] = [[169]]']),
    ]),
    ('division', [
        BOX('Rechne 162 mit dem Divisionsverfahren in eine Dualzahl um.', 34,
            loes='162:2=81 R0 · 81:2=40 R1 · 40:2=20 R0 · 20:2=10 R0 · 10:2=5 R0 · 5:2=2 R1 · 2:2=1 R0 · 1:2=0 R1 → von unten nach oben: 10100010₂'),
    ]),
    ('m1', [
        TAB('**M1:** Welche LEDs (64 32 16 8 4 2 1) müssen leuchten?', ['Zahl', 'Zerlegung', 'Dualzahl (7 LEDs)'],
            [['40', '[[32 + 8]]', '[[0101000]]'], ['33', '[[32 + 1]]', '[[0100001]]'], ['17', '[[16 + 1]]', '[[0010001]]']], h=6),
        A('**M1 Aufgabe 2:** Nenne die größte Zahl, die 7 bzw. 8 LEDs darstellen können.', 1, '7 LEDs: 1111111₂ = 127 · 8 LEDs: 11111111₂ = 255'),
    ]),
]),

'02_Bits_Bytes_Rechner': dict(skip=['uebungen'], heft_tpl=NEUMANN_TPL,
    heft_hint='Ergänze das Von-Neumann-Modell um den Bus. Schreibe dann die Merksätze ab.',
    sections=[
    ('bits', [
        TAB('Ergänze die Tabelle.', ['Anzahl Bits', '1', '2', '3', '4', '8'], [['Kombinationen', '2', '[[4]]', '[[8]]', '[[16]]', '[[256]]']], h=6),
    ]),
    ('einheiten', [
        GL('Rechne um.', ['3 GB = [[3000]] MB', '5 Byte = [[40]] Bit', '2500 KB = [[2,5]] MB', '1 TB = [[1 000 000]] MB']),
    ]),
    ('neumann', [
        ZU('Ordne die Bauteile des Von-Neumann-Rechners ihren Aufgaben zu.', ['Steuerwerk', 'Rechenwerk', 'Speicher (RAM)', 'Ein-/Ausgabewerk', 'Bus-System'],
           ['Schnittstelle zu Maus, Tastatur, Drucker', 'Leiterbahnen für den Datenaustausch', 'rechnet und vergleicht', 'enthält Programme und Daten', 'holt und entschlüsselt Befehle'], loes=[4, 5, 2, 3, 1]),
    ]),
    ('m1', [
        A('**M1:** Beschreibe, wie Steuerwerk, Speicher und Rechenwerk beim Befehl „ADD Zelle 7“ zusammenarbeiten.', 3, 'Das Steuerwerk holt den Befehl über den Bus aus dem Speicher und entschlüsselt ihn. Es lässt die Zahl aus Zelle 7 laden, das Rechenwerk addiert sie zum Akku. Dann wird der Befehlszähler erhöht.'),
        A('**M1:** Erkläre den Begriff „Von-Neumann-Flaschenhals“.', 2, 'Alle Befehle und Daten müssen einzeln durch den Bus. Er ist eine Engstelle, die den schnellen Prozessor bremst.'),
    ]),
]),

'03_ASCII': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Codiere deinen Vornamen im ASCII-Code.',
    sections=[
    ('ascii', [
        L('Der ASCII-Code codiert [[128]] Zeichen mit [[7]] Bit: 95 druckbare Zeichen und 33 [[Steuerzeichen]]. Groß- und Kleinbuchstaben unterscheiden sich um genau [[32]].'),
    ]),
    ('uebersetzen', [
        TAB('Codiere das Wort „POST“.', ['Zeichen', 'P', 'O', 'S', 'T'], [['dezimal', '[[80]]', '[[79]]', '[[83]]', '[[84]]'], ['binär', '[[01010000]]', '[[01001111]]', '[[01010011]]', '[[01010100]]']], h=6),
    ]),
    ('nullen', [
        A('Begründe, warum führende Nullen in der Binärfolge mitgeschrieben werden.', 2, 'Damit jedes Zeichen genau 8 Bit lang ist. Nur so erkennt der Computer, wo ein Zeichen anfängt und aufhört.'),
    ]),
    ('unicode', [
        A('Erkläre, warum der ASCII-Code erweitert wurde und was Unicode ist.', 2, 'ASCII war für englische Texte gemacht; Umlaute und andere Alphabete fehlten. Der erweiterte ASCII-Code nutzt 8 Bit (256 Zeichen). Unicode enthält Zeichen aller Schriften und Emojis.'),
    ]),
    ('m1', [
        GL('**M1:** Decodiere die Botschaften.', ['01001001 01001110 01000110 01001111 = [[INFO]]', '01000010 01001001 01010100 = [[BIT]]', '01001000 01101001 = [[Hi]]']),
    ]),
]),

'04_Bilder_codieren': dict(skip=['uebungen'],
    heft_tpl='<div class="tpl"><div class="bx" style="--c:#4338CA;flex:none;height:24mm;width:24mm;padding:0;background-image:linear-gradient(#999 .3mm,transparent .3mm),linear-gradient(90deg,#999 .3mm,transparent .3mm);background-size:3mm 3mm"></div></div>',
    heft_hint='Male im Raster ein 8 × 8-Schwarz-Weiß-Bild und notiere die Bitfolge der ersten zwei Zeilen. Schreibe dann die Merksätze ab.',
    sections=[
    ('sw', [
        L('Ein Bild wird in ein Raster aus [[Pixeln]] zerlegt. Im Schwarz-Weiß-Bild braucht jedes Pixel [[1]] Bit. Die Werte werden zeilenweise von [[oben links]] nach unten rechts gespeichert.'),
    ]),
    ('decode', [
        BOX('Das Bild ist 4 Pixel breit (1 = weiß, 0 = schwarz). Zeichne es: 1001 0000 0110 1001', 26, loes='Zeile 1: weiß schwarz schwarz weiß · Zeile 2: alle schwarz · Zeile 3: schwarz weiß weiß schwarz · Zeile 4: weiß schwarz schwarz weiß'),
    ]),
    ('grau', [
        TAB('Ergänze die Tabelle.', ['Bildart', 'Bit pro Pixel', 'Anzahl Farben/Stufen'],
            [['Schwarz-Weiß', '[[1]]', '[[2]]'], ['Graustufen', '[[8]]', '[[256]]'], ['RGB-Farbe', '[[24]]', '[[über 16 Millionen]]']], h=6),
    ]),
    ('groesse', [
        GL('Berechne die Dateigröße (ohne Kompression).', ['Schwarz-Weiß, 40 × 20 Pixel: [[800]] Bit = [[100]] Byte', 'Graustufen, 100 × 100 Pixel: [[10 000]] Byte', 'RGB, 1920 × 1080 Pixel: [[6 220 800]] Byte ≈ [[6,2]] MB']),
    ]),
    ('m1', [
        A('**M1:** Erkläre den Aufbau einer PNM-Datei vom Typ P1.', 2, 'Kopfzeile P1 (Schwarz-Weiß), dann Breite und Höhe, danach die Pixelwerte als 0 und 1 (1 = schwarz), getrennt durch Leerzeichen.'),
    ]),
]),

'05_Komprimieren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Codiere „WWWWWWSSSWWWW“ und berechne den Kompressionsfaktor.',
    sections=[
    ('rle', [
        GL('Wende die Lauflängencodierung an.', ['AAAAABBBCC → [[5A3B2C]]', 'WWWWWWWWSSSSWWWW → [[8W4S4W]]', '3X1Y5Z → [[XXXYZZZZZ]]']),
    ]),
    ('binbild', [
        A('Erkläre, warum die Lauflängencodierung bei einem Schachbrettmuster nicht lohnt.', 2, 'Bei jedem Pixel wechselt die Farbe. Jede Lauflänge ist 1, also wird für jedes Pixel ein eigener Wert gespeichert – die Daten werden sogar größer.'),
    ]),
    ('faktor', [
        GL('Berechne den Kompressionsfaktor.', ['24 Bit → 18 Bit: [[18 : 24 = 0,75]]', '64 Bit → 16 Bit: [[0,25]]', '100 KB → 120 KB: [[1,2]] (Daten wurden größer)']),
    ]),
    ('verlust', [
        TAB('Vergleiche.', ['', 'verlustfrei', 'verlustbehaftet'], [['Original wiederherstellbar?', '[[ja]]', '[[nein]]'], ['Beispiele', '[[PNG, ZIP, Lauflängen]]', '[[JPEG, MP3]]']], h=7),
    ]),
    ('m1', [
        A('**M1:** Begründe, welches Format du für ein Urlaubsfoto und welches für ein Logo mit durchsichtigem Hintergrund wählst.', 2, 'Foto: JPEG – klein, Verluste fallen bei Fotos kaum auf. Logo: PNG – verlustfrei, scharfe Kanten und Transparenz möglich.'),
    ]),
]),

'06_Hexadezimal': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Lege eine Tabelle dezimal | binär | hex für 0 bis 16 an.',
    sections=[
    ('systeme', [
        L('Das Hexadezimalsystem hat die Basis [[16]]. Es nutzt die Ziffern 0–9 und [[A]] bis F, wobei F für [[15]] steht.'),
    ]),
    ('umrechnen', [
        TAB('Ergänze die Tabelle.', ['dezimal', 'binär', 'hexadezimal'],
            [['10', '[[1010]]', '[[A]]'], ['[[31]]', '0001 1111', '[[1F]]'], ['[[255]]', '[[1111 1111]]', 'FF'], ['2292', '[[1000 1111 0100]]', '[[8F4]]']], h=6),
    ]),
    ('farben', [
        L('In HTML wird eine Farbe mit sechs Hex-Stellen angegeben: die ersten zwei für [[Rot]], die mittleren für [[Grün]], die letzten für [[Blau]]. #000000 ist [[Schwarz]], #FFFFFF ist [[Weiß]].'),
    ]),
    ('m1', [
        TAB('**M1:** Um welche Farben handelt es sich?', ['Code', 'R', 'G', 'B', 'Farbe'],
            [['#00008B', '[[0]]', '[[0]]', '[[139]]', '[[Dunkelblau]]'], ['#FCFCFC', '[[252]]', '[[252]]', '[[252]]', '[[fast Weiß]]'], ['#00EE00', '[[0]]', '[[238]]', '[[0]]', '[[Grün]]']], h=6),
    ]),
]),

'07_Analog_Digital': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne eine Schwingung und darunter die gestufte digitale Version.',
    sections=[
    ('signale', [
        L('Analoge Signale verändern sich [[kontinuierlich]]. Digitale Signale haben nur endlich viele, [[diskrete]] Werte.'),
    ]),
    ('abtasten', [
        A('Beschreibe, wie ein analoges Signal schrittweise in ein digitales Signal übersetzt wird.', 3, 'Das Signal wird in festen Zeitabständen abgetastet (Abtastrate in Hz). Jeder Messwert wird auf eine Stufe gerundet und als Dualzahl gespeichert. Werte zwischen den Messpunkten gehen verloren.'),
    ]),
    ('speicher', [
        GL('Berechne den Speicherbedarf einer WAV-Datei.', ['44 100 Hz, 16 Bit, Stereo, 10 s: 44 100 · 16 · 2 · 10 : 8 = [[1 764 000]] Byte ≈ [[1,8]] MB', 'als MP3 etwa: [[0,18]] MB']),
    ]),
    ('m1', [
        TAB('**M1:** Vergleiche analoge und digitale Anzeigen.', ['', 'analog', 'digital'], [['Vorteil', '[[Tendenz schnell erkennbar]]', '[[genau ablesbar, speicherbar]]'], ['Nachteil', '[[ungenaues Ablesen]]', '[[nur Stufen, braucht Strom]]']], h=7),
        A('**M1:** Begründe, weshalb die Zahl der Messpunkte die Qualität beeinflusst.', 2, 'Zwischen den Messpunkten gehen Werte verloren. Mehr Messpunkte bilden das Original genauer ab, brauchen aber mehr Speicher.'),
    ]),
]),

'08_Grafische_Codes': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Berechne die Prüfziffer der ISBN 978-3-14-149724-? mit Rechenweg.',
    sections=[
    ('ean', [
        L('Der EAN-Barcode codiert eine [[13]]-stellige Artikelnummer. Die letzte Ziffer ist die [[Prüfziffer]].'),
    ]),
    ('pruef', [
        TAB('Berechne die Prüfziffer der ISBN 978-3-14-149717-?', ['Ziffer', '9', '7', '8', '3', '1', '4', '1', '4', '9', '7', '1', '7'],
            [['Faktor', '1', '3', '1', '3', '1', '3', '1', '3', '1', '3', '1', '3'], ['Produkt', '9', '[[21]]', '8', '[[9]]', '1', '[[12]]', '1', '[[12]]', '9', '[[21]]', '1', '[[21]]']], h=6),
        GL('Summe und Prüfziffer:', ['Summe = [[125]] · nächste Zehnerzahl [[130]] · Prüfziffer = [[5]]']),
    ]),
    ('qr', [
        ZU('Ordne die Bereiche des QR-Codes ihren Aufgaben zu.', ['Positionsmarkierungen', 'Synchronisationslinien', 'Ausrichtungsmarkierung', 'Datenfeld'],
           ['enthält die eigentlichen Daten', 'zeigen die Größe des Datenfeldes', 'zeigen, wie der Code gedreht ist', 'zusätzliche Orientierung bei großen Codes'], loes=[4, 2, 1, 3]),
    ]),
    ('m1', [
        TAB('**M1:** Bestimme das Paritätsbit.', ['Daten', 'Anzahl Einsen', 'Paritätsbit'], [['1011001', '[[4]]', '[[0]]'], ['1110000', '[[3]]', '[[1]]'], ['0000001', '[[1]]', '[[1]]']], h=6),
        A('**M1:** Erkläre, warum ein Paritätsbit zwei verfälschte Bits nicht erkennt.', 2, 'Zwei Fehler ändern die Anzahl der Einsen um 0 oder 2 – gerade bleibt gerade. Das Paritätsbit passt wieder.'),
    ]),
]),

'09_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe den Erklärungen zu.', ['Byte', 'ASCII', 'Pixel', 'Redundanz', 'Abtastrate'],
           ['Messungen pro Sekunde', 'Bildpunkt', '8 Bit', 'zusätzliche Information zur Fehlererkennung', '128 Zeichen mit 7 Bit'], loes=[5, 3, 1, 4, 2]),
    ]),
    ('t1', [
        TAB('**T1:** Ergänze.', ['dezimal', 'binär', 'hex'], [['45', '[[101101]]', '[[2D]]'], ['[[200]]', '11001000', '[[C8]]'], ['[[171]]', '[[10101011]]', 'AB']], h=6),
    ]),
    ('t2', [
        GL('**T2:** Decodiere.', ['01001000 01000101 01011000 = [[HEX]]']),
    ]),
    ('t3', [
        GL('**T3:** Rechne.', ['RGB-Bild 20 × 10 Pixel: [[600]] Byte', 'WWWWSSSSSSW → [[4W6S1W]]']),
    ]),
    ('t4', [
        A('**T4:** Erkläre an einem Beispiel, wie eine Prüfziffer einen Zahlendreher erkennt.', 2, 'Beim Vertauschen zweier Nachbarziffern ändern sich ihre Faktoren (1 und 3). Die Summe ändert sich meist, die berechnete Prüfziffer passt nicht mehr zur angegebenen.'),
    ]),
]),
}
