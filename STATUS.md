# Clover Status

Last updated: 2026-10-14

## Research question

> **How can a machine understand the real world through vision alone?**

## Product goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

The repository follows:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

The immediate priority is breadth, traceability and coverage. We are collecting the full research landscape before making a new Clover algorithmic commitment.

Stage-1 freshness has been checked through **2026-10-14**.

Start with:

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
7. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
8. [`research/README.md`](research/README.md)

## Stage-1 foundation — active / expanding

The current inventory explicitly tracks directions including:

- epistemology, inverse problems and partial observability;
- human/developmental visual cognition;
- classical geometry, SfM, VO and SLAM;
- optical flow, correspondence and tracking;
- static self-supervised representation;
- predictive video representation;
- learned geometry;
- NeRF / Gaussian Splatting / 4D reconstruction;
- object-centric representation;
- scene graphs and semantic mapping;
- persistent / episodic memory;
- belief revision and forgetting;
- intuitive, relational and quantitative physics;
- physics-structured / differentiable world models;
- contact, friction, articulation and deformable-object dynamics;
- mass, density, center of mass, inertia, material and function grounding;
- stiffness / compliance and tactile-grounded physical state;
- liquids / viscosity and other weakly visible physical properties;
- granular packing / cohesion and preparation-dependent material state;
- cutting, splitting, merging, breakage and irreversible topology change;
- thermal / temperature-aware manipulation as a visible-spectrum boundary case;
- causal representation learning;
- counterfactual visual reasoning;
- explicit intervention / counterfactual datasets and benchmarks;
- active perception and next-best-view;
- system identification and action consequences;
- generative world models;
- world-action models;
- world models as belief state, simulator and data engine;
- VLA and direct policy;
- hierarchical embodied reasoning;
- robot foundation models;
- human / egocentric video transfer;
- affordance learning;
- model-based control and belief-space planning;
- semantic memory and multi-session map revision;
- uncertainty and calibration;
- open-world / OOD recognition;
- continual / lifelong learning;
- simulation, Real2Sim and synthetic data;
- large robot datasets;
- benchmark design and shortcut auditing;
- systems integration and compounded failure;
- multi-agent / social world modeling;
- unified physical-AI surveys.

This list is intentionally expandable. If a direction materially constrains the mother question, Stage 1 should collect it.

## World-state / observability map

[`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md) provides a variable-level Stage-1 map spanning:

```text
observation state
geometric state
entity / hidden-object state
physical state
latent physical parameters
functional / affordance state
causal / controllability state
epistemic state
social / intentional state
```

It separately records whether current evidence comes from:

```text
static RGB
passive temporal video
active visual viewpoint changes
action-response interaction
non-visual / privileged sensing
```

The most important distinction introduced by this map is:

```text
statistically predictable from pixels
≠
physically identifiable from pixels
```

This is now a first-class Stage-1 research question.

## Identifiability / information-limit foundation

[`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md) separates:

```text
predictability
observability
identifiability
calibration / epistemic correctness
action sufficiency
```

It connects classical visual ambiguity, POMDP belief state, active perception, system identification, causal-representation identifiability and modern identifiable world-model research.

The controlling question is no longer merely:

```text
Can the model guess the hidden variable?
```

but:

```text
What evidence makes that variable identifiable?
Under what assumptions?
What alternative worlds remain compatible with the same visual evidence?
When should the correct answer be uncertainty or another information-gathering action?
```

## Hidden physical properties / irreversible change

[`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md) now deepens the Stage-1 map for:

```text
mass / density
center of mass / inertia
friction
stiffness / compliance
temperature
liquids / viscosity
granular packing / cohesion
contact / deformable state
cutting / splitting / merging / breakage
counterfactual and intervention datasets
```

The key distinctions are:

```text
property useful for action
≠
property learned from vision alone

statistical prediction from appearance
≠
physical identification from evidence

same entity, new pose
≠
entity split / merge / topology change

future looks plausible
≠
future responds correctly to an intervention
```

Important current references include:

- visual mass estimation — https://arxiv.org/abs/2601.20303
- VisPhysQuant — https://arxiv.org/abs/2603.16958
- ViTacPhys — https://arxiv.org/abs/2608.21355
- HEARTH temperature dataset — https://arxiv.org/abs/2609.23418
- friction via visual/haptic evidence — https://arxiv.org/abs/2010.08277
- friction via proxy interactions — https://arxiv.org/abs/2604.24188
- DR-WM — https://arxiv.org/abs/2610.17630
- PointCast — https://arxiv.org/abs/2609.28393
- WorldContact — https://arxiv.org/abs/2609.19600
- ManiSoft — https://arxiv.org/abs/2605.18617
- DoughNet — https://arxiv.org/abs/2404.12524
- CulinaryCut-VLAP — https://arxiv.org/abs/2601.06451
- Sashimi-Bot — https://www.nature.com/articles/s44182-026-00098-9
- What-If World — https://arxiv.org/abs/2605.27589
- CRONOS — https://arxiv.org/abs/2605.23699
- CausalPhys — https://arxiv.org/abs/2606.05966
- CG-World — https://arxiv.org/abs/2607.26452
- CHAIN — https://arxiv.org/abs/2602.21015

These sources collectively make physical-property provenance and intervention sensitivity explicit Stage-1 concerns.

## 2026-10-14 frontier refresh

The current edge includes several references that materially change the comparison space:

- **Gemini 4 Argon for Robotics** — https://developers.googleblog.com/gemini-4-argon-for-robotics/ — `OFFICIAL_REPORTED_RESULT`; general multimodal physical-reasoning / Real2Sim / robot-tool-use counter-hypothesis.
- **ERQA** — https://github.com/embodiedreasoning/ERQA — `OPEN_SOURCE`; embodied/spatial reasoning benchmark and evaluation harness.
- **DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630 — `PRIMARY_PAPER`; separates visual geometry from contact/friction properties calibrated through action-response evidence.
- **HEARTH** — https://arxiv.org/abs/2609.23418 — `PRIMARY_PAPER`; RGB-thermal-3D dataset demonstrating temperature as task-relevant hidden physical state.
- **ViTacPhys** — https://arxiv.org/abs/2608.21355 — `PRIMARY_PAPER`; mass/friction/stiffness inference grounded in visual+tactile demonstrations.
- **What-If World** — https://arxiv.org/abs/2605.27589 — `PRIMARY_PAPER`; paired intervention benchmark for embodied world models.
- **CRONOS** — https://arxiv.org/abs/2605.23699 — `PRIMARY_PAPER`; counterfactual physical-consistency benchmark under controlled visual interventions.
- **CG-World** — https://arxiv.org/abs/2607.26452 — `PRIMARY_PAPER`; large structured world-state data with action/mechanism intervention branches and explicit physics/contact metadata.
- **CHAIN** — https://arxiv.org/abs/2602.21015 — `PRIMARY_PAPER`; interactive physics-driven benchmark for causal action sequences under geometric/contact/support constraints.
- **Physically Guided Visual Mass Estimation** — https://arxiv.org/abs/2601.20303 — `PRIMARY_PAPER`; treats single-RGB mass inference as ill-posed and factorizes through volume/density-related priors.
- **PointCast** — https://arxiv.org/abs/2609.28393 — `PRIMARY_PAPER`; persistent point-state model across rigid, articulated, cloth and rope regimes.
- **SyncWorld** — https://arxiv.org/abs/2609.09155 — `PRIMARY_PAPER`; visual calibration of action→visual mapping across cameras/environments/embodiments.
- **Robot-Factored World Models** — https://arxiv.org/abs/2607.22535 — `PRIMARY_PAPER`; factors action realization/robot rendering from environment response.
- **WROP** — https://arxiv.org/abs/2609.28654 — `PRIMARY_PAPER`; trains object permanence/solidity with controlled cognitive-science-inspired curricula.
- **OASIS-Map** — https://arxiv.org/abs/2607.14899 — `PRIMARY_PAPER`; multi-session object-level map change detection.
- **R4DSG** — https://arxiv.org/abs/2608.11017 — `PRIMARY_PAPER`; RGB-only relative 4D scene-graph memory for persistent objects and environmental change.
- **GR00T N1.7** — https://github.com/NVIDIA/Isaac-GR00T — `OPEN_SOURCE`; current strong open VLA/direct-policy reference.
- **Riemann-1.0** — https://arxiv.org/abs/2608.27033 — `PRIMARY_PAPER`; unified causal WAM jointly modeling observations, robot state and action.
- **Qwen-RobotWorld** — https://arxiv.org/abs/2606.17030 — `PRIMARY_PAPER`; language-conditioned video world modeling across embodied domains.
- **Xiaomi-Robotics-U0** — https://arxiv.org/abs/2607.11643 — `PRIMARY_PAPER`; world foundation model used as generator, transfer mechanism and data engine.
- **Being-M0.7** — https://arxiv.org/abs/2610.11283 — `PRIMARY_PAPER`; latent visual-motion world-action route.
- **HWAM** — https://arxiv.org/abs/2610.12026 — `PRIMARY_PAPER`; explicit post-execution body-state prediction.
- **Identifiable World Models** — https://arxiv.org/abs/2610.07028 — `PRIMARY_PAPER`; hybrid distributed + identifiable-state route.
- **Artisan** — https://arxiv.org/abs/2610.13947 — `PRIMARY_PAPER`; physical/function-aware articulated asset evaluation.
- **Vantage / Seek-and-View** — https://arxiv.org/abs/2610.11810 — `PRIMARY_PAPER`; active viewpoint/evidence acquisition.
- **RobotWorld** — https://arxiv.org/abs/2610.10409 — `PRIMARY_PAPER`; exposes composition, task-state, recovery and completion-verification failures.
- **Video2World** — https://arxiv.org/abs/2610.04432 — `PRIMARY_PAPER`; separates visual similarity from dynamics and functional correctness.

These are **research materials and comparators**, not Clover components.

## Current method references

Important tracked references now span:

```text
classical geometry / tracking
ORB-SLAM3 · RAFT

static / video representation
DINOv3 · V-JEPA 2 / 2.1

learned 3D / 4D world structure
DUSt3R · VGGT / VGGT-Ω · NeRF / 3DGS · 4DVGGT-D · DP-DeGauss

entities / memory / dynamic-world revision
SAM 3.1 · Slot Attention · PLATO · PersistBench · WROP · S-EMBER · VISTA · PerSeM · TAO-Amodal · OASIS-Map · R4DSG

physical property / hidden physics
visual mass estimation · VisPhysQuant · ViTacPhys · HEARTH · friction interaction models · DR-WM · PointCast · WorldContact · ManiSoft · DoughNet · CulinaryCut-VLAP · Sashimi-Bot

physical / causal understanding
IntPhys 2 · Minimal Video Pairs · Principia · RoboPhys-3D · CausalVQA · What-If World · CRONOS · CausalPhys · CG-World · CHAIN · causal representation learning

active evidence / calibration
Vantage · SyncWorld · agentic video understanding

generative / world models
Atlas · Cosmos 3 · Video2World · Qwen-RobotWorld · Xiaomi-Robotics-U0

VLA / direct policy / robot foundation systems
OpenVLA · π0.5 · GR00T N1.7 · Gemini Robotics · Gemini 4 Argon · Helix · Skild

world-action models
ReWAM · Riemann-1.0 · Being-M0.7 · HWAM · related WAMs

hybrid / identifiable state
Identifiable World Models · causal representation identifiability literature
```

## Dataset / benchmark collection

Tracked resources include:

- Ego4D;
- Perception Test;
- DROID;
- Open X-Embodiment;
- LIBERO;
- CALVIN;
- RoboCasa;
- ManiSkill;
- ERQA;
- RobotWorld;
- Video2World;
- RoboWM-Bench;
- RoboTrustBench;
- TAO-Amodal;
- WROP;
- VisPhysQuant;
- HEARTH;
- What-If World;
- CRONOS;
- CausalPhys;
- CG-World;
- CHAIN;
- IntPhys 2;
- Minimal Video Pairs;
- CausalVQA;
- PersistBench;
- S-EMBER;
- Principia;
- RoboPhys-3D;
- EmbodimentSemantic;
- Artisan physical/articulated-asset benchmark resources;
- ManiSoft soft-robot manipulation resources.

Stage 1 records what each dataset/benchmark actually measures, its inputs, hidden ground truth, shortcuts, licensing and reproducibility.

## Boundary distinctions strengthened by current evidence

```text
statistically predictable from pixels
≠
physically identifiable from pixels

observation
≠
true hidden state
≠
belief over possible states

visual geometry
≠
hidden physical parameters

shape / category / material appearance
≠
mass / density / friction / stiffness / temperature

passive observation
≠
action-response system identification

reversible rigid motion
≠
cutting / splitting / merging / breakage

plausible prediction
≠
intervention-sensitive prediction
≠
physically executable consequence

reference action
≠
realized robot state

visible tracking
≠
amodal completion
≠
object permanence

remembering the old world
≠
recognizing that the world changed

appearance / reconstruction quality
≠
articulation / mass / material / function

long context
≠
active evidence acquisition

strong multimodal reasoner + tools
≠
proof of vision-only world understanding

world model for belief
≠
world simulator
≠
world data engine
```

## Existing Clover prototype

Pre-reset Clover mechanisms remain `INTERNAL_HYPOTHESIS` material. They conceptually belong to Stage 4 Innovation until evidence promotes, transforms or rejects them.

No historical mechanism is protected.

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- optimizing leaderboard scores;
- claiming explicit state is superior to latent state;
- claiming a direct policy is sufficient;
- claiming a generative world model is sufficient;
- choosing hardware before the scientific mechanism;
- treating one benchmark as the definition of understanding.

## Next transition

Stage 2 Analysis becomes the primary activity only when Stage 1 coverage is broad enough that method selection for deeper reports is not distorted by obvious missing fields.

Analysis will then produce one-method-one-report mechanism breakdowns; Stage 3 Synthesis will compare their strengths, weaknesses and common gaps; only Stage 4 Innovation will formalize Clover-original algorithms.

## Not yet demonstrated

Clover has not yet publicly demonstrated general real-world visual world understanding, a final world representation, comprehensive positive-result SOTA, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, a validated original algorithm, or a final hardware mapping.

These remain research targets.
