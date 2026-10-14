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

## 3. What "understanding" currently means

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
- generalization to unfamiliar objects, scenes and compositions;
- active acquisition of missing visual evidence;
- measurable value for decision and action.

This definition is itself a research object and may become more precise.

## 4. Comprehensive positive-result target

"Comprehensive positive result" does **not** mean first place on one dataset.

The target evidence stack has at least six dimensions.

### U — Understanding

Can the system correctly represent identity, persistence, space, time, physics and causality?

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

"Vision alone" is not left ambiguous.

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

## 6. Current research posture

The 2026-10-14 Research Reset established:

- CPU-first is not a scientific assumption;
- field crystallization is not a scientific assumption;
- CSP / SEP / licence mechanisms are not scientific assumptions;
- Transformer and non-Transformer architectures are both admissible;
- explicit and distributed representations are both admissible;
- reconstruction, prediction, generation and interaction learning are competing or complementary hypotheses;
- benchmark SOTA is evidence, not the project objective.

Past Clover mechanisms remain candidate hypotheses until they survive comparison with prior art and discriminating experiments.

## 7. Benchmark policy

Benchmarks are diagnostic instruments.

The eventual evidence stack should combine:

```text
controlled diagnostic benchmarks
+ shortcut-resistant tests
+ causal/interventional tasks
+ long-horizon embodied tasks
+ unfamiliar real environments
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

> **Survey / Research Foundation**

Immediate goals:

1. map prior art deeply;
2. distinguish what each route actually proves;
3. identify unresolved contradictions;
4. build a primary-source literature base;
5. define the capability/evaluation space;
6. only then freeze a next-generation Clover representation.

Large-scale reproduction and leaderboard comparison are intentionally downstream.

## 10. Historical Clover ideas

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

## 11. Final principle

> **Protect the question, not the current answer.**
