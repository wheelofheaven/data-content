+++
title = "Antediluvian Chronologies"
description = "The Sumerian King List, Berossos, and the Genesis 5/11 patriarchs side by side — with Masoretic, Samaritan, and Septuagint figures in parallel. CC0 download."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Antediluvian Chronologies"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-08"
keywords = ["antediluvian", "Sumerian King List", "Berossos", "Genesis genealogy", "patriarch ages", "Septuagint chronology", "Masoretic text", "Samaritan Pentateuch", "biblical chronology dataset", "digital humanities", "open data", "CC0 download"]

stats = [
    { label = "Figures", value = "38" },
    { label = "Lists", value = "4" },
    { label = "Textual witnesses", value = "MT · SP · LXX" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/antediluvian-chronologies.csv", format = "text/csv", note = "One row per figure — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/antediluvian-chronologies.json", format = "application/json", note = "Self-describing: columns + rows; absent values as null." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Antediluvian Chronologies. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/antediluvian-chronologies/"
citation_bibtex = '''@misc{woh-antediluvian-chronologies,
  title  = {Wheel of Heaven Antediluvian Chronologies},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/antediluvian-chronologies/}
}'''
+++

The long-lived generations around the Flood, in one table: the **eight
antediluvian kings** of the Sumerian King List (WB-444 recension — 241,200
years across five cities), the **ten kings of Berossos** (120 sars =
432,000 years), and the **Genesis 5 and 11 patriarchs** — with the
Masoretic, Samaritan Pentateuch, and Septuagint figures side by side in
parallel columns. Scholars reconstruct this comparison by hand every time
the biblical-chronology debate comes up; here it is once, machine-readable,
every number anchored to a primary-text locator.

## The four lists

- **`sumerian-king-list-wb444`** — Alulim of Eridu through Ubara-Tutu of
  Shuruppak, reign lengths as the prism gives them, ending "then the flood
  swept over." Verified line-by-line against the corpus's own
  [digitized King List](/library/sumerian-king-list-woh/), which every row
  deep-links.
- **`berossos`** — Aloros through Xisouthros (= Ziusudra), reigns counted in
  *sars* of 3,600 years, from the *Babyloniaca* fragments (FGrH 680 F 3).
  The 432,000-year total is the figure made famous by *Hamlet's Mill*.
- **`genesis-5`** — Adam through Noah: age at fathering, remaining years,
  and total for each patriarch in **MT, SP, and LXX**. Masoretic figures
  verified verse-by-verse against [our Genesis translation](/library/genesis-woh/).
- **`genesis-11`** — Shem through Terah (the postdiluvian decline curve),
  same three-witness treatment.

## Where the witnesses disagree

The three textual traditions are not minor variants of one another — they
encode different chronologies, and the table makes the divergences exact:

- The **LXX adds a century** to most fathering ages (Adam begets at 230, not
  130), stretching the world-era by ~1,400 years.
- The **LXX-only second Kainan** (Genesis 11:13 LXX; Luke 3:36) gets his own
  row, with the MT and SP columns honestly null.
- **Methuselah** in the majority LXX reading (167/802) survives the Flood by
  fourteen years — the note records the Alexandrinus variant that repairs it.
- The **SP compresses Genesis 5** so that Jared, Methuselah, and Lamech all
  die in the Flood year, and gives Terah 145 years so Abram leaves Harran at
  his father's death.
- **Eber** manages three different lifespans in three witnesses
  (464 / 404 / 504).

Every `fathering + remaining = total` identity in the table is checked
programmatically at build time; where a witness doesn't state a number, the
cell is null rather than reconstructed.

## How Wheel of Heaven reads it

Two features of this material carry the corpus's larger argument. First, the
**shape is shared**: Mesopotamia and Genesis both remember a sequence of
extraordinarily long-lived figures before the Flood and a stepwise decline
after it — the [antediluvian](/wiki/antediluvian/) entry treats the parallel
at length. Second, the numbers are **structured, not random**: Berossos'
120 sars and the sexagesimal reign-lengths belong to the same numerical
world as the precessional figures examined in
[Hamlet's Mill](/wiki/hamlets-mill/) and the corpus's
[World Ages](/datasets/world-ages/) reckoning. The canon reads the long
lifespans as memory of the creators' longevity technology rather than
mythical inflation — a reading developed in the [wiki](/wiki/antediluvian/),
while this table stays neutral comparative data.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same
files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/antediluvian-chronologies](https://huggingface.co/datasets/wheelofheaven/antediluvian-chronologies)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/antediluvian-chronologies](https://www.kaggle.com/datasets/zarazinsfuss/antediluvian-chronologies)
