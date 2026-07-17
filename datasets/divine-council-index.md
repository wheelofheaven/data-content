+++
title = "Divine-Council Index"
description = "A comparative CC0 index of the divine council across the ancient traditions — presiding figure, council term, members, function, and primary reference, with links to the digitized texts. CSV and JSON."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Divine-Council Index"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-07"
keywords = ["divine council", "sons of God", "assembly of the gods", "comparative religion", "ancient Near East", "Ugaritic", "biblical studies", "digital humanities"]

stats = [
    { label = "Attestations", value = "11" },
    { label = "Traditions", value = "6" },
    { label = "Formats", value = "CSV · JSON" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/divine-council-index.csv", format = "text/csv", note = "One row per attestation — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/divine-council-index.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Divine-Council Index. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/divine-council-index/"
citation_bibtex = '''@misc{woh-divine-council-index,
  title  = {Wheel of Heaven Divine-Council Index},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/divine-council-index/}
}'''
+++

Across the ancient Near East and its heirs, the gods do not act alone — they
**convene**. An index of that recurring institution, the *divine council*: for
each attestation, the presiding figure, the **council term** in its own
language, the members, the function, and the primary reference — each row
linked to the digitized text where the library holds one.

## Traditions covered

Ugaritic (the assembly of El in the *Baal Cycle*), Hebrew (*Psalm* 82, *1
Kings* 22, *Job*, *Deuteronomy* 32, *Isaiah* 6), Babylonian (*Enūma Eliš*,
*Atra-ḫasīs*), Second Temple (the *Book of the Watchers*), Hurrian-Hittite (the
*Song of Emergence*), and Latter-day Saint (the premortal council of the *Book
of Moses*).

## What it's for

The scholarly case that Israel's God was once *one voice in a council* — argued
by Frank Moore Cross, E. T. Mullen, Mark S. Smith, and Michael Heiser — rests
on passages scattered across a dozen corpora in five languages. This index
gathers the core attestations into one sortable table, as CSV and JSON, free to
filter, merge, and cite.

## How Wheel of Heaven reads it

Line the councils up and a single institution shows through the local vocabulary:
a presiding figure, a bounded body of "sons" or "holy ones," and decisions —
over kingship, over the nations, over the fate of humankind — taken *in
assembly* rather than by fiat. The Wheel of Heaven corpus reads that institution
as one and the same referent across the traditions: the
[Council of the Eternals](/wiki/council-of-eternals/), the governing body of the
[Elohim](/wiki/elohim/) civilization, of which the biblical *bene elohim* and
the Ugaritic *sons of El* are the compressed cultural memory. The same council
that, in the [flood dataset](/datasets/flood-myths/), is recorded deciding on
the reset.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/divine-council-index](https://huggingface.co/datasets/wheelofheaven/divine-council-index)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/divine-council-index](https://www.kaggle.com/datasets/zarazinsfuss/divine-council-index)
