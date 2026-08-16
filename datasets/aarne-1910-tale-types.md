+++
title = "Aarne 1910 Tale-Type Index"
description = "The founding catalogue of the Aarne–Thompson–Uther system, fully structured: all 1910 tale types with German text, English glosses, and cross-references. CC0."
template = "dataset-page.html"

[extra]
core_claim_ids = ["woh-claim-0056", "woh-claim-0060"]
core_versions = { woh-claim-0056 = "0.1.0", woh-claim-0060 = "0.1.0" }
dataset_name = "Aarne 1910 Tale-Type Index (Verzeichnis der Märchentypen)"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-08"
keywords = ["Aarne-Thompson-Uther", "tale type index", "Verzeichnis der Märchentypen", "folklore dataset", "folktale classification", "fairy tales", "ATU index", "Antti Aarne", "digital humanities", "open data", "CC0 download"]

stats = [
    { label = "Rows", value = "603" },
    { label = "Glossed titles", value = "533" },
    { label = "Source year", value = "1910" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/aarne-1910-tale-types.csv", format = "text/csv", note = "One row per type (incl. lettered subtypes) — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/aarne-1910-tale-types.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Aarne, Antti. Verzeichnis der Märchentypen (FFC 3, 1910), structured dataset ed. Zara Zinsfuss. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/aarne-1910-tale-types/"
citation_bibtex = '''@misc{woh-aarne-1910,
  title  = {Aarne 1910 Tale-Type Index (Verzeichnis der M{\"a}rchentypen), structured dataset},
  author = {Aarne, Antti and Zinsfuss, Zara},
  year   = {2026},
  note   = {Source text 1910, public domain; dataset CC0-1.0},
  url    = {https://www.wheelofheaven.world/datasets/aarne-1910-tale-types/}
}'''
+++

In 1910 the Finnish folklorist **Antti Aarne** published the *Verzeichnis der
Märchentypen* — the first systematic catalogue of folktale types, and the
founding document of what became, through Stith Thompson's revisions (1928,
1961) and Hans-Jörg Uther's (2004), the **Aarne–Thompson–Uther (ATU)
system** used by folklorists everywhere. Type 300 is still the Dragon-Slayer,
type 510 is still Cinderella, because Aarne numbered them here first.

This dataset is, to our knowledge, the first complete machine-readable
edition of that founding catalogue: **603 rows** covering every numbered type
and lettered subtype, with the German title and description, the catalogue's
full section structure, group captions, Aarne's cross-references to
Grundtvig's Danish index (`Gg`) and the Grimms' *Kinder- und Hausmärchen*
(`Grimm`), the printed page number — and an **English gloss** for each of the
533 titled types.

## Provenance, honestly labeled

The rows were parsed from the **proofread German Wikisource transcription**
of FFC 3 (status *fertig*, proofread twice against the scans), page by page,
with the parse verified against the printed table of contents. The 1910
source text is **public domain worldwide** (Aarne died in 1925); the
transcription of a public-domain text adds no new copyright; the structuring
and the English glosses are our own work, released **CC0**. Unlike the later
editions of the index — 1928, 1961, and 2004 all remain in copyright — this
edition can be redistributed, embedded, and built upon without restriction.

## What's in a row

`type_label` (e.g. `313 A`), numeric `type_start`/`type_end` for ranges,
`subtype`, `title_de`, `description_de`, `title_en` (gloss), the catalogue
structure (`part` — Tiermärchen / Eigentliche Märchen / Schwänke —
`division`, `subsection`, and nested `group_label`/`group_title` captions
such as *505–508 Der dankbare Tote*), `grundtvig_no`, `grimm_no`, and `page`.

One caveat for careful users: this is the **1910 numbering**. The great
majority of numbers survive unchanged into ATU 2004, but later editions
added, merged, and occasionally renumbered types — treat the numbers as
Aarne's, not as a substitute for the current ATU catalogue.

## What it's for

Reference tables in folklore databases, historical study of the
classification itself, joining against motif-indexed corpora, and training
data grounded in a clean-provenance source. It is the "official layer"
companion to the [Myth Index](/datasets/myth-index/), which cross-references
Thompson motif numbers and carries an `aarne_1910_type` join column.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same
files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/aarne-1910-tale-types](https://huggingface.co/datasets/wheelofheaven/aarne-1910-tale-types)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/aarne-1910-tale-types](https://www.kaggle.com/datasets/zarazinsfuss/aarne-1910-tale-types)
