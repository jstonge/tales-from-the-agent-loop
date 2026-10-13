---
topic:
kind: post
by:
  - "[[Micah Lee]]"
harness:
  - claude-code
status: unread
date: 2026-10-13
addedBy: Ben Cooley
sourceUrl: https://micahflee.com/sandboxing-coding-agents/
recBy:
tags:
  - agent-security
  - sandboxing
localCopy: "[[sources/micahflee-sandboxing-coding-agents|archived copy]]"
---

# micahflee-sandboxing-coding-agents

> [!agent] Claude summary
> Micah Lee's follow-up to his agentic-coding post is a concrete setup guide for running coding agents in isolation: each agent gets a Docker Sandbox that can reach exactly one GitHub repo, authenticated by a fine-grained PAT scoped to that repo, and it signs its commits with a dedicated SSH key that is never loaded into the sandbox's normal environment. The load-bearing detail is the credential scoping, not the tooling: the agent key is registered on GitHub as a *signing* key only — never an authentication key, which would hand the agent every repo the account can reach — and the host's own SSH agent is deliberately not forwarded; a `start-isolated-ssh.sh` script starts a throwaway agent holding only the signing key, so the sandbox can sign without seeing anything else. Commits are authored as "Micah Lee (agent)", making machine-authored history legible in `git log` and on GitHub as a verified signature. It's a first-person macOS walkthrough built on Docker Sandboxes and Claude, so it assumes that stack and skims past the sandbox's own escape resistance in favour of credential hygiene; treat it as one practitioner's recipe rather than a survey of isolation options.

## Why do I bring this up?

### Ben Cooley
Sandboxing agents is a good idea to create safe boundaries on machines.
