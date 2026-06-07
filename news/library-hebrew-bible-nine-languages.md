+++
title = "Library: Hebrew Bible Now Reads in Nine Languages"
description = "As of June 7, 2026, every Hebrew Bible book in the Wheel of Heaven library carries text in nine languages — English ASV plus eight imported PD translations."
date = 2026-06-07
template = "news-page.html"

[extra]
event_date = 2026-06-07
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "The library now hosts every Hebrew Bible book in nine languages: English (ASV 1901) plus eight imported public-domain translations covering German, Spanish, French, Japanese, Korean, Russian, Simplified Chinese, and Traditional Chinese. Each verse renders in the reader's site language alongside the canonical English reading, with the imported edition, year, and license recorded per book in the catalog. The choice of edition per language is documented in a methodology page on the docs site."
canon_links = [
    { title = "Hebrew Bible", path = "/wiki/hebrew-bible/" },
    { title = "Genesis", path = "/wiki/genesis/" },
    { title = "Elohim", path = "/wiki/elohim/" },
    { title = "Dhorme Bible Translation", path = "/wiki/dhorme-bible-translation/" }
]
sources = [
    { title = "Imported translations: per-language source program", url = "https://docs.wheelofheaven.world/contributing/content/imported-translations/", outlet = "Wheel of Heaven docs", date = "2026-06-07" },
    { title = "data-library catalog and chapter files", url = "https://github.com/wheelofheaven/data-library", outlet = "Wheel of Heaven data-library", date = "2026-06-07" }
]
+++

## What shipped

As of June 7, 2026, the Wheel of Heaven library hosts the full Hebrew Bible — Genesis through Zephaniah, thirty-six books — in nine languages. Every chapter renders the English ASV 1901 baseline alongside imported public-domain editions in German, Spanish, French, Japanese, Korean, Russian, Simplified Chinese, and Traditional Chinese. Readers consulting the library in any of the nine site languages now see the text in their reading language without having to route through English.

The imported editions are named, dated, and openly licensed: **Elberfelder 1905** (German), **Reina-Valera 1909** (Spanish), **Crampon 1923** with PD Dhorme additions where extant (French), **口語訳 1955** (Japanese), the Korean Revised Version of **1961** (Korean), the **Synodal 1876** (Russian), and the **Chinese Union Version** in both Simplified and Traditional scripts. Per-book provenance — translation name, year, license, source URL, retrieval date — is recorded in the library catalog for every entry. The catalog also reports per-language coverage: where versification shifts between the Masoretic and Vulgate or Synodal traditions leave a verse unaligned, the English ASV remains as a fallback.

## Why this is the right shape for the library

The library has always treated the Hebrew Bible as the operative source-text the project reads, not as a destination translation. The English ASV is the reading surface for the project's primary audience; the underlying Hebrew is what the canon actually engages with. What was missing, until today, was a clean way for non-English readers to consult the library without making English a mandatory intermediate stop.

The choice of edition per language follows the canon's source-tier discipline. Each imported translation is a critical or near-critical edition from the nineteenth or twentieth century — old enough to be public domain, recent enough to be philologically serious. Where the canon's preferred reading would require a modern edition still under copyright, the project either uses the public-domain subset of that edition or notes the gap explicitly. The clearest case is French: the Dhorme Pléiade Bible — the edition Raël himself worked from during the 1973 contact — sits under French copyright until roughly 2071. The library uses Crampon 1923 as the baseline, with Dhorme's earlier public-domain Job (1929) and Samuel (1910) replacing Crampon for those three books where they exist. The full reasoning for every language — why Elberfelder rather than Luther, why Crampon rather than Darby, why 口語訳 rather than 新共同訳, why the 1961 KRV rather than the strict 1938 — lives on the docs site at [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/).

The corpus reads the Hebrew Bible as a layered text whose Elohim referent is operative in the original language. Modern translations are downstream interpretive moves, and which interpretive move a translation makes is visible at specific verses — Genesis 1:1, Psalm 82, Exodus 3:14, the divine-name pericopes throughout. Hosting eight imported translations side-by-side with the ASV makes that visibility ordinary: the reader who wants to compare what Elberfelder, Crampon, the Synodal, and the CUV do with a contested verse can now do so without leaving the library page.

## Where this sits in the longer plan

The imported-translations pipeline is one half of the library's mandate. The other half is the [Wheel of Heaven Translation](https://docs.wheelofheaven.world/contributing/content/source-text-translation/), currently advancing through Genesis chapter by chapter — a fresh English reading produced from the Hebrew under the project's own glossary discipline, with a Translator-Editor-Reviewer pipeline behind every chapter. The imported translations cover the **breadth** (every book, eight languages, public-domain editions, shipped today); the WoH Translation provides the **depth** (one tradition, one book at a time, philologically defended, still in progress).

Both pipelines feed the same `paragraphs[].i18n[lang]` field on each chapter file, which means the library template renders them through the same interface. When the WoH Translation of Genesis reaches its first stable release, it will sit alongside these imported readings as the project's own contribution to the comparative landscape it has been building.

## Where to see it

- Library index: [/library/](/library/) — every Hebrew Bible book now lists nine languages in its availability matrix
- A sample chapter: [/library/genesis/](/library/genesis/) (or in your reading language: `/de/library/genesis/`, `/ja/library/genesis/`, …)
- Catalog and provenance per book: [`data-library/catalog.json` on GitHub](https://github.com/wheelofheaven/data-library/blob/main/catalog.json)
- Methodology and per-language source-program reasoning: [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)

## Known follow-ups

Three. The French Dhorme placeholders for 1-Samuel, 2-Samuel, and Job are still pending a clean OCR pass — the underlying djvu scans on the Internet Archive interleave Hebrew apparatus and commentary too aggressively to extract programmatically. The Obadiah chapter file has a scaffolding gap (only one of twenty-one verses is split out at the paragraph level) that the catalog currently misreports as complete coverage. And the 1-Chronicles German Elberfelder source-of-record (bibel-online.net) has a known duplicate-content quirk in chapters 13, 17, 18, 22, and 28 that the catalog notes in `_meta.notes` but the merge pipeline has not yet filtered downstream. None of these block readability of the imported text; all three are tracked for the next pass.

---

*— Filed June 7, 2026, Wheel of Heaven editorial desk.*
