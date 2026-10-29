---
topic:
kind: post
by:
  - "[[LangChain]]"
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.langchain.com/blog/context-engineering-for-agents
recBy:
tags:
  - context-engineering
  - agent-patterns
localCopy: "[[sources/langchain-context-engineering-for-agents|archived copy]]"
---

# langchain-context-engineering-for-agents

> [!agent] Claude summary
> LangChain's claim is that the main job in building a long-running agent is deciding what sits in the context window at each step, and that nearly every technique in use falls into four buckets: write (save context outside the window, as scratchpads or cross-session memories), select (pull the relevant part back in, whether memories, tools or retrieved knowledge), compress (summarize or trim, as in Claude Code's auto-compact), and isolate (split context across sub-agents, sandboxes, or fields of a state object the LLM doesn't see). The framing is borrowed from Karpathy (context window as RAM) and Drew Breunig's list of failure modes: poisoning, distraction, confusion, clash. Load-bearing is the taxonomy plus the repeated admission that selection and summarization are the hard parts, with Simon Willison's ChatGPT-injects-his-location example as the cautionary case. Most of the examples are cited second-hand from Anthropic, Cognition, Windsurf and Hugging Face, not measured by LangChain. The second half maps each bucket to LangGraph/LangSmith features, so read it as a vendor catalogue, and it gives no numbers for what any strategy buys you. It is a good vocabulary to hold next to [[langchain-the-art-of-loop-engineering]], which is about the loops around the agent, whereas this post is about what flows through the innermost one. [[langchain-deepagents-docs]] is the library that packages several of these patterns.

## Why do I bring this up?

### Jonathan St-Onge

