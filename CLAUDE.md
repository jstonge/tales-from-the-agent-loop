# Working conventions

## Mark what Claude wrote

Anything Claude produces in this vault sits in a `[!claude]` callout, so a
reader can tell at a glance whose words they're reading — orange, with a bot
icon, styled by `.obsidian/snippets/claude-callout.css`. Reading notes use
`> [!claude] Claude summary`; generated sections of a synthesis note use
`> [!claude] Claude survey` as a banner above the block. The rule is not the
exact wording — it's that no unlabelled prose in this vault should be Claude's.

The snippet has to be enabled once per machine: Settings → Appearance → CSS
snippets. Without it the callout still renders, just in the default blue. On
GitHub it degrades to a plain blockquote showing the literal `[!claude]`.

This matters more than it looks. Two people are writing here to decide what to
build, and an unattributed paragraph silently becomes something "we think". If
a section is assembled rather than argued, say so and let it be argued with.

Sections under an `### <author name>` heading are that person's, always. Claude
never writes there, and never flips `status:`.

## Tables for surveys

When a synthesis note surveys several things side by side, default to a table —
it's for scanning and comparing, which is what a landscape is for. Name the
columns in the note so they can be challenged.

Tables compress, and the evidence is usually what gets squeezed out. When a
claim is load-bearing — a benchmark number, a specific mechanism — keep a prose
section below the table rather than losing it to a cell.

## Where notes live

- vault root — your own synthesis notes, written across sources
- `reading/` — one note per source, made by `bin/note`
- `who/` — people and organisations: who they are and what they've made
- `sources/` — archived full text of what was read; nobody's words but the author's

`bin/note` routes on `--template`, so a new shape is a template file plus an
entry in `FOLDERS`. Entity notes get no `### <author>` heading — they're shared
reference, not anyone's take.
