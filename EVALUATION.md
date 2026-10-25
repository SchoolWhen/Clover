<a id="top"></a>

# Evaluation and evidence

Maintained: **2026-10-25** · Current project stage: **Research** ([status](STATUS.md)).

Benchmarks, capability batteries, protocol controls and the evidence ladder. Designs and external results are not Clover measurements.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="evidence-retention-diagnostics"></a>

## 2026-10-25 当前补充：压缩与证据保留的区分条件

**下一步应区分的资料与诊断问题：**

| 问题 | 必须保留的对照 | 不能用来替代的指标 |
|---|---|---|
| 压缩是否删掉了当前任务证据 | 同一骨干、同一采样视频、原 tokens / 压缩 tokens | 仅 FLOPs 或吞吐 |
| 当未来任务改变，历史细节是否还可用 | 压缩前不透露后续 query；同字节预算的状态、显式记忆、可检索原证据对照 | 同一问题上的平均 QA 分数 |
| 失败来自采样还是表示 | 原始视频、采样帧、视觉编码、合并/裁剪逐层对照 | 把低帧率错漏全部归罪于推理 |
| 再观察能否补回缺失信息 | 可再观察 / 事件已消失或动作不可逆 | 假定每次都能安全重看 |
| 效率是否满足具身循环 | 含解码、编码、检索、状态更新的端到端 P50/P95 与峰值内存 | 已缓存编码、LLM 子阶段加速或外部 GPU 比例 |

这是后续分析与证据登记的区分表，不是要求 Stage 1 立即实施一套架构。物体永久性和未知任务的证据保留问题仍开放；当前两项压缩工作只是强效率参照。

## Contents

- [Stage 6 — Evaluation](#topic-research-evaluation)
- [Evaluation Principles](#topic-docs-evaluation-evaluation-principles)
- [Clover Understanding Battery — Working Design](#topic-docs-evaluation-understanding-battery)
- [Evaluation & Benchmark Map](#topic-docs-evaluation-benchmark-map)
- [Benchmarks and Tasks](#topic-research-survey-benchmarks_tasks)

<a id="topic-research-evaluation"></a>

## Stage 6 — Evaluation

### Experiments, Results and Falsification

Source record updated: 2026-10-14

**Status:** FRAMEWORK DEFINED; full execution is downstream of Analysis, Synthesis and selected implementations.

Evaluation asks whether the claimed capability actually appears under controlled conditions and whether it survives comparison with strong alternatives.

### Evidence ladder

```text
unit / synthetic diagnostic
→ controlled benchmark
→ controlled real-world test
→ unfamiliar real environment
→ long-horizon embodied task
```

Not every question requires the full ladder, but claims must not exceed the highest evidence level reached.

### Required result metadata

```text
hypothesis or baseline
exact model / checkpoint
exact code version
exact dataset / split
visual protocol V0–V3
learning provenance L0–L4
prompt / query protocol when applicable
hardware
metric definition
number of trials
uncertainty / variance
failure cases
reproduction status
```

### Evaluation dimensions

- geometry;
- identity;
- object permanence;
- temporal consistency;
- observability / unknown;
- memory / retrieval;
- belief revision;
- intuitive physics;
- quantitative / relational physics;
- causality / intervention;
- counterfactual reasoning;
- active perception;
- open-world generalization;
- camera / embodiment shift;
- planning usefulness;
- action success;
- recovery;
- latency / memory / energy when relevant.

### Baseline rule

Compare across qualitatively different method families, not only variants of Clover.

### Results rule

Report negative results. Preserve failures that kill an idea. Do not hide trade-offs behind one average score.

### Output

Stage 6 produces result tables, figures, ablations, failure logs and explicit hypothesis status changes. Interpretation belongs to Stage 7 Reflection.

---

<a id="topic-docs-evaluation-evaluation-principles"></a>

## Evaluation Principles

### 1. Benchmarks are instruments

A benchmark answers a narrow measurement question. It does not define Clover's research problem.

### 2. Capability before leaderboard position

Before asking whether Clover is first on a leaderboard, ask whether the protocol measures a capability required by a general-purpose visual robot brain.

### 3. Use real tasks at the top of the evidence hierarchy

Controlled benchmarks are essential for diagnosis, but the eventual claim must survive unfamiliar physical environments and embodied tasks.

### 4. Separate perception success from world-model success

Detection, segmentation, depth, flow, reconstruction and tracking can each be excellent while the system still lacks a persistent, revisable world model.

### 5. Separate prediction from causality

Future prediction is evidence of useful dynamics, not automatically causal understanding. Strong causal claims require intervention-sensitive or counterfactual protocols.

### 6. Separate answer accuracy from coverage

If a system can refuse or return Unknown, report at minimum:

- coverage;
- correctness conditional on answering;
- unjustified assertion rate;
- refusal/unknown rate.

A system cannot obtain an apparent scientific win by refusing almost everything.

### 7. Track privileged information

Every evaluation should document what enters the model:

- RGB only?
- camera calibration?
- multiple cameras?
- depth?
- language?
- actions/proprioception?
- ground-truth state?

Examiner truth must not leak into the model path.

### 8. Attack shortcuts

Where possible use minimal pairs, scene/background probes, temporal shuffle, crop-only and language-only controls.

### 9. Compare representations on downstream consequences

Representation quality should eventually be judged by what it enables:

- better generalization;
- more reliable world queries;
- faster recovery;
- less data;
- better planning;
- lower compute;
- more stable long-horizon behavior.

### 10. Report evidence provenance

Distinguish:

- independently reproduced result;
- peer-reviewed/public benchmark result;
- official project result;
- vendor-reported closed-system result;
- Clover internal result.

Do not present these as equivalent evidence.

---

<a id="topic-docs-evaluation-understanding-battery"></a>

## Clover Understanding Battery — Working Design

**Status:** OPEN / design document
**Purpose:** define what a future comprehensive evaluation would need to measure without turning any one benchmark into the project objective.

### 1. Principle

The battery must answer:

> **Does the system form and use a coherent world understanding from visual evidence?**

A future scientific result should combine controlled diagnostics, open-world visual data and embodied tasks.

### 2. Capability families

#### U1 — Existence and observability

Questions:

- Is something present?
- Was it observed?
- Is it currently unobserved rather than absent?
- Is free space actually established or merely unseen?

Failure to distinguish these states is a fundamental worldview error.

#### U2 — Identity and permanence

Questions:

- Is this the same entity after viewpoint change?
- Does the entity persist through occlusion?
- Can it reappear after leaving the field of view?
- Can the system handle split/merge/deformation without arbitrary ID continuity?

Potential instruments: EgoTracks, SAM 2-style tracking baselines, custom occlusion/reappearance sequences.

#### U3 — Spatial structure

Questions:

- Where is an entity relative to the camera/world/other entities?
- Is A inside/on/behind/near B?
- What space is traversable?
- Does geometry remain coherent across views?

Potential instruments: geometry/reconstruction benchmarks, controlled multi-view tasks.

#### U4 — Temporal structure and dynamics

Questions:

- What changed?
- What is moving, and how?
- Which state is stable?
- What happens next?

Potential instruments: Perception Test, Something-Something V2, controlled trajectory tasks.

#### U5 — Intuitive physics

Questions:

- Can an object disappear without cause?
- Can solids interpenetrate?
- Is a trajectory physically continuous?
- Which events are possible/impossible?

Potential instrument: IntPhys 2.

#### U6 — Causality and counterfactuals

Questions:

- Why did the state change?
- What would happen under a different intervention?
- What action would produce a requested world-state change?

Potential instruments: CausalVQA plus future intervention twins in simulation/robotics.

#### U7 — Memory and revision

Questions:

- Can a fact survive outside the current context window?
- Can later evidence correct an earlier world belief?
- Can stable knowledge be consolidated without retaining every frame?

Potential instruments: Ego4D long-history subsets + custom long-duration visual tasks.

#### U8 — Generalization

Hold out:

- objects;
- scenes;
- compositions;
- viewpoints;
- dynamics;
- robot environments.

The key is not only OOD accuracy but whether the system knows when the new case invalidates an existing assumption.

#### U9 — Active perception

Task form:

Two or more world hypotheses remain indistinguishable from the current view. The robot must choose a visual action that resolves the ambiguity before committing to a downstream action.

This directly tests whether uncertainty can drive information-seeking behavior.

#### U10 — Decision usefulness

Compare downstream agents with and without the candidate worldview while controlling the rest of the stack as much as possible.

Measure:

- task success;
- unnecessary actions;
- replanning;
- recovery from world changes;
- search/compute cost;
- unsafe/unjustified commitments.

### 3. Anti-shortcut requirements

Every core diagnostic should consider:

- minimal pairs;
- background-only probe;
- static-frame probe;
- temporal shuffle;
- crop/scene-ID leakage;
- near-duplicate audit;
- language-only baseline when language is involved.

### 4. Pure-vision protocol labels

Results should identify the sensory protocol explicitly:

- **V0:** monocular RGB + temporal ordering;
- **V1:** RGB + camera calibration;
- **V2:** calibrated multi-camera RGB;
- **V3:** embodied active vision where actions determine future views.

Do not collapse these into one 'vision-only' number.

### 5. Evidence levels

A claim can have different evidence levels:

1. **unit/mechanism evidence**;
2. **controlled scientific diagnostic**;
3. **public benchmark evidence**;
4. **real-world visual transfer**;
5. **embodied task evidence**;
6. **unseen real-environment evidence**.

A high score at a lower level does not imply the higher levels.

### 6. Current status

This battery is a map for future evaluation. The current project phase is not yet running the complete battery. Its immediate purpose is to stop research from collapsing onto one convenient metric.

---

<a id="topic-docs-evaluation-benchmark-map"></a>

## Evaluation & Benchmark Map

Source record updated: 2026-10-14

Benchmarks are measurement instruments. This map records what each instrument is capable of measuring, what it cannot establish, and how it may eventually contribute to a broader Clover evaluation.

### 1. Intuitive physics

#### IntPhys 2

**Primary source:** https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/

**Measures:** violation-of-expectation judgments around four macroscopic principles:

- Permanence
- Immutability
- Spatio-Temporal Continuity
- Solidity

**Strengths:** controlled synthetic environment, clean possible/impossible contrast, human reference performance.

**Known limitation for Clover:** success is still a narrow judgment task. A model could distinguish violations without constructing a persistent general-purpose world state useful for robotics.

**Role:** physics diagnostic, not project objective.

---

### 2. Shortcut resistance

#### Minimal Video Pairs (MVPBench)

**Primary source:** https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

**Scale reported by authors:** 55K multiple-choice video QA examples.

**Core design:** each example has a visually similar minimal-change pair with the same question and opposing answer; credit requires the pair to be answered consistently.

**Strength:** explicitly attacks superficial visual/textual shortcuts.

**Role for Clover:** not only a benchmark; its minimal-pair philosophy should influence our own scientific tests.

---

### 3. Causal and counterfactual video reasoning

#### CausalVQA

**Primary source:** https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

**Question families:**

- counterfactual;
- hypothetical;
- anticipation;
- planning;
- descriptive.

**Strength:** real-world video rather than only narrow simulation.

**Limitation:** QA correctness does not prove that the model maintains a causal world representation; language priors can contribute.

**Role:** causal reasoning diagnostic paired later with intervention-based robot/simulation experiments.

---

### 4. General video perception and reasoning

#### Perception Test

**Primary source:** https://github.com/google-deepmind/perception_test

Tasks include:

- multiple-choice video QA;
- object tracking;
- action localization;
- point tracking;
- sound localization;
- grounded video QA.

The dataset was designed around memory, abstract patterns, physics and semantics. Clover should restrict itself to compatible visual-only tasks when evaluating the SSOT.

**Role:** broad diagnostic battery, especially tracking/memory/physics subsets.

#### Something-Something V2

**Role:** motion/action representation diagnostic. Useful for measuring temporal representations, but task recognition is not world understanding by itself.

---

### 5. Egocentric visual experience

#### Ego4D

**Primary source:** https://ego4d-data.org/docs/

Ego4D documents roughly 3,600+ hours of in-the-wild egocentric video from many everyday settings, together with benchmark tasks and annotations.

Especially relevant components:

- episodic memory;
- long-term object tracking / EgoTracks;
- forecasting;
- hand-object interactions;
- object state changes.

**Role for Clover:** real visual-history research: persistence, long-term memory, anticipation and human-object interaction.

**Caution:** some Ego4D modalities include audio, gaze, stereo or 3D data. A strict Clover visual protocol must explicitly select permitted inputs.

---

### 6. Robot interaction data

#### DROID

**Primary source:** https://droid-dataset.github.io/

DROID reports 76K demonstration trajectories / 350 hours of interaction across 564 scenes and 86 tasks.

**Role for Clover:** study what action-conditioned interaction adds beyond passive video; not an immediate benchmark target.

#### Open X-Embodiment

**Primary sources:**

- https://github.com/google-deepmind/open_x_embodiment
- https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/

Google DeepMind reports pooled data across 22 robot embodiments, more than 500 skills, about 150,000 tasks and more than one million episodes.

**Role:** cross-embodiment generalization and the question of whether diversity forces more abstract physical representations.

---

### 7. Lifelong and long-horizon robot learning

#### LIBERO

**Primary source:** https://libero-project.github.io/main.html

Focus: knowledge transfer in lifelong robot learning.

**Role:** future measurement of whether world knowledge transfers rather than catastrophically interfering across tasks.

#### CALVIN

**Primary source:** https://github.com/mees/calvin

Open benchmark for language-conditioned long-horizon manipulation and multi-step task sequences.

**Role:** future downstream test of persistent world-state usefulness. Because CALVIN is language-conditioned, it cannot by itself isolate vision-only understanding.

#### RoboCasa365

**Primary source:** https://robocasa.ai/

The 2026 release reports 365 tasks, 2,500+ kitchen scenes and 2,200+ hours of robot demonstrations, with composite/long-horizon settings and an open leaderboard.

**Role:** future generalist-robot evaluation, especially unseen compositional tasks.

---

### 8. What is still missing

No single benchmark above measures the full Clover goal:

```text
persistent visual world formation
+ open-world observability
+ physical prediction
+ causal revision
+ active perception
+ long-horizon memory
+ decision usefulness
+ real robot generalization
```

The eventual evaluation therefore needs a **battery**, not a single score.

### 9. Current policy

During the present research-mapping phase:

- catalog benchmarks;
- understand protocol and failure modes;
- do not optimize Clover around them;
- do not infer world understanding from benchmark success alone;
- defer large-scale reproduction/comparison until a new representation hypothesis is ready.

---

<a id="topic-research-survey-benchmarks_tasks"></a>

## Benchmarks and Tasks

Source record updated: 2026-10-15

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

### 1. Evaluation hierarchy

#### Level 1 — Cognitive / world-understanding diagnostics

Does the representation contain the structure needed to answer controlled questions about existence, identity, permanence, space, time, observability, physics, causality and counterfactuals?

#### Level 2 — Persistent world-model capability

Can the model maintain, predict, reconstruct, revise or retrieve world state across time?

#### Level 3 — Active evidence acquisition

Can the system recognize that current evidence is insufficient and deliberately obtain a better view or discriminating interaction?

#### Level 4 — Embodied brain capability

Can a robot use its world understanding to complete unfamiliar physical tasks over long horizons, recover when the world changes and avoid unjustified action?

#### Level 5 — Deployment / evidence robustness

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

### 2. Vision and learning-evidence protocol

#### Observation protocol

- **V0:** monocular RGB + temporal order/timestamp; no depth/LiDAR/tactile/force/IMU/GT pose/GT identity.
- **V1:** V0 + camera intrinsics.
- **V2:** calibrated multi-camera RGB.
- **V3:** embodied active vision; action changes future visual evidence.

#### Learning-evidence provenance

- `L0` visual self-supervision only;
- `L1` visual labels/annotations;
- `L2` language/world knowledge;
- `L3` action-conditioned demonstrations/experience;
- `L4` non-visual or privileged physical evidence.

Do not compare protocols as if they have the same information budget.

---

### 3. U1 — intuitive physics: IntPhys 2

- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Use for controlled permanence, immutability, continuity and solidity diagnostics.

---

### 4. U2 — anti-shortcut physical reasoning: MVP / Minimal Video Pairs

- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Use minimal-change paired videos to test whether physical-understanding gains survive counterexamples.

---

### 5. U3 — causal/counterfactual video reasoning: CausalVQA

- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Use language-only/question-only controls because language priors are a confound.

---

### 6. U4 — general visual/video diagnostics: Perception Test

- Code/data: https://github.com/google-deepmind/perception_test

Prefer visual subsets for tracking, memory, physics, temporal relations and grounded evidence.

---

### 7. U5 — persistent world memory: PersistBench

- Paper: https://arxiv.org/abs/2609.20819
- Project/code: https://guangzhaohe.com/persistbench

Use for object permanence, motion continuity and appearance preservation after objects leave the field of view.

---

### 8. U6 — streaming episodic memory: S-EMBER

- Official: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper: https://arxiv.org/abs/2607.02689

Use for grounded streaming recall and temporal evidence localization.

---

### 9. U7 — relational / calibration-independent physics: Principia

- Paper: https://arxiv.org/abs/2609.04200

Use for relational physical-law consistency beyond video appearance quality.

---

### 10. U8 — 3D/state/action-grounded world-model evaluation: RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

Keep distinct:

```text
plausible video
≠ correct 3D/state
≠ correct executable consequence
```

---

### 11. U9 — custom object permanence / occlusion battery

Test visible→occluded→visible, leave/re-enter FOV, similar-object swaps, camera motion, hidden external movement/removal.

Measure identity continuity, false persistence/absence, uncertainty, correction latency and memory cost.

---

### 12. U10 — unknown vs unobserved

Require the system not to treat missing evidence as absence.

Measure unjustified assertion, refusal/coverage, calibration and downstream action consequences.

---

### 13. U11 — world change and belief revision

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

### 14. U12 — intervention twins

Use same/near-same visual prefixes with controlled different interventions and different valid consequences.

Measure consequence accuracy, affected-variable localization, false causal attribution and counterfactual consistency.

---

### 15. U13 — active perception

Relevant sources:

- Bajcsy Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage

Measure correctness, views/actions requested, information gain, avoidable motion, latency and unnecessary evidence collection.

---

### 16. U14 — novel object dynamics

Use objects/types absent from training labels where possible. Measure dynamic prediction, adaptation, transfer and language-prior sensitivity.

---

### 17. U15 — long-horizon household task

Use multi-step find→inspect→retrieve→transport→place tasks with hidden change/recovery. Record per-step world state, decision premise, action, execution effect, memory, recovery and latency.

Relevant suites:

- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/
- ManiSkill — https://github.com/haosulab/ManiSkill

---

### 18. U16 — real-execution world-model fidelity: WorldOracle

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

### 19. U17 — hardware/setup robustness: LIBERO-RIG

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

### 20. U18 — long-horizon scaling: LADDER

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

### 21. U19 — rollout-free offline policy evaluation: RoboFQE

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

### 22. U20 — partial-observability memory representation: Grid or Nodes?

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

### 23. Supporting validation resources — not standalone “understanding” benchmarks

#### RoboSimStudio

- Paper — https://arxiv.org/abs/2610.18835
- Project — https://robosimstudio.github.io

Use for explicit Real2Sim experiments where solver/contact model/physical parameters are editable and simulator hypotheses can be compared against observed behavior.

#### RoboWM-Bench

- Paper — https://arxiv.org/abs/2604.19092

Use for visual-plausibility vs executable-behavior distinction.

#### RoboTrustBench

- Paper — https://arxiv.org/abs/2606.01600

Use for constraint-sensitive, counterfactual and adversarial world-model evaluation.

#### Video2World

- Paper — https://arxiv.org/abs/2610.04432

Use for geometric/dynamic/functional correctness of reconstructed simulation worlds.

---

### 24. Required reporting dimensions

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

### 25. Anti-shortcut / robustness audit

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

### 26. First Understanding Battery candidate — expanded

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

### Evaluation principle

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
