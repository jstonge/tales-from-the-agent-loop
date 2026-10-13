---
topic: agent harness
kind: docs
harness:
  - deepagents
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://docs.langchain.com/oss/python/deepagents/overview
recBy:
tags:
  - agent-patterns
localCopy: "[[sources/langchain-deepagents-docs|archived copy]]"
---

# langchain-deepagents-docs

Claude summary:

> LangChain's agent harness library, sitting on the LangGraph runtime for durable execution — the batteries-included end of the spectrum this vault keeps circling. What it ships built in: a virtual filesystem with pluggable backends (in-memory, local disk, LangGraph store) and declarative path permissions, subagent spawning into isolated context windows, long-term memory and skills, context summarization and offloading, human-in-the-loop interrupts, and sandboxed code execution. Architecturally it's a middleware stack with harness profiles, so you subtract capabilities through `excluded_tools` rather than adding them — the exact inverse of [[wickham-coding-agent-six-functions]] and of Pi's "if I don't need it, it won't be built" in [[IndyDevDan-the-Pi-Coding-Agent]]. That makes it the strongest statement of the position opposing [[anthropic-building-effective-agents]], which says to skip frameworks until one earns its keep; LangChain publish their own "Deep Agents vs. Claude Agent SDK" comparison, which is worth reading next to it.
>
> Archive caveat: this is the JS-rendered overview hub, so code blocks, tables and several sections (Quickstart, example trace, multimodal extensions) came through empty, and the per-capability pages aren't captured.

## Why do I bring this up?

### Jonathan St-Onge

