+++
title = "As Foolish to Search for the Beginning"
description = "The canon says looking for time's beginning is a category error. In 2025–26, JWST keeps finding a cosmos too old, too soon — and the Big Bang's beginning keeps receding."
template = "articles-page.html"
date = 2026-07-11
draft = true

[extra]
claim_type = "speculative"
editorial_pass = "2026-05"
article_type = "explainer"
category = "Cosmology"
author = "Zara Zinsfuss"
author_slug = "zara-zinsfuss"
summary = "SCAFFOLD — broad strokes only, to be written out later in 2026. The temporal companion to 'The Infinite in Both Directions.' Where that Explainer argues the cosmos is infinite in scale, this one argues it is infinite in time: it has no beginning to find. The spine is the growing observational strain on the Big Bang — JWST's 'impossible early galaxies' (MoM-z14 at ~280 million years, hyper-mature clusters like XLSSC 122 at cosmic noon), reported galaxy-spin anisotropy, and the revival of cyclic, bouncing, and black-hole ('Schwarzschild') cosmologies that dissolve the singular origin. Read against the canon's flat refusal to look for a first moment — 'It is as foolish to search for the beginning of the universe in time as it is to search for the beginning of space' — the article argues these are not a crisis for the canon but a slow drift of mainstream physics toward a shape the canon has always held. It labels that convergence reading speculative in the project's own sense, keeps the science measured (bounce and black-hole cosmology are minority proposals, not consensus), and lets a defender of standard ΛCDM cross-examine the result."
keywords = ["Big Bang", "infinity", "temporal infinity", "eternal universe", "cyclic cosmology", "bounce cosmology", "black hole cosmology", "MoM-z14", "impossible early galaxies", "JWST", "cosmological principle", "Elohim hypothesis"]

# —— REFERENCE SCAFFOLD ——
# Seeded from the source video (Territory, 10 Jul 2026) chased back to primaries,
# plus canon anchors and in-corpus cross-links. ALL primary citations below are
# provisional and MUST be verified (authors, journals, arXiv IDs, dates) before
# publish. Six-source minimum NOT yet audited — see the checklist note in the body.
references = [
    # — Canon: the temporal-infinity warrant —
    { id = "the-book-which-tells-the-truth", locator = "Chapter 5, 'The End of the World' (¶57, 'Mankind, a disease of the universe' — 'in both directions, it is infinite')" },
    { id = "extraterrestrials-took-me-to-their-planet", locator = "Chapter 2, 'The Second Encounter' — 'Neither God nor Soul': 'nothing is lost, nothing is created, everything is transformed'; the centerless universe" },
    { title = "Let's Welcome the Extra-terrestrials — 'Who Created the Creator of the Creators?' ('It is as foolish to search for the beginning of the universe in time as it is to search for the beginning of space'; 'Everything is eternal, be it in the form of matter or energy')", author = "Claude Vorilhon (Raël)", date = "1979" },

    # — In-corpus cross-links (the pieces this article sits between) —
    { title = "Infinity — Wheel of Heaven wiki (the three dimensions; temporal infinity = no beginning, no end)", author = "Wheel of Heaven", date = "2026" },
    { title = "The Infinite in Both Directions — Wheel of Heaven Explainer (the spatial/hierarchical sibling to this piece)", author = "Zara Zinsfuss / Wheel of Heaven", date = "2026" },
    { title = "Cosmic Chain — Wheel of Heaven wiki (civilizations seeding civilizations without a first link)", author = "Wheel of Heaven", date = "2026" },

    # — The observational strain (VERIFY EVERY FIELD) —
    { title = "MoM-z14: a luminous galaxy at z≈14.4 (~280 Myr after the Big Bang) — arXiv:2505.11263 [VERIFY authors, venue: Naidu et al.?]", author = "TBD", date = "2025" },
    { title = "XLSSC 122 — strong-lensing mass of a mature galaxy cluster at z≈2 / cosmic noon (AAS-reported) [VERIFY paper + IOP/MNRAS ref from video description]", author = "TBD", date = "2025" },
    { title = "'Impossible early galaxies' — too-massive too-early candidates in JWST CEERS [VERIFY: Labbé et al. 2023, Nature; Boylan-Kolchin 2023, Nat. Astron.]", author = "TBD", date = "2023" },
    { title = "Asymmetry in galaxy spin directions in JWST fields [VERIFY: Shamir 2025, MNRAS — the anisotropy claim, and note it is contested]", author = "TBD", date = "2025" },

    # — The cyclic / bounce / black-hole family (minority proposals — label as such) —
    { title = "Conformal Cyclic Cosmology (aeons without a first) — 'Cycles of Time'", author = "Roger Penrose", date = "2010" },
    { title = "The cyclic / ekpyrotic universe", author = "Paul J. Steinhardt & Neil Turok", date = "2002" },
    { title = "Universe in a black hole / Einstein–Cartan torsion big-bounce [VERIFY: Popławski, Phys. Lett. B / Astrophys. J.]", author = "Nikodem Popławski", date = "2010" },
    { title = "Cosmological natural selection ('The Life of the Cosmos') — black holes as universe-producers", author = "Lee Smolin", date = "1997" },

    # — Critical / skeptic voice (the cross-examination) —
    { title = "[GATHER] A robust defense of ΛCDM: the JWST 'crisis' as resolvable within the standard model (dust/AGN/IMF, photometric-z pitfalls, homogeneity surveys). Candidate: the SDSS/WiggleZ homogeneity results already cited in the sibling article + a 2024–25 rebuttal review.", author = "TBD", date = "TBD" },
]
+++

<!--
════════════════════════════════════════════════════════════════════════
EDITOR'S SCAFFOLD — NOT FOR PUBLICATION AS-IS. draft = true.
Written 2026-07-11. Broad strokes to be filled out later in 2026.

Provenance: prompted by a Territory YouTube explainer (10 Jul 2026,
"...JWST / MoM-z14 / XLSSC 122 / black-hole cosmology"). The video is a
TERTIARY roundup — do NOT cite it. It is only the pointer that sent us to
the primaries listed in the reference scaffold above.

Relationship to existing corpus:
  • This is the TEMPORAL companion to `the-infinite-in-both-directions`
    (which owns spatial/hierarchical infinity via fractal cosmology).
    Cross-link them as siblings; do not re-argue the fractal case here.
  • Anchor claim lives in `wiki/infinity.md` (temporal dimension) — this
    article is the observation-driven ARGUMENT for that wiki claim.
  • Cross-link `mass-effect`, `cosmic-chain`, `four-levels` where natural.

Claim discipline (from .claude/rules/content-editing.md):
  • "The cosmos has no beginning in time" = FRAMEWORK claim (canon-explicit,
    mainstream rejects). State it directly, labelled as the canon's premise.
  • "Mainstream physics is drifting toward the canon's shape" = SPECULATIVE.
    This is the article's thesis and its honest label. Do not oversell.
  • JWST anomalies, bounce/black-hole cosmology = SCIENTIFIC claims — keep
    hedged and MEASURED. Bounce and black-hole cosmology are MINORITY
    proposals; the honest claim is "the anomalies keep the door open," NOT
    "science now agrees the Big Bang is dead."
  • Skeptic voice gets its own section, in its own voice.

TODO before promoting out of draft:
  [ ] Verify every primary citation (authors / venue / arXiv / date).
  [ ] Run the six-source audit (canon ✓, ancient primary — N/A? justify,
      scholarly ✓, scientific ✓, comparative tradition — steady-state /
      other eternal-universe cosmologies?, critical ✓). Note: a cosmology
      Explainer may legitimately swap "ancient primary" for a second
      scientific/historical source — flag the deviation explicitly.
  [ ] Confirm the anisotropy claim is presented as CONTESTED (Shamir's
      spin-asymmetry result is disputed; don't lean on it hard).
  [ ] Decide final title/slug. Current: canon-quote fragment. Alt working
      titles: "Too Old, Too Soon"; "The Beginning That Keeps Receding".
  [ ] De-slop pass + AI-idiom read-back before sign-off (antithesis tic,
      reader-directives, cutesy one-liners).
════════════════════════════════════════════════════════════════════════
-->

## The beginning that keeps receding

<!-- HOOK. Open on the concrete 2025–26 observations, plainly stated: JWST
keeps finding a universe more built-up, earlier, than the standard timeline
allows. MoM-z14 shining at ~280 Myr; a fully-assembled, dark-matter-heavy
cluster (XLSSC 122) at an epoch that was supposed to be still assembling.
The pattern, not any single object, is the story: every time the model is
surprised, the fix pushes structure formation earlier — the "beginning"
of maturity keeps sliding back toward the beginning of time. End the hook
on the canon's flat line: it is as foolish to look for time's first moment
as for space's first inch. State the thesis in one sentence. -->

## What the canon actually claims about time

<!-- Lay out the FRAMEWORK claim cleanly, sourced. Yahweh to Raël: matter is
eternal — "nothing is lost, nothing is created, everything is transformed";
the universe has no center and no edge; and searching for a temporal
beginning is a category error on par with searching for the northmost point
past the North Pole (the wiki's own analogy). Distinguish this from the two
things it is NOT: (1) not a claim that "nothing happened 13.8 Gyr ago" — a
local expansion event is compatible with an eternal cosmos; (2) not
mathematical/Cantorian infinity. Cross-link `wiki/infinity.md` and the
sibling article. Keep it tight — the wiki does the heavy lifting. -->

## The standard model's own beginning problem

<!-- Fair, MEASURED exposition of ΛCDM: finite age, cosmic horizon,
cosmological principle, gravity as the slow patient engine. Then the strain,
honestly scoped: the "impossible early galaxies" literature (2023 onward),
MoM-z14, mature clusters at cosmic noon, high N/C chemistry echoing globular
clusters at 280 Myr. Be explicit that "surprising" ≠ "refuted": the field's
own framing is "something is missing," not "the Big Bang is wrong." That
honesty is the section's credibility. -->

## When the singularity dissolves

<!-- The revival of origin-free cosmologies, presented as MINORITY but
serious physics — not fringe, not consensus. Penrose's conformal cyclic
cosmology (aeons, no first). Steinhardt–Turok cyclic/ekpyrotic. Torsion /
Einstein–Cartan big-bounce (Popławski): at extreme density spin generates a
repulsion that replaces the singularity with a rebound — a bounce, not a
bang. Black-hole ("Schwarzschild") cosmology: our universe as the interior
of a black hole in a parent universe; each black hole a doorway to a baby
universe (tie to Smolin's cosmological natural selection and the fine-tuning
angle). The through-line: each of these REMOVES the first moment. That is
the shape the canon has always drawn. -->

## The convergence — and its honest label

<!-- THE THESIS, and the place to be most careful. The argument is NOT
"science proves the canon." It is: the canon committed early and flatly to a
beginningless cosmos; mainstream cosmology, under observational pressure, is
independently generating models with the same property. That convergence is
SPECULATIVE (project sense) — a re-framing that goes beyond any single
source. Name what would falsify or weaken it (e.g. the anomalies resolve
inside plain ΛCDM with better dust/IMF modeling). Do not flatten the
distinct traditions of thought into "the same"; note where the physics and
the canon genuinely differ (the canon's eternity is also hierarchical/
fractal and value-laden — see the sibling article — which no bounce model
implies). -->

## The cross-examination

<!-- Give the standard-model defender the floor, in their own voice. The
"crisis" is oversold; photometric redshifts get revised; brightness excess
has mundane fixes (AGN, top-heavy IMF, stochastic star formation); the
homogeneity surveys (SDSS LRG, WiggleZ) still show a transition to
smoothness that fractal/anisotropy claims must answer to; the spin-asymmetry
result is contested and may be a measurement artifact. Let this land
without immediately rebutting it — the article's honesty is the point.
Then the measured close: none of this restores a NECESSARY beginning; it
only shows the beginning is not yet forced by the data. That is all the
canon needs to remain live. -->

## What a beginningless cosmos is for

<!-- Land the ethical/orientational payload, briefly, tying to the Four
Levels and the Infinity framework: why the canon cares that time has no
first moment (it dissolves the creator-of-the-creator regress; it locates
meaning in the chain rather than an origin; it reframes "before the Big
Bang?" as a malformed question). Echo the sibling article's closing move
without repeating it. Callback to the opening image: the beginning of
maturity keeps receding because there is no beginning to reach. -->

## Further reading

<!-- Sibling: The Infinite in Both Directions. Wiki: Infinity; Fractal
Cosmology; Mass Effect; Cosmic Chain; Four Levels. External primaries once
verified. -->
