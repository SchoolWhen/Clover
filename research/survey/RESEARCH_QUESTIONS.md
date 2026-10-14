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

---

## RQ1 — What is a world representation?

The term *world model* currently refers to incompatible objects: a SLAM map, 3D reconstruction, object graph, predictive latent, video generator, policy hidden state, simulator or language description.

Candidate families:

- **explicit metric geometry** — pose/depth/map; precise and queryable, weak in semantics/abstraction;
- **object-centric state** — entities/slots/tracks; useful for identity/composition, but object boundaries are ambiguous;
- **distributed latent** — V-JEPA/policy state; learnable and expressive, harder to inspect/update locally;
- **continuous fields** — useful for spatial support/local interaction, potentially costly/semantically unclear;
- **generative simulator** — samples plausible futures, but plausibility is not epistemic truth.

**Status:** `OPEN`. The next representation must be selected by capability, not aesthetics.

---

## RQ2 — Must understanding be explicit?

Explicit state gives direct query, targeted revision, checking and planning. Classical geometry shows that explicit camera/map/uncertainty variables can be powerful.

But modern evidence argues against assuming full factorization. Meta's *Interpreting Physics in Video World Models* reports physical variables emerging in distributed hierarchical representations, including high-dimensional population codes.

- Paper: https://arxiv.org/abs/2602.07050
- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

A serious candidate is therefore:

```text
distributed learned representation
+ small explicit query/action state
+ evidence provenance
```

Identifiable World Models is relevant to this middle ground:
https://arxiv.org/abs/2610.07028

---

## RQ3 — Which parts of geometry should be learned?

Projective geometry, rotations, camera projection, epipolar constraints, visibility and bundle adjustment already have strong mathematical structure. Yet DUSt3R/VGGT show that learned systems can recover geometry densely and robustly from difficult image collections.

- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195

The real question is not hand-coded vs neural. It is which invariants should be guaranteed, which estimators should be learned, and how both should interact.

---

## RQ4 — Prediction, reconstruction or generation?

These objectives do not optimize the same thing.

- **prediction:** V-JEPA 2/2.1 — learn task-relevant temporal structure in latent space;
- **reconstruction:** DUSt3R/VGGT — recover spatial structure;
- **generation/simulation:** Atlas/Cosmos — model plausible possible worlds and rollouts.

A model may reconstruct well but have poor action state, predict well without persistent identity, or generate plausible but unjustified hidden details.

ReWAM is important because it argues that reconstruction quality or generic perceptual features alone do not guarantee control-useful state:
https://arxiv.org/abs/2609.38163

**Status:** `OPEN`; hybrid objectives are plausible.

---

## RQ5 — What can vision alone identify?

Some quantities are directly visible: boundary, texture, image motion, occlusion and appearance. Others require assumptions or temporal evidence: depth, 3D shape, identity, support/contact likelihood, persistent existence.

Some quantities are generally not uniquely identifiable from vision alone: exact contact force, exact friction coefficient, exact hidden material state, exact mass without interaction, or arbitrary unseen geometry from one view.

Clover therefore needs distinctions such as:

```text
observed
inferred
ambiguous
unobserved
contradicted
```

rather than a binary knows/does-not-know state.

---

## RQ6 — What does interaction add that passive video cannot?

Passive video contains broad dynamics, transformations and demonstrations. V-JEPA 2 shows how much can be learned from action-free video before adding a comparatively small amount of action-conditioned robot data.

- V-JEPA 2: https://arxiv.org/abs/2506.09985

Interaction can add controllability, intervention, action consequence, affordance and active information gathering. A key experiment is to construct worlds that are observationally similar but distinguishable through intervention.

---

## RQ7 — Objects, fields, geometry, or a combination?

Objects help identity/relations/action. Fields help continuous support/local interaction. Geometry gives metric constraints. None alone obviously solves semantics, open-world learning, dynamics and causality.

A candidate synthesis is:

```text
dense visual evidence
→ persistent spatial support
→ emergent entity abstractions
→ task-relevant relations
```

But this must be tested rather than inherited from historical Clover.

---

## RQ8 — What is persistent memory?

A robot's world does not vanish when the camera turns away. Candidate memories include raw evidence, compressed world state, episodic events, semantic concepts, or a hybrid.

VISTA is important because it demonstrates a strong separation between base model and lossless visual-memory/retrieval harness:
https://arxiv.org/abs/2610.02200

Open question:

> What should remain authoritative when current pixels disappear?

---

## RQ9 — How should memory revise itself?

Persistent memory without correction accumulates error. Required loop:

```text
new evidence
→ contradiction detection
→ affected-state localization
→ revision
→ downstream update
```

Historical Clover's Evidence Replay idea remains a candidate because compressed state may later need reinterpretation under new evidence or a new query. It must compete with recurrent/contextual learned memory rather than being assumed correct.

---

## RQ10 — What is physical understanding?

Useful ladder:

- **P0:** visual continuation;
- **P1:** relevant state transition;
- **P2:** sensitivity to invariants/constraints such as permanence, continuity, exclusion, support and collision;
- **P3:** intervention-sensitive prediction;
- **P4:** counterfactual consistency;
- **P5:** improved action/planning/recovery.

IntPhys 2, MVPBench and CausalVQA cover only subsets of this ladder.

---

## RQ11 — What is causal understanding?

Temporal prediction alone is not causality.

```text
temporal correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Historical *Counter-Witness First Causality* remains an internal hypothesis:

```text
expected world
→ mismatch
→ minimum broken dependency
→ causal candidate
```

Its value is that it connects prediction error, belief revision and causal discovery. It remains unvalidated.

---

## RQ12 — How should uncertainty and observability be represented?

Critical distinctions:

```text
not visible ≠ empty
unobserved ≠ absent
unknown type ≠ nonexistent
low confidence ≠ false
confidence ≠ authority
```

Classical Bayesian robotics and POMDPs remain important prior art. World epistemic state, statistical confidence/calibration and any future proof/authority mechanism must not be conflated.

---

## RQ13 — What role should language play?

The scientific question says *vision alone*. Yet modern high-performing systems such as Gemini Robotics ER 2, RT-2, OpenVLA and π0.5 use language/multimodal pretraining.

Language can inject object semantics, commonsense physics, task knowledge and action concepts. Evaluation must therefore distinguish knowledge inferred from visual evidence from knowledge recalled through text pretraining.

Useful future comparison:

```text
vision-only
vs vision + language prior
vs vision-only world state + language task interface
```

---

## RQ14 — Do we need active perception?

A robot can move to reveal evidence: change viewpoint, approach, inspect behind an obstacle, or perform a light interaction.

Vantage is relevant because better view/evidence selection improves spatial reasoning without changing the base VLM:
https://arxiv.org/abs/2610.11810

Core question:

> Can the system represent what it does not know well enough to select the next visual action?

---

## RQ15 — Should a worldview measurably improve action?

This may be the strongest discriminator. If two representations have similar perception scores but one plans faster, generalizes better, recovers after world change, needs less robot data or avoids unjustified actions, it is a stronger robot-world representation.

Eventually compare, under matched data/compute/tasks:

```text
policy alone
vs policy + persistent worldview
```

---

## RQ16 — What does “type” mean for a machine?

Possible type systems:

- semantic category;
- geometry/topology;
- dynamical response;
- affordance;
- learned equivalence class of predicted transformations.

Historical Clover type growth should be re-evaluated against these alternatives. The target is transfer to novel objects/actions, not reproducing human category names.

---

## RQ17 — What should remain invariant across embodiments?

A general robot brain may control arms, mobile manipulators, humanoids or quadrupeds. A promising separation is:

```text
embodiment-independent world state
+ embodiment-specific controllability/effect model
```

Open X-Embodiment makes this question increasingly testable:
https://github.com/google-deepmind/open_x_embodiment

---

## RQ18 — What is the correct relationship between world and action?

Candidate structures include:

```text
observation → action
observation → reasoning/plan → action
observation → explicit world → planning → action
observation + action ↔ future state
observation → generated futures → select action
```

Direct VLA, hierarchical embodied reasoning, model-based RL and world-action models are competing answers. No structure currently has universal dominance.

A recent survey of World-Action Models is useful context:
https://arxiv.org/abs/2609.16074

---

## RQ19 — How should real-world understanding be evaluated?

A credible claim needs more than one dataset:

1. controlled physical diagnostics;
2. shortcut-resistant pairs;
3. persistent-memory tests;
4. open-world real video;
5. causal interventions;
6. active perception;
7. long-horizon embodied tasks;
8. unseen environments;
9. measurable action usefulness.

RoboPhys-3D is a useful 2026 signal that perceptual/video quality can miss execution-level world-model failures:
https://arxiv.org/abs/2608.28718

---

## RQ20 — When should hardware influence the theory?

The scientific representation should not be selected merely because it is convenient on M4, CUDA or any other device. But once an algorithm is specified, hardware/software co-design matters.

Future questions include sparse vs dense operations, shared-state placement, CPU/GPU synchronization, Metal semantics, memory bandwidth and representation compression.

```text
M4 suitability ≠ scientific correctness
```

---

## RQ21 — Why did classical CPU-era vision not become general world understanding?

The answer is not simply “CPU was too slow.” Classical vision was often limited by handcrafted/task-specific representations, small-scale objectives and fragmented pipelines. Modern progress came from co-evolution of:

```text
learned representation
+ large datasets
+ scalable objectives
+ optimization
+ accelerator hardware
```

The lesson is not to abandon CPU. It is to avoid repeating the representation bottleneck while pursuing efficiency.

Historical anchors:

- SIFT: https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- AlexNet: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet: https://arxiv.org/abs/1512.03385
- ViT: https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020

---

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

A next-generation Clover proposal must state which research questions it answers, which evidence supports it, what would falsify it, and which questions remain open.
