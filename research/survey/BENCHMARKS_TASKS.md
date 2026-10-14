# Benchmarks and Tasks

Last updated: 2026-10-14

Clover does not use a single benchmark as the definition of "understanding".

This document maps evaluation instruments to the capability they actually measure.

---

# 1. Evaluation hierarchy

A useful evaluation stack has three levels.

## Level 1 — Cognitive / world-understanding diagnostics

Question:

> Does the representation contain the structure needed to answer a controlled question?

Examples:

- object permanence;
- collision;
- spatial relation;
- temporal order;
- causal/counterfactual reasoning;
- memory retrieval.

These tests are valuable because they isolate mechanisms.

They are not sufficient because a model can score well without being a useful robot brain.

## Level 2 — World-model capability

Question:

> Can the model predict, reconstruct, update or plan through world state?

Examples:

- future prediction;
- image-goal planning;
- long occlusion;
- world change;
- novel viewpoint;
- intervention twins;
- state reconstruction.

## Level 3 — Embodied brain capability

Question:

> Can a robot use the world understanding to complete unfamiliar physical tasks over long horizons?

Examples:

- unseen home;
- unknown object;
- active information gathering;
- mid-task world change;
- recovery;
- multi-room tasks;
- deformable manipulation.

A final Clover result should span all three levels.

---

# 2. Vision protocol must accompany every result

## V0 — Strict monocular vision

Input:

- RGB;
- temporal order/timestamp.

No:

- depth;
- LiDAR;
- tactile;
- force;
- IMU;
- GT pose;
- GT object identity.

## V1 — Calibrated monocular

V0 plus camera intrinsics.

## V2 — Calibrated multi-camera

Multiple RGB cameras.

## V3 — Embodied active vision

The robot can act to change future visual evidence.

Do not compare V0 and V2 results as if they had the same information budget.

---

# 3. Intuitive physics

## 3.1 IntPhys 2

- Official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Main axes:

```text
Permanence
Immutability
Spatio-Temporal Continuity
Solidity
```

Why useful:

- controlled;
- violation-of-expectation style;
- targeted physical invariants.

What it does not prove:

- persistent real-world memory;
- action usefulness;
- open-world object generalization;
- causal intervention competence;
- real robot autonomy.

Use label:

`DIAGNOSTIC`

---

## 3.2 MVPBench

- Paper: https://arxiv.org/abs/2506.09987
- Official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Design:

A visually similar pair shares the same question but has opposite correct answers.

The pair must be answered correctly as a unit.

Why useful:

- explicitly suppresses superficial shortcuts;
- forces sensitivity to the physically relevant difference.

Clover should borrow this **experimental design principle**, not merely chase the leaderboard.

---

# 4. Causality / counterfactuals

## 4.1 CausalVQA

- Official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Focus:

```text
counterfactual
hypothetical
anticipation
planning
cause/effect
```

Why useful:

Moves beyond descriptive video QA.

Limitation:

Natural-language QA can still blur:

```text
visual evidence
and
language prior knowledge
```

A Clover-specific causal evaluation should eventually contain non-language machine-queryable tasks and controlled interventions.

---

# 5. General video understanding

## 5.1 Perception Test

- Repository: https://github.com/google-deepmind/perception_test

Tasks include:

- video QA;
- object tracking;
- point tracking;
- action localization;
- grounded video reasoning.

Use:

Broad diagnostic coverage.

Limitation:

Not a persistent world-model benchmark by itself.

---

## 5.2 Something-Something v2

- Dataset/project: https://developer.qualcomm.com/software/ai-datasets/something-something

Use:

Motion/action understanding.

Why Clover cares:

Actions are defined by object transformations and temporal structure, making the dataset useful for representation diagnostics.

Limitation:

Short clips; weak persistent memory requirement.

---

## 5.3 EPIC-KITCHENS

- Official site: https://epic-kitchens.github.io/

Use:

- egocentric action;
- object interaction;
- anticipation;
- real household visual dynamics.

Limitation:

Dataset labels/tasks do not directly define a world state.

---

## 5.4 Ego4D

- Official: https://ego4d-data.org/
- Documentation: https://ego4d-data.org/docs/

Use:

Large-scale egocentric real-world visual history.

Potential Clover questions:

- long-term object continuity;
- place understanding;
- episodic memory;
- forecasting;
- action context.

---

# 6. Memory

## 6.1 VISTA / ARC-AGI-3 style interactive memory

VISTA paper:

https://arxiv.org/abs/2610.02200

The interesting experimental idea is not ARC-AGI-3 as a world-understanding benchmark.

It is:

> Same underlying model, different visual-memory harness.

This isolates the contribution of evidence memory/retrieval.

## 6.2 S-EMBER

Official Meta publication listing:

https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

Why track:

Streaming egocentric retrieval is closer to long-lived embodied visual memory than isolated short clips.

---

# 7. Spatial understanding / reconstruction

## 7.1 Geometry metrics

For VGGT/VGGT-Ω/SLAM-style systems, useful measurements include:

- camera pose error;
- depth error;
- 3D point-map error;
- track consistency;
- loop/relocalization robustness;
- dynamic-scene failure.

But geometry score is not enough for:

- semantics;
- causality;
- identity under category/appearance change;
- action utility.

## 7.2 Spatial reasoning benchmarks

Vantage paper:

https://arxiv.org/abs/2610.11810

SpatialCORE paper:

https://arxiv.org/abs/2609.38716

These lines are useful for testing whether better evidence organization / grounding improves spatial reasoning.

Clover should distinguish:

```text
metric geometry
qualitative relation
task-relevant geometry
```

---

# 8. Robot datasets as evaluation environments

## 8.1 LIBERO

- Project: https://libero-project.github.io/main.html
- Code: https://github.com/Lifelong-Robot-Learning/LIBERO

Focus:

- lifelong robot learning;
- knowledge transfer;
- task suites.

Use for Clover later:

Testing whether a worldview improves transfer/recovery, not merely policy success.

---

## 8.2 CALVIN

- Code: https://github.com/mees/calvin

Focus:

Long-horizon language-conditioned manipulation sequences.

Use:

Sequence completion / long-horizon consistency.

Caution:

Language-conditioned success is not pure visual understanding.

---

## 8.3 RoboCasa / RoboCasa365

- Project: https://robocasa.ai/
- Leaderboard: https://robocasa.ai/leaderboard.html

Why useful:

Large variety of kitchen scenes and compositional household tasks.

Particularly relevant distinction:

```text
seen atomic task
vs
seen composite
vs
unseen composite
```

This is closer to general robot-brain evaluation than isolated manipulation.

---

## 8.4 ManiSkill

- Code: https://github.com/haosulab/ManiSkill

Use:

Large-scale robot simulation and task development.

Role for Clover:

Potential infrastructure later, not a scientific definition of understanding.

---

# 9. Robot/world-model evaluation

## 9.1 RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

Why important:

A growing world-model evaluation direction measures more than visual quality.

The key idea is to reconstruct/measure state and execution-relevant physical outcome.

This supports the Clover principle:

> **Plausible video is not enough; the world state must be correct enough for action.**

---

# 10. Final embodied tasks should be capability-based, not dataset-based

Clover should eventually define a small number of high-value real task families.

## T1 — Object permanence

Example:

1. observe object A;
2. object becomes occluded;
3. camera/robot moves;
4. object reappears;
5. query identity and location.

Required evidence:

- same-object continuity;
- uncertainty during occlusion;
- correction if expectation fails.

## T2 — Unknown vs unobserved

Example:

Robot sees a room with an occluded area.

Ask:

- is the area free?
- is there an object?
- do you know?

Correct response requires:

```text
unobserved
≠
free
≠
absent
```

## T3 — World change

1. build a world hypothesis;
2. an external agent changes the scene;
3. observe partial evidence;
4. update only affected state;
5. recover plan.

Measures:

- stale-state detection;
- belief revision;
- downstream replan.

## T4 — Long-horizon household task

Example:

```text
find target
→ navigate
→ open/inspect area
→ retrieve
→ transport
→ place
→ recover from moved target / blocked path
```

Measures:

- memory;
- spatial state;
- active perception;
- decision;
- recovery;
- execution.

## T5 — Intervention twin

Two episodes share nearly identical visual prefix.

A controlled intervention differs.

The model must predict different consequences.

Measures:

- intervention sensitivity;
- causal state;
- counterfactual competence.

## T6 — Active perception

The target state is not identifiable from the current view.

The agent must choose a visual action:

```text
move camera
change viewpoint
approach
look behind
```

Measures:

- knowing what is unknown;
- selecting information-gaining action;
- updating belief.

## T7 — Novel object dynamics

Introduce object not present in training categories.

The system must infer behavior from observed interactions rather than name/class label.

Measures:

- open-world representation;
- dynamics/type induction;
- action transfer.

---

# 11. Required evaluation dimensions

Every serious future Clover experiment should report more than task success.

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

When applicable:

```text
identity continuity
spatial error
physical consistency
causal/intervention accuracy
world-update locality
planning search cost
```

---

# 12. Anti-shortcut audit

A "world understanding" result should be challenged with:

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

If a shortcut reproduces the score, the original score is not strong evidence of visual world understanding.

MVPBench is a useful external example of this philosophy.

---

# 13. Real-robot capability references

These are not benchmarks we control, but they define the capability frontier.

## Figure Helix 2.5

- https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Reported:

- unseen homes;
- long-horizon whole-body tasks;
- active perception;
- rigid/deformable manipulation.

## Skild S1

- https://skild.ai/blogs/s1

Reported:

- in-context video task specification;
- long-horizon unseen tasks.

## Gemini Robotics ER 2

- https://deepmind.google/models/gemini-robotics/embodied-reasoning/

Reported:

- embodied/spatial reasoning;
- high-level planning;
- tool orchestration.

These are capability references, not independently reproduced Clover baselines yet.

---

# 14. Evaluation principle

The end state should look like:

```text
controlled diagnostics
        +
shortcut-resistant tests
        +
real-world visual transfer
        +
embodied long-horizon tasks
        +
action usefulness
```

not:

```text
one benchmark
→ "understanding solved"
```
