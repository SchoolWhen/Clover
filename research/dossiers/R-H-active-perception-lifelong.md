# R-H — Active Perception and Lifelong World Formation

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

> **Can a machine represent what it does not know well enough to act in order to acquire better visual evidence, then accumulate and revise world knowledge over long periods without catastrophic forgetting?**

This domain connects perception, uncertainty, action and continual learning.

A useful loop is:

```text
ambiguity / missing evidence
→ candidate sensing action
→ expected information gain
→ move / look / inspect
→ new visual evidence
→ world-state update
→ future memory / learning
```

## 2. Canonical active perception

### Active Perception

- Ruzena Bajcsy, 1988: https://ieeexplore.ieee.org/abstract/document/5968

The core idea is that perception is not passive reception of fixed observations; sensing actions can be selected to reduce uncertainty or expose task-relevant information.

**Clover implication:** V3 embodied vision should not be treated as V0 plus a robot body. Action changes the future evidence distribution.

## 3. Modern view-seeking spatial reasoning

### Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Vantage identifies missing question-relevant spatial evidence, selects a new view, and then uses geometry-grounded evidence to improve reasoning.

**Demonstrates:** reasoning failure can be caused by missing observation, and targeted view acquisition can improve spatial understanding without simply scaling model parameters.

**Clover question:** can the world state itself expose what evidence is missing and choose a visual action accordingly?

## 4. Active perception can be learned from human behavior

### Vision in Action

- Paper: https://arxiv.org/abs/2506.15666

Vision in Action learns search, tracking and focusing behavior from human demonstrations for bimanual manipulation with a controllable camera/head.

**Demonstrates:** active visual strategies can be learned jointly with manipulation rather than hand-coded.

**Open question:** do these camera actions optimize information gain, imitate human behavior, or both?

### SaPaVe

- Paper: https://arxiv.org/abs/2603.12193

SaPaVe studies active perception and manipulation within a VLA-style framework and separates camera actions from manipulation actions.

**Clover significance:** sensing action and world-changing action may need different semantics even if both are physically executed by the same robot.

## 5. Lifelong visual representation learning

### Lifelong Representations: Continual Self-Supervised Learning for Vision Models

- Survey: https://arxiv.org/abs/2607.09785

This survey organizes continual self-supervised vision around replay, distillation, regularization, architecture, model merging and objective-level adaptation.

**Clover relevance:** a general robot brain will receive an effectively unbounded unlabeled visual stream; offline pretraining plus frozen deployment is not the complete long-term setting.

## 6. Robot experience can become a continuing data engine

### Skild S1

- Official report: https://www.skild.ai/blogs/s1
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Skild describes in-context task learning from video demonstration and explicitly frames rapid deployment as a way to bootstrap new real-world robot interaction data back into the training pipeline.

### Physical Self-Play

- Official report: https://skild.ai/blogs/physical-self-play
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Skild reports post-training a base robot model through simulated self-play for soccer before transfer to a humanoid robot.

**Research significance:** a mature physical learner may combine passive human experience, demonstrations, robot interaction, simulation and self-generated curricula.

**Caution:** these are company-reported results and do not establish a universal lifelong-learning recipe.

## 7. Generative replay is an emerging continual-learning route

### REGEN / World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays

- Paper: https://arxiv.org/abs/2606.27374

REGEN uses a world-action model to synthesize pseudo-replay trajectories for past tasks during continual adaptation.

**Demonstrates:** generative world/action models may reduce forgetting without retaining all original demonstrations.

**Reported bottlenecks:** long-horizon visual degradation and action-observation inconsistency.

**Clover implication:** generated replay must remain epistemically distinct from observed evidence; synthetic memory is not automatically truth.

## 8. Active perception and memory are coupled

A system can only choose an information-gathering action if it represents some form of unresolved uncertainty.

Conversely, newly acquired evidence must update persistent state or memory in a way that matters later.

Therefore the loop should be evaluated end-to-end:

```text
unknown / ambiguity
→ sensing action
→ new evidence
→ belief update
→ later query / action improvement
```

A camera movement that merely produces more pixels without reducing task-relevant uncertainty is not useful active perception.

## 9. Lifelong learning must distinguish three forms of change

A deployed system encounters:

```text
world changes        — the environment changed
knowledge changes    — the model learned something new
task changes         — current goals changed
```

Conflating them can produce severe errors. For example, adapting model weights to a temporary world configuration may destroy stable general knowledge.

## 10. Operational research questions

1. Can the system recognize when current visual evidence is insufficient?
2. How should expected information gain be estimated from a learned representation?
3. Are camera/sensing actions distinct from task-manipulation actions in the internal model?
4. When should the robot explore versus act on current belief?
5. What should be learned online in weights, external memory or persistent world state?
6. How should lifelong learning avoid catastrophic forgetting?
7. Can self-generated or synthetic experience be used without contaminating evidence-grounded truth?
8. How should knowledge transfer across embodiments and cameras?
9. Can a robot discover new object dynamics through interaction while preserving old knowledge?

## 11. Baseline families

| Family | Comparator | What it isolates |
|---|---|---|
| Passive perception | fixed camera/history policy | no information-seeking action |
| Geometry-guided view selection | Vantage | targeted spatial evidence acquisition |
| Learned active camera behavior | Vision in Action / SaPaVe | sensing-action policy learned from data |
| In-context adaptation | S1-style evidence | task adaptation without weight update |
| Continual SSL | CSSL baselines | weight-level visual representation adaptation |
| Replay-based continual learning | real replay / generative replay | forgetting mitigation |
| Self-play / autonomous curriculum | reported physical self-play | self-generated learning experience |

## 12. Discriminating experiments

### T-H-01 — Insufficient-view test

Present a task that cannot be solved reliably from the initial view.

Compare:

```text
passive policy
random view action
hand-designed view heuristic
learned active perception
world-state-driven information gain
```

Measure success, number of sensing actions and uncertainty reduction.

### T-H-02 — Active object permanence

After an object leaves view, allow the robot to choose whether and where to look for it.

Measure:

- search efficiency;
- correct uncertainty before search;
- re-identification;
- downstream task success.

### T-H-03 — Continual visual stream

Sequentially expose the model to new environments/dynamics over days or episodes.

Measure:

```text
new capability gained
old capability retained
adaptation speed
memory/storage growth
compute cost
```

### T-H-04 — Synthetic replay contamination

Compare real replay, generated replay and no replay.

Measure not only forgetting but also false world beliefs introduced by synthetic trajectories.

### T-H-05 — World change vs learning

Change an environment state temporarily, then restore it.

Test whether the system updates local world memory without incorrectly rewriting stable general knowledge.

## 13. Kill conditions

An active-perception mechanism should be rejected if it does not outperform passive/random sensing at matched action cost.

A lifelong-learning mechanism should be rejected if capability gains require unacceptable forgetting, latency, storage growth or false synthetic beliefs.

In-context memory, weight updates and persistent world state should remain separate research variables until experiments show which form of adaptation is actually needed.

## 14. Clover landing

Current conclusion:

> **A general visual robot brain likely needs both information-seeking action and long-term adaptation, but the mechanism is open. Active perception must prove that it reduces uncertainty efficiently, and lifelong learning must distinguish observed evidence, current world state and durable model knowledge.**
