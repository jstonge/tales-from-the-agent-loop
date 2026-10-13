---
topic: agent harness
kind: repo
by:
  - "[[LangChain]]"
harness:
  - deepagents
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://github.com/langchain-ai/deepagents
recBy:
tags:
  - agent-patterns
localCopy: "[[sources/langchain-deepagents-repo|archived copy]]"
---

# langchain-deepagents-repo

> [!agent] Claude summary
> The repo README for the library documented in [[langchain-deepagents-docs]], and it's blunter than the docs: "an open source agent harness — an opinionated agent that runs out of the box", with the four principles stated as opinionated, extensible, model-agnostic, production-ready. Two things here that the docs overview doesn't surface — a JS/TS port (`deepagents.js`), and **Deep Agents Code**, a pre-built terminal coding agent installed by `curl | bash` and pitched explicitly as "similar to Claude Code or Cursor, powered by any LLM". So LangChain isn't only shipping a harness library, they're shipping a Claude Code competitor built on it, which makes this the second entry in the vault making that pitch after [[IndyDevDan-the-Pi-Coding-Agent]]. The quickstart is four lines — `create_deep_agent(model=..., system_prompt=...)` then `.invoke()` — which is the whole argument for the batteries-included position in one screen.

## Why do I bring this up?

### Jonathan St-Onge

