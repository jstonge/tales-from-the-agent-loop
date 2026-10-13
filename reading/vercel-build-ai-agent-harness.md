---
topic:
kind: course
harness:
  - teensycode
status: read
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://vercel.com/academy/build-ai-agent-harness
recBy:
tags:
  - agent-from-scratch
localCopy: "[[sources/vercel-build-ai-agent-harness|archived copy]]"
---

# vercel-build-ai-agent-harness

Claude summary:

> A Vercel Academy course that builds a coding-agent harness called TeensyCode across eleven TypeScript modules. The organising idea is causal — each step exists because the previous one broke something: read because the chatbot can't see files, grep because it can't search, bash because it can't run commands, then safety gates because now it can `rm -rf`. Beyond the loop it covers context pruning, a sandbox abstraction with swappable local and in-memory backends, subagent delegation with per-job models, and an askUser human-in-the-loop protocol. Worth noting that the stack is Vercel's own throughout — AI Gateway for model routing, Vercel Sandbox, Vercel Workflow — so part of the architecture is product placement rather than necessity. The archived copy is the course index only; the module content sits behind separate pages.

## Why do I bring this up?

### Jonathan St-Onge

**2026-10-13** — Although it was most certainly at least partly written by an agent, it remains a good introduction to building a custom agent coding loop. It works through a concrete example of building an agent from scratch, with exercises to show what happens when you forgo this or that tool. I hope to find a better reference for building agents from scratch (see [[wickham-what-is-an-agent]] for better one), but this one is alright to get started, I guess
