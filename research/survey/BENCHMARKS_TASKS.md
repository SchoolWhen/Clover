# Benchmarks and Tasks

Last updated: 2026-10-15

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
+ real-execution world-model fidelity
+ hardware/setup robustness
+ offline policy-evaluation sanity checks
```

---

## 1. Evaluation hierarchy

### Level 1 — Cognitive / world-understanding diagnostics

Does the representation contain the structure needed to answer controlled questions about existence, identity, permanence, space, time, observability, physics, causality and counterfactuals?

### Level 2 — Persistent world-model capability

Can the model maintain, predict, reconstruct, revise or retrieve world state across time?

### Level 3 — Active evidence acquisition

Can the system recognize that current evidence is insufficient and deliberately obtain a better view or discriminating interaction?

### Level 4 — Embodied brain capability

Can a robot use its world understanding to complete unfamiliar physical tasks over long horizons, recover when the world changes and avoid unjustified action?

### Level 5 — Deployment / evidence robustness

Does the result survive:

```text
real-world execution comparison
hardware/calibration/control-loop changes
cross-simulator variation
offline-vs-rollout evaluation differences
latency / memory / runtime constraints
```

A final Clover result must eventually span all five levels.

---

## 2. Vision and learning-evidence protocol

### Observation protocol

- **V0:** monocular RGB + temporal order/timestamp; no depth/LiDAR/tactile/force/IMU/GT pose/GT identity.
- **V1:** V0 + camera intrinsics.
- **V2:** calibrated multi-camera RGB.
- **V3:** embodied active vision; action changes future visual evidence.

### Learning-evidence provenance

- `L0` visual self-supervision only;
- `L1` visual labels/annotations;
- `L2` language/world knowledge;
- `L3` action-conditioned demonstrations/experience;
- `L4` non-visual or privileged physical evidence.

Do not compare protocols as if they have the same information budget.

---

## 3. U1 — intuitive physics: IntPhys 2

- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Use for controlled permanence, immutability, continuity and solidity diagnostics.

---

## 4. U2 — anti-shortcut physical reasoning: MVP / Minimal Video Pairs

- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Use minimal-change paired videos to test whether physical-understanding gains survive counterexamples.

---

## 5. U3 — causal/counterfactual video reasoning: CausalVQA

- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Use language-only/question-only controls because language priors are a confound.

---

## 6. U4 — general visual/video diagnostics: Perception Test

- Code/data: https://github.com/google-deepmind/perception_test

Prefer visual subsets for tracking, memory, physics, temporal relations and grounded evidence.

---

## 7. U5 — persistent world memory: PersistBench

- Paper: https://arxiv.org/abs/2609.20819
- Project/code: https://guangzhaohe.com/persistbench

Use for object permanence, motion continuity and appearance preservation after objects leave the field of view.

---

## 8. U6 — streaming episodic memory: S-EMBER

- Official: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper: https://arxiv.org/abs/2607.02689

Use for grounded streaming recall and temporal evidence localization.

---

## 9. U7 — relational / calibration-independent physics: Principia

- Paper: https://arxiv.org/abs/2609.04200

Use for relational physical-law consistency beyond video appearance quality.

---

## 10. U8 — 3D/state/action-grounded world-model evaluation: RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

Keep distinct:

```text
plausible video
≠ correct 3D/state
≠ correct executable consequence
```

---

## 11. U9 — custom object permanence / occlusion battery

Test visible→occluded→visible, leave/re-enter FOV, similar-object swaps, camera motion, hidden external movement/removal.

Measure identity continuity, false persistence/absence, uncertainty, correction latency and memory cost.

---

## 12. U10 — unknown vs unobserved

Require the system not to treat missing evidence as absence.

Measure unjustified assertion, refusal/coverage, calibration and downstream action consequences.

---

## 13. U11 — world change and belief revision

```text
world hypothesis
→ hidden/external change
→ partial new evidence
→ stale-state detection
→ revision
→ downstream query/replan
```

Measure stale detection, incorrect persistence, update locality, recovery and recompute cost.

---

## 14. U12 — intervention twins

Use same/near-same visual prefixes with controlled different interventions and different valid consequences.

Measure consequence accuracy, affected-variable localization, false causal attribution and counterfactual consistency.

---

## 15. U13 — active perception

Relevant sources:

- Bajcsy Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage

Measure correctness, views/actions requested, information gain, avoidable motion, latency and unnecessary evidence collection.

---

## 16. U14 — novel object dynamics

Use objects/types absent from training labels where possible. Measure dynamic prediction, adaptation, transfer and language-prior sensitivity.

---

## 17. U15 — long-horizon household task

Use multi-step find→inspect→retrieve→transport→place tasks with hidden change/recovery. Record per-step world state, decision premise, action, execution effect, memory, recovery and latency.

Relevant suites:

- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/
- ManiSkill — https://github.com/haosulab/ManiSkill

---

## 18. U16 — real-execution world-model fidelity: WorldOracle

- Paper — https://arxiv.org/abs/2610.18826

WorldOracle gives an action-conditioned world model the **same initial observation and low-level action sequence** as a real execution, then compares predicted and actual outcomes.

It evaluates:

```text
physical state correctness
interaction spatial alignment
key interaction area fidelity
multi-view action coherence
```

The evaluation suite includes long multi-segment successful and failed real executions across multiple dynamics/embodiments.

Use for:

> whether a predicted world rollout matches what actually happened, not merely whether it looks plausible.

Do not infer policy quality or complete world understanding from this benchmark alone.

---

## 19. U17 — hardware/setup robustness: LIBERO-RIG

- Paper — https://arxiv.org/abs/2610.18843

LIBERO-RIG holds tasks fixed while perturbing eleven hardware/setup axes, including camera mounting/optics, camera-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height and gripper pads. Each axis has five severity levels, totaling 210 conditions across four LIBERO suites.

Reported pooled VLA success:

```text
nominal       0.932
mid severity  0.767
highest       0.509
```

Use for distinguishing:

```text
scene/task generalization
≠ hardware/calibration/control-loop robustness
```

---

## 20. U18 — long-horizon scaling: LADDER

- Paper — https://arxiv.org/abs/2610.18053
- Project — https://ladder.insait.ai

LADDER scales from 1 to 10 subgoals within controlled task families: 145 tasks, eight categories, two embodiments and 2,024 simulated episodes per evaluated system.

Reported signal:

```text
low-level policy: 85.4% at one subgoal
→ near zero on extended tasks
```

Orchestration improves performance but remains bounded by physical execution errors; a GPT-6 Astra tool-selection setup is reported around 62% with substantial time/cost.

Use for separating planning/orchestration failures from low-level execution compounding.

---

## 21. U19 — rollout-free offline policy evaluation: RoboFQE

- Paper — https://arxiv.org/abs/2610.18699

RoboFQE estimates target-policy return from offline robot trajectories without running new simulator, learned-world-model or real-world rollouts.

Use as an **EV4/offline sanity-check instrument** for policy ranking when real robot rollouts are unavailable or expensive.

Important boundary:

```text
offline policy evaluation
≠ closed-loop deployment validation
```

Its value is especially relevant when autoregressive video evaluators accumulate long-horizon prediction error.

---

## 22. U20 — partial-observability memory representation: Grid or Nodes?

- Paper — https://arxiv.org/abs/2610.18637

This controlled FloWM study compares a dense grid memory to an oracle-fed node/Kalman representation under partial observability.

Reported diagnostic signals include:

```text
out-of-view node memory: 14 KB
FloWM grid:             5.6 MB

diagonal OOD motion:
FloWM detection         11%
unchanged tracker       93%
```

The oracle node memory is not a deployable learned baseline. Use this study to motivate measurements of:

```text
memory bytes
representation inductive bias
out-of-distribution motion
probe/readout dependence
```

---

## 23. Supporting validation resources — not standalone “understanding” benchmarks

### RoboSimStudio

- Paper — https://arxiv.org/abs/2610.18835
- Project — https://robosimstudio.github.io

Use for explicit Real2Sim experiments where solver/contact model/physical parameters are editable and simulator hypotheses can be compared against observed behavior.

### RoboWM-Bench

- Paper — https://arxiv.org/abs/2604.19092

Use for visual-plausibility vs executable-behavior distinction.

### RoboTrustBench

- Paper — https://arxiv.org/abs/2606.01600

Use for constraint-sensitive, counterfactual and adversarial world-model evaluation.

### Video2World

- Paper — https://arxiv.org/abs/2610.04432

Use for geometric/dynamic/functional correctness of reconstructed simulation worlds.

---

## 24. Required reporting dimensions

Every serious architecture/baseline comparison should report a vector rather than one scalar.

At minimum:

```text
in-domain
held-out scene
held-out object/composition
held-out dynamics
camera shift
hardware/setup shift
real-world transfer
real-execution rollout fidelity
task/query correctness
coverage / answer rate
unjustified assertion rate
unknown/refusal quality
memory/persistence
recovery
latency p50/p95/p99
memory bytes
energy when measurable
```

Where relevant also include physical consistency, intervention accuracy, temporal evidence localization, update locality, planning/search cost, offline-evaluation uncertainty and task success.

Use Pareto analysis rather than hiding trade-offs inside one weighted score.

---

## 25. Anti-shortcut / robustness audit

Challenge results with:

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
camera calibration perturbation
control-rate perturbation
latency / frame-drop injection
cross-simulator replay
```

If a shortcut reproduces the score, the original result is weak evidence for world understanding.

---

## 26. First Understanding Battery candidate — expanded

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
U16 WorldOracle                       predicted-vs-real action-conditioned futures
U17 LIBERO-RIG                        hardware/setup robustness
U18 LADDER                            horizon scaling / compounding execution
U19 RoboFQE                           rollout-free offline policy evaluation
U20 Grid-or-Nodes diagnostic          memory efficiency / inductive bias
```

This battery is intentionally heterogeneous. U19 and U20 are supporting diagnostics, not replacements for real closed-loop evaluation.

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
+ real-execution grounding
+ hardware/setup perturbation
+ validation-evidence tier
```

not:

```text
one benchmark → “understanding solved”
```
