# Working conventions

## Mark what an agent wrote

Anything an agent produces in this vault sits in an `[!agent]` callout, so a
reader can tell at a glance whose words they're reading — orange, with a bot
icon, styled by `.obsidian/snippets/agent-callout.css`. The title names the
agent that actually wrote it: `> [!agent] Claude summary` on a reading note,
`> [!agent] Claude survey` as a banner on a generated section. `bin/note` takes
the name from `$VAULT_AGENT`, defaulting to `Claude`, so set it once if you work
with something else:

```sh
export VAULT_AGENT=Codex
```

The rule is not the exact wording — it's that no unlabelled prose in this vault
is an agent's, and that the label doesn't claim the wrong one.

The snippet has to be enabled once per machine: Settings → Appearance → CSS
snippets. Without it the callout still renders, just in the default blue. On
GitHub it degrades to a plain blockquote showing the literal `[!agent]`.

This matters more than it looks. Two people are writing here to decide what to
build, and an unattributed paragraph silently becomes something "we think". If
a section is assembled rather than argued, say so and let it be argued with.

Sections under an `### <author name>` heading are that person's, always. Claude
never writes there, and never flips `status:`.

## Say where a fact came from

The vault's own archives in `sources/` are checkable — anyone can open the file
and see whether a summary is fair. A fact from a web search isn't, and it ages
differently: funding rounds, star counts and release dates go stale in a way
that an archived article doesn't.

So when a note carries background that isn't in `sources/`, say so in the block,
with the date it was looked up. It costs one line and tells a future reader
which claims to re-check.

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
