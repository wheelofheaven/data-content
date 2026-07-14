+++
title = "Precessional World Ages"
description = "The 12 precessional World Ages on the Wheel of Heaven reckoning — zodiac, symbol, start/end year, Genesis-day mapping, and summary — as a downloadable CC0 dataset. CSV and JSON."
template = "dataset-page.html"

[extra]
dataset_name = "Wheel of Heaven Precessional World Ages"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-07"
keywords = ["precession of the equinoxes", "Great Year", "astrological ages", "World Ages", "archaeoastronomy", "Age of Aquarius", "chronology"]

stats = [
    { label = "Ages", value = "12" },
    { label = "Years per age", value = "2,160" },
    { label = "Formats", value = "CSV · JSON" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "CSV", url = "https://api.wheelofheaven.world/v1/datasets/world-ages.csv", format = "text/csv", note = "One row per age — opens in any spreadsheet." },
    { label = "JSON", url = "https://api.wheelofheaven.world/v1/datasets/world-ages.json", format = "application/json", note = "Self-describing: columns + rows." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Precessional World Ages. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/world-ages/"
citation_bibtex = '''@misc{woh-world-ages,
  title  = {Wheel of Heaven Precessional World Ages},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/world-ages/}
}'''
+++

The equinox does not hold still against the stars — it drifts backward through
the zodiac, one full circuit every ~25,920 years. Divide that **Great Year** by
twelve and you get the **World Ages**, each ~2,160 years long. This dataset is
the corpus's reckoning of all twelve — zodiac sign and symbol, start and end
year, the Genesis "day" the corpus maps the age to, and a one-line summary,
each row linked to the full timeline entry.

## What's in it

Twelve rows, from the Age of Capricorn (c. 21,810 BCE) to the current Age of
Aquarius (from 1950 CE). Columns: `age`, `zodiac`, `symbol`, `start_year`,
`end_year`, `genesis_day`, `url`, `summary`. Extracted directly from the live
[timeline](/timeline/) entries, so the dataset and the site stay in step.

## What it's for

The precessional-ages framework sits behind a great deal of comparative work —
Hamlet's Mill, archaeoastronomy, the "Age of Aquarius." Here is one project's
complete, dated scheme in a machine-readable form, free to plot, compare, and
cite.

## How Wheel of Heaven reads it

The corpus treats the twelve ages not as astrology but as a **calendar** — the
clock against which it dates the events its other datasets record. The
[flood](/datasets/flood-myths/) falls in the Age of Cancer; the mapping of the
first eight ages onto the eight "days" of the [Genesis](/wiki/genesis/) creation
account (`genesis_day`, columns above) is the corpus's claim that *Genesis 1 is
a compressed precessional chronology* rather than a week. The full argument is
in the [World Age](/wiki/world-age/) entry and the [timeline](/timeline/).
