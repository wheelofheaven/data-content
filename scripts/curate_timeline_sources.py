#!/usr/bin/env python3
"""Add portable internal links and structured source metadata to Timeline chapters.

The Timeline is reused by the website, EPUB, and print pipelines. Keep links as
ordinary Markdown so their labels remain useful outside Zola, and keep external
sources in frontmatter so the website can aggregate them into /sources/.

Usage:
    python scripts/curate_timeline_sources.py          # report pending changes
    python scripts/curate_timeline_sources.py --write  # apply the curation pass
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TIMELINE = ROOT / "timeline"

CHAPTERS = [
    "preamble",
    "in-the-beginning",
    "age-of-capricorn",
    "age-of-sagittarius",
    "age-of-scorpio",
    "age-of-libra",
    "age-of-virgo",
    "age-of-leo",
    "age-of-cancer",
    "age-of-gemini",
    "age-of-taurus",
    "age-of-aries",
    "age-of-pisces",
    "age-of-aquarius",
    "the-wheel-keeps-turning",
]

# Hosted paragraph identifiers use c<chapter>p<paragraph>, matching the library
# JSON schema. Only books currently hosted in data-library belong here.
HOSTED_BOOKS = {
    "Genesis": "genesis",
    "Exodus": "exodus",
    "Numbers": "numbers",
    "Deuteronomy": "deuteronomy",
    "Joshua": "joshua",
    "Judges": "judges",
    "1 Samuel": "1-samuel",
    "2 Samuel": "2-samuel",
    "1 Kings": "1-kings",
    "2 Kings": "2-kings",
    "Job": "job",
    "Psalms": "psalms",
    "Psalm": "psalms",
    "Isaiah": "isaiah",
    "Jeremiah": "jeremiah",
    "Ezekiel": "ezekiel",
    "Daniel": "daniel",
    "Joel": "joel",
    "Matthew": "matthew",
    "Mark": "mark",
    "Luke": "luke",
    "John": "john",
    "Acts": "acts",
    "Revelation": "revelation",
}

WIKI_LINKS = {
    "preamble": [
        ("Elohim", "elohim"),
        ("Council", "council-of-eternals"),
        ("synthetic biology", "synthetic-biology"),
        ("Great Flood", "great-flood"),
        ("dragons", "dragons"),
        ("Raëlian", "raelism"),
        ("precessional", "precession"),
        ("zodiac", "zodiac"),
        ("comparative mythology", "comparative-mythology"),
    ],
    "in-the-beginning": [
        ("Elohim", "elohim"),
        ("home planet", "elohim-home-planet"),
        ("Council", "council-of-eternals"),
        ("genetic engineering", "genetic-engineering"),
        ("Yahweh", "yahweh"),
        ("Satan", "satan"),
        ("astrobiology", "astrobiology"),
    ],
    "age-of-capricorn": [
        ("Elohim", "elohim"),
        ("Great Year", "great-year"),
        ("precession", "precession"),
        ("zodiac", "zodiac"),
        ("Yahweh", "yahweh"),
        ("synthetic biology", "synthetic-biology"),
        ("astrobiology", "astrobiology"),
        ("terraforming", "terraforming"),
        ("home planet", "elohim-home-planet"),
    ],
    "age-of-sagittarius": [
        ("Elohim", "elohim"),
        ("terraforming", "terraforming"),
        ("Pangaea", "pangaea"),
        ("flood", "great-flood"),
        ("Yahweh", "yahweh"),
    ],
    "age-of-scorpio": [
        ("Elohim", "elohim"),
        ("synthetic biology", "synthetic-biology"),
        ("synthetic genomics", "synthetic-genomics"),
        ("life-engineering", "life-engineering"),
        ("Yahweh", "yahweh"),
    ],
    "age-of-libra": [
        ("Elohim", "elohim"),
        ("zodiac", "zodiac"),
        ("precession", "precession"),
        ("world age", "world-age"),
        ("doubled signature", "doubled-signature"),
        ("chronology", "chronology"),
        ("archaeoastronomy", "archaeoastronomy"),
    ],
    "age-of-virgo": [
        ("Elohim", "elohim"),
        ("dragons", "dragons"),
        ("serpent", "serpent"),
        ("Satan", "satan"),
        ("Leviathan", "leviathan"),
        ("synthetic biology", "synthetic-biology"),
        ("flood", "great-flood"),
    ],
    "age-of-leo": [
        ("Elohim", "elohim"),
        ("genetic engineering", "genetic-engineering"),
        ("Adam and Eve", "adam-and-eve"),
        ("Eden", "eden"),
        ("Lucifer", "lucifer"),
        ("Tree of Life", "tree-of-life"),
        ("Tree of the Knowledge of Good and Evil", "tree-of-the-knowledge-of-good-and-evil"),
        ("serpent", "serpent"),
        ("Satan", "satan"),
        ("world age", "world-age"),
    ],
    "age-of-cancer": [
        ("Elohim", "elohim"),
        ("Eden", "eden"),
        ("Lucifer", "lucifer"),
        ("Satan", "satan"),
        ("serpent", "serpent"),
        ("Yahweh", "yahweh"),
        ("Council", "council-of-eternals"),
        ("Tree of Life", "tree-of-life"),
        ("Tree of the Knowledge of Good and Evil", "tree-of-the-knowledge-of-good-and-evil"),
        ("Adam and Eve", "adam-and-eve"),
        ("flood", "great-flood"),
        ("Noah", "noah"),
        ("antediluvian", "antediluvian"),
    ],
    "age-of-gemini": [
        ("Elohim", "elohim"),
        ("Great Flood", "great-flood"),
        ("Noah", "noah"),
        ("Noah's ark", "noahs-ark"),
        ("Noahic covenant", "noahic-covenant"),
        ("Tower of Babel", "tower-of-babel"),
        ("Babel", "babel"),
        ("confusion of tongues", "confusion-of-tongues"),
        ("alliance", "the-alliance"),
        ("theomachy", "theomachy"),
        ("Elohimian space wars", "elohimian-space-wars"),
        ("Leviathan", "leviathan"),
    ],
    "age-of-taurus": [
        ("Abraham", "abraham"),
        ("Sodom and Gomorrah", "sodom-and-gomorrah"),
        ("alliance", "the-alliance"),
        ("serpent", "serpent"),
        ("Yahweh", "yahweh"),
        ("Council", "council-of-eternals"),
        ("Tower of Babel", "tower-of-babel"),
        ("antediluvian", "antediluvian"),
        ("ancient builders", "ancient-builders"),
    ],
    "age-of-aries": [
        ("Moses", "moses"),
        ("alliance", "the-alliance"),
        ("prophet", "prophet"),
        ("Yahweh", "yahweh"),
        ("Council", "council-of-eternals"),
        ("Elijah", "elijah"),
        ("precession", "precession"),
        ("Kabbalah", "kabbalah"),
        ("cosmic competition", "cosmic-competition"),
        ("apocalypse", "apocalypse"),
    ],
    "age-of-pisces": [
        ("Jesus", "jesus"),
        ("alliance", "the-alliance"),
        ("prophet", "prophet"),
        ("Muhammad", "muhammad"),
        ("Satan", "satan"),
        ("apocalypse", "apocalypse"),
        ("doubled signature", "doubled-signature"),
        ("cosmic competition", "cosmic-competition"),
        ("Great Return", "great-return"),
    ],
    "age-of-aquarius": [
        ("embassy", "embassy"),
        ("apocalypse", "apocalypse"),
        ("prophet", "prophet"),
        ("Rael", "rael"),
        ("Golden Age", "golden-age"),
        ("Great Return", "great-return"),
        ("Elohim", "elohim"),
        ("Raëlian", "raelism"),
        ("doubled signature", "doubled-signature"),
        ("New Commandments", "new-commandments"),
        ("geniocracy", "geniocracy"),
        ("Third Temple", "third-temple"),
        ("humanitarianism", "humanitarianism"),
        ("New Jerusalem", "new-jerusalem"),
        ("alliance", "the-alliance"),
    ],
    "the-wheel-keeps-turning": [
        ("infinity", "infinity"),
        ("fractal cosmology", "fractal-cosmology"),
        ("four levels", "four-levels"),
        ("cosmic chain", "cosmic-chain"),
        ("alliance", "the-alliance"),
        ("Elohim", "elohim"),
        ("Great Year", "great-year"),
        ("world age", "world-age"),
        ("Wheel of Heaven", "wheel-of-heaven"),
        ("Golden Age", "golden-age"),
        ("embassy", "embassy"),
    ],
}

LIBRARY_TITLE_LINKS = {
    "preamble": [
        ("Hebrew Bible", "/wiki/hebrew-bible/"),
        ("Enuma Elish", "/library/enuma-elish/"),
        ("Atrahasis", "/library/atrahasis/"),
        ("Book of the Watchers", "/library/book-of-enoch/"),
    ],
    "age-of-cancer": [("Book of Enoch", "/library/book-of-enoch/")],
    "age-of-gemini": [
        ("Atrahasis", "/library/atrahasis/"),
        ("Enuma Elish", "/library/enuma-elish/"),
        ("Book of Jubilees", "/library/book-of-jubilees/"),
    ],
    "age-of-taurus": [("Epic of Gilgamesh", "/library/epic-of-gilgamesh/")],
    "age-of-pisces": [
        ("Qur'an", "/library/quran/"),
        ("Book of Mormon", "/library/mormon-book/"),
    ],
}

HAMLETS_MILL = {
    "title": "Hamlet's Mill: An Essay Investigating the Origins of Human Knowledge and Its Transmission Through Myth",
    "author": "Giorgio de Santillana and Hertha von Dechend",
    "date": "1969",
    "medium": "nonfiction-book",
    "url": "https://wheelofheaven.github.io/de-santillana-von-dechend-hamlets-mill/",
}

EXTERNAL_REFERENCES = {
    "preamble": [
        {
            "title": "Le Renard pâle",
            "author": "Marcel Griaule and Germaine Dieterlen",
            "date": "1965",
            "medium": "nonfiction-book",
        },
        {
            "title": "Dogon Restudied: A Field Evaluation of the Work of Marcel Griaule",
            "author": "Walter E. A. van Beek",
            "publication": "Current Anthropology 32 (2), 139-167",
            "date": "1991",
            "medium": "academic-paper",
            "url": "https://pure.uvt.nl/ws/portalfiles/portal/1002365/dogonrestudied.pdf",
        },
        {
            "title": "Jurassic Park",
            "author": "Michael Crichton",
            "date": "1990",
            "medium": "fiction-book",
        },
        {
            "title": "Chaos: Making a New Science",
            "author": "James Gleick",
            "date": "1987",
            "medium": "nonfiction-book",
        },
        {
            "title": "Mathematics and the Unexpected",
            "author": "Ivar Ekeland",
            "date": "1988",
            "medium": "nonfiction-book",
        },
        HAMLETS_MILL,
    ],
    "age-of-libra": [HAMLETS_MILL],
    "age-of-virgo": [
        {
            "title": "A Hebrew and English Lexicon of the Old Testament",
            "author": "Francis Brown, S. R. Driver, and Charles A. Briggs",
            "date": "1906",
            "medium": "nonfiction-book",
        },
        {
            "title": "The Hebrew and Aramaic Lexicon of the Old Testament",
            "author": "Ludwig Koehler, Walter Baumgartner, and Johann Jakob Stamm",
            "date": "1994-2000",
            "medium": "nonfiction-book",
        },
    ],
    "age-of-leo": [
        {
            "title": "The Apportionment of Human Diversity",
            "author": "Richard C. Lewontin",
            "publication": "Evolutionary Biology 6, 381-398",
            "date": "1972",
            "medium": "academic-paper",
        },
        {
            "title": "Mitochondrial DNA and human evolution",
            "author": "Rebecca L. Cann, Mark Stoneking, and Allan C. Wilson",
            "publication": "Nature 325, 31-36",
            "date": "1987",
            "medium": "academic-paper",
            "url": "https://doi.org/10.1038/325031a0",
        },
    ],
    "age-of-taurus": [
        {
            "title": "RETRACTED ARTICLE: A Tunguska sized airburst destroyed Tall el-Hammam a Middle Bronze Age city in the Jordan Valley near the Dead Sea",
            "author": "Ted E. Bunch et al.",
            "publication": "Scientific Reports 11, 18632",
            "date": "2021",
            "medium": "academic-paper",
            "url": "https://doi.org/10.1038/s41598-021-97778-3",
            "description": "Retracted by Scientific Reports on April 24, 2025; retained here for auditability.",
        },
        {
            "title": "Retraction Note: A Tunguska sized airburst destroyed Tall el-Hammam a Middle Bronze Age city in the Jordan Valley near the Dead Sea",
            "author": "Scientific Reports Editors",
            "publication": "Scientific Reports 15, 14291",
            "date": "2025",
            "medium": "article",
            "url": "https://doi.org/10.1038/s41598-025-99265-5",
            "description": "The editors state that the original article's airburst claims were not sufficiently supported by the data.",
        },
        {
            "title": "No mineralogic or geochemical evidence of impact at Tall el-Hammam, a Middle Bronze Age city in the Jordan Valley near the Dead Sea",
            "author": "Steven J. Jaret and R. Scott Harris",
            "publication": "Scientific Reports 12, 5189",
            "date": "2022",
            "medium": "academic-paper",
            "url": "https://doi.org/10.1038/s41598-022-08216-x",
        },
        {
            "title": "Misunderstandings about the Tunguska event, shock wave physics, and airbursts have resulted in misinterpretations of evidence at Tall el-Hammam",
            "author": "Mark Boslough and Andy Bruno",
            "publication": "Scientific Reports 15, 13869",
            "date": "2025",
            "medium": "academic-paper",
            "url": "https://doi.org/10.1038/s41598-025-98362-9",
        },
        {
            "title": "Redating the Great Sphinx of Giza",
            "author": "Robert M. Schoch",
            "publication": "KMT 3 (2), 52-59",
            "date": "1992",
            "medium": "article",
        },
    ],
    "age-of-aries": [
        {
            "title": "The Spaceships of Ezekiel",
            "author": "Josef F. Blumrich",
            "date": "1974",
            "medium": "nonfiction-book",
        }
    ],
    "age-of-pisces": [
        HAMLETS_MILL,
        {
            "title": "Qur'anic Geography",
            "author": "Dan Gibson",
            "date": "2011",
            "medium": "nonfiction-book",
        },
        {
            "title": "Early Islamic Qiblas",
            "author": "Dan Gibson",
            "date": "2017",
            "medium": "nonfiction-book",
        },
    ],
    "age-of-aquarius": [
        HAMLETS_MILL,
        {
            "title": "Creation of a bacterial cell controlled by a chemically synthesized genome",
            "author": "Daniel G. Gibson et al.",
            "publication": "Science 329 (5987), 52-56",
            "date": "2010",
            "medium": "academic-paper",
            "url": "https://doi.org/10.1126/science.1190719",
        },
        {
            "title": "Design and synthesis of a minimal bacterial genome",
            "author": "Clyde A. Hutchison III et al.",
            "publication": "Science 351 (6280), aad6253",
            "date": "2016",
            "medium": "academic-paper",
            "url": "https://doi.org/10.1126/science.aad6253",
        },
    ],
    "the-wheel-keeps-turning": [
        HAMLETS_MILL,
        {
            "title": "Qur'anic Geography",
            "author": "Dan Gibson",
            "date": "2011",
            "medium": "nonfiction-book",
        },
        {
            "title": "Early Islamic Qiblas",
            "author": "Dan Gibson",
            "date": "2017",
            "medium": "nonfiction-book",
        },
    ],
}


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("+++\n"):
        raise ValueError("missing TOML frontmatter")
    _, frontmatter, body = text.split("+++", 2)
    return frontmatter, body


def linked_spans(text: str) -> list[tuple[int, int]]:
    return [match.span() for match in re.finditer(r"\[[^\]]+\]\([^)]+\)", text)]


def is_linked(position: int, spans: list[tuple[int, int]]) -> bool:
    return any(start <= position < end for start, end in spans)


def link_first(text: str, label: str, target: str) -> tuple[str, int]:
    if f"]({target})" in text:
        return text, 0
    pattern = re.compile(rf"(?<![\w-]){re.escape(label)}(?![\w-])", re.IGNORECASE)
    spans = linked_spans(text)
    for match in pattern.finditer(text):
        if not is_linked(match.start(), spans):
            replacement = f"[{match.group(0)}]({target})"
            return text[: match.start()] + replacement + text[match.end() :], 1
    return text, 0


def link_hosted_citations(text: str) -> tuple[str, int]:
    names = "|".join(re.escape(name) for name in sorted(HOSTED_BOOKS, key=len, reverse=True))
    pattern = re.compile(rf"(?<![\w-])({names})\s+(\d+):(\d+)(?:[-–]\d+)?", re.IGNORECASE)
    count = 0
    offset = 0
    spans = linked_spans(text)
    parts: list[str] = []
    for match in pattern.finditer(text):
        if is_linked(match.start(), spans):
            continue
        book, chapter, paragraph = match.group(1), match.group(2), match.group(3)
        slug = HOSTED_BOOKS[next(name for name in HOSTED_BOOKS if name.lower() == book.lower())]
        parts.append(text[offset : match.start()])
        parts.append(f"[{match.group(0)}](/library/{slug}/#c{chapter}p{paragraph})")
        offset = match.end()
        count += 1
    if not count:
        return text, 0
    parts.append(text[offset:])
    return "".join(parts), count


def toml_reference(reference: dict[str, str]) -> str:
    fields = ", ".join(f"{key} = {json.dumps(value, ensure_ascii=False)}" for key, value in reference.items())
    return f"    {{ {fields} }},"


def add_references(frontmatter: str, references: list[dict[str, str]]) -> tuple[str, int]:
    if not references or re.search(r"(?m)^references\s*=", frontmatter):
        return frontmatter, 0
    lines = ["references = [", *(toml_reference(reference) for reference in references), "]", ""]
    block = "\n".join(lines)
    marker = "\n[[extra."
    if marker in frontmatter:
        frontmatter = frontmatter.replace(marker, f"\n{block}\n[[extra.", 1)
    else:
        frontmatter = f"{frontmatter}\n{block}"
    return frontmatter, len(references)


def curate(path: Path) -> tuple[str, dict[str, int], list[str]]:
    frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
    stats = {"citations": 0, "library_titles": 0, "wiki": 0, "references": 0}
    misses: list[str] = []

    body, stats["citations"] = link_hosted_citations(body)
    for label, target in LIBRARY_TITLE_LINKS.get(path.stem, []):
        body, count = link_first(body, label, target)
        stats["library_titles"] += count
        if not count and f"]({target})" not in body:
            misses.append(f"library title: {label}")
    for label, slug in WIKI_LINKS.get(path.stem, []):
        body, count = link_first(body, label, f"/wiki/{slug}/")
        stats["wiki"] += count
        if not count and f"](/wiki/{slug}/)" not in body:
            misses.append(f"wiki: {label}")

    frontmatter, stats["references"] = add_references(frontmatter, EXTERNAL_REFERENCES.get(path.stem, []))
    return f"+++{frontmatter}+++{body}", stats, misses


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write curated Markdown files")
    args = parser.parse_args()

    totals = {"citations": 0, "library_titles": 0, "wiki": 0, "references": 0}
    pending = 0
    for chapter in CHAPTERS:
        path = TIMELINE / f"{chapter}.md"
        curated, stats, misses = curate(path)
        changed = curated != path.read_text(encoding="utf-8")
        pending += changed
        if args.write and changed:
            path.write_text(curated, encoding="utf-8")
        for key, value in stats.items():
            totals[key] += value
        status = "updated" if args.write and changed else "pending" if changed else "clean"
        print(f"{path.name}: {status}; " + ", ".join(f"{key}={value}" for key, value in stats.items()))
        for miss in misses:
            print(f"  note: no match for {miss}")

    print("totals: " + ", ".join(f"{key}={value}" for key, value in totals.items()))
    print(f"files with pending changes: {pending}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
