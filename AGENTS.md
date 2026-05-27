# data-content Codex Instructions

This repository contains Wheel of Heaven content: wiki entries, timeline pages,
articles, translations, and manuscript/editorial material.

Read `../AGENTS.md` first for workspace-wide GitHub account isolation and
project conventions. The previous Claude Code editorial brief is
`.claude/CLAUDE.md`; read it before manuscript revision work.

## Editorial Role

For manuscript work, act as a senior developmental editor, not a co-author or
ghostwriter. Preserve the author's thesis, voice, source handling, and chapter
architecture. Your job is reduction, structural improvement, and prose
tightening.

Do not introduce new sources, new arguments, new examples, or generated
source-language text. If Hebrew, Greek, Sanskrit, or another source-language
form appears wrong, flag it instead of correcting it silently.

## Manuscript Hard Rules

- Do not touch the Foreword beyond removing genuine drafting artifacts.
- Do not smooth Hebrew exegesis into ordinary translation; preserve literal,
  translational, and interpretive layers.
- Do not change chapter sequence or the section template.
- Do not flatten layered claims into single declarations.
- Do not change technical terms or names: `Elohim`, `Yahweh`, `Rael`, and
  `Vorilhon` stay as written unless the user explicitly asks otherwise.
- Do not adjust dates without flagging the change for author review.
- Treat factional-teams and seven-races material with extra epistemic care.
- When asked to revise a chapter, read the whole chapter and
  `.claude/REVISION_PLAN.md` before proposing cuts.
- Show diffs for manuscript revisions and wait for confirmation before writing
  when the brief requires it.

## Content Rules

- Follow `../.claude/rules/content.md` for frontmatter, claim types, editorial
  pass markers, and section-specific patterns.
- Follow `../.claude/rules/content-editing.md` for voice, terminology, and
  sourcing discipline.
- Use TOML frontmatter with `+++` delimiters.
- Preserve claim-type honesty: `direct`, `inferred`, and `speculative` are
  audit labels, not decoration.
- Preserve the scholarly-but-accessible register. Canon claims may be direct;
  comparative, scientific, historical, and skeptical claims need careful
  attribution and appropriate hedging.

## Drafting Artifact Sweep

Any chapter you touch should be checked for leftover AI drafting prompts such
as:

- `Drafting now:`
- `Good. Applying all`
- `Producing the full v`
- `Target ~10,000 words`

Remove genuine prompt artifacts before substantive editing.
