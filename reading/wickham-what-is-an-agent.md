---
topic:
kind: post
harness:
status: read
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://tidydesign.substack.com/p/what-is-an-agent
recBy:
tags:
  - agent-from-scratch
localCopy: "[[sources/wickham-what-is-an-agent|archived copy]]"
---

# wickham-what-is-an-agent

> [!claude] Claude summary
> The first post in the series, built up from nothing: a conversation is a stateless exchange of JSON turns, a tool call is the model asking you to run a function and hand back the result, and a harness is the loop that does that for you automatically. The payoff is a one-line definition — an agent is an LLM, in a harness, calling tools repeatedly in a loop, deciding each next step from the last result — split into read tools that observe the world and write tools that change it, which is why the read/write cycle is where the iteration comes from. Demonstrated in R with ellmer in about a dozen lines. It ends on the problem it can't solve: he has just handed an LLM the ability to delete files, and sandboxing, git and backups only help while the actions stay on your own machine. Continues in [[wickham-coding-agent-six-functions]].

## Why do I bring this up?

### Jonathan St-Onge

**2026-10-13** — Hadley being Hadley, he explains in plain words what tech bros explain in jargon. This is the first blog post in a series on building agents from scratch. I also like that it goes a long way toward showing that an agent can even be coded in `R`, which sometimes makes the whole thing feel more humble.
