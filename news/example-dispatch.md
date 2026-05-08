+++
title = "Example Dispatch: How a Newsroom Entry Reads an Event"
description = "Demonstrates the Newsroom dispatch format — a short, dated piece that reads a current event through the Wheel of Heaven canon."
date = 2026-05-08
template = "news-page.html"

[extra]
event_date = 2026-05-07
event_type = "announcement"
claim_type = "inferred"
summary = "An example Dispatch showing the structure: lede, canon angle, context, sources. Replace this with a real event when the section goes live."
canon_links = [
    { title = "Elohim", path = "/wiki/elohim/" },
    { title = "Ancient Astronaut Theory", path = "/wiki/ancient-astronaut-theory/" }
]
sources = [
    { title = "Source headline goes here", url = "https://example.com/source", outlet = "Outlet Name", date = "2026-05-07" }
]
+++

## What happened

One or two short paragraphs stating the event in plain terms. No editorial yet — just the facts of what was announced, discovered, observed, or commemorated. Link to the primary source(s) inline where helpful.

## The canon angle

This is where the Dispatch earns its keep. Read the event through the Wheel of Heaven frame: which canon claim does it touch, sharpen, complicate, or echo? Two to four paragraphs, scholarly register. Canon claims can be stated directly; comparative and scientific claims stay hedged per `.claude/rules/content-editing.md`.

## Context

Optional. Where the event sits in a longer story — prior reporting, related discoveries, the relevant precessional age, the wiki entries it touches.

## Sources

The primary news source(s) that prompted the Dispatch are listed in the `sources` frontmatter array and rendered automatically in the footer. Use this section only for additional context citations not already in `sources`.
