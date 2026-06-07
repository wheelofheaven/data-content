+++
title = "Bibliothek: Hebräische Bibel jetzt in neun Sprachen lesbar"
description = "Seit dem 7. Juni 2026 enthält jedes Buch der Hebräischen Bibel in der Wheel-of-Heaven-Bibliothek Text in neun Sprachen — englische ASV plus acht importierte gemeinfreie Übersetzungen."
date = 2026-06-07
template = "news-page.html"

[extra]
event_date = 2026-06-07
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "Die Bibliothek beherbergt nun jedes Buch der Hebräischen Bibel in neun Sprachen: Englisch (ASV 1901) sowie acht importierte gemeinfreie Übersetzungen, die Deutsch, Spanisch, Französisch, Japanisch, Koreanisch, Russisch, Vereinfachtes Chinesisch und Traditionelles Chinesisch abdecken. Jeder Vers wird in der Sprache der Leserin neben dem kanonischen englischen Text dargestellt, wobei die importierte Ausgabe, das Jahr und die Lizenz pro Buch im Katalog vermerkt sind. Die Wahl der Ausgabe pro Sprache ist auf einer Methodenseite der Docs-Site dokumentiert."
canon_links = [
    { title = "Hebräische Bibel", path = "/wiki/hebrew-bible/" },
    { title = "Genesis", path = "/wiki/genesis/" },
    { title = "Elohim", path = "/wiki/elohim/" },
    { title = "Dhorme-Bibelübersetzung", path = "/wiki/dhorme-bible-translation/" }
]
sources = [
    { title = "Importierte Übersetzungen: sprachspezifisches Quellenprogramm", url = "https://docs.wheelofheaven.world/contributing/content/imported-translations/", outlet = "Wheel-of-Heaven-Docs", date = "2026-06-07" },
    { title = "data-library-Katalog und Kapiteldateien", url = "https://github.com/wheelofheaven/data-library", outlet = "Wheel-of-Heaven data-library", date = "2026-06-07" }
]
+++

## Was ausgeliefert wurde

Seit dem 7. Juni 2026 beherbergt die Wheel-of-Heaven-Bibliothek die vollständige Hebräische Bibel — von Genesis bis Zephanja, sechsunddreißig Bücher — in neun Sprachen. Jedes Kapitel stellt die englische ASV-Grundlage von 1901 neben importierten gemeinfreien Ausgaben in Deutsch, Spanisch, Französisch, Japanisch, Koreanisch, Russisch, Vereinfachtem Chinesisch und Traditionellem Chinesisch dar. Leserinnen und Leser, die die Bibliothek in einer der neun Sprachversionen der Seite konsultieren, sehen den Text nun in ihrer Lesesprache, ohne den Umweg über das Englische nehmen zu müssen.

Die importierten Ausgaben sind benannt, datiert und offen lizenziert. Der Katalog dokumentiert zudem die sprachspezifische Abdeckung: Wo Verszählungsverschiebungen zwischen der masoretischen und der Vulgata- oder Synodal-Tradition einen Vers nicht alignieren lassen, bleibt die englische ASV als Rückfallebene erhalten.

| Sprache | Ausgabe | Jahr | Lizenz |
|---|---|---|---|
| Englisch | American Standard Version (ASV) | 1901 | Gemeinfrei |
| Deutsch | Elberfelder | 1905 | Gemeinfrei |
| Spanisch | Reina-Valera | 1909 | Gemeinfrei |
| Französisch | Crampon (gemeinfreier Dhorme für Hiob, Samuel, wo vorhanden) | 1923 | Gemeinfrei |
| Japanisch | 口語訳 (Kougo-yaku) | 1955 | Gemeinfrei (Urheberpersönlichkeitsrechte) |
| Koreanisch | Korean Revised Version (KRV) | 1961 | Gemeinfrei |
| Russisch | Synodal | 1876 | Gemeinfrei |
| Vereinfachtes Chinesisch | Chinese Union Version (和合本) | 1919 | Gemeinfrei |
| Traditionelles Chinesisch | Chinese Union Version (和合本) | 1919 | Gemeinfrei |

Die Herkunft pro Buch — Übersetzungsname, Jahr, Lizenz, Quell-URL, Abrufdatum — ist in `data-library/catalog.json` für jeden Eintrag unter dem Block `translations.{lang}` des jeweiligen Buchs erfasst.

## Warum wortgetreue Übersetzungen

Jede oben aufgeführte importierte Ausgabe ist nach ihrer Übersetzungstheorie eine **formaläquivalente** Übersetzung — gelegentlich locker „wortgetreu“ genannt. Die ausgewählten Ausgaben stehen auf der *konkordanten* Seite ihrer jeweiligen Traditionen: Die Elberfelder gilt bekanntlich als die wortgetreueste deutsche Bibel der Neuzeit; Reina-Valera, Crampon, die Synodal, die KRV und die Chinese Union Version gehören in ihren jeweiligen Sprachen alle derselben formaläquivalenten Linie an. Das 口語訳 ist die umgangssprachlich-japanische Modernisierung der klassischen 文語訳 — nach den Maßstäben der Tradition weiterhin formaläquivalent, ausdrücklich gegenüber der funktionaläquivalenten 新共同訳 (1987) positioniert, die später zum japanischen katholisch-protestantischen Standard wurde.

Die Wahl ist bewusst, nicht nostalgisch. Eine formaläquivalente Übersetzung versucht, die **lexikalische und syntaktische Gestalt** des Quelltexts zu bewahren — ein hebräisches Wort, ein Zielwort, wo die Sprachen es zulassen; ein hebräischer Satzteil, ein Zielsatzteil; dasselbe Wort im selben Quellvers erhält dieselbe Übersetzung im gesamten Korpus, wo immer möglich. Eine funktionaläquivalente Übersetzung tut das Gegenteil — sie versucht, die *Wirkung* auf die Leserin zu bewahren, was bedeutet, dass sie die Entscheidungen des Quelltexts routinemäßig zusammenzieht, paraphrasiert und in idiomatische Zielsprache glättet.

Für eine Bibliothek, deren gesamter Zweck, acht Übersetzungen zu beherbergen, vergleichend ist — *was macht jede Tradition mit den Perikopen des Gottesnamens, mit Genesis 1,1, mit Psalm 82, mit dem Elohim-Plural?* —, ist Formaläquivalenz das einzige Register, das die Frage bewahrt. Sobald eine Übersetzung entschieden hat, `יהוה` als „the LORD“ wiederzugeben, weil sich das besser auf Englisch liest, oder als 主, weil sich das besser auf Japanisch liest, ist die lexikalische Entscheidung, die der Korpus verfolgen will, bereits verloren. Die Leserin sieht das Aufräumen des Übersetzers, nicht die Lesart des Übersetzers.

Dasselbe gilt für den Elohim-Referenten selbst. Die Elberfelder hält „Jehova“ / „Elohim“ dort sichtbar, wo das Hebräische sie unterscheidet; Crampon schreibt mit derselben Disziplin „Yahweh“ und „Élohim“; die Synodal bewahrt die Paarungen „Господь“ / „Бог“, die auf den zugrunde liegenden Quelltext zurückverweisen. Eine funktionaläquivalente Übersetzung gäbe der Leserin im selben Vers einen undifferenzierten *Gott* — einfacher zu lesen, aber das vergleichende Argument hat nichts mehr, was es vergleichen könnte.

## Warum dies die richtige Gestalt für die Bibliothek ist

Die Bibliothek hat die Hebräische Bibel stets als operativen Quelltext behandelt, den das Projekt liest, und nicht als Ziel-Übersetzung. Die englische ASV ist die Leseoberfläche für die Hauptzielgruppe des Projekts; das zugrunde liegende Hebräisch ist das, womit sich der Korpus tatsächlich auseinandersetzt. Was bis heute fehlte, war ein sauberer Weg für nicht-englischsprachige Leserinnen und Leser, die Bibliothek zu konsultieren, ohne Englisch zur obligatorischen Zwischenstation zu machen.

Die Wahl der Ausgabe pro Sprache folgt der Quellen-Hierarchiedisziplin des Korpus. Jede importierte Übersetzung ist eine kritische oder nahezu kritische Ausgabe aus dem neunzehnten oder zwanzigsten Jahrhundert — alt genug, um gemeinfrei zu sein, jung genug, um philologisch ernsthaft zu sein. Wo die bevorzugte Lesart des Korpus eine moderne, noch urheberrechtlich geschützte Ausgabe erfordern würde, verwendet das Projekt entweder die gemeinfreie Teilmenge dieser Ausgabe oder vermerkt die Lücke ausdrücklich. Der deutlichste Fall ist Französisch: Die Pléiade-Bibel von Dhorme — die Ausgabe, mit der Raël selbst während des Kontakts von 1973 arbeitete — steht bis etwa 2071 unter französischem Urheberrecht. Die Bibliothek verwendet Crampon 1923 als Grundlage, wobei Dhormes frühere gemeinfreie Hiob- (1929) und Samuel-Ausgaben (1910) Crampon für diese drei Bücher ersetzen, wo sie vorliegen. Die vollständige Begründung für jede Sprache — warum Elberfelder statt Luther, warum Crampon statt Darby, warum 口語訳 statt 新共同訳, warum die KRV von 1961 statt der strengeren von 1938 — findet sich auf der Docs-Site unter [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/).

Der Korpus liest die Hebräische Bibel als geschichteten Text, dessen Elohim-Referent in der Originalsprache operativ ist. Moderne Übersetzungen sind nachgelagerte interpretative Bewegungen, und welche interpretative Bewegung eine Übersetzung vollzieht, ist an bestimmten Versen sichtbar — Genesis 1,1, Psalm 82, Exodus 3,14, die Perikopen des Gottesnamens durch den Text hindurch. Acht importierte Übersetzungen Seite an Seite mit der ASV zu beherbergen, macht diese Sichtbarkeit gewöhnlich: Wer vergleichen möchte, was Elberfelder, Crampon, die Synodal und die CUV mit einem umstrittenen Vers tun, kann das nun tun, ohne die Bibliotheksseite zu verlassen.

## Wo dies im längeren Plan steht

Die Pipeline für importierte Übersetzungen ist die eine Hälfte des Auftrags der Bibliothek. Die andere Hälfte ist die [Wheel-of-Heaven-Übersetzung](https://docs.wheelofheaven.world/contributing/content/source-text-translation/), die sich derzeit Kapitel für Kapitel durch Genesis vorarbeitet — eine frische englische Lesart aus dem Hebräischen, hergestellt unter der projekteigenen Glossardisziplin, mit einer Translator-Editor-Reviewer-Pipeline hinter jedem Kapitel. Die importierten Übersetzungen decken die **Breite** ab (jedes Buch, acht Sprachen, gemeinfreie Ausgaben, heute ausgeliefert); die WoH-Übersetzung liefert die **Tiefe** (eine Tradition, ein Buch nach dem anderen, philologisch verteidigt, weiterhin in Arbeit).

Beide Pipelines speisen dasselbe Feld `paragraphs[].i18n[lang]` in jeder Kapiteldatei, was bedeutet, dass die Bibliotheksvorlage sie über dieselbe Schnittstelle darstellt. Wenn die WoH-Übersetzung von Genesis ihre erste stabile Fassung erreicht, wird sie neben diesen importierten Lesarten als der eigene Beitrag des Projekts zur vergleichenden Landschaft stehen, die es aufgebaut hat.

## Wo dies zu sehen ist

- Bibliotheksindex: [/library/](/library/) — jedes Buch der Hebräischen Bibel listet nun neun Sprachen in seiner Verfügbarkeitsmatrix auf
- Ein Beispielkapitel: [/library/genesis/](/library/genesis/) (oder in Ihrer Lesesprache: `/de/library/genesis/`, `/ja/library/genesis/`, …)
- Katalog und Herkunft pro Buch: [`data-library/catalog.json` auf GitHub](https://github.com/wheelofheaven/data-library/blob/main/catalog.json)
- Methodik und sprachspezifische Begründung des Quellenprogramms: [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)

## Bekannte Nacharbeiten

Drei. Die französischen Dhorme-Platzhalter für 1-Samuel, 2-Samuel und Hiob warten noch auf einen sauberen OCR-Durchgang — die zugrunde liegenden djvu-Scans im Internet Archive verschachteln hebräischen Apparat und Kommentar zu stark, um sie programmatisch zu extrahieren. Die Obadja-Kapiteldatei weist eine Gerüstlücke auf (nur einer von einundzwanzig Versen ist auf Absatzebene aufgeschlüsselt), die der Katalog derzeit fälschlich als vollständige Abdeckung meldet. Und die deutsche Elberfelder-Quelle für 1-Chronik (bibel-online.net) hat in den Kapiteln 13, 17, 18, 22 und 28 eine bekannte Duplikatinhaltsanomalie, die der Katalog in `_meta.notes` vermerkt, die Merge-Pipeline aber stromabwärts noch nicht herausgefiltert hat. Keine dieser Punkte blockiert die Lesbarkeit des importierten Textes; alle drei sind für den nächsten Durchgang vorgemerkt.

---

*— Eingereicht am 7. Juni 2026, Wheel-of-Heaven-Redaktion.*
