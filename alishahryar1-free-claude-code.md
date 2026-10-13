---
topic:
kind: repo
harness:
  - claude-code
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://github.com/Alishahryar1/free-claude-code
recBy:
tags:
localCopy: "[[sources/alishahryar1-free-claude-code|archived copy]]"
---

# alishahryar1-free-claude-code

Claude summary:

> FCC is a local proxy that pretends to be Anthropic's API, so Claude Code and ten other agents (Codex, Pi, OpenCode, Aider…) run on whatever model you route them to: 61 cloud providers plus local LM Studio, llama.cpp or Ollama. The idea behind it is the one this vault keeps returning to: the harness and the model are separable parts. Here Claude Code's loop, tools and prompts stay as they are, and only the model behind them changes, with per-tier routing (`MODEL_OPUS`, `MODEL_HAIKU`, …) and an ordered fallback chain when a provider fails. That makes it a practical way to test how much of Claude Code's behaviour comes from the harness rather than the model, the question [[IndyDevDan-the-Pi-Coding-Agent]] raises from the other side by swapping the harness instead. Treat the headline numbers with caution: "1.3B+ free tokens", "up to 90% lower token usage" and "ToS-friendly" are the project's own claims and the README gives no evidence for them. Its own fine print says free tiers change and a failed request can use up quota at several providers before one succeeds. The archive is the README only, mostly a provider table and install steps (`curl | sh`), so nothing here shows how well smaller non-Claude models handle Claude Code's tool-heavy system prompt.

## Why do I bring this up?

### Jonathan St-Onge

