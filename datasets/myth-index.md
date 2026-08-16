+++
title = "Myth Index"
description = "A machine-readable CC0 index of 75 myth-motif attestations across 9 families — flood, divine council, theomachy, creation, giants — with Thompson motif cross-references."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Myth Index"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-08"
keywords = ["myth index", "mythology dataset", "comparative mythology data", "Thompson Motif-Index", "flood myth", "divine council", "chaoskampf", "creation of humans", "giants", "tower of Babel", "digital humanities", "open data", "CC0 download"]

stats = [
    { label = "Attestations", value = "75" },
    { label = "Motif families", value = "9" },
    { label = "Fields", value = "13" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/myth-index.csv", format = "text/csv", note = "One row per attestation — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/myth-index.json", format = "application/json", note = "Self-describing: columns + rows; motif lists as arrays." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Myth Index. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/myth-index/"
citation_bibtex = '''@misc{woh-myth-index,
  title  = {Wheel of Heaven Myth Index},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/myth-index/}
}'''
+++

A cross-cultural index of mythological motifs, one row per **attestation**: a
named **primary text**, a **locator** into it, a two-sentence **summary**, and
**Thompson Motif-Index** cross-references — spanning nine motif families from
the flood to the immortality quest, across the ancient Near East, the
Mediterranean, India, East Asia, Scandinavia, and the Americas.

## Motif families covered

**Flood** (11), **divine council** (17), **theomachy** (8) — imported from the
three specialized Wheel of Heaven concordances — plus six new families:
**creation of humans** (9), **sky-descent** (6), **tower of Babel** (5),
**giants** (7), **garden-paradise** (6), and the **immortality quest** (6).

## How the index relates to the specialized datasets

The Myth Index is the *spine*. For the three families that already have
dedicated concordances, each row's `see_dataset` column points at the
specialized table — the [Flood-Myth Concordance](/datasets/flood-myths/),
the [Divine-Council Index](/datasets/divine-council-index/), and the
[Theomachy Cross-References](/datasets/theomachy-crossrefs/) — which carry the
full per-family column depth (survivor and vessel, council term and presiding
figure, champion and weapon). The index row gives every family the same
comparable shape.

## The scholarly crosswalk

Each row carries `thompson_motifs` — motif numbers from Stith Thompson's
*Motif-Index of Folk-Literature* (A1010 *Deluge*, A167.1 *Council of the
gods*, F531.6.1.1 *Sons of God and daughters of men*, and so on). Motif
numbers are the standard scholarly address system for exactly this material,
so the index joins cleanly against any motif-indexed corpus.

The `atu_type` and `aarne_1910_type` columns are present but sparse — and
that sparseness is deliberate honesty: the Aarne–Thompson–Uther system
catalogues *folktales*, while myth material is addressed by the Motif-Index's
A-section. Rows only carry a tale-type number where a genuine type exists.
The companion dataset, the
[Aarne 1910 Tale-Type Index](/datasets/aarne-1910-tale-types/), publishes the
founding tale-type catalogue itself in structured form.

## How the rows were built

Every row requires a named primary text and a locator — the same
"primary text required" rule as the specialized concordances. Summaries
describe what the source says; they are deliberately separated from the
`woh_reading` column, which carries the Wheel of Heaven canon reading where
the canon states one (the ark as genetic repository, Eden as the creators'
laboratory-garden, the tower as a rocket project). Blank `woh_reading` means
the corpus offers no canon-specific claim for that attestation — the
comparative layer stands on its own.

## How Wheel of Heaven reads it

Read across the families and the corpus's larger claim comes into view: the
same small set of administrative scenes — an assembly that decrees, a
laboratory that creates, a garden that encloses, a reset that spares one
lineage, a technology withheld — recurring across traditions that had no
contact. The corpus reads that convergence as memory of a shared history
rather than a shared imagination; the argument is developed across the
[wiki](/wiki/comparative-mythology/) and the
[library](/library/) of digitized sources this index links into.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same
files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/myth-index](https://huggingface.co/datasets/wheelofheaven/myth-index)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/myth-index](https://www.kaggle.com/datasets/zarazinsfuss/myth-index)
