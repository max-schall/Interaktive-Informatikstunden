from render import *

ALPHA_TPL = ('<table class="t" style="margin:2.5mm 3mm .5mm;width:auto;font-size:8pt"><tr><th>Klar</th>' + ''.join(f'<td style="width:5.6mm;text-align:center">{c}</td>' for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
             + '</tr><tr><th>Geheim</th>' + '<td style="height:6mm"></td>' * 26 + '</tr></table>')

WS = {
'01_Caesar': dict(skip=['uebungen'], heft_tpl=ALPHA_TPL,
    heft_hint='Trage das Geheimalphabet für den Schlüssel 3 ein. Schreibe dann die Merksätze ab.',
    sections=[
    ('begriffe', [
        L('Der Sender verwandelt den [[Klartext]] mit einem [[Schlüssel]] in einen [[Geheimtext]]. Werden Buchstaben umgestellt, spricht man von [[Transposition]], werden sie ersetzt, von [[Substitution]].'),
    ]),
    ('skytale', [
        A('Beschreibe, wie man mit einer Skytale ver- und entschlüsselt. Was ist der Schlüssel?', 2, 'Ein Streifen wird um einen Stab gewickelt und längs beschrieben. Abgewickelt ist der Text durcheinander. Nur mit einem Stab gleichen Umfangs kann man ihn lesen – der Umfang ist der Schlüssel.'),
    ]),
    ('caesar', [
        A('Beschreibe, wie mit der Caesar-Scheibe ein Klartext verschlüsselt wird.', 2, 'Die innere Scheibe wird um den Schlüssel gedreht. Zu jedem Buchstaben des Klartextes (außen) liest man den darunter liegenden Buchstaben (innen) ab.'),
    ]),
    ('werkzeug', [
        GL('Ver- oder entschlüssele mit Caesar.', ['HALLO, Schlüssel 3 → [[KDOOR]]', 'INFORMATIK, Schlüssel 5 → [[NSKTWRFYNP]]', 'FDHVDU, Schlüssel 3 → [[CAESAR]]']),
    ]),
    ('m1', [
        GL('**M1:** Entschlüssele die Botschaften.', ['YWJKKUZSPY XHMZQMTK, Schlüssel 5 → [[TREFFPUNKT SCHULHOF]]', 'LQIRUPDWLN LVW WROO, Schlüssel 3 → [[INFORMATIK IST TOLL]]']),
    ]),
]),

'02_Vigenere': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Verschlüssele „HALLO“ mit „KEY“ mit allen Zwischenschritten.',
    sections=[
    ('idee', [
        TAB('Verschlüssele HALLO mit dem Schlüsselwort KEY.', ['Klartext', 'H', 'A', 'L', 'L', 'O'],
            [['Schlüssel', 'K', 'E', 'Y', '[[K]]', '[[E]]'], ['Verschiebung', '10', '[[4]]', '[[24]]', '[[10]]', '[[4]]'], ['Geheimtext', '[[R]]', '[[E]]', '[[J]]', '[[V]]', '[[S]]']], h=6),
    ]),
    ('quadrat', [
        L('Im Vigenère-Quadrat sucht man oben den [[Klartextbuchstaben]] und links den [[Schlüsselbuchstaben]]. Im Kreuzungspunkt steht der [[Geheimtextbuchstabe]]. Weil viele Alphabete genutzt werden, ist es ein [[polyalphabetisches]] Verfahren.'),
    ]),
    ('werkzeug', [
        A('Erkläre, warum ein längeres Schlüsselwort die Vigenère-Verschlüsselung sicherer macht.', 2, 'Je länger das Schlüsselwort, desto mehr verschiedene Verschiebungen gibt es und desto seltener wiederholt sich das Muster. Häufigkeitsanalysen werden schwieriger.'),
    ]),
    ('otp', [
        A('Nenne die Bedingungen, unter denen das One-Time-Pad absolut sicher ist, und einen Nachteil.', 2, 'Der Schlüssel ist zufällig, mindestens so lang wie der Klartext und wird nur einmal verwendet. Nachteil: Für jede Nachricht muss ein neuer, gleich langer Schlüssel erzeugt und übergeben werden.'),
    ]),
    ('m1', [
        SORT('**M1:** Substitution oder Transposition?', ['Skytale', 'Caesar', 'Vigenère', 'Fleißnersche Schablone', 'One-Time-Pad'], ['Substitution', 'Transposition'], h=14,
             loes=[['Caesar', 'Vigenère', 'One-Time-Pad'], ['Skytale', 'Fleißnersche Schablone']]),
    ]),
]),

'03_Daten_verschluesseln': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne Lena → Server → Tom einmal Punkt-zu-Punkt, einmal Ende-zu-Ende und markiere den Klartext.',
    sections=[
    ('automatisch', [
        A('Nenne vier Beispiele für Daten, die verschlüsselt übertragen werden sollten, und woran du im Browser eine verschlüsselte Verbindung erkennst.', 2, 'Passwörter, Adresse, Telefonnummer, private Fotos, Bankdaten. Im Browser: https:// und das Schloss-Symbol.'),
    ]),
    ('wege', [
        TAB('Vergleiche die beiden Arten.', ['', 'Punkt-zu-Punkt', 'Ende-zu-Ende'],
            [['verschlüsselt zwischen …', '[[je zwei Stationen]]', '[[Sender und Empfänger]]'], ['Klartext auf dem Server?', '[[ja]]', '[[nein]]'], ['Sicherheit', '[[geringer]]', '[[höher]]']], h=7),
    ]),
    ('m1', [
        ZU('**M1:** Ordne zu (1 = Punkt-zu-Punkt, 2 = Ende-zu-Ende).', ['Punkt-zu-Punkt', 'Ende-zu-Ende'],
           ['Der E-Mail-Anbieter kann die Mails lesen.', 'Der Messenger-Anbieter sieht nur verschlüsselte Daten.', 'Nur das Handy des Empfängers hat den Schlüssel.', 'Jeder Server entschlüsselt und verschlüsselt neu.'], loes=[1, 2, 2, 1]),
    ]),
    ('kombi', [
        GL('Verschlüssele zweimal: erst Caesar mit Schlüssel 1, dann rückwärts lesen.', ['HALLO → Caesar: [[IBMMP]] → rückwärts: [[PMMBI]]']),
    ]),
]),

'04_Verschluesselungsarten': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Zeichne das Briefkasten-Modell mit öffentlichem und privatem Schlüssel.',
    sections=[
    ('sym', [
        A('Erkläre das Schlüsselverteilungsproblem der symmetrischen Verschlüsselung.', 2, 'Sender und Empfänger brauchen denselben Schlüssel. Er muss übertragen werden; fängt ihn jemand ab, kann er alle Nachrichten entschlüsseln.'),
    ]),
    ('asym', [
        L('Bei der asymmetrischen Verschlüsselung hat der Empfänger ein Schlüsselpaar. Mit dem [[öffentlichen]] Schlüssel wird verschlüsselt, nur mit dem [[privaten]] Schlüssel kann entschlüsselt werden. Der private Schlüssel bleibt immer beim [[Empfänger]].'),
    ]),
    ('hybrid', [
        A('Beschreibe in Stichpunkten, wie die hybride Verschlüsselung funktioniert.', 3, 'Zufälligen Session-Key wählen · Nachricht damit symmetrisch verschlüsseln · Session-Key mit dem öffentlichen Schlüssel des Empfängers verschlüsseln · beides senden · Empfänger entschlüsselt Session-Key mit privatem Schlüssel und damit die Nachricht.'),
    ]),
    ('m1', [
        SORT('**M1:** Symmetrisch oder asymmetrisch?', ['ein gemeinsamer Schlüssel', 'sehr schnell', 'Caesar', 'öffentlicher Schlüssel', 'Briefkasten-Modell', 'kein geheimer Schlüsselaustausch'], ['symmetrisch', 'asymmetrisch'], h=14,
             loes=[['ein gemeinsamer Schlüssel', 'sehr schnell', 'Caesar'], ['öffentlicher Schlüssel', 'Briefkasten-Modell', 'kein geheimer Austausch']]),
    ]),
]),

'05_Kryptoanalyse': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab. Knacke das Geheimwort IVHFIIVKIPII und notiere dein Vorgehen.',
    sections=[
    ('kryptologie', [
        L('Die Kryptologie besteht aus der [[Kryptografie]], die sichere Verfahren entwickelt, und der [[Kryptoanalyse]], die Verschlüsselungen ohne Schlüssel knackt.'),
    ]),
    ('haeufigkeit', [
        A('Im Caesar-Geheimtext ist der Buchstabe X am häufigsten. Bestimme den wahrscheinlichen Schlüssel und begründe.', 2, 'X steht vermutlich für E, den häufigsten Buchstaben im Deutschen. Von E nach X sind es 19 Stellen → Schlüssel 19.'),
    ]),
    ('brute', [
        A('Beschreibe den Ablauf einer Brute-Force-Attacke auf eine Caesar-Verschlüsselung.', 2, 'Der Geheimtext wird nacheinander mit allen 25 Schlüsseln entschlüsselt. Der Schlüssel, der einen sinnvollen Text ergibt, ist der richtige.'),
    ]),
    ('schutz', [
        A('Begründe, warum längere Passwörter besser vor Brute-Force-Angriffen schützen.', 2, 'Mit jedem zusätzlichen Zeichen vervielfacht sich die Zahl der Möglichkeiten (z. B. ×26 bei Kleinbuchstaben). Das Ausprobieren dauert dann viel zu lange.'),
    ]),
    ('m1', [
        GL('**M1:** Knacke die Geheimwörter (Caesar, Schlüssel unbekannt).', ['HUGEHHUH → [[ERDBEERE]] (Schlüssel [[3]])', 'NSKTWRFYNP → [[INFORMATIK]] (Schlüssel [[5]])']),
    ]),
]),

'06_Kuerzester_Weg': dict(skip=['uebungen'],
    heft_hint='Schreibe die Merksätze ab und lege die Dijkstra-Tabelle für den Graphen aus Station 3 an.',
    sections=[
    ('graph', [
        L('Ein Straßennetz wird als [[Graph]] dargestellt. Kreuzungen sind [[Knoten]], Straßen sind [[Kanten]]. Jede Kante hat [[Kosten]], z. B. die Länge.'),
    ]),
    ('brute', [
        A('Begründe, warum die Brute-Force-Methode für ein Navigationsgerät ungeeignet ist.', 2, 'In großen Straßennetzen gibt es unvorstellbar viele Wege. Alle durchzurechnen würde viel zu lange dauern.'),
    ]),
    ('dijkstra', [
        TAB('Führe Dijkstra durch (S–A 20, S–C 10, C–A 30, C–B 50, A–B 20, A–D 50, B–D 20, B–Z 40, D–Z 10).', ['Knoten', 'S', 'A', 'B', 'C', 'D', 'Z'],
            [['Kosten', '0', '[[20]]', '[[40]]', '[[10]]', '[[60]]', '[[70]]'], ['Vorgänger', '–', '[[S]]', '[[A]]', '[[S]]', '[[B]]', '[[D]]']], h=6),
        GL('Kürzester Weg von S nach Z:', ['[[S → A → B → D → Z]] mit Kosten [[70]]']),
    ]),
    ('m1', [
        BOX('**M1:** Zeichne einen eigenen Graphen mit 5 Knoten und Kantenwerten. Lass deinen Nachbarn den kürzesten Weg bestimmen.', 34),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, skip=['quiz-st'], heft_label='Notizen', heft_title='Das muss ich noch üben', heft_sub='Fragen, Merkpunkte, Begriffe',
    sections=[
    ('begriffe', [
        ZU('Ordne die Fachbegriffe den Erklärungen zu.', ['Transposition', 'Substitution', 'Ende-zu-Ende', 'privater Schlüssel', 'Brute Force'],
           ['alle Schlüssel ausprobieren', 'Buchstaben werden ersetzt', 'Buchstaben werden umgestellt', 'nur Sender und Empfänger können lesen', 'entschlüsselt, bleibt geheim'], loes=[5, 2, 1, 3, 4]),
    ]),
    ('t1', [
        GL('**T1:** Entschlüssele.', ['Caesar, Schlüssel 4: XVIJJIR → [[TREFFEN]]', 'Vigenère, Schlüsselwort AB: GFHFIN → [[GEHEIM]]']),
    ]),
    ('t2', [
        A('**T2:** Erkläre, warum bei Public Key kein geheimer Schlüssel übertragen werden muss.', 2, 'Verschlüsselt wird mit dem öffentlichen Schlüssel, den jeder haben darf. Entschlüsseln kann nur der private Schlüssel, der den Empfänger nie verlässt.'),
    ]),
    ('t3', [
        A('**T3:** Beschreibe, wie du einen langen Caesar-Geheimtext ohne Schlüssel knackst.', 2, 'Buchstaben zählen, der häufigste steht vermutlich für E. Der Abstand ergibt den Schlüssel. Alternativ alle 25 Schlüssel ausprobieren.'),
    ]),
    ('t4', [
        A('**T4:** Nenne die Schritte des Algorithmus von Dijkstra.', 2, 'Start 0, Rest ∞ · unbesuchten Knoten mit geringsten Kosten wählen · Nachbarkosten aktualisieren, Vorgänger notieren · als besucht markieren · wiederholen · Weg rückwärts ablesen.'),
    ]),
]),
}
