+++
title = "Grimm KHM Tale-Type Crosswalk"
description = "All 211 Grimm tales (1857 numbering) with German and English titles, ATU tale types, Aarne-1910 joins, first editions, and Wikisource links. CC0 download."
template = "dataset-page.html"

[extra]
dataset_name = "Grimm KHM Tale-Type Crosswalk"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-08"
keywords = ["Grimm fairy tales dataset", "Kinder- und Hausmärchen", "ATU index", "tale type", "Aarne-Thompson-Uther", "folklore dataset", "fairy tale classification", "KHM", "digital humanities", "open data", "CC0 download"]

stats = [
    { label = "Tales", value = "211" },
    { label = "With ATU type", value = "198" },
    { label = "Aarne-1910 joins", value = "153" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/grimm-khm-index.csv", format = "text/csv", note = "One row per tale — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/grimm-khm-index.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Zinsfuss, Zara. Grimm KHM Tale-Type Crosswalk. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/grimm-khm-index/"
citation_bibtex = '''@misc{woh-grimm-khm-index,
  title  = {Grimm KHM Tale-Type Crosswalk},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/grimm-khm-index/}
}'''
+++

Every tale of the Grimms' *Kinder- und Hausmärchen* in the canonical **1857
numbering** — the 201 tales (KHM 1–200 plus 151a) and the 10 children's
legends (KL 1–10) — in one machine-readable table: German title, English
title, **ATU tale-type number**, the edition in which the tale first appeared
(1812/15 through 1857), and a link to the 1857 German text on Wikisource.

## The two-way join

This is the companion corpus to the
[Aarne 1910 Tale-Type Index](/datasets/aarne-1910-tale-types/), and the two
datasets join in both directions. Aarne's catalogue cites Grimm tales by KHM
number in its `grimm_no` column; this crosswalk inverts those citations into
an `aarne_1910_types` column — so *Hansel and Gretel* (KHM 15) carries Aarne
type `327 A`, and Aarne type `327 A` cites KHM 15. The 153 back-references
come from Aarne's own 1910 text, not from a modern mapping — a
provenance-clean join between the founding catalogue and the corpus it
indexed most heavily.

## What's in a row

`khm_no` (e.g. `KHM 15`, `KL 3`), `part` (KHM or KL), `title_de`, `title_en`,
`atu_type` (e.g. `327A`), `atu_episode_types` (secondary types noted for the
tale), `type_note` (the full type annotation), `aarne_1910_types`,
`first_edition`, and `wikisource_de` (the 1857 text).

## Sources, honestly labeled

German titles, 1857 numbering, and first-edition data come from the
**German Wikisource** edition tables of the KHM (public domain). The ATU
type assignments follow the standard concordance compiled by the folklorist
**D. L. Ashliman** (University of Pittsburgh) — type numbers and mappings
are facts of the classification system, reproduced here as data; his site
remains the reference for tale-by-tale commentary. English titles follow
the conventional translations. Thirteen tales carry no type (`atu_type`
empty) because they are unclassified in the ATU system — mostly the
legends and a few late narrative pieces; the blank is faithful, not
missing data.

## What it's for

The KHM is the most-studied folktale corpus in existence, and this table is
the join layer between its texts and the classification systems: attach tale
types to any KHM text corpus, group tales by type family, trace which
editions added which types, or pivot into the
[Aarne 1910 catalogue](/datasets/aarne-1910-tale-types/) and the
[Myth Index](/datasets/myth-index/) for the motif-level view.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same
files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/grimm-khm-index](https://huggingface.co/datasets/wheelofheaven/grimm-khm-index)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/grimm-khm-index](https://www.kaggle.com/datasets/zarazinsfuss/grimm-khm-index)
