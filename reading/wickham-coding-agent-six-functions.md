---
topic: coding agent tools
kind: post
by:
  - "[[Hadley Wickham]]"
harness:
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://tidydesign.substack.com/p/a-coding-agent-is-six-functions-in
recBy:
tags:
  - agent-from-scratch
localCopy: "[[sources/wickham-coding-agent-six-functions|archived copy]]"
---

# wickham-coding-agent-six-functions

> [!claude] Claude summary
> Later post in the same series as [[wickham-what-is-an-agent]], and the one that finally drains the magic out of the thing: a coding agent is just a harness plus six tools — read, write, edit, list, search, run command — and only three of those are load-bearing. He builds the whole agent in R with ellmer in about a page of deliberately boring code, then earns each addition instead of asserting it: the edit tool exists because rewriting 500 lines to change one is slow and error-prone, and the shell tool is the security hole that motivates path sandboxing. A useful contrast with [[vercel-build-ai-agent-harness]], which spends many more words saying less.

## Why do I bring this up?

### Jonathan St-Onge

