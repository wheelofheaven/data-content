+++
title = "Flood-Myth Concordance"
description = "A machine-readable, comparative CC0 dataset of eleven ancient flood myths — survivor, warner, cause, vessel, landing, aftermath. Download as CSV or JSON."
template = "dataset-page.html"

[extra]
core_claim_ids = ["woh-claim-0010", "woh-claim-0060"]
core_versions = { woh-claim-0010 = "0.1.0", woh-claim-0060 = "0.1.0" }
dataset_name = "Wheel of Heaven Flood-Myth Concordance"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-07"
keywords = ["flood myth dataset", "machine-readable", "deluge", "comparative mythology data", "ancient Near East", "Atrahasis", "Gilgamesh", "Genesis flood", "digital humanities", "open data", "CC0 download"]

stats = [
    { label = "Traditions", value = "11" },
    { label = "Fields", value = "13" },
    { label = "Formats", value = "CSV · JSON" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/flood-myths.csv", format = "text/csv", note = "One row per tradition — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/flood-myths.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Flood-Myth Concordance. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/flood-myths/"
citation_bibtex = '''@misc{woh-flood-myths,
  title  = {Wheel of Heaven Flood-Myth Concordance},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/flood-myths/}
}'''
+++

A single table lining up the ancient flood traditions field by field — the
**survivor**, the power that **decrees** the flood, the one who **warns** the
hero, the stated **cause**, the **vessel**, the **birds** released, the
**landing place**, and the **aftermath** — each row linked to the digitized
source text where the Wheel of Heaven library holds one.

## Traditions covered

Sumerian (Ziusudra), Babylonian *Atra-ḫasīs* and *Gilgamesh* XI (Utnapishtim),
Hebrew *Genesis* (Noah), Islamic *Qurʾān* (Nūḥ), Greek Deucalion, the
Greco-Babylonian Berossus (Xisuthros), the Vedic *Śatapatha Brāhmaṇa* (Manu),
the Aztec *Leyenda de los Soles* (Tata and Nena), the Andean Viracocha
chronicles (Betanzos, Molina), and the Norse *Prose Edda* (Bergelmir).

## What it's for

Comparative-mythology work usually reconstructs this table by hand from a dozen
scattered editions. Here it is once, in the open, as CSV and JSON — free to
sort, filter, merge, and cite. The **JSON** is self-describing (columns + rows);
the **CSV** opens in any spreadsheet.

## How the table was built

Each row is a flood tradition attested in a **primary text** — named in the
*Source text* column. A tradition is included when its flood account survives
in a readable source and states enough of the shared elements to populate the
comparative columns; the concordance is deliberately conservative, favouring
eleven well-attested traditions over a long tail of fragmentary or contested
parallels. Where the corpus has digitized the source, the *Read in* link points
into the Wheel of Heaven library; where it has not, the source is named but not
yet hosted.

The columns are the recurring elements of the ancient Near Eastern and
Indo-European flood narrative — the **survivor**, the power that **decrees** the
flood, the figure who **warns** the hero, the stated **cause**, the **vessel**,
the **birds** released, the **landing place**, and the **aftermath**. A blank
cell means the element is absent or unstated in that tradition's source, not
that it was dropped.

*Approximate date* is the scholarly consensus for the **composition of the
source text**, not for any event it narrates. Traditions are grouped by textual
family, so the two Babylonian rows (*Atra-ḫasīs* and the *Gilgamesh* Tablet XI)
appear separately: they are distinct compositions, not two readings of one text.

This is **version 1.1** of the concordance. Version 1.0 shipped eight rows
across the Near Eastern and Mediterranean core; 1.1 adds three traditions from
outside it — Aztec (Tata and Nena), Andean (Viracocha), and Norse (Bergelmir) —
for eleven rows in all. It is CC0, so it can be extended, corrected, or merged
without permission; additions should preserve the "primary text required" rule
so every row stays anchored to a citable source.

## How Wheel of Heaven reads it

The rows are laid out as neutral comparative data — but read down the columns
and a shared *procedure* appears rather than a shared mood: a destruction
decided in assembly and sworn as irrevocable, a single survivor given precise
instructions and told to preserve *the seed of all living things*, and a
warning delivered by one member of the planning body against the will of
another. The Wheel of Heaven corpus reads that convergence not as a borrowed
folk-motif but as the administrative record of a **managed reset** — treated at
length in [The Flood Was a Reset, Not a Punishment](/articles/the-flood-was-a-reset-not-a-punishment/)
and the [Great Flood](/wiki/great-flood/) entry.


This concordance is one family of the broader [Myth Index](/datasets/myth-index/), which lines up nine motif families — flood, divine council, theomachy, creation of humans, and more — in a single spine table with Thompson Motif-Index cross-references.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/flood-myths](https://huggingface.co/datasets/wheelofheaven/flood-myths)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/flood-myths](https://www.kaggle.com/datasets/zarazinsfuss/flood-myths)
