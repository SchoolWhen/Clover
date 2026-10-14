# R-G — World Model ↔ Action: VLA, WAM and Planning

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

> **Does a robot need a persistent world model between perception and action, or can a sufficiently strong policy / world-action model solve the same problems implicitly?**

This is one of the strongest falsifiers for Clover's historical explicit-worldview direction.

Competing structures include:

```text
observation → action policy
observation/history → latent policy state → action
world representation → planner → action
predictive world model → model-based planning → action
joint world-action model → future state/action
high-level embodied reasoner → low-level VLA
```

No structure is assumed to win.

## 2. Open VLA baseline

### OpenVLA

- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

OpenVLA is a 7B open-source VLA trained on large-scale robot demonstrations and pretrained visual/language representations.

**Why it matters:** it is a practical, reproducible strong direct-policy comparator.

**Clover question:** what failure remains when a strong VLA already maps visual/language context directly to robot actions?

## 3. Open-world policy generalization

### π0.5

- Paper: https://arxiv.org/abs/2504.16054
- Official overview: https://www.pi.website/blog/pi05

π0.5 reports broad real-world manipulation generalization using heterogeneous multimodal and robot training.

**Research significance:** explicit persistent world state cannot be justified by saying direct policies inherently fail to generalize.

**Confound:** its training evidence is not vision-only; language, action and other supervision materially contribute.

## 4. World-Action Models

### World-Action Models for Robot Learning and Control: A Survey

- Paper: https://arxiv.org/abs/2609.16074
- Project: https://rcl-robotics.github.io/Awesome-World-Action-Models

WAMs explicitly couple future-world prediction with executable action generation.

The survey identifies open challenges including:

- world/action factorization;
- spatial and multi-view consistency;
- long-horizon memory;
- action alignment;
- closed-loop learning;
- efficient inference.

**Clover significance:** world modeling and action are increasingly being trained jointly rather than treated as rigid independent modules.

### World Action Models: The Next Frontier in Embodied AI

- Paper: https://arxiv.org/abs/2605.12090

Provides a complementary taxonomy distinguishing cascaded and joint WAMs and highlights evaluation across visual fidelity, physical commonsense and action plausibility.

## 5. Representation for world-action models is itself unresolved

### ReWAM

- Paper: https://arxiv.org/abs/2609.38163

ReWAM reports controlled evidence that reconstruction fidelity or generic pretrained perceptual features alone do not automatically produce the most useful control representation.

**Key lesson:**

```text
best reconstruction representation
≠ automatically best action representation
```

Task/action gradients can shape a bottleneck toward state useful for control.

### Being-M0.7

- Paper: https://arxiv.org/abs/2610.11283

Being-M0.7 learns visual-motion priors from mixed human data and then adapts them to humanoid action generation.

**Why it matters:** it is a strong 2026 example of compact future-aware latent state feeding whole-body action rather than explicit symbolic world state.

## 6. Hierarchical embodied reasoning remains competitive

### Gemini Robotics ER 2

- Official: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/

Gemini Robotics ER 2 is explicitly positioned as a high-level reasoner that understands physical situations, plans multi-step behavior and hands motor execution to a lower-level VLA.

**Clover significance:** the industry frontier itself contains both end-to-end policy routes and reasoner→policy hierarchies.

## 7. Strong implicit policies are serious falsifiers

### Figure Helix 2.5

- Official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Figure reports zero-shot whole-body autonomy across 30 unseen homes and large gains from human-experience pretraining.

### Skild S1

- Official report: https://www.skild.ai/blogs/s1
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Skild reports in-context robot task learning from a single video demonstration, including long-horizon unseen tasks.

These systems are not independently reproduced Clover baselines, but they raise the standard for any claim that explicit world state is necessary.

## 8. The required Clover falsifier

The eventual comparison must be matched as tightly as possible:

```text
strong policy
vs
same / comparable policy + Clover world representation
```

Measure:

- unseen-scene transfer;
- unseen-object transfer;
- long-horizon success;
- planning/search cost;
- sample efficiency;
- world-change recovery;
- active-perception quality;
- unjustified action rate;
- diagnosis/debuggability where measurable;
- latency and memory.

If a worldview provides no independent benefit, that is evidence against the worldview program, not a reason to change the metric.

## 9. World prediction must be evaluated through action consequences

### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D emphasizes 3D/state/task-grounded evaluation of generated world-model rollouts.

This supports a critical distinction:

```text
video quality
≠ state correctness
≠ action usefulness
```

### Reference action vs realized state

World-action research such as HWAM stresses that an intended/reference action and the state actually reached by the robot can diverge.

- HWAM: https://arxiv.org/abs/2610.12026

A robot brain must ultimately reason over realized world effects, not only issued action tokens.

## 10. Operational research questions

1. Does persistent world state improve strong direct policies on unseen environments?
2. Does prediction help action because it captures future state, or merely because it regularizes representation learning?
3. Should world and action be jointly trained or modularly connected?
4. What state should be embodiment-independent versus embodiment-specific?
5. Does explicit world state reduce planning/search cost?
6. Which world-model metrics correlate with actual task success?
7. How should execution feedback update the world model?
8. Can a high-level reasoner remain reliable without a persistent queryable world state?

## 11. Baseline families

| Family | Comparator | What it isolates |
|---|---|---|
| Direct VLA | OpenVLA | observation/language→action baseline |
| Open-world VLA | π0.5 evidence | broad generalization without exposed world state |
| Predictive WAM | ReWAM / Being-M0.7 | action-grounded predictive latent |
| High-level reasoner | Gemini Robotics ER 2 | reasoning/planning separated from motor VLA |
| Robot foundation policy | Helix 2.5 / S1 reports | strong real-world implicit policy/generalization |
| Explicit worldview + policy | future Clover candidate | must prove independent downstream value |

## 12. Discriminating experiments

### T-G-01 — Matched worldview value

Use the same task suite and, where possible, same visual/action backbone.

Compare:

```text
policy history only
policy + learned latent world model
policy + explicit/queryable world state
hybrid
```

### T-G-02 — World change recovery

Move the target or block the path mid-task.

Measure detection, replan latency and final success.

### T-G-03 — State correctness vs action success

Record both internal/world-query correctness and final task success.

This prevents a policy from looking “world-aware” merely because the final action happened to succeed.

### T-G-04 — Unseen embodiment/camera

Separate world representation transfer from controller transfer by changing camera or robot embodiment.

### T-G-05 — Prediction objective ablation

Compare reconstruction-, future-latent- and action-conditioned prediction at matched model/data scale.

## 13. Kill conditions

The explicit-worldview program should be weakened or rejected if a strong policy/WAM reaches equal or better:

- generalization;
- recovery;
- long-horizon success;
- sample efficiency;
- active perception;
- planning efficiency;

without the complexity of persistent explicit state.

Conversely, a direct policy should not be treated as sufficient if it fails systematically on state revision, unknown/unobserved handling or long-horizon world changes that a world-aware system solves.

## 14. Clover landing

Current conclusion:

> **World understanding must eventually prove value through action. The decisive scientific test is not whether a world representation is elegant, but whether it improves strong embodied baselines on generalization, recovery, planning and long-horizon behavior.**
