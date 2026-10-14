# Clover

**Open research on how machines can understand the real world through vision alone.**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover is a long-term open research project. **The question is fixed; the answer is open.**

[中文说明](README.zh-CN.md)

## Start here

For a new agent, researcher or contributor:

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)
9. [`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md)
10. [`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)
11. [`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md)
12. [`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md)
14. [`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md)
15. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
16. [`AGENTS.md`](AGENTS.md)
17. [`STATUS.md`](STATUS.md)
18. [`research/README.md`](research/README.md)

## Current stage — 1 Research

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next cycle
```

**Stage 1 Research is active.** The current job is to collect and structure the problem space broadly before deciding what Clover itself should invent.

## Stage-1 question chain

```text
What relevant research exists?
↓
What state exists in the real world?
↓
How does that state become RGB evidence?
↓
What hidden state is identifiable from that evidence?
↓
Which physical properties require history, active views, interaction or non-visual sensing?
↓
What information must an internal state preserve?
↓
When has the representation aliased distinct worlds/histories?
↓
At what granularity / timescale should state be represented?
↓
What view / probe / action is worth acquiring next?
↓
What if the current hypothesis set is incomplete, stale, unsafe to test, or socially constrained?
↓
How should hypotheses, mechanisms, experiments, falsification and provenance be managed?
↓
Can the candidate run under realistic edge/closed-loop constraints, and how strong is its simulation-to-real validation evidence?
↓
Which current methods and benchmarks discriminate competing answers?
```

This is a research map, not a proposed Clover architecture.

## Core Stage-1 distinctions

```text
pixels ≠ world state

statistical predictability ≠ physical identifiability

vision alone ≠ passive vision only

observational indistinguishability ≠ representation failure

complete physical description
≠ minimal predictive state
≠ minimal control-sufficient state
≠ general-purpose world state

minimum state ≠ best state at every timescale

maximum information gain ≠ best safe / permitted experiment

uncertainty over known hypotheses
≠ correct hypothesis missing entirely

uncertain state
≠ stale / wrong world model

parameter estimation
≠ model selection
≠ mechanism discovery
≠ open-world model expansion

current development machine
≠ final edge computer
≠ scientific hypothesis

model inference latency
≠ camera-to-action closed-loop latency

single-simulator success
≠ sim2sim robustness
≠ sim2real transfer
≠ target-robot validation

reflection ≠ falsification

current best hypothesis ≠ permanent truth

external-world state ≠ self / embodiment state

visible behavior of another agent
≠ its hidden goal / belief
```

## What Stage 1 currently covers

The inventory is intentionally wider than “world models” or “VLA.” It includes:

- inverse problems, observability, identifiability, uncertainty and POMDPs;
- human/developmental visual cognition;
- image formation / inverse rendering / camera acquisition;
- transparency, reflection, refraction, blur, rolling shutter and adverse visual conditions;
- classical geometry, SfM, VO, SLAM, correspondence and tracking;
- static/video self-supervised representation;
- learned geometry, NeRF/3DGS/4D reconstruction;
- object-centric representation, scene graphs and semantic mapping;
- persistent/episodic memory and world change;
- hidden physical properties: mass, inertia, friction, stiffness, temperature, viscosity and material state;
- rigid, articulated, deformable, fluid and granular dynamics;
- irreversible topology change: cutting, splitting, merging and breakage;
- intuitive/quantitative/causal physical reasoning;
- active perception, active system identification and intervention;
- generative world models, world-action models and VLA/direct policies;
- belief state, predictive state, information state and representation sufficiency;
- state aliasing and Markov-state diagnostics;
- state abstraction, bisimulation, hierarchical / multi-timescale state;
- structured/equivariant memory;
- value of information, epistemic actions and safe probing;
- open-world hypothesis generation and verification;
- mechanism/causal-structure discovery and Bayesian experiment design;
- hypothesis provenance, falsification and refutation memory;
- world-model changepoints, slow drift and model misspecification;
- self/body schema and embodiment mismatch;
- help-seeking, abstention and human escalation;
- social/intentional hidden state, recursive belief and permission constraints;
- uncertainty calibration, OOD and continual/test-time adaptation;
- edge inference, quantization, memory/latency/power constraints and hardware-aware profiling;
- simulation fidelity, domain randomization, sim2sim, sim2real, real2sim and digital-twin/system-identification workflows;
- hardware-in-the-loop / proxy-hardware validation and reality-gap measurement;
- simulation/data engines, datasets, benchmarks, reproducibility and systems integration.

If another direction materially constrains the mother question, it should be added even if it does not fit an existing category.

## Current practical environment

The current local development reference is a **Mac mini with Apple M4**.

This is useful for:

```text
model development
Apple-Silicon profiling
MLX / Core AI / Core ML experiments
quantization / compression studies
local MuJoCo and controlled simulation
end-to-end software/runtime measurements
```

It is **not** assumed to be the final robot computer and does not determine the scientific representation.

Current Isaac Sim standard requirements do not support macOS/non-NVIDIA hardware, so GPU-heavy Isaac/Isaac-Lab work should be treated as an optional remote/Linux-NVIDIA validation path rather than a local prerequisite.

See [`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md).

## No-real-robot validation policy

Clover currently has no target physical robot. Therefore validation claims should be tiered:

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single simulator
EV2 randomized simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data validation
EV5 real-to-sim / digital-twin validation
EV6 real deployment runtime / compute hardware in the loop
EV7 proxy physical hardware
EV8 target real robot
```

Do not describe EV0–EV6 as demonstrated sim2real success.

The absence of a robot limits claim strength; it does not justify postponing validation.

## Current frontier highlights

The thin current-edge index is [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md). As of **2026-10-14**, important additions include:

- SpecWM — https://arxiv.org/abs/2610.15429
- DR-WM — https://arxiv.org/abs/2610.17630
- Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/
- Mental-Models — https://arxiv.org/abs/2610.12453
- Identifiable World Models — https://arxiv.org/abs/2610.07028
- RobotWorld — https://arxiv.org/abs/2610.10409
- Video2World — https://arxiv.org/abs/2610.04432
- HUME — https://arxiv.org/abs/2607.06501
- Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html
- robust / constrained Bayesian experimental design — https://proceedings.mlr.press/v300/tang26d.html and https://proceedings.mlr.press/v306/guo26g.html

These are research objects and comparators, not Clover components.

## Later stages

### 2 Analysis
One important method → one small mechanism report.

### 3 Synthesis
Compare methods across common dimensions, strengths, weaknesses, trade-offs and failure modes.

### 4 Innovation
Only after a gap is well supported do Clover-original hypotheses become serious candidates.

### 5 Implementation
Build reproducible code.

### 6 Evaluation
Run experiments, ablations, cross-simulator tests and eventual real-world tests.

### 7 Reflection
Interpret failures, reject bad assumptions and begin the next research cycle.

## “Vision alone” protocol

Observation protocol:

- `V0` — monocular RGB + temporal order;
- `V1` — V0 + camera intrinsics;
- `V2` — calibrated multi-camera RGB;
- `V3` — active embodied vision where action changes future visual evidence.

Learning provenance:

- `L0` — visual self-supervision;
- `L1` — visual labels/annotations;
- `L2` — language/world-knowledge supervision;
- `L3` — action-conditioned demonstrations/experience;
- `L4` — non-visual or privileged physical evidence.

This prevents “RGB at deployment” from being confused with “learned only from vision.”

## What we do not assume

Clover does **not** assume that CPU/GPU/NPU choice determines the science, that the Mac mini M4 is the final target hardware, that one simulator is reality, that sim-only success proves transfer, that explicit state must beat distributed latent state, that field/object/geometry/token must be the final primitive, that hierarchy is automatically superior to flat state, that information gain is itself the final algorithm, that the correct hypothesis set is always known, that prediction/reconstruction/generation is necessarily sufficient, or that one benchmark defines understanding.

Historical Clover mechanisms remain ideas until the research process supports or rejects them.

## Project definition

- [SSOT](SSOT.md)
- [Principles](PRINCIPLES.md)
- [Status](STATUS.md)
- [Roadmap](ROADMAP.md)
- [Research lifecycle](research/PIPELINE.md)
- [Flat Stage-1 navigation](research/README.md)

---

**Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**