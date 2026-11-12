from render import *

WS = {
'01_Informatik': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere zum Navi je ein Beispiel für Darstellung, Speicherung, Übertragung und Verarbeitung.',
    sections=[
    ('darstellen', [
        L('**Informationen** sind [[Daten]] mit einem für Menschen verständlichen Inhalt. Die häufigste Darstellung ist der [[Text]]. Veränderungen über die Zeit zeigt ein [[Graph]], Beziehungen wie im Stammbaum eine [[Baumstruktur]].'),
    ]),
    ('zuordnen', [
        SORT('Sortiere die Beispiele nach ihrer typischen Darstellung.', ['Einkaufszettel', 'Aktienkurs', 'Stammbaum', 'Lageplan', 'Abfahrtstafel', 'Ordnerstruktur', 'Temperaturverlauf', 'Foto vom Treffpunkt'],
             ['Liste / Tabelle', 'Graph', 'Baum', 'Abbildung'], h=18,
             loes=[['Einkaufszettel', 'Abfahrtstafel'], ['Aktienkurs', 'Temperaturverlauf'], ['Stammbaum', 'Ordnerstruktur'], ['Lageplan', 'Foto vom Treffpunkt']]),
    ]),
    ('m1', [
        TAB('**M1 Aufgabe 1:** Stelle Jonas’ Verbindung zur Buchmesse strukturiert als Tabelle dar.', ['Uhrzeit', 'Verkehrsmittel', 'von', 'nach'],
            [['08:12', '[[Bus 21]]', '[[Dorfplatz]]', '[[Hauptbahnhof]]'], ['08:41', '[[S-Bahn S1]]', '[[Hauptbahnhof]]', '[[Messe]]'], ['09:10', '[[zu Fuß]]', '[[Messe]]', '[[Halle 3]]']], h=6),
        A('**M1 Aufgabe 2:** Nenne Medien, die die Wegbeschreibung verständlicher machen.', 1, 'Lageplan, Foto vom Treffpunkt, Karte mit Fußweg, Screenshot aus der App'),
    ]),
    ('informatik', [
        L('Informatik ist die Wissenschaft, die sich mit der [[Darstellung]], [[Speicherung]], [[Übertragung]] und [[Verarbeitung]] von Informationen beschäftigt.'),
        A('Erkläre, warum ein Navigationsgerät während der ganzen Fahrt eine Satellitenverbindung braucht.', 2, 'Die aktuelle Position ändert sich ständig. Nur über die Satelliten kann das Navi die Position bestimmen und die Route anpassen.'),
    ]),
    ('teilbereiche', [
        ZU('Ordne die Tätigkeiten den Teilbereichen der Informatik zu.', ['theoretische Informatik', 'technische Informatik', 'praktische Informatik', 'angewandte Informatik'],
           ['Röntgenbilder per Computer auswerten', 'einen schnelleren Prozessor entwerfen', 'eine Fahrplan-App programmieren', 'untersuchen, ob ein Problem lösbar ist'], loes=[4, 2, 3, 1]),
    ]),
    ('m2', [
        A('**M2 Aufgabe 1:** Beschreibe, wie die Informatik den Bezahlvorgang an der Kasse prägt.', 3, 'Der Scanner liest den Strichcode, der Preis wird im zentralen Rechner abgefragt, die Preise werden addiert, Einnahmen und Warenausgang gespeichert und der Bon wird gedruckt.'),
    ]),
]),

'02_EVA_Hardware': dict(skip=['uebungen'],
    heft_tpl='<div class="tpl"><div class="bx" style="--c:#2459D6;height:9mm;text-align:center">Eingabe</div><span class="ar">→</span><div class="bx" style="--c:#B45309;height:9mm;text-align:center">Verarbeitung</div><span class="ar">→</span><div class="bx" style="--c:#BE185D;height:9mm;text-align:center">Ausgabe</div></div>',
    heft_hint='Schreibe die Merksätze ab. Ergänze im EVA-Rahmen je zwei Geräte.',
    sections=[
    ('system', [
        SORT('Sortiere: Hardware, Software oder Netzwerkkomponente?', ['Prozessor', 'Betriebssystem', 'WLAN-Modul', 'Akku', 'Browser', 'Netzwerkkarte', 'Controller', 'Spiel'],
             ['Hardware', 'Software', 'Netzwerkkomponente'], h=16, loes=[['Prozessor', 'Akku', 'Controller'], ['Betriebssystem', 'Browser', 'Spiel'], ['WLAN-Modul', 'Netzwerkkarte']]),
        A('Begründe, ob ein Wasserhahn ein Informatiksystem ist.', 1, 'Ein normaler Wasserhahn nicht: Er hat keine Software und verarbeitet keine Daten. (Ein Sensor-Wasserhahn mit Chip schon.)'),
    ]),
    ('eva', [
        BOXES('Zerlege das Beispiel in das EVA-Prinzip: Du suchst am Tablet mit der Karten-App einen Ort.', ['Eingabe', 'Verarbeitung', 'Ausgabe'], 20,
              loes=['Ortsname über den Touchscreen', 'Prozessor sucht den Ort und berechnet die Route', 'Karte mit Route auf dem Bildschirm']),
    ]),
    ('eingabe', [
        L('Unter jeder Taste liegen zwei [[Folien]] mit Leiterbahnen. Beim Drücken berühren sie sich, der [[Stromkreis]] schließt sich und ein Chip sendet eine eindeutige Zahl an den Computer. Beim Touchscreen verändert der leitfähige [[Finger]] die Ladung im Raster.'),
    ]),
    ('komponenten', [
        ZU('Ordne die Komponenten ihren Aufgaben zu.', ['Prozessor (CPU)', 'Arbeitsspeicher (RAM)', 'SSD', 'Grafikeinheit', 'Hauptplatine', 'Lüfter'],
           ['berechnet die Bilder', 'kühlt den Prozessor', 'verbindet alle Komponenten', 'steuert alle Abläufe', 'speichert dauerhaft', 'Kurzzeitgedächtnis, flüchtig'], loes=[4, 6, 5, 1, 3, 2]),
    ]),
    ('m1', [
        A('**M1 Aufgabe 2:** Erkläre, warum Daten im Arbeitsspeicher schneller abgerufen werden als von der Festplatte.', 2, 'Der RAM enthält nur die Daten, mit denen der Prozessor gerade arbeitet, und ist direkt angebunden. Auf der Festplatte müssen die Daten erst aus einem großen Lager herausgesucht werden.'),
    ]),
]),

'03_Datenspeicherung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne für Mo–Do, welche Dateien das differentielle und das inkrementelle Backup sichern.',
    sections=[
    ('arten', [
        TAB('Ergänze die Tabelle.', ['Art der Speicherung', 'Wie werden 0 und 1 gespeichert?', 'Beispiel'],
            [['magnetisch', '[[Magnetisierung, Schreib-Lese-Kopf]]', '[[Festplatte (HDD)]]'], ['optisch', '[[Laser wird unterschiedlich reflektiert]]', '[[CD, DVD]]'], ['elektronisch', '[[Ladung in Speicherzellen]]', '[[SSD, USB-Stick]]']], h=8, widths=[22, 48, 30]),
    ]),
    ('vergleich', [
        A('Erkläre den Unterschied zwischen flüchtigen und permanenten Speichern.', 2, 'Flüchtige Speicher (RAM) verlieren ihre Daten, sobald der Strom weg ist. Permanente Speicher (SSD, HDD, USB-Stick) behalten sie.'),
        A('Erläutere, warum die Daten auf einer CD nicht mehr lesbar sein können, wenn sie zerkratzt ist.', 1, 'Die Kratzer stören die Reflexion des Laserstrahls, sodass 0 und 1 nicht mehr erkannt werden.'),
    ]),
    ('backup', [
        TAB('Am Sonntag gibt es ein Vollbackup. Mo wird das Referat, Di Mathe, Mi wieder das Referat geändert. Was sichert das Backup am Mittwoch?', ['Backup-Art', 'gesichert am Mittwoch'],
            [['Vollbackup', '[[alle Dateien]]'], ['differentiell', '[[Referat und Mathe]]'], ['inkrementell', '[[nur Referat]]']], h=7, widths=[30, 70]),
    ]),
    ('m1', [
        A('**M1 Aufgabe 1:** Erkläre, ob es sinnvoll ist, bei jeder Gelegenheit ein Vollbackup zu erstellen.', 2, 'Sehr sicher und einfach wiederherzustellen, aber es braucht viel Platz und Zeit. Besser: regelmäßig Vollbackup, dazwischen differentiell oder inkrementell.'),
        A('**M1 Aufgabe 2:** Entwickle eine eigene Backupstrategie.', 3, 'z. B. sonntags Vollbackup auf externe Festplatte (nicht neben dem Laptop aufbewahren), werktags inkrementell in die Cloud.'),
    ]),
]),

'04_Netzwerke': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Skizziere dein Heimnetzwerk.',
    sections=[
    ('lokal', [
        L('Ein [[LAN]] ist ein kabelgebundenes lokales Netzwerk, im [[WLAN]] funken die Geräte. Der [[Router]] verbindet die Geräte untereinander und mit dem Internet. Das [[Modem]] überträgt die Signale zum Provider.'),
    ]),
    ('verteiler', [
        ZU('Ordne die Netzwerkkomponenten ihren Aufgaben zu.', ['Router', 'Modem', 'Switch', 'Hub', 'Repeater'],
           ['verteilt Daten an alle Geräte', 'verstärkt Funksignale', 'verbindet verschiedene Netzwerke', 'verteilt Daten gezielt an das Zielgerät', 'überträgt Signale zum Internetanbieter'], loes=[4, 5, 1, 3, 2]),
        A('Erkläre, warum Switches meist bevorzugt werden, obwohl sie teurer sind.', 2, 'Ein Switch schickt Daten nur an den Empfänger. Die anderen Leitungen bleiben frei, es können mehr Daten gleichzeitig übertragen werden.'),
    ]),
    ('architektur', [
        TAB('Vergleiche die beiden Netzwerkarchitekturen.', ['', 'Client-Server', 'Peer-to-Peer'],
            [['Aufbau', '[[zentraler Server, viele Clients]]', '[[alle Rechner gleichberechtigt]]'], ['Vorteil', '[[zentrale Verwaltung und Speicherung]]', '[[kein Server nötig]]'], ['Nachteil', '[[fällt der Server aus, geht nichts]]', '[[jeder ist selbst verantwortlich]]']], h=9, widths=[16, 42, 42]),
    ]),
    ('m1', [
        L('Eine [[Firewall]] kontrolliert mit Regeln den Zugriff auf das Netzwerk. Bei einer [[Whitelist]] sind nur eingetragene Seiten erlaubt, bei einer [[Blacklist]] sind eingetragene Seiten gesperrt.'),
        A('**M1:** Nenne je zwei Adressen für die Whitelist einer Grundschule und die Blacklist eurer Schule.', 2, 'Whitelist: Lernplattform, Kindersuchmaschine. Blacklist: Glücksspielseiten, bekannte Betrugsseiten.'),
    ]),
]),

'05_Routing_Internet': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Markiere in 192.168.100.17 Netzwerk- und Hostanteil.',
    sections=[
    ('ip', [
        TAB('Gib Netzwerkanteil und Hostanteil an (Subnetzmaske 255.255.255.0).', ['IP-Adresse', 'Netzwerkanteil', 'Hostanteil'],
            [['192.245.178.24', '[[192.245.178]]', '[[24]]'], ['204.211.179.21', '[[204.211.179]]', '[[21]]'], ['147.103.98.12', '[[147.103.98]]', '[[12]]']], h=6),
        MC('Welche Geräte gehören zum selben Netzwerk wie 192.245.178.24?', ['*192.245.178.52', '192.245.179.24', '204.211.179.21', '*192.245.178.200'], cols=2),
    ]),
    ('routing', [
        A('Erkläre, was in einer Routingtabelle steht und warum sie regelmäßig neu berechnet wird.', 3, 'Sie gibt an, über welchen Nachbarn N ein Ziel Z mit wie vielen Sprüngen H erreicht wird. Sie wird neu berechnet, damit Routen angepasst werden können, wenn ein Router ausfällt oder ein anderer Weg günstiger ist.'),
    ]),
    ('pakete', [
        L('Große Datenmengen werden in [[Pakete]] zerteilt, die einzeln und oft auf [[unterschiedlichen]] Wegen zum Ziel reisen und dort wieder [[zusammengesetzt]] werden. Das [[DNS]] übersetzt Namen in IP-Adressen.'),
    ]),
    ('m1', [
        A('**M1:** Nenne die Elemente, aus denen das Internet besteht.', 1, 'Computer und Server, Router, Glasfaser- und Seekabel, Satelliten und Richtfunk, Provider'),
        A('**M1:** Nenne drei Tipps, wie du bei der Internetnutzung CO₂ sparen kannst.', 2, 'WLAN statt mobiler Daten, Videos in geringerer Auflösung, Autoplay aus, Ökostrom, Geräte lange nutzen'),
    ]),
]),

'06_Internetdienste_WWW': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne den Weg Browser → DNS-Server → Webserver → Browser.',
    sections=[
    ('dienste', [
        TAB('Ergänze die Protokolle.', ['Internetdienst', 'Protokoll'],
            [['Webseiten abrufen', '[[HTTP / HTTPS]]'], ['E-Mail senden', '[[SMTP]]'], ['Dateien übertragen', '[[FTP]]'], ['Internettelefonie', '[[VoIP]]']], h=6, widths=[55, 45]),
    ]),
    ('url', [
        TAB('Zerlege die URL https://www.schule-musterstadt.de/klasse7/stundenplan.html', ['Teil', 'Bezeichnung'],
            [['https', '[[Protokoll]]'], ['schule-musterstadt', '[[Domain]]'], ['.de', '[[Top-Level-Domain]]'], ['/klasse7/stundenplan.html', '[[Pfad und Datei]]']], h=6, widths=[55, 45]),
    ]),
    ('aufruf', [
        A('Beschreibe das Abrufen einer Webseite über einen Browser.', 4, 'Man gibt die URL ein. Der Browser fragt beim DNS-Server die IP-Adresse ab. Dann schickt er eine HTTP-Anfrage an den Webserver. Der Server antwortet mit einem Statuscode (z. B. 200 OK) und dem HTML-Dokument. Der Browser stellt die Seite dar.'),
    ]),
    ('html', [
        GL('Schreibe den HTML-Code.', ['Überschrift „Klasse 7b“: [[<h1>Klasse 7b</h1>]]', 'Das Wort „wichtig“ fett: [[<b>wichtig</b>]]', 'Ein Absatz „Hallo“: [[<p>Hallo</p>]]']),
    ]),
    ('m1', [
        A('**M1:** Begründe, warum es in bestimmten Fällen sinnvoll ist, HTTPS zu nutzen.', 2, 'Bei Anmeldungen, Onlinebanking oder Einkäufen werden vertrauliche Daten übertragen. HTTPS verschlüsselt sie, sodass Lauscher sie nicht lesen können.'),
    ]),
]),

'07_Cloud': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege eine Tabelle mit je drei Vor- und Nachteilen an.',
    sections=[
    ('aufbau', [
        L('Eine Cloud ist ein Netz verbundener [[Server]] in Serverfarmen. Man greift über das [[Internet]] darauf zu. Eine Musik-App lädt ein Lied vom Server und spielt es ab, ohne es dauerhaft zu [[speichern]].'),
    ]),
    ('sync', [
        A('Erkläre, was beim Synchronisieren passiert, wenn ein Gerät offline ist.', 2, 'Neue Dateien bleiben zunächst nur auf dem Gerät. Sobald es wieder online ist, werden sie hochgeladen und an alle anderen Geräte verteilt.'),
    ]),
    ('m1', [
        A('**M1:** Beschreibe mithilfe des Diagramms, wofür Clouds privat am meisten genutzt werden.', 2, 'Am häufigsten für Fotos und Videos (78 %), dann Dokumente (64 %) und Backups (51 %).'),
    ]),
    ('m2', [
        TAB('**M2:** Stelle Vor- und Nachteile von Clouds gegenüber.', ['Vorteile', 'Nachteile'],
            [['[[Zugriff von überall]]', '[[nur mit Internet]]'], ['[[Schutz vor Datenverlust]]', '[[Datenschutz, Anbieter außerhalb der EU]]'], ['[[gemeinsam bearbeiten]]', '[[Gefahr durch Hacker]]']], h=7),
        A('**M2:** Nimm Stellung zu Alinas Aussage „Ich habe nichts zu verbergen“.', 3, 'Auch private Fotos, Adressen und Nachrichten können missbraucht werden. Viele Anbieter unterliegen nicht dem europäischen Datenschutz. Deshalb: sicheres Passwort, vertrauenswürdiger Anbieter, sensible Daten nicht hochladen.'),
    ]),
]),

'08_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe den Erklärungen zu.', ['Informatik', 'RAM', 'Router', 'DNS', 'HTML'],
           ['übersetzt Namen in IP-Adressen', 'Auszeichnungssprache für Webseiten', 'flüchtiger Arbeitsspeicher', 'verbindet Netzwerke', 'Wissenschaft von der Verarbeitung von Informationen'], loes=[4, 5, 2, 3, 1]),
    ]),
    ('t1', [
        A('**T1:** Erkläre das EVA-Prinzip am Beispiel eines Kassenscanners.', 2, 'Eingabe: Scanner liest den Strichcode. Verarbeitung: Kassenrechner sucht den Preis und addiert. Ausgabe: Display zeigt die Summe, der Drucker druckt den Bon.'),
    ]),
    ('t2', [
        RF(['r|Eine HDD speichert magnetisch.', 'f|Der RAM ist ein permanenter Speicher.|Der RAM ist flüchtig.', 'f|Ein inkrementelles Backup sichert alle Daten.|Es sichert nur Änderungen seit dem letzten Backup.']),
    ]),
    ('t3', [
        A('**T3:** Gib Netzwerk- und Hostanteil von 192.168.100.17 an und erkläre den Unterschied zwischen Hub und Switch.', 2, 'Netzwerkanteil 192.168.100, Hostanteil 17. Ein Hub schickt Daten an alle Geräte, ein Switch nur an den Empfänger.'),
    ]),
    ('t4', [
        A('**T4:** Beschreibe in Stichpunkten, was beim Aufruf einer Webseite passiert.', 2, 'URL eingeben → DNS liefert IP-Adresse → HTTP-Anfrage → Statuscode und HTML zurück → Browser zeigt die Seite an.'),
    ]),
]),
}
