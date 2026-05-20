+++
title = "README"
draft = true
render = false
+++

# Wheel of Heaven Content

Source content for the Wheel of Heaven knowledge base. This repository contains all wiki entries, timeline pages, articles, and multilingual translations.

## Overview

This content is consumed by multiple targets:
- **[www.wheelofheaven.world](https://www.wheelofheaven.world)** - Main website (Zola static site)
- **[api.wheelofheaven.world](https://api.wheelofheaven.world)** - JSON API endpoints

## Structure

```
data-content/
├── _index.md                 # Homepage content
├── wiki/                     # Encyclopedia entries
├── timeline/                 # World Ages and historical periods
├── resources/                # External resources catalog
├── essentials/               # Quick reference guides
├── explainers/               # In-depth articles
├── articles/                 # Blog posts
├── library/                  # Library section pages
├── de/                       # German translations
├── es/                       # Spanish translations
├── fr/                       # French translations
├── ja/                       # Japanese translations
├── ko/                       # Korean translations
├── ru/                       # Russian translations
├── zh/                       # Simplified Chinese
└── zh-Hant/                  # Traditional Chinese
```

## Content Format

Content files use Markdown with TOML frontmatter:

```markdown
+++
title = "Page Title"
description = "SEO description"
template = "wiki-page.html"

[extra]
category = "Category Name"
+++

Content body in Markdown...
```

## Languages

| Code | Language |
|------|----------|
| en | English (default) |
| de | Deutsch |
| es | Español |
| fr | Français |
| ja | 日本語 |
| ko | 한국어 |
| ru | Русский |
| zh | 简体中文 |
| zh-Hant | 繁體中文 |

## Usage

This repository is used as a Git submodule:

```bash
# In www.wheelofheaven.io (the main website repo)
git submodule add git@github.com:wheelofheaven/data-content.git content

# Update to latest
git submodule update --remote content
```

## Contributing

1. Fork this repository
2. Create a branch for your changes
3. Submit a pull request

See [Contributing Guidelines](https://www.wheelofheaven.world/contributing) for the broad overview, and the **[developer docs at docs.wheelofheaven.world](https://docs.wheelofheaven.world)** for the per-content-type how-tos:

- [Wiki Entry](https://docs.wheelofheaven.world/contributing/content/wiki-entry/) — frontmatter, structure, sourcing, terminology
- [Article](https://docs.wheelofheaven.world/contributing/content/article/) — long-form, idea-driven, evergreen
- [Newsroom Dispatch](https://docs.wheelofheaven.world/contributing/content/newsroom-dispatch/) — short, event-anchored
- [Translations](https://docs.wheelofheaven.world/contributing/content/translations/) — workflow + per-language conventions for the 10 supported languages
- [Frontmatter Reference](https://docs.wheelofheaven.world/reference/frontmatter/) — every TOML field with worked examples

## License

CC0-1.0 (Public Domain)
