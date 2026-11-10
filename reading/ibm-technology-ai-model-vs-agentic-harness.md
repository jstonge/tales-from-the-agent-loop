---
topic:
kind: video
by:
  - "[[IBM Technology]]"
harness:
status: unread
date: 2026-10-19
addedBy: Jonathan St-Onge
sourceUrl: https://www.youtube.com/watch?v=ZELPNFXJ4_o
recBy:
tags:
  - context-engineering
  - agent-patterns
localCopy: "[[sources/ibm-technology-ai-model-vs-agentic-harness|archived copy]]"
---

# ibm-technology-ai-model-vs-agentic-harness

> [!agent] Claude summary
> IBM Technology's claim is that an agent is a model plus a harness, and that when two products built on the same model feel different, the harness is the usual reason. The "brain in a jar" framing: the model alone can't open a file, run code or browse, and the harness is what gives it hands. They split the harness into three parts: tools (files, code in a sandbox, web, computer use, the CLI, and MCP for external services), memory (instruction files like `agents.md`, context compaction, search instead of dumping everything in) and the loop (plan, act, observe, repeat, with verification such as tests, screenshots or a reviewer model running throughout). Of those, only the verification point goes past the standard textbook picture; the rest is the same ground as [[braintrust-agent-while-loop]], [[anthropic-building-effective-agents]] and [[langchain-context-engineering-for-agents]], at beginner depth. The load-bearing assertion, that most recent capability gains come from the harness rather than the model, is stated with no benchmark or example, so treat it as a framing and not as evidence; [[nvidia-avo-arc-agi-3]] is the note in the vault that actually argues it with numbers. The closing caveat is the most useful part: the model/harness line is fluid, since planning and self-verification are moving into model training while consistency over long tasks is increasingly shaped by project files. The archive is a complete auto-caption transcript of an eight-minute video, with no gaps I could see.

## Why do I bring this up?

### Jonathan St-Onge

