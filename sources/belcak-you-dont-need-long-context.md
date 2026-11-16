---
sourceUrl: https://arxiv.org/html/2611.05306v1
fetched: 2026-11-16
source: article text
---

# You don’t need long context

###### Abstract

Abstract. Later tokens are costlier to generate than earlier tokens. On frontier open weight models, the disparity in cost may rise to as much as 7x. Through frequent compaction, we show across a broad range of long-horizon and long-input tasks that frontier language models sacrifice little to no task accuracy when maintaining short contexts. We further demonstrate that LLM performance does not collapse on long-horizon software engineering tasks even when taking at most one action per context, and based on that we outline the concept of semantic state space models (SSSMs). Our findings question the need for long-context language models.

## 1 Introduction

Not all tokens are generated equal.
Token generation latency and memory footprint both grow with the number of tokens in a language model’s context.
This is due to the inherent linear<sup>1</sup><sup>1</sup>
            1
            
            
            
            
            
            
            
          Model architectures with a constant cost of token generation with respect to context depth have been repeatedly proposed but have never been fully embraced – linear-cost attention-based mechanisms remain the backbone of all popular language models. relationship between the computational cost of generating a token and its depth within a context \[25\].
Figure 1 shows the cloud token generation cost as a function of context window size for a selection of popular open-weight models.
Observe that there is a considerable monetary benefit to serving models on cloud GPUs with consistently shorter contexts.
This fact is often hidden from the end user since retail token prices are quoted at a fixed price per $1$M tokens regardless of the input context length.
Note that the extent of cost reductions ($3.6\times$ to $7\times$) rivals or exceeds that of many other orthogonal optimization methods such as aggressive quantization or structured sparsification \[5, 14, 8\].

Monetary cost is not the only quality of LM workloads that suffers when inputs are long.

Figure 2 shows the token generation latency, throughput, and memory footprint of several popular locally-run coding models as a function of the input context length. Observe how the generation inter-token latency approximately doubles for several models across the measured context lengths, implying a doubling of the time required to generate a response at longer contexts.

Put simply, the longer the input context provided to the language model (LM), the slower, more memory hungry, and more expensive its output token generation.

Given the considerable benefits of keeping input context short in both cloud and edge LM use, one would assume that popular LMs would have naturally evolved to operate on contexts only as short as necessary to complete their tasks. This could not be farther from the truth. As seen in Table 1, which compares the lengths of well-known works of writing with the context window sizes of representative proprietary and open-weight models, context window sizes have vastly outgrown many influential writings. It would seem that models have been evolving to accommodate the ever larger possible inputs rather than to maximize efficiency.

| Literary works |  |  | Model context window sizes |  |  | 
| Work | Words | Tokens | Model | Words | Tokens | 
| The Old Man and the Sea \[21\] | $\sim 27$K | $\sim 37$K | MiniMax M2.7 \[31\] | $\sim 150$K | $200$K | 
| The Great Gatsby \[15\] | $\sim 48$K | $\sim 64$K | Claude Opus 4.5 \[2\] | $\sim 150$K | $200$K | 
| Qur’an (Saheeh Int’l translation) \[38\] | $\sim 156$K | $\sim 207$K | Gemma 4 31B \[16\] | $\sim 192$K | $256$K | 
| King James New Testament \[26\] | $\sim 181$K | $\sim 241$K | Kimi K2.6 \[32\] | $\sim 192$K | $256$K | 
| Great Expectations \[12\] | $\sim 184$K | $\sim 245$K | Qwen 3 Coder Next \[9\] | $\sim 197$K | $262$K | 
| The Lord of the Rings \[42\] | $\sim 481$K | $\sim 640$K | Gemini 3.8 Flash \[13\] | $\sim 750$K | $1$M | 
| War and Peace \[43\] | $\sim 566$K | $\sim 753$K | GLM 5.2 \[51\] | $\sim 750$K | $1$M | 
| King James Old Testament \[26\] | $\sim 603$K | $\sim 802$K | GPT 5.6 Sol \[35\] | $\sim 790$K | $1.05$M | 

The enormous context window sizes of contemporary LMs and the tangible cost advantages of keeping their contexts short thus appear to be at odds with each other. While operating with longer contexts might in some cases be thought beneficial to model task accuracy, we must ask:

1. RQ0 
Are long contexts necessary?

If not, let’s do away with long contexts and long-context models. And, if there are currently any objective benefits of keeping long context models, we can likely preserve them by making the appropriate post-training adjustments to future models.

To answer 0, look at where the so-called long contexts (and, correspondingly, large context windows) in language modeling come from. Broadly, there are two types of workloads that often result in long input contexts being passed to LMs:

1. LCW1
2. LCW2

Examining these two types of workloads more closely, it is not immediately clear whether operating on long contexts is necessary in order to complete them. In particular, the entire conversational history of 1 does not necessarily need to be considered at every step of a long-horizon operation in order to successfully complete the task. Likewise, the long inputs of 2 do not necessarily need to be ingested in their entirety at all times in order for the workload to conclude successfully. Moreover, observe that the tasks in 2 can always be reduced to 1 by storing the long input as a resource and equipping the LM with a tool for selective input reading.

Motivated by the advantages of keeping LM generation contexts short and the apparent lack of clear justification for the popular practice for ingesting long inputs all at once and maintaining long conversational histories as discussed above, we decompose 0 to pose the following research questions:

1. RQ1 
Can long-horizon tasks be completed without long contexts?
2. RQ2 
Can long-input tasks be completed without long contexts?
3. RQ3 
Can long-horizon tasks be completed taking no more than a single action per context?

The rest of this paper is aimed at curtly answering these questions.

## 2 Methodology

We use one methodology to answer all research questions posed in Section 1.

### 2.1 Definitions

The base term “context” is, unfortunately, considerably overloaded in language modelling. Below we outline our working definitions intended to fix the meaning of otherwise vaguely interpreted terms commonly used in the community and relied on throughout this paper. Their numerical boundaries are rough rules of thumb.

##### Inference step.

An *inference step* is one invocation of an LM to produce output.
In agentic workflows, it typically coincides with one agent turn of a conversation.

##### Input context.

At a given inference step, the *input context* is the complete sequence of tokens made available to the LM to produce output.
It may include system instructions, the task input, prior model outputs, tool results, and any other conversational history.

##### Output context.

At a given inference step, the *output context* is the complete sequence of tokens generated by the LM in the inference step.
It may include a thinking trace, tool calls, user-oriented outputs, or other model output artifacts.

##### Context.

At a given inference step, the *context* is the input context, the input context and an associated output context, or the input context and any token space reserved for a possible output context.

##### Context window and context window size.

The *context window* is the space of tokens an LM can comprehend at any given point, usually imposed by the model’s architecture or indirectly by its post-training data bias.
Contexts exceeding context windows may cause system errors or unexpected behavior.
The *context window size* is the maximum number of tokens that an LM endpoint can process in one invocation, whether imposed by the model’s context window or narrowed by its serving configuration.

##### Long context.

We call a context *long* when its length approaches constituting a significant fraction of context window size of many contemporary frontier models, which tends to rest at approximately $256$K tokens or more at the time of this study.
We further call an execution regime or context-management strategy *long-context* if it permits the context to grow toward that scale, even when an individual run terminates before reaching the context window size.

##### Short context.

We call a context *short* when its length is much closer to zero than to the context window size common to many contemporary frontier models.
In the operating regimes emphasized in this work, short contexts are commonly limited to roughly $16$K–$50$K tokens.
Note that we take “short” to mean short relative to common context window sizes; it does not mean that the context is small in an absolute linguistic sense.
Even context window sizes of $16$K–$50$K tokens suffice to contain elaborate literary works (cf. Table 1).

##### Long-input task.

A *long input task* is a task which is accompanied by a *long input* – i.e., input information that would constitute a long context if ingested directly.
The term *long input* refers to the size of the available task input, irrespective of whether a harness places all of it in the model context at once or exposes it through selective input reading.

##### Long-horizon task.

A *long-horizon task* is a task whose completion requires many sequential model actions, with later actions depending on the observations, artifacts, or decisions produced by earlier ones.
Absent context management, the resulting interaction history accumulates across the task and may grow toward a model’s context window size and form a long context.

### 2.2 Benchmarks

We assess the merits of 1, 2 and 3 by considering two groups of benchmarks corresponding to the sources of long context identified in Section 1: long-horizon tasks (1), whose interaction histories grow as an agent acts, and long-input tasks (2), whose source material can itself fill or exceed a model’s context window size. Our ensemble of benchmarks covers realistic software-engineering, information-seeking, and tool-use workloads with controlled long-input diagnostics.

##### Long-horizon task benchmarks.

The long-horizon task benchmark group aims to represent real sequential workflows in which the model must repeatedly inspect an environment, select an action, observe its result, and use that result to decide what to do next. Without context management, every command, tool response, retrieved document, and intermediate decision is appended to an ever-growing history. The software-engineering benchmarks are particularly representative examples because repository exploration, implementation, and validation naturally form long sequences of interdependent actions. The remaining benchmarks broaden this group to information retrieval, user interaction, and cross-tool orchestration.

- • 
SWE-bench Verified \[23\] is a human-validated set of 500 real GitHub issue-resolution tasks from popular repositories, where the agent must produce a patch that passes the repository’s held-out test suite.
- • 
SWE-bench Multilingual \[48\] comprises 300 manually curated issue-resolution tasks from repositories across nine programming languages. It tests repository exploration, implementation, and validation across different language ecosystems.
- • 
Terminal-Bench 2.1 \[30\] is an agentic benchmark of 89 real command-line tasks executed in sandboxed containers and scored by per-task verifiers, measuring end-to-end terminal problem-solving beyond single-repository patching.
- • 
FRAMES \[27\] contains 824 challenging multi-hop questions whose answers require combining information from two to fifteen Wikipedia articles. In our agentic formulation, the model searches a fixed Wikipedia corpus, opens relevant articles incrementally, and submits a free-form answer evaluated against the reference answer by an LM judge. The benchmark consequently tests iterative retrieval and evidence integration while allowing the retrieved evidence to accumulate in the interaction history.
- • 
$\tau^{2}$-bench \[7\] evaluates agents that converse with a simulated user while operating domain-specific tools under explicit policy constraints. We use the 184-task golden set spanning retail, airline, and telecommunications; success requires both satisfying the user’s request and bringing the environment to the correct final state. Its mixture of dialogue, reasoning, and state-changing tool calls tests whether information established early in an interaction remains usable by later actions.
- • 
BFCLv3 \[36\] evaluates multi-turn tool use in simulated environments. We use its 200 long-context episodes, which require agents to retain information across user turns and schedule state-changing tool calls.

##### Long-input task benchmarks.

The long-input task benchmark group holds the task question comparatively short while making the information needed to answer it large, at least in principle. It includes three broad, realistic long-document QA benchmarks and four needle-style benchmarks.

- • 
LongBench v2 \[6\] comprises 503 challenging multiple-choice questions with heterogeneous, predominantly natural inputs ranging from $8$K to approximately $2$M words. Its six task families cover single- and multi-document question answering, long in-context learning, long dialogue, code-repository understanding, and structured-data understanding.
- • 
LOONG \[45\] is a 1,600-question multi-document benchmark in which a question typically depends on multiple complete financial reports, legal cases, or academic papers in either English or Chinese. Its locating, comparison, clustering, and chain-of-reasoning tasks are designed so that evidence is distributed across multiple load-bearing documents.
- • 
Artificial Analysis Long Context Reasoning (AA-LCR) \[4\] comprises 100 human-crafted questions requiring reasoning across sets of real-world documents averaging approximately $100$K input tokens. Its seven document categories include company and industry reports, government consultations, academic and legal documents, marketing materials, and survey reports. Answers require integrating evidence and performing multi-step reasoning across documents, rather than retrieving a directly stated fact.
- • 
Needle in a Haystack (NIAH) \[24\] consists of target sentences inserted at controlled depths in long bodies of unrelated essay text and of asking for the fact expressed by that sentence. Our 125-instance grid varies both insertion depth and document length, with contexts extending from $16$K to roughly $500$K tokens.
- • 
RULER \[22\] is a synthetic long-context suite containing thirteen tasks: eight needle-retrieval variants, variable tracking, common- and frequent-word extraction, and two multi-hop question-answering tasks. We evaluate all thirteen at $256$K and $500$K tokens and score the recall of the required answer set.
- • 
Counting-Stars \[39\] scatters 32 marked numbers throughout a long text and asks the model to recover them all. We use the complete 192-question public set, spanning English and Chinese, acquisition and reasoning variants, and documents from $4$K to $128$K tokens. The reasoning variant includes initially incorrect counts that are subsequently corrected, requiring the model to distinguish the final value from a nearby distractor rather than merely copy every marked number.
- • 
BABILong \[28\] consists of short facts from the bAbI \[46\] reasoning tasks embedded into book text. Answering requires locating the relevant statements and then performing operations such as fact chaining, counting, negation, or set tracking. We evaluate 550 questions across all ten task types and five input lengths from $64$K to $1$M tokens.

Note that even the needle-style benchmarks considered often do not feature a clear lexical overlap aiding easy retrieval. They do, however, require aggregation, variable tracking, or reasoning over multiple retrieved facts for the correct answer to be produced.

### 2.3 Models

We perform our study on two groups of models. Large closed-weight models are used as the workers in our principal task-accuracy experiments, while large open-weight models support the cloud system throughput study and complementary local experiments.

##### Large closed-weight models.

Our principal benchmark experiments use Claude Opus 4.5 and GPT 5.6 Sol. We select these models as representative of the strong general-purpose models used for coding, tool use, and other long-horizon workflows. Using independently developed model families also reduces the risk that an observed effect of compaction is specific to one provider or post-training recipe.

##### Large open-weight models.

We use large open-weight models for two additional parts of the experimentation. First, the cloud-throughput study in Figure 1 uses models large enough to require multi-GPU deployment and exposes the effect of context window size under saturated serving load:

We fit the context-cost ratio from these throughput measurements and define the 1 optimized-retail-cost estimate in Appendix B.

Second, we use locally deployable open-weight models for the on-device systems measurements in Figure 2 and for complementary task-level experiments. We deploy them on an NVIDIA DGX Spark \[33\], whose 128GB of unified memory leaves about 109GB available for local LM serving.

Such deployments are relevant when source code or other task data must remain on-device for privacy or cost reasons.
The two Qwen checkpoints are served in NVFP4 \[1\]; the remaining three are served from GGUF weights through llama.cpp using 3- to 4-bit *k*-/*i*-quantization.
Together they cover hybrid linear/softmax attention, distinct interleaved sliding-window/global-attention stacks, gated grouped-query attention, and conventional full grouped-query softmax attention.
This architectural diversity helps to test the sufficiency of short context claimed in 1 across models with different attention mechanisms and post-training characteristics.

- • 
Qwen 3.6 27B \[37\] is a 27B-parameter dense model served in NVFP4. Its layers alternate in a 3:1 pattern between Gated DeltaNet and gated full attention. It has a context window size of $256$K tokens.
- • 
Qwen 3 Coder Next \[9\] is a sparse MoE model with 80B total and 3B active parameters, served in NVFP4. It uses the same hybrid Gated DeltaNet/full-attention pattern and has a context window size of $256$K tokens.
- • 
Gemma 4 31B \[16\] is a 31B-parameter dense model served from GGUF Q4\_K\_M weights. It interleaves $1024$-token local sliding-window attention with global-attention layers and has a context window size of $256$K tokens.
- • 
Step 3.7 Flash (198B A11B) \[40\] is a sparse MoE model with 198B total and 11B active parameters, served from GGUF Q3\_K\_M weights. It interleaves $512$-token sliding-window and full-attention layers in a 3:1 pattern, uses head-wise gated grouped-query attention, and has a context window size of $256$K tokens.
- •

### 2.4 Harnesses

We use two closely related base harnesses. Both implement a minimal ReAct loop: the task is supplied in an initial user message, the model issues one Bash action at a time, and each action and its result are appended to the conversation \[49\]. When used, the Bash environment exposes the files, programs, and benchmark-specific utilities available to the agent. Each Bash invocation treats the related standard output, return code, and any execution error as action results.

##### mini-swe-agent.

For software-engineering and terminal tasks, we use the released mini-swe-agent harness \[41\], with only the environment integration required by each benchmark. Its system prompt describes the software-engineering workflow, and its Bash environment provides the task repository or container. When done, the agent submits its proposed pull request as a patch for evaluation.

##### mini-agent.

For the remaining benchmarks, we use our mini-agent harness, which is a straightforward generalization of mini-swe-agent away from software engineering. It retains the same agent loop, model interface, and Bash interface, but uses benchmark-specific instructions, environments, and submission rules. The instructions specify the available commands, task procedure, and required answer format. Only the system instruction and task description are provided in the initial user message. Supporting inputs and tools are made available through the environment. When done, an evaluation benchmark adapter recognizes the designated submission command, extracts its payload, terminates the episode, and records the prediction in the benchmark evaluator’s required format.

#### 2.4.1 Accommodations for long conversational context

We compare three context-management regimes applied to the base harnesses described above. These regimes determine which interaction history is presented to the model. The regimes’ functioning is illustrated in Figure 3.

##### Full-History Accumulation (FHA).

The baseline full-history accumulation regime appends every model action and environment observation to a single conversation for the duration of the task. No history is removed or replaced during a run. This is the default mode of operation for mini-swe-agent and mini-agent.

##### End-of-Conversation Compaction (EoCC).

This regime follows the full-history ReAct loop until the length of the conversational context crosses a pre-specified compaction threshold. The model is then instructed within the active conversation to produce a bounded, task-relevant compaction of its state (see Appendix A). A higher total context limit reserves space for this compaction turn and terminates the conversation if compaction does not complete in time. The harness starts a fresh conversation containing the original task and the compacted state, and execution resumes under the same system prompt. This cycle repeats whenever the compaction threshold is crossed. We write these two values as “total context limit / compaction threshold” in tokens.

##### Single-Action Compaction (SAC).

This regime maintains a compact semantic state and essentially no conversational history. Each conversation receives the task and current semantic state, performs exactly one environment action, observes its result, and updates the semantic state. The harness then discards that conversation and starts a fresh one for the next action. For the experiments in Section 5, we apply SAC as a context-management regime to mini-swe-agent; the underlying agent harness, model, and task environment otherwise remain unchanged. SAC therefore keeps the active conversational context shortest of the three regimes and operationalizes the single-action setting of 3.

##### Context length measures.

We distinguish *total length* from *peak length*.
For a full-history baseline, total length is the length of its execution’s conversation.
For EoCC and SAC, total length is the sum of the final lengths of all conversations created during the execution.
Peak length is the length of the largest conversation produced during the task.
Both measures are expressed in thousands of tokens (K) and summarized across tasks as mean / median / maximum or median / maximum, as indicated in each table.

#### 2.4.2 Accommodations for long inputs

We enable selective input reading by storing each long input as one or more documents (e.g., input01.txt, input02.txt) in the agent’s filesystem environment rather than placing their full contents in the initial conversation. The task message identifies the available documents, and the agent performs selective input reading using standard Bash tools (e.g., sed, awk, head). This method of input presentation makes selective input reading an explicit environment action and thereby reduces a long-input workload to a long-horizon workload. We provide the agent instructions and examples of selective reading in Appendix E.

### 2.5 Latency and throughput measurement

##### Cloud serving.

For each model, we use the smallest H100 node-deployment that can hold the served checkpoint and a KV cache at the maximum evaluated context window size: eight H100 GPUs for Qwen 3 Coder Next and sixteen for GLM 5.2 and Kimi K2.6. For each context window size, we draw request lengths uniformly from nested prefixes of a shared token sequence, with sufficient space reserved for generation. We prefill the longest prefix once, enable prefix caching, and require every subsequent prefix request to generate exactly $1,024$ tokens. After warm-up, we sweep request concurrency and measure sustained aggregate decode throughput as completed output tokens divided by elapsed time. We report the highest-throughput setting with no KV-cache preemption; repeated measurements varied by at most 2%. The results are in Figure 4. The cost values in Figure 1 convert these throughput measurements to the cost of $1$M output tokens using the stated hourly GPU price.

##### Local serving.

On the DGX Spark, we evaluate one model instance and one request at a time. For each model, we construct a sequence at its maximum supported length and measure generation after prefixes of increasing length drawn from that sequence. At each length, we record the mean inter-token latency over the next $1,024$ generated tokens and the total device-memory consumption. The batch-one decode throughput in Figure 2 is the reciprocal of the mean inter-token latency.

## 3 Long-horizon tasks don’t need long contexts

*Can long-horizon tasks be completed without long contexts?*Answer: Yes. Frequent compaction keeps the context short while broadly maintaining task accuracy.

Following the outline of Section 2, we evaluate EoCC on 6 benchmarks representing long-horizon workloads and measure the performance of EoCC-modified harnesses against their baseline FHA counterparts. For each benchmark and model, we sequentially decrease the total context token limit and the corresponding compaction threshold to fit the total context limit. This has the effect of lowering the maximum context window needed by the model and of triggering increasingly more frequent compactions while executing long-horizon tasks. We describe what these compactions are designed to preserve in Appendix A. For SWE-bench Verified, TerminalBench 2.1, SWE-bench Multilingual, and FRAMES, we evaluate the models at total context limits / compaction thresholds (cf. Section 2.4.1) of $48$K/$36$K, $32$K/$24$K, $24$K/$18$K, and $16$K/$12$K. For BFCLv3, we consider $24$K/$18$K, $16$K/$12$K, and $12$K/$8$K, while for Tau2Bench, we consider $16$K/$12$K, $12$K/$8$K, and $8$K/$6$K.

Figure 5 plots the EoCC accuracies and estimated cost savings relative to FHA baselines against increasing levels of compaction.

Skimming through the line plots, observe first that the performance broadly remains flat, sometimes falling a few points below, sometimes remaining elevated above the baseline. More specifically, across all benchmarks and compaction thresholds, the relative performance of Opus 4.5 ranges from -3.7 to +5.6ppts, while the relative performance of GPT 5.6 Sol ranges from -3.3 to +4.4. The ranges are somewhat deceiving when considered by themselves, however: for either model, no more than 5 out of 22 threshold configurations lose more than 2ppts of the baseline. Secondly, observe the multiples of cost savings across all benchmarks, ranging from 2.2x to 8.8x for Opus 4.5 and from 2.4x to 5.0x for GPT 5.6 Sol. These represent the estimated cost savings as a consequence of serving only shorter context window sizes, and are considerable.

One pathology that could occur due to frequent compaction is that while it may successfully enforce smaller context window size, the full workflow history might be becoming longer as a consequence of the model having to re-do previously done tasks or to revisit previously seen information. Such behavior could result in an increased total token spend per task, ultimately erasing some of the cost savings due to smaller context windows. In our experimentation, this was generally not the case. Detailed per-benchmark accuracy, token spend, total length, cost and their discussion are provided in Appendix C.

In sum, we observe that even the naive approach to keeping context short by compacting agent’s work history once its conversation reaches a certain restrictive threshold leads to, broadly-speaking, on-par performance in model performance on long-horizon tasks when using frontier closed-weight models. Complementary results for open-weight models are provided in Appendix D. It would seem that the benefits of maintaining long contexts manifest themselves inconsistently and are not drastic so as to discourage efforts to keep the working context short in autonomous agentic workloads. Hence our answer to 1: yes.

### 3.1 Long-horizon tasks may sometimes need the history

Long-horizon tasks may sometimes need the history, but that does not mean that they require long contexts.

Compaction is a lossy context compression method. Information will be lost as a consequence of compacting a conversational history. Even more information will be lost if the conversational history being compacted already contains a result of an earlier compaction.

It is not too difficult to construct a task whose accuracy is guaranteed to suffer when a compaction is performed. Consider, for example, an agent that has access to a tool that generates coin tosses and reports the outcome of each coin toss in its tool result. With a compaction budget fixed, the agent is guaranteed to eventually start losing information about the outcomes of some of the coin tosses. If, at some point, the agent needs to inspect the sequence of coin toss outcomes (e.g., access the $i$th outcome), it is guaranteed to eventually fail as a consequence of some compaction necessarily eliminating some of its toss outcome records, with the compaction being the cause.

Observe, however, that any such example can be eliminated by creating a harness that keeps a record of every message of any agentic conversation, and makes it readily accessible to the agent by the means of a selective reading tool. The querying of the agent’s conversational history then becomes a long-input task, which we tackle in 2.

In other words, there is a difference between information that needs to be a part of model context and information that could, in principle, be retrieved selectively on a “need-to-know basis”.

Note that the findings of our experimentation above are not that “you don’t ever need to access conversational history”, but roughly that “you don’t need to keep the entire conversational history in the context in order to complete long-horizon tasks”.

## 4 Long-input tasks don’t need long contexts

*Can long-input tasks be completed without long contexts?*Answer: Yes. Selective input reading and compaction keep contexts short, maintaining task accuracy.

We evaluate EoCC on 7 benchmarks representing long-input workloads and measure the performance of EoCC-modified harnesses against their baseline full-input counterparts. For each benchmark and model, the full-input baseline receives the entirety of the input as prescribed by the benchmark while the compacting harness uses Bash tools to perform selective reading of inputs from environment filesystem (see Appendix E). Where appropriate in EoCC runs, we further sequentially decrease the total context token limit and the corresponding compaction threshold to fit the total context limit. For many long-input tasks (especially the needle-based tasks), one restrictive total token limit is enough to showcase on-par or better performance.

Figure 6 plots the EoCC accuracies and estimated cost savings relative to FHA baselines against one or multiple levels of compaction.

Looking through the line plots, observe first that the performance broadly remains flat, sometimes falling a few points below, sometimes remaining elevated above the baseline. More specifically, across all benchmarks and compaction thresholds, the relative performance of Opus 4.5 ranges from -0.4 to +40.0ppts, while the relative performance of GPT 5.6 Sol ranges from +1.0 to +30.9 (!). Observe also the multiples of cost savings across all benchmarks, ranging from 6.5x to 54.6x for Opus 4.5 and from 4.4x to 233.3x for GPT 5.6 Sol. These represent the estimated cost savings as a consequence of both selective input reading and serving only shorter context window sizes, and warrant serious consideration.

Figures 7 and 8 plot total conversation length, summed across stretches, against document length. On logarithmic document-length axes spanning orders of magnitude, conversation lengths on the linear vertical axes remain concentrated in broadly similar bands for most tasks, with some longer outliers. The dashed equal-length reference $y=x$ rises exponentially in these plotting coordinates, whereas most conversations do not grow proportionally with document length. This shows that even as document length increases, the conversation length remains broadly bounded.

Detailed per-benchmark accuracy, token spend, cost, compactions and their discussion are provided in Appendix F.

In summary, we observe that selective input reading, with compaction available as a fallback, matches or improves long input baseline performance across almost all long-input benchmarks and remains close to baseline in the remaining case, while keeping peak live context far below baseline conversation lengths. The near-zero median number of compactions and the roughly constant conversation lengths as document size grows support the intuition that despite the long inputs provided to tasks, the actual amount of information required to solve those tasks remains low. Thus, the size of a task’s input does not itself establish a need for long context. Hence our answer to 2: yes.

## 5 Compaction can be performed after every action

*Can long-horizon tasks be completed taking no more than a single action per context?*Answer: Yes. Single-action compaction maintains an effective compact semantic state.

The combined comparison in Table 2 shows that, for Claude Opus 4.5, SAC preserves the mini-swe-agent baseline accuracy on SWE-bench Verified and improves it by 4.6 percentage points on Terminal-Bench. For GPT 5.6 Sol, SAC reaches 82.4% on SWE-bench Verified and 84.3% on Terminal-Bench (75 of 89 tasks solved), below its mini baseline by 2.0 and 3.3 percentage points, respectively. Meanwhile, across both models and benchmarks, median peak live context under SAC is only $7$–$9$K tokens, and the maximum falls from $130$–$200$K to $15$–$37$K tokens.

Thus, SAC preserves or improves baseline accuracy for Claude Opus 4.5, while GPT 5.6 Sol incurs small accuracy reductions. This is somewhat remarkable, considering that both models reduce each interaction to a single action and carry only a compact semantic state between contexts. The resulting live contexts are far shorter than the full-history conversations, showing that compaction frequency can be pushed to relative extremes without catastrophic consequences for task accuracy. Hence our answer to 3: yes.

### 5.1 Semantic State Space Models (SSSMs).

The above observations of Section 5 and earlier observations of Sections 3 and 4 force a reflection: If powerful models can broadly maintain performance by compacting often or even compacting after taking a single action, cannot all long-context workflows be coerced into becoming single-action workflows through compaction? In other words, could not all models potentially be performing single-action compaction (SAC) by default? To do so would roughly correspond to maintaining a semantic state across long-context workflows.

We propose the notion of a Semantic State Space Model (SSSM). A SSSM is a model post-trained to (1) comprehend an input language description of a state of a conversation, (2) reason about the appropriate next action or about the task at hand, (3) take an action, (4) register its outcome, and (5) update the language description of the conversation’s state with the reasoning conclusions, action decisions, and action outcomes in a way that allows a separate inference instance of the SSSM to continue the conversation toward completion. The notion of a SSSM is closely related to that of a State-Space Model \[20, 19, 18\]. Unlike an SSM, which maintains a black-box neural state between token generations, an SSSM maintains an explainable natural language (hence “semantic”) state between turns of a continuing conversation.

The utility of SSSMs as opposed to existing conversational models trained for growing full-history conversations lies in their increased token efficiency – as shown in Figure 1, there is a considerable cost benefit to maintaining short contexts. We further surmise that it is considerably more data-efficient to train semantic state-space models due to the lack of need to teach the model to pay attention to the suitable patches of earlier context. Ultimately, we see no reason why SSSMs could not match the performance of full-history-accumulating models, which begs the question: Why train full-history-accumulating models in the first place?

## 6 Conclusion

Our experiments provide affirmative answers to all three research questions 1, 2 and 3. In particular, we found that on long-horizon tasks, even simple end-of-conversation compaction usually matches or slightly improves on full-history accuracy, with only modest losses in the remaining settings. We showed that on long-input tasks, selective input reading with compaction as a fallback matches or improves (sometimes considerably) the full-input baselines in almost every case while keeping live context short. Finally, single-action compaction nearly preserves or improves on the baseline accuracy while carrying only a compact semantic state between actions.

1, 2 and 3 were motivated by the root question 0: “Are long contexts necessary?” Based on the affirmative answers to all of the above, we conclude that long contexts are not necessary for the completion of “long-context” tasks. This is far from surprising. After all, the very motivation behind the definition of computability rests on the assumption that anything computable may be computed by comprehending only a bounded amount of input at a time and maintaining only a finite state of mind \[44\].

Our evidence does not rule out the existence of tasks for which long context is beneficial, nor does it prove that every possible task can be solved with short context. It does, however, show that the standard arguments in favor of long contexts stemming from long input and long conversational horizons are insufficient: disciplined state maintenance and selective access remove the presumed necessity in every setting we tested. We believe that with the appropriate adjustments made to the post-training of LMs, the context window size requirements currently imposed on these models by the standard arguments for long contexts could be removed, and model context window sizes could shrink drastically, significantly improving the cost of token generation on the cloud and the speed of token generation on local inference accelerators.

## References

- \[1\] (2025) Introducing NVFP4 for efficient and accurate low-precision inference. Note: NVIDIA Technical Blog External Links: Link Cited by: §2.3.
- \[2\] (2025) Introducing Claude Opus 4.5. Note: Official announcement External Links: Link Cited by: Table 1.
- \[3\] (2026) Claude Opus 4.5 model overview and pricing. Note: Claude Platform documentationAccessed September 29, 2026 External Links: Link Cited by: Appendix B, Table 3.
- \[4\] (2025) Artificial analysis long context reasoning benchmark (LCR). Artificial Analysis, Inc.. Note: Hugging Face dataset External Links: Link Cited by: 3rd item.
- \[5\] (2024) QUIK: towards end-to-end 4-bit inference on generative large language models. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp. 3355–3371. External Links: Document, Link Cited by: §1.
- \[6\] (2025) LongBench v2: towards deeper understanding and reasoning on realistic long-context multitasks. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Vienna, Austria, pp. 3639–3664. External Links: Document, 2412.15204, Link Cited by: 2, 1st item.
- \[7\] (2025) $\tau^{2}$-Bench: evaluating conversational agents in a dual-control environment. External Links: 2506.07982, Link Cited by: 5th item.
- \[8\] (2020) Exploiting NVIDIA ampere structured sparsity with cuSPARSELt. Note: NVIDIA Technical Blog External Links: Link Cited by: §1.
- \[9\] (2026) Qwen3-Coder-Next technical report. External Links: 2603.00729, Link Cited by: Table 1, 3rd item, 2nd item.
- \[10\] (2026) The MiniMax-M2 series: mini activations unleashing max real-world intelligence. External Links: 2605.26494, Link Cited by: 5th item.
- \[11\] (2025) SWE-Bench Pro: can AI agents solve long-horizon software engineering tasks?. External Links: 2509.16941, Link Cited by: 1.
- \[12\] (1998) Great expectations. Note: Project GutenbergProject Gutenberg eBook no. 1400 External Links: Link Cited by: Table 1.
- \[13\] (2026) Introducing Gemini 3.8 Flash and 3.8 Flash Cyber. Note: Google official blog External Links: Link Cited by: Table 1.
- \[14\] (2024) Extreme compression of large language models via additive quantization. In Proceedings of the 41st International Conference on Machine Learning, Proceedings of Machine Learning Research, Vol. 235, pp. 12284–12303. External Links: Link Cited by: §1.
- \[15\] (2021) The great gatsby. Note: Project GutenbergProject Gutenberg eBook no. 64317 External Links: Link Cited by: Table 1.
- \[16\] (2026) Gemma 4 technical report. External Links: 2607.02770, Link Cited by: Table 1, 3rd item.
- \[17\] (2026) GLM-5: from vibe coding to agentic engineering. External Links: 2602.15763, Link Cited by: 1st item.
- \[18\] (2024) Mamba: linear-time sequence modeling with selective state spaces. External Links: 2312.00752, Link Cited by: §5.1.
- \[19\] (2022) Efficiently modeling long sequences with structured state spaces. External Links: 2111.00396, Link Cited by: §5.1.
- \[20\] (2021) Combining recurrent, convolutional, and continuous-time models with linear state space layers. In Advances in Neural Information Processing Systems, M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. W. Vaughan (Eds.), Vol. 34, pp. 572–585. External Links: Link Cited by: §5.1.
- \[21\] (1952) The old man and the sea. Charles Scribner’s Sons, New York. Cited by: Table 1.
- \[22\] (2024) RULER: what’s the real context size of your long-context language models?. External Links: 2404.06654, Link Cited by: 5th item.
- \[23\] (2024) SWE-bench: can language models resolve real-world GitHub issues?. In The Twelfth International Conference on Learning Representations, External Links: 2310.06770, Link Cited by: 1st item.
- \[24\] (2023) Needle in a haystack: pressure testing LLMs. Note: GitHub repositoryCanonical benchmark implementation; no arXiv paper External Links: Link Cited by: 4th item.
- \[25\] (2023) On the computational complexity of self-attention. In International conference on algorithmic learning theory, pp. 597–619. Cited by: §1.
- \[26\] (1989) The king james version of the bible. Note: Project GutenbergProject Gutenberg eBook no. 10 External Links: Link Cited by: Table 1, Table 1.
- \[27\] (2025) Fact, fetch, and reason: a unified evaluation of retrieval-augmented generation. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Albuquerque, New Mexico, pp. 4745–4759. External Links: Document, 2409.12941, Link Cited by: 4th item.
- \[28\] (2024) BABILong: testing the limits of LLMs with long context reasoning-in-a-haystack. In Advances in Neural Information Processing Systems, Vol. 37, pp. 106519–106554. External Links: Document, 2406.10149, Link Cited by: 7th item.
- \[29\] (2024) Lost in the middle: how language models use long contexts. Transactions of the Association for Computational Linguistics 12, pp. 157–173. External Links: Document, Link Cited by: 2.
- \[30\] (2026) Terminal-Bench: benchmarking agents on hard, realistic tasks in command line interfaces. External Links: 2601.11868, Link Cited by: 3rd item.
- \[31\] (2026) MiniMax-M2.7 checkpoint configuration. Note: Official Hugging Face model repositoryAccessed October 27, 2026 External Links: Link Cited by: Table 1, 5th item.
- \[32\] (2026) Kimi K2.6: from code to creation, from one to many. Note: Official model releaseAccessed September 14, 2026 External Links: Link Cited by: Table 1, 2nd item.
- \[33\] (2025) NVIDIA DGX spark arrives for world’s AI developers. Note: NVIDIA Newsroom External Links: Link Cited by: §2.3.
- \[34\] (2026) GPT-5.6 Sol model pricing. Note: OpenAI API documentationAccessed September 29, 2026 External Links: Link Cited by: Appendix B, Table 3.
- \[35\] (2026) GPT-5.6 Sol model specifications. Note: OpenAI API documentationAccessed September 16, 2026 External Links: Link Cited by: Table 1.
- \[36\] (2025) The berkeley function calling leaderboard (bfcl): from tool use to agentic evaluation of large language models. In Forty-second International Conference on Machine Learning, Cited by: 6th item.
- \[37\] (2026) Qwen3.6-27B: flagship-level coding in a 27B dense model. External Links: Link Cited by: 1st item.
- \[38\] (1997) The qur’an: arabic text with corresponding english meanings. Abul-Qasim Publishing House, Jeddah, Saudi Arabia. Cited by: Table 1.
- \[39\] (2025) Counting-Stars: a multi-evidence, position-aware, and scalable benchmark for evaluating long-context large language models. In Proceedings of the 31st International Conference on Computational Linguistics, Abu Dhabi, UAE, pp. 3753–3763. External Links: 2403.11802, Link Cited by: 6th item.
- \[40\] (2026) Step-3.7-Flash model card. Note: Hugging Face model cardAccessed September 14, 2026 External Links: Link Cited by: 4th item.
- \[41\] (2025) mini-swe-agent: the minimal AI software engineering agent. External Links: Link Cited by: §G.1, §2.4.
- \[42\] (1954) The lord of the rings. George Allen & Unwin, London. Note: Three volumes Cited by: Table 1.
- \[43\] (2001) War and peace. Note: Project GutenbergProject Gutenberg eBook no. 2600 External Links: Link Cited by: Table 1.
- \[44\] (1937) On computable numbers, with an application to the Entscheidungsproblem. Proceedings of the London Mathematical Society s2-42 (1), pp. 230–265. External Links: Document, Link Cited by: §6.
- \[45\] (2024) Leave no document behind: benchmarking long-context LLMs with extended multi-doc QA. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Miami, Florida, USA, pp. 5627–5646. External Links: Document, 2406.17419, Link Cited by: 2, 2nd item.
- \[46\] (2015) Towards AI-complete question answering: a set of prerequisite toy tasks. External Links: 1502.05698, Link Cited by: 7th item.
- \[47\] (2024) SWE-agent: agent-computer interfaces enable automated software engineering. In The Thirty-eighth Annual Conference on Neural Information Processing Systems, External Links: Link Cited by: 1.
- \[48\] (2025) SWE-smith: scaling data for software engineering agents. External Links: 2504.21798, Link Cited by: 2nd item.
- \[49\] (2023) ReAct: synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning Representations, External Links: 2210.03629, Link Cited by: §2.4.
- \[50\] (2026) GLM-5.2 model card. Note: Hugging Face model cardAccessed September 14, 2026 External Links: Link Cited by: 1st item.
- \[51\] (2026) GLM-5.2. Note: Official model release blog External Links: Link Cited by: Table 1.
- \[52\] (2023) WebArena: a realistic web environment for building autonomous agents. arXiv preprint arXiv:2307.13854. External Links: Link Cited by: 1.

## Appendix A What characterizes a good compaction?

It is a common experience of human-in-the-loop agent-aided SWE workflows that after a compaction is performed, certain crucial information disappears from the context and has to be obtained again, slowing down the SWE process or perhaps even confusing the model and losing crucial user preferences included in previous instructions. Note that human-in-the-loop agent-aided SWE workflows consist of two parts: autonomous SWE work performed by the agent, and reception and comprehension of the human’s steering feedback. Because of this, compactions produced for such workflows need to account for not only the information the agent needs to achieve its goals, but also for all potential information that might be relevant to follow-up autonomous work that might be triggered as a result of the human’s feedback.

In our experimentation, we initially set out to identify the cheapest, most useful method of compaction that can preserve as much task accuracy as possible on autonomous SWE work. We discovered that treating compaction as a mere special case of summarization is suboptimal for this purpose. LM summarizations generally attempt to give equal weight to all facts present in the input and are prone to overemphasize repeated segments of the agent trace regardless of their ultimate relevance to the tail of the trace being compacted. We explored the subject along two axes: the method (e.g., summarization or message pruning) and the information being pruned (e.g., the entire trace or only the trace segment since the last compaction plus the contents of the last compaction). We discovered that the best compactions are not those that faithfully capture the gist of the agentic trace, but those that best select facts relevant to the work yet to be performed – i.e., they are not narratives of the execution history but carefully cherry-picked briefs for further execution. In particular, we found that the most accuracy-preserving compactions, regardless of the frequency of compaction, are those that contain (1) a verbatim or near-verbatim copy of the input task, (2) a record of agent’s current occupation, intentions, and planned next steps, and (3) all the artifacts that are of direct relevance to future execution, including (3a) a decomposed plan made from the input task, (3b) a list of requirements detailing when to consider the task complete, and any pieces of information or pointers to artifacts containing information that is of relevance to the aforementioned two. Finally, we found that the above structure of compactions readily extends even to workflows that are not necessarily SWE-related in their nature. We used the same compaction structure for every type of workflow considered in this work.

## Appendix B Estimated optimized retail cost

For model $M$, let $C_{\text{output},M}(W)$ denote the USD per million output tokens at size $W$. For measured models, let $T_{M}(W)$ be the peak aggregate decode throughput (output tokens per second after input-context processing, assuming KV cached input). Fixed GPU allocation and hourly rate imply the $16$K-to-$256$K cost ratio

|  | $$ r_{M}=\frac{C_{\text{output},M}(16\mathrm{K})}{C_{\text{output},M}(256\mathrm{K})}=\frac{T_{M}(256\mathrm{K})}{T_{M}(16\mathrm{K})}=\begin{cases}0.2772&\text{GLM 5.2},\\ 0.1777&\text{Kimi K2.6},\\ 0.1439&\text{Qwen 3 Coder Next}.\end{cases} $$ |  | (1) | 

We take the rounded mean of the above measurements, $r=0.20$.

For target frontier model $M$, let $W^{\text{max}}_{M}$ be the assumed reference context window size: $200,000$ tokens for Opus 4.5 and $272$K for GPT 5.6 Sol \[3, 34\]. The GPT’s $272$K reference context window size is its standard-price ceiling (the model supports $1,050,000$ tokens, but our compaction $W$ never exceeds the standard-price ceiling). For each compaction experiment, let $W\leq W^{\text{max}}_{M}$ be the EoCC total context limit and let $W^{\text{max}}_{M}$ be the context window size for the FHA baseline (Section 2.4.1). To estimate the cost of output $C^{\text{estimate}}_{\text{output},M}(W)$ of model $M$, we anchor $C_{\text{output},M}(W^{\text{max}}_{M})$ at the standard retail output price, $25 for Opus 4.5 or $20 for GPT 5.6 Sol, and then interpolate to $r$-times-the-standard-price at $16$K, clamping smaller $W$s:

|  | $$ C^{\text{est.}}_{\text{output},M}(W)=C_{\text{output},M}(W^{\text{max}}_{M})\left[r+(1-r)\frac{\max(W,16\mathrm{K})-16\mathrm{K}}{W^{\text{max}}_{M}-16\mathrm{K}}\right]. $$ |  | (2) | 

Let $C_{\text{input},M}(W)$ and $C_{\text{cached},M}(W)$ be the est. USD per million uncached-input and cached-input tokens, respectively. These we deduce by preserving the original 5:1 output-to-uncached-input ratio and 10:1 uncached-input-to-cached-input ratio of the frontier models:

|  | $$ C_{\text{input},M}(W)=\frac{C^{\text{est.}}_{\text{output},M}(W)}{5},\qquad C_{\text{cached},M}(W)=\frac{C^{\text{est.}}_{\text{input},M}(W)}{10}. $$ |  | (3) | 

For every experiment with model $M$ maintaining the EoCC total context limit at $W$, let $I$, $H$, and $O$ be aggregate millions of uncached input, cached input (cache hits), and generated output tokens, respectively.
We compute the estimate of the final *estimated optimized retail cost* as reported in the paper as:

|  | $$ {EORC}_{M}(W)=IC^{\text{est.}}_{\text{input},M}(W)+HC^{\text{est.}}_{\text{cached},M}(W)+OC^{\text{est.}}_{\text{output},M}(W). $$ |  | (4) | 

## Appendix C Detailed long-horizon results

The tables below report accuracy and cost profiles for Claude Opus 4.5 and GPT 5.6 Sol. Each table compares a baseline FHA agent (Section 2.4) against an EoCC agent with different total context limits and compaction thresholds (Section 2.4.1). Values are written as “total context limit / compaction threshold” in tokens: the agent compacts when the running context approaches the compaction threshold and never exceeds the total context limit.

Throughout the results, notice the following:

- • 
In terms of accuracy, compactions tend to perform closely on-par with or slightly better than the corresponding baseline.
- • 
In terms of total token spend, new input token counts generally increase with decreasing context window size while the re-used cached tokens generally decrease, consistently with the intuitive expectation. Output tokens are generally elevated when compacting.

Inspecting Table 3, we observe that every evaluated pair of total context limit and compaction threshold matches or improves on the baseline for GPT 5.6 Sol; Claude Opus 4.5 improves at every setting except the tightest ($16$K / $12$K), where accuracy decreases by 1.2 percentage points. The best results improve accuracy by 4.8 percentage points for Claude Opus 4.5 and 4.4 points for GPT 5.6 Sol.

On SWE-bench Multilingual (Table 4), the largest accuracy gains occur at $48$K / $36$K: 1.7 percentage points for Claude Opus 4.5 and 0.7 points for GPT 5.6 Sol. At the tightest setting ($16$K / $12$K), accuracy falls below the corresponding baselines by 2.0 and 1.6 percentage points, respectively.

The Terminal-Bench results in Table 5 show a similar pattern: compaction improves Claude Opus 4.5 at every evaluated pair of total context limit and compaction threshold. GPT 5.6 Sol improves by 1.2 percentage points at $48$K / $36$K and loses 1.1, 2.2, and 2.2 points at $32$K / $24$K, $24$K / $18$K, and $16$K / $12$K, respectively. The largest gain is 5.6 percentage points for Claude Opus 4.5 with a $32$K total context limit and $24$K compaction threshold.

As shown in Table 6, on FRAMES, compaction reduces accuracy by 1.3–3.7 percentage points for Claude Opus 4.5 and 1.5–3.3 points for GPT 5.6 Sol relative to their updated baselines of 81.0% and 90.2%. At $16$K / $12$K, the reductions are 1.4 and 3.1 points, while estimated optimized costs fall by $7.7\times$ and $3.8\times$, respectively.

On the 200 long-context multi-turn episodes of BFCLv3, Table 7 reports accuracy, token consumption, compaction frequency and accumulated total context.

Finally, Table 8 shows that compaction keeps Claude Opus 4.5 within 1.1 percentage points of its 79.3% baseline accuracy on $\tau^{2}$-bench: accuracy is 78.2% with a $12$K total context limit and $8$K compaction threshold, matches the baseline with $16$K / $12$K, and reaches 78.8% with $8$K / $6$K. GPT 5.6 Sol improves with a $12$K total context limit and $8$K compaction threshold and remains near its baseline with the other total context limits and compaction thresholds.

## Appendix D Open-weight model results

We also evaluate the five quantized open-weight models described in Section 2.3 on SWE-bench Verified and Terminal-Bench 2.1 (Tables 9 and 10). The compaction settings are $48$K / $40$K, $32$K / $24$K, and $16$K / $12$K, expressed as total context limit / compaction threshold.

Robustness to compaction varies across models. Qwen 3.6 27B and MiniMax M2.7 are comparatively robust, whereas Gemma 4 31B, Step 3.7 Flash, and especially Qwen 3 Coder Next show larger losses as the context budget tightens. Qwen 3 Coder Next catastrophically collapses on SWE-bench Verified from 53.0% to 3.6% at $16$K / $12$K, mostly because its verbose trajectories leave too little room for useful progress between compactions. At this tightest setting, every model loses SWE-bench accuracy relative to its baseline, although Qwen 3.6 27B and MiniMax M2.7 retain their Terminal-Bench baseline scores.

Observe that despite the gradual tightening of the compaction threshold, all models maintain their ability to complete a significant fraction of the benchmark workflows successfully. This goes on to show that even small- to medium-sized compact coding models with no explicit compaction post-training exhibit material utility while operating with shorter context window sizes.

## Appendix E Selective reading of long inputs

Our generalized adaptation of mini-swe-agent, mini-agent, exposes long benchmark inputs as text files that the agent can inspect through a bash tool. LongBench v2 uses one document file, whereas LOONG and AA-LCR expose multiple source files. The operation of mini-agent is straightforward. The model receives the question and file information and then chooses which text to retrieve in order to start answering the question. A succession of Bash-invoked searches then scan entire files, but only their returned matched excerpts enter the model’s context.

The basic process of a single search is to identify the entities, quantities, or claims needed for the answer, and then to read a small surrounding window to interpret the candidate evidence. Further related searches might then be used to retrieve more candidates looked up using broader sets of synonyms. Standard commands such as grep, sed, head, and tail are the backbone of the search process. Convenience commands provide document sizes (doc-stats), file manifests (docs-list), bounded reads (doc-read), and search-term variants (doc-syn) allow for more surgical readouts from files and expanded search follow-ups.

### E.1 Instructions supplied to the agent.

The base system prompt gives the following man-like tool description:

The system prompt also makes the preference for selective reading explicit:

### E.2 Examples from recorded runs.

The following excerpts retain only commands and selected tool output. They are illustrative traces, not estimates of typical reading cost.

1\. LongBench v2: locate a word, then read its grammatical context. In the question of the dataset’s first sample, the agent translates a Kalamang sentence using a grammar of roughly $1$M characters ($19$K lines). It searches for a word from the sentence and uses the returned line number to select a 36-line passage.

Through a follow-up doc-read, the agent retrieves surrounding grammar and examples, rather than relying solely on the lexical match retrieved with the earlier grep.

2\. LOONG: search across papers, then verify a paper’s identity. The question of the dataset’s first sample asks for citation relationships among three supplied papers (roughly $138$K characters in total). The agent searches two other papers for the target paper’s name. Later, it reads only the beginning of the matching paper to verify its title.

This example combines a grep search across files with a surgical $1$K-character follow-up read.

3\. AA-LCR: read the context needed to apply an exclusion. The question of the second sample asks for industries ranked by consumer-related infringements over three decades, explicitly excluding broadcasting. Four supplied documents contain roughly $404$K characters. After narrowing the search to one report, the mini-agent retrieves a short passage containing the industry names, counts, and time span.

Here, a sequence of grep searches and doc-reads is executed until the key relevant passage has been identified.

## Appendix F Detailed long-input results

To demonstrate 2, we compare the performance of selectively-reading, compacting agents against the more straightforward benchmark baselines that involve pasting long inputs into the models’ work conversations. Following the long-input accommodations in Section 2.4.2, the agents tested read only task-relevant portions of each document and use compaction when their working context reaches the compaction threshold. Compaction thresholds are reported as “total context limit / compaction threshold” in tokens.

LongBench v2 shows that selective input reading preserves baseline-level accuracy without placing the full documents in the models’ working context. In Table 11, GPT 5.6 Sol improves by 1.8 percentage points and Claude Opus 4.5 remains within 0.4 points of its baseline. The $16$K total context limit bounds peak live context, while compaction events remain infrequent.

LOONG provides the clearest realistic multi-document result in support of our answer to 2: every setting in Table 12 improves both average score and perfect-answer rate for both models over the full-input baseline. Depending on the setting, peak live context is bounded at $16$–$48$K tokens. Compaction is correspondingly rare: both models have a median of zero compactions at the two larger settings, and even at $16$K / $12$K the medians are very low.

AA-LCR shows the same benefit on multi-document reasoning (Table 13). At $16$K / $12$K, Claude Opus 4.5 reaches 84.0% accuracy versus 65.0% for the full-input baseline, while GPT 5.6 Sol reaches 83.0% versus 82.0%.

On NIAH, selective input reading raises both models to 100% accuracy (Table 14). The agents find the relevant evidence so directly that neither model performs a single compaction. We attribute the stark success on this benchmark to existence of some more straightforward lexical overlap between the needles (and their known common synonyms) and the questions that are used to search for the needles. Here we take the opportunity to also note that the entire concept of needle-in-a-haystack benchmarks is based on the premise that there is such a thing as a long-context task. Starting from that premise, needle-in-a-haystack benchmarks are proposed as a proxy to evaluate model abilities to retrieve from such context as a part of operations the model under evaluation might have to perform in order to deal with the supposedly existing class of long-context tasks. Again, we highlight that we have found no evidence of existence of inherently long-context tasks and have so far been able to address all tasks that have previously been producing long contexts by the simple means of selective input reading and compaction.

RULER further firmly supports our findings: mean recall rises from 62.5% to 95.7% for Claude Opus 4.5 and from 65.5% to 96.4% for GPT 5.6 Sol (Table 15). Peak live context is bounded by a $16$K total context limit. The median number of compactions is zero for both models, showing that selective input reading usually solves the tasks before any compactions are needed.

On Counting-Stars, selective input reading reaches a 99.7% mean score and 81.2% exact match for both models, improving the exact-match rate from 65.1% for Claude Opus 4.5 and 76.6% for GPT 5.6 Sol (Table 16). Neither model performs any compaction, so the result comes entirely from reading only the relevant input portions.

BABILong combines selective input reading with a large accuracy gain (Table 17), where accuracy improves by 24.9 percentage points for Claude Opus 4.5 and 23.3 points for GPT 5.6 Sol. Peak live context is bounded at $16$K tokens. GPT 5.6 Sol never compacts, and Claude Opus 4.5 performs at most one compaction per task, once again showing that selective input reading does nearly all of the context reduction.

## Appendix G Agent outlines

The templates below give outlines of the structure of compaction prompts in mini-swe-agent and mini-agent used in this work.

### G.1 mini-swe-agent

We use the released mini-swe-agent harness \[41\] v2.4, with negligible changes for environment integration and context management. The underlying task-solving loop is fully retained.

To compact its earlier work, we use the following prompt passed as a user message once the compaction threshold is met.

##### Compaction prompt

### G.2 mini-agent

As described in Section 2, we generalize the base released mini-swe-agent harness into a mini-agent harness by removing SWE-specific instructions and adding instructions enabling additional classes of agentic workflows.

##### System prompt

##### User prompt

##### Compaction prompt

| Variable | Description | 
| task | Supplied question or task, including answer options and output requirements. | 
| input\_details | Source filenames, document manifest, sizes, working directory, and other instance metadata. | 
| tools | Available commands, arguments, and limits on retrieved text. | 
| work\_instructions | Evidence-gathering procedure, calculations, verification requirements, and permitted changes. | 
| command\_rules | Number of Bash calls required on work turns and shell execution behavior. | 
| submission\_instructions | Exact completion command and required answer or artifact format. | 
| context\_instructions | Instructions for resuming execution from the compacted state and producing the next compaction before starting a fresh conversation; empty without compaction. | 
| recap\_section | Instructions for continuing execution, followed by the compacted state from the preceding conversation; empty without compaction. | 
| recap | Compacted state inserted into recap\_section for the next conversation; initially a brief statement that no prior work exists. | 
| persistence | Which files and environment state remain available across conversations, and which information must be preserved in the compacted state. | 
| handoff\_details | Additional instructions specifying evidence, input coverage, calculations, or implementation state to preserve in the compaction. | 
| submission\_reminder | Checks required before task completion and the completion protocol to preserve in the compacted state. |
