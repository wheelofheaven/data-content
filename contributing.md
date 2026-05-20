+++
title = "Contributing"
description = "Five ways to contribute to Wheel of Heaven — discussion, translation, content corrections, code, financial support. The project is open-source and welcomes serious engagement, including disagreement."
template = "info-page.html"

[extra]
claim_type = "direct"
editorial_pass = "2026-05"
cta_title = "Repository on GitHub"
cta_text = "The corpus, the site infrastructure, and the contribution guidelines all live in the public repository. Pull requests, issues, and translation work are welcomed there."
cta_url = "https://github.com/wheelofheaven"
cta_label = "Open the GitHub organization"
cta_external = true
+++

Wheel of Heaven is open-source under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) and welcomes contributors. The project is conducted in the first-person singular voice of one author, but the surrounding work — translation, editing, infrastructure, public discussion — benefits from many hands.

Contributors are not required to agree with the project's framework. Critical engagement is welcomed.

## Before you start

Read the [Code of Conduct](/code-of-conduct/). Participation in the project's public spaces — Discussions, issues, pull requests — assumes it.

Skim the [FAQ](/faq/), especially the entries on the working hypothesis, the source families, and how the project handles claim types. These give the context that makes most contributions easier.

## Ways to contribute

### Discussion and questions

The [GitHub Discussions](https://github.com/orgs/wheelofheaven/discussions) are the project's main public forum. Honest questions, substantive objections, alternative readings, and new sources are all welcomed there. Threads sometimes feed directly back into the corpus — a sharp question may end up reflected in a wiki entry or an FAQ answer.

### Translation

The site is published in nine languages, with English as the source. Translations are derived from the English original by hand and by tool, with editorial review where possible. Additional languages are welcomed; existing translations can always be improved.

If you are interested in translating, open a Discussion thread or an issue describing the language and scope. The project will provide the source material, the glossary of project-specific terms, and the style guide. The [Translations guide](https://docs.wheelofheaven.world/contributing/content/translations/) at docs.wheelofheaven.world documents the workflow, the glossary, and per-language conventions (formal/informal address, punctuation, RTL handling for Hebrew).

### Content corrections and suggestions

If a page on the site is factually wrong, has a broken link, misquotes a source, or misrepresents a scholarly position, the project would rather know than not. Open an issue on the [repository](https://github.com/wheelofheaven) with the page URL and the specific correction.

Interpretive disagreements — where you read a source differently than the corpus does — belong in Discussions, not in issues. The project welcomes them, but they are a different kind of contribution than a factual correction.

### Code and infrastructure

The site is a Zola-built static site with a Tera template theme ([Bifrost](https://github.com/wheelofheaven/bifrost)) and SCSS styles. The build runs on a public CI pipeline. Pull requests are welcome for bug fixes, accessibility improvements, performance work, and small features that fit the project's scholarly register.

For setup, conventions, the multi-repo project map, and theme/pipeline guides, see the developer documentation at [docs.wheelofheaven.world](https://docs.wheelofheaven.world) — start with the [Quickstart](https://docs.wheelofheaven.world/getting-started/quickstart/) for a five-minute local preview, or [Local Setup](https://docs.wheelofheaven.world/contributing/dev/local-setup/) for the full multi-repo environment.

For larger changes — visual redesigns, navigation restructuring, new content sections — open a Discussion first.

### Financial support

The project is currently funded entirely out of pocket by the author. Voluntary contributions through [Open Collective](https://opencollective.com/wheelofheaven) go toward hosting, infrastructure, and translation work. The CC0 license means the content cannot be monetized exclusively by anyone, including the project itself — financial support is genuinely voluntary and goes only to running the project.

## What contributions look like in practice

A good contribution names what it is changing, why, and on what basis. A pull request that fixes a broken link in a wiki entry needs a one-line description. A pull request that revises a substantive reading needs more — at minimum, the source for the new reading and a paragraph on why it improves on the current one.

The project's editorial standards apply to contributions: scholarly register, source-aware, claim type labelled honestly. The [content guides at docs.wheelofheaven.world](https://docs.wheelofheaven.world/contributing/content/overview/) describe these in detail — per-content-type pages for [wiki entries](https://docs.wheelofheaven.world/contributing/content/wiki-entry/), [Articles](https://docs.wheelofheaven.world/contributing/content/article/), and [Newsroom Dispatches](https://docs.wheelofheaven.world/contributing/content/newsroom-dispatch/), plus the [editorial-passes primer](https://docs.wheelofheaven.world/contributing/content/editorial-passes/) on `claim_type` and `editorial_pass`.

If you are not sure whether a contribution fits, open a Discussion first. The author will say so directly, and may suggest a better shape for the contribution. There is no penalty for asking.
