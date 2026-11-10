---
topic:
kind: post
by:
  - "[[Sebastian Raschka]]"
harness:
  - mini-coding-agent
status: unread
date: 2026-11-10
addedBy: Jonathan St-Onge
sourceUrl: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent
recBy:
tags:
  - agent-from-scratch
  - context-engineering
  - agent-patterns
localCopy: "[[sources/raschka-components-of-a-coding-agent|archived copy]]"
---

# raschka-components-of-a-coding-agent

> [!agent] Claude summary
> Raschka's claim is that a coding agent is a model plus a harness, and that the harness, not the model, is what makes Claude Code or Codex feel stronger than the same model in a chat box. He breaks the harness into six components, illustrated by his own pure-Python Mini Coding Agent: live repo context (git state, AGENTS.md, layout gathered up front), a stable prompt prefix that the runtime caches, validated and permission-gated tools, context reduction (clipping plus compressing older transcript while keeping recent events rich), two-layer session memory (full transcript plus a small working memory), and bounded subagents. The most useful ideas are that tool checks (known tool, valid arguments, approval, path inside the workspace) make the model less free but more reliable, and that "a lot of apparent model quality is really context quality". The claim that a good open-weight model in a good harness would match the frontier pairing is explicitly flagged by him as speculation, and nothing here is benchmarked; compare [[nvidia-avo-arc-agi-3]] for a numbers-backed version of the harness argument. It overlaps with [[wickham-coding-agent-six-functions]], [[langchain-context-engineering-for-agents]], [[anthropic-writing-tools-for-agents]] and [[ibm-technology-ai-model-vs-agentic-harness]], but is the more concrete of the group on caching and on separating compact transcript from working memory. The archive is the full article text, about 3,250 words, but the figures the prose keeps pointing to are not in it, and the tail is a book promotion.

## Why do I bring this up?

### Jonathan St-Onge

