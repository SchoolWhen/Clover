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
| 1 | [`RESEARCH_STATE_VARIABLES.md`](RESEARCH_STATE_VARIABLES.md) | world-state variables, evidence routes and current observability map | **ACTIVE** |
| 1 | [`RESEARCH_IDENTIFIABILITY.md`](RESEARCH_IDENTIFIABILITY.md) | predictability vs observability vs identifiability; partial observability, interventions and information limits | **ACTIVE** |
| 1 | [`RESEARCH_PHYSICAL_PROPERTIES.md`](RESEARCH_PHYSICAL_PROPERTIES.md) | hidden physical properties, contact, deformables, topology change and intervention/counterfactual datasets | **ACTIVE — added 2026-10-14** |
| 1 | [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md) | current primary/official sources that materially expand/challenge the inventory | **ACTIVE — refreshed 2026-10-14** |
| 2 | [`ANALYSIS.md`](ANALYSIS.md) | one-method-one-report mechanism analysis | template ready |
| 3 | [`SYNTHESIS.md`](SYNTHESIS.md) | compare strengths, weaknesses, trade-offs and gaps | future |
| 4 | [`INNOVATION.md`](INNOVATION.md) | Clover-original hypotheses / algorithms / ideas | ideas only |
| 5 | [`IMPLEMENTATION.md`](IMPLEMENTATION.md) | reproducible code and systems | future core stage |
| 6 | [`EVALUATION.md`](EVALUATION.md) | experiments and Results | framework ready |
| 7 | [`REFLECTION.md`](REFLECTION.md) | interpret failures and start the next cycle | future |

A new agent should start with `PIPELINE.md`, read the stable `RESEARCH.md` inventory, inspect `RESEARCH_STATE_VARIABLES.md` to understand what “world state” may contain, then read `RESEARCH_IDENTIFIABILITY.md` to understand which variables are actually constrained by which evidence. `RESEARCH_PHYSICAL_PROPERTIES.md` deepens the weakly visible physical-property and irreversible-change boundary. `RESEARCH_FRONTIER.md` is the current research edge.

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

`RESEARCH_STATE_VARIABLES.md` makes the mother question more concrete by separating observable/geometric/entity/physical/latent-physical/functional/causal/epistemic state and recording whether current evidence comes from static RGB, passive video, active viewpoints, action-response or non-visual/privileged sensing.

`RESEARCH_IDENTIFIABILITY.md` establishes a theory vocabulary for Stage 1: a variable can be statistically predictable without being physically identifiable; more frames do not automatically remove ambiguity; actions can act as interventions that reveal otherwise hidden dynamics; and uncertainty may be the correct answer when multiple worlds remain compatible with the visual evidence.

`RESEARCH_PHYSICAL_PROPERTIES.md` now collects evidence about mass, center of mass/inertia, friction, stiffness/compliance, temperature, liquids/viscosity, granular packing, contact/deformation, cutting/splitting/merging and counterfactual/intervention datasets. It explicitly records where current strong work uses tactile, force, thermal, depth, simulator state or controlled actions rather than silently calling the result vision-only.

`RESEARCH_FRONTIER.md` tracks newly important primary/official work such as execution-grounded world-model evaluation, trustworthiness/counterfactual evaluation, contact/deformable dynamics, behavior-grounded physical parameters, articulated physical assets, video-to-simulation functional correctness, persistent semantic maps, amodal tracking, general multimodal robotics reasoning, current open VLA baselines and competing world-action-model state strategies.

## 2026-10-14 frontier snapshot

The latest Stage-1 refresh includes these research references:

| Source | Type | Why Stage 1 should track it |
|---|---|---|
| Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/ | `OFFICIAL_REPORTED_RESULT` | current general multimodal physical reasoner spanning Real2Sim, closed-loop robot control, world-model steering and self-improvement; strong counter-hypothesis to robot-specific reasoning stacks |
| ERQA — https://github.com/embodiedreasoning/ERQA | `OPEN_SOURCE` | reproducible embodied/spatial reasoning diagnostic used by current frontier models |
| DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630 | `PRIMARY_PAPER` | separates RGB geometry from physical parameters learned through action-response; directly relevant to the identifiability boundary of “vision alone” |
| Physically Guided Visual Mass Estimation — https://arxiv.org/abs/2601.20303 | `PRIMARY_PAPER` | explicitly formulates single-RGB mass inference as ill-posed and factorizes the problem through geometry/volume and material/density priors |
| PhysQuantAgent / VisPhysQuant — https://arxiv.org/abs/2603.16958 | `PRIMARY_PAPER` | real-object physical-quantity benchmark for mass estimation; useful but RGB-D, so not a strict V0/V1 comparator |
| ViTacPhys — https://arxiv.org/abs/2608.21355 | `PRIMARY_PAPER` | estimates mass/friction/stiffness for grasping using visual+tactile demonstrations; useful evidence about properties current systems do not rely on vision alone to infer |
| HEARTH — https://arxiv.org/abs/2609.23418 | `PRIMARY_PAPER` | RGB-thermal-3D temperature-aware manipulation dataset; provides a clear hidden-state boundary where visible appearance alone can be insufficient |
| PointCast — https://arxiv.org/abs/2609.28393 | `PRIMARY_PAPER` | identity-bearing point-set world state spanning rigid, articulated, cloth and rope regimes; strong test of representation sharing across material classes |
| PointWorld — https://arxiv.org/abs/2601.03782 | `PRIMARY_PAPER` | 3D point-flow state/action representation for cross-embodiment manipulation; RGB-D rather than strict monocular RGB |
| SyncWorld — https://arxiv.org/abs/2609.09155 | `PRIMARY_PAPER` | shows that numerical robot actions need visual calibration to acquire setup-specific pixel/world meaning across embodiment and viewpoint changes |
| Robot-Factored World Models — https://arxiv.org/abs/2607.22535 | `PRIMARY_PAPER` | factors action realization and rendered robot geometry away from scene-response prediction; useful interface alternative to raw action conditioning |
| WROP — https://arxiv.org/abs/2609.28654 | `PRIMARY_PAPER` | trains object permanence/solidity directly with cognitive-science-inspired synthetic curricula; complementary to realistic persistence benchmarks |
| OASIS-Map — https://arxiv.org/abs/2607.14899 | `PRIMARY_PAPER` | multi-session mapping for appeared/disappeared/moved/replaced objects; important for belief revision when the real world changes between observations |
| R4DSG — https://arxiv.org/abs/2608.11017 | `PRIMARY_PAPER` | RGB-only persistent object/change memory using relative 4D scene graphs for long egocentric video |
| DoughNet — https://arxiv.org/abs/2404.12524 | `PRIMARY_PAPER` | visual predictive model that explicitly handles splitting/merging topology in deformable manipulation |
| CulinaryCut-VLAP — https://arxiv.org/abs/2601.06451 | `PRIMARY_PAPER` | contact-rich cutting and topology-changing manipulation with physics-simulator, force/torque and pose supervision |
| Sashimi-Bot — https://www.nature.com/articles/s44182-026-00098-9 | `PRIMARY_PAPER` | real deformable-object cutting with visual+tactile feedback; makes topology-altering state change a real-robot manipulation problem |
| What-If World — https://arxiv.org/abs/2605.27589 | `PRIMARY_PAPER` | paired causal interventions on real DROID/nuScenes frames; tests whether generated futures change correctly when one physical variable changes |
| CRONOS — https://arxiv.org/abs/2605.23699 | `PRIMARY_PAPER` | controlled interventions on viewpoint/scene/category/appearance while holding physical event type fixed |
| CausalPhys — https://arxiv.org/abs/2606.05966 | `PRIMARY_PAPER` | physical reasoning benchmark spanning perception, anticipation, intervention and goal orientation with expert causal graphs |
| CG-World — https://arxiv.org/abs/2607.26452 | `PRIMARY_PAPER` | large structured world-state dataset with action/mechanism interventions, contacts, physics caches and counterfactual branch metadata |
| ManiSoft — https://arxiv.org/abs/2605.18617 | `PRIMARY_PAPER` | makes the robot body's own deformable physical state part of visual manipulation, not only the external object's state |
| Decision-Aware Uncertainty Evaluation — https://arxiv.org/abs/2603.10061 | `PRIMARY_PAPER` | evaluates calibration/selective prediction under partial visual evidence; relevant to “know when you do not know” |
| GR00T N1.7 — https://github.com/NVIDIA/Isaac-GR00T | `OPEN_SOURCE` | current strong open VLA/direct-policy baseline with human-video pretraining and cross-embodiment action representation |
| Riemann-1.0 — https://arxiv.org/abs/2608.27033 | `PRIMARY_PAPER` | unified causal WAM jointly modeling multi-view observations, robot state and action across large heterogeneous experience |
| Qwen-RobotWorld — https://arxiv.org/abs/2606.17030 | `PRIMARY_PAPER` | language-conditioned future-world modeling across multiple embodied domains; language as an action abstraction is itself a research hypothesis |
| Xiaomi-Robotics-U0 — https://arxiv.org/abs/2607.11643 | `PRIMARY_PAPER` | world foundation model used as embodied generator/transfer model/data engine; separates data-generation utility from epistemic world-state fidelity |
| Being-M0.7 — https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | latent visual-motion world-action route transferring large-scale human experience to humanoid control |
| HWAM — https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | explicitly predicts realized post-execution body state to model the action-execution gap |
| Identifiable World Models — https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | hybrid alternative between opaque latent state and hand-designed explicit state |
| Artisan — https://arxiv.org/abs/2610.13947 | `PRIMARY_PAPER` | adds articulation, collision, gravity stability, mass/material properties and downstream function to physical 3D-asset evaluation |
| Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810 | `PRIMARY_PAPER` | question-conditioned viewpoint/evidence acquisition for multi-view spatial reasoning |
| Agentic Video Understanding — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/ | `OFFICIAL_REPORTED_RESULT` | evidence-acquisition policy can change long-video accuracy/efficiency independently of base representation |
| RobotWorld — https://arxiv.org/abs/2610.10409 | `PRIMARY_PAPER` | exposes composition, persistent task-state, recovery and completion-verification failures across diverse robot-use tasks |
| Video2World — https://arxiv.org/abs/2610.04432 | `PRIMARY_PAPER` | separates visual/geometric similarity from dynamic and functional correctness in reconstructed worlds |

These entries are **research objects and comparators**, not Clover components.

## What the newest evidence changes

The current frontier strengthens several Stage-1 distinctions that should remain visible before Analysis begins:

```text
statistically predictable from pixels
≠
physically identifiable from pixels

visual geometry
≠
hidden physical parameters

shape / material appearance
≠
mass / density / friction / stiffness / temperature

passive observation
≠
action-response system identification

observation
≠
belief
≠
identified latent state

reversible state update
≠
entity split / merge / cutting / breakage

plausible future video
≠
intervention-sensitive future
≠
executable action consequence

reference action
≠
realized robot state

appearance / geometry
≠
articulation / mass / material / function

rigid world state
≠
deformable / contact / fluid / granular state

remembering the old world
≠
recognizing that the world changed

strong general reasoner + tools
≠
proof of vision-only world understanding

long context / static sampling
≠
active evidence acquisition

world model for belief
≠
world simulator
≠
world data engine

opaque distributed latent
vs
explicit state
is not the only choice;
hybrid identifiable coordinates are now a serious alternative
```

## Detailed Stage-1 assets

The flat stage files are the primary navigation. Existing deeper material remains available as supporting evidence:

- [`RESEARCH_STATE_VARIABLES.md`](RESEARCH_STATE_VARIABLES.md) — physical/world variables and current evidence/observability map.
- [`RESEARCH_IDENTIFIABILITY.md`](RESEARCH_IDENTIFIABILITY.md) — information limits, partial observability, interventions and identifiability assumptions.
- [`RESEARCH_PHYSICAL_PROPERTIES.md`](RESEARCH_PHYSICAL_PROPERTIES.md) — hidden physical properties, contact/deformation, irreversible topology change and intervention datasets.
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
