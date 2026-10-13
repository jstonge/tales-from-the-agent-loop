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

> [!agent] Claude survey
> Assembled from the reading notes linked below. Argue with it under Thinking rather than editing it into agreement.

| Harness              | What it is                                                                | The distinctive move                                                                    | Covered by                                                                          |
| -------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **deepagents**       | LangChain's batteries-included harness, on the LangGraph runtime          | You *subtract* capabilities with `excluded_tools` rather than add them                  | [[langchain-deepagents-docs\|docs]] · [[langchain-deepagents-repo\|repo]]           |
| **pi**               | Deliberately minimal open-source agent; ~200-token prompt, no safety mode | A session is a tree, not a transcript — branching and compaction fall out of that       | [[IndyDevDan-the-Pi-Coding-Agent\|video]] · [[pi-how-pi-works\|docs]]               |
| **avo**              | NVIDIA's long-horizon research agent                                      | Persistent memory across context windows, plus a supervisor that redirects stalled runs | [[nvidia-avo-arc-agi-3\|post]]                                                      |
| **teensycode**       | The harness you build yourself across Vercel's eleven-module course       | Each step exists because the previous one broke — a parts list with reasons             | [[vercel-build-ai-agent-harness\|course]]                                           |
| **claude-code**      | Anthropic's coding agent; the reference point the others measure against  | Only described here by its competitors — no direct note yet                             | [[IndyDevDan-the-Pi-Coding-Agent\|video]] · [[alishahryar1-free-claude-code\|repo]] |
| **opencode**         | Open-source coding agent, mostly install docs                             | Planning vs acting as two named agents (`plan`/`build`), not a permission mode          | [[anomalyco-opencode-repo\|repo]]                                                   |
| **deepseek-harness** | DeepSeek's `dsh`, explicitly a developer preview                          | Everything is a plugin, built on a framework called Cordis                              | [[deepseek-harness-repo\|repo]]                                                     |

## What this doesn't cover

> [!agent] Claude survey
> Absent entirely, with no reading note yet: Cursor, Codex, Aider, Amp, Gemini CLI,
and Anthropic's own Claude Agent SDK — which matters, since two of the notes here
reference LangChain's published comparison against it.
>
> Thin where present: `claude-code` is only described by its competitors, and
`deepseek-harness` and `opencode` are storefront READMEs whose actual design
lives in docs sites nobody has archived. Treat those three as placeholders
rather than assessments.


## Thinking

### Jonathan St-Onge
