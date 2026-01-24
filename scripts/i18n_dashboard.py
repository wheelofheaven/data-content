#!/usr/bin/env python3
"""
Internationalization Dashboard for Wheel of Heaven

Generates detailed translation coverage reports with:
- Per-language coverage statistics
- Per-section breakdown
- Missing content identification
- Quality metrics (description length, title presence)
- Exportable reports (JSON, HTML)

Usage:
    python scripts/i18n_dashboard.py                    # Terminal output
    python scripts/i18n_dashboard.py --json             # JSON output
    python scripts/i18n_dashboard.py --html > report.html  # HTML report
"""

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

# Content root
CONTENT_ROOT = Path(__file__).parent.parent

# Supported languages
LANGUAGES = ["en", "de", "es", "fr", "ja", "ko", "ru", "zh", "zh-Hant"]
LANGUAGE_NAMES = {
    "en": "English",
    "de": "Deutsch",
    "es": "Español",
    "fr": "Français",
    "ja": "日本語",
    "ko": "한국어",
    "ru": "Русский",
    "zh": "简体中文",
    "zh-Hant": "繁體中文"
}

# Sections to track
SECTIONS = ["wiki", "timeline", "resources", "essentials", "explainers"]


def parse_frontmatter(content: str) -> dict:
    """Extract TOML frontmatter from markdown content."""
    if not content.startswith("+++"):
        return {}

    parts = content.split("+++", 2)
    if len(parts) < 3:
        return {}

    frontmatter_str = parts[1].strip()
    frontmatter = {}

    for line in frontmatter_str.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("["):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            frontmatter[key] = value

    return frontmatter


def get_english_content() -> dict:
    """Get all English source content organized by section."""
    english = {}

    for section in SECTIONS:
        section_path = CONTENT_ROOT / section
        if not section_path.exists():
            continue

        english[section] = {}
        for md_file in section_path.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            rel_path = md_file.relative_to(section_path)
            content = md_file.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)

            english[section][str(rel_path)] = {
                "path": str(md_file),
                "title": fm.get("title", ""),
                "description": fm.get("description", ""),
                "word_count": len(content.split())
            }

    return english


def get_translation_coverage(english: dict) -> dict:
    """Calculate translation coverage for each language."""
    coverage = {}

    for lang in LANGUAGES[1:]:  # Skip English
        lang_path = CONTENT_ROOT / lang
        coverage[lang] = {
            "total_files": 0,
            "translated_files": 0,
            "sections": {},
            "missing": [],
            "quality": {
                "with_title": 0,
                "with_description": 0,
                "avg_description_len": 0
            }
        }

        desc_lengths = []

        for section, files in english.items():
            section_stats = {
                "total": len(files),
                "translated": 0,
                "missing": []
            }

            for rel_path, en_data in files.items():
                coverage[lang]["total_files"] += 1
                trans_path = lang_path / section / rel_path

                if trans_path.exists():
                    section_stats["translated"] += 1
                    coverage[lang]["translated_files"] += 1

                    # Check quality
                    content = trans_path.read_text(encoding="utf-8")
                    fm = parse_frontmatter(content)

                    if fm.get("title"):
                        coverage[lang]["quality"]["with_title"] += 1
                    if fm.get("description"):
                        coverage[lang]["quality"]["with_description"] += 1
                        desc_lengths.append(len(fm["description"]))
                else:
                    section_stats["missing"].append({
                        "path": str(rel_path),
                        "title": en_data["title"]
                    })
                    coverage[lang]["missing"].append(f"{section}/{rel_path}")

            coverage[lang]["sections"][section] = section_stats

        if desc_lengths:
            coverage[lang]["quality"]["avg_description_len"] = sum(desc_lengths) / len(desc_lengths)

    return coverage


def print_terminal_report(english: dict, coverage: dict):
    """Print colored terminal report."""
    print("\n" + "=" * 70)
    print("  WHEEL OF HEAVEN - TRANSLATION COVERAGE DASHBOARD")
    print("  Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 70)

    # Overall summary
    total_en = sum(len(files) for files in english.values())
    print(f"\n  Source Content: {total_en} English files across {len(english)} sections\n")

    # Language summary table
    print("  " + "-" * 66)
    print(f"  {'Language':<15} {'Coverage':>10} {'Progress':>35} {'Missing':>8}")
    print("  " + "-" * 66)

    for lang in LANGUAGES[1:]:
        data = coverage[lang]
        total = data["total_files"]
        translated = data["translated_files"]
        pct = (translated / total * 100) if total > 0 else 0
        missing = total - translated

        # Progress bar
        bar_width = 30
        filled = int(bar_width * pct / 100)
        bar = "█" * filled + "░" * (bar_width - filled)

        # Color coding
        if pct >= 80:
            status = "✓"
        elif pct >= 50:
            status = "○"
        else:
            status = "✗"

        lang_name = f"{LANGUAGE_NAMES[lang]} ({lang})"
        print(f"  {status} {lang_name:<13} {pct:>6.1f}%   [{bar}] {missing:>6}")

    print("  " + "-" * 66)

    # Section breakdown
    print("\n  SECTION BREAKDOWN:")
    print("  " + "-" * 66)

    for section in SECTIONS:
        if section not in english:
            continue
        total = len(english[section])
        print(f"\n  {section.upper()} ({total} files)")

        for lang in LANGUAGES[1:]:
            if section in coverage[lang]["sections"]:
                sect_data = coverage[lang]["sections"][section]
                pct = (sect_data["translated"] / sect_data["total"] * 100) if sect_data["total"] > 0 else 0
                print(f"    {lang:>7}: {sect_data['translated']:>3}/{sect_data['total']:>3} ({pct:>5.1f}%)")

    # Priority translations (high-impact missing content)
    print("\n  PRIORITY TRANSLATIONS (most needed):")
    print("  " + "-" * 66)

    for lang in ["ko", "zh-Hant"]:  # Languages with lowest coverage
        if lang in coverage:
            print(f"\n  {LANGUAGE_NAMES[lang]} - Top 5 missing:")
            for item in coverage[lang]["missing"][:5]:
                print(f"    - {item}")

    print("\n" + "=" * 70 + "\n")


def generate_html_report(english: dict, coverage: dict) -> str:
    """Generate HTML dashboard report."""
    total_en = sum(len(files) for files in english.values())

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Translation Coverage Dashboard - Wheel of Heaven</title>
    <style>
        :root {{
            --bg: #1a1a2e;
            --surface: #16213e;
            --text: #e4e4e4;
            --muted: #888;
            --accent: #f9c74f;
            --success: #4ade80;
            --warning: #fbbf24;
            --error: #f87171;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }}
        h1, h2 {{ color: var(--accent); }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }}
        .stat-card {{
            background: var(--surface);
            padding: 1.5rem;
            border-radius: 12px;
        }}
        .stat-card h3 {{ margin: 0 0 0.5rem; font-size: 0.9rem; color: var(--muted); }}
        .stat-card .value {{ font-size: 2rem; font-weight: bold; }}
        .progress-bar {{
            background: #333;
            border-radius: 8px;
            overflow: hidden;
            height: 24px;
            margin: 0.5rem 0;
        }}
        .progress-fill {{
            height: 100%;
            transition: width 0.3s;
        }}
        .lang-row {{
            background: var(--surface);
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        .lang-name {{ width: 150px; font-weight: bold; }}
        .lang-progress {{ flex: 1; }}
        .lang-stats {{ width: 100px; text-align: right; color: var(--muted); }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }}
        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #333;
        }}
        th {{ color: var(--muted); font-weight: normal; }}
        .high {{ color: var(--success); }}
        .medium {{ color: var(--warning); }}
        .low {{ color: var(--error); }}
    </style>
</head>
<body>
    <h1>Translation Coverage Dashboard</h1>
    <p style="color: var(--muted);">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

    <div class="stats-grid">
        <div class="stat-card">
            <h3>Source Files</h3>
            <div class="value">{total_en}</div>
        </div>
        <div class="stat-card">
            <h3>Languages</h3>
            <div class="value">{len(LANGUAGES)}</div>
        </div>
        <div class="stat-card">
            <h3>Sections</h3>
            <div class="value">{len(english)}</div>
        </div>
    </div>

    <h2>Coverage by Language</h2>
"""

    for lang in LANGUAGES[1:]:
        data = coverage[lang]
        pct = (data["translated_files"] / data["total_files"] * 100) if data["total_files"] > 0 else 0

        if pct >= 80:
            color = "var(--success)"
            status = "high"
        elif pct >= 50:
            color = "var(--warning)"
            status = "medium"
        else:
            color = "var(--error)"
            status = "low"

        html += f"""
    <div class="lang-row">
        <div class="lang-name">{LANGUAGE_NAMES[lang]}</div>
        <div class="lang-progress">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {pct}%; background: {color};"></div>
            </div>
        </div>
        <div class="lang-stats {status}">{data['translated_files']}/{data['total_files']} ({pct:.1f}%)</div>
    </div>
"""

    html += """
    <h2>Coverage by Section</h2>
    <table>
        <tr>
            <th>Section</th>
"""

    for lang in LANGUAGES[1:]:
        html += f"<th>{lang}</th>"

    html += "</tr>"

    for section in SECTIONS:
        if section not in english:
            continue
        html += f"<tr><td><strong>{section}</strong></td>"

        for lang in LANGUAGES[1:]:
            if section in coverage[lang]["sections"]:
                sect = coverage[lang]["sections"][section]
                pct = (sect["translated"] / sect["total"] * 100) if sect["total"] > 0 else 0

                if pct >= 80:
                    cls = "high"
                elif pct >= 50:
                    cls = "medium"
                else:
                    cls = "low"

                html += f'<td class="{cls}">{pct:.0f}%</td>'
            else:
                html += "<td>-</td>"

        html += "</tr>"

    html += """
    </table>
</body>
</html>
"""

    return html


def main():
    parser = argparse.ArgumentParser(description="Translation coverage dashboard")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--html", action="store_true", help="Output as HTML")
    args = parser.parse_args()

    english = get_english_content()
    coverage = get_translation_coverage(english)

    if args.json:
        result = {
            "generated": datetime.now().isoformat(),
            "source_files": sum(len(f) for f in english.values()),
            "languages": LANGUAGE_NAMES,
            "coverage": coverage
        }
        print(json.dumps(result, indent=2))
    elif args.html:
        print(generate_html_report(english, coverage))
    else:
        print_terminal_report(english, coverage)


if __name__ == "__main__":
    main()
