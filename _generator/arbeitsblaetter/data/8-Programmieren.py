from render import *

WS = {
'01_Textbasiert': dict(skip=['uebungen'],
    sections=[
    ('vergleich', [
        L('Bei einer [[grafischen]] Programmiersprache werden Befehle als Blöcke dargestellt. Bei einer [[textbasierten]] Sprache schreibt man den [[Quellcode]] aus Zeichen, Symbolen und Schlüsselwörtern. Ein Compiler oder eine Laufzeitumgebung, hier der [[Browser]], macht ihn für den Computer verständlich.'),
    ]),
    ('syntax', [
        CODE('Das Programm enthält vier Syntaxfehler. Markiere sie und schreibe auf, wie es richtig heißt.',
             '// Kreis mit Beschriftung\ncanvas.init([0,20], [0,12]);\nCanvas.circle(10, 6, 5, {fill:"blue"};\nCanvas.text(2, 2, Hallo)', 2,
             'Zeile 2: `Canvas` groß schreiben · Zeile 3: schließende Klammer fehlt: `{fill:"blue"});` // Zeile 4: `"Hallo"` in Anführungszeichen · Semikolon am Ende fehlt'),
    ]),
    ('canvas', [
        GL('Ergänze zu `Canvas.init([0,20], [0,12])` und `Canvas.circle(10, 6, 5)`.',
           ['x-Werte von [[0]] bis [[20]] · y-Werte von [[0]] bis [[12]] · Ursprung: [[unten links]]',
            'Kreis: Mittelpunkt [[(10 | 6)]], Radius [[5]]']),
    ]),
    ('argumente', [
        ZU('Ordne die Teile von `Canvas.circle(10, 6, 5, {fill:"blue"})` zu.', ['`Canvas.circle`', '`10`', '`6`', '`5`', '`{fill:"blue"}`'],
           ['Radius', 'optionale Farbe', 'x-Koordinate des Mittelpunkts', 'Befehl zum Zeichnen eines Kreises', 'y-Koordinate des Mittelpunkts'], loes=[4, 5, 2, 1, 3]),
        L('Optionale Parameter stehen in [[geschweiften]] Klammern mit Namen. Fehlen sie, gilt ein [[Standardwert]]. Kommazahlen schreibt man mit [[Punkt]], z. B. 2.5.'),
    ]),
    ('m1', [
        CODE('**M1:** Ergänze den Code für ein hellblaues Fenster (1,4 × 1,4) und einen Baum.',
             '// Fenster\nCanvas.rect(5.5, 4.8, [[1.4]], [[1.4]], {fill:"[[lightblue]]"});\n// Baum: Stamm und Krone\nCanvas.[[rect]](14, 3, 0.6, 2.5, {fill:"sienna"});\nCanvas.[[circle]](14, 5.2, 1.6, {fill:"forestgreen"});', 0),
        A('Begründe, warum das Fenster erst nach dem Haus gezeichnet werden muss.', 1, 'Die Reihenfolge bestimmt, was vorne liegt: Später gezeichnete Formen überdecken frühere. Sonst wäre das Fenster vom Haus verdeckt.'),
    ]),
]),

'02_Schleifen': dict(skip=['uebungen'],
    sections=[
    ('for', [
        GL('Benenne die drei Angaben in `for (var i = 0; i < 10; i = i + 1)`.',
           ['`var i = 0` → [[Initialisierung der Zählvariablen]]', '`i < 10` → [[Schleifenbedingung]]', '`i = i + 1` → [[Zählschritt]]']),
        L('Zuerst wird die Zählvariable [[initialisiert]]. Dann wird die [[Bedingung]] geprüft. Ist sie wahr, werden die Anweisungen in { } ausgeführt, danach folgt der [[Zählschritt]]. Ist sie [[falsch]], endet die Schleife.'),
    ]),
    ('reihe', [
        CODE('Wie viele Kreise zeichnet das Programm und wo liegen sie?',
             'for (var x = 1; x < 20; x = x + 2) {\n  Canvas.circle(x, 6, 0.8, {fill:"blue"});\n}', 1,
             '10 Kreise, ihre Mittelpunkte liegen bei x = 1, 3, 5, …, 19 auf der Höhe y = 6.'),
    ]),
    ('verschachtelt', [
        CODE('Wie viele Quadrate zeichnet das Programm? Begründe.',
             'for (var y = 0; y < 4; y = y + 1) {\n  for (var x = 0; x < 5; x = x + 1) {\n    Canvas.rect(x + 0.5, y + 0.5, 0.9, 0.9);\n  }\n}', 2,
             '20 Quadrate: Die äußere Schleife läuft 4-mal (Zeilen). Bei jedem Durchlauf läuft die innere Schleife komplett, also 5-mal (Spalten): 4 · 5 = 20.'),
    ]),
    ('m1', [
        TAB('**M1:** Im Schleifenblock steht jeweils `Console.print(i);`. Was wird ausgegeben?', ['Schleife', 'Ausgabe'],
            [['`for (var i = 0; i < 5; i = i + 1)`', '[[0 1 2 3 4]]'],
             ['`for (var i = 2; i < 12; i = i + 3)`', '[[2 5 8 11]]'],
             ['`for (var i = 10; i > 0; i = i - 2)`', '[[10 8 6 4 2]]'],
             ['`for (var i = 1; i <= 16; i = i * 2)`', '[[1 2 4 8 16]]']], h=7, widths=[62, 38]),
    ]),
]),

'03_Variablen_Bedingungen': dict(skip=['uebungen'],
    sections=[
    ('var', [
        RF(['r|`var x = 5;` deklariert die Variable x und initialisiert sie mit 5.',
            'f|`2zahl` ist ein gültiger Variablenname.|Namen beginnen mit einem Buchstaben, z. B. `zahl2`.',
            'f|`"rot"` hat den Datentyp Zahl.|`"rot"` ist eine Zeichenkette.',
            'r|`17 % 5` ergibt 2.']),
    ]),
    ('trace', [
        CODE('Gehe Zeile für Zeile vor: Welche Werte haben a und b am Ende?',
             'var a = 3;\nvar b = 4;\na = a * b;\nb = a + 1;\na = a % 5;\n// am Ende: a = [[2]]   b = [[13]]', 0),
    ]),
    ('if', [
        CODE('Was gibt das Programm aus?',
             'if (x >= 7) {\n  Console.print("groß");\n} else {\n  Console.print("klein");\n}\n// x = 3: [[klein]]   x = 12: [[groß]]   x = 7: [[groß]]', 0),
        L('Bei `&&` (und) müssen [[beide]] Vergleiche wahr sein, bei `||` (oder) [[mindestens einer]].'),
    ]),
    ('m1', [
        TAB('**M1:** Es gilt x = 4 und y = 7. Ist die Bedingung wahr oder falsch?', ['Bedingung', 'wahr / falsch'],
            [['`x < 5`', '[[wahr]]'], ['`x > 5 && y > 5`', '[[falsch]]'], ['`x > 5 || y > 5`', '[[wahr]]'],
             ['`x + y >= 11`', '[[wahr]]'], ['`y % 2 == 0`', '[[falsch]]']], h=6, widths=[60, 40]),
    ]),
]),

'04_Datenfelder': dict(skip=['uebungen'],
    sections=[
    ('array', [
        GL('Es gilt `var A = [4, 8, 15, 16];`. Ergänze.',
           ['`A[0]` = [[4]] · `A[3]` = [[16]] · `A.length` = [[4]]',
            'nach `A.push(23);` gilt `A.length` = [[5]] und `A[4]` = [[23]]',
            'nach `A[1] = 9;` enthält A die Werte [[4, 9, 15, 16, 23]]']),
    ]),
    ('schleife', [
        CODE('Ergänze das Programm, das die Durchschnittstemperatur der Woche berechnet.',
             'var T = [12, 15, 11, 18, 14, 9, 19];\nvar summe = [[0]];\nfor (var i = 0; i < [[T.length]]; i = i + 1) {\n  summe = summe + [[T[i] ]];\n}\nConsole.print(summe / T.length);   // Ausgabe: [[14]]', 0),
    ]),
    ('tauschen', [
        CODE('Die Werte von `A[0]` und `A[1]` sollen getauscht werden. Ergänze.',
             'var h = [[A[0] ]];\nA[0] = [[A[1] ]];\nA[1] = [[h]];', 0),
        A('Erkläre, warum `A[0] = A[1]; A[1] = A[0];` nicht funktioniert.', 1, 'Nach der ersten Zuweisung ist der alte Wert von A[0] verloren; beide Elemente haben dann den Wert von A[1].'),
    ]),
    ('m1', [
        CODE('**M1:** Das Programm soll die Summe ausgeben, zeigt aber `NaN`. Finde die zwei Fehler und verbessere sie.',
             'var A = [3, 7, 1, 9, 5];\nvar summe;\nfor (var i = 0; i <= A.length; i = i + 1) {\n  summe = summe + A[i];\n}\nConsole.print(summe);', 2,
             '1. `var summe;` hat keinen Startwert, `undefined + 3` ergibt `NaN`. Richtig: `var summe = 0;` // 2. `i <= A.length` läuft einen Schritt zu weit, `A[5]` gibt es nicht. Richtig: `i < A.length`'),
        SORT('Syntaktischer oder semantischer Fehler?', ['fehlendes Semikolon', 'Summe ohne Startwert', 'Klammer nicht geschlossen', 'Schleife läuft einen Schritt zu weit'], ['syntaktisch', 'semantisch'], h=12,
             loes=[['fehlendes Semikolon', 'Klammer nicht geschlossen'], ['Summe ohne Startwert', 'Schleife läuft einen Schritt zu weit']]),
    ]),
]),

'05_Funktionen': dict(skip=['uebungen'],
    sections=[
    ('befehl', [
        L('Ein Befehl wird mit dem Schlüsselwort [[function]], einem eindeutigen [[Namen]] und Argumenten in [[runden]] Klammern definiert. Die Anweisungen stehen in [[geschweiften]] Klammern.'),
        CODE('Ergänze ein drittes Argument für die Farbe und zeichne einen roten Smiley bei (5 | 6).',
             'function smiley(x, y, [[farbe]]) {\n  Canvas.circle(x, y, 2, {fill:[[farbe]]});\n  // Augen und Mund …\n}\nsmiley([[5, 6, "red"]]);', 0),
    ]),
    ('funktion', [
        CODE('Was geben die Aufrufe zurück?',
             'function flaeche(a, b) {\n  return a * b;\n}\nfunction hypotenuse(a, b) {\n  return Math.sqrt(a * a + b * b);\n}\n// flaeche(3, 4) → [[12]]      flaeche(2.5, 2) → [[5]]\n// hypotenuse(3, 4) → [[5]]    flaeche(hypotenuse(6, 8), 2) → [[20]]', 0),
        A('Schreibe eine Funktion `umfang(r)`, die den Kreisumfang 2 · π · r zurückgibt.', 3, '`function umfang(r) {` // `  return 2 * Math.PI * r;` // `}`'),
    ]),
    ('m1', [
        L('Unterprogramme entwickelt man in drei Schritten: [[Anforderungen]] festlegen → [[implementieren]] → mit Testfällen [[testen]].'),
        CODE('**M1:** Laut Anforderung gibt `note(punkte)` ab 12 Punkten die Note 5. Welcher Testfall schlägt fehl? Verbessere den Fehler.',
             '  if (punkte >= 22) { return 4; }\n  if (punkte > 12) { return 5; }\n  return 6;', 2,
             'Der Grenzfall 12 Punkte liefert 6 statt 5. Richtig: `if (punkte >= 12) { return 5; }`'),
    ]),
]),

'06_Animationen': dict(skip=['uebungen'],
    sections=[
    ('animation', [
        CODE('Ergänze den Code für den hüpfenden Ball.',
             'function on_frame(t) {\n  Canvas.[[clear]]();\n  x = x + [[vx]];\n  y = y + vy;\n  if (x > 20 - r || x < r) { vx = [[-vx]]; }\n  Canvas.circle(x, y, r, {fill:"crimson"});\n}', 0),
        A('Erkläre, wie durch `on_frame` eine Bewegung entsteht.', 2, '`on_frame` wird für jedes Bild (etwa 60-mal pro Sekunde) aufgerufen. Jedes Mal wird gelöscht, die Position um die Geschwindigkeit verändert und neu gezeichnet. Die schnelle Folge leicht veränderter Bilder wirkt wie Bewegung.'),
    ]),
    ('interaktion', [
        ZU('Ordne zu.', ['`on_frame(t)`', '`on_mouse_down(x, y)`', '`on_key_down(key)`', '`"LEFT"`', '`Canvas.clear()`'],
           ['wird bei einem Tastendruck aufgerufen', 'löscht die Zeichenfläche', 'wird für jedes Bild aufgerufen', 'Zeichenkette für die Pfeiltaste nach links', 'wird bei einem Klick aufgerufen'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('rekursion', [
        CODE('Der Befehl `ringe` ruft sich selbst auf. Wie viele Kreise entstehen?',
             'function ringe(x, y, r, tiefe) {\n  if (tiefe == 0) { return; }\n  Canvas.circle(x, y, r, {fill:"none"});\n  ringe(x - r / 2, y, r / 2, tiefe - 1);\n  ringe(x + r / 2, y, r / 2, tiefe - 1);\n}\n// Rekursionstiefe 1: [[1]]   Tiefe 2: [[3]]   Tiefe 3: [[7]]', 0),
        A('Wozu dient die Zeile `if (tiefe == 0) { return; }`?', 1, 'Sie ist die Abbruchbedingung. Ohne sie würde sich der Befehl endlos selbst aufrufen.'),
    ]),
]),

'07_Sortieren': dict(skip=['uebungen'],
    sections=[
    ('hand', [
        GL('Wie viele Tauschvorgänge benachbarter Karten brauchst du mindestens?', ['[3, 1, 2] → [[2]]   ·   [4, 3, 2, 1] → [[6]]']),
    ]),
    ('bubble', [
        TAB('Sortiere [5, 2, 8, 1] mit Bubblesort. Notiere das Datenfeld nach jedem Durchlauf.', ['', 'Datenfeld'],
            [['Start', '[5, 2, 8, 1]'], ['nach Durchlauf 1', '[[[2, 5, 1, 8] ]]'], ['nach Durchlauf 2', '[[[2, 1, 5, 8] ]]'], ['nach Durchlauf 3', '[[[1, 2, 5, 8] ]]']], h=6, widths=[40, 60]),
    ]),
    ('selection', [
        TAB('Sortiere [5, 2, 8, 1] mit Selectionsort. Notiere das Datenfeld nach jedem Schritt.', ['', 'Datenfeld'],
            [['Start', '[5, 2, 8, 1]'], ['nach Schritt 1', '[[[1, 2, 8, 5] ]]'], ['nach Schritt 2', '[[[1, 2, 8, 5] ]]'], ['nach Schritt 3', '[[[1, 2, 5, 8] ]]']], h=6, widths=[40, 60]),
        L('Selectionsort braucht ähnlich viele [[Vergleiche]] wie Bubblesort, aber deutlich weniger [[Vertauschungen]].'),
    ]),
    ('aufwand', [
        GL('Bubblesort braucht im schlimmsten Fall etwa n · n / 2 Vergleiche.', ['n = 10 → [[50]]   ·   n = 20 → [[200]]   ·   n = 1000 → [[500 000]]', 'doppelte Länge → etwa [[vierfache]] Zahl an Vergleichen']),
    ]),
    ('m1', [
        CODE('**M1:** Ergänze den Kern von Bubblesort.',
             'for (var i = 0; i < B.length - 1; i = i + 1) {\n  for (var j = 0; j < B.length - 1 - i; j = j + 1) {\n    if (B[j] [[>]] B[j + 1]) {\n      var h = [[B[j] ]];\n      B[j] = [[B[j + 1] ]];\n      B[j + 1] = [[h]];\n    }\n  }\n}', 0),
    ]),
]),

'08_Bildverarbeitung': dict(skip=['uebungen'],
    sections=[
    ('rgb', [
        L('Bildschirme mischen Farben aus rotem, grünem und blauem Licht: [[additive]] Farbmischung. Jeder Anteil hat einen Wert von 0 bis [[255]]. Das ergibt 256 · 256 · 256 ≈ [[16,7 Millionen]] Farben.'),
        TAB('Welche Farbe entsteht?', ['RGB', '(255, 0, 0)', '(0, 0, 0)', '(255, 255, 255)', '(255, 255, 0)', '(0, 255, 255)', '(128, 128, 128)'],
            [['Farbe', '[[Rot]]', '[[Schwarz]]', '[[Weiß]]', '[[Gelb]]', '[[Cyan]]', '[[Grau]]']], h=7),
    ]),
    ('filter', [
        TAB('Berechne die neuen Farbwerte für das Pixel (200, 100, 30).', ['Filter', 'Rechnung', 'neuer Wert'],
            [['Graustufen', '[[(200 + 100 + 30) / 3 = 110]]', '[[(110, 110, 110)]]'],
             ['Negativ', '[[255 − Wert]]', '[[(55, 155, 225)]]'],
             ['Heller', '[[Wert + 50, höchstens 255]]', '[[(250, 150, 80)]]'],
             ['Schwarz-Weiß', '[[Mittelwert 110 ≤ 128]]', '[[(0, 0, 0) schwarz]]']], h=7, widths=[24, 44, 32]),
    ]),
    ('m1', [
        CODE('**M1:** Ergänze den Negativ-Filter.',
             'for (var y = 0; y < Bild.height; y = y + 1) {\n  for (var x = 0; x < [[Bild.width]]; x = x + 1) {\n    var p = Bild.get(x, y);\n    Bild.set(x, y, [[ [255 - p[0], 255 - p[1], 255 - p[2] ] ]]);\n  }\n}\nBild.show();', 0),
        A('Erkläre, warum für einen Filter zwei verschachtelte Schleifen nötig sind.', 1, 'Das Bild ist ein Raster: Die äußere Schleife durchläuft die Zeilen (y), die innere die Spalten (x). So wird jedes Pixel genau einmal umgerechnet.'),
    ]),
]),

'09_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Quellcode', 'Datenfeld', 'Funktion', 'Rekursion', 'Bubblesort'],
           ['gibt mit return einen Wert zurück', 'Programmtext aus Zeichen, Symbolen und Schlüsselwörtern', 'ein Befehl ruft sich selbst auf', 'benachbarte Elemente vergleichen und tauschen', 'viele Werte unter einem Namen, Index ab 0'], loes=[3, 1, 4, 5, 2]),
    ]),
    ('t1', [
        CODE('**T1:** Finde die drei Syntaxfehler und verbessere sie.',
             'Canvas.init([0,20], [0,12]);\nCanvas.rect(5, 5, 4, 2, {fill:red});\ncanvas.circle(10, 6, 2);\nCanvas.line(0, 0, 20, 12;', 2,
             'Zeile 2: `"red"` in Anführungszeichen // Zeile 3: `Canvas` groß schreiben // Zeile 4: schließende Klammer fehlt: `Canvas.line(0, 0, 20, 12);`'),
    ]),
    ('t2', [
        CODE('**T2:** Was wird ausgegeben?',
             'for (var i = 1; i < 10; i = i + 2) {\n  if (i % 3 == 0) {\n    Console.print(i);\n  }\n}\n// Ausgabe: [[3 9]]', 0),
    ]),
    ('t3', [
        CODE('**T3:** Was liefert die Funktion?',
             'function groesstes(A) {\n  var m = A[0];\n  for (var i = 1; i < A.length; i = i + 1) {\n    if (A[i] > m) { m = A[i]; }\n  }\n  return m;\n}\n// groesstes([4, 17, 9]) → [[17]]    groesstes([-3, -8]) → [[-3]]', 0),
    ]),
    ('t4', [
        A('**T4:** Im Sternenhimmel-Projekt wirken Datenfeld, Schleife, Funktion, Animation und Interaktion zusammen. Beschreibe, wofür jeder Baustein gebraucht wird.', 3,
          'Datenfeld `sterne`: speichert Position und Größe aller Sterne // Schleife: legt 60 Sterne an und zeichnet alle Sterne // Funktion `stern`: zeichnet einen funkelnden Stern // `on_frame`: zeichnet jedes Bild neu (Animation) // `on_mouse_down`: fügt per Klick einen Stern hinzu (Interaktion)'),
    ]),
]),
}
