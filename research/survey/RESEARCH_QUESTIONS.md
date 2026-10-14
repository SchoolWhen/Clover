# Research Questions

Last updated: 2026-10-14

Synthesis layer of the Clover Survey. These questions must be understood before the next Clover representation is frozen.

> **SSOT:** How can a machine understand the real world through vision alone?

> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

---

## 1. What exactly is hidden, and what is actually observed?

A camera observes images, not the world state itself. The underlying problem is partially observable.

Useful background:

- POMDPs in Robotics — https://arxiv.org/abs/2209.10342
- Probabilistic Robotics — https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Clover must distinguish at least:

```text
observed
inferred
predicted
ambiguous
unobserved
contradicted
```

**Status: OPEN.**

## 2. What is a world representation?

A SLAM map, 3D reconstruction, object graph, predictive latent, video generator, policy hidden state and simulator are all called “world models” but are not interchangeable.

Candidate families:

```text
explicit geometry
object/entity state
distributed predictive latent
continuous field
episodic/persistent memory
generative simulator
hybrid/identifiable latent
```

**Status: OPEN.**

## 3. Must understanding be explicit?

Explicit state supports direct queries, revision, verification and planning. Distributed representations remain serious counter-hypotheses.

- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Identifiable World Models — https://arxiv.org/abs/2610.07028

The question is not “can we name variables?” but whether explicit state produces capabilities that distributed state cannot match at comparable data/compute.

## 4. Which parts of geometry should be learned?

Projective geometry, camera projection, visibility and bundle adjustment have strong mathematical formulations. DUSt3R/VGGT show learned estimators can recover geometry robustly.

- ORB-SLAM3 — https://arxiv.org/abs/2007.11898
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651
- VGGT-Ω — https://arxiv.org/abs/2605.15195

Research target: identify the division of labor between exact structure and learned priors.

## 5. What does static visual SSL already solve?

DINOv3 now provides a stronger static baseline than the previous Survey assumed.

- DINOv3 — https://ai.meta.com/research/publications/dinov3/
- Code — https://github.com/facebookresearch/dinov3

Question:

> Which claimed world-understanding capabilities disappear when the comparator is a very strong frozen image representation rather than an older encoder?

## 6. Prediction, reconstruction or generation?

These objectives preserve different information:

- V-JEPA predicts in latent space — https://arxiv.org/abs/2506.09985
- VGGT/Ω reconstruct geometry — https://arxiv.org/abs/2605.15195
- Atlas/Cosmos generate/simulate — https://www.worldlabs.ai/blog/atlas · https://arxiv.org/abs/2606.02800
- ReWAM challenges reconstruction-only control state — https://arxiv.org/abs/2609.38163

Which objective produces the most useful state for persistence, prediction, causality and action?

## 7. Is reconstruction a sufficient proxy for spatial understanding?

VGGT-Ω provides direct evidence that reconstruction features can help VLA and language alignment.

- https://arxiv.org/abs/2605.15195

But spatial reconstruction does not automatically establish memory, causality or action utility.

Required comparison:

```text
reconstruction accuracy
vs
world-query accuracy
vs
persistent memory
vs
action improvement
```

## 8. What can vision alone identify?

Visible boundary, motion, texture and appearance are visual evidence. 3D shape, identity, support and persistence require temporal evidence and assumptions. Exact force, friction, mass or hidden geometry may be underdetermined.

The system must not silently convert learned priors into observations.

## 9. What does “vision alone” mean for training, not just deployment?

Existing V0–V3 labels describe observation at inference. Modern VLM/VLA systems may also learn from language, actions, proprioception or privileged simulator state.

Background Research proposes a second provenance annotation:

```text
L0 visual self-supervision
L1 visual labels
L2 language/world knowledge
L3 action-conditioned experience
L4 non-visual / privileged physical evidence
```

Question: how much capability is attributable to visual experience itself?

## 10. Objects, fields, geometry, or combinations?

Objects help identity/composition; dense features scale well; geometry supplies metric constraints; fields may support local continuous computation.

Relevant evidence:

- Slot Attention — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO — https://www.nature.com/articles/s41562-022-01394-8
- DINOv3 — https://arxiv.org/abs/2508.10104
- VGGT-Ω — https://arxiv.org/abs/2605.15195

Historical Clover must re-test its field/entity hierarchy rather than preserve it.

## 11. What is the difference between visible tracking and object permanence?

SAM 3.1 is a strong contemporary visible-entity baseline:

- research — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- code — https://github.com/facebookresearch/sam3

PersistBench explicitly evaluates what happens after the object leaves view:

- https://arxiv.org/abs/2609.20819

Question: what internal mechanism maintains identity/existence when perception no longer supplies the object?

## 12. What is persistent memory?

Possible memories:

```text
raw visual evidence
compressed world state
episodic events
object state
task state
semantic concepts
hybrids
```

Relevant sources:

- PersistBench — https://arxiv.org/abs/2609.20819
- S-EMBER — https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200

**Status: OPEN.** Evidence Replay is one candidate, not the default answer.

## 13. Which information may be forgotten safely?

A world model cannot retain all pixels indefinitely at high resolution.

The real problem is query/task sufficiency:

> What distinctions must survive compression for the family of world queries and actions the system claims to support?

Compare:

```text
fixed context
recurrent latent
hierarchical memory
query-conditioned retention
selective replay
```

## 14. How should memory revise itself?

```text
new evidence
→ contradiction
→ affected state
→ revision
→ downstream update
```

Measure stale detection, correction latency, update locality and downstream action recovery.

Historical belief-revision and proof/provenance machinery should only survive if they improve these outcomes.

## 15. What is physical understanding?

Suggested ladder:

```text
visual continuation
→ physical plausibility
→ relational/invariant consistency
→ task-relevant state transition
→ intervention-sensitive prediction
→ quantitative state when identifiable
→ improved action/recovery
```

Relevant instruments:

- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVP — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia — https://arxiv.org/abs/2609.04200
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

## 16. Do useful physical variables need compact coordinates?

Meta's mechanistic study reports distributed high-dimensional motion representations:

- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Question:

```text
compact interpretable state
vs
distributed decodable state
vs
identifiable hybrid
```

Which representation best supports generalization, intervention and action at matched cost?

## 17. What is causal understanding?

```text
correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Relevant sources:

- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- CRL identifiability — https://proceedings.mlr.press/v238/varici24a.html
- multi-node interventions — https://proceedings.mlr.press/v236/bing24a

Historical Counter-Witness causality is a candidate linking prediction error and revision; it must show intervention/counterfactual gains over learned dynamics.

## 18. What does interaction add?

Passive video can learn broad statistical dynamics. Interaction adds:

```text
controllability
intervention
action consequence
affordance
active information acquisition
```

V-JEPA 2 provides a concrete passive-video → action-conditioned example:

- https://arxiv.org/abs/2506.09985

Causal-representation theory also motivates interventions as information sources.

## 19. Do we need active perception?

Can the system represent uncertainty well enough to decide the next visual action?

- Bajcsy — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810

Core loop:

```text
ambiguity
→ information need
→ look/move/inspect
→ new RGB evidence
→ belief update
```

## 20. How should uncertainty and observability be represented?

```text
not visible ≠ empty
unobserved ≠ absent
unknown type ≠ nonexistent
low confidence ≠ false
confidence ≠ authority
plausible completion ≠ observed fact
```

Bayesian state estimation and POMDP belief state are important prior art. Historical Clover epistemic/licence semantics are one possible implementation, not the definition of the problem.

## 21. When is generative completion useful, and when is it dangerous?

Atlas/Cosmos demonstrate strong generation/simulation routes:

- Atlas — https://www.worldlabs.ai/blog/atlas
- Cosmos 3 — https://arxiv.org/abs/2606.02800

Question: can a model exploit plausible hidden completion for planning while retaining explicit knowledge that the completion is hypothetical rather than observed?

## 22. What role should language play?

Language injects semantics, world knowledge and task concepts.

Gemini ER 2, π0.5, OpenVLA and related systems mix visual evidence with language/action priors:

- Gemini ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- π0.5 — https://arxiv.org/abs/2504.16054
- OpenVLA — https://arxiv.org/abs/2406.09246

Vision-only evaluation must distinguish visual inference from language-prior recall.

## 23. Is a persistent world state actually necessary for strong robot behavior?

Direct and implicit policies are serious falsifiers:

- π0.5 — https://arxiv.org/abs/2504.16054
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1

Critical eventual comparison:

```text
strong matched policy
vs
strong matched policy + persistent world representation
```

A worldview must improve measurable embodied outcomes to justify itself.

## 24. What should the world↔action relationship be?

Competing structures:

```text
direct policy
hierarchical reasoner + VLA
explicit world + planner
world-action model
generative simulator + planner
```

Relevant evidence:

- Gemini ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- WAM survey — https://arxiv.org/abs/2609.16074
- HWAM — https://arxiv.org/abs/2610.12026

## 25. What does “type” mean for a machine?

Possible type systems:

```text
semantic category
geometry class
dynamical equivalence
affordance/effect equivalence
learned transformation class
```

Evaluate by transfer to novel objects/actions rather than human-label agreement alone.

## 26. What should remain invariant across embodiments?

Candidate separation:

```text
embodiment-independent world structure
+
embodiment-specific controllability/effect model
```

Relevant sources:

- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment
- Skild omni-bodied thesis — https://skild.ai/blogs/building-the-general-purpose-robotic-brain

## 27. How should real-world understanding be evaluated?

Combine:

```text
controlled physics
shortcut-resistant pairs
persistent memory
streaming recall
real video
intervention
active perception
world change/revision
long-horizon tasks
unseen environments
action usefulness
```

RoboPhys-3D is especially relevant to state/action-grounded evaluation:

- https://arxiv.org/abs/2608.28718

## 28. What should a Failure Matrix record?

At minimum:

```text
geometry
identity
permanence
temporal consistency
observability
memory/retrieval
physics
causality
counterfactuals
OOD/generalization
camera shift
revision/recovery
long horizon
action utility
compute
```

This matrix should exist before a new representation decision.

## 29. When should hardware influence theory?

Hardware should not select the scientific representation.

The order remains:

```text
science problem
→ representation
→ algorithm
→ compute structure
→ CPU/GPU/Metal/other mapping
```

M4 suitability is an engineering property, not scientific correctness.

## 30. Why did CPU-era classical vision not become general world understanding?

Not simply speed. Important limits included handcrafted/task-specific representations, fragmented pipelines, limited data scaling and weak learned abstraction.

Historical anchors:

- SIFT — https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- AlexNet — https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet — https://arxiv.org/abs/1512.03385
- ViT — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020

## 31. What should the next Clover architecture decision look like?

Not:

```text
interesting paper
→ add mechanism
```

Not:

```text
historical Clover idea
→ search for supporting evidence
```

Required chain:

```text
Background Research
→ strong baseline setup
→ Understanding Battery
→ Failure Matrix
→ unresolved cross-family contradiction
→ candidate representations
→ discriminating experiment
→ falsifier
→ architecture decision
→ implementation
```

A next-generation Clover proposal must state what observed failure it solves, what evidence supports it, what would kill it and what remains open.
