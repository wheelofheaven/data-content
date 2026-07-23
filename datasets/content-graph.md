+++
title = "Wheel of Heaven Content Graph"
description = "A downloadable CC0 knowledge graph of the Wheel of Heaven corpus — every page is a node, every curated or in-text link a typed edge. JSON and GraphML."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Content Graph"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-07"
keywords = ["knowledge graph", "comparative mythology", "ancient astronaut theory", "network dataset", "linked data", "digital humanities"]
api_url = "https://api.wheelofheaven.world/v1/graph/"
schema_url = "https://api.wheelofheaven.world/v1/schema/content-graph/"

stats = [
    { label = "Nodes (pages)", value = "167" },
    { label = "Typed edges", value = "1,369" },
    { label = "Edge types", value = "see_also · in_body" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/graph/content-graph.json", format = "application/json", note = "Self-describing — nodes, typed edges, stats, and a QA block." },
    { label = "GraphML", url = "https://api.wheelofheaven.world/v1/graph/content-graph.graphml", format = "application/graphml+xml", note = "Drops straight into Gephi, Cytoscape, or networkx." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Content Graph. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/content-graph/"
citation_bibtex = '''@misc{woh-content-graph,
  title  = {Wheel of Heaven Content Graph},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/content-graph/}
}'''
+++

Every page on Wheel of Heaven is a **node**; every curated *See also* link and
every in-text cross-reference is a typed **edge**. This dataset is that graph,
extracted from the live corpus and released into the public domain — free to
download, analyse, redistribute, and cite.

## What's in it

- **Nodes** — wiki entries, articles, timeline ages, and dispatches, each with
  its `id` (`section/slug`), `title`, `kind`, `claim_type`, `category`, degree,
  and canonical `url`.
- **Typed edges** — `see_also` (a curated, hand-written relatedness link) and
  `in_body` (a prose cross-reference between entries). Directed.
- **A QA block** — the orphans, asymmetric `see_also` pairs, and dangling links
  the graph build surfaces. We ship it in the file; it's how the project catches
  broken cross-links.

## Using it

The **JSON** is self-describing: load it and read `nodes`, `edges`, `stats`, and
`qa`. The **GraphML** opens directly in Gephi, Cytoscape, or `networkx` for
layout and network analysis. For programmatic traversal, the live
[API](https://api.wheelofheaven.world/v1/graph/) serves the same graph plus
per-node ego-networks at `/v1/graph/{section}/{slug}/`, and every content
endpoint carries its own typed `links.related`.

## Scope

English corpus only, regenerated on every deploy — treat the counts above as the
current scale and the [live API](https://api.wheelofheaven.world/v1/graph/) as
the source of truth. For per-page relatedness in any of the nine site languages,
each page's own *See also* block is the localized equivalent.

## Also available on

This dataset is also published, CC0, on two open-data platforms — the same files, mirrored for reach and preservation:

- **Hugging Face** — [huggingface.co/datasets/wheelofheaven/content-graph](https://huggingface.co/datasets/wheelofheaven/content-graph)
- **Kaggle** — [kaggle.com/datasets/zarazinsfuss/content-graph](https://www.kaggle.com/datasets/zarazinsfuss/content-graph)
