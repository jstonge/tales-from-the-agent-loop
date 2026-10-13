---
topic:
kind: post
by:
  - "[[NVIDIA]]"
harness:
  - avo
status: unread
date: 2026-10-13
addedBy: Jonathan St-Onge
sourceUrl: https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/
recBy:
tags:
  - agent-patterns
localCopy: "[[sources/nvidia-avo-arc-agi-3|archived copy]]"
---

# nvidia-avo-arc-agi-3

> [!claude] Claude summary
> NVIDIA's claim is that long-horizon capability belongs to the harness, not the model. They back it with a transfer story: the same AVO agent ran a seven-day GPU-kernel search, beating FlashAttention-4 by up to 10.5%, and then solved all 183 levels of the ARC-AGI-3 public set with Claude Opus 5, against the roughly 30% ARC Prize reports for the bare model. The two mechanisms they name as load-bearing are persistent memory, which carries implementations, profiler output and reasoning across context windows, and a supervisor that watches for stalled or looping trajectories and redirects the main agent. That's a heavier answer to running out of context than the summary-entry compaction in [[pi-how-pi-works]]. The post is careful to say none of its comparisons are controlled: the 30% baseline used a different reasoning setting, and the 12% fewer actions than VISTA comes from a different observation format and backend. So the memory and supervisor are asserted to matter, not shown to, and the numbers are public-set only, not the private competition set. It describes the architecture but doesn't point to released code, so for now AVO is something to read about, not run.

## Why do I bring this up?

### Jonathan St-Onge

