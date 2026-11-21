+++
title = "Divine-Council Index"
description = "Sixteen passages where divine beings gather with a ruler, across eleven traditions, each field checked against a named edition. CC0 CSV and JSON."
template = "dataset-page.html"

[extra]
core_claim_ids = ["woh-claim-0011", "woh-claim-0060"]
core_versions = { woh-claim-0011 = "0.1.0", woh-claim-0060 = "0.1.0" }
dataset_name = "Wheel of Heaven Divine-Council Index"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
dataset_version = "1.2"
updated = "2026-11-21"
keywords = ["divine council", "sons of God", "assembly of the gods", "comparative religion", "ancient Near East", "Ugaritic", "biblical studies", "digital humanities"]

stats = [
    { label = "Passages", value = "16" },
    { label = "Traditions", value = "11" },
    { label = "Cited observations", value = "80" },
    { label = "Formats", value = "CSV · JSON" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/divine-council-index.csv", format = "text/csv", note = "One row per attestation — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/divine-council-index.json", format = "application/json", note = "Self-describing: rows, observations, source register and the withdrawn row." },
    { label = "Observations CSV", url = "https://api.wheelofheaven.world/v1/datasets/divine-council-index-observations.csv", format = "text/csv", note = "One row per checked field: value, evidence state, references, note." },
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

In many ancient texts the gods do not act alone: they gather around a ruler,
as an assembly, a court or a throne attendance. This index lists sixteen such
passages. For each it gives the presiding figure, the term the text uses, the
members, the function and the exact reference, and it records whether the
passage itself shows the gathered beings deliberating. Every field was checked
against a named edition and carries an evidence state.

## Traditions covered

Ugaritic (El and the gods in the *Baal Cycle*), Hebrew (*Psalm* 82, *1 Kings*
22, *Job* 1–2, *Deuteronomy* 32, *Isaiah* 6), Babylonian (*Enūma Eliš*,
*Atra-ḫasīs*), Sumerian (the gods who have Enlil seized in *Enlil and
Ninlil*), Second Temple (the *Book of the Watchers*), Greek (the Olympian
assemblies of the *Iliad*), Roman (Jupiter's *concilium* in Ovid's
*Metamorphoses*), Egyptian (the Ennead in *The Contendings of Horus and Seth*),
Norse (the *rökstólar* of the *Völuspá*), Hindu (the gods on Meru in the
*Mahābhārata*), and Latter-day Saint (the premortal scene of the *Book of
Abraham* and *Book of Moses*).

## What it's for

The scholarly case that Israel's God was once *one voice in a council* — argued
by Frank Moore Cross, E. T. Mullen, Mark S. Smith, and Michael Heiser — rests
on passages scattered across a dozen corpora in five languages. This index
gathers the core attestations into one sortable table, as CSV and JSON, free to
filter, merge, and cite.

## How the table was built

{% claim(type="inferred", id="woh-claim-0060") %}Each row is a passage in a
primary text, read in a named edition, in which divine beings gather with a
ruler.{% end %} The `scene_type` column says what kind of gathering it is:

- **assembly**: the gods gather to decide or to be addressed on a matter
  (*1 Kings* 22, *Enūma Eliš*, *Atra-ḫasīs*, the *Iliad*, Ovid, the *Völuspá*,
  the *Mahābhārata*, the Latter-day Saint scene, the *Baal Cycle*);
- **court**: a case is heard or beings present themselves before the ruler
  (*Psalm* 82, *Job*, the *Book of the Watchers*, *Enlil and Ninlil*, the
  *Contendings*);
- **throne vision**: beings attend a throne without a stated assembly
  (*Isaiah* 6);
- **allotment**: a distribution among divine beings with no narrated
  gathering (*Deuteronomy* 32).

The `deliberation` column records separately whether the passage itself shows
the members deliberating. It often does not: in *Job* only Yahweh and the satan
speak, and the *Book of the Watchers* says outright that God "needed no
counsellor" (1 Enoch 14:22).

Each of the five descriptive fields carries an **evidence state**: *attested*
(the edition says it), *qualified* (restoration, attribution or translation
changes its force; the note says how), *not stated*, or *not checked*. Read an
empty or qualified cell with its note. The observations CSV gives one line per
checked field, with references.

**What changed in version 1.2.** Version 1.1 gathered seventeen rows from
secondary summaries. A source audit checked every field against a named
edition, and an independent review re-checked the main findings. Fourteen rows
were corrected. Among the corrections: the *Enūma Eliš* assembly gives Marduk
kingship and a weapon, but not the Tablet of Destinies, which he takes from
Kingu; in *Atra-ḫasīs* Anu is king and Enlil counsellor; *Enlil and Ninlil*
names no assembly term; Ovid's gods assent to destroying humankind, and Jupiter
alone then chooses the flood; "Lord of Spirits" belongs to the *Similitudes*,
not the *Book of the Watchers*. One row was withdrawn: the Hurrian-Hittite
*Song of Emergence* has no assembly, only kingship passing by combat. Several
passages could not be read in an open edition, among them the *Baal Cycle*
assembly (KTU 1.2 I) and the Qumran text of *Deuteronomy* 32:8; those cells
are marked *not checked* or *qualified*. The full audit, review and source
register are in the
[core research repository](https://github.com/wheelofheaven/core/tree/main/docs/research/divine-council-index).

The table is CC0. Additions should keep the rule: a passage in a named edition,
with every field cited.

## How Wheel of Heaven reads it

Set side by side, these passages show a recurring picture: a ruler, a bounded
company of divine beings, and decisions over kingship, over the nations or
over the fate of humankind. The Wheel of Heaven corpus compares that picture
with the [Council of the Eternals](/wiki/council-of-eternals/) of the canon,
the governing body of the [Elohim](/wiki/elohim/) civilization, whose
majority stands behind its president, Yahweh (*Let's Welcome the
Extraterrestrials* 2:28). The
comparison is a resemblance. It does not identify these councils with one
another or with the canon's council, and the table's evidence does not decide
that question. In the canon, the Council's decision about the Flood was
destruction; the preservation of life was the exiles' act against it (see the
[flood dataset](/datasets/flood-myths/)).

This concordance is one family of the broader [Myth Index](/datasets/myth-index/), which lines up nine motif families — flood, divine council, theomachy, creation of humans, and more — in a single spine table with Thompson Motif-Index cross-references.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/divine-council-index](https://huggingface.co/datasets/wheelofheaven/divine-council-index)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/divine-council-index](https://www.kaggle.com/datasets/zarazinsfuss/divine-council-index)
