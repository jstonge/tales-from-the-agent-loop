---
topic:
kind: paper
by:
  - "[[Peter Belcak]]"
  - "[[Saurav Muralidharan]]"
  - "[[Jindong Jiang]]"
  - "[[Yonggan Fu]]"
  - "[[Wonmin Byeon]]"
  - "[[Hanrong Ye]]"
  - "[[Ryan Angilly]]"
  - "[[Ali Taghibakhshi]]"
  - "[[Shih-Yang Liu]]"
  - "[[Siru Ouyang]]"
harness:
status: unread
date: 2026-11-16
addedBy: Ben Cooley
sourceUrl: https://arxiv.org/html/2611.05306v1
recBy:
tags:
  - context-engineering
localCopy: "[[sources/belcak-you-dont-need-long-context|archived copy]]"
---

# belcak-you-dont-need-long-context

> [!agent] Copilot summary
> Belcak et al. argue that long input and long interaction histories do not by themselves require long model contexts: selective file reading and repeated task-focused compaction kept measured accuracy broadly near or above full-context baselines across their benchmark suite. Their strongest demonstration is single-action compaction: mini-swe-agent starts a fresh conversation for each environment action, carrying only a compact semantic state; Opus 4.5 matched or improved on two tested coding benchmarks, while GPT 5.6 Sol lost 2.0 and 3.3 percentage points, so the result is not uniform. They propose semantic state space models (SSSMs), trained to update a natural-language state across action boundaries, but this is a research direction rather than a system evaluated in the paper; the large cost savings are estimates derived from throughput measurements and assumed pricing, not direct production-billing measurements. The evidence supports short-context agent design for the tested workloads, not the broadest suggestion that long contexts can be eliminated; compare its state-and-retrieval approach with [[langchain-context-engineering-for-agents]].

## Why do I bring this up?

### Ben Cooley

