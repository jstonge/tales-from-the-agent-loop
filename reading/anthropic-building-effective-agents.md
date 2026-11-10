---
topic: workflows vs agents
kind: post
by:
  - "[[Anthropic]]"
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://www.anthropic.com/engineering/building-effective-agents
recBy:
tags:
  - agent-from-scratch
  - agent-patterns
localCopy: "[[sources/anthropic-building-effective-agents|archived copy]]"
---

# anthropic-building-effective-agents

> [!agent] Claude summary
> Anthropic's taxonomy splits agentic systems into workflows, where the path through the LLM is code you wrote, and agents, where the model picks its own steps. The useful part is the claim that an agent is just an LLM calling tools in a loop against feedback from its environment, and that you should call the API directly until a framework earns its keep. Slightly funny coming from a company selling an agent SDK, but it has aged better than most of what shipped around it.

## Why do I bring this up?

### Jonathan St-Onge

Once upon a time, I would have called that a "seminal paper"  for whatever topic I was trying to understand. But now we deal with blog posts. I brought this paper up because it brings how the following point

> Tools might look like simple function calling. But they should be designed for agents. The way agents wield tools is unlike how we humans declare functions in scripts. It depends on the agent context, their ability to reach for that tool, and most importantly, how tools help agents being more effective at solving problems. I also find interesting that testing came along with tool usage.

A few other things that came to my mind when reading the text:
- **By tracking tool usage when testing**. The authors mention the importance of surface common workflows allowing further tool consolidation. JGY told me about such example at his company. They evaluated the order in which tools were being use by their agent, revealing how a common patterns across users. Then they consolidated such that instead of having 12 independent tool calls they could have 1 tool call specific to that recurrent workflow, reducing token use and latency.
- **Tools should not be simple wrappers over API endpoint**. I think i'm guilty of thinking of tools in that way. They say that we should not do that because "agents have distinct 'affordances' to traditional software". I am not sure about their usage of affordances here, but they put in quotes so I'll tolerate it. By "affordances", they mean that, for instance, LLMs have limited information that they can process at once. It is different from traditional software where computer memory is abundant. Returning ALL contact list in a tool call, or maybe full tables (as markdown), is inefficient because the LLM will burn tokens going through that list/table. Instead, tools are better when they let agents hit the high-impact sections of that list, taking advantage of features like progressive disclosures.



