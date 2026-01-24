#!/usr/bin/env python3
"""
Content Validation Script for Wheel of Heaven

Validates:
- Frontmatter (required fields, correct types)
- Internal links (checks if referenced pages exist)
- Translation coverage (compares against English source)

Usage:
    python scripts/validate.py                    # Run all validations
    python scripts/validate.py --frontmatter      # Only frontmatter
    python scripts/validate.py --links            # Only links
    python scripts/validate.py --coverage         # Only translation coverage
    python scripts/validate.py --fix              # Auto-fix simple issues
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Optional

# Content root
CONTENT_ROOT = Path(__file__).parent.parent

# Supported languages
LANGUAGES = ["en", "de", "es", "fr", "ja", "ko", "ru", "zh", "zh-Hant"]

# Sections that should have content
SECTIONS = ["wiki", "timeline", "resources", "essentials", "explainers"]

# Required frontmatter fields by section (for English source)
REQUIRED_FIELDS = {
    "wiki": ["title", "description", "template"],
    "timeline": ["title", "description", "template"],
    "resources": ["title", "description", "template"],
    "essentials": ["title", "description", "template"],
    "explainers": ["title", "description", "template"],
    "_default": ["title"],
}

# Required fields for translations (less strict - can inherit template)
REQUIRED_FIELDS_TRANSLATION = {
    "wiki": ["title", "description"],
    "timeline": ["title", "description"],
    "resources": ["title", "description"],
    "essentials": ["title", "description"],
    "explainers": ["title", "description"],
    "_default": ["title"],
}

# Valid templates by section
VALID_TEMPLATES = {
    "wiki": ["wiki-page.html"],
    "timeline": ["timeline-section.html", "timeline-page.html"],
    "resources": ["resources-page.html", "resources-section.html"],
    "essentials": ["essentials-page.html", "essentials-section.html"],
    "explainers": ["explainer-page.html"],
}


class ValidationError:
    def __init__(self, file: Path, message: str, severity: str = "error"):
        self.file = file
        self.message = message
        self.severity = severity  # error, warning, info

    def __str__(self):
        icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}.get(self.severity, "•")
        rel_path = self.file.relative_to(CONTENT_ROOT) if self.file else "N/A"
        return f"{icon} [{self.severity.upper()}] {rel_path}: {self.message}"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract TOML frontmatter from markdown content."""
    if not content.startswith("+++"):
        return {}, content

    parts = content.split("+++", 2)
    if len(parts) < 3:
        return {}, content

    frontmatter_str = parts[1].strip()
    body = parts[2].strip()

    # Simple TOML parser
    frontmatter = {}
    current_section = frontmatter

    for line in frontmatter_str.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("[") and line.endswith("]"):
            section_name = line[1:-1]
            if section_name not in frontmatter:
                frontmatter[section_name] = {}
            current_section = frontmatter[section_name]
            continue

        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            # Parse value
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            elif value.startswith("["):
                try:
                    value = json.loads(value.replace("'", '"'))
                except:
                    pass
            elif value == "true":
                value = True
            elif value == "false":
                value = False
            elif value.isdigit():
                value = int(value)

            current_section[key] = value

    return frontmatter, body


def get_section(file_path: Path) -> Optional[str]:
    """Get the section name from file path."""
    rel_path = file_path.relative_to(CONTENT_ROOT)
    parts = rel_path.parts

    # Skip language directories
    if parts[0] in LANGUAGES[1:]:  # Non-English
        if len(parts) > 1 and parts[1] in SECTIONS:
            return parts[1]
    elif parts[0] in SECTIONS:
        return parts[0]

    return None


def is_translation(file_path: Path) -> bool:
    """Check if file is a translation (non-English)."""
    rel_path = file_path.relative_to(CONTENT_ROOT)
    parts = rel_path.parts
    return parts[0] in LANGUAGES[1:]


def validate_frontmatter(errors: list[ValidationError]) -> int:
    """Validate frontmatter in all markdown files."""
    count = 0

    for md_file in CONTENT_ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue

        content = md_file.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(content)

        if not frontmatter:
            if md_file.name != "_index.md":
                errors.append(ValidationError(md_file, "Missing frontmatter"))
            continue

        section = get_section(md_file)
        is_trans = is_translation(md_file)

        # Use less strict requirements for translations
        if is_trans:
            required = REQUIRED_FIELDS_TRANSLATION.get(section, REQUIRED_FIELDS_TRANSLATION["_default"])
        else:
            required = REQUIRED_FIELDS.get(section, REQUIRED_FIELDS["_default"])

        # Check required fields
        for field in required:
            if field not in frontmatter:
                errors.append(ValidationError(md_file, f"Missing required field: {field}"))

        # Check template validity
        if section and "template" in frontmatter:
            valid = VALID_TEMPLATES.get(section, [])
            if valid and frontmatter["template"] not in valid:
                errors.append(ValidationError(
                    md_file,
                    f"Invalid template '{frontmatter['template']}' for section '{section}'",
                    "warning"
                ))

        # Check description length
        if "description" in frontmatter:
            desc = frontmatter["description"]
            if isinstance(desc, str):
                if len(desc) < 50:
                    errors.append(ValidationError(
                        md_file, f"Description too short ({len(desc)} chars, min 50)", "warning"
                    ))
                elif len(desc) > 300:
                    errors.append(ValidationError(
                        md_file, f"Description too long ({len(desc)} chars, max 300)", "warning"
                    ))

        # Check title
        if "title" in frontmatter:
            title = frontmatter["title"]
            if isinstance(title, str) and len(title) > 70:
                errors.append(ValidationError(
                    md_file, f"Title too long ({len(title)} chars, max 70 for SEO)", "warning"
                ))

        count += 1

    return count


def validate_links(errors: list[ValidationError]) -> int:
    """Validate internal links in markdown files."""
    count = 0

    # Build index of existing pages
    existing_pages = set()
    for md_file in CONTENT_ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue
        rel_path = md_file.relative_to(CONTENT_ROOT)
        # Convert to URL path
        if md_file.name == "_index.md":
            url_path = "/" + str(rel_path.parent) + "/"
        else:
            url_path = "/" + str(rel_path.with_suffix("")) + "/"
        url_path = url_path.replace("\\", "/")
        existing_pages.add(url_path.lower())

    # Also add section roots
    for section in SECTIONS:
        existing_pages.add(f"/{section}/")
        for lang in LANGUAGES[1:]:
            existing_pages.add(f"/{lang}/{section}/")

    # Check links in each file
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    wiki_link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

    for md_file in CONTENT_ROOT.rglob("*.md"):
        if md_file.name == "README.md":
            continue

        content = md_file.read_text(encoding="utf-8")
        _, body = parse_frontmatter(content)

        # Check markdown links
        for match in link_pattern.finditer(body):
            link_text, link_url = match.groups()

            # Skip external links, anchors, and special protocols
            if link_url.startswith(("http://", "https://", "mailto:", "#", "/")):
                if link_url.startswith("/"):
                    # Check internal absolute links
                    clean_url = link_url.split("#")[0].lower()
                    if not clean_url.endswith("/"):
                        clean_url += "/"
                    if clean_url not in existing_pages and not clean_url.startswith("/images/"):
                        errors.append(ValidationError(
                            md_file, f"Broken internal link: {link_url}", "warning"
                        ))
                continue

            # Relative links
            if link_url.startswith("../") or not link_url.startswith("/"):
                # Resolve relative path
                try:
                    target = (md_file.parent / link_url).resolve()
                    target_rel = target.relative_to(CONTENT_ROOT.resolve())
                    url_path = "/" + str(target_rel).replace("\\", "/")
                    if not url_path.endswith("/"):
                        url_path += "/"
                    if url_path.lower() not in existing_pages:
                        errors.append(ValidationError(
                            md_file, f"Broken relative link: {link_url}", "warning"
                        ))
                except (ValueError, OSError):
                    errors.append(ValidationError(
                        md_file, f"Invalid relative link: {link_url}", "warning"
                    ))

        count += 1

    return count


def validate_coverage(errors: list[ValidationError]) -> dict:
    """Check translation coverage against English source."""
    coverage = defaultdict(lambda: {"total": 0, "translated": 0, "missing": []})

    # Get English source files (files in section directories, not in language directories)
    english_files = {}
    for section in SECTIONS:
        section_path = CONTENT_ROOT / section
        if section_path.exists():
            for md_file in section_path.rglob("*.md"):
                rel_path = md_file.relative_to(CONTENT_ROOT)
                english_files[str(rel_path)] = md_file

    # Check each language
    for lang in LANGUAGES[1:]:
        lang_path = CONTENT_ROOT / lang

        for en_rel_path, en_file in english_files.items():
            # Expected translation path: de/wiki/elohim.md for wiki/elohim.md
            trans_path = lang_path / en_rel_path

            coverage[lang]["total"] += 1

            if trans_path.exists():
                coverage[lang]["translated"] += 1
            else:
                coverage[lang]["missing"].append(en_rel_path)

    return dict(coverage)


def print_coverage_report(coverage: dict):
    """Print translation coverage report."""
    print("\n📊 Translation Coverage Report")
    print("=" * 50)

    for lang in sorted(coverage.keys()):
        data = coverage[lang]
        total = data["total"]
        translated = data["translated"]
        pct = (translated / total * 100) if total > 0 else 0

        bar_len = 30
        filled = int(bar_len * pct / 100)
        bar = "█" * filled + "░" * (bar_len - filled)

        print(f"{lang:8} [{bar}] {pct:5.1f}% ({translated}/{total})")

    print()


def main():
    parser = argparse.ArgumentParser(description="Validate Wheel of Heaven content")
    parser.add_argument("--frontmatter", action="store_true", help="Only validate frontmatter")
    parser.add_argument("--links", action="store_true", help="Only validate internal links")
    parser.add_argument("--coverage", action="store_true", help="Only check translation coverage")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    # Default to all if none specified
    run_all = not (args.frontmatter or args.links or args.coverage)

    errors: list[ValidationError] = []
    stats = {}

    print("🔍 Validating content...\n")

    # Frontmatter validation
    if run_all or args.frontmatter:
        print("Checking frontmatter...")
        stats["frontmatter_files"] = validate_frontmatter(errors)

    # Link validation
    if run_all or args.links:
        print("Checking internal links...")
        stats["link_files"] = validate_links(errors)

    # Coverage report
    coverage = {}
    if run_all or args.coverage:
        print("Checking translation coverage...")
        coverage = validate_coverage(errors)

    # Output results
    if args.json:
        result = {
            "errors": [{"file": str(e.file), "message": e.message, "severity": e.severity} for e in errors],
            "stats": stats,
            "coverage": coverage
        }
        print(json.dumps(result, indent=2))
    else:
        # Print errors
        error_count = sum(1 for e in errors if e.severity == "error")
        warning_count = sum(1 for e in errors if e.severity == "warning")

        if errors:
            print(f"\n{'='*50}")
            print("Issues Found:")
            print("="*50)
            for error in sorted(errors, key=lambda e: (e.severity != "error", str(e.file))):
                print(error)

        # Print coverage
        if coverage:
            print_coverage_report(coverage)

        # Summary
        print("="*50)
        print(f"Summary: {error_count} errors, {warning_count} warnings")

        if args.strict:
            sys.exit(1 if errors else 0)
        else:
            sys.exit(1 if error_count > 0 else 0)


if __name__ == "__main__":
    main()
