# Clover Roadmap

Last updated: 2026-10-14

The roadmap is organized around the fixed research question rather than version numbers:

> **How can a machine understand the real world through vision alone?**

The long-term goal is:

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

The roadmap is evidence-driven and intentionally places **background research, baselines, evaluation battery and failure mapping before the next representation hypothesis**.

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world Evaluation
→ Hardware Co-design
```

## Phase R0 — Public Research Foundation

**Implemented / maintained**

- define the research question and product goal;
- establish public research principles;
- separate current facts, hypotheses and history;
- define evidence labels and source policy;
- document the V0–V3 vision protocols;
- initialize the public GitHub research record.

## Phase R1 — Background Research / Problem Reconstruction

**CURRENT**

Build a deep, source-backed account of the strongest existing answers to the research question.

Research domains include:

- partial observability, uncertainty and active perception;
- classical computer vision and geometry;
- self-supervised image/video representation;
- spatial intelligence and learned reconstruction;
- object-centric representation;
- persistent visual memory;
- intuitive physics and physical-state inference;
- causal representation and intervention;
- generative world models;
- embodied VLM/VLA/world-action models;
- robot foundation models;
- model-based robotics and POMDPs;
- real-world generalization and recovery.

Required outputs:

```text
BACKGROUND_RESEARCH.md
SOURCE_MAP.md
FRONTIER_METHODS.md
PAPERS.md
BENCHMARKS_TASKS.md
DATASETS_CODE.md
RESEARCH_QUESTIONS.md
```

**Exit condition:** we can explain, with primary/official evidence, what major approaches represent, what evidence they use, what they demonstrably achieve, where they fail, and which contradictions require direct experiments.

## Phase R2 — Baseline Reconstruction

Establish minimal but strong baselines across qualitatively different representation families.

Initial families:

```text
A classical geometry/state estimation
B static self-supervised visual representation
C predictive video representation
D learned geometry/spatial reconstruction
E visible entity tracking/object-centric baseline
F embodied reasoning / VLA baseline
```

Current candidate references:

- ORB-SLAM3 / RAFT;
- DINOv3;
- V-JEPA 2 / 2.1;
- VGGT / VGGT-Ω;
- SAM 3.1 / object-centric methods;
- OpenVLA and, where access permits, Gemini Robotics ER 2 or comparable strong embodied reasoning systems.

The purpose is not leaderboard optimization. It is to measure what each representation actually contains and which failure modes are structural.

## Phase R3 — Understanding Battery

Create a unified evaluation protocol spanning at least:

```text
existence / identity
object permanence
spatial relation
temporal relation
observability / unknown
world change / revision
physical plausibility
quantitative/relational physics
causality / intervention
counterfactuals
streaming memory
active perception
long-horizon action usefulness
```

The battery should combine public benchmarks with custom machine-computable queries and real visual tasks.

Candidate public instruments include:

- IntPhys 2;
- MVP / Minimal Video Pairs;
- CausalVQA;
- Perception Test visual subsets;
- PersistBench;
- S-EMBER;
- Principia;
- RoboPhys-3D;
- robot task suites when embodied evaluation becomes active.

## Phase R4 — Failure Matrix

For each baseline and method family, record failures across:

```text
geometry
identity
object permanence
temporal consistency
observability / uncertainty
memory / retrieval
physics
causality
counterfactuals
OOD/generalization
camera shift
world change / revision
long horizon
action utility
compute/latency/memory
```

Do not collapse the matrix into one scalar score.

**Exit condition:** we can state which failures are common across strong existing approaches and which are specific to one representation family.

## Phase R5 — Representation Hypothesis

Only now compare candidate answers to the central representation question:

- explicit geometry/state;
- distributed predictive latent;
- object-centric representation;
- continuous fields / machine-native primitives;
- persistent episodic/world state;
- identifiable/hybrid representations;
- generative simulator-style state;
- structures not yet identified.

A candidate must state:

```text
problem
prior art
representation
learning signal
prediction
falsifier
evaluation
action relevance
compute implications
```

Historical Clover mechanisms may be retained, transformed, merged or rejected.

## Phase R6 — World Formation / Learning

Study how the selected representation is acquired and maintained from visual experience:

- self-supervision;
- prediction and reconstruction;
- temporal persistence;
- memory and selective retention;
- contradiction and belief revision;
- physical reasoning;
- causal/interventional learning;
- active perception and interaction.

## Phase R7 — Robot Brain

Connect validated world understanding to:

- Decision;
- Tool / capability selection;
- planning;
- Execution;
- replanning and recovery;
- active information gathering.

The decisive comparison is not architectural elegance. It is whether the world representation measurably improves unfamiliar-environment behavior over a matched strong direct policy.

## Phase R8 — Real-world Evaluation

Use controlled and real tasks as instruments:

- world/physical understanding;
- causality and counterfactuals;
- open-world generalization;
- long-horizon embodied tasks;
- moved-object / blocked-path recovery;
- active perception;
- real-world transfer;
- baseline comparison and ablation.

Evidence should progress from:

```text
controlled synthetic
→ controlled real
→ unseen real environments
```

## Phase R9 — Hardware Co-design

Only after the scientific mechanism is established, map the computation to the best substrate:

- CPU;
- GPU;
- Metal / Apple Silicon unified memory;
- Neural Engine / Core ML where appropriate;
- other accelerators where scientifically justified.

Measure:

```text
latency
memory
energy
bandwidth
throughput
synchronization/dispatch cost
```

Hardware is optimized around the validated algorithm. It does not select the representation in advance.

## Final rule

> **Research Map first. Representation hypothesis later. Protect the question, not the current answer.**
