---
topic: workflows vs agents
kind: post
by:
  - "[[Anthropic]]"
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.anthropic.com/engineering/building-effective-agents
recBy:
tags:
  - agent-from-scratch
  - agent-patterns
localCopy: "[[sources/anthropic-building-effective-agents|archived copy]]"
---

# anthropic-building-effective-agents

> [!claude] Claude summary
> Anthropic's taxonomy splits agentic systems into workflows, where the path through the LLM is code you wrote, and agents, where the model picks its own steps. The useful part is the claim that an agent is just an LLM calling tools in a loop against feedback from its environment, and that you should call the API directly until a framework earns its keep. Slightly funny coming from a company selling an agent SDK, but it has aged better than most of what shipped around it.

## Why do I bring this up?

### Jonathan St-Onge

