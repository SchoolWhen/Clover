# Clover SSOT

Last updated: 2026-10-14

## 1. Highest research question

> **How can a machine understand the real world through vision alone?**

This is the highest single source of truth for Clover.

## 2. Product goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

At a system level, the long-term loop is:

```text
visual experience
      ↓
world understanding
      ↓
decision
      ↓
tool / capability selection
      ↓
execution
      ↓
new visual experience
```

The internal representation and learning architecture are not frozen.

## 3. What “understanding” currently means

Clover does not treat understanding as a philosophical label or a single benchmark score.

The working technical target requires internal structure that supports, at minimum:

- existence and object identity;
- persistence through time and occlusion;
- spatial and temporal structure;
- observability, uncertainty and unknown state;
- physically plausible and quantitatively meaningful dynamics;
- cause, intervention and counterfactual reasoning;
- long-horizon memory and belief revision;
- generalization to unfamiliar objects, scenes, cameras, dynamics and compositions;
- active acquisition of missing visual evidence;
- measurable value for decision, planning, execution and recovery.

This definition remains a research object and may become more precise.

## 4. Evidence dimensions

A comprehensive result is not first place on one dataset.

Evidence should cover:

### U — Understanding
Identity, persistence, space, time, observability, physics and causality.

### G — Generalization
New objects, scenes, cameras, dynamics, compositions and embodiments.

### P — Prediction
What will happen, could happen, cannot happen and would happen under intervention.

### A — Action usefulness
Decision, planning, recovery and execution value.

### R — Real-world transfer
Controlled settings → unfamiliar real environments.

### E — Efficiency
Latency, memory, energy, bandwidth and hardware requirements once capability is established.

No single axis substitutes for the others.

## 5. Vision protocols

### V0 — Strict monocular vision

Allowed:

- monocular RGB frames;
- frame ordering / timestamps.

Not allowed as model evidence:

- depth;
- LiDAR;
- tactile;
- force;
- IMU;
- GT pose;
- GT object identity;
- privileged simulator state.

### V1 — Calibrated monocular vision

V0 plus declared camera intrinsics.

### V2 — Multi-camera vision

Calibrated RGB from multiple cameras.

### V3 — Embodied active vision

The robot can move to obtain new visual evidence. Sensory evidence remains visual, but action changes what can be observed.

### Learning-evidence provenance

When relevant, also annotate how knowledge was acquired:

- `L0` — visual self-supervision only;
- `L1` — visual labels / annotations;
- `L2` — language / world-knowledge supervision;
- `L3` — action-conditioned demonstrations or interaction experience;
- `L4` — non-visual or privileged physical evidence such as proprioception, force/tactile, IMU, depth/LiDAR or simulator state.

A model receiving RGB at deployment but trained with language, actions or privileged state is not scientifically equivalent to `V0/L0`.

## 6. Current research posture

The Research Reset established:

- CPU-first is not a scientific assumption;
- field crystallization is not a scientific assumption;
- CSP / SEP / licence mechanisms are not scientific assumptions;
- Transformer and non-Transformer architectures are both admissible;
- explicit, distributed and hybrid representations are all admissible;
- reconstruction, prediction, generation and interaction learning are competing or complementary hypotheses;
- benchmark SOTA is evidence, not the project objective.

Past Clover mechanisms remain candidate hypotheses until they survive comparison with prior art, strong baselines and discriminating experiments.

## 7. Canonical research lifecycle

Clover now uses one flat seven-stage lifecycle:

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

Definitions:

- **Research** — collect directions, sources, methods, datasets, benchmarks and frontier work.
- **Analysis** — produce method-by-method mechanism reports.
- **Synthesis** — compare strengths, weaknesses, trade-offs, common failures and gaps.
- **Innovation** — formulate Clover-original hypotheses and algorithms from demonstrated gaps.
- **Implementation** — build reproducible baselines, diagnostics and selected hypotheses.
- **Evaluation** — run experiments, Results, ablations, generalization and real-world tests.
- **Reflection** — interpret failures, update hypothesis status and decide the next research cycle.

The stages describe epistemic maturity, not software versions.

## 8. Current stage

> **Stage 1 — Research is ACTIVE.**

The immediate goal is broad material collection and source traceability.

Current tasks:

1. map every materially relevant research direction;
2. collect canonical and current primary papers;
3. collect official project pages, code and checkpoints;
4. collect datasets and benchmarks;
5. record visual protocol and learning provenance where possible;
6. record what each source actually demonstrates and does not demonstrate;
7. identify important missing areas and keep searching;
8. maintain strong baseline candidates without turning baseline execution into the current project goal.

Stage 1 is intentionally broader than the current eight deep dossiers. Any research direction that materially constrains the mother question should be collected.

Primary current entry points:

1. `research/PIPELINE.md`
2. `research/RESEARCH.md`
3. `research/README.md`
4. `research/survey/SOURCE_MAP.md`
5. `research/survey/BACKGROUND_RESEARCH.md`

Deeper survey/dossier files support Stage 1 but are not separate project phases.

## 9. Benchmark policy

Benchmarks are diagnostic instruments.

The evidence stack may include:

```text
controlled diagnostic benchmarks
+ shortcut-resistant tests
+ persistent / streaming memory tests
+ causal / interventional tasks
+ real visual transfer
+ active perception
+ long-horizon embodied tasks
+ unfamiliar real environments
+ action usefulness
```

A benchmark score alone does not establish world understanding.

## 10. Hardware policy

The current local platform is Apple M4.

Policy:

> **Algorithm-first, hardware-co-designed.**

CPU, GPU, Metal, MPS and Neural Engine are design resources, not scientific priors.

## 11. Historical Clover ideas

The following remain useful candidate hypotheses, not SSOT:

- field crystallization;
- machine-native primitives;
- evidence / belief separation;
- spacetime support;
- persistent world state;
- epistemic licences;
- evidence replay;
- world compilation;
- query-conditioned computation;
- counter-witness causality;
- world growth and revision.

They belong conceptually to Stage 4 Innovation until evidence promotes, transforms or rejects them.

## 12. Innovation gate

A new Clover core algorithm should not be justified by historical preference or one strong external paper.

Required chain:

```text
broad Research
→ method Analysis
→ cross-method Synthesis
→ well-supported unresolved gap
→ original hypothesis
→ falsifier
→ Implementation
→ Evaluation
→ Reflection
```

Small diagnostic code may be used earlier when reading alone cannot resolve a question, but implementation effort does not substitute for analysis.

## 13. Final principle

> **Protect the question, not the current answer. Research broadly before inventing narrowly.**
