# Stage 1 — Open-World Epistemics, Model Mismatch and Epistemic Safety

Last updated: 2026-10-14
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study what happens when the current world model is incomplete, wrong, outdated, unsafe to test, or insufficient to explain another agent.

The central questions are:

```text
What if the correct hypothesis is not yet in the model?
How can a robot detect that its world model has become invalid?
How should the robot distinguish state uncertainty from model-structure uncertainty?
When should it seek more evidence, ask for help, abstain, or stop?
How should the robot represent its own changing embodiment?
How should it reason about hidden goals / beliefs of other agents?
```

---

## 1. A useful uncertainty taxonomy

Stage 1 should keep at least these cases distinct:

### E1 — observation uncertainty

The world state may be known in principle, but the current image is ambiguous, occluded, blurred, reflective, etc.

### E2 — state uncertainty

The observation history does not determine which current hidden state is true.

### E3 — parameter uncertainty

The structure of the model is accepted, but unknown parameters remain, such as friction, mass, actuator gain or transition probabilities.

### E4 — model-structure uncertainty

Several different mechanisms could explain the same evidence.

Example:

```text
drawer is locked
vs
drawer is jammed
vs
drawer has an unknown latch
vs
controller is weak
```

### E5 — hypothesis-set incompleteness / open-world uncertainty

The correct explanation is not represented among the current hypotheses.

### E6 — regime change / model invalidation

The model used to be adequate, but the robot/world/controller has changed.

### E7 — social / intentional uncertainty

Another agent has hidden goals, beliefs, preferences or future actions.

### E8 — epistemic-action safety

The robot knows that additional evidence would help, but acquiring it may be risky, expensive, irreversible or socially inappropriate.

These are different research problems.

---

## 2. Open-world hypothesis generation and verification

### HUME — Hypothesis-driven Model Expansion under Uncertainty

Primary paper: https://arxiv.org/abs/2607.06501
Official project: https://open-world-planning.github.io/
RSS 2026 program: https://roboticsconference.org/2026/program/papers/181/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

HUME treats missing knowledge in open-world robot planning as uncertain hypotheses rather than silently filling gaps with fixed assumptions. Foundation models generate candidate hypotheses over objects, attributes and action effects; automated planning schedules actions that both pursue the task and verify those hypotheses; refuted hypotheses are removed and new hypotheses can be generated.

Stage-1 significance:

```text
uncertainty over known hypotheses
≠
the model is missing a hypothesis entirely.
```

HUME is one of the clearest current robotics examples of **model expansion**, not only state estimation.

Important limitations / provenance:

- hypothesis generation uses foundation-model priors, not vision-only learning;
- verification may use detectors/VLMs and structured symbolic planning;
- its abstract PDDL-style world model is not evidence for a universal machine-native representation;
- generating a plausible hypothesis does not make it physically identified.

Stage-2 questions:

```text
How should candidate hypotheses be generated without treating language prior as ground truth?
What evidence is sufficient to promote, retain, reject or split a hypothesis?
How does a robot represent 'none of the current hypotheses explain this'?
```

### Explicit world model for open-world manipulation

**Building Explicit World Model for Zero-Shot Open-World Object Manipulation**
Primary paper: https://arxiv.org/abs/2603.13825
Evidence: `PRIMARY_PAPER`

This route combines open-set perception, a reconstructed digital twin and simulation-based evaluation of candidate interactions.

Why it matters:

It provides a strong explicit-model/open-set comparator, but its simulator-backed digital twin should not be confused with proof that the true physical world state is identifiable from RGB.

---

## 3. World-model falsification and regime change

A general robot should distinguish:

```text
my current state estimate is uncertain
```

from:

```text
my transition/model assumptions are no longer valid.
```

### Changepoint-Aware World Models (CAWM)

Primary paper: https://arxiv.org/abs/2609.18950
Evidence: `PRIMARY_PAPER`

CAWM monitors internal world-model prediction error, detects abrupt dynamics changes with an online changepoint test and discards stale replay while retaining the learned representation.

Robot-relevant examples include changed gravity and actuator gain.

Stage-1 implication:

```text
prediction error
```

can be evidence for:

```text
ordinary stochasticity
state-estimation error
observation corruption
representation failure
or a changed transition regime.
```

A robust system must not collapse these explanations into one scalar uncertainty score.

### Feedback World Model

**Feedback World Model Enables Precise Guidance of Diffusion Policy**
Primary paper: https://arxiv.org/abs/2605.15705
Evidence: `PRIMARY_PAPER`

The work uses the discrepancy between predicted and actually observed next states during deployment to correct world-model guidance online.

Stage-1 relevance:

Execution itself creates a falsification signal:

```text
predicted consequence
vs
observed consequence.
```

This supports treating action execution as an ongoing model-checking process, not only policy rollout.

### Sirius-Fleet

**Multi-Task Interactive Robot Fleet Learning with Visual World Models**
Primary paper: https://proceedings.mlr.press/v270/liu25g.html
Evidence: `PRIMARY_PAPER`

Sirius-Fleet uses visual world models plus anomaly predictors to monitor deployed robot actions and request human correction when predicted outcomes appear anomalous.

Stage-1 distinction:

```text
world-model prediction
+
anomaly / failure monitor
+
human escalation
```

is a different systems hypothesis from assuming the world model is always trusted.

---

## 4. The robot's own body is part of the uncertain world state

### Full-Body Visual Self-Modeling of Robot Morphologies

Primary paper: https://arxiv.org/abs/2111.06389
Project: https://robot-morphology.cs.columbia.edu/
Evidence: `BACKGROUND_REFERENCE` / `OFFICIAL_PROJECT`

This work learns a query-driven visual self-model of robot morphology and demonstrates damage detection/localization/recovery.

Why it remains relevant:

```text
world model
```

should not silently mean only the external world. A robot also needs a model of what physical body it currently has.

### Diffusion-Based Body Schema Learning Enabling Abnormal-State Adaptation

Primary paper: https://arxiv.org/abs/2608.01029
Evidence: `PRIMARY_PAPER`

The method studies musculoskeletal body schema under abnormal states such as muscle rupture and actuator jamming, using diffusion-based estimation rather than assuming a fixed low-dimensional body state.

Stage-1 implication:

```text
self model at deployment
```

may need to remain revisable under damage or actuator failure.

### The Embodiment Gap in Robot Foundation Models

Primary paper: https://arxiv.org/abs/2608.18433
Evidence: `PRIMARY_PAPER`

This survey separates reusable model/data/representation knowledge from the embodiment-specific work still required to execute on a new robot.

Use it as a warning against reporting cross-embodiment success without recording:

```text
what structure transfers
what action interface changes
what calibration/adaptation is needed
what remains robot-specific.
```

Related Stage-1 sources already tracked:

- LAC-WM — https://arxiv.org/abs/2610.10846
- SyncWorld — https://arxiv.org/abs/2609.09155
- Robot-Factored World Models — https://arxiv.org/abs/2607.22535

---

## 5. Epistemic safety: information is not free

Active perception often drives a robot toward uncertain regions because they offer the most information. The same regions may also be the least safe.

### Splat-CBF

Primary paper: https://arxiv.org/abs/2609.23100
Evidence: `PRIMARY_PAPER`

Splat-CBF combines next-best-view information objectives with collision safety constraints in uncertain 3D Gaussian maps.

Stage-1 research role:

```text
maximize information gain
subject to safety constraints.
```

It provides a concrete counterexample to the naive rule:

```text
choose the action with maximum information gain.
```

### Conflict-Aware Active Perception and Control

Primary paper: https://arxiv.org/abs/2605.20566
Evidence: `PRIMARY_PAPER`

This work also combines risk-aware expected information gain with control-barrier-function safety, making the perception/safety conflict explicit.

### ATOM-CBF

PMLR/L4DC 2026: https://proceedings.mlr.press/v331/yun26a.html
Evidence: `PRIMARY_PAPER`

ATOM-CBF adapts the safety margin of perception-based control under out-of-distribution measurements by explicitly accounting for epistemic uncertainty.

Stage-1 implication:

Uncertainty should sometimes cause:

```text
more conservative action
```

rather than:

```text
more aggressive exploration.
```

### Epistemic-action utility

A future diagnostic should distinguish:

```text
TaskValue(a)
InformationValue(a)
Risk(a)
Cost(a)
Irreversibility(a)
SocialCost(a)
```

without assuming a final Clover objective yet.

---

## 6. Help-seeking, abstention and metareasoning

A general-purpose agent may need to choose not only **which physical action**, but **which cognitive / information action**:

```text
act
look again
move viewpoint
probe
retrieve memory
simulate
ask a human
abstain
stop
```

### KnowNo / Robots That Ask For Help

Primary paper: https://arxiv.org/abs/2307.01928
Project: https://robot-help.github.io/
Evidence: `BACKGROUND_REFERENCE` / `OFFICIAL_PROJECT`

KnowNo calibrates uncertainty in LLM-based robot planners and asks for help when ambiguity is not safely resolvable.

Its language-planning setting is not evidence for vision-only world understanding, but it is a useful reference for **selective escalation** rather than silent guessing.

### HiL-Bench

Primary paper: https://arxiv.org/abs/2604.09408
Evidence: `PRIMARY_PAPER`

HiL-Bench is not a robotics benchmark, but directly measures whether agents detect unresolved blockers and ask for help instead of guessing.

Stage-1 relevance:

The same metareasoning failure can appear in embodied systems:

```text
uncertainty detected
but no escalation
```

or:

```text
escalation triggered too often / too vaguely.
```

### Candidate Stage-1 metareasoning taxonomy

```text
M1 act autonomously
M2 gather more passive visual evidence
M3 move to a better viewpoint
M4 perform a physical probe/intervention
M5 run internal prediction/simulation
M6 retrieve stored evidence/history
M7 ask a human / external source
M8 abstain / enter safe state
```

The research question is not yet which controller implements this. It is what evidence should justify each transition.

---

## 7. Other agents create another partially observed world

The real world includes humans and other autonomous agents whose internal goals are not directly visible.

### Structured LLM Reasoning for Human–Robot Coordination Under Hidden Goals

Primary paper: https://arxiv.org/abs/2608.04309
Evidence: `PRIMARY_PAPER`

The work formulates cooperative interaction with private goal views as a Dec-POMDP and includes action-conditioned Theory-of-Mind inference, hierarchical planning, verification and replanning.

Stage-1 implication:

```text
visible human motion
≠
human goal / belief / intention.
```

The latent state of another agent may require history, communication and behavioral intervention evidence.

### MindPower

Primary paper: https://arxiv.org/abs/2511.23055
Evidence: `PRIMARY_PAPER`

MindPower integrates multimodal perception with Theory-of-Mind reasoning over both self and other-agent mental state for embodied decisions/actions.

Important caveat:

These methods rely strongly on language-model priors and multimodal supervision. They are not evidence that mental states are directly visually identifiable.

### Social-state distinctions

Stage 1 should keep distinct:

```text
body pose / visible action
short-term motion intention
current task goal
belief about world
preference
cooperative / adversarial role
social norm / permission
```

These have different evidence requirements.

---

## 8. Model confidence is not enough

A single uncertainty scalar cannot fully represent:

```text
I cannot see the state
I saw it but the representation forgot it
my parameter estimate is broad
I do not know which mechanism applies
none of my current models explain the observation
my model used to work but the world changed
I know the informative experiment but it is unsafe
another agent has hidden intent
```

Stage 1 should therefore compare methods by **uncertainty type**, not only confidence calibration.

---

## 9. Candidate later diagnostics

### D-OE1 — missing-hypothesis test

Construct situations where all provided candidate models are wrong. Measure whether the agent can represent:

```text
none of the above / model incomplete
```

rather than force probability mass onto a wrong model.

### D-OE2 — hypothesis expansion test

Give partial evidence, then require generation of new candidate explanations followed by verification actions.

### D-OE3 — model invalidation test

Change dynamics after a long stable period. Measure detection latency, false alarms, adaptation cost and whether stale evidence is retained incorrectly.

### D-OE4 — self-model damage test

Alter actuator gain, morphology, payload, camera mounting or joint availability and test whether the internal self model updates.

### D-OE5 — safe-information test

Offer:

```text
high information / high risk
medium information / low risk
low information / no risk
```

and evaluate whether information seeking respects safety.

### D-OE6 — escalation test

Create ambiguous conditions where the optimal behavior is to ask, abstain or seek more evidence rather than guess.

### D-OE7 — hidden-goal test

Two visible behavior histories share similar motion but arise from different hidden goals. Test belief maintenance and evidence-seeking interaction.

---

## 10. Adjacent research gaps still worth collecting

The current scan suggests these should remain visible without creating more top-level files yet:

```text
open-set mechanism discovery
model-class selection / nonparametric world models
persistent hypothesis provenance
scientific falsification / experiment design
human-query cost models
social permission / consent for probing actions
multi-agent belief recursion
safe exploration under irreversible actions
unknown unknown detection
model ensemble collapse / correlated uncertainty
self-model and external-world-model coupling
```

---

## 11. Stage-1 questions

```text
Can a robot recognize that its current hypothesis set is incomplete?
How should new world-model hypotheses be proposed and grounded?
How can state uncertainty be separated from model-structure uncertainty?
How should prediction error be attributed to noise, state error, representation error or regime change?
When should a model be adapted, replaced or rejected?
What parts of the robot's own body/controller must be represented as revisable state?
How should information gain be traded against risk and irreversibility?
When should the agent ask for help or abstain?
How should hidden goals/beliefs of other agents be represented without hallucinating them as observed facts?
```

---

## Current rule

A general world model must be allowed to say:

```text
I do not know the state.
I do not know the parameter.
I do not know which mechanism is correct.
My current model may be wrong.
The world may have changed.
I need more evidence.
The informative experiment is unsafe.
I should ask for help / abstain.
```

None of these statements is a Clover architecture decision. They are Stage-1 requirements for what a credible future theory of real-world understanding may need to account for.
