---
topic:
kind: post
by:
  - "[[LangChain]]"
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.langchain.com/blog/the-art-of-loop-engineering
recBy:
tags:
  - agent-patterns
  - agent-evals
localCopy: "[[sources/langchain-the-art-of-loop-engineering|archived copy]]"
---

# langchain-the-art-of-loop-engineering

> [!agent] Claude summary
> LangChain's take on swyx's "loopcraft": an agent is four nested loops, and the work worth doing is in the outer two. Loop 1 is the bare model-calls-tools loop (the one [[braintrust-agent-while-loop]] and [[wickham-what-is-an-agent]] build up). Loop 2 wraps it in a grader, deterministic or LLM-as-judge, that sends failures back as feedback. Loop 3 runs it from events (crons, webhooks, Slack) rather than on request. Loop 4, which they call the most important, runs an analysis agent over traces and rewrites the harness's prompts, tools, or grader. The one structural idea is that loop 4's return arrow reaches inside loop 1 rather than restarting it, the same "the harness improves itself" bet as [[nvidia-avo-arc-agi-3]]. The rest maps each loop to a LangChain/LangSmith product (`create_agent`, `RubricMiddleware`, Fleet, Engine), so treat it as a vendor framing as well as a taxonomy. The post shows no numbers on whether loop 4 actually improves the docs agent it uses as its example. Archive caveat: the diagrams and the closing "tabular view" of the four loops were images and didn't come through.

## Why do I bring this up?

### Jonathan St-Onge

