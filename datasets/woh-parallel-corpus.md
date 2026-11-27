+++
title = "Wheel of Heaven Parallel Corpus"
description = "10,917 verse-aligned rows across 48 ancient texts — Hebrew, Greek, Ge'ez, Coptic, Akkadian, Ugaritic, Avestan — beside new English translations. Free download."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Parallel Corpus"
dataset_version = "1.0"
license = "CC-BY-SA-4.0"
license_url = "https://creativecommons.org/licenses/by-sa/4.0/"
updated = "2026-11-26"
keywords = ["parallel corpus", "ancient languages dataset", "biblical Hebrew parallel text", "Koine Greek", "Ge'ez", "Coptic", "Akkadian", "cuneiform", "Ugaritic", "Avestan", "machine translation", "transliteration", "religious texts dataset", "Hugging Face", "open data"]

stats = [
    { label = "Rows", value = "10,917" },
    { label = "Books", value = "48" },
    { label = "Source languages", value = "9" },
    { label = "License", value = "CC BY-SA 4.0" },
]

downloads = [
    { label = "Hugging Face", url = "https://huggingface.co/datasets/wheelofheaven/woh-parallel-corpus", format = "application/jsonl", note = "One JSONL file per book; load all or one book by config name." },
    { label = "Kaggle", url = "https://www.kaggle.com/datasets/zarazinsfuss/woh-parallel-corpus", format = "application/jsonl", note = "The same files as a single Kaggle download." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Parallel Corpus, version 1.0. Wheel of Heaven, 2026. CC BY-SA 4.0. https://www.wheelofheaven.world/datasets/woh-parallel-corpus/"
citation_bibtex = '''@misc{woh-parallel-corpus,
  title  = {Wheel of Heaven Parallel Corpus},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {Version 1.0; CC BY-SA 4.0, per-row source licences},
  url    = {https://www.wheelofheaven.world/datasets/woh-parallel-corpus/}
}'''
+++

Every book of the Wheel of Heaven Translation Program in one dataset: the
source text in its own script, a transliteration, and the new English
translation, aligned verse by verse. It covers the Hebrew Bible books the
program has translated, the Greek New Testament books, 1 Enoch and Jubilees
from their Aramaic, Hebrew, Greek and Geʿez witnesses, the Gospel of Thomas in
Coptic, the Vendidad in Avestan, the Theogony, Tobit and the Wisdom of Solomon
in Greek, and the Mesopotamian and Ugaritic texts (Atrahasis, Adapa,
Gilgamesh XI, the Baal Cycle, the Sumerian poems and the King List).

## What each row holds

- **`original`** and **`original_lang`**: the source text and its language, line
  by line where a book mixes witnesses.
- **`original_attestation`**: whether the line comes from a complete manuscript
  tradition, from a Dead Sea Scrolls fragment whose gaps the editor filled, from
  reconstruction, or from a composite of several tablets.
- **`transliteration`**, and for cuneiform texts **`cuneiform`** with a
  confidence flag. The cuneiform is back-rendered from the transliteration with
  the OGSL sign list, a reading aid rather than an attested tablet.
- **`english`**: the Wheel of Heaven translation, with the translator's
  **`commentary`** where the editor annotated a verse, and a public-domain
  **`reference_english`** (ASV 1901, World English Bible, Charles) where one is
  available.
- **`witness_primary`** and **`witness_secondary`**: the manuscripts behind the line.

Load all books together, or one book by its config name (`genesis-woh`,
`book-of-enoch-woh`, …). Each book is also published as its own dataset with
its translation glossary and a book-specific card.

## Licence

The Wheel of Heaven layer (translation, commentary, glossary references and the
transliterations generated for this corpus) is CC0. Some source editions are
not: the SBL Greek New Testament and the Coptic Scriptorium Gospel of Thomas are
CC BY 4.0, and the Perseus and First1KGreek texts are CC BY-SA 4.0. Every row
names its source licence in `original_license`, so the collection is offered
under CC BY-SA 4.0 and single rows can be reused under their own terms. The
Sumerian sources (ETCSL) are not openly licensed; for those books only the
English is included.

## Read the texts

Each book opens in the [library](/library/) reader, where the interlinear view
shows the same original, transliteration and cuneiform word by word.

## Also available on

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/woh-parallel-corpus](https://huggingface.co/datasets/wheelofheaven/woh-parallel-corpus)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/woh-parallel-corpus](https://www.kaggle.com/datasets/zarazinsfuss/woh-parallel-corpus)
