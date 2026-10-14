# Research

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover uses one flat research lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next research cycle
```

**Current stage: 1 — Research.**  
Stage-1 freshness checked through: **2026-10-14**.

## Read this folder in order

| Stage | File | Purpose | Current status |
|---|---|---|---|
| 0 | [`PIPELINE.md`](PIPELINE.md) | explains the complete lifecycle | canonical |
| 1 | [`RESEARCH.md`](RESEARCH.md) | stable broad source/method/dataset/benchmark inventory | **ACTIVE** |
| 1 | [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md) | current primary/official sources that materially expand/challenge the inventory | **ACTIVE — refreshed 2026-10-14** |
| 2 | [`ANALYSIS.md`](ANALYSIS.md) | one-method-one-report mechanism analysis | template ready |
| 3 | [`SYNTHESIS.md`](SYNTHESIS.md) | compare strengths, weaknesses, trade-offs and gaps | future |
| 4 | [`INNOVATION.md`](INNOVATION.md) | Clover-original hypotheses / algorithms / ideas | ideas only |
| 5 | [`IMPLEMENTATION.md`](IMPLEMENTATION.md) | reproducible code and systems | future core stage |
| 6 | [`EVALUATION.md`](EVALUATION.md) | experiments and Results | framework ready |
| 7 | [`REFLECTION.md`](REFLECTION.md) | interpret failures and start the next cycle | future |

A new agent should start with `PIPELINE.md`, read the stable `RESEARCH.md` inventory, then scan `RESEARCH_FRONTIER.md` for the current research edge before opening deeper survey material.

## Current Stage 1 goal

The current objective is not to decide the next Clover architecture.

It is to collect the field broadly enough that later analysis is not biased by a narrow set of papers or historical Clover ideas.

Collect:

```text
research directions
canonical foundations
latest strong methods
primary papers
official project pages
open code / checkpoints
datasets
benchmarks
reported capabilities
known limitations
labs / projects to monitor
open questions
```

`RESEARCH.md` currently tracks dozens of directions including epistemology, classical geometry, static/video SSL, 3D/4D reconstruction, neural scene representations, object-centric models, scene graphs, persistent memory, physical reasoning, causal learning, active perception, system identification, generative world models, world-action models, VLA, robot foundation models, egocentric video, affordance learning, model-based control, uncertainty/OOD, continual learning and simulation/data engines.

`RESEARCH_FRONTIER.md` tracks newly important primary/official work such as execution-grounded world-model evaluation, trustworthiness/counterfactual evaluation, contact/deformable dynamics, video-to-simulation functional correctness, persistent semantic maps, amodal tracking, behavior-grounded physical parameter inference, general multimodal robotics reasoning and current open VLA/WAM baselines.

## 2026-10-14 frontier snapshot

The latest Stage-1 refresh adds or promotes these research references:

| Source | Type | Why Stage 1 should track it |
|---|---|---|
| Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/ | `OFFICIAL_REPORTED_RESULT` | current general multimodal physical reasoner spanning Real2Sim, closed-loop robot control, world-model steering and self-improvement; strong counter-hypothesis to robot-specific reasoning stacks |
| ERQA — https://github.com/embodiedreasoning/ERQA | `OPEN_SOURCE` | reproducible 400-example embodied/spatial reasoning diagnostic used by current frontier models |
| DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630 | `PRIMARY_PAPER` | separates RGB geometry from physical parameters learned through action-response; directly relevant to the identifiability boundary of “vision alone” |
| GR00T N1.7 — https://github.com/NVIDIA/Isaac-GR00T | `OPEN_SOURCE` | current strong open VLA/direct-policy baseline with human-video pretraining and cross-embodiment action representation |
| Being-M0.7 — https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | current latent world-action route transferring large-scale human visual-motion priors to humanoid control |
| HWAM — https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | current WAM route that explicitly predicts realized post-execution body state to model the action-execution gap |
| Identifiable World Models — https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | strengthens a hybrid alternative between opaque latent state and hand-designed explicit state |
| Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810 | `PRIMARY_PAPER` | active question-conditioned evidence/view acquisition for multi-view spatial reasoning |
| Agentic Video Understanding — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/ | `OFFICIAL_REPORTED_RESULT` | shows evidence-acquisition policy can change long-video accuracy/efficiency independently of base representation |
| RobotWorld — https://arxiv.org/abs/2610.10409 | `PRIMARY_PAPER` | exposes composition, persistent task-state, recovery and completion-verification failures across diverse robot-use tasks |
| Video2World — https://arxiv.org/abs/2610.04432 | `PRIMARY_PAPER` | separates visual/geometric similarity from dynamic and functional correctness in reconstructed worlds |

These entries are **research objects and comparators**, not Clover components.

## What the newest evidence changes

The current frontier strengthens several Stage-1 distinctions that should remain visible before Analysis begins:

```text
visual geometry
≠
hidden physical parameters

plausible future video
≠
executable action consequence

reference action
≠
realized robot state

strong general reasoner + tools
≠
proof of vision-only world understanding

long context / static sampling
≠
active evidence acquisition

opaque distributed latent
vs
explicit state
is not the only choice;
hybrid identifiable coordinates are now a serious alternative
```

## Detailed Stage-1 assets

The flat stage files are the primary navigation. Existing deeper material remains available as supporting evidence:

- [`survey/RESEARCH_OVERVIEW.md`](survey/RESEARCH_OVERVIEW.md) — visual research map.
- [`survey/BACKGROUND_RESEARCH.md`](survey/BACKGROUND_RESEARCH.md) — broad background synthesis.
- [`survey/SOURCE_MAP.md`](survey/SOURCE_MAP.md) — source → evidence → claim → limitation map.
- [`survey/FRONTIER_METHODS.md`](survey/FRONTIER_METHODS.md) — method-family references.
- [`survey/PAPERS.md`](survey/PAPERS.md) — paper/project/code index.
- [`survey/BENCHMARKS_TASKS.md`](survey/BENCHMARKS_TASKS.md) — benchmark and task inventory.
- [`survey/DATASETS_CODE.md`](survey/DATASETS_CODE.md) — datasets and reproducibility resources.
- [`dossiers/`](dossiers/) — deeper domain notes. These support Stage 1 Research and later Stage 2 Analysis; they are not separate project phases.

## Source policy

For durable claims, prefer:

```text
primary paper / preprint
official technical or model page
official open-source repository
company/lab reported capability (explicitly labeled)
secondary signal only for discovery
```

Every important source should preserve:

```text
exact URL
what it demonstrates
what it does not demonstrate
input / training provenance
reproducibility status
relevant dataset / benchmark
```

## Current rule

Do not prematurely promote Research material into Innovation.

The intended flow is:

```text
collect broadly
→ analyze important methods one by one
→ synthesize strengths / weaknesses / gaps
→ propose original hypotheses
→ implement
→ evaluate
→ reflect
```

**Research broadly first. Protect the question, not the current answer.**
