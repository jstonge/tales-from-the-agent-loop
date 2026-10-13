---
name: vault-synthesis
description: Build a synthesis note in `synthesis/` that surveys what's in reading/ — most often "which harnesses are out there and what do they do", but equally a note comparing two approaches or pulling together everything on one theme. Use this whenever the user asks what tools or systems the vault covers, wants a landscape or overview or state-of-play, asks to compare several things they've read about, or wants to pull scattered reading notes together into one place. Distinct from vault-note, which turns a single URL into a single reading note.
---

# Vault synthesis

A reading note answers "what does this source say". A synthesis note answers
"what's out there, and what is it". This builds the second from the first.

These land in `synthesis/`, not the vault root. The root is for the user's own
thinking — written, not compiled — and a generated survey sitting there would
blur the one distinction the layout exists to keep.

`tools/synth` assembles the skeleton; you write the prose. That division is the
same one `tools/note` uses, and for the same reason: the tool can group notes
deterministically, but only you can read them and say what a thing actually is.

## The loop

**1. See what you have.**

```sh
tools/vault-index
```

The `BY HARNESS` block is the shape of the answer. A harness covered by one
`repo` note is a thinner claim than one covered by `docs, repo, video` — say so
later rather than presenting both with equal confidence.

**2. Scaffold.**

```sh
tools/synth --slug current-harnesses --topic "harness landscape"
tools/synth --slug minimal-vs-batteries --harness pi,deepagents,teensycode
```

With no `--harness` it takes every harness in the vault. Pass a subset when the
note is an argument about particular ones rather than a survey of all.

You get a `## Harnesses` section under a `> [!agent] <name> survey` banner: one
table row per harness, with `Harness` and `Covered by` filled in and the `What
it is` and `The distinctive move` cells left blank.

**3. Read the notes, then fill each row.**

Open the reading notes listed under `Covered by` — the links are a pointer, not
a source. Fill the two empty cells:

- `What it is` in one clause: who makes it, what layer it sits at.
- `The distinctive move` — the one thing it does differently from the rest.
  "You subtract capabilities with `excluded_tools` rather than add them" beats
  "a rich feature set", and it's what makes the landscape read as contrasts
  rather than a list of independent blurbs.

The table is for scanning, so it squeezes evidence out. When a row rests on
specific detail — a benchmark number, a named mechanism — keep a prose
paragraph below the table rather than losing it to a cell. If a harness
deserves more than a paragraph, that's a reading note or its own synthesis.

**4. Say what the survey doesn't cover.** Note harnesses you know exist but
have no reading note for, and harnesses whose coverage is thin. A landscape
that doesn't mark its own edges reads as complete when it isn't.

## Attribution

Everything `tools/synth` generates sits under a `> [!agent] <name> survey`
banner, and anything you add to those sections stays under one. See `AGENTS.md` — the rule
across this vault is that no unlabelled prose is Claude's, because two people
are writing here and an unattributed paragraph quietly becomes something "we
think".

The survey defaults to a table, which is right for scanning and comparing. Watch
what the cells squeeze out: when a claim rests on specific evidence — a
benchmark number, a named mechanism — keep a prose section below the table
rather than losing it.

## What stays yours

`## Thinking` is the user's, under their `### <name>` heading with dated
entries. Never write there — the harness descriptions are reportage, that
section is argument, and the whole point of the split is that a reader can tell
which is which.

If the survey makes a conclusion obvious — one approach dominates, two are
converging — put it in the harness descriptions as observation, or say it to
the user in chat. Don't put it under their name.

## Keeping it current

Re-running with `--force` rebuilds the skeleton from the current notes, which
drops the descriptions you wrote. Prefer editing the note in place when new
reading notes land: add the `###` section for a new harness, append the new
`[[wikilink]]` under an existing one. Check `tools/vault-index` against the note
to see what's drifted.
