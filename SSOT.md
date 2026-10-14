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

The decomposition is useful, but the internal representation and learning architecture are not frozen.

## 3. What “understanding” currently means

Clover does not treat understanding as a philosophical label or a single benchmark score.

The working technical definition requires a system to form and revise internal structure that supports, at minimum:

- existence and object identity;
- persistence through time and occlusion;
- spatial structure;
- temporal structure;
- observability and unknown state;
- physically plausible dynamics;
- cause, intervention and counterfactual reasoning;
- long-horizon memory and belief revision;
- generalization to unfamiliar objects, scenes, cameras, dynamics and compositions;
- active acquisition of missing visual evidence;
- measurable value for decision, planning, execution and recovery.

This definition remains a research object and may become more precise.

## 4. Comprehensive positive-result target

“Comprehensive positive result” does **not** mean first place on one dataset.

The target evidence stack has at least six dimensions.

### U — Understanding

Can the system correctly represent identity, persistence, space, time, observability, physics and causality?

### G — Generalization

Does the capability transfer to new objects, scenes, cameras, dynamics and compositions?

### P — Prediction

Can the system answer what will happen, what could happen, what cannot happen and what would happen under an intervention?

### A — Action usefulness

Does the world representation improve decision, planning, recovery and execution?

### R — Real-world transfer

Does the same scientific mechanism survive the path from controlled settings to unfamiliar real environments?

### E — Efficiency

What are the latency, memory, energy, bandwidth and hardware requirements once capability is established?

No single axis substitutes for the others.

## 5. Vision protocols

“Vision alone” is not left ambiguous.

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

Still vision, but materially more information than V0/V1.

### V3 — Embodied active vision

The robot can move to obtain new visual evidence.

The sensory evidence remains visual, but action changes what can be observed.

### Learning-evidence provenance

Observation protocol alone is not enough to describe modern systems. When relevant, the research record also annotates how knowledge was acquired:

- `L0` — visual self-supervision only;
- `L1` — visual labels / annotations;
- `L2` — language / world-knowledge supervision;
- `L3` — action-conditioned demonstrations or interaction experience;
- `L4` — non-visual or privileged physical evidence such as proprioception, force/tactile, IMU, depth/LiDAR or simulator state.

These labels are descriptive, not a quality ranking.

A model that receives RGB at deployment but was trained with language, actions or privileged state is not scientifically equivalent to a `V0/L0` system.

## 6. Current research posture

The 2026-10-14 Research Reset established:

- CPU-first is not a scientific assumption;
- field crystallization is not a scientific assumption;
- CSP / SEP / licence mechanisms are not scientific assumptions;
- Transformer and non-Transformer architectures are both admissible;
- explicit, distributed and hybrid representations are all admissible;
- reconstruction, prediction, generation and interaction learning are competing or complementary hypotheses;
- benchmark SOTA is evidence, not the project objective.

Past Clover mechanisms remain candidate hypotheses until they survive comparison with prior art, strong baselines and discriminating experiments.

## 7. Benchmark policy

Benchmarks are diagnostic instruments.

The eventual evidence stack should combine:

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

## 8. Hardware policy

The current local platform is Apple M4.

Apple unified memory makes CPU/GPU collaboration attractive, but it does not make communication or synchronization free.

The policy is:

> **Algorithm-first, hardware-co-designed.**

The representation and algorithm determine whether work belongs on CPU, GPU/Metal, Neural Engine, or a combination.

## 9. Current phase

Current phase:

> **Background Research / Problem Reconstruction**

The required research order is:

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

Immediate goals:

1. build a primary-source-backed background map of the full problem;
2. distinguish what each major route actually represents and proves;
3. record training/evidence provenance and important confounds;
4. identify unresolved contradictions across method families;
5. define strong, qualitatively different baselines;
6. define the capability/evaluation battery;
7. only after baseline and failure evidence, freeze a next-generation Clover representation.

Large-scale reproduction and leaderboard optimization remain downstream. Minimal baseline reconstruction is allowed when it answers a discriminating research question and cannot be replaced by a smaller analysis.

## 10. Primary current research surfaces

Read in this order after this SSOT:

1. `research/survey/BACKGROUND_RESEARCH.md`
2. `research/survey/SOURCE_MAP.md`
3. `research/survey/README.md`
4. `research/survey/FRONTIER_METHODS.md`
5. `research/survey/RESEARCH_QUESTIONS.md`
6. `research/survey/PAPERS.md`
7. `research/survey/BENCHMARKS_TASKS.md`
8. `research/survey/DATASETS_CODE.md`

The Source Map should connect every durable external claim to a primary paper, official technical source or open repository, plus the limitation of that evidence.

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

They may be retained, transformed, merged, falsified or removed.

## 12. Architecture-decision gate

A new Clover architecture may not be justified by historical preference or one strong external paper.

Required chain:

```text
background evidence
→ strong baseline
→ Understanding Battery
→ Failure Matrix
→ unresolved cross-family contradiction
→ candidate representation
→ discriminating experiment / falsifier
→ architecture decision
```

## 13. Final principle

> **Protect the question, not the current answer.**
