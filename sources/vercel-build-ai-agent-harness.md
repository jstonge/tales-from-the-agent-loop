---
sourceUrl: https://vercel.com/academy/build-ai-agent-harness
fetched: 2026-10-13
source: article text
---

A tool loop with three tools is a demo. The problems start when you try to use it for real work. You read a 5,000-line file and it stays in context forever. You give it `bash` and it runs `rm -rf`. You ask it to refactor a module and it explains how to refactor a module. One long task fills the context window and the agent loses its own instructions. The cloud sandbox costs money per minute and your code disappears when it times out.

**Harness** is the word for the system around the agent that handles all of this. This course builds `TeensyCode` from scratch.

### What You'll Build

`TeensyCode` is a working AI coding agent harness with a compact TypeScript core, a real toolset, and multiple sandbox backends. Something you understand completely because you built every piece:

- **The loop:** `ToolLoopAgent` with `read`, `grep`, `write`, `edit`, `bash`, `task`, and `askUser` tools
- **Safety gates:** Execute-level safety with safe-command allowlists, evolving into configurable approval (interactive, background, delegated)
- **Behavioral prompts:** A structured system prompt with Agency, Guardrails, and Handling Ambiguity sections, plus `AGENTS.md` injection for per-project configuration
- **Sandbox abstraction:** One `Sandbox` interface, two implementations: local (Node fs and child\_process) and in-memory (just-bash with a copy-on-write virtual filesystem). Swap the backend, the tools don't change
- **Context management:** `pruneMessages`, bounded tool output, and cache control to keep long-running sessions usable and affordable
- **Subagent delegation:** Explorer and executor roles with isolated context, constrained tools, and a model picked per job
- **Human-in-the-loop:** `askUser` with multiple-choice options and an ambiguity protocol that prefers search, then questions, then action
- **Sandbox lifecycle:** State-machine thinking, snapshot and restore, and durable workflow concepts
- **Extensibility:** Event bus, skills with progressive disclosure, and custom tool registration

### Prerequisites

- TypeScript, async/await, basic terminal experience
- An `AI_GATEWAY_API_KEY` environment variable
- Node.js 20+ or Bun runtime
- Recommended: Building Filesystem Agents course

### How The Course Works

**Causal sequence.** Each step exists because the previous one broke something. Step 1 adds `read` because the chatbot can't see files. Step 2 adds `grep` because the agent can't search. Step 3 adds `bash` because it can't run commands, but now it can `rm -rf`. Each step spotlights one concept while the rest stays runnable.

**Modules 1 through 6** are build-along. You write code, run it, verify. **Module 7** is concept and analysis (sandbox lifecycle involves durable workflows and state machines you can't safely demo locally). **Modules 8 through 11** mix building and analysis.

## Course Modules

### Module 1: The Agent Loop

Build a `ToolLoopAgent` from zero tools (a chatbot) to `read` and `grep` (an agent) to `bash` with safety gates.

- From Chat to Agent, where one tool turns a chatbot into an agent
- Your First Tools, where tool descriptions become the model selection API
- Completing the Toolbox, where dangerous tools get execute-level gates

### Module 2: Tool Design

Evolve descriptions into a 5-section contract, extract the factory pattern, and build configurable approval.

- Descriptions That Work: WHEN TO USE, WHEN NOT TO USE, DO NOT USE FOR, EXAMPLES
- Shell Execution with Safety: factory plus operations separates contract from execution
- Approval Gates: boolean to function to discriminated union

### Module 3: The System Prompt

Shape behavior with structured instructions, dynamic composition, verification gates, and `AGENTS.md`.

- Structuring Agent Instructions: Agency plus Guardrails, act don't explain
- Dynamic Prompt Construction: `buildSystemPrompt()` adapts to runtime context
- Verification Gates: typecheck, lint, test, build contract
- Project Context: drop an `AGENTS.md`, change the agent

### Module 4: The Sandbox Abstraction

One interface, three implementations. Tools call `sandbox.exec()`, not `child_process.exec()`.

- Designing the Interface: the `Sandbox` type with `readFile`, `exec`, `stop`
- Local Implementation: Node fs plus child\_process wrapper
- In-Memory Implementation: just-bash with a copy-on-write overlay
- Cloud Implementation: remote VM concept and tradeoffs
- Lifecycle Hooks: `afterStart`, `beforeStop`, `onTimeout`

### Module 5: Context Management

Every tool call stays in context forever. Fix it with pruning, bounded output, and cache control.

- The Problem: token logging shows linear growth
- Pruning Old Results: `pruneMessages` keeps stale tool output from piling up
- Tool Output Design: prevention over cleanup, with bounded caps on every tool
- Cache Control: provider headers reduce repeated context costs

### Module 6: Subagent Delegation

Parent plans, subagents execute. Isolated context, constrained tools, role-based models.

- Why Delegate: single-agent failure modes
- Explorer Subagent: read-only, cheap model, constrained exploration
- Executor Subagent: full tools, stronger model, delegated trust
- Task Tool: routing, permissions, model per role

### Module 7: Sandbox Lifecycle

Cloud sandboxes cost money and time out. Concept and analysis module.

- State Machine: state transitions, timeouts, and activity tracking
- Snapshot and Restore: freeze, restore, and idempotency hazards
- Durable Workflows: Vercel Workflow with `sleep()`
- Hard-Won Lessons: production gotchas from lifecycle work

### Module 8: Human-in-the-Loop

Agents that guess wrong waste more time than agents that ask.

- Structured Questions: `askUser` with multiple choice and an ambiguity protocol
- Approval Config: config for modes, events for policies

### Module 9: Planning and Verification

Plan before acting, verify after acting.

- Todo Tool: task decomposition with state tracking
- Fast Context Understanding: grep first, read only what you'll change
- Verification Contract: gate sequence with scoped claims

### Module 10: Surfaces

The agent is headless. CLI, TUI, and web are rendering strategies.

- CLI Entry Point: args, sandbox factory, clean shutdown
- Streaming and Tool Rendering: real-time text plus tool call display
- Web Surface: same agent, different renderer

### Module 11: Extensibility

Events, not inheritance. Skills as progressive disclosure. Tools as registrations.

- Skills System: names in the prompt, full content on demand
- Custom Tools: register without forking, compose existing tools
- Extension Points: lifecycle events for subscribe, block, modify

### Capstone

Run your harness against a real project. Not "add a hello world endpoint" but "add rate limiting to the auth routes." Watch where context overflows. Watch where it picks the wrong tool. Watch where the subagent gets bad instructions. Fix what breaks.

## Tech Stack

| Component | Purpose | 
|---|---|
| AI SDK | `ToolLoopAgent`, `tool()`, `stepCountIs`, `pruneMessages`, streaming | 
| AI Gateway | Model routing. `"anthropic/claude-haiku-4-5"` as a string, no wrapper | 
| Vercel Sandbox | Remote VM with an isolated filesystem, git, and npm | 
| just-bash | In-memory virtual filesystem and simulated bash | 
| Vercel Workflow | Durable workflows for sandbox lifecycle | 
| Zod v3 | Tool input schemas. v4 breaks AI SDK v6 types | 

On this page
