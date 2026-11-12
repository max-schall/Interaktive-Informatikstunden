from render import *

WS = {
'01_Automaten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Zustandsdiagramm des Kaugummi-Automaten.',
    sections=[
    ('kaugummi', [
        TAB('Nenne Eingabe und Ausgabe.', ['Automat', 'gültige Eingabe', 'Ausgabe'], [['Kaugummi-Automat', '[[Münze, Griff drehen]]', '[[Kaugummi]]'], ['Fahrkartenautomat', '[[Ziel wählen, bezahlen]]', '[[Fahrkarte]]'], ['Wasserkocher', '[[Schalter, 100 °C erreicht]]', '[[heißes Wasser, Abschalten]]']], h=7),
    ]),
    ('diagramm', [
        L('Im Zustandsdiagramm sind Zustände [[Kreise]] und Übergänge [[Pfeile]] mit der Eingabe. Der [[Startzustand]] hat einen Pfeil von außen, der [[Endzustand]] einen doppelten Kreis.'),
    ]),
    ('pfand', [
        A('Erkläre den Unterschied zwischen einer Schleife (Pfandautomat) und einem Alternativweg (Snackautomat).', 2, 'Schleife: Eine Eingabe (Flasche) führt in denselben Zustand zurück, nur der Betrag ändert sich. Alternativweg: Verschiedene Eingaben (2 € oder 1 € + 1 €) führen zum gleichen Ziel.'),
    ]),
    ('m1', [
        TAB('**M1:** Zustandstabelle der Fußgängerampel.', ['Zustand', 'Eingabe/Ereignis', 'Folgezustand', 'Ausgabe'], [['Rot', '[[Knopf gedrückt]]', '[[Warten]]', '[[„Signal kommt“]]'], ['Warten', '[[3 s vergangen]]', '[[Grün]]', '[[grünes Licht, Ton]]'], ['Grün', '[[10 s vergangen]]', '[[Rot]]', '[[rotes Licht]]']], h=7),
    ]),
]),

'02_KI': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege eine Tabelle mit je drei Chancen und Risiken von KI an.',
    sections=[
    ('was', [
        TAB('Vergleiche.', ['', 'schwache KI', 'starke KI'], [['Fähigkeit', '[[eine spezielle Aufgabe]]', '[[beliebige neue Aufgaben, kreativ, sozial]]'], ['Beispiel', '[[Schachprogramm, Sprachassistent]]', '[[gibt es noch nicht]]']], h=8),
    ]),
    ('smarthome', [
        L('Im [[Internet der Dinge]] tauschen Alltagsgeräte Daten aus. Ein Haushalt, dessen Geräte per App oder Sprache gesteuert werden, heißt [[Smart Home]].'),
    ]),
    ('auto', [
        A('**M1:** Erkläre den Unterschied zwischen assistiertem und autonomem Fahren.', 2, 'Assistiert: KI unterstützt bei einzelnen Aufgaben (Abstand, Spur), der Mensch fährt. Autonom: Das Auto fährt vollständig allein, ohne Fahrer.'),
    ]),
    ('m2', [
        A('**M2:** Stelle Vermutungen an, warum viele Menschen KI bei Gerichtsurteilen ablehnen.', 2, 'Urteile betreffen Menschen stark; KI kann Fehler aus einseitigen Daten übernehmen; Entscheidungen sind schwer nachvollziehbar; Verantwortung und Menschlichkeit fehlen.'),
    ]),
]),

'03_Maschinen_lernen': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne einen Entscheidungsbaum für Apfel, Banane, Erdbeere, Birne und Kiwi.',
    sections=[
    ('eva', [
        A('Beschreibe den Unterschied zwischen einem klassischen Programm und einem lernfähigen System.', 2, 'Ein klassisches Programm hat einen festen Lösungsweg. Ein lernfähiges System entwickelt aus Trainingsdaten eigene Regeln und hat einen veränderbaren Erfahrungsschatz.'),
    ]),
    ('baum', [
        A('**M1:** Die Kiwi wird als Birne erkannt. Ergänze ein Attribut und beschreibe die Änderung.', 2, 'Beim Ast „nicht gelb, nicht rot“ einen Knoten „behaarte Schale?“ einfügen: ja → Kiwi, nein → Birne.'),
    ]),
    ('ueberwacht', [
        A('Beschreibe, wie beim überwachten Lernen eine neue Frucht eingeordnet wird.', 2, 'Das System vergleicht sie mit den beschrifteten Trainingsdaten und ordnet sie der Gruppe ihrer nächsten Nachbarn zu.'),
    ]),
    ('unueberwacht', [
        L('Beim unüberwachten Lernen enthalten die Daten [[keine Lösungen]]. Das System erkennt selbst Muster und bildet [[Gruppen]].'),
    ]),
    ('verstaerkt', [
        A('Erkläre, wie der Roboter lernt, welche Tür am besten ist.', 2, 'Er probiert Türen aus und erhält positive (Akku) oder negative Rückmeldung. Mit der Zeit wählt er häufiger die Tür mit den meisten Belohnungen, probiert aber ab und zu andere.'),
    ]),
    ('m2', [
        ZU('**M2:** Ordne die Lernart zu.', ['überwacht', 'unüberwacht', 'teilüberwacht', 'verstärkend'],
           ['Saugroboter lernt durch Zusammenstöße', 'nur wenige Fotos sind beschriftet', 'Tierfotos mit Namen', 'Kunden werden gruppiert'], loes=[4, 3, 1, 2]),
    ]),
]),

'04_Neuronale_Netze': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne ein Netz mit 3 Eingabe-, 4 verborgenen und 2 Ausgabe-Neuronen.',
    sections=[
    ('neuron', [
        GL('Berechne das Freibad-Neuron (Gewichte 3, 4, 2, −5; Schwelle 5).', ['Sonne 1, warm 1, Freunde 0, Arbeit 0: Summe [[7]] → Ausgabe [[1]]', 'Sonne 1, warm 1, Freunde 1, Arbeit 1: Summe [[4]] → Ausgabe [[0]]']),
    ]),
    ('schichten', [
        ZU('Ordne die Schichten zu.', ['Eingabeschicht', 'verborgene Schicht', 'Ausgabeschicht'], ['berechnet die Endwerte', 'nimmt z. B. Pixelwerte auf', 'verarbeitet die Informationen'], loes=[3, 1, 2]),
    ]),
    ('lernen', [
        A('Erkläre, wie das Perzeptron lernt, Katzen und Hunde zu unterscheiden.', 2, 'Es ordnet jedes Tier ein. Bei einem Fehler werden die Gewichte ein kleines Stück in die richtige Richtung verändert. Nach vielen Runden liegt die Trennlinie richtig.'),
    ]),
    ('m1', [
        A('**M1:** Beschreibe, was die Schichten bei der Bilderkennung erkennen.', 2, 'Eingabe: Pixel · 1. verborgene Schicht: Kanten · 2.: Formen · 3.: Teile wie Ohren und Augen · Ausgabe: Wahrscheinlichkeit, z. B. Katze 92 %.'),
        A('**M1:** Nenne zwei Gründe für Fehler bei der Bilderkennung.', 1, 'ungewöhnliche Perspektive oder Licht, einseitige Trainingsdaten, verdeckte Objekte'),
    ]),
]),

'05_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Zustand', 'schwache KI', 'Entscheidungsbaum', 'Gewicht', 'verstärkendes Lernen'],
           ['Lernen durch Belohnung', 'Stärke einer Verbindung', 'Situation eines Automaten', 'Knoten mit Ja/Nein-Fragen', 'auf eine Aufgabe spezialisiert'], loes=[5, 4, 1, 3, 2]),
    ]),
    ('t1', [
        GL('**T1:** Kaugummi-Automat: In welchem Zustand ist er?', ['Münze → drehen → Münze: [[Ausgabe]] (Münze ist hier ungültig)', 'drehen → Münze: [[frei]]']),
    ]),
    ('t2', [
        A('**T2:** Nenne zwei Beispiele für schwache KI aus deinem Alltag.', 1, 'Sprachassistent, Gesichtserkennung, Filmempfehlungen, Übersetzungsprogramm'),
    ]),
    ('t3', [
        A('**T3:** Erkläre den Unterschied zwischen überwachtem und unüberwachtem Lernen.', 2, 'Überwacht: Trainingsdaten enthalten die richtige Lösung. Unüberwacht: keine Lösungen, das System bildet selbst Gruppen.'),
    ]),
    ('t4', [
        GL('**T4:** Eingaben 1, 0, 1 · Gewichte 2, 5, 3 · Schwelle 4', ['Summe = [[5]] → Ausgabe [[1]]']),
    ]),
]),
}
