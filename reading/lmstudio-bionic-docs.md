---
topic:
kind: docs
by:
  - "[[LM Studio]]"
harness:
  - bionic
status: unread
date: 2026-10-14
addedBy: Jonathan St-Onge
sourceUrl: https://lmstudio.ai/docs/bionic
recBy:
tags:
localCopy: "[[sources/lmstudio-bionic-docs|archived copy]]"
---

# lmstudio-bionic-docs

> [!agent] Claude summary
> Bionic is LM Studio's agent harness, shipped as a separate app from LM Studio itself, and its one positioning claim is that it is built *for open models*. The concrete idea is that model placement is a per-session choice: local weights on your own machine, a model on another of your devices over "LM Link", or larger open models in LM Studio's own "Secure Cloud" with zero data retention. That is the same goal as [[alishahryar1-free-claude-code]] (good agent ergonomics without a frontier-lab API), but approached from the other direction: a new harness built around the model runtime, rather than a proxy that points an existing harness at a different backend. Two caveats. The cloud tier is a vendor service, so "staying in control of your privacy and AI spend" means trusting their ZDR promise once you leave local. And this archive is only the docs welcome page: it calls Bionic "an excellent agentic harness" but says nothing about the loop, tools, context handling or sandboxing, so it shouldn't be counted as evidence for any of those in [[current-harnesses]] until the deeper pages are read.

## Why do I bring this up?

### Jonathan St-Onge

