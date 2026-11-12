from render import *

WS = {
'01_Mit_Daten_arbeiten': dict(skip=['uebungen'],
    sections=[
    ('struktur', [
        A('Erkläre, warum Daten gleicher Art in jedem Datensatz an derselben Stelle stehen müssen.', 2, 'Nur so ist immer klar, an welcher Stelle welche Teilinformation steht. Ein Programm kann dann gezielt darauf zugreifen, z. B. alle Entfernungen in Spalte 3 vergleichen.'),
    ]),
    ('typen', [
        TAB('Welcher Datentyp passt?', ['Daten', 'Datentyp'], [['Anzahl der Schüler: 27', '[[Ganzzahl]]'], ['Preis: 3,25 €', '[[Gleitkommazahl]]'], ['bezahlt: wahr', '[[Wahrheitswert]]'], ['Straße: Hofweg 6', '[[Zeichenkette]]'], ['Telefon: 08675/9876', '[[Zeichenkette]]']], h=6, widths=[55, 45]),
    ]),
    ('tabelle', [
        L('Ein Dokument der Tabellenkalkulation heißt [[Arbeitsmappe]]. Sie enthält [[Tabellenblätter]] aus Spalten und Zeilen. Der Schnittpunkt einer Spalte und einer Zeile ist eine [[Zelle]]. Ihre Adresse besteht aus dem [[Spaltenbuchstaben]] und der Zeilennummer, z. B. C2.'),
        GL('Gib die Zelladresse an.', ['3. Spalte, 5. Zeile → [[C5]]   ·   1. Spalte, 12. Zeile → [[A12]]   ·   6. Spalte, 1. Zeile → [[F1]]']),
    ]),
    ('objekte', [
        ZU('Ordne zu: Wie beschreibt man eine Zelle objektorientiert?', ['ZELLE', 'Zelle D1', 'Hintergrundfarbe', 'setze Hintergrundfarbe', 'grün'],
           ['Methode', 'Klasse', 'Attributwert', 'Objekt', 'Attribut'], loes=[4, 1, 5, 2, 3]),
    ]),
    ('m1', [
        TAB('**M1:** Werte die Pinnwand aus. Wie viele Personen haben an welchem Tag Zeit?', ['', 'Montag', 'Dienstag', 'Mittwoch'], [['Anzahl', '[[5]]', '[[3]]', '[[2]]']], h=7),
        A('Welcher Wochentag bietet sich an? Nenne die Funktion, mit der das Programm die Kreuze zählt.', 1, 'Der Montag. Gezählt wird z. B. mit `=ZÄHLENWENN(B3:B10;"x")`.'),
    ]),
]),

'02_Diagramme': dict(skip=['uebungen'],
    sections=[
    ('typen', [
        TAB('Wofür eignet sich welcher Diagrammtyp?', ['Diagrammtyp', 'geeignet für'], [['Kreisdiagramm', '[[Anteile an einem Ganzen]]'], ['Liniendiagramm', '[[Verlauf über die Zeit]]'], ['Säulen-/Balkendiagramm', '[[Vergleich von Werten]]']], h=7, widths=[35, 65]),
    ]),
    ('wahl', [
        SORT('Ordne den passenden Diagrammtyp zu.', ['Temperatur im Tagesverlauf', 'Ergebnis einer Wahl in Prozent', 'Einwohner der fünf größten Städte', 'Einwohnerzahl seit 1950', 'Verteilung meines Taschengelds', 'Stimmen je Kandidat'], ['Kreis', 'Linie', 'Säule'], h=14,
             loes=[['Ergebnis einer Wahl', 'Taschengeld'], ['Temperatur', 'Einwohnerzahl seit 1950'], ['fünf größte Städte', 'Stimmen je Kandidat']]),
    ]),
    ('m1', [
        A('**M1:** Die Werte 82 %, 86 % und 89 % werden in einem Säulendiagramm mit einer Achse ab 80 % dargestellt. Beschreibe, welcher Eindruck entsteht.', 2, 'Die letzte Säule (9 Einheiten über 80) wirkt etwa viereinhalbmal so hoch wie die erste (2 Einheiten) – obwohl der Wert nur um 7 Prozentpunkte gestiegen ist. Der Anstieg wird stark übertrieben.'),
        A('Erkläre, was man bei der Erstellung von Diagrammen beachten muss.', 2, 'Säulen- und Balkendiagramme ab dem Nullpunkt zeichnen, Achsen beschriften, eine passende Einteilung wählen. Sonst entsteht ein verzerrter Eindruck.'),
    ]),
    ('m2', [
        RF(['r|Am häufigsten nutzen die 16- bis 24-Jährigen soziale Netzwerke (90 %).',
            'f|Die Prozentwerte zu „Wo nutzen die Deutschen Social Media?“ ergeben zusammen 100 %.|Mehrfachnennungen waren möglich – deshalb passt kein Kreisdiagramm.',
            'r|Die Zahl der Nutzer weltweit ist von 2014 bis 2022 von 1,86 auf 4,62 Milliarden gestiegen.']),
    ]),
    ('m3', [
        A('**M3:** Vergleiche den Strommix 2012 und 2022. Welche Energieträger haben stark zu- bzw. abgenommen?', 2, 'Zugenommen: vor allem Wind (7,4 % → 38,2 %). Abgenommen: Kernenergie (16 % → 6,3 %), Braunkohle (26 % → 18,9 %), Steinkohle (19 % → 11,4 %).'),
        A('Was kann ein Kreisdiagramm nicht zeigen?', 1, 'Wie viel Strom insgesamt erzeugt wurde und wie sich die Werte Jahr für Jahr entwickelt haben.'),
    ]),
    ('selbst', [
        BOX('Zeichne zu eurer Umfrage ein Säulendiagramm mit beschrifteten Achsen.', 38, loes='Säulendiagramm: x-Achse Netzwerke, y-Achse Anzahl ab 0, Säulen gleich breit, Titel.'),
    ]),
]),

'03_Mit_Daten_rechnen': dict(skip=['uebungen'],
    sections=[
    ('formate', [
        A('In B3 steht „2 Euro“. Die Formel `=B3-B4` zeigt `#WERT!`. Erkläre und verbessere.', 2, '„2 Euro“ ist Text – mit Text kann nicht gerechnet werden. Richtig: `2` oder `2 €` (Format Währung) eintragen.'),
    ]),
    ('formel', [
        L('Berechnungen beginnen immer mit einem [[=]]. Man kann mit festen Zahlen oder mit [[Zellbezügen]] rechnen. Vorteil der Zellbezüge: Ändern sich die Daten, wird das Ergebnis [[automatisch]] angepasst.'),
        GL('Schreibe die Formel für C5 (C2 = 100, C3 = 50, C4 = 5,50).', ['mit Zahlen: [[=100-50-5,50]]   ·   mit Zellbezug: [[=C2-C3-C4]]   ·   Ergebnis: [[44,50]]']),
    ]),
    ('funktionen', [
        GL('Es gilt C3 = 18, C4 = 21, C5 = 17, C6 = 22, C7 = 20, C8 = 25.', ['`=SUMME(C3:C7)` → [[98]]   ·   `=SUMME(C3;C5)` → [[35]]', '`=MITTELWERT(C3:C8)` → [[20,5]]   ·   `=MAX(C3:C8)` → [[25]]']),
        L('Ein [[Doppelpunkt]] schließt einen Bereich ein. Einzelne Zellen trennt ein [[Semikolon]]. Der Mittelwert ist die [[Summe]] aller Werte geteilt durch ihre [[Anzahl]].'),
    ]),
    ('m1', [
        TAB('**M1:** Kassenstand der Klasse 10d. Notiere Formel und Ergebnis.', ['Zelle', 'Formel', 'Ergebnis'],
            [['B10 Gesamteinnahmen', '[[=SUMME(B3:B9)]]', '[[800,00 €]]'], ['B13 Kassenstand Juni', '[[=B12+B10]]', '[[912,00 €]]'], ['B15 Kassenstand Juli', '[[=B13-B14]]', '[[121,50 €]]']], h=7, widths=[34, 40, 26]),
    ]),
    ('m2', [
        A('**M2:** Schreibe die Formel für den Notenschnitt der Klasse 10a (Noten in B3 bis B12) und erkläre, wie der Wert berechnet wird.', 2, '`=MITTELWERT(B3:B12)`. Das Programm addiert alle Noten und teilt die Summe durch die Anzahl der Noten (10).'),
    ]),
]),

'04_Wenn_Funktion': dict(skip=['uebungen'],
    sections=[
    ('bedingung', [
        BOX('Zeichne das Struktogramm: Bei mindestens 20 °C wird draußen gefeiert, sonst drinnen. Danach wird aufgeräumt.', 34,
            loes='Verzweigung „Temperatur ≥ 20 °C?“ – ja: Feier draußen · nein: Feier drinnen; darunter über die ganze Breite: aufräumen.'),
    ]),
    ('logik', [
        L('Die WENN-Funktion besteht aus drei Teilen: der [[Prüfung]], dem [[Dann-Wert]] und dem [[Sonst-Wert]]. Die Teile werden durch ein [[Semikolon]] getrennt. Texte stehen in [[Anführungszeichen]].'),
        GL('Was gibt `=WENN(A3>=20;"draußen";"drinnen")` aus?', ['A3 = 18 → [[drinnen]]   ·   A3 = 20 → [[draußen]]   ·   A3 = 25 → [[draußen]]']),
    ]),
    ('m1', [
        A('**M1:** Schreibe die Formel für C3: „ja“, wenn die Person in B3 mindestens 16 Jahre alt ist, sonst „nein“.', 1, '`=WENN(B3>=16;"ja";"nein")`'),
    ]),
    ('m2', [
        TAB('**M2:** Bestanden hat, wer höchstens 10 Fehlerpunkte hat.', ['Zelle', 'Formel'], [['E3 (Summe)', '[[=SUMME(B3:D3)]]'], ['F3 (bestanden?)', '[[=WENN(E3<=10;"Ja";"Nein")]]']], h=7, widths=[30, 70]),
    ]),
    ('m3', [
        A('**M3:** Ab einem Bestand von 20 oder weniger wird nachbestellt. Notiere zwei verschiedene Formeln für C3.', 2, '`=WENN(B3<=20;"Ja";"Nein")` // `=WENN(B3>20;"Nein";"Ja")`'),
    ]),
]),

'05_Datenbanken': dict(skip=['uebungen'],
    sections=[
    ('gut', [
        L('Werden dieselben Daten mehrfach gespeichert, spricht man von [[Redundanz]]. Ändert man sie nur an einer Stelle, entstehen Widersprüche – die Daten sind nicht mehr [[konsistent]].'),
    ]),
    ('dbs', [
        ZU('Ordne die Bausteine eines Datenbanksystems zu.', ['Anwendersoftware', 'Datenbankmanagementsystem', 'Datenbank', 'Metadaten'],
           ['enthält die eigentlichen Daten in Tabellen', 'Programm, mit dem Nutzer arbeiten', 'Daten über die Daten (Tabellen, Datentypen, Rechte)', 'nimmt Anfragen entgegen und greift auf die Daten zu'], loes=[3, 1, 4, 2]),
    ]),
    ('relational', [
        TAB('Ausleihe Nr. 2 hat P_Nr = 1 und F_Nr = 3. Ergänze.', ['Begriff', 'Beispiel aus der Videothek'],
            [['Primärschlüssel der Tabelle Filme', '[[F_Nr]]'], ['Fremdschlüssel in der Tabelle Ausleihe', '[[P_Nr, F_Nr]]'], ['Datenfeld (Attribut)', '[[z. B. F_Titel]]'], ['Wer hat Ausleihe Nr. 2 ausgeliehen?', '[[Michael (P_Nr 1)]]'], ['Welcher Film war es?', '[[Bad Boys (F_Nr 3)]]']], h=6, widths=[50, 50]),
    ]),
    ('abfrage', [
        GL('Lies die SQL-Abfrage.', ['`SELECT * FROM Filme WHERE F_Genre = \'Action\'` → zeigt [[alle Actionfilme]]', '`… WHERE F_FSK <= 12 ORDER BY F_Titel` → Filme bis FSK 12, [[nach Titel sortiert]]']),
    ]),
    ('m1', [
        A('**M1:** Anja und Elena Bohn haben dieselbe Adresse. Ist das eine Redundanz? Begründe.', 2, 'Nein. Es sind zwei verschiedene Personen mit eigener ID und eigenem Geburtsdatum. Redundant wäre derselbe Kunde zweimal.'),
        A('Erkläre die Bedeutung der ID-Nummern für die Datenbank.', 2, 'Die ID ist der Primärschlüssel und identifiziert jeden Datensatz eindeutig. Andere Tabellen verweisen über sie (als Fremdschlüssel) auf den Kunden.'),
    ]),
    ('m2', [
        A('**M2:** Erläutere am Beispiel Bahnticket, was Mehrbenutzerbetrieb bedeutet und warum kein Platz doppelt vergeben wird.', 2, 'Website, App, Automat und Reisebüro greifen als Clients gleichzeitig auf die zentrale Datenbank auf dem Server zu. Das DBMS sperrt einen Platz während der Buchung, sodass kein anderer Client ihn gleichzeitig buchen kann.'),
    ]),
]),

'06_Big_Data': dict(skip=['uebungen'],
    sections=[
    ('was', [
        SORT('Strukturiert oder unstrukturiert?', ['Kundentabelle', 'Urlaubsfoto', 'Sprachnachricht', 'Notenliste', 'E-Mail', 'Fahrplan-Datenbank'], ['strukturiert', 'unstrukturiert'], h=14,
             loes=[['Kundentabelle', 'Notenliste', 'Fahrplan-Datenbank'], ['Urlaubsfoto', 'Sprachnachricht', 'E-Mail']]),
        A('Beschreibe den Unterschied zwischen strukturierten und unstrukturierten Daten.', 2, 'Strukturierte Daten liegen in Zeilen und Spalten nach festem Muster vor (ca. 20 %), sind leichter zu verwalten. Unstrukturierte Daten wie Bilder, Videos, Texte haben kein festes Format (ca. 80 %).'),
    ]),
    ('merkmale', [
        L('Merkmale von Big Data: riesige [[Größe]] der Datenmengen, hohe [[Geschwindigkeit]], mit der Daten entstehen, große [[Vielfalt]] der Datenarten und die Frage nach der [[Richtigkeit]] der Daten.'),
    ]),
    ('nutzen', [
        A('Erkläre, wie ein Online-Shop aus vielen Warenkörben Empfehlungen ableitet.', 2, 'Er zählt, welche Produkte häufig zusammen gekauft werden (Muster). Kauft ein Kunde Chips, empfiehlt der Shop das Produkt, das am häufigsten zusammen mit Chips gekauft wurde, z. B. Cola.'),
    ]),
    ('m1', [
        TAB('**M1:** Nenne je zwei Chancen und Risiken von Big Data.', ['Chancen', 'Risiken'], [['[[Krankheiten früher erkennen]]', '[[Profile ohne Wissen der Nutzer]]'], ['[[Staus vorhersagen]]', '[[Datendiebstahl]]']], h=8),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Zelladresse', 'Funktion', 'Redundanz', 'Primärschlüssel', 'Big Data'],
           ['Daten sind mehrfach gespeichert', 'riesige, oft unstrukturierte Datenmengen', 'Spaltenbuchstabe + Zeilennummer', 'eindeutige ID eines Datensatzes', 'vorgefertigte Formel, z. B. SUMME'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('t1', [
        TAB('**T1:** Abschlussfahrt (Bus 150 €, Übernachtung 982 €, Eintritte 336 €, Stadtführung 95 €).', ['Aufgabe', 'Formel', 'Ergebnis'],
            [['Summe in B7', '[[=SUMME(B3:B6)]]', '[[1.563,00 €]]'], ['Bus + 15 % (C3)', '[[=B3*1,15]]', '[[172,50 €]]'], ['Übernachtung + 15 % (C4)', '[[=B4*1,15]]', '[[1.129,30 €]]'], ['Mehrkosten', '[[=C7-B7]]', '[[169,80 €]]']], h=6, widths=[34, 38, 28]),
    ]),
    ('t2', [
        GL('**T2:** Station A misst 23, 21, 22, 24, 24, 21, 23 °C.', ['Formel: [[=MITTELWERT(B3:B9)]]   ·   Mittelwert: [[≈ 22,6 °C]]']),
    ]),
    ('t3', [
        A('**T3:** Schreibe die Formel: „Ja“, wenn der Bestand in B3 unter 200 liegt, sonst „Nein“.', 1, '`=WENN(B3<200;"Ja";"Nein")`'),
    ]),
    ('t4', [
        GL('**T4:** Lina 8, Betys 12, Irida 11, Stefania 15, Ilcan 8 Stimmen.', ['Summe: [[54]] Stimmen   ·   Anteil Stefania: [[≈ 27,8 %]]   ·   passendes Diagramm für Anteile: [[Kreisdiagramm]]']),
    ]),
]),
}
