+++
title = "Library: The First Audio Plays Are Live"
description = "As of June 13, 2026, The Book Which Tells the Truth ships as a multi-voice audio play in English, German, and French — and Extraterrestrials Took Me to Their Planet in English."
date = 2026-06-13
template = "news-page.html"

[extra]
event_date = 2026-06-13
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "The Wheel of Heaven library hosts its first multi-voice audio plays. The Book Which Tells the Truth (1974) is now available in English, German, and French, and Extraterrestrials Took Me to Their Planet (1975) in English. Each production casts a separate voice for the narrator, the in-scene Raël, and Yahweh — Yahweh's voice carrying a subtle hall reverb to mark his off-world origin — and opens with a scripted Audio Play Intro voiced by a neutral outside-the-fiction narrator. Intro scripts are ready in all nine project languages; per-language audio renders will follow."
canon_links = [
    { title = "The Book Which Tells the Truth", path = "/library/the-book-which-tells-the-truth/" },
    { title = "Extraterrestrials Took Me to Their Planet", path = "/library/extraterrestrials-took-me-to-their-planet/" },
    { title = "Elohim", path = "/wiki/elohim/" },
    { title = "Yahweh", path = "/wiki/yahweh/" }
]
sources = [
    { title = "Audio Play Pipeline (rendering chain)", url = "https://docs.wheelofheaven.world/contributing/dev/audio-play-pipeline/", outlet = "Wheel of Heaven docs", date = "2026-06-13" },
    { title = "Audio Play Cue Sheets (production scaffolding)", url = "https://docs.wheelofheaven.world/contributing/dev/audio-play-cue-sheets/", outlet = "Wheel of Heaven docs", date = "2026-06-13" },
    { title = "Listen index", url = "https://www.wheelofheaven.world/listen/", outlet = "Wheel of Heaven library", date = "2026-06-13" }
]
+++

## What shipped

As of June 13, 2026, the Wheel of Heaven library hosts its first multi-voice audio plays. *The Book Which Tells the Truth* (1974) is available as a full production in English, German, and French — three live renderings of Raël's foundational text in the languages it most needs to reach first. *Extraterrestrials Took Me to Their Planet* (1975), the immediate sequel, ships in English alongside it.

Each production is roughly three and a half hours of finished audio per language: per-paragraph TTS through ElevenLabs's multilingual model, treated per speaker, concatenated with timing-aware silences, with an ambient sound bed under the off-world scenes. The reader page's existing Listen button now picks up the prerecorded production silently when a manifest exists, while continuing to fall back to the in-browser studio engine for everything else in the corpus.

## The voice cast

A production-side decision baked into both books: a single voice plays Raël across his two temporal vantages — Raël-the-author writing after the encounters ended, and Raël-the-questioner inside the encounters — with the casting differentiated only by prosody defaults (slightly more stability on the in-scene questions). The voice the project ships with is **Phoenix**, a smooth English-library voice that handles all four languages natively through the multilingual model. The original casting was a French-accented voice; listener feedback flagged the accent as distracting outside French, and Phoenix replaced it.

*Yahweh* is voiced by **Jon — Natural Authority**, kept consistent across all four languages. Jon's tracks go through a per-speaker treatment pass that adds a subtle hall reverb plus a +3 dB low-shelf at 120 Hz — enough to mark the off-world origin sonically without disrupting intelligibility. The production cache keys both the raw render and the treated output on the source audio's full key, so a voice swap or text edit invalidates the treated layer cleanly. (An earlier bug in this scheme is why the first English render of TBWTT briefly shipped with the new voice on the raw audio but the *previous* voice on the treated concat. The cache-key fix is documented; the bug is closed.)

A third role belongs to the **AudioplayNarrator** — a neutral voice outside the audio play's fictional frame, who reads the scripted intro that precedes Chapter 1. The voice is **Jarnathan — Confident and Versatile**, deliberately untreated. Jarnathan is also the project-wide neutral Wheel of Heaven voice; any future non-book audio — metadata readers, announcements, site-level reads — will reuse him so the "voice of the site" stays consistent across projects.

## The intro

Both books open with a scripted Audio Play Intro: a one-minute opener voiced by Jarnathan that sits outside the fictional frame and tells the listener who is about to speak, when the encounters happened, and what the canon claim is. The intro is not part of the source text — it is the production's own framing.

The TBWTT intro is most distinctive on one point: it clarifies that the in-text "narrator" IS Raël writing after the fact, looking back from his perspective as author, and that the questions inside the dialogue are Raël-the-questioner in real time. The distinction is native to the Raëlian frame and easy for a passing listener to miss. The ETTMTP intro carries the parallel framing for the sequel: Raël as narrator after his return from the Elohim planet, and Yahweh as guide rather than off-scene teacher.

Intro scripts are language-keyed and live in each book's `audioplay/manifest.yaml`. All nine project languages — English, German, French, Spanish, Russian, Japanese, Korean, Simplified Chinese, Traditional Chinese — now carry intro text. The four current renders (TBWTT EN/DE/FR, ETTMTP EN) have those intros baked in; the remaining language renders will pick up the intros automatically when they run.

## The architecture

The production sits on three layers that the docs site documents in full. Per-paragraph TTS lives in `chapter-N.json` paragraphs, identified by speaker label. Production-side scene tags — which paragraphs play under an ambient bed — moved from inline JSON fields to `{slug}/audioplay/cues/cN.yaml` cue sheets, with a reader fallback that still honors inline tags on un-migrated books. Book-level production config (the intro, default pauses, future SFX cues) lives in `{slug}/audioplay/manifest.yaml`.

Editorial paragraph kinds — whether a paragraph is body text, a section title, or a continuation of a split quotation — live alongside the speaker label on the chapter JSON itself, because they are not production-only. The renderer reads them to add a longer pause before titles and to drop the inter-paragraph silence entirely on continuations, which is how the audio version of *Genesis X-32* — a verse split across two paragraphs in the source text — reads as a single utterance. The reader page uses the same `kind` field to render titles as headings and tighten continuations visually.

## What's next

ETTMTP in German and French are queued behind a verification render — the intros are ready, the texts have passed the audio-play script normalizer (citation tails restored, Roman numerals in surviving prose verbalized as Arabic digits, parenthetical scripture references stripped from speech and kept in the reader), and the cost runs roughly $60 per book per language. The other six site languages — Spanish, Russian, Japanese, Korean, Simplified and Traditional Chinese — sit behind the same gate: intros are written for both books, voice cast is already wired in the multilingual map, and the TTS sidecars lint clean.

A separate near-term lift is restoring the section headings inside *The Keys*, ETTMTP's third chapter. The print edition organizes the chapter under named sub-headings — Humanity, Birth, Education, Sensual Meditation, and the others — that were lost at ingestion. Reintroducing them from the print source upgrades both the reader page (the chapter currently scrolls as one block) and the audio render (each heading would get a section-break pause). It is editorial work, not production work, and is not blocking the existing renders.

Further out is the SFX layer — Phase 4 of the cue-sheet plan — which extends the per-chapter cue sheet to fire one-shot sound effects at scene boundaries and key narrative beats. The design is documented, the SFX library is empty, and shipping it is gated on a small editorial pass to choose which beats actually need a cue.

## Where to listen

- *The Book Which Tells the Truth*: [English](/library/the-book-which-tells-the-truth/), [German](/de/library/the-book-which-tells-the-truth/), [French](/fr/library/the-book-which-tells-the-truth/) — the Listen button surfaces on the book page once you reach it.
- *Extraterrestrials Took Me to Their Planet*: [English](/library/extraterrestrials-took-me-to-their-planet/).
- [The Listen index](/listen/) collects every published audio play and notes which languages each is rendered in.

The site service worker tracks asset versions, so a returning listener may need a hard refresh or close-and-reopen the tab to drop the previous cache.

---

*— Filed June 13, 2026, Wheel of Heaven editorial desk.*
