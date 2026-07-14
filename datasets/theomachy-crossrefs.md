+++
title = "Theomachy Cross-References"
description = "A comparative CC0 dataset of the combat myth (chaoskampf) across the ancient traditions — champion, adversary, chaos form, weapon, outcome, reference — with links to the digitized texts. CSV and JSON."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Theomachy Cross-References"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-07"
keywords = ["theomachy", "chaoskampf", "combat myth", "comparative mythology", "ancient Near East", "dragon slaying", "Leviathan", "digital humanities"]

stats = [
    { label = "Combat myths", value = "8" },
    { label = "Traditions", value = "8" },
    { label = "Formats", value = "CSV · JSON" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/theomachy-crossrefs.csv", format = "text/csv", note = "One row per combat myth — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/theomachy-crossrefs.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Theomachy Cross-References. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/theomachy-crossrefs/"
citation_bibtex = '''@misc{woh-theomachy-crossrefs,
  title  = {Wheel of Heaven Theomachy Cross-References},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/theomachy-crossrefs/}
}'''
+++

One of the most widely distributed plots in the ancient world: a young
storm-and-order god confronts an older adversary of chaos — sea, dragon, or
serpent — defeats it, and takes or secures kingship. Scholars call it the
*Chaoskampf*. This dataset lines up eight instances field by field — the
**champion**, the **adversary**, the form chaos takes, the **weapon**, and the
**outcome** — each row linked to the digitized source text where the library
holds one.

## Instances

Marduk vs Tiamat (*Enūma Eliš*), Baal vs Yam and the serpent Lôtan (*Baal
Cycle*), Yahweh vs Leviathan / Rahab / the Sea (Psalms, Isaiah, Job), Zeus vs
Typhon (*Theogony*), Indra vs Vṛtra (*Rig Veda*), the Storm-god vs Illuyanka
(Hittite), Ra vs Apophis (Egyptian), and Michael vs the dragon (*Revelation*).

## What it's for

The kinship of these myths — Ugaritic *Lôtan* and Hebrew *Leviathan* are the
same word — is a textbook case in comparative mythology, argued from Gunkel's
*Schöpfung und Chaos* onward. This table gathers the core instances into one
sortable file, as CSV and JSON, free to filter, merge, and cite.

## How Wheel of Heaven reads it

The pattern is usually explained by diffusion — one Chaoskampf borrowed down the
generations. The Wheel of Heaven corpus takes the shared plot as something
sharper: the compressed cultural memory of an actual conflict — the
[Theomachy](/wiki/theomachy/), the multi-age political-military struggle between
the [Elohim](/wiki/elohim/) home-world Council and the exiled-creator faction on
Earth — retold by each tradition as its own dragon-slaying. The "serpent" who
withholds order, in this reading, is the losing side of that war, and the
[flood](/datasets/flood-myths/) is one of its campaigns.
