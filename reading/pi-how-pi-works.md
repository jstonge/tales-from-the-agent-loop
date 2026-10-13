---
topic:
kind: docs
by:
  - "[[Mario Zechner]]"
harness:
  - pi
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://pi.dev/docs/latest/how-pi-works
recBy:
tags:
  - pi
localCopy: "[[sources/pi-how-pi-works|archived copy]]"
---

# pi-how-pi-works

> [!agent] Claude summary
> Pi's own one-page account of its architecture. The idea that does the most work is that a session is a tree and not a transcript. Every entry in a JSONL file points to its parent, and the next model request is rebuilt from the active branch alone. Branching, forking and compaction all fall out of that one choice. Compaction just inserts a summary entry that later requests read in place of older messages, and the originals stay on disk. The agent loop itself is the familiar one from [[wickham-coding-agent-six-functions]]: request, stream, run tool calls, record results, repeat while there's work. Pi's additions are queueing rules. Steering messages land after the current turn, follow-ups land after the run finishes, and aborting hands queued messages back to the editor. Two things cut against the minimal framing in [[IndyDevDan-the-Pi-Coding-Agent]]. First, extensions are TypeScript loaded in-process that can register tools, providers, commands and UI, which puts Pi closer to the plugin model of [[deepseek-harness-repo]] than "minimal" suggests. Second, the trust section is candid that there's no sandbox: tools get the process's OS permissions, and extensions run inside it. This is an overview only. It doesn't name the built-in tools, say when compaction fires, or say what project trust actually gates.

## Why do I bring this up?

### Jonathan St-Onge

