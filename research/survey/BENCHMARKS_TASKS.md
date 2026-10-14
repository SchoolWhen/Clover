# Benchmarks and Tasks

Last updated: 2026-10-14

Clover does not use a single benchmark as the definition of “understanding.” Benchmarks are instruments for discriminating representation hypotheses.

The current evaluation design follows:

```text
controlled capability diagnostic
+ anti-shortcut test
+ persistent/streaming memory test
+ causal/interventional test
+ real visual transfer
+ active perception
+ embodied long-horizon task
+ action usefulness
```

---

## 1. Evaluation hierarchy

### Level 1 — Cognitive / world-understanding diagnostics

Does the representation contain the structure needed to answer controlled questions about:

```text
existence
identity
permanence
space
time
observability
physics
causality
counterfactuals
```

### Level 2 — Persistent world-model capability

Can the model maintain, predict, reconstruct, revise or retrieve world state across time?

Examples:

- long occlusion;
- object leaving/re-entering field of view;
- streaming episodic retrieval;
- novel viewpoint;
- world change;
- contradiction/revision;
- intervention twins;
- future-state prediction.

### Level 3 — Active evidence acquisition

Can the system recognize that current evidence is insufficient and deliberately obtain a better view?

### Level 4 — Embodied brain capability

Can a robot use its world understanding to complete unfamiliar physical tasks over long horizons, recover when the world changes and avoid unjustified action?

A final Clover result must eventually span all four levels.

---

## 2. Vision and learning-evidence protocol

### Observation protocol

- **V0:** monocular RGB + temporal order/timestamp; no depth/LiDAR/tactile/force/IMU/GT pose/GT identity.
- **V1:** V0 + camera intrinsics.
- **V2:** calibrated multi-camera RGB.
- **V3:** embodied active vision; action changes future visual evidence.

Do not compare protocols as if they have the same information budget.

### Learning-evidence provenance

When material, annotate whether the model was trained with:

- `L0` visual self-supervision only;
- `L1` visual labels/annotations;
- `L2` language/world knowledge;
- `L3` action-conditioned demonstrations/experience;
- `L4` non-visual or privileged physical evidence.

A deployment-time RGB model trained using large text/action/privileged datasets is not equivalent to a `V0/L0` model.

---

## 3. U1 — intuitive physics: IntPhys 2

- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Controlled permanence, immutability, spatiotemporal continuity and solidity diagnostics using violation-of-expectation tests.

Use for: **conceptual intuitive physics under controlled visual conditions**.

Do not use as sole evidence for: real-world memory, quantitative physics, causality or robot autonomy.

---

## 4. U2 — anti-shortcut physical reasoning: MVP / Minimal Video Pairs

- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Each sample has a minimally changed paired video with the same question and opposite answer. Pair scoring directly attacks visual/textual shortcuts.

Use for: **whether a claimed physical-understanding gain survives minimal counterexamples**.

The experimental-design principle should also be copied into Clover custom tasks.

---

## 5. U3 — causal/counterfactual video reasoning: CausalVQA

- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Question families include:

```text
counterfactual
hypothetical
anticipation
planning
descriptive
```

Use for: broad real-video causal/counterfactual diagnostic.

Caution: natural-language QA can mix visual understanding with language priors. Record language-only/question-only controls.

---

## 6. U4 — general visual/video diagnostics: Perception Test

- Code/data: https://github.com/google-deepmind/perception_test

Contains real-world tracking, point tracking, action localization, video QA and grounded video QA tasks.

For Clover, prefer visual subsets that can isolate:

- object/point tracking;
- memory;
- physics;
- temporal relations;
- grounded evidence.

Do not silently use audio when reporting a vision-only protocol.

---

## 7. U5 — persistent world memory: PersistBench

- Paper: https://arxiv.org/abs/2609.20819
- Project/code: https://guangzhaohe.com/persistbench

PersistBench uses 360° video as an omniscient reference to evaluate models after objects leave the ordinary field of view.

Measures:

```text
object permanence
motion continuity
appearance preservation
```

This is a critical addition because:

```text
visible tracking / reconstruction
≠
persistent memory
```

Use it to test long-context, recurrent latent, explicit-state and replay-style memory systems under matched observation histories.

---

## 8. U6 — streaming episodic memory: S-EMBER

- Official: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper: https://arxiv.org/abs/2607.02689

S-EMBER evaluates causal streaming recall rather than offline search over an entire video file.

Important dimensions:

```text
answer correctness
temporal evidence localization
grounded recall
streaming/causal access
```

Use for: long-horizon visual memory where the system must remember what it actually saw and locate the supporting evidence.

---

## 9. U7 — relational / calibration-independent physics: Principia

- Paper: https://arxiv.org/abs/2609.04200

Principia evaluates Newtonian consistency through relations between paired objects, avoiding dependence on absolute scale/frame-rate/camera calibration.

Phenomena include:

```text
gravity
restitution
friction
rotational inertia
projectile motion
momentum
pendulum
mass-spring oscillation
```

Use for: whether a visual/world model preserves relational physical laws beyond video appearance quality.

---

## 10. U8 — 3D/state/action-grounded world-model evaluation: RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates generated/world-model rollouts at four levels:

```text
pixel fidelity
3D geometry consistency
state-level understanding
task-level completeness
```

Use for: testing the claim that plausible generated video corresponds to correct state and executable consequence.

Key principle:

```text
plausible video
≠
correct 3D/state
≠
correct executable consequence
```

---

## 11. U9 — custom object permanence / occlusion battery

Required custom tasks should isolate:

```text
visible → occluded → visible
visible → leaves FOV → reappears
multiple similar objects swap/cross
camera moves while object is hidden
object moved by external agent while hidden
object removed while hidden
```

Measure:

- identity continuity;
- false persistence;
- false absence;
- uncertainty during occlusion;
- re-identification latency;
- correction when expectation fails;
- memory bytes / compute.

---

## 12. U10 — unknown vs unobserved

Construct scenes where the correct answer requires refusing to treat missing evidence as a negative fact.

```text
unobserved ≠ free
unobserved ≠ absent
unknown type ≠ nonexistent
occluded ≠ removed
```

Measure:

- unjustified assertion rate;
- refusal/coverage;
- calibration;
- downstream action consequences.

---

## 13. U11 — world change and belief revision

Protocol:

```text
world hypothesis
→ hidden/external change
→ partial new evidence
→ stale-state detection
→ local/global revision
→ downstream query/replan
```

Measure:

- stale detection latency;
- incorrect persistence;
- update locality;
- dependent-query correctness;
- recovery time;
- memory/recompute cost.

This task is representation-neutral: explicit state, recurrent latent, long-context policy and replay systems should all be evaluated.

---

## 14. U12 — intervention twins

Create pairs with:

```text
same or near-same visual prefix
different controlled intervention
→ different valid consequence
```

Examples:

- support removed vs retained;
- object pushed vs untouched;
- container opened vs not opened;
- barrier moved vs fixed;
- tool applied vs merely present.

Measure:

- consequence accuracy;
- affected-variable localization when available;
- false causal attribution;
- counterfactual consistency;
- recovery latency.

This operationalizes intervention-sensitive world sufficiency without assuming a specific Clover causal representation.

---

## 15. U13 — active perception

Current observation is deliberately insufficient. The agent must decide whether and where to look/move/inspect.

Relevant sources:

- Bajcsy Active Perception: https://ieeexplore.ieee.org/abstract/document/5968
- Vantage: https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage

Measure:

```text
task/query correctness
actions/views requested
information gain
avoidable motion
latency
failure to seek evidence
unnecessary evidence collection
```

---

## 16. U14 — novel object dynamics

Use objects/types absent from training labels or semantic categories where possible.

The system should infer behavior from visual history and interaction rather than category lookup.

Measure:

- dynamic prediction;
- adaptation speed;
- transfer to new shapes/material appearance;
- language-prior sensitivity;
- action usefulness.

---

## 17. U15 — long-horizon household task

Canonical structure:

```text
find target
→ navigate / move camera
→ inspect/open
→ retrieve
→ transport
→ place
→ target moved or path blocked
→ re-observe
→ revise/replan
→ completion
```

Do not score only final success.

Record per step:

```text
world-state correctness
decision premise correctness
action/tool choice
execution effect
memory state
recovery
latency
```

Relevant future suites:

- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/ · https://robocasa.ai/leaderboard.html
- ManiSkill — https://github.com/haosulab/ManiSkill

---

## 18. Geometry / spatial diagnostics

Geometry methods should report, where applicable:

```text
pose error
depth error
point-map consistency
track consistency
relocalization
dynamic-scene robustness
camera-shift robustness
```

Relevant sources:

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- RAFT: https://arxiv.org/abs/2003.12039
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195

Geometry scores do not automatically establish semantics, causality, persistence or action usefulness.

---

## 19. Required reporting dimensions

Every serious architecture/baseline comparison should report a vector rather than one scalar.

At minimum:

```text
in-domain
held-out scene
held-out object/composition
held-out dynamics
camera shift
real-world transfer
task/query correctness
coverage / answer rate
unjustified assertion rate
unknown/refusal quality
memory/persistence
recovery
latency
memory bytes
energy when measurable
```

Where relevant also include:

- identity continuity;
- spatial error;
- physical consistency;
- intervention accuracy;
- temporal evidence localization;
- update locality;
- planning/search cost;
- task success.

Use Pareto analysis rather than hiding trade-offs inside one weighted score.

---

## 20. Anti-shortcut audit

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
minimal-change paired video
```

If a shortcut reproduces the score, the original result is weak evidence for world understanding.

---

## 21. Strong external robot capability references

These are capability references, not Clover-reproduced baselines:

- Gemini Robotics ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Gemini Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1
- π0.5 — https://arxiv.org/abs/2504.16054

For company-reported systems, preserve `OFFICIAL_REPORTED_RESULT` status unless independently reproduced.

---

## 22. First Understanding Battery candidate

```text
U1  IntPhys 2                         intuitive physics
U2  MVP                               anti-shortcut physical understanding
U3  CausalVQA                         causal/counterfactual video reasoning
U4  Perception Test visual subsets    tracking/memory/real-video perception
U5  PersistBench                      object permanence outside FOV
U6  S-EMBER                           streaming episodic memory
U7  Principia                         relational physical consistency
U8  RoboPhys-3D                       state/action-grounded world-model quality
U9  custom occlusion/reappearance     identity/permanence
U10 custom unknown/unobserved         epistemic correctness
U11 custom world change/revision      stale detection/belief revision
U12 custom intervention twins         intervention sensitivity
U13 custom active perception          information-seeking vision
U14 custom novel dynamics             open-world physical transfer
U15 long-horizon embodied task        action usefulness/recovery
```

This battery is intentionally heterogeneous. The objective is to find cross-family failure structure, not declare a winner from one number.

---

## Evaluation principle

```text
benchmark battery
+ shortcut resistance
+ persistent memory
+ causal intervention
+ real visual transfer
+ active evidence gathering
+ embodied long-horizon tasks
+ action usefulness
```

not:

```text
one benchmark → “understanding solved”
```
