# tales-from-the-agent-loop

![Simon Stålenhag, Tales from the Loop — cover art](assets/tales-from-the-loop-cover.png)

> I first learned about [Tales from the Loop](https://www.simonstalenhag.se/tftl.html) from this [soundtrack](https://www.youtube.com/watch?v=2PkbfZWqqSw&list=PLEFjGrqW-nqkACZYF5oStYVjqhhsOWtnL) by Philip Glass and Paul Leonard-Morgan. I loved the imagery. It’s about stories from a sci-fi suburbia built on top of The Loop, a deep underground particle accelerator that creates wrinkles in the inhabitants’ lives.

The Loop in Stålenhag’s work is a place, with some frontier technology that people at the surface barely understand. The Loop also causes wrinkles in our reality, but it is disembodied. As it is now, most tech bros talk of the Loop belonging to the agent. The Agent Loop is how LLMs stretch their hands into the digital realm, taking actions on our filesystem and beyond (the web). In doing so, they can create wrinkles in our reality: spiking website traffic, making open-source developers’ lives miserable, and putting white-collar workers out of their jobs.

In this project, we learn about that emerging Agent Loop from a humanistic perspective. How can we share the Loop with the Agent in ways that are empowering to us as humans? Maybe a day will come when we’ll need to ask whether we should make the LLM happy in that loop too... but we’re not there yet.

## How to get started

Clone it and open the folder as a vault in [Obsidian](https://obsidian.md):

```sh
git clone https://github.com/jstonge/tales-from-the-agent-loop.git
```

Then enable **Settings → Appearance → CSS snippets → `agent-callout`**. It tints
agent-written blocks orange, so you can tell whose words are whose.

### Add what you read

Hand your agent the link:

```
/vault-note https://tidydesign.substack.com/p/what-is-an-agent
```

It archives the page to `sources/`, makes a note in `reading/`, and drafts a
summary marked as the agent's. `## Why do I bring this up?` is left for you,
under your own name. Once there are a few, `/vault-synthesis` surveys across
them — see [`current-harnesses`](synthesis/current-harnesses.md).

### Write your own notes

Your own thinking goes at the root as atomic notes — one idea each, linked to
each other and to the reading. Make a new note, run **Templates: Insert
template** (Cmd+P) → `atomic-notes`, and put your name in `addedBy`. For hints
on what a note is missing:

```
/vault-review grant-discovery-loop
```

It answers in chat and never edits the note.

### Where things live

| | |
| --- | --- |
| the root | our own thinking, one atomic note per idea |
| `reading/` | one note per thing read |
| `synthesis/` | surveys compiled across the reading notes |
| `who/` | the people and organisations behind them |
| `sources/` | archived full text, so nothing depends on a live URL |

The conventions agents follow are in [AGENTS.md](AGENTS.md). Using something
other than Claude Code, or curious how it works underneath? See
[tools/README.md](tools/README.md).
