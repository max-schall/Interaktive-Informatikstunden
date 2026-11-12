from render import *

WS = {
'01_Digitaler_Wandel': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und stelle Vor- und Nachteile des Online-Handels in einer Tabelle gegenüber.',
    sections=[
    ('medien', [
        TAB('Ordne die Erfindungen zeitlich (1 = älteste).', ['Erfindung', 'Handy', 'Buchdruck', 'Telefon', 'World Wide Web', 'Radio'], [['Reihenfolge', '[[4]]', '[[1]]', '[[2]]', '[[5]]', '[[3]]']], h=6),
        A('Wähle eine Erfindung und bewerte, wie sie Alltag und Kommunikation verändert hat.', 2, 'z. B. Smartphone: Kommunikation jederzeit und überall, Bilder und Videos in Sekunden weltweit – aber auch ständige Erreichbarkeit.'),
    ]),
    ('jugend', [
        A('Vergleiche deine eigene Internetnutzung mit den Ergebnissen der Studie.', 2, ''),
    ]),
    ('handel', [
        TAB('Vergleiche den Kauf einer Jacke.', ['', 'im Laden', 'online'], [['Vorteile', '[[anprobieren, Beratung, sofort mitnehmen]]', '[[rund um die Uhr, große Auswahl, Lieferung]]'], ['Nachteile', '[[Öffnungszeiten, kleinere Auswahl]]', '[[Rücksendungen, Müll, Daten werden gesammelt]]']], h=10),
    ]),
    ('industrie', [
        A('Beschreibe zwei Beispiele für Industrie 4.0 und erläutere, wie sie die Produktion effizienter machen.', 3, 'Wartungssensoren melden Probleme, bevor eine Maschine ausfällt – weniger Stillstand. Fahrerlose Transportsysteme bringen Teile genau dann, wenn sie gebraucht werden – keine Wartezeiten, weniger Lager.'),
        A('Nenne ein Risiko der Industrie 4.0.', 1, 'Arbeitsplätze können wegfallen; viele Daten werden gesammelt.'),
    ]),
]),

'02_Personenbezogene_Daten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Prüfe die Berechtigungen von drei Apps und notiere, was du geändert hast.',
    sections=[
    ('arten', [
        SORT('Sortiere die personenbezogenen Daten.', ['Name', 'IBAN', 'E-Mail-Adresse', 'Körpergröße', 'Geburtsdatum', 'IP-Adresse', 'Kreditkartennummer', 'Augenfarbe'],
             ['allgemeine Daten', 'Bankdaten', 'Onlinedaten', 'physische Merkmale'], h=14, loes=[['Name', 'Geburtsdatum'], ['IBAN', 'Kreditkartennummer'], ['E-Mail-Adresse', 'IP-Adresse'], ['Körpergröße', 'Augenfarbe']]),
        L('Seit [[2018]] gilt in der ganzen EU die [[Datenschutz-Grundverordnung]] (DSGVO).'),
    ]),
    ('profil', [
        A('Nenne drei Tipps für den Umgang mit persönlichen Daten in sozialen Netzwerken.', 2, 'Überlege genau, was du veröffentlichst · gib nur das Nötigste an · stelle das Profil auf privat · nutze sichere, verschiedene Passwörter.'),
    ]),
    ('cookies', [
        TAB('Cookies: nützlich oder problematisch?', ['nützlich', 'problematisch'], [['[[Warenkorb bleibt gespeichert]]', '[[Surfverhalten wird aufgezeichnet]]'], ['[[Anmeldung bleibt erhalten]]', '[[personalisierte Werbung]]']], h=7),
    ]),
    ('m1', [
        TAB('**M1:** Welche Berechtigungen braucht die App wirklich?', ['App', 'nötige Berechtigungen'], [['Taschenlampe', '[[Kamera (Blitz)]]'], ['Karten-App', '[[Standort]]'], ['Dokumenten-Scanner', '[[Kamera, Fotos]]']], h=6, widths=[35, 65]),
    ]),
]),

'03_Digitale_Kommunikation': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere fünf Netiquette-Regeln für euren Klassenchat.',
    sections=[
    ('arten', [
        A('Begründe, warum man bei der Wahl der E-Mail-Adresse vorsichtig sein sollte.', 2, 'Die Adresse wird auch für Bewerbungen, Schule und Behörden genutzt. Eine unseriöse Adresse macht einen schlechten Eindruck.'),
    ]),
    ('kollab', [
        ZU('Ordne zu.', ['Forum', 'Wiki', 'Blog', 'Vlog'], ['Tagebuch im Internet', 'Diskussion in Postings und Threads', 'Blog mit Videos', 'jeder kann die Seite bearbeiten'], loes=[3, 1, 4, 2]),
    ]),
    ('wiki', [
        A('Erkläre, warum ein Wiki trotz „Vandalismus“ zuverlässig sein kann.', 2, 'Jede Änderung wird in der Versionsgeschichte gespeichert. Falsche Änderungen können schnell erkannt und eine frühere Version wiederhergestellt werden.'),
    ]),
    ('m1', [
        A('**M1:** Schreibe den Beitrag „WIE GEHT DAS??? eure anleitung is müll“ so um, dass er die Netiquette einhält.', 3, 'z. B. „Hallo zusammen, ich komme mit der Anleitung leider nicht weiter. Könnt ihr mir sagen, wie ich das Update starte? Vielen Dank!“'),
    ]),
]),

'04_Risiken': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere die fünf Warnzeichen einer Phishing-Mail als Checkliste.',
    sections=[
    ('chancen', [
        TAB('Nenne je zwei Chancen und Risiken der digitalen Kommunikation.', ['Chancen', 'Risiken'], [['[[Videochat mit Verwandten]]', '[[Cybermobbing]]'], ['[[Online-Unterricht]]', '[[Phishing und Schadprogramme]]']], h=7),
    ]),
    ('mobbing', [
        A('Beschreibe, was du tun kannst, wenn du von Cybermobbing betroffen bist.', 3, 'Nicht antworten, Beweise mit Screenshots sichern, Täter blockieren und melden, mit Vertrauensperson sprechen (Eltern, Lehrkraft, Nummer gegen Kummer 116 111), ggf. Anzeige erstatten.'),
    ]),
    ('phishing', [
        L('Warnzeichen einer Phishing-Mail: gefälschte [[Absender]]-Adresse, vorgetäuschter [[Zeitdruck]], Abfrage [[vertraulicher]] Daten, [[Links]] zu gefälschten Webseiten und sprachliche [[Fehler]].'),
    ]),
    ('echt', [
        A('Erkläre, woran du bei einem Link erkennst, zu welcher Webseite er wirklich führt.', 2, 'Entscheidend ist der Domainname direkt vor dem ersten „/“: Bei https://musterbank.de.konto-check.example/login ist es konto-check.example, nicht die Bank.'),
    ]),
    ('m1', [
        ZU('**M1:** Ordne die Malware zu.', ['Virus', 'Wurm', 'Trojaner', 'Spyware', 'Ransomware'],
           ['verschlüsselt Daten und fordert Lösegeld', 'tarnt sich als nützliches Programm', 'spioniert Daten aus', 'verbreitet sich selbstständig', 'infiziert Programme und Dateien'], loes=[5, 3, 4, 2, 1]),
    ]),
]),

'05_Creative_Commons': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Lege eine Tabelle an: Lizenz | teilen | bearbeiten | kommerziell.',
    sections=[
    ('urheber', [
        A('Begründe, ob ein Einverständnis nötig ist: (a) Foto deiner Freundin im Klassenchat, (b) Foto eines Fußballprofis im Spiel.', 2, '(a) Ja, Recht am eigenen Bild. (b) Nein, er ist eine Person der Zeitgeschichte bei einem öffentlichen Ereignis.'),
    ]),
    ('cc', [
        TAB('Was ist erlaubt?', ['Lizenz', 'teilen', 'bearbeiten', 'kommerziell nutzen'],
            [['CC BY', '[[ja]]', '[[ja]]', '[[ja]]'], ['CC BY-ND', '[[ja]]', '[[nein]]', '[[ja]]'], ['CC BY-NC', '[[ja]]', '[[ja]]', '[[nein]]'], ['CC0', '[[ja]]', '[[ja]]', '[[ja, ohne Namensnennung]]']], h=6),
    ]),
    ('m1', [
        RF(['r|Ein CC BY-Bild darf ich im Referat mit Namensnennung zeigen.', 'f|Ein CC BY-NC-Bild darf ein Shop für Werbung nutzen.|NC = nicht kommerziell.', 'f|Jedes Bild aus der Bildersuche ist frei verwendbar.|Die meisten Bilder sind urheberrechtlich geschützt.']),
    ]),
    ('quelle', [
        A('Schreibe eine vollständige Quellenangabe nach TULLU für ein Bild deiner Wahl.', 2, 'z. B. „Igel im Laub“ von M. Berg, CC BY-SA 4.0, Link zur Lizenz, gefunden auf bilder.example'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['DSGVO', 'Cookie', 'Netiquette', 'Phishing', 'CC0'],
           ['Verhaltensregeln im Netz', 'frei, ohne Bedingungen', 'Datenschutzgesetz der EU', 'Daten mit gefälschten Nachrichten abgreifen', 'kleiner Datensatz auf dem Gerät'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('t1', [
        A('**T1:** Nenne je eine Chance und ein Risiko der digitalen Transformation.', 1, 'Chance: effizientere, rohstoffsparende Produktion. Risiko: Wegfall von Arbeitsplätzen.'),
    ]),
    ('t2', [
        A('**T2:** Nenne vier personenbezogene Daten aus verschiedenen Kategorien.', 1, 'Name, IBAN, E-Mail-Adresse, Augenfarbe'),
    ]),
    ('t3', [
        A('**T3:** Nenne drei Warnzeichen einer Phishing-Mail.', 1, 'gefälschter Absender, Zeitdruck, Abfrage von PIN/Passwort, verdächtige Links, Sprachfehler'),
    ]),
    ('t4', [
        A('**T4:** Erkläre die Lizenz CC BY-NC-SA.', 2, 'Namensnennung Pflicht, keine kommerzielle Nutzung, Bearbeitungen müssen unter derselben Lizenz weitergegeben werden.'),
    ]),
]),
}
