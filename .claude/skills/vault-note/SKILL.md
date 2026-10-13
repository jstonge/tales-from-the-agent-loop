---
name: vault-note
description: Create or fill in a reading note in this Obsidian vault from a URL — archives the source to sources/, reads it, and writes an attributed summary via bin/note. Usually invoked directly as `/vault-note <url> [kind]`, where kind is one of post, course, video, paper, docs, repo, book. Also use it whenever the user drops a bare URL with little or no instruction, says they want to save/add/note an article, blog post, paper, course, GitHub repo, or YouTube video, asks to summarize something for the vault, or asks to fill in notes that are missing summaries. A bare URL in this vault almost always means "make a note for this."
---

# Vault note

Turn a URL into a finished note in this vault. The user hands you a link; you
come back with a note whose frontmatter is filled, whose source is archived
locally, and whose summary you actually wrote after reading the thing.

`bin/note` does all the file writing. Your job is the part it can't do: read the
source and say something true about it.

## Invocation

Called as `/vault-note [url] [kind]`. Both arguments are optional and may arrive
in any phrasing — a bare link, a link plus "it's a course", or nothing at all.

**Open by stating the kind and the alternatives.** The kind is guessed from the
URL and the guess is sometimes wrong, so make it cheap to correct by showing the
menu up front rather than burying the choice in frontmatter the user has to go
read:

> Kind: **course** (inferred). Available — `post` · `course` · `video` · `paper`
> · `docs` · `repo` · `book`. Tell me if that's wrong and I'll re-run.

Then continue without waiting. Blocking on confirmation costs the user a round
trip for a field that's usually right and takes seconds to fix if it isn't.

**If no URL was given**, ask for one and show the same list, so they can answer
both in a single message:

> Which URL? And what kind is it — `post` · `course` · `video` · `paper` ·
> `docs` · `repo` · `book`? I'll infer the kind from the link if you'd rather
> not say.

For a `book` there may be no URL at all; that's expected, see **Kind** below.

## The loop

**1. Archive and read before you write anything.**

```sh
bin/note <url> --slug <slug> [--kind <kind>] [--tags a,b]
```

This writes `sources/<slug>.md` (the full article, or a flattened transcript for
video) and creates the note. Then read `sources/<slug>.md` — the whole thing, not
the first screen. The summary is the only part of this job that requires
judgment, and you can't exercise it on a page you skimmed.

**2. Write the summary and run it back in.**

```sh
bin/note <url> --slug <slug> --force --no-archive <<'EOF'
Your summary.
EOF
```

`--no-archive` because step 1 already fetched it; re-fetching wastes a round
trip. `--force` is safe here: re-running edits the note in place rather than
rebuilding it from the template, so the user's frontmatter, tags, and anything
they wrote under `## Why do I bring this up?` survive, and an existing
`Claude summary:` block is replaced rather than duplicated.

Summary text goes in on stdin so apostrophes and quotes don't have to survive
shell escaping. Use a quoted heredoc (`<<'EOF'`) so backticks and `$` stay literal.

## Two kinds of note

Reading notes live in `reading/`, one per source, and are what this skill makes.
The vault root is for the user's own synthesis notes — their thinking across
several sources, made from `my-templates/synthesis.md`. Those have no
`sourceUrl`, no archive and no `kind`, and `bin/note` routes on the template:
`--template reading` (the default) writes to `reading/`, anything else writes to
the root.

Don't write synthesis notes unprompted. They're the user's argument, not a
summary, and the whole point of the split is that one is sourced and the other
is thought. If asked to start one, scaffold it with
`bin/note --slug <topic> --template synthesis` and leave the thinking to them.

## Choosing the slug

Shape it `<author-or-source>-<short-title>`, kebab-case, no date — matching
`wickham-what-is-an-agent`, `anthropic-building-effective-agents`. The slug
becomes both the filename and the H1, so it should read as a title, not an ID.

## Writing the summary

Three to five sentences. The block is labeled `Claude summary:` and rendered as
a blockquote, so it is explicitly yours — you can make judgments, and you should.
A summary that only restates the table of contents is worse than useless, because
the user already has the archived copy sitting next to it.

What earns its place:

- The actual claim, in the author's strongest form — not "discusses agents" but
  what they say an agent *is*.
- What's load-bearing versus decorative. If a post lists six tools and says only
  three matter, that's the sentence worth keeping.
- Honest friction: a vendor's course recommending the vendor's stack, a video
  whose claims rest on a demo, a post whose tooling section is stale. Say it
  plainly and move on; don't editorialize past what the source supports.
- Caveats about the archive itself — if it's a course index rather than the
  course, or a transcript with gaps, note it in the summary so the vault doesn't
  overclaim.

Avoid marketing verbs: no "dives into", "explores", "unpacks", "delves".

**Connect it to what's already here.** One call gives you the whole vault —
the tags already in use, and a one-line gist of every note:

```sh
bin/vault-index
```

Run it once, before writing. Reuse a tag that already exists rather than coining
a synonym, and if the source continues, contradicts, or overlaps a note in that
list, link it with `[[note-name]]`. Nothing else in this pipeline adds those
cross-references, so if you skip it they don't get made.

Read a neighbouring note in full only when the index line leaves you genuinely
unsure whether there's a link worth making — the gist is usually enough, and
reading every file gets slower every time the vault grows.

## Attribution

The `> [!claude] Claude summary` callout is not decoration. See
`CLAUDE.md`: no unlabelled prose in this vault is Claude's. If you add anything
to a note beyond the summary, label it the same way.

## Leave the user's side of the note alone

`## Why do I bring this up?` is theirs. Never write in it, even when you have an
opinion that would fit — the whole point of the attributed-blockquote split is
that the reader can tell at a glance which thoughts are whose.

That section is split further by an `### <author name>` heading per person, so
two collaborators can write in one note without editing the same lines (which is
what produces sync conflicts). `bin/note` seeds a heading for whoever creates the
note and never touches the section again. Each contribution under a heading is
stamped with the date it was written, so a take can evolve without rewriting
what was thought earlier:

```md
### Jonathan St-Onge

**2026-10-13** — first impression
**2026-11-02** — revisited after actually trying it
```

If someone asks you to record a take on their behalf, write it under their
heading in that form, creating the heading if it's absent — and never under
someone else's. Use the date they wrote it, not the note's creation date. The same goes for `status:` — see below.

## By

`--by "<name>"` records who made the source, as a wikilink into `who/`.
Comma-separated when there's more than one. Check `bin/vault-index` for the
existing spelling before adding a name — `LangChain` and `langchain` would split
the same author in two.

If `who/<name>.md` doesn't exist yet, the link dangles until someone writes it.
That's fine and is how the folder grows; mention it to the user rather than
leaving it silent.

## Harness

Set `--harness <name>` when the source is about a nameable system: `deepagents`,
`pi`, `claude-code`, `teensycode`. Comma-separated when a source covers more than
one (`--harness pi,claude-code` for a comparison). Leave it empty when there's no
named system. Check the index for an existing spelling before coining a variant.

## Status, addedBy and recBy

Every note starts `status: unread`. Don't flip it to `read` on the user's behalf
— reading an archived copy to write the summary isn't the user reading it, and
that field is how they track their own queue.

`addedBy` is filled automatically from `git config user.name` (falling back to
`whoami`), and is only written when the note doesn't already have one — so
re-running on a note a collaborator added won't reattribute it to you. Pass
`--added-by <name>` only when recording a note on someone else's behalf.

`recBy` is who pointed them at the source. Set it with `--set recBy=<url or
name>` only when the user says where it came from; there's no way to infer it.

## Kind

Inferred from the URL, so usually leave it alone: YouTube/Vimeo → `video`, arXiv
and `.pdf` → `paper`, `/academy/` and `/course/` → `course`, `docs.*` and
`/reference/` → `docs`, GitHub/GitLab/Codeberg hosts → `repo`, otherwise `post`.
Host-anchoring keeps `docs.github.com` as `docs` rather than `repo`. Pass
`--kind` when the URL lies — a course hosted at a plain blog path, say. `book` has no URL signature and the URL
argument is optional, so a book is `bin/note --kind book --slug ...` with no link.

## Known rough edges

Report these rather than papering over them:

- **Video transcripts are auto-captions.** Expect mistranscriptions — "Claude
  Code" routinely comes through as "clawed code" or "cloud code". Correct
  silently while reading, but never quote the transcript verbatim as if exact.
- **PDFs don't archive.** `kind: paper` infers fine, but a direct `.pdf` link
  fails extraction and leaves the note without a `localCopy:`. Say so.
- **Some pages archive only partially** — a course index instead of the modules,
  a paywalled post's preview. Check the word count against what you'd expect and
  tell the user when the archive is thin.

## Filling in notes that lack summaries

To find them: a note is missing a summary when there's nothing between the `# `
heading and `## Why do I bring this up?`. Work through them one at a time with
the same loop — archive, read, summarize. Existing notes may already have the
user's own prose under `## Why do I bring this up?`; that stays untouched.
