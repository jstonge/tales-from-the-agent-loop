---
name: vault-synthesis
description: Build a synthesis note at the vault root that surveys what's in reading/ — most often "which harnesses are out there and what do they do", but equally a note comparing two approaches or pulling together everything on one theme. Use this whenever the user asks what tools or systems the vault covers, wants a landscape or overview or state-of-play, asks to compare several things they've read about, or wants to pull scattered reading notes together into one place. Distinct from vault-note, which turns a single URL into a single reading note.
---

# Vault synthesis

A reading note answers "what does this source say". A synthesis note answers
"what's out there, and what is it". This builds the second from the first.

`bin/synth` assembles the skeleton; you write the prose. That division is the
same one `bin/note` uses, and for the same reason: the tool can group notes
deterministically, but only you can read them and say what a thing actually is.

## The loop

**1. See what you have.**

```sh
bin/vault-index
```

The `BY HARNESS` block is the shape of the answer. A harness covered by one
`repo` note is a thinner claim than one covered by `docs, repo, video` — say so
later rather than presenting both with equal confidence.

**2. Scaffold.**

```sh
bin/synth --slug current-harnesses --topic "harness landscape"
bin/synth --slug minimal-vs-batteries --harness pi,deepagents,teensycode
```

With no `--harness` it takes every harness in the vault. Pass a subset when the
note is an argument about particular ones rather than a survey of all.

You get a `## Harnesses` section, one `###` per harness, each listing its
reading notes with their one-line gists and a `<!-- what it does -->` marker.

**3. Read the notes, then replace each marker.**

Open the reading notes listed under each harness — the gists are a pointer, not
a source. Replace each marker with two or three sentences:

- What it is in one clause: who makes it, what layer it sits at.
- What it actually gives you — the capabilities, concretely. "Subagents,
  virtual filesystem, human-in-the-loop" beats "a rich feature set".
- Where it sits relative to the others. The value of a landscape is the
  contrasts; a list of independent blurbs is just the index with more words.

Keep each one short enough to scan. If a harness deserves more than a
paragraph, that's a reading note or its own synthesis note.

**4. Say what the survey doesn't cover.** Note harnesses you know exist but
have no reading note for, and harnesses whose coverage is thin. A landscape
that doesn't mark its own edges reads as complete when it isn't.

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
`[[wikilink]]` under an existing one. Check `bin/vault-index` against the note
to see what's drifted.
