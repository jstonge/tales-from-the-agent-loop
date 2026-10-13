---
topic:
kind: repo
by:
  - "[[DeepSeek]]"
harness:
  - deepseek-harness
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://github.com/deepseek-ai/deepseek-harness
recBy:
tags:
localCopy: "[[sources/deepseek-harness-repo|archived copy]]"
---

# deepseek-harness-repo

> [!claude] Claude summary
> DeepSeek's own agent harness (`dsh`), and the README makes exactly one architectural claim: everything is a plugin, built on Cordis, a composition framework described in a separate paper (*A Programming Paradigm for Spatiotemporal Composability*). Beyond that the README is a launcher: one `npx` command that starts a local Web UI, build-from-source steps, and community links. It says nothing about the agent loop, tools, context handling, or which models it targets. That design lives in the docs site and the architecture guide, so this archive is the front door and not the thing itself. A separate `docs` note would be the place to get at the substance, the way [[langchain-deepagents-docs]] sits beside [[langchain-deepagents-repo]]. Take the developer-preview warning ("THERE WILL BE COMPATIBILITY-BREAKING CHANGES") at face value. Plugin-everything sits at the opposite end from the minimal-core pitch in [[IndyDevDan-the-Pi-Coding-Agent]], so it's worth checking which of the two actually produces a smaller loop.

## Why do I bring this up?

### Jonathan St-Onge

