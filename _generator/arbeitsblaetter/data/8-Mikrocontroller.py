from render import *

MX_TPL = ('<table class="t" style="margin:2.5mm 3mm .5mm;width:auto">' + ('<tr>' + '<td style="width:7mm;height:7mm"></td>' * 5 + '</tr>') * 5 + '</table>')

WS = {
'01_Mikrocontroller': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Calliope mini und beschrifte sechs Bauteile.',
    sections=[
    ('alltag', [
        L('Ein [[Mikrocontroller]] ist ein sehr kleiner Computer, bei dem Prozessor und [[Speicher]] auf einem Chip sitzen. Er steckt z. B. in [[Waschmaschinen]], Ampeln und Fitnessarmbändern.'),
    ]),
    ('bauteile', [
        ZU('Ordne die Bauteile ihren Aufgaben zu.', ['LED-Matrix', 'Tasten A und B', 'Pins', 'Mikrofon', 'USB-Anschluss'],
           ['Programm übertragen, Strom', 'Lautstärke messen', 'Text und Bilder anzeigen', 'Berührung erkennen', 'Eingaben auslösen'], loes=[5, 4, 1, 3, 2]),
    ]),
    ('eva', [
        SORT('Ordne nach dem EVA-Prinzip.', ['Taste A', 'Prozessor', 'Lautsprecher', 'Lichtsensor', 'RGB-LED', 'Temperatursensor', 'Arbeitsspeicher', 'LED-Matrix'], ['Eingabe', 'Verarbeitung', 'Ausgabe'], h=16,
             loes=[['Taste A', 'Lichtsensor', 'Temperatursensor'], ['Prozessor', 'Arbeitsspeicher'], ['Lautsprecher', 'RGB-LED', 'LED-Matrix']]),
    ]),
    ('m1', [
        A('**M1:** Beschreibe, was das erste Programm macht.', 2, 'Es zeigt „Hallo!“. Danach wird ständig geprüft: Bei Taste A erscheint ein Herz und die LED leuchtet rot, bei Taste B ein Smiley und ein Ton erklingt.'),
    ]),
]),

'02_NEPO': dict(skip=['uebungen'], heft_tpl=MX_TPL,
    heft_hint='Zeichne in das Raster dein eigenes Bild. Schreibe dann die Merksätze ab.',
    sections=[
    ('lab', [
        ZU('Ordne die Blockgruppen zu.', ['Aktion', 'Sensoren', 'Kontrolle', 'Logik', 'Mathematik'],
           ['Vergleiche wie < und =', 'Text, Bild, LED, Ton ausgeben', 'Zufallszahl, Rechnen', 'Werte von Licht, Temperatur abfragen', 'Wiederholung, Bedingung, warten'], loes=[4, 1, 5, 2, 3]),
    ]),
    ('aktion', [
        A('Beschreibe, wie man in NEPO ein eigenes Bild auf der LED-Matrix anzeigt.', 1, 'Den Aktionsblock „zeige Bild“ an den Startblock hängen und im Bild-Editor die 25 Felder an- oder ausschalten.'),
    ]),
    ('wuerfel', [
        BOX('Schreibe das Würfel-Programm als Struktogramm.', 30, loes='wiederhole unendlich oft: wenn geschüttelt? ja → setze Zahl auf Zufallszahl von 1 bis 6, zeige Text Zahl, spiele Ton'),
    ]),
    ('m1', [
        A('**M1:** Erkläre, warum das Blinken nach Drücken von Taste B schneller wird.', 2, 'Die Variable Pause wird um 100 verringert. Die Warte-Blöcke nutzen die Pause, also wird kürzer gewartet und die LED blinkt schneller.'),
    ]),
]),

'03_Variablen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und schreibe das Programm für den Torzähler als Struktogramm auf.',
    sections=[
    ('typen', [
        TAB('Welcher Variablentyp passt?', ['Inhalt', 'Typ'], [['Anzahl der Tore', '[[Zahl]]'], ['Name des Spielers', '[[Zeichenkette]]'], ['Spiel läuft? (wahr/falsch)', '[[logischer Wert]]'], ['Farbe der LED', '[[Farbe]]']], h=6, widths=[60, 40]),
    ]),
    ('tore', [
        A('Beschreibe, wie der Torzähler die Tore zählt und zurückgesetzt wird.', 2, 'Die Variablen ToreA und ToreB starten bei 0. Bei Taste A bzw. B wird die passende Variable um 1 erhöht und angezeigt. Bei Berührung von Pin 1 werden beide wieder auf 0 gesetzt.'),
    ]),
    ('farbe', [
        GL('Welche Farbe zeigt die LED?', ['Rot 255, Grün 255, Blau 255 → [[Weiß]]', 'Rot 255, Grün 0, Blau 0 → [[Rot]]', 'Rot 255, Grün 255, Blau 0 → [[Gelb]]']),
    ]),
    ('m1', [
        GL('**M1:** Welche Zahl wird angezeigt?', ['setze x auf 2 · wiederhole 3 mal: ändere x um 4 · ändere x um −1 → [[13]]']),
    ]),
]),

'04_Sensoren': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Miss an fünf Stellen Helligkeit und Temperatur und notiere sie.',
    sections=[
    ('sensoren', [
        TAB('Was misst der Sensor?', ['Sensor', 'Messgröße'], [['Lichtsensor', '[[Helligkeit 0–100]]'], ['Temperatursensor', '[[Temperatur in °C]]'], ['Mikrofon', '[[Lautstärke]]'], ['Lagesensor', '[[Neigung, Schütteln]]']], h=6, widths=[40, 60]),
    ]),
    ('licht', [
        A('Beschreibe das Nachtlicht-Programm.', 2, 'In einer Endlosschleife wird die Helligkeit gemessen. Ist sie kleiner als 30, zeigt der Calliope einen Mond und die LED leuchtet gelb, sonst eine Sonne und die LED ist aus.'),
    ]),
    ('temp', [
        TAB('Welche Farbe zeigt das Ampel-Thermometer?', ['Temperatur', '12 °C', '18 °C', '25 °C', '30 °C'], [['Farbe', '[[blau]]', '[[grün]]', '[[grün]]', '[[rot]]']], h=6),
    ]),
    ('m1', [
        BOX('**M1:** Schreibe das Programm der Lärmampel in NEPO-Blöcken auf.', 32, loes='Start · wiederhole unendlich oft: setze L auf Lautstärke · wenn L > 70: LED rot, Bild KREUZ · sonst wenn L > 40: LED gelb · sonst: LED grün, Bild HAKEN'),
    ]),
]),

'05_Sensor_Aktor': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Lege eine Tabelle System | Sensor | Aktor für fünf Beispiele an.',
    sections=[
    ('prinzip', [
        L('Ein [[Sensor]] misst Eigenschaften der Umgebung. Das [[Steuerelement]] verarbeitet die Daten. Ein [[Aktor]] setzt den Befehl um, z. B. ein Motor oder ein Lautsprecher.'),
    ]),
    ('rolltreppe', [
        A('Beschreibe das Sensor-Aktor-System der Rolltreppe.', 2, 'Die Lichtschranke (Sensor) merkt, wenn der Lichtstrahl unterbrochen wird. Die Steuerung startet daraufhin den Elektromotor (Aktor), die Treppe fährt.'),
    ]),
    ('auto', [
        A('**M1:** Beschreibe die Einparkhilfe: Welcher Sensor misst was, welcher Aktor reagiert wie?', 2, 'Ultraschallsensoren messen den Abstand zum Hindernis. Der Lautsprecher piept umso schneller, je kleiner der Abstand ist; sehr nah kommt ein Dauerton.'),
    ]),
    ('regel', [
        A('**M2:** Erkläre, wie ein smartes Thermostat die Temperatur regelt.', 2, 'Es misst ständig die Ist-Temperatur und vergleicht sie mit der Solltemperatur. Ist es zu kalt, öffnet der Stellmotor das Heizungsventil; ist der Sollwert erreicht, wird es geschlossen.'),
    ]),
    ('alarm', [
        A('Begründe, warum der Lichtsensor für die Alarmanlage im Schuhkarton geeignet ist.', 2, 'Im geschlossenen Karton ist es dunkel. Wird er geöffnet, steigt die Helligkeit deutlich – das kann der Lichtsensor zuverlässig erkennen.'),
    ]),
]),

'06_Funk': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Struktogramm für den Empfänger der Funk-Alarmanlage.',
    sections=[
    ('funk', [
        L('Mit dem [[Funkmodul]] können Calliope Daten austauschen. Sender und Empfänger müssen denselben [[Kanal]] nutzen. Gesendet werden Zahlen, logische Werte oder [[Zeichenketten]].'),
    ]),
    ('liste', [
        A('Erkläre, wie eine Nachrichtenliste funktioniert und welchen Vorteil sie hat.', 2, 'Jede Nachricht bekommt eine Nummer; gesendet wird nur die Zahl. Der Empfänger schlägt in der gleichen Liste nach. Vorteil: kurze Nachrichten, Außenstehende verstehen sie nicht.'),
    ]),
    ('m1', [
        A('**M1:** Beschreibe, wie der Empfänger beim Abstimmungsgerät die Stimmen zählt.', 2, 'Er prüft wiederholt, ob eine Nachricht angekommen ist. Bei 1 erhöht er die Variable Ja, bei 0 die Variable Nein um 1. Mit Taste A zeigt er das Ergebnis.'),
    ]),
    ('projekt', [
        SORT('Ordne die Aufgaben dem Sender oder Empfänger der Funk-Alarmanlage zu.', ['misst die Helligkeit', 'sendet „OFFEN“', 'prüft, ob eine Nachricht da ist', 'spielt Alarmton', 'liegt in der Truhe'], ['Sender', 'Empfänger'], h=14,
             loes=[['misst die Helligkeit', 'sendet „OFFEN“', 'liegt in der Truhe'], ['prüft Nachricht', 'spielt Alarmton']]),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Mikrocontroller', 'NEPO', 'Sensor', 'Aktor', 'Funkkanal'],
           ['setzt Befehle um', 'muss bei Sender und Empfänger gleich sein', 'Computer auf einem Chip', 'misst Eigenschaften der Umgebung', 'grafische Programmiersprache'], loes=[4, 5, 1, 2, 3]),
    ]),
    ('t1', [
        A('**T1:** Nenne je zwei Eingabe- und Ausgabebauteile des Calliope.', 1, 'Eingabe: Tasten, Pins, Lichtsensor, Mikrofon. Ausgabe: LED-Matrix, RGB-LED, Lautsprecher.'),
    ]),
    ('t2', [
        GL('**T2:** Welche Zahl wird angezeigt?', ['setze Tore auf 1 · Taste A 4-mal: ändere Tore um 2 → [[9]]']),
    ]),
    ('t3', [
        A('**T3:** Nenne ein Sensor-Aktor-System aus deinem Alltag mit Sensor und Aktor.', 1, 'z. B. automatische Tür: Bewegungsmelder → Motor; Straßenlaterne: Lichtsensor → Lampe'),
    ]),
    ('t4', [
        A('**T4:** Nenne zwei Voraussetzungen für Funkkommunikation zwischen zwei Calliope.', 1, 'Beide haben ein Programm mit Senden/Empfangen und nutzen denselben Kanal.'),
    ]),
]),
}
