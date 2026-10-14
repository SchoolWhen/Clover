# Evaluation & Benchmark Map

Last updated: 2026-10-14

Benchmarks are measurement instruments. This map records what each instrument is capable of measuring, what it cannot establish, and how it may eventually contribute to a broader Clover evaluation.

## 1. Intuitive physics

### IntPhys 2

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

## 2. Shortcut resistance

### Minimal Video Pairs (MVPBench)

**Primary source:** https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

**Scale reported by authors:** 55K multiple-choice video QA examples.

**Core design:** each example has a visually similar minimal-change pair with the same question and opposing answer; credit requires the pair to be answered consistently.

**Strength:** explicitly attacks superficial visual/textual shortcuts.

**Role for Clover:** not only a benchmark; its minimal-pair philosophy should influence our own scientific tests.

---

## 3. Causal and counterfactual video reasoning

### CausalVQA

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

## 4. General video perception and reasoning

### Perception Test

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

### Something-Something V2

**Role:** motion/action representation diagnostic. Useful for measuring temporal representations, but task recognition is not world understanding by itself.

---

## 5. Egocentric visual experience

### Ego4D

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

## 6. Robot interaction data

### DROID

**Primary source:** https://droid-dataset.github.io/

DROID reports 76K demonstration trajectories / 350 hours of interaction across 564 scenes and 86 tasks.

**Role for Clover:** study what action-conditioned interaction adds beyond passive video; not an immediate benchmark target.

### Open X-Embodiment

**Primary sources:**

- https://github.com/google-deepmind/open_x_embodiment
- https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/

Google DeepMind reports pooled data across 22 robot embodiments, more than 500 skills, about 150,000 tasks and more than one million episodes.

**Role:** cross-embodiment generalization and the question of whether diversity forces more abstract physical representations.

---

## 7. Lifelong and long-horizon robot learning

### LIBERO

**Primary source:** https://libero-project.github.io/main.html

Focus: knowledge transfer in lifelong robot learning.

**Role:** future measurement of whether world knowledge transfers rather than catastrophically interfering across tasks.

### CALVIN

**Primary source:** https://github.com/mees/calvin

Open benchmark for language-conditioned long-horizon manipulation and multi-step task sequences.

**Role:** future downstream test of persistent world-state usefulness. Because CALVIN is language-conditioned, it cannot by itself isolate vision-only understanding.

### RoboCasa365

**Primary source:** https://robocasa.ai/

The 2026 release reports 365 tasks, 2,500+ kitchen scenes and 2,200+ hours of robot demonstrations, with composite/long-horizon settings and an open leaderboard.

**Role:** future generalist-robot evaluation, especially unseen compositional tasks.

---

## 8. What is still missing

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

## 9. Current policy

During the present research-mapping phase:

- catalog benchmarks;
- understand protocol and failure modes;
- do not optimize Clover around them;
- do not infer world understanding from benchmark success alone;
- defer large-scale reproduction/comparison until a new representation hypothesis is ready.
