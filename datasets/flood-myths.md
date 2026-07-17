+++
title = "Flood-Myth Concordance"
description = "A comparative CC0 dataset of the ancient flood traditions — survivor, decreeing power, warner, cause, vessel, birds, landing place, aftermath — with links to the digitized source texts. CSV and JSON."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Flood-Myth Concordance"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-07"
keywords = ["flood myth", "deluge", "comparative mythology", "ancient Near East", "Atrahasis", "Gilgamesh", "Genesis flood", "digital humanities"]

stats = [
    { label = "Traditions", value = "8" },
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
Greco-Babylonian Berossus (Xisuthros), and the Vedic *Śatapatha Brāhmaṇa*
(Manu).

## What it's for

Comparative-mythology work usually reconstructs this table by hand from a dozen
scattered editions. Here it is once, in the open, as CSV and JSON — free to
sort, filter, merge, and cite. The **JSON** is self-describing (columns + rows);
the **CSV** opens in any spreadsheet.

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

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/flood-myths](https://huggingface.co/datasets/wheelofheaven/flood-myths)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/flood-myths](https://www.kaggle.com/datasets/zarazinsfuss/flood-myths)
