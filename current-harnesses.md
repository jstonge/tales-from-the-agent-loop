---
topic: harness landscape
harness:
  - claude-code
  - deepagents
  - pi
  - avo
  - deepseek-harness
  - opencode
  - teensycode
date: 2026-10-13
addedBy: Jonathan St-Onge
tags:
---

# current-harnesses

## Harnesses

### claude-code

Anthropic's coding agent, and the reference point most of the vault measures itself against. No note covers it head-on: one characterises it from a competitor's side — a ~10k-token system prompt, five permission modes, Anthropic models prioritised, closed source — and the other from underneath, by proxying the API so the loop stays and only the model changes. Second-hand coverage.

- [[IndyDevDan-the-Pi-Coding-Agent]] — IndyDevDan's pitch is that Pi — an open-source, deliberately minimal agent — is the only real Claude Code…
- [[alishahryar1-free-claude-code]] — FCC is a local proxy that pretends to be Anthropic's API, so Claude Code and ten other agents (Codex, Pi,…

_Covered by 2 note(s): repo, video._

### deepagents

LangChain's batteries-included harness, riding the LangGraph runtime for durable execution. Ships a virtual filesystem over pluggable backends with declarative path permissions, subagents in isolated context windows, long-term memory and skills, context summarisation and offloading, human-in-the-loop interrupts, and sandboxed shell. It's a middleware stack with harness profiles, so you *subtract* capabilities via `excluded_tools` rather than add them — the opposite move from everything else here. They also ship Deep Agents Code, a terminal coding agent built on it.

- [[langchain-deepagents-docs]] — LangChain's agent harness library, sitting on the LangGraph runtime for durable execution — the…
- [[langchain-deepagents-repo]] — The repo README for the library documented in [[langchain-deepagents-docs]], and it's blunter than the docs:…

_Covered by 2 note(s): docs, repo._

### pi

The opposite pole: open source, deliberately minimal, a ~200-token system prompt, no safety mode unless you build one. Everything beyond the loop is an extension you write, including subagents, which aren't built in. Its distinctive architectural choice is that a session is a tree rather than a transcript — JSONL entries point at their parent and each request is rebuilt from the active branch, so branching, forking and compaction all fall out of that one decision.

- [[IndyDevDan-the-Pi-Coding-Agent]] — IndyDevDan's pitch is that Pi — an open-source, deliberately minimal agent — is the only real Claude Code…
- [[pi-how-pi-works]] — Pi's own one-page account of its architecture. The idea that does the most work is that a session is a tree…

_Covered by 2 note(s): docs, video._

### avo

NVIDIA's long-horizon agent, and the strongest "the harness is the capability, not the model" claim in the vault. Two mechanisms carry it: persistent memory that moves implementations, profiler output and reasoning across context windows, and a supervisor that watches for stalled or looping trajectories and redirects. Evidence is a seven-day GPU-kernel search that beat FlashAttention-4 by up to 10.5%, and all 183 ARC-AGI-3 public levels against roughly 30% for the bare model — though they state plainly that none of the comparisons are controlled.

- [[nvidia-avo-arc-agi-3]] — NVIDIA's claim is that long-horizon capability belongs to the harness, not the model. They back it with a…

_Covered by 1 note(s): post._

### deepseek-harness

DeepSeek's `dsh`. The README makes exactly one architectural claim — everything is a plugin, built on a composition framework called Cordis — and is otherwise a launcher: one `npx` command, build steps, community links. Nothing on the loop, tools, context handling or target models. Explicitly a developer preview.

- [[deepseek-harness-repo]] — DeepSeek's own agent harness (`dsh`), and the README makes exactly one architectural claim: everything is a…

_Covered by 1 note(s): repo._

### opencode

Calls itself "the open source AI coding agent", but the README is mostly install paths. The one piece of design it shows is a mode split: a full-access `build` agent and a `plan` agent that refuses edits and asks before running shell commands, toggled with Tab, plus a `@general` subagent. That's the same planning-versus-acting split Claude Code has, expressed as two named agents rather than a permission mode.

- [[anomalyco-opencode-repo]] — OpenCode calls itself "the open source AI coding agent", but almost all of the README is install…

_Covered by 1 note(s): repo._

### teensycode

Not a product — the harness you build yourself across eleven modules of Vercel's course. Its value here is as a parts list: tool loop, safety gates, behavioural prompts, sandbox abstraction, context pruning, subagent delegation, human-in-the-loop. Each step exists because the previous one broke, which makes it the clearest account of *why* a harness has the pieces it has.

- [[vercel-build-ai-agent-harness]] — A Vercel Academy course that builds a coding-agent harness called TeensyCode across eleven TypeScript…

_Covered by 1 note(s): course._

## What this doesn't cover

Absent entirely, with no reading note yet: Cursor, Codex, Aider, Amp, Gemini CLI,
and Anthropic's own Claude Agent SDK — which matters, since two of the notes here
reference LangChain's published comparison against it.

Thin where present: `claude-code` is only described by its competitors, and
`deepseek-harness` and `opencode` are storefront READMEs whose actual design
lives in docs sites nobody has archived. Treat those three as placeholders
rather than assessments.

## Thinking

### Jonathan St-Onge
