---
topic:
kind: repo
by:
  - "[[Nous Research]]"
harness:
  - hermes-agent
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://github.com/nousresearch/hermes-agent
recBy:
tags:
  - agent-patterns
  - context-engineering
localCopy: "[[sources/nousresearch-hermes-agent-repo|archived copy]]"
---

# nousresearch-hermes-agent-repo

> [!agent] Claude summary
> Hermes Agent is Nous Research's general-purpose agent, and the README's one architectural bet is a "closed learning loop": the agent writes skills after complex tasks, revises them during use, nudges itself to save memories, and searches its own past sessions (FTS5 plus LLM summaries) to build a model of the user over time. The rest is deployment breadth: one gateway process serving Telegram, Slack, Discord and others, a built-in cron scheduler that delivers results to those channels, seven terminal backends including serverless ones that hibernate when idle, and isolated subagents. That makes it closer to a long-lived assistant than the coding-agent harnesses elsewhere in the vault. The README is a feature list and does no evaluation, so "the only agent with a built-in learning loop" and the claim that skills self-improve are assertions with no evidence here, and the Architecture page describing the actual loop wasn't archived (only this README was). The Nous Portal subscription is pushed throughout, though other providers are supported. It lines up with the loop taxonomy in [[langchain-the-art-of-loop-engineering]] (cron delivery is the event-driven loop, skill self-improvement is the harness-rewriting one) and with the write and select memory strategies in [[langchain-context-engineering-for-agents]].

## Why do I bring this up?

### Jonathan St-Onge

