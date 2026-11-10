+++
title = "Prophets & Religions Catalogue"
description = "A catalogue of 48 religious traditions and their founders — period, framework-relevant content, and the corpus's comparative tier, its own heuristic for organising comparison. Downloadable CC0 CSV and JSON."
template = "dataset-page.html"

[extra]
core_claim_ids = ["woh-claim-0038", "woh-claim-0060"]
core_versions = { woh-claim-0038 = "0.1.1", woh-claim-0060 = "0.1.0" }
dataset_name = "Wheel of Heaven Prophets & Religions Catalogue"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-11"
keywords = ["comparative religion", "new religious movements", "prophets", "founders", "revelation", "religious studies", "digital humanities"]

stats = [
    { label = "Traditions", value = "48" },
    { label = "Fields", value = "7" },
    { label = "Formats", value = "CSV · JSON" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/prophets-and-religions.csv", format = "text/csv", note = "One row per tradition — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/prophets-and-religions.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Prophets & Religions Catalogue. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/prophets-and-religions/"
citation_bibtex = '''@misc{woh-prophets-and-religions,
  title  = {Wheel of Heaven Prophets \& Religions Catalogue},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/prophets-and-religions/}
}'''
+++

Forty-eight religious traditions in one table — the **founder or prophet**, the
**period**, the content each tradition contributes to the Wheel of Heaven
framework, and, in the last column, the corpus's **comparative tier** — its own
heuristic for organising comparison.

## Columns

`tradition`, `period`, `founder`, `comparative_tier`, `principal_content`,
`woh_wiki` (a link to the wiki entry where one exists). Extracted from the
[list of prophets & religions](/wiki/list-of-prophets-and-religions/) entry, so
the catalogue and the site stay in step.

## Reading the `comparative_tier` column

This column is **not a neutral scholarly rating, not a canon ranking and not an
authenticity verdict** — it is the Wheel of Heaven corpus's own heuristic for
organising comparison across contact-and-revelation traditions. The canon gives
no tiers. `Canonical` marks only the traditions whose founders the Raëlian canon
itself names (Moses, Jesus, Buddha, Muhammad, and Raëlism as the canon itself);
the scale then runs `Highly likely` → `Likely` → `Unlikely` → `Highly unlikely`.
Mormonism is **not graded**: Raël names Joseph Smith in his own commentary
(LWTE 3:27), and the corpus gives no verdict on the LDS founding. {% claim(type="inferred", id="woh-claim-0060") %}It is offered transparently as an interpretive
instrument, not as consensus fact;{% end %} the neutral biographical data in the other
columns can be used entirely independently of it. The column was named
`authenticity` until November 2026.

## What it's for

A machine-readable census of contact-and-revelation traditions — useful for
comparative religion and new-religious-movements research whether or not you
share the corpus's frame. Free to filter, sort, and cite; the
`comparative_tier` column is simply one project's labelled heuristic, there to be argued with.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/prophets-and-religions](https://huggingface.co/datasets/wheelofheaven/prophets-and-religions)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/prophets-and-religions](https://www.kaggle.com/datasets/zarazinsfuss/prophets-and-religions)
