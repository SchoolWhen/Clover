# Research Questions

Last updated: 2026-10-14

Synthesis layer of the Clover Survey. Each question should be understood before the next Clover architecture is frozen.

> **SSOT:** How can a machine understand the real world through vision alone?

## 1. What is a world representation?
A SLAM map, 3D reconstruction, object graph, predictive latent, video generator, policy hidden state and simulator are all called “world models” but are not interchangeable. Candidate families: explicit geometry, object-centric state, distributed latent, continuous fields and generative simulators. **Status: OPEN.**

## 2. Must understanding be explicit?
Explicit state supports queries/revision/checking/planning, but distributed physical representations are real competitors. Meta study: https://arxiv.org/abs/2602.07050. Identifiable-latent bridge: https://arxiv.org/abs/2610.07028

## 3. Which parts of geometry should be learned?
Projective geometry, rotation, camera projection, visibility and bundle adjustment have strong mathematics; DUSt3R/VGGT show learned estimators can recover geometry robustly. https://arxiv.org/abs/2312.14132 · https://arxiv.org/abs/2503.11651 · https://arxiv.org/abs/2605.15195

## 4. Prediction, reconstruction or generation?
V-JEPA predicts latent future; VGGT reconstructs geometry; Atlas/Cosmos generate/simulate. These objectives preserve different information. ReWAM argues reconstruction fidelity alone does not guarantee control-useful state: https://arxiv.org/abs/2609.38163

## 5. What can vision alone identify?
Visible boundary/motion/texture are direct evidence. 3D shape, identity, support and persistence require assumptions/temporal evidence. Exact force, friction, mass or arbitrary hidden geometry are generally not uniquely identifiable. Needed states include observed, inferred, ambiguous, unobserved and contradicted.

## 6. What does interaction add?
Passive video learns broad dynamics; interaction adds controllability, intervention, action consequence, affordance and active information. V-JEPA 2 provides a concrete passive→action-conditioned example: https://arxiv.org/abs/2506.09985

## 7. Objects, fields, geometry, or combinations?
Objects help identity/composition; fields help local continuous structure; geometry supplies metric constraints. None obviously solves semantics+dynamics+causality alone. Historical Clover must re-test its field/entity hierarchy rather than preserve it.

## 8. What is persistent memory?
Possible memories: raw evidence, compressed world state, episodic events, semantic concepts, hybrids. VISTA shows the memory/retrieval harness itself can change long-horizon reasoning: https://arxiv.org/abs/2610.02200

## 9. How should memory revise itself?

```text
new evidence → contradiction → affected state → revision → downstream update
```

Evidence Replay remains a candidate, not a commitment.

## 10. What is physical understanding?
Suggested ladder: visual continuation → relevant state transition → invariants/constraints → intervention-sensitive prediction → counterfactual consistency → improved action/recovery.

## 11. What is causal understanding?

```text
correlation → predictive dependency → intervention-sensitive dependency → counterfactual model
```

Historical Counter-Witness causality is a candidate connecting prediction error and revision.

## 12. How should uncertainty/observability be represented?

```text
not visible ≠ empty
unobserved ≠ absent
unknown type ≠ nonexistent
low confidence ≠ false
confidence ≠ authority
```

Bayesian robotics/POMDPs remain important prior art.

## 13. What role should language play?
Language injects semantics/world knowledge/task concepts. Vision-only evaluation must distinguish visual inference from language-prior recall. Compare vision-only, vision+language prior, and vision-world-state + language task interface.

## 14. Do we need active perception?
Can the system represent what it does not know well enough to choose the next view/action? Vantage: https://arxiv.org/abs/2610.11810

## 15. Should a worldview measurably improve action?
Eventually compare matched strong policy vs policy+worldview on generalization, planning cost, recovery, sample efficiency and unjustified actions.

## 16. What does “type” mean for a machine?
Possible types: semantic, geometric, dynamical, affordance-based, or learned equivalence classes of predicted transformations. Evaluate by novel-object/action transfer.

## 17. What should remain invariant across embodiments?
Candidate separation:

```text
embodiment-independent world state
+ embodiment-specific controllability/effect model
```

Open X-Embodiment: https://github.com/google-deepmind/open_x_embodiment

## 18. What is the right world↔action relationship?
Direct policy, hierarchical reasoner, explicit world+planner, world-action model and generative simulator+planner are competing structures. WAM survey: https://arxiv.org/abs/2609.16074

## 19. How should real-world understanding be evaluated?
Combine controlled physics, shortcut-resistant pairs, persistent memory, real video, intervention, active perception, long-horizon tasks, unseen environments and action usefulness. RoboPhys-3D: https://arxiv.org/abs/2608.28718

## 20. When should hardware influence theory?
Hardware should not select the scientific representation, but algorithm/hardware co-design matters after the state and computation are defined. M4 suitability is not scientific correctness.

## 21. Why did CPU-era classical vision not become general world understanding?
Not simply speed: handcrafted/task-specific representations, fragmented pipelines, limited data scaling and weak end-to-end representation learning mattered. Modern progress co-evolved learned representation, data, objectives, optimization and accelerators.

Historical anchors: SIFT https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf · AlexNet https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf · ResNet https://arxiv.org/abs/1512.03385 · ViT https://arxiv.org/abs/2010.11929 · CLIP https://arxiv.org/abs/2103.00020

## 22. What should the next Clover architecture decision look like?

```text
Survey evidence
→ unresolved contradiction
→ candidate representations
→ discriminating experiment
→ architecture decision
→ implementation
```

A next-generation Clover proposal must state what it explains, what evidence supports it, what would falsify it and what remains open.
