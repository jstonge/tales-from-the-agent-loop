---
topic:
kind: video
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.youtube.com/watch?v=zaLQ0AnY9dI
recBy:
tags:
  - agent-patterns
localCopy: "[[sources/witteveen-jev-in-your-agent-harness|archived copy]]"
---

# witteveen-jev-in-your-agent-harness

> [!claude] Claude summary
> Witteveen's claim is that most model calls in an agent loop are disguised `if` statements: which tool, which skill, is this command safe, is this result good enough. He says those should go to a small decision model (TypeSafe's Jev or the open alternatives), which returns typed probabilities in milliseconds rather than paying for a full LLM call. The part worth keeping is where it plugs in. There are four hooks in any loop: before the prompt is built (which skills to load), before the model call (which model), before a tool runs (is it safe), and after a result (go around again?). His two demos make the first hook concrete. One picks a skill category and then a skill, in two steps, so the system prompt carries ten category names instead of fifty skill descriptions, which takes the on-demand skill loading in [[pi-how-pi-works]] one step further. The other re-ranks retrieved passages for RAG. The friction is the one he names himself: these models can be prompt-injected. That's awkward for risk gating, and his fix (first ask the same model whether the input contains an injection) doesn't remove the weakness. The demos are hand-picked cases in a UI with no speed or accuracy numbers, so "faster and cheaper" is asserted, not measured.

## Why do I bring this up?

### Jonathan St-Onge

