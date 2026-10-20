from render import *

# Vorgedruckter EVA-Rahmen im Hefteintrag (die Schüler tragen Geräte ein)
EVA_TPL = ('<div class="tpl"><div class="bx" style="--c:#2459D6">E · Eingabe</div><span class="ar">→</span>'
           '<div class="bx" style="--c:#B45309">V · Verarbeitung</div><span class="ar">→</span>'
           '<div class="bx" style="--c:#BE185D">A · Ausgabe</div></div>')

WS = {
'02_Informatiksysteme': dict(
    heft_tpl=EVA_TPL,
    skip=['uebungen'],  # Übungen nur interaktiv in der Präsentation
    heft_hint='Trage zuerst in die drei Kästen Beispielgeräte ein. Schreibe dann die Merksätze aus der Präsentation darunter.',
    heft_loes=('<p><b>E</b> Eingabe: Tastatur, Maus, Mikrofon, Kamera → <b>V</b> Verarbeitung: Prozessor (CPU) → <b>A</b> Ausgabe: Bildschirm, Drucker, Lautsprecher</p><ol>'
               '<li>Ein <b>Informatiksystem</b> besteht aus <b>Hardware</b> (Geräte und Bauteile) und <b>Software</b> (Programme). Über ein <b>Netzwerk</b> tauschen Systeme Daten aus; das größte ist das Internet.</li>'
               '<li>Computer arbeiten nach dem <b>EVA-Prinzip</b>: Eingabe → Verarbeitung → Ausgabe.</li>'
               '<li><b>Eingabegeräte</b> geben Daten in den Computer ein, z. B. Tastatur, Maus, Mikrofon, Kamera, Controller.</li>'
               '<li>Der <b>Prozessor (CPU)</b> verarbeitet die Daten, zusammen mit Arbeitsspeicher und Grafikkarte.</li>'
               '<li><b>Ausgabegeräte</b> geben die Ergebnisse aus, z. B. Bildschirm, Drucker, Lautsprecher, Kopfhörer.</li>'
               '<li>Manche Geräte sind <b>Ein- und Ausgabegerät zugleich</b>, z. B. Touchscreen oder Headset.</li>'
               '<li>Die <b>Geschichte der Kommunikation</b> reicht von der Höhlenmalerei über Buchdruck, Telefon und Computer bis zum Internet und zur künstlichen Intelligenz. Nachrichten werden immer schneller übertragen.</li></ol>'),
    sections=[
    ('systeme', [
        L('Ein Informatiksystem besteht aus [[Hardware]] (Teile zum Anfassen) und [[Software]] (Programme). '
          'Über ein [[Netzwerk]] tauschen Systeme Daten aus. Das größte Netzwerk ist das [[Internet]].'),
        A('**A** Nenne drei Informatikgeräte, die du nutzt, und begründe, wofür du sie nutzt.', 2,
          'individuell, z. B. Smartphone (Nachrichten, Fotos), Laptop (Hausaufgaben, Recherche), Spielkonsole (Spielen)'),
    ]),
    ('eva', [
        L('Computer arbeiten nach dem [[EVA]]-Prinzip: [[Eingabe]] → [[Verarbeitung]] → [[Ausgabe]]. '
          'Die Daten verarbeitet vor allem der [[Prozessor]] (CPU) mit Arbeitsspeicher und Grafikkarte. '
          'Besteht ein System aus mehreren Geräten, müssen sie miteinander [[verbunden]] sein.'),
    ]),
    ('smartphone', [
        TAB('Kreuze an: Wozu gehören die Bauteile des Smartphones (Abb. 2)?', ['Bauteil', 'Eingabe', 'Verarbeitung', 'Ausgabe'],
            [['Kamera', '[[✗]]', '', ''], ['Lagesensor', '[[✗]]', '', ''], ['Prozessor (innen)', '', '[[✗]]', ''],
             ['Lautsprecher', '', '', '[[✗]]'], ['Touchscreen', '[[✗]]', '', '[[✗]]']], h=5.5, widths=[40, 20, 20, 20]),
    ]),
    ('m1', [
        TAB('**Aufgabe 1** Ordne den Geräten die Begriffe Ein- oder Ausgabegerät zu. Begründe deine Zuordnung.',
            ['Gerät', 'Ein- oder Ausgabe?', 'Begründung'],
            [['Kopfhörer', '[[Ausgabe]]', '[[gibt Töne aus]]'], ['Controller', '[[Eingabe]]', '[[Tasten geben Befehle ein]]'],
             ['Maus', '[[Eingabe]]', '[[Bewegungen und Klicks werden eingegeben]]'], ['Drucker', '[[Ausgabe]]', '[[gibt Texte und Bilder auf Papier aus]]'],
             ['Tastatur', '[[Eingabe]]', '[[Buchstaben und Zahlen werden eingegeben]]'], ['Bildschirm', '[[Ausgabe]]', '[[zeigt Bilder und Texte an]]']],
            h=6, widths=[20, 22, 58]),
        A('**Aufgabe 2** Nenne je zwei weitere Beispiele für Eingabe- und Ausgabegeräte.', 2,
          'Eingabegeräte: z. B. Webcam, Mikrofon, Scanner, Joystick, Touchpad // Ausgabegeräte: z. B. Beamer, Lautsprecher, 3D-Drucker, Smartwatch-Display'),
    ]),
    ('karte', [
        BOXES('**Aufgabe 3** Beschreibe das EVA-Prinzip: Du suchst am Tablet mit der Karten-App einen Ort.', ['Eingabe', 'Verarbeitung', 'Ausgabe'], 24,
              loes=['Ich tippe den Ortsnamen über den Touchscreen ein (oder spreche ihn ins Mikrofon).',
                    'Der Prozessor sucht den Ort in den Kartendaten und berechnet den Kartenausschnitt; die Grafikkarte erzeugt das Bild.',
                    'Der Bildschirm zeigt die Karte mit einer Markierung am gesuchten Ort (evtl. Ansage über den Lautsprecher).']),
    ]),
    ('headset', [
        A('**Aufgabe 4** Erkläre am Beispiel eines Headsets, dass die Zuordnung in Ein- und Ausgabegerät nicht immer eindeutig ist.', 3,
          'Ein Headset besteht aus Kopfhörern und einem Mikrofon. Über die Kopfhörer werden Töne ausgegeben (Ausgabe), über das Mikrofon wird die Stimme eingegeben (Eingabe). '
          'Das Headset ist also Ein- und Ausgabegerät zugleich; die Zuordnung hängt davon ab, welches Bauteil man betrachtet.'),
    ]),
    ('zeitleiste', [
        TAB('Ergänze die Jahreszahlen aus der Zeitleiste und nummeriere die Erfindungen in der richtigen Reihenfolge (1 = älteste).',
            ['Erfindung', 'Jahr', 'Nr.', 'Erfindung', 'Jahr', 'Nr.'],
            [['Telefonie', '[[1876]]', '[[3]]', 'Buchdruck', '[[1452]]', '[[1]]'],
             ['Öffnung WWW', '[[1991]]', '[[5]]', 'Telegrafie', '[[1837]]', '[[2]]'],
             ['ChatGPT', '[[2022]]', '[[6]]', 'Computer', '[[1941]]', '[[4]]']], h=5.5, widths=[24, 13, 9, 24, 13, 9]),
    ]),
    ('zl-aufgaben', [
        SORT('Halten diese Erfindungen Informationen **fest** oder **übertragen** sie sie in die Ferne? Sortiere.',
             ['Höhlenmalerei', 'Rauchzeichen', 'Buchdruck', 'Telegrafie', 'Fotografie', 'Telefonie', 'Schallplatte', 'E-Mail'],
             ['Informationen festhalten', 'In die Ferne übertragen'], h=12,
             loes=[['Höhlenmalerei', 'Buchdruck', 'Fotografie', 'Schallplatte'], ['Rauchzeichen', 'Telegrafie', 'Telefonie', 'E-Mail']]),
    ]),
]),

'01_Informationen_Medien': dict(
    heft_hint='Schreibe die Merksätze ab und zeichne die Informationsübertragung (Sender → Daten/Medium → Empfänger).',
    sections=[
    ('auftakt', [
        SORT('Ordne die Begriffe der Mindmap den Ästen zu.', ['Tastatur', 'Betriebssystem', 'Tablet', 'Daten', 'Grafikkarte', 'Computerspiele', 'Smartphone', 'Informationen'],
             ['Hardware', 'Software', 'Computer', 'Informatik im Alltag'], h=11,
             loes=[['Tastatur', 'Grafikkarte'], ['Betriebssystem', 'Computerspiele'], ['Tablet', 'Smartphone'], ['Daten', 'Informationen']]),
    ]),
    ('information', [
        L('Eine Information muss erst dargestellt werden, bevor man sie weitergeben kann. Das Darstellen nennt man [[Repräsentation]]. '
          'Zur Weitergabe braucht man ein [[Trägermedium]], z. B. Papier, einen Bildschirm oder die Luft.'),
        A('Nenne drei Arten, wie man die Information „Mir ist kalt.“ darstellen kann.', 1, 'sagen (Sprache), schreiben (Text), Emoji senden (Bild), Arme verschränken oder bibbern (Geste)'),
    ]),
    ('sprache', [
        A('Erkläre am Datum 09.04.27, warum eine gemeinsame Sprache wichtig ist.', 2,
          'In Deutschland bedeutet es der 9. April 2027, in den USA der 4. September 2027, weil dort der Monat vorne steht. Ohne gleiche Regeln interpretiert der Empfänger die Daten falsch.'),
    ]),
    ('daten', [
        TAB('Ein Schäfer hat 20 Schafe und schnitzt 20 Kerben in einen Ast. Ergänze.', ['Information', 'Daten', 'Medium'],
            [['[[20 Schafe]]', '[[20 Kerben]]', '[[der Ast]]']], h=7),
    ]),
    ('medien', [
        A('Nenne zwei Möglichkeiten, wie Medien manipulieren können, und wie du dich davor schützt.', 2,
          'Einseitig berichten, wichtige Details weglassen, Bilder verändern. // Schutz: Informationen kritisch prüfen und verschiedene Quellen vergleichen.'),
    ]),
    ('m1', [
        TAB('**M1 Aufgabe 3:** Ordne den Bildern die Begriffe Repräsentation, Interpretation, Information und Daten zu.', ['Bild', 'Begriff'],
            [['Junge hat eine Idee für ein Lied', '[[Information]]'], ['Junge schreibt die Noten auf', '[[Repräsentation]]'],
             ['das fertige Notenblatt', '[[Daten]]'], ['eine Band spielt das Lied', '[[Interpretation]]']], h=6, widths=[60, 40]),
        A('**M1 Aufgabe 5:** Nimm Stellung: „Noten sind die Sprache der Musik.“', 2,
          'Dafür: Noten sind eine gemeinsame Sprache mit festen Regeln, Musiker weltweit können sie lesen. Dagegen: Nicht jeder kann Noten lesen, und Gefühl oder Stil lassen sich nur teilweise aufschreiben.'),
    ]),
    ('uebungen', [
        RF(['r|Ein Emoji ist eine Form der Repräsentation.',
            'f|Medien zeigen immer alle Details einer Nachricht.|Medien können Details weglassen oder einseitig berichten.',
            'r|Beim Schäfer sind die Kerben die Daten.']),
    ]),
]),

'03_Aufbau_Computer': dict(
    heft_hint='Schreibe die Merksätze ab und zeichne den Programmstart als Pfeilkette: Benutzer → CPU → RAM → Monitor.',
    sections=[
    ('komponenten', [
        ZU('Ordne die Komponenten ihren Aufgaben zu.', ['Prozessor (CPU)', 'Arbeitsspeicher (RAM)', 'Festplatte (HDD/SSD)', 'Grafikkarte', 'Netzteil', 'Hauptplatine'],
           ['versorgt alle Komponenten mit Energie', 'verarbeitet alle Daten und steuert die Abläufe', 'verbindet alle Komponenten miteinander',
            'speichert Daten dauerhaft', 'wandelt die Abläufe in Bilder um', 'speichert Daten nur kurz, solange sie gebraucht werden'], loes=[5, 1, 6, 3, 4, 2]),
    ]),
    ('prozessor', [
        L('Die zentrale Komponente ist der [[Prozessor]], auch [[CPU]] genannt. Er steuert alle Abläufe. Dabei wird er warm, deshalb kühlt ihn ein [[Lüfter]].'),
    ]),
    ('speicher', [
        TAB('Vergleiche die beiden Speicher.', ['', 'Arbeitsspeicher (RAM)', 'Festplatte (HDD/SSD)'],
            [['Name', '[[Hauptspeicher]]', '[[sekundärer Speicher]]'], ['beim Ausschalten', '[[Daten werden gelöscht]]', '[[Daten bleiben erhalten]]'],
             ['vergleichbar mit', '[[Kurzzeitgedächtnis]]', '[[Langzeitgedächtnis]]']], h=6.5, widths=[24, 38, 38]),
    ]),
    ('weitere', [
        A('Erkläre, warum man die Grafikkarte als „eigenen kleinen Computer“ bezeichnen kann.', 1, 'Sie hat eine große Rechenleistung und ist komplex aufgebaut; sie berechnet selbstständig die Bilder.'),
    ]),
    ('m1', [
        A('**M1 Aufgabe 1:** Beschreibe, wie die Komponenten beim Aufrufen eines Programms zusammenwirken.', 3,
          'Der Benutzer öffnet das Programm. Die CPU holt sich das Programm von der Festplatte. Der RAM erhält eine Kopie der Programmanweisungen. Der Monitor stellt das Programm dar.'),
        A('**M1 Aufgabe 2:** Beschreibe, was mit den Daten im RAM geschieht, nachdem das Programm geschlossen wird.', 1,
          'Sie werden freigegeben bzw. gelöscht; nicht gespeicherte Arbeit geht verloren.'),
        A('**M1 Aufgabe 4:** Stelle Vermutungen an, warum moderne Grafikkarten bis zu drei Lüfter besitzen.', 1,
          'Sie rechnen sehr viel und werden dabei heiß; mehrere Lüfter kühlen besser (und leiser).'),
    ]),
    ('uebungen', [
        RF(['f|Der RAM speichert Daten dauerhaft.|Der RAM verliert die Daten beim Ausschalten.',
            'r|Alle Komponenten sind mit der Hauptplatine verbunden.',
            'r|SSD und HDD sind sekundäre Speicher.']),
    ]),
]),

'04_Programme_Dateien': dict(
    heft_hint='Schreibe die Merksätze ab und zeichne einen kleinen Ordnerbaum mit sinnvollen Dateinamen.',
    sections=[
    ('anmelden', [
        L('Zur Anmeldung braucht man [[Zugangsdaten]]: einen [[Benutzernamen]] und ein [[Kennwort]]. Alternativen sind eine [[PIN]], ein [[Fingerabdruck]] oder die Gesichtserkennung.'),
    ]),
    ('desktop', [
        A('Beschreibe, was man in der Taskleiste findet.', 2, 'Den Zugang zum Startmenü, die Suche, Informationen zu Netzwerkzustand, Akkuzustand, Lautstärke sowie Datum und Uhrzeit.'),
    ]),
    ('formate', [
        TAB('**M1** Ordne den Datei-Endungen die Dateiformate und Programme zu.', ['Endung', 'Dateiformat', 'Programm'],
            [['.doc', 'Textdokument', 'Textverarbeitung'], ['.mp4', '[[Video]]', '[[Videoplayer]]'], ['.ppt', '[[Präsentation]]', '[[Präsentationsprogramm]]'],
             ['.pdf', '[[PDF-Dokument]]', '[[PDF-Anzeigeprogramm]]'], ['.jpg', '[[Foto/Bild]]', '[[Bildbetrachter]]']], h=6, widths=[18, 36, 46]),
    ]),
    ('ordner', [
        A('**M2 Aufgabe 2:** Nenne Vorteile und Nachteile vom Speichern in Ordnerstrukturen.', 2,
          'Vorteile: schnell wiederfinden, übersichtlich. // Nachteile: Ordner anlegen kostet Zeit; falsch abgelegte Dateien findet man schwer.'),
        BOX('**M2 Aufgabe 4:** Zeichne eine Ordnerstruktur für: Mathe_Hausaufgabe.docx, Anmeldung_Verein.pdf, Trainingsplan.pdf, Englisch_Vokabeln.pdf, Klassenfoto.jpg.', 32,
            loes='Dokumente → Hausaufgaben (Mathe_Hausaufgabe.docx, Englisch_Vokabeln.pdf), Sportverein (Anmeldung_Verein.pdf, Trainingsplan.pdf); Bilder → Klassenfoto.jpg'),
    ]),
    ('uebungen', [
        MC('Welche Dateinamen sind sinnvoll? Kreuze an.', ['*Bio_Referat_Fledermaus.pptx', 'Dokument1.docx', '*Klassenfahrt_Bodensee_2025.jpg', 'asdf.pdf'], cols=2),
    ]),
]),

'05_Datenspeicherung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Lege eine Tabelle an: Speicherart – So funktioniert es – Beispiele.',
    sections=[
    ('dokument', [
        SORT('Intern oder extern? Sortiere die Speicher.', ['USB-Stick', 'SSD im Laptop', 'externe Festplatte', 'Speicher im Smartphone', 'gebrannte CD'],
             ['intern', 'extern'], h=11, loes=[['SSD im Laptop', 'Speicher im Smartphone'], ['USB-Stick', 'externe Festplatte', 'gebrannte CD']]),
        A('Nenne zwei Risiken externer Speicher.', 1, 'Bei Beschädigung kommt man nicht mehr an die Daten; bei Verlust können Fremde die Daten lesen.'),
    ]),
    ('arten', [
        TAB('Vervollständige die Tabelle.', ['Speicherart', 'So funktioniert es', 'Beispiele'],
            [['optisch', '[[Laserstrahl, Reflexion]]', '[[CD, DVD]]'], ['magnetisch', '[[magnetisierbares Material, Lese-Schreib-Kopf]]', '[[HDD, Kassette]]'],
             ['elektronisch', '[[elektronische Bauteile]]', '[[SSD, Speicherkarte, RAM]]']], h=7, widths=[20, 45, 35]),
    ]),
    ('backup', [
        TAB('**M1 Aufgabe 1:** Vervollständige.', ['Backup-Art', 'gesicherte Daten'],
            [['Voll-Backup', 'alle Daten'], ['differentielles Backup', '[[alle Daten, die seit dem letzten Voll-Backup geändert wurden]]'],
             ['inkrementelles Backup', '[[nur Änderungen seit dem letzten Backup]]']], h=7, widths=[30, 70]),
    ]),
    ('m1', [
        A('**M1 Aufgabe 2:** Erkläre, ob es sinnvoll ist, bei jeder Gelegenheit ein Voll-Backup zu erstellen.', 2,
          'Ein Voll-Backup ist sicher, braucht aber viel Zeit und Speicherplatz, weil auch Unverändertes jedes Mal gesichert wird. Besser: Voll-Backup mit differentiellen oder inkrementellen Backups kombinieren.'),
        A('**M1 Aufgabe 3:** Entwickle deine Backup-Strategie (wie oft, welche Art, welches Medium).', 3,
          'z. B. einmal im Monat ein Voll-Backup auf eine externe Festplatte, jede Woche ein differentielles Backup; die Festplatte sicher getrennt vom Laptop aufbewahren.'),
    ]),
]),

'06_Computerspiele': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne einen Zeitstrahl 1970 bis heute mit je einer Neuerung pro Jahrzehnt.',
    sections=[
    ('geschichte', [
        TAB('Ergänze je eine Neuerung.', ['Jahrzehnt', 'Neuerung'],
            [['1970er', '[[erste Videospiele (Pong), Arcade-Automaten]]'], ['1980er', '[[Heimkonsolen, erster Handheld]]'], ['1990er', '[[3D-Grafik, CD-ROM]]'],
             ['2000er', '[[Online-Spiele, Multiplayer, Bewegungssteuerung]]'], ['2010er', '[[Virtual Reality, Smartphone-Spiele, Augmented Reality]]'], ['ab 2020', '[[Cloud Gaming, 4K, KI]]']], h=6, widths=[20, 80]),
    ]),
    ('m1', [
        ZU('**M1 Aufgabe 1:** Ordne die Abbildungen den Jahrzehnten zu.', ['1970er', '2000er', '2010er'],
           ['Senioren spielen mit Bewegungs-Controller', 'Mann spielt mit dem Smartphone draußen (AR)', 'Spielautomat in einer Spielhalle'], loes=[2, 3, 1]),
    ]),
    ('fps', [
        A('**M2:** Erkläre, was FPS bedeutet und warum sie bei einem Rennspiel wichtiger sind als bei einem Puzzle-Spiel.', 2,
          'FPS = Frames per Second, Bilder pro Sekunde. Je mehr FPS, desto flüssiger. Beim Rennspiel bewegt sich alles schnell und man muss sofort reagieren; beim Puzzle bewegt sich wenig.'),
    ]),
    ('cloud', [
        L('Beim [[Cloud Gaming]] läuft das Spiel auf einem leistungsstarken [[Server]] und wird als [[Video]] auf das eigene Gerät übertragen.'),
    ]),
    ('entwickeln', [
        A('**Expertenwissen:** Nenne die Phasen der Entwicklung eines Computerspiels in der richtigen Reihenfolge.', 2,
          'Idee und Konzept → Game-Design → Produktion (Programmierung, Figuren, Sound, Design) → Testphase und Fehlerbehebung → Werbung → Veröffentlichung → Updates und DLC'),
    ]),
    ('faehigkeiten', [
        A('Nenne drei Fähigkeiten, die Gaming fördern kann, und zwei Regeln für einen bewussten Umgang.', 2,
          'Reaktionsgeschwindigkeit, Problemlösefähigkeit, Teamarbeit/Kommunikation, Konzentration, Sprache. // Altersgerechte Spiele wählen, Bildschirmzeit im Blick behalten, Pausen machen.'),
    ]),
    ('fussball', [
        TAB('**M1:** Vergib Punkte von 1 (sehr schwach) bis 5 (sehr stark).', ['Fähigkeit', 'analoges Fußballspiel', 'digitales Fußballspiel'],
            [['Teamfähigkeit', '', ''], ['körperliche Fitness', '', ''], ['Geschicklichkeit', '', ''], ['strategisches Denken', '', ''], ['Kommunikation', '', '']], h=5.5, widths=[36, 32, 32]),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe den Erklärungen zu.', ['Hardware', 'Software', 'Backup', 'Repräsentation', 'Dateiformat'],
           ['Sicherungskopie von Daten', 'wird an der Endung erkannt', 'Darstellen einer Information', 'alles, was man anfassen kann', 'Programme, die auf dem Gerät laufen'], loes=[3, 5, 4, 1, 2]),
    ]),
    ('t1', [
        A('**T1:** Erkläre das EVA-Prinzip an einem Beispiel am Computer.', 2,
          'Eingabe: Text über die Tastatur. Verarbeitung: Der Prozessor verarbeitet die Daten mit dem Arbeitsspeicher. Ausgabe: Der Monitor zeigt den Text, der Drucker druckt ihn.'),
    ]),
    ('t2', [
        A('**T2:** Erkläre den Unterschied zwischen Hauptspeicher und sekundärem Speicher.', 2,
          'Der Hauptspeicher (RAM) speichert nur kurz und verliert die Daten beim Ausschalten. Der sekundäre Speicher (HDD/SSD) speichert dauerhaft.'),
    ]),
    ('t3', [
        A('**T3:** Nenne den Unterschied zwischen einem differentiellen und einem inkrementellen Backup.', 2,
          'Differentiell: alles seit dem letzten Voll-Backup Geänderte. Inkrementell: nur die Änderungen seit dem letzten Backup.'),
    ]),
    ('t4', [
        A('**T4:** Beschreibe, wie du vom Anmelde-Bildschirm in ein Textverarbeitungsprogramm gelangst.', 2,
          'Benutzername und Kennwort eingeben, anmelden; im Desktop über die Taskleiste das Startmenü öffnen; die Textverarbeitung suchen und anklicken.'),
    ]),
    ('quiz-st', [
        RF(['r|Ein Touchscreen ist Ein- und Ausgabegerät.', 'f|Eine CD ist ein magnetischer Speicher.|Eine CD ist ein optischer Speicher.']),
    ]),
]),
}
