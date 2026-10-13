# `bin/note`

Renders a note from `my-templates/reading.md` into `reading/` and archives the source to
`sources/` so the note survives link rot. It does no thinking of its own — ask
Claude to read the page and call it, or use the `/vault-note` skill.

```sh
bin/note https://example.com/post \
    --slug author-short-title \
    --kind post \
    --harness deepagents \
    --tags agent-patterns <<'EOF'
Two or three sentences of summary.
EOF
```

The summary comes in on stdin so it never has to survive shell quoting, and
lands under the H1 as an attributed blockquote:

```md
Claude summary:

> Two or three sentences of summary.
```

so it always reads as a draft someone else wrote, not as your own note.
`--slug` is both the filename and the H1. `## Why do I bring this up?` is left
for you, subdivided by an `### <author>` heading per person:

```md
## Why do I bring this up?

### Jonathan St-Onge

...

### A Colleague

...
```

Contributions are stamped with the date they were written — `**2026-10-13** —
your take` — so an opinion can change over months without erasing the earlier
one. Obsidian's Templates plugin has an **Insert current date** command
(`Settings → Hotkeys → "Insert current date"`) worth binding to a key.

Each of you only edits your own lines, which keeps Obsidian Sync and git from
producing conflict copies. `bin/note` seeds a heading for whoever creates the
note and never touches the section afterwards — a second author adds their own
heading by hand.

| flag | |
| --- | --- |
| `--slug NAME` | required; filename and H1, no `.md` |
| `--kind KIND` | `post` `course` `video` `paper` `docs` `repo` `book`; inferred from the URL |
| `--harness NAME` | which system the note is about; comma-separated for comparisons |
| `--tags a,b` | appended to the template's tags, deduped |
| `--added-by NAME` | who's adding the note; defaults to `git config user.name` |
| `--set KEY=VALUE` | set any frontmatter key, repeatable; adds the key if missing |
| `--template NAME` | a template in `my-templates/`, without `.md` (default: `reading`) |
| `--no-archive` | skip the `sources/` copy |
| `--force` | overwrite an existing note |

## Layout

`reading/` holds one note per source — what this tool makes. The vault root
holds your own synthesis notes, written from `my-templates/synthesis.md`:
no `sourceUrl`, no archive, no `kind`, just your thinking with links out to the
reading notes it draws on. `--template` routes between them, so

```sh
bin/note --slug harness-design-space --template synthesis
```

scaffolds one at the root with the date and your name already filled in.
`sources/` holds the archived full text, kept out of both.

## Fields

`kind` is what the source *is*; it's inferred from the URL — YouTube and Vimeo
are `video`, arXiv and `.pdf` are `paper`, `/academy/` and `/course/` are
`course`, `docs.*` and `/reference/` are `docs`, GitHub, GitLab and Codeberg
hosts are `repo`, everything else is `post`. Repo detection is host-anchored, so
`docs.github.com` stays `docs`. `book` has no URL signature, so pass
`--kind book`; the URL argument is optional for exactly that case.

`harness` is which system a note is *about*, which `kind` can't express — a
video about Pi is still `kind: video`. Together they let notes be grouped by
system rather than only by source format. Leave it empty when there's no named
system.

`status` starts at `unread` and is yours to flip. `recBy` records who pointed
you at the source. `addedBy` is filled from `git config user.name` (falling back
to `whoami`) and is written only once — re-running on a note a collaborator
added won't reattribute it, and `--added-by` overrides when you're recording
something on someone else's behalf. Both are plain fields, so a new one is a line in
`my-templates/note.md` — the CLI picks it up with no code change, and
`--set KEY=VALUE` fills any key whether the template has it or not.

## Archiving

Shells out to `uvx trafilatura` for pages and `uvx yt-dlp` for YouTube, so
there's nothing to install. Video transcripts are flattened into timestamped
paragraphs; they're auto-captions, so expect transcription errors. The note
links the copy as `localCopy:`.

Re-running on a note that already exists edits it in place rather than
rebuilding it from the template: your frontmatter, your tags and anything you
wrote under `## Why do I bring this up?` survive, and an existing
`Claude summary:` block is replaced rather than duplicated.

`.claude/skills/vault-note/scripts/vault-index.py` prints the tag vocabulary,
the grouping by harness, and a one-line gist per note.
