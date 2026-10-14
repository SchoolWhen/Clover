# Benchmarks and Tasks

Last updated: 2026-10-14

Clover does not use a single benchmark as the definition of "understanding".

This document maps evaluation instruments to the capability they actually measure.

## 1. Evaluation hierarchy

### Level 1 — Cognitive / world-understanding diagnostics

Question: **Does the representation contain the structure needed to answer a controlled question?**

Examples: object permanence, collision, spatial relation, temporal order, causal/counterfactual reasoning and memory retrieval.

### Level 2 — World-model capability

Question: **Can the model predict, reconstruct, update or plan through world state?**

Examples: future prediction, image-goal planning, long occlusion, world change, novel viewpoint, intervention twins and state reconstruction.

### Level 3 — Embodied brain capability

Question: **Can a robot use world understanding to complete unfamiliar physical tasks over long horizons?**

Examples: unseen home, unknown object, active information gathering, mid-task world change, recovery, multi-room tasks and deformable manipulation.

A final Clover result should span all three levels.

## 2. Vision protocol must accompany every result

- **V0:** monocular RGB + temporal order/timestamp; no depth/LiDAR/tactile/force/IMU/GT pose/GT identity.
- **V1:** V0 + declared camera intrinsics.
- **V2:** calibrated multi-camera RGB.
- **V3:** embodied active vision; action changes future visual evidence.

Do not compare protocols as if they have the same information budget.

## 3. Intuitive physics

### IntPhys 2
- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Axes: permanence, immutability, spatio-temporal continuity and solidity.

Useful for controlled physical diagnostics; not sufficient for memory, causal interaction, open-world generalization or robot autonomy.

### MVPBench
- Paper: https://arxiv.org/abs/2506.09987
- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Minimal paired videos share a question but require opposite answers. The important contribution for Clover is the **anti-shortcut experimental design**, not only the leaderboard.

## 4. Causality / counterfactuals

### CausalVQA
- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Targets counterfactual, hypothetical, anticipation, planning and cause/effect reasoning over physical video.

Limitation: natural-language QA can mix visual evidence with language priors. Clover eventually needs machine-queryable intervention tasks too.

## 5. General video / egocentric understanding

### Perception Test
- Code: https://github.com/google-deepmind/perception_test

Broad video tasks: tracking, point tracking, action localization and QA.

### Something-Something v2
- Resource: https://developer.qualcomm.com/software/ai-datasets/something-something

Useful for motion/transformation-sensitive semantics; short clips do not test long-term world memory.

### EPIC-KITCHENS
- Official: https://epic-kitchens.github.io/

Useful for egocentric object interaction and anticipation.

### Ego4D
- Official: https://ego4d-data.org/
- Docs: https://ego4d-data.org/docs/

Useful for long-duration egocentric memory, place/object continuity and forecasting.

## 6. Memory

### VISTA-style memory isolation
- Paper: https://arxiv.org/abs/2610.02200

The valuable experiment is “same base model, different memory/retrieval harness”, which isolates the contribution of visual evidence memory.

### S-EMBER
- Meta publications: https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

Streaming egocentric retrieval is closer to persistent embodied memory than isolated short-video QA.

## 7. Spatial evaluation

Geometry methods should be measured through camera/pose/depth/point-map/track consistency, relocalization and dynamic-scene robustness. These measurements do not automatically establish semantics, causality or action usefulness.

Relevant method sources:
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- Vantage: https://arxiv.org/abs/2610.11810
- SpatialCORE: https://arxiv.org/abs/2609.38716

## 8. Robot learning/task suites

### LIBERO
- Project: https://libero-project.github.io/main.html
- Code: https://github.com/Lifelong-Robot-Learning/LIBERO

Useful for lifelong transfer; later Clover evaluation should inspect world/recovery value, not only policy success.

### CALVIN
- Code: https://github.com/mees/calvin

Useful for long-horizon task sequences; language conditioning is a confound for strict vision-only claims.

### RoboCasa / RoboCasa365
- Project: https://robocasa.ai/
- Leaderboard: https://robocasa.ai/leaderboard.html

Household/kitchen scene diversity and seen-vs-unseen compositional tasks are highly relevant to eventual robot-brain evaluation.

### ManiSkill
- Code: https://github.com/haosulab/ManiSkill

Potential scalable task/simulation infrastructure, not a definition of understanding.

## 9. World-model physical evaluation

### RoboPhys-3D
- Paper: https://arxiv.org/abs/2608.28718

Important direction: evaluate reconstructed/execution-relevant state rather than relying on perceptual/video quality alone.

Principle:

```text
plausible video ≠ correct state ≠ correct executable consequence
```

## 10. Proposed Clover capability tasks

### T1 — Object permanence
Observe object → occlusion/camera movement → reappearance. Measure identity continuity, uncertainty during occlusion and correction when expectation fails.

### T2 — Unknown vs unobserved
Occluded region must not be labeled free/absent simply because it is unseen.

```text
unobserved ≠ free ≠ absent ≠ unknown type
```

### T3 — World change and revision
Build world hypothesis → external change → partial evidence → local update → downstream replan. Measure stale-state detection and revision locality.

### T4 — Long-horizon household task

```text
find target
→ navigate
→ inspect/open
→ retrieve
→ transport
→ place
→ recover from moved target / blocked path
```

Measures memory, space, active perception, decision and recovery.

### T5 — Intervention twin
Nearly identical visual prefix, different controlled intervention, different valid consequence. Measure intervention sensitivity and counterfactual competence.

### T6 — Active perception
Current view is insufficient; agent must move/look/inspect to reduce ambiguity. Measure awareness of missing evidence and information-gaining action selection.

### T7 — Novel object dynamics
Unseen category/type; infer behavior from observed interactions rather than label lookup. Measure open-world dynamics/type induction and action transfer.

## 11. Required future reporting dimensions

At minimum:

```text
task success
world-state correctness
coverage / answer rate
unjustified assertion rate
unknown/refusal quality
generalization
recovery
latency
memory
energy when measurable
```

Where applicable also report identity continuity, spatial error, physical consistency, intervention accuracy, update locality and planning cost.

## 12. Anti-shortcut audit

Challenge any world-understanding result with:

```text
background-only
foreground-only
single-frame
temporal shuffle
reversed video
crop
camera metadata
scene ID
duplicate / near-duplicate
language-only
question-only
```

If a shortcut reproduces the score, the original score is weak evidence of world understanding.

## 13. Real-robot capability references

These are current capability references, not independently reproduced Clover baselines.

- Figure Helix 2.5: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1: https://skild.ai/blogs/s1
- Gemini Robotics ER 2: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

The durable frontier is moving toward unseen environments, long horizons, active perception, mobile/whole-body manipulation and recovery.

## 14. Evaluation principle

The end state should combine:

```text
controlled diagnostics
+ shortcut-resistant tests
+ real-world visual transfer
+ embodied long-horizon tasks
+ action usefulness
```

not:

```text
one benchmark → "understanding solved"
```
