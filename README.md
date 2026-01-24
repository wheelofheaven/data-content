+++
title = "README"
draft = true
render = false
+++

# Wheel of Heaven Content

Source content for the Wheel of Heaven knowledge base. This repository contains all wiki entries, timeline pages, articles, and multilingual translations.

## Overview

This content is consumed by multiple targets:
- **[www.wheelofheaven.io](https://www.wheelofheaven.io)** - Main website (Zola static site)
- **[api.wheelofheaven.io](https://api.wheelofheaven.io)** - JSON API endpoints

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
# In www.wheelofheaven.io
git submodule add git@github.com:wheelofheaven/data-content.git content

# Update to latest
git submodule update --remote content
```

## Contributing

1. Fork this repository
2. Create a branch for your changes
3. Submit a pull request

See [Contributing Guidelines](https://www.wheelofheaven.io/contributing) for details.

## License

CC0-1.0 (Public Domain)
