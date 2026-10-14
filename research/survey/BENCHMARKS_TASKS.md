# Benchmarks and Tasks

Last updated: 2026-10-14

Clover does not use a single benchmark as the definition of "understanding".

## Evaluation hierarchy

### Level 1 — Cognitive / world-understanding diagnostics
Does the representation contain the structure needed to answer a controlled question? Examples: permanence, collision, spatial relation, temporal order, causality and memory retrieval.

### Level 2 — World-model capability
Can the model predict, reconstruct, update or plan through world state? Examples: future prediction, long occlusion, novel viewpoint, world change, intervention twins and state reconstruction.

### Level 3 — Embodied brain capability
Can a robot use world understanding to complete unfamiliar physical tasks over long horizons? Examples: unseen homes, unknown objects, active information gathering, recovery, multi-room tasks and deformable manipulation.

A final Clover result should span all three levels.

## Vision protocol

- **V0:** monocular RGB + temporal order/timestamp; no depth/LiDAR/tactile/force/IMU/GT pose/GT identity.
- **V1:** V0 + camera intrinsics.
- **V2:** calibrated multi-camera RGB.
- **V3:** embodied active vision; action changes future visual evidence.

Do not compare protocols as if they have the same information budget.

## Physical understanding

### IntPhys 2
- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Controlled permanence, immutability, continuity and solidity diagnostics. Not sufficient for real-world memory, causal interaction or robot autonomy.

### MVPBench
- Paper: https://arxiv.org/abs/2506.09987
- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Minimal paired videos make shortcut exploitation harder. The experimental-design principle matters more than the leaderboard.

### CausalVQA
- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Targets counterfactual, hypothetical, anticipation, planning and cause/effect reasoning. Natural-language QA can still mix visual evidence with language priors.

## General video / egocentric understanding

- **Perception Test:** https://github.com/google-deepmind/perception_test
- **Something-Something:** https://developer.qualcomm.com/software/ai-datasets/something-something
- **EPIC-KITCHENS:** https://epic-kitchens.github.io/
- **Ego4D:** https://ego4d-data.org/ · https://ego4d-data.org/docs/

These cover tracking, motion, interactions, anticipation and real egocentric histories, but do not by themselves define persistent world state.

## Memory diagnostics

### VISTA-style isolation
- Paper: https://arxiv.org/abs/2610.02200

“Same base model, different visual-memory harness” is a valuable way to isolate memory/retrieval contribution.

### S-EMBER
- Meta publications: https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

Streaming egocentric retrieval is closer to persistent embodied memory than isolated clips.

## Spatial evaluation

Geometry methods should report pose/depth/point-map/track consistency, relocalization and dynamic-scene robustness. Geometry scores do not automatically establish semantics, causality or action usefulness.

Relevant sources:
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- Vantage: https://arxiv.org/abs/2610.11810
- SpatialCORE: https://arxiv.org/abs/2609.38716

## Robot task suites

- **LIBERO:** https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- **CALVIN:** https://github.com/mees/calvin
- **RoboCasa:** https://robocasa.ai/ · https://robocasa.ai/leaderboard.html
- **ManiSkill:** https://github.com/haosulab/ManiSkill

These are future task/evaluation resources, not the current optimization target.

## Execution-grounded world-model evaluation

### RoboPhys-3D
- Paper: https://arxiv.org/abs/2608.28718

Important direction: evaluate reconstructed/execution-relevant state rather than relying on perceptual/video quality alone.

```text
plausible video ≠ correct state ≠ correct executable consequence
```

## Proposed Clover capability tasks

### T1 — Object permanence
Observe object → occlusion/camera movement → reappearance. Measure identity continuity, uncertainty during occlusion and correction when expectation fails.

### T2 — Unknown vs unobserved
Occluded region must not be labeled free/absent because it is unseen.

```text
unobserved ≠ free ≠ absent ≠ unknown type
```

### T3 — World change and revision
World hypothesis → external change → partial evidence → local update → downstream replan. Measure stale-state detection and revision locality.

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

### T5 — Intervention twin
Nearly identical visual prefix, different controlled intervention, different consequence. Measure intervention sensitivity and counterfactual competence.

### T6 — Active perception
Current view is insufficient; agent must move/look/inspect to reduce ambiguity.

### T7 — Novel object dynamics
Unseen category/type; infer behavior from interactions rather than label lookup.

## Required future reporting

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

Where applicable: identity continuity, spatial error, physical consistency, intervention accuracy, update locality and planning cost.

## Anti-shortcut audit

Challenge world-understanding results with:

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

If a shortcut reproduces the score, the original score is weak evidence.

## Real-robot capability references

- Figure Helix 2.5: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1: https://skild.ai/blogs/s1
- Gemini Robotics ER 2: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

These are capability references, not independently reproduced Clover baselines.

## Evaluation principle

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
