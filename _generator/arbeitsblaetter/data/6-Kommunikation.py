from render import *

WS = {
'01_Digitale_Kommunikation': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne das Sender-Empfänger-Modell mit einem eigenen Beispiel.',
    sections=[
    ('auftakt', [
        A('**A:** Beschreibe, was problematisch sein kann, wenn man abends im Bett das Smartphone nutzt.', 1, 'Man schläft schlechter, ist am nächsten Tag müde und verliert das Gefühl für die Zeit.'),
    ]),
    ('modell', [
        L('Bei der Kommunikation übermittelt ein [[Sender]] über einen [[Kanal]] Informationen an einen [[Empfänger]]. Der Sender [[codiert]] die Information, der Empfänger [[decodiert]] sie.'),
    ]),
    ('kanaele', [
        SORT('Ordne die Beispiele den Kommunikationskanälen zu.', ['Telefonat', 'Lächeln', 'Verkehrsschild', 'Textnachricht', 'Schulterzucken', 'Emoji'], ['verbal', 'nonverbal', 'visuell'],
             loes=[['Telefonat', 'Textnachricht'], ['Lächeln', 'Schulterzucken'], ['Verkehrsschild', 'Emoji']]),
    ]),
    ('m1', [
        A('Erkläre den Unterschied zwischen Ein-Weg- und Zwei-Wege-Kommunikation an je einem Beispiel.', 2, 'Ein-Weg: Nur einer sendet, der Empfänger kann nicht antworten, z. B. Musik hören, Werbeplakat. // Zwei-Wege: Beide senden und empfangen, z. B. Chat, Videokonferenz.'),
    ]),
    ('m2', [
        TAB('**M2** Direkt oder verzögert? Ein-Weg oder Zwei-Wege?', ['Medium', 'direkt / verzögert', 'Ein-Weg / Zwei-Wege'],
            [['Radio', 'direkt', 'Ein-Weg'], ['E-Mail', '[[verzögert]]', '[[Zwei-Wege]]'], ['Videochat', '[[direkt]]', '[[Zwei-Wege]]'], ['Sprachnachricht', '[[verzögert]]', '[[Zwei-Wege]]'], ['Forumsbeitrag', '[[verzögert]]', '[[Zwei-Wege]]']], h=6.5, widths=[30, 35, 35]),
    ]),
]),

'02_Mediennutzung': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Notiere deine Medienzeit von gestern und vergleiche sie mit der Empfehlung.',
    sections=[
    ('regeln', [
        TAB('Empfehlungen für Freizeit-Medien', ['Alter', 'Empfehlung pro Tag'], [['bis 10 Jahre', '[[30–60 Minuten]]'], ['11 bis 13 Jahre', '[[60–90 Minuten]]'], ['ab 14 Jahren', '[[bis zu 2 Stunden]]']], h=7, widths=[35, 65]),
    ]),
    ('pruefen', [
        A('**A:** Notiere drei Regeln zur Mediennutzung, die es bei dir zu Hause gibt (oder geben könnte).', 3, 'z. B. kein Handy beim Essen // Handy ab 20 Uhr im Flur // erst Hausaufgaben, dann Medien'),
    ]),
    ('m1', [
        A('**M1:** Welche Geräte und Medien nutzen 12- bis 19-Jährige am häufigsten täglich, welche am seltensten?', 2, 'Am häufigsten: Smartphone (98 %), Internet (96 %), Musik hören (94 %). Am seltensten: Podcasts hören (26 %).'),
    ]),
    ('m2', [
        BOX('**M2:** Erstelle dein Medientagebuch für einen Tag (Uhrzeit – Tätigkeit – Gerät).', 45, loes='individuell; z. B. 7 Uhr chatten (Smartphone), 15 Uhr Video streamen (Tablet) …'),
    ]),
]),

'03_E_Mails': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und schreibe eine kurze formelle E-Mail an deine Lehrkraft.',
    sections=[
    ('adresse', [
        GL('Zerlege die E-Mail-Adresse max.mustermann@westermann.de.', ['Benutzername: [[max.mustermann]]', 'Zeichen: [[@]]', 'Domain: [[westermann.de]]']),
    ]),
    ('aufbau', [
        ZU('**M1** Ordne die Teile einer E-Mail zu.', ['Betreff', 'Anrede', 'Hauptteil', 'Schlussformel'],
           ['Sehr geehrte Frau Müller,', 'Mit freundlichen Grüßen', 'Termin Besprechung Referat', 'Sind Sie nächste Woche verfügbar?'], loes=[2, 4, 1, 3]),
    ]),
    ('cc', [
        L('Bei [[cc]] sehen alle Empfänger, wer die E-Mail bekommt. Bei [[bcc]] (Blindkopie) bleiben die Empfänger geheim. Eine Datei verschickt man als [[Anhang]].'),
    ]),
    ('werkstatt', [
        A('**M1 Aufgabe 3–4:** Warum ist die E-Mail „Hey, wir haben uns ewig nicht gesehen …“ nicht für die Schulleitung geeignet? Warum sollte der Benutzername kein lustiger Name sein?', 2, 'Die Anrede ist zu locker, es fehlen Sie-Form, Betreff und höfliche Schlussformel. // Ein lustiger Benutzername wirkt bei Schule, Vereinen oder Bewerbungen unseriös.'),
    ]),
]),

'04_Chatten': dict(skip=['uebungen', 'unbekannt'],
    heft_hint='Schreibe die Merksätze ab und notiere die fünf Hinweise für das Chatten mit je einem Beispiel.',
    sections=[
    ('messenger', [
        ZU('**M1** Ordne die Emojis den Gefühlen zu.', ['😢', '😱', '😎', '😡', '😘'], ['wütend', 'cool', 'traurig', 'liebevoll', 'schockiert'], loes=[4, 3, 1, 5, 2]),
    ]),
    ('regeln', [
        TAB('Hinweise für das Chatten', ['Hinweis', 'Beispiel'],
            [['Verrate nichts!', '[[neutraler Benutzername, keine echten Daten]]'], ['Sei vorsichtig!', '[[keine Freundschaftsanfragen oder Links von Fremden]]'], ['Sei immer fair!', '[[keine Bilder anderer ohne Erlaubnis hochladen]]'], ['Mobbe niemanden!', '[[Störer melden, nicht mitmachen]]']], h=7, widths=[30, 70]),
    ]),
    ('m2', [
        A('**M2 Aufgabe 2:** Beschreibe an einem Beispiel, dass die Wahl der Emojis die Stimmung einer Nachricht verändert.', 2, '„Du hast mein Rad schon wieder ausgeliehen 😊“ wirkt freundlich, mit 😡 wirkt der gleiche Satz wütend.'),
    ]),
]),

'05_Posten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und schreibe eine Checkliste: Bevor ich poste …',
    sections=[
    ('regeln', [
        TAB('Was sollte man beim Posten beachten?', ['Regel', 'Bedeutung'],
            [['Urheberrecht', '[[nur eigene Fotos posten, fremde nur mit Erlaubnis]]'], ['Persönlichkeitsrecht', '[[abgebildete Personen um Erlaubnis fragen]]'], ['DSGVO', '[[keine persönlichen Daten wie Adresse oder Kennzeichen]]']], h=7, widths=[30, 70]),
    ]),
    ('check', [
        A('Nenne vier Dinge, die auf einem Foto nicht zu sehen sein sollten, bevor du es postest.', 2, 'Hausnummer oder Adresse, Autokennzeichen, Live-Standort, fremde Personen ohne Erlaubnis, Hinweise wie „niemand zu Hause“.'),
    ]),
    ('m1', [
        A('**M1:** Lea möchte die Lagerfeuer-Bilder posten und nur die Accounts markieren. Gib ihr einen Rat.', 2, 'Markieren reicht nicht: Alle gut erkennbaren Personen müssen vorher zustimmen. Das Nummernschild muss verpixelt werden.'),
    ]),
]),

'06_Passwoerter': dict(skip=['uebungen', 'zwei'],
    heft_hint='Schreibe die Merksätze ab und erkläre die Satzmethode an einem ausgedachten Beispielsatz.',
    sections=[
    ('datenklau', [
        L('Beim [[Phishing]] versuchen Kriminelle, mit gefälschten [[E-Mails]] oder Nachrichten an persönliche Daten zu kommen. Die Nachricht enthält einen [[Link]] zu einer gefälschten Webseite.'),
    ]),
    ('passwort', [
        TAB('**M1** Bewerte die Passwörter.', ['Passwort', 'sicher?', 'Begründung'],
            [['qwertzuiop', '[[nein]]', '[[Tastaturmuster]]'], ['FCSchalke04', '[[nein]]', '[[Verein, zu kurz, keine Sonderzeichen]]'], ['29smjMdoSj_#1asS', '[[ja]]', '[[lang, gemischt, ohne Wörter]]'], ['passwort', '[[nein]]', '[[einfaches Wort]]']], h=6.5, widths=[32, 16, 52]),
    ]),
    ('satz', [
        GL('Bilde ein Passwort mit der Satzmethode.', ['Mein Hund Bello frisst jeden Morgen 2 Brötchen & 1 Ei! → [[MHBfjM2B&1E!]]']),
    ]),
    ('m2', [
        A('**M2:** Nenne drei Hinweise, dass die E-Mail von „hades-versand.com“ eine Phishing-Mail ist.', 2, 'unbekannter Absender, unpersönliche Anrede „Sehr geehrter Kunde“, Druck durch ein wartendes Paket, Link zu fremder Adresse, Grammatikfehler'),
    ]),
]),

'07_Werbung': dict(skip=['uebungen', 'feed'],
    heft_hint='Schreibe die Merksätze ab und beschreibe eine Werbung, die dir aufgefallen ist (Botschaft – Zielgruppe – Trick).',
    sections=[
    ('zweck', [
        L('Werbung möchte Menschen auf etwas [[aufmerksam]] machen und vom [[Kauf]] überzeugen. Sie ist [[visuelle]] Kommunikation mit Bildern, Farben und kurzen Texten.'),
    ]),
    ('m1', [
        A('**M1:** Nenne fünf verschiedene Werbemaßnahmen in einer Einkaufsstraße und drei im Internet.', 3, 'Straße: Ladenschilder, Plakate an der Litfaßsäule, Werbung auf dem Bus, Aufsteller, Schaufenster. // Internet: gesponserte Posts, Werbung vor Videos, Influencer-Werbung, Pop-ups.'),
    ]),
    ('m2', [
        A('**M2:** Was ist ein Klischee? Nenne ein Beispiel aus der Werbung.', 2, 'Eine feste Vorstellung über Menschen, die nicht der Wirklichkeit entspricht. Beispiel: Frauen beim Putzen, starke Männer in Autowerbung.'),
    ]),
]),

'08_Datenschutz': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und notiere, welche Apps auf deinem Smartphone auf den Standort zugreifen dürfen.',
    sections=[
    ('daten', [
        ZU('Ordne die Beispiele den Datenarten zu.', ['Bankdaten', 'Onlinedaten', 'Physische Merkmale', 'Allgemeine Personendaten'], ['IP-Adresse', 'Name und Geburtsdatum', 'Kontonummer', 'Augenfarbe'], loes=[2, 4, 1, 3]),
    ]),
    ('dsgvo', [
        L('Die [[Datenschutzgrundverordnung]] (DSGVO) regelt den Umgang mit Daten in der EU. Unternehmen brauchen eine [[Zustimmung]]. Am besten ist man [[datensparsam]].'),
    ]),
    ('inkognito', [
        RF(['r|Der Inkognito-Modus speichert keinen Verlauf auf dem Gerät.', 'f|Im Inkognito-Modus ist man im Internet unsichtbar.|Webseiten und Anbieter können trotzdem sehen, was aufgerufen wird.', 'r|Anhänge von Unbekannten sollte man nicht öffnen.']),
    ]),
    ('m1', [
        A('**M1:** Welches von Amfiras Bildern (Selfie vor Kirche, Geburtstagskarte mit Adresse und Ticket, Baum) würdest du posten? Begründe.', 2, 'Den Baum: Er zeigt keine persönlichen Daten. Auf der Karte sind Name, Adresse und der Ticket-Code zu sehen; beim Selfie verrät der Ort, wo sie ist.'),
    ]),
    ('m2', [
        A('**M2:** Welche Berechtigungen braucht eine Shopping-App wirklich? Begründe.', 2, 'Nur den Netzwerkzugriff, um zu bestellen. Kontakte, Mikrofon, Standort, Anrufe oder Bildergalerie sind nicht nötig.'),
    ]),
]),

'09_Gefahren': dict(skip=['uebungen', 'chancen'],
    heft_hint='Schreibe die Merksätze ab und notiere Hilfsangebote: Vertrauensperson, Nummer gegen Kummer 116 111, juuuport.de.',
    sections=[
    ('grooming', [
        A('Was ist Cyber-Grooming? Nenne zwei Warnsignale.', 2, 'Erwachsene erschleichen sich im Internet das Vertrauen von Kindern, um sie zu missbrauchen. // Warnsignale: fragt nach Fotos oder Webcam, will sich treffen, soll geheim bleiben.'),
    ]),
    ('schad', [
        L('Schadprogramme wie [[Würmer]] oder [[Trojaner]] verstecken sich in Anhängen und hinter [[Links]]. Sie stehlen unbemerkt [[Daten]].'),
    ]),
    ('mobbing', [
        A('Was kannst du tun, wenn in deiner Klassengruppe jemand gemobbt wird?', 2, 'nicht mitmachen, zum Betroffenen halten, Screenshots machen, Nachrichten melden, mit Eltern oder Vertrauenslehrkraft sprechen'),
    ]),
    ('m1', [
        GL('**M1** Berechne die Kosten des Probeabos (ab dem 4. Monat 16,99 € pro Monat).', ['nach 6 Monaten: 3 · 16,99 € = [[50,97 €]]', 'nach 12 Monaten: 9 · 16,99 € = [[152,91 €]]']),
    ]),
]),

'10_Fake_News': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und die vier Punkte der Checkliste „Gib Fake News keine Chance!“.',
    sections=[
    ('fake', [
        A('Was sind Fake News, und warum werden sie verbreitet?', 2, 'Absichtlich falsche Nachrichten, Bilder oder Videos. Sie sollen Menschen beeinflussen oder täuschen oder bringen Aufmerksamkeit und Geld durch Werbung.'),
    ]),
    ('check', [
        TAB('**M1** Checkliste', ['Prüfpunkt', 'Frage'],
            [['Hinterfrage die Nachricht!', '[[Woher kommt sie? Welche Absicht?]]'], ['Überprüfe den Ursprung!', '[[Gibt es eine Quelle? Bestätigen andere?]]'], ['Überprüfe das Bild!', '[[Wer hat es wann und wo aufgenommen?]]'], ['Leite nicht einfach weiter!', '[[Kann es anderen schaden? Melden!]]']], h=7, widths=[36, 64]),
    ]),
    ('verstoerend', [
        A('**M1 (S. 133):** Leander bekommt das Video nicht mehr aus dem Kopf. Was kann er tun?', 2, 'mit Eltern oder einer Vertrauensperson sprechen, das Video melden, bei klicksafe.de oder jugend.support Hilfe suchen; nächstes Mal „Nein“ sagen'),
    ]),
]),

'11_Netzwerke': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne dein Heimnetzwerk mit Router, Modem und vier Geräten.',
    sections=[
    ('lokal', [
        L('Geräte am gleichen Ort bilden ein [[lokales]] Netzwerk (LAN, per Funk [[WLAN]]). Im Mittelpunkt steht der [[Router]]. Er verbindet über den [[Provider]] mit dem Internet.'),
    ]),
    ('global', [
        SORT('Ordne den Schichten des Internets zu.', ['E-Mail', 'Server', 'Website', 'Kabel', 'Streaming', 'Router'], ['Internetdienste', 'Technische Schicht'], loes=[['E-Mail', 'Website', 'Streaming'], ['Server', 'Kabel', 'Router']]),
    ]),
    ('dns', [
        A('Was ist eine IP-Adresse, und wozu dient das DNS?', 2, 'Die IP-Adresse ist die „Anschrift“ eines Geräts im Internet. Das DNS ist wie ein Telefonbuch: Es übersetzt Webadressen in IP-Adressen.'),
    ]),
    ('m2', [
        A('**M2:** Warum werden beim Aufrufen einer Webseite manche Router nicht genutzt?', 1, 'Die Daten nehmen den schnellsten Weg; andere Router liegen auf Umwegen. Fällt ein Router aus, wird ein anderer Weg genommen.'),
    ]),
]),

'12_KI': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und zeichne eine Zeitleiste der KI mit vier Meilensteinen.',
    sections=[
    ('ki', [
        A('Was ist künstliche Intelligenz? Nenne drei Beispiele aus dem Alltag.', 2, 'Maschinen lösen Aufgaben selbst; sie werden mit Daten trainiert. Beispiele: Sprachassistent, Übersetzung, Saugroboter, Websuche.'),
    ]),
    ('m1', [
        ZU('**M1** Ordne die Stufen zu.', ['assistiertes Fahren', 'automatisiertes Fahren', 'autonomes Fahren'], ['Das Auto fährt ganz ohne Fahrer.', 'Ein Tempomat hält die Geschwindigkeit.', 'Der Fahrer gibt Aufgaben zeitweise ab.'], loes=[3, 1, 2]),
    ]),
    ('stark', [
        TAB('Starke und schwache KI', ['', 'schwache KI', 'starke KI'], [['Was kann sie?', '[[festgelegte Aufgaben, z. B. Übersetzen]]', '[[selbstständig lernen, kreativ denken]]'], ['Gibt es sie?', '[[ja, im Alltag]]', '[[nein, nur Theorie]]']], h=7, widths=[22, 39, 39]),
    ]),
    ('filme', [
        A('Nenne die drei Kategorien von KI in Filmen.', 1, 'die gefährliche KI, die friedliche KI, die empfindungsfähige KI'),
    ]),
    ('zeit', [
        GL('Ergänze die Zeitleiste.', ['1936: [[Turingmaschine]]', '1997: [[Deep Blue schlägt den Schachweltmeister]]', '2011: [[KI erreicht den Alltag (Sprachassistenten)]]']),
    ]),
]),

'13_Generative_KI': dict(skip=['uebungen', 'chancen'],
    heft_hint='Schreibe die Merksätze ab und notiere einen guten Prompt für eine Fantasiegeschichte.',
    sections=[
    ('generativ', [
        L('Generative KI [[erzeugt]] Texte, Bilder, Musik oder Videos. Für Texte nutzt man ein [[Large Language Model]] (LLM). Die Eingabe heißt [[Prompt]].'),
    ]),
    ('llm', [
        A('Beschreibe, wie ein LLM den Satz „Es war einmal eine …“ fortsetzt.', 2, 'Es berechnet aus gelernten Textzusammenhängen Wahrscheinlichkeiten für das nächste Wort, z. B. Prinzessin 50 %, Königstochter 35 %, und wählt ein wahrscheinliches Wort.'),
    ]),
    ('prompt', [
        A('**M1 Aufgabe 2:** Verbessere den Prompt „Schreibe etwas über Sport!“.', 2, 'z. B.: Du bist Sportreporterin einer Schülerzeitung. Schreibe einen Bericht (80 Wörter) über das Fußballturnier unserer Schule für Schülerinnen und Schüler der Klasse 5.'),
    ]),
    ('bilder', [
        A('**M2:** Nenne drei Merkmale, an denen man KI-Bilder erkennen kann.', 1, 'verzerrte Hände, fehlerhafte Schrift, unlogische Objekte, ungleichmäßige Merkmale'),
    ]),
    ('deepfakes', [
        A('Was ist ein Deepfake? Nenne eine Gefahr.', 2, 'Eine mit KI erstellte, täuschend echte Fälschung eines Bildes, Videos oder einer Stimme. Gefahr: falsche Nachrichten von Politikern, Mobbing, Betrug mit falscher Identität.'),
    ]),
]),

'14_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe zu.', ['Phishing', 'DNS', 'Prompt', 'Cyber-Mobbing', 'Deepfake'],
           ['Eingabe für eine KI', 'täuschend echte KI-Fälschung', 'Telefonbuch des Internets', 'Daten-Angeln mit gefälschten Nachrichten', 'Beleidigen im Internet'], loes=[3, 5, 2, 1, 4]),
    ]),
    ('t1', [
        A('Vergleiche direkte und verzögerte Kommunikation an je einem Beispiel.', 1, 'Direkt in Echtzeit, z. B. Videoanruf; verzögert zeitversetzt, z. B. E-Mail.'),
    ]),
    ('t2', [
        A('Beschreibe den Aufbau einer E-Mail-Adresse.', 1, 'Benutzername @ Domain, z. B. max.mustermann@westermann.de'),
    ]),
    ('t3', [
        A('Nenne die zwei Schichten des Internets mit je zwei Beispielen.', 1, 'Technische Schicht: Router, Server, Kabel. Internetdienste: E-Mail, Webseiten, Streaming.'),
    ]),
    ('t4', [
        A('Nenne zwei Eigenschaften eines präzisen Prompts und ein Risiko generativer KI.', 1, 'klare Anweisung, Antwortlänge, Rolle, Beispiele; Risiko: falsche Informationen, Fake News, Deepfakes.'),
    ]),
]),
}
