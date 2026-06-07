+++
title = "Bibliothèque : la Bible hébraïque désormais lisible en neuf langues"
description = "Au 7 juin 2026, chaque livre de la Bible hébraïque dans la bibliothèque de la Roue du Ciel comporte le texte en neuf langues — l'ASV anglaise et huit traductions du domaine public importées."
date = 2026-06-07
template = "news-page.html"

[extra]
event_date = 2026-06-07
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "La bibliothèque héberge désormais chaque livre de la Bible hébraïque en neuf langues : l'anglais (ASV 1901) ainsi que huit traductions du domaine public importées couvrant l'allemand, l'espagnol, le français, le japonais, le coréen, le russe, le chinois simplifié et le chinois traditionnel. Chaque verset s'affiche dans la langue du site choisie par le lecteur, à côté de la lecture canonique anglaise, l'édition importée, l'année et la licence étant consignées par livre dans le catalogue. Le choix de l'édition par langue est documenté dans une page de méthodologie sur le site de documentation."
canon_links = [
    { title = "Bible hébraïque", path = "/wiki/hebrew-bible/" },
    { title = "Genèse", path = "/wiki/genesis/" },
    { title = "Elohim", path = "/wiki/elohim/" },
    { title = "Traduction de la Bible par Dhorme", path = "/wiki/dhorme-bible-translation/" }
]
sources = [
    { title = "Traductions importées : programme des sources par langue", url = "https://docs.wheelofheaven.world/contributing/content/imported-translations/", outlet = "Documentation Wheel of Heaven", date = "2026-06-07" },
    { title = "Catalogue data-library et fichiers de chapitres", url = "https://github.com/wheelofheaven/data-library", outlet = "Wheel of Heaven data-library", date = "2026-06-07" }
]
+++

## Ce qui a été livré

Au 7 juin 2026, la bibliothèque de la Roue du Ciel héberge l'intégralité de la Bible hébraïque — de la Genèse à Sophonie, soit trente-six livres — en neuf langues. Chaque chapitre affiche la base de référence anglaise ASV 1901 aux côtés d'éditions importées du domaine public en allemand, espagnol, français, japonais, coréen, russe, chinois simplifié et chinois traditionnel. Les lecteurs qui consultent la bibliothèque dans l'une quelconque des neuf langues du site voient désormais le texte dans leur langue de lecture sans avoir à passer par l'anglais.

Les éditions importées sont nommées, datées et placées sous une licence ouverte. Le catalogue indique également la couverture par langue : lorsque les divergences de versification entre les traditions massorétique, de la Vulgate ou synodale laissent un verset non aligné, l'ASV anglaise demeure comme solution de repli.

| Langue | Édition | Année | Licence |
|---|---|---|---|
| Anglais | American Standard Version (ASV) | 1901 | Domaine public |
| Allemand | Elberfelder | 1905 | Domaine public |
| Espagnol | Reina-Valera | 1909 | Domaine public |
| Français | Crampon (Dhorme du domaine public pour Job et Samuel lorsque disponible) | 1923 | Domaine public |
| Japonais | 口語訳 (Kougo-yaku) | 1955 | Domaine public (droits moraux) |
| Coréen | Korean Revised Version (KRV) | 1961 | Domaine public |
| Russe | Synodal | 1876 | Domaine public |
| Chinois simplifié | Chinese Union Version (和合本) | 1919 | Domaine public |
| Chinois traditionnel | Chinese Union Version (和合本) | 1919 | Domaine public |

La provenance par livre — nom de la traduction, année, licence, URL de la source, date de récupération — est consignée dans `data-library/catalog.json` pour chaque entrée, sous le bloc `translations.{lang}` de chaque livre.

## Pourquoi des traductions littérales

Chaque édition importée ci-dessus est, par sa théorie de la traduction, une traduction d'**équivalence formelle** — parfois appelée familièrement « littérale ». Les éditions retenues se rangent du côté *concordant* de leur tradition respective : l'Elberfelder est notoirement la Bible allemande la plus mot-à-mot de l'époque moderne ; la Reina-Valera, Crampon, la Synodale, la KRV et la Chinese Union Version appartiennent toutes à la même lignée d'équivalence formelle dans leur propre langue. La 口語訳 est la modernisation en japonais courant de la 文語訳 classique — encore d'équivalence formelle selon les standards de la tradition, délibérément positionnée contre la 新共同訳 (1987), d'équivalence dynamique, qui devint plus tard la version standard catholico-protestante japonaise.

Ce choix est délibéré, non nostalgique. Une traduction d'équivalence formelle cherche à préserver la **forme lexicale et syntaxique** de la source — un mot hébreu, un mot cible, lorsque les langues le permettent ; une proposition hébraïque, une proposition cible ; un même mot dans un même verset source reçoit la même traduction à travers le corpus lorsque cela est possible. Une traduction d'équivalence dynamique fait l'inverse — elle cherche à préserver l'*effet* sur le lecteur, ce qui implique qu'elle condense, paraphrase et lisse régulièrement les choix de la source en une langue cible idiomatique.

Pour une bibliothèque dont la raison d'être consiste à héberger huit traductions à des fins comparatives — *que fait chaque tradition des péricopes du nom divin, de Genèse 1,1, du Psaume 82, du pluriel Elohim ?* — l'équivalence formelle est le seul registre qui préserve la question. Dès qu'une traduction a décidé de rendre `יהוה` par « le SEIGNEUR » parce que cela se lit mieux en anglais, ou par 主 parce que cela se lit mieux en japonais, le choix lexical que le canon cherche à suivre a déjà disparu. Le lecteur voit le toilettage du traducteur, non sa lecture.

Le même raisonnement vaut pour le référent Elohim lui-même. L'Elberfelder garde « Jehova » / « Elohim » apparents là où l'hébreu les distingue ; Crampon écrit « Yahvé » et « Élohim » avec la même rigueur ; la Synodale préserve les paires « Господь » / « Бог » qui renvoient au texte source. Une traduction d'équivalence dynamique donnerait, dans le même verset, un *Dieu* indifférencié — plus facile à lire, mais l'argument comparatif n'aurait plus rien à comparer.

## Pourquoi c'est la bonne forme pour la bibliothèque

La bibliothèque a toujours traité la Bible hébraïque comme le texte-source opérationnel que le projet lit, et non comme une traduction de destination. L'ASV anglaise est la surface de lecture pour le public principal du projet ; l'hébreu sous-jacent est ce avec quoi le canon dialogue réellement. Ce qui manquait, jusqu'à aujourd'hui, c'était un moyen propre pour les lecteurs non anglophones de consulter la bibliothèque sans faire de l'anglais une étape intermédiaire obligatoire.

Le choix de l'édition par langue suit la discipline de hiérarchie des sources du canon. Chaque traduction importée est une édition critique ou quasi critique du XIXᵉ ou du XXᵉ siècle — assez ancienne pour appartenir au domaine public, assez récente pour être philologiquement sérieuse. Là où la lecture privilégiée par le canon exigerait une édition moderne encore sous droits d'auteur, le projet utilise soit le sous-ensemble du domaine public de cette édition, soit signale explicitement la lacune. Le cas le plus clair est celui du français : la Bible de la Pléiade traduite par Dhorme — l'édition à partir de laquelle Raël lui-même a travaillé lors du contact de 1973 — demeure sous droits d'auteur français jusque vers 2071. La bibliothèque utilise Crampon 1923 comme base de référence, le Job (1929) et le Samuel (1910) de Dhorme, antérieurs et tombés dans le domaine public, remplaçant Crampon pour ces trois livres lorsqu'ils existent. Le raisonnement complet pour chaque langue — pourquoi Elberfelder plutôt que Luther, pourquoi Crampon plutôt que Darby, pourquoi 口語訳 plutôt que 新共同訳, pourquoi la KRV de 1961 plutôt que la version stricte de 1938 — figure sur le site de documentation à [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/).

Le corpus lit la Bible hébraïque comme un texte en couches dont le référent Elohim est opératoire dans la langue originale. Les traductions modernes sont des gestes interprétatifs en aval, et le geste interprétatif que pose une traduction est visible à des versets précis — Genèse 1,1, Psaume 82, Exode 3,14, les péricopes du nom divin disséminées dans tout le corpus. Héberger huit traductions importées côte à côte avec l'ASV rend cette visibilité ordinaire : le lecteur qui souhaite comparer ce que l'Elberfelder, Crampon, la Synodale et la CUV font d'un verset contesté peut désormais le faire sans quitter la page de la bibliothèque.

## Où cela s'inscrit dans le plan plus large

Le pipeline des traductions importées constitue une moitié du mandat de la bibliothèque. L'autre moitié est la [Traduction de la Roue du Ciel](https://docs.wheelofheaven.world/contributing/content/source-text-translation/), qui progresse actuellement chapitre par chapitre à travers la Genèse — une nouvelle lecture anglaise produite à partir de l'hébreu selon la discipline glossaire propre au projet, avec un pipeline Traducteur-Éditeur-Réviseur derrière chaque chapitre. Les traductions importées couvrent l'**étendue** (chaque livre, huit langues, éditions du domaine public, livrées aujourd'hui) ; la Traduction de la Roue du Ciel apporte la **profondeur** (une tradition, un livre à la fois, philologiquement défendu, encore en cours).

Les deux pipelines alimentent le même champ `paragraphs[].i18n[lang]` sur chaque fichier de chapitre, ce qui signifie que le gabarit de la bibliothèque les affiche via la même interface. Lorsque la Traduction de la Roue du Ciel de la Genèse atteindra sa première version stable, elle prendra place aux côtés de ces lectures importées comme la contribution propre du projet au paysage comparatif qu'il a patiemment construit.

## Où consulter le résultat

- Index de la bibliothèque : [/library/](/library/) — chaque livre de la Bible hébraïque liste désormais neuf langues dans sa matrice de disponibilité
- Un chapitre exemple : [/library/genesis/](/library/genesis/) (ou dans votre langue de lecture : `/de/library/genesis/`, `/ja/library/genesis/`, …)
- Catalogue et provenance par livre : [`data-library/catalog.json` sur GitHub](https://github.com/wheelofheaven/data-library/blob/main/catalog.json)
- Méthodologie et raisonnement du programme des sources par langue : [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)

## Suites connues

Trois. Les placeholders français Dhorme pour 1-Samuel, 2-Samuel et Job attendent encore une passe OCR propre — les scans djvu sous-jacents sur Internet Archive entrelacent l'apparat critique hébreu et le commentaire de manière trop agressive pour permettre une extraction programmatique. Le fichier de chapitre d'Abdias présente une lacune de structure (un seul verset sur vingt-et-un est découpé au niveau du paragraphe) que le catalogue indique à tort comme une couverture complète. Et la source de référence allemande Elberfelder pour 1-Chroniques (bibel-online.net) présente une particularité connue de contenu dupliqué dans les chapitres 13, 17, 18, 22 et 28 que le catalogue signale dans `_meta.notes` mais que le pipeline de fusion n'a pas encore filtrée en aval. Aucun de ces points ne bloque la lisibilité du texte importé ; tous trois sont consignés pour la prochaine passe.

---

*— Déposé le 7 juin 2026, rédaction de la Roue du Ciel.*
