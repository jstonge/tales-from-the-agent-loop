---
topic:
kind: post
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.braintrust.dev/blog/agent-while-loop
recBy:
tags:
  - agent-patterns
  - agent-evals
  - context-engineering
localCopy: "[[sources/braintrust-agent-while-loop|archived copy]]"
---

# braintrust-agent-while-loop

> [!claude] Claude summary
> Braintrust argues that Claude Code and the OpenAI Agents SDK both come down to a `while` loop that calls tools, and that frameworks, graphs and multi-phase planners tend to get thrown out on the way to production. That's the same deflation as [[wickham-coding-agent-six-functions]], but for engineers, with sub-agents recast as a tool call that starts another loop. The strongest claim is a number: tool responses make up 67.6% of an agent's tokens and the system prompt 3.4%, so tool outputs deserve prompt-level care (short, filtered, readable, never raw JSON). That overlaps almost entirely with [[anthropic-writing-tools-for-agents]], but the post never says what "a typical agent conversation" was. Braintrust sells evals, and the post's answer to "how do you know the narrow tool is better" is an eval chart that, like the list of eval steps, didn't make it into the archive.

## Why do I bring this up?

### Jonathan St-Onge

