---
topic: tool design
kind: post
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.anthropic.com/engineering/writing-tools-for-agents
recBy:
tags:
  - agent-patterns
localCopy: "[[sources/anthropic-writing-tools-for-agents|archived copy]]"
---

# anthropic-writing-tools-for-agents

Claude summary:

> The claim is that a tool is a contract between deterministic code and a non-deterministic caller, and that context is the scarce resource. So wrapping API endpoints one-to-one is the common mistake: `list_contacts` should become `search_contacts`, chained calls should collapse into one `schedule_event`, and tools should return names instead of UUIDs and errors that say what to try next. The load-bearing part is the method, not the checklist. Build realistic multi-step eval tasks, run them in a plain while-loop, read the raw transcripts (including what the agent *didn't* say), and let Claude Code refactor the tools against held-out tests. The evidence is mostly Anthropic's internal evals and a few anecdotes, and the post promotes MCP and Claude Code throughout. It's the tool-side companion to [[anthropic-building-effective-agents]] and argues for a richer, task-shaped toolset than the generic primitives in [[wickham-coding-agent-six-functions]]. Archive caveat: the extraction dropped all bulleted lists and images, including the eval-task and before/after response examples, so open the live page for those.

## Why do I bring this up?

### Jonathan St-Onge

