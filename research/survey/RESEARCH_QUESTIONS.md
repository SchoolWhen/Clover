# Research Questions

Last updated: 2026-10-14

This is the synthesis layer of the Clover Survey. Each question below must be understood before the next Clover architecture is frozen.

> **SSOT:** How can a machine understand the real world through vision alone?

The questions form one chain:

```text
visual evidence
→ representation
→ persistence / memory
→ dynamics / causality
→ uncertainty / observability
→ decision / action
```

## RQ1 — What is a world representation?

“World model” can mean a SLAM map, 3D reconstruction, object graph, predictive latent, video generator, policy hidden state, simulator or language description. These are not interchangeable.

Candidate families:
- explicit metric geometry;
- object-centric state;
- distributed latent;
- continuous fields;
- generative simulator.

**Status:** `OPEN`. The next representation must be selected by capability, not aesthetics.

## RQ2 — Must understanding be explicit?

Explicit state supports direct query, local revision, checking and planning. But modern mechanistic analysis reports distributed/hierarchical physical representations rather than only compact classical state variables.

- Paper: https://arxiv.org/abs/2602.07050
- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

A serious hybrid candidate is:

```text
distributed learned representation
+ small explicit query/action state
+ evidence provenance
```

Identifiable World Models is relevant: https://arxiv.org/abs/2610.07028

## RQ3 — Which parts of geometry should be learned?

Projective geometry, rotations, camera projection, visibility and bundle adjustment have strong mathematical structure. DUSt3R/VGGT show that learned systems can recover geometry densely and robustly.

- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195

Question: which invariants should be guaranteed, which estimators learned, and how should both interact?

## RQ4 — Prediction, reconstruction or generation?

- Prediction: V-JEPA 2/2.1.
- Reconstruction: DUSt3R/VGGT.
- Generation/simulation: Atlas/Cosmos.

A model can reconstruct accurately but have poor action state, predict well without persistent identity, or generate plausible but unjustified hidden detail.

ReWAM argues reconstruction quality alone does not guarantee control-useful representation: https://arxiv.org/abs/2609.38163

**Status:** `OPEN`; hybrid objectives are plausible.

## RQ5 — What can vision alone identify?

Directly visible quantities include boundary, texture, image motion and visible occlusion. Depth, 3D shape, identity, support/contact likelihood and persistent existence require assumptions or temporal evidence. Exact contact force, friction, hidden material state, mass without interaction and arbitrary hidden geometry are generally not uniquely identifiable from vision alone.

Clover therefore needs distinctions such as:

```text
observed
inferred
ambiguous
unobserved
contradicted
```

## RQ6 — What does interaction add that passive video cannot?

Passive video contains dynamics, transformations and demonstrations. V-JEPA 2 shows strong action-free video learning before an action-conditioned robot stage: https://arxiv.org/abs/2506.09985

Interaction may add controllability, intervention, action consequence, affordance and active information gathering. A key experiment is to construct worlds observationally similar under passive viewing but distinguishable through intervention.

## RQ7 — Objects, fields, geometry, or a combination?

Objects help identity/relations/action. Fields help continuous support/local interaction. Geometry gives metric constraints. None obviously solves open-world semantics, dynamics and causality alone.

A candidate synthesis:

```text
dense visual evidence
→ persistent spatial support
→ emergent entity abstractions
→ task-relevant relations
```

This must be tested rather than inherited from historical Clover.

## RQ8 — What is persistent memory?

A robot's world does not vanish when the camera turns away. Candidate memory types include raw evidence, compressed world state, episodic events, semantic concepts or hybrids.

VISTA is important because it isolates the contribution of a visual-memory/retrieval harness: https://arxiv.org/abs/2610.02200

Core question: **what remains authoritative when current pixels disappear?**

## RQ9 — How should memory revise itself?

Persistent memory without correction accumulates error.

```text
new evidence
→ contradiction detection
→ affected-state localization
→ revision
→ downstream update
```

Historical Evidence Replay remains a candidate, but must compete with learned recurrent/contextual memory.

## RQ10 — What is physical understanding?

Useful ladder:
- P0 visual continuation;
- P1 relevant state transition;
- P2 invariants/constraints such as permanence, continuity, exclusion, support/collision;
- P3 intervention-sensitive prediction;
- P4 counterfactual consistency;
- P5 improved action/planning/recovery.

IntPhys 2, MVPBench and CausalVQA cover only subsets of this ladder.

## RQ11 — What is causal understanding?

```text
temporal correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Historical Counter-Witness First Causality remains an internal hypothesis connecting prediction error, belief revision and causal discovery. It remains unvalidated.

## RQ12 — How should uncertainty and observability be represented?

```text
not visible ≠ empty
unobserved ≠ absent
unknown type ≠ nonexistent
low confidence ≠ false
confidence ≠ authority
```

Classical Bayesian robotics and POMDPs remain important prior art. World epistemic state, statistical confidence/calibration and any future verification/authority mechanism must not be conflated.

## RQ13 — What role should language play?

Modern high-performing systems such as Gemini Robotics ER 2, RT-2, OpenVLA and π0.5 use language/multimodal pretraining. Language injects object semantics, commonsense physics, task knowledge and action concepts.

Evaluation must distinguish visual inference from recalled language/world priors.

Useful future comparison:

```text
vision-only
vs vision + language prior
vs vision-only world state + language task interface
```

## RQ14 — Do we need active perception?

A robot can move to reveal evidence: change viewpoint, approach or inspect behind an obstacle. Vantage shows evidence/view selection can improve spatial reasoning: https://arxiv.org/abs/2610.11810

Question: **can the system represent what it does not know well enough to choose the next visual action?**

## RQ15 — Should a worldview measurably improve action?

If two representations have similar perception scores but one plans faster, generalizes better, recovers after world change, needs less robot data or avoids unjustified actions, it is a stronger robot-world representation.

Eventually compare under matched data/compute/tasks:

```text
policy alone
vs policy + persistent worldview
```

## RQ16 — What does “type” mean for a machine?

Possible internal types:
- semantic category;
- geometry/topology;
- dynamical response;
- affordance;
- learned equivalence class of predicted transformations.

The target is transfer to novel objects/actions, not reproducing human category names.

## RQ17 — What should remain invariant across embodiments?

A general robot brain may control arms, mobile manipulators, humanoids or quadrupeds. A promising separation is:

```text
embodiment-independent world state
+ embodiment-specific controllability/effect model
```

Open X-Embodiment: https://github.com/google-deepmind/open_x_embodiment

## RQ18 — What is the correct relationship between world and action?

Candidate structures:

```text
observation → action
observation → reasoning/plan → action
observation → explicit world → planning → action
observation + action ↔ future state
observation → generated futures → select action
```

No structure currently has universal dominance. Current WAM survey: https://arxiv.org/abs/2609.16074

## RQ19 — How should real-world understanding be evaluated?

A credible claim needs controlled physics, shortcut-resistant pairs, persistent-memory tests, real video, interventions, active perception, long-horizon tasks, unseen environments and measurable action usefulness.

RoboPhys-3D is a useful signal that perceptual/video quality can miss execution-level failures: https://arxiv.org/abs/2608.28718

## RQ20 — When should hardware influence the theory?

The scientific representation should not be selected merely because it maps conveniently to M4/CUDA/etc. Once an algorithm is specified, hardware/software co-design matters.

Questions include sparse vs dense operations, shared-state placement, synchronization, Metal semantics, memory bandwidth and representation compression.

```text
M4 suitability ≠ scientific correctness
```

## RQ21 — Why did classical CPU-era vision not become general world understanding?

The answer is not simply “CPU was too slow.” Classical vision was often limited by handcrafted/task-specific representations, fragmented pipelines, limited data scaling and weak end-to-end representation learning. Modern progress came from co-evolution of:

```text
learned representation
+ large datasets
+ scalable objectives
+ optimization
+ accelerator hardware
```

Historical anchors:
- SIFT: https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- AlexNet: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet: https://arxiv.org/abs/1512.03385
- ViT: https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020

The lesson is not “abandon CPU”; it is **do not repeat the representation bottleneck while pursuing efficiency**.

## RQ22 — What should the next Clover architecture decision look like?

Not:

```text
we like field crystallization → implement it
strong paper appears → add its framework
GPU models win → convert everything to Transformer
```

Instead:

```text
Survey evidence
→ unresolved contradiction
→ candidate representations
→ discriminating experiment
→ architecture decision
→ implementation
```

A next-generation Clover proposal must state which questions it answers, what evidence supports it, what would falsify it and what remains open.
