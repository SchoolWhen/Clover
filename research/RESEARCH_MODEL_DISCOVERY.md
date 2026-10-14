# Stage 1 — Model Discovery, Falsification and Scientific Reasoning

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a harder setting than ordinary state estimation:

> What should an embodied learner do when the currently available world-model class is incomplete, several mechanisms remain compatible with the evidence, or the next useful action should be chosen as an experiment rather than only as task execution?

The central loop is:

```text
observation / failure
→ candidate explanations
→ choose discriminating evidence / intervention
→ observe consequence
→ update confidence
→ reject / retain / refine / expand model
→ preserve provenance
→ repeat
```

This loop is a research object, not a proposed Clover control loop.

---

## 1. Model discovery is not the same as parameter estimation

Keep distinct:

```text
state estimation
— which current state is true?

parameter estimation
— which values inside a known model are true?

model selection
— which member of a known family is best?

structure / mechanism discovery
— what dependency or causal structure applies?

open-world model expansion
— is the correct mechanism missing from the current hypothesis set?
```

A robot that only estimates parameters inside a fixed simulator is not automatically discovering world structure.

---

## 2. Unknown unknowns and model misspecification

### Unknown Unknowns: Model Misspecification in Machine Learning for Physics

Primary paper: https://arxiv.org/abs/2608.13633  
Evidence: `PRIMARY_PAPER`

This 2026 physics perspective treats unknown unknowns as failures of the assumed model class rather than merely wide posterior uncertainty. It emphasizes that no single diagnostic can certify that a model is correctly specified; robustness requires complementary diagnostics, model revision and repeated checking.

Stage-1 implication:

```text
calibrated uncertainty inside a wrong model class
≠
robustness to model misspecification.
```

For Clover, this is useful background for asking whether a robot can detect evidence that none of its current mechanisms explains.

---

## 3. Open-world hypothesis generation and model expansion

### HUME — Hypothesis-driven Model Expansion under Uncertainty

Primary paper: https://arxiv.org/abs/2607.06501  
Official project: https://open-world-planning.github.io/  
Open code: https://github.com/threefruits/HUME  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`

HUME represents knowledge gaps as hypotheses, incorporates them into an explicit planning model, uses execution to verify them, rejects contradicted hypotheses and can generate replacements.

Research role:

```text
closed hypothesis set
vs
hypothesis-set expansion.
```

Important limitation:

The hypothesis generator is strongly language/foundation-model dependent and the representation is symbolic/PDDL-style. The result is therefore evidence that **model expansion is operationally useful**, not evidence that its symbolic ontology is the right machine-native world representation.

Stage-2 questions:

```text
How should a visual embodied system generate novel mechanism hypotheses without treating language priors as truth?
What evidence should promote, split or retire a hypothesis?
How should multiple incompatible but still viable explanations coexist?
```

---

## 4. Causal/mechanism discovery from interventions

### Relaxing Faithfulness with Intervention-Only Causal Discovery

PMLR/UAI 2026: https://proceedings.mlr.press/v337/mazaheri26b.html  
Evidence: `PRIMARY_PAPER`

The work shows that hard interventions can identify causal structure under assumptions that allow cancellation patterns violating ordinary observational faithfulness. It also characterizes equivalence classes when intervention scope is insufficient.

Stage-1 lesson:

```text
observational dependence structure
≠
full causal mechanism.
```

Intervention can be the primary carrier of structure information.

### Causal Discovery in Action

PMLR/CLeaR 2026: https://proceedings.mlr.press/v323/panayiotou26a.html  
Evidence: `PRIMARY_PAPER`

For chain-reaction systems, blocking interventions uniquely identify causal structure under specific structural assumptions and can outperform observational heuristics.

Stage-1 lesson:

Mechanism discovery can become tractable when the class of possible physical mechanisms has structure, but the guarantee depends on those assumptions.

### Towards Completeness in Causal Discovery from Soft Interventions with Known Targets

PMLR/ICML 2026: https://proceedings.mlr.press/v306/zhou26s.html  
Evidence: `PRIMARY_PAPER`

Studies what can be oriented/identified from soft interventions with latent confounding and known intervention targets.

### SCOUT

PMLR/ICML 2026: https://proceedings.mlr.press/v306/turkoglu26a.html  
Evidence: `PRIMARY_PAPER`

Studies nonlinear cyclic causal discovery from soft interventional data when intervention targets are unknown.

### MetaCaDI

PMLR/UAI 2026: https://proceedings.mlr.press/v337/ong26a.html  
Evidence: `PRIMARY_PAPER`

Meta-learns shared causal structure across environments and identifies unknown intervention targets with few-shot adaptation.

### Test-Time Interventional Causal Learning (TICL)

PMLR/ICML 2026: https://proceedings.mlr.press/v306/chen26t.html  
Evidence: `PRIMARY_PAPER`

Learns causal structure at test time from interventional data, including settings where intervention targets are not supplied directly.

### Stage-1 interpretation

These papers should not be imported as robot architectures. Their value is theoretical:

```text
mechanism structure may be unidentifiable observationally
interventions can reduce equivalence classes
unknown intervention targets are themselves latent variables
cyclic / confounded / heterogeneous mechanisms require different assumptions
```

A future embodied theory must state which assumptions make its causal claims identifiable.

---

## 5. Scientific experiment design: choose actions to discriminate hypotheses

A robot performing epistemic actions is solving an experimental-design problem.

### Bayesian Experimental Design via Score Matching

PMLR/UAI 2026: https://proceedings.mlr.press/v337/phillips26a.html  
Evidence: `PRIMARY_PAPER`

Develops policy-based Bayesian experimental design around expected information gain while reducing the computational burden of repeated policy optimization.

### Constrained Bayesian Experimental Design via Online Planning

PMLR/ICML 2026: https://proceedings.mlr.press/v306/guo26g.html  
Evidence: `PRIMARY_PAPER`

Explicitly handles dynamic constraints, varying costs and physically restricted design sequences in sequential experimental design.

### Robust Bayesian Active Learning under Model Misspecification

PMLR/AISTATS 2026: https://proceedings.mlr.press/v300/tang26d.html  
Evidence: `PRIMARY_PAPER`

Shows that selecting only maximally informative samples can amplify model error under misspecification. Its acquisition objective combines informativeness, representativeness and error de-amplification.

### On the Misinformation in a Statistical Experiment

PMLR/AISTATS 2026: https://proceedings.mlr.press/v300/callahan26a.html  
Evidence: `PRIMARY_PAPER`

Shows that under model/inference misspecification, an experiment ranked as more informative can make inference more confidently wrong.

### Amortized Safe Active Learning for Real-Time Data Acquisition

PMLR/AISTATS 2026: https://proceedings.mlr.press/v300/li26b.html  
Evidence: `PRIMARY_PAPER`

Studies information acquisition under explicit safety constraints and fast deployment-time query selection.

### Stage-1 implication

The naive rule:

```text
choose argmax expected information gain
```

is not generally enough.

A future embodied scientific policy may need to reason about:

```text
informativeness
representativeness
model misspecification
safety
cost
irreversibility
social permission
future task value
```

This remains a research question, not a Clover objective.

---

## 6. Hypothesis provenance and refutation memory

A scientific world learner should not only store its current best hypothesis. It may need to preserve:

```text
hypothesis identity
source / prior
supporting observations
contradicting observations
interventions performed
predictions made before observing outcomes
failure attribution
reason for rejection
conditions under which the hypothesis may become relevant again
```

### SAGE — Multi-Hypothesis Failure Attribution

Primary paper: https://arxiv.org/abs/2606.31478  
Open code: https://github.com/JieMaMagic/SAGE  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

SAGE is an autonomous-research system rather than a robot world model. It keeps multiple explanations for failed experiments, evaluates evidence for each, then routes the verified cause to hypothesis, experimental-design or implementation changes.

Why it matters to Stage 1:

```text
one failure
→ one verbal reflection
```

is a poor analogue for scientific model revision.

The useful transferable idea is **multiple working hypotheses + evidence-grounded failure attribution + measured-result grounding**, not the software architecture itself.

### Socratic agents for autonomous scientific discovery

Primary paper: https://arxiv.org/abs/2606.26722  
Evidence: `PRIMARY_PAPER`

AHOIS uses a critic to challenge hypotheses, formulate falsification criteria, generate counterexamples and run closed-loop experiments on a physical optical system.

Research role:

It offers an existence proof that hypothesis generation, criticism, experiment choice and revision can be integrated around a real physical apparatus. It does not establish that the same approach transfers to open-world robotic vision.

### Stage-1 gap

Robotics/world-model literature still lacks a widely accepted benchmark for **hypothesis provenance and refutation memory**.

A future diagnostic should ask whether an agent remembers not only what it believes, but:

```text
why it believes it
what evidence would falsify it
which rejected explanations should not be silently resurrected
```

---

## 7. Representation design is itself an experimental hypothesis

Two current results sharpen the question of what latent state should preserve.

### Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling

PMLR/ICML 2026: https://proceedings.mlr.press/v306/feng26aa.html  
Evidence: `PRIMARY_PAPER`

This work combines active probing with structured world-model learning to recover compact task-sufficient factors for control.

It directly links:

```text
what the agent probes
↔
which latent factors become recoverable
↔
which factors the state keeps.
```

Important limitation:

Task sufficiency is not open-world sufficiency. A compact representation can legitimately discard variables irrelevant to the evaluated tasks.

### SpecWM — World Modeling through Spectral Alignment

Primary paper: https://arxiv.org/abs/2610.15429  
Submitted: 2026-10-11  
Evidence: `PRIMARY_PAPER`

SpecWM explicitly controls representation geometry through target similarity kernels. Different kernels change which physical quantities are linearly recoverable and which nuisance factors are suppressed; temporal spectral alignment improves model-based planning in reported OGBench/CALVIN experiments.

Stage-1 significance:

```text
representation objective
→ information preserved
→ information discarded
→ downstream planning behavior.
```

This is an important current counterpoint to the idea that a generic pretrained latent automatically preserves the right world variables.

---

## 8. Model discovery under non-stationarity

Model discovery is not only needed once. The mechanism class may change over time.

Relevant Stage-1 sources already tracked:

- Changepoint-Aware World Models — https://arxiv.org/abs/2609.18950
- ReDRAW — https://proceedings.mlr.press/v331/lanier26a.html
- ROAM — https://proceedings.mlr.press/v330/chen26a.html
- WorMI — https://proceedings.mlr.press/v267/yoo25a.html

Additional theory/background:

- multiple-change-point learning — https://proceedings.mlr.press/v306/gafni26a.html
- distribution-valued online change-point detection — https://proceedings.mlr.press/v306/zeng26f.html

Stage-1 distinction:

```text
abrupt changepoint
≠
slow drift
≠
new latent regime
≠
previously unseen mechanism class.
```

A future system should not assume one detector handles all four.

---

## 9. Other-agent model discovery and recursive beliefs

The world may contain agents whose hidden state includes beliefs about **our** beliefs.

### Mental-Models for Multi-Agent Systems

Primary paper: https://arxiv.org/abs/2610.12453  
Open code: https://github.com/hananshafi/Mental-Models  
Submitted: 2026-10-08  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

The work learns reusable latent partner-state representations with first- and second-order mental-state structure for multi-agent decision making.

### RecToM — Recursive Theory of Mind

Primary paper: https://arxiv.org/abs/2606.11724  
Evidence: `PRIMARY_PAPER`

RecToM explicitly constructs nested perspectives for higher-order belief reasoning.

These are not proofs that mental state is visually identifiable. They establish useful computational distinctions:

```text
world state
other agent's belief about world
my belief about their belief
my belief about their belief about my belief
```

For robotics, recursive depth should be treated as a cost/necessity question rather than assumed infinite.

---

## 10. Social permission is part of epistemic-action validity

A physical probe can be safe in the collision sense and still be unacceptable.

Examples:

```text
open a person's drawer to inspect contents
move a personal object to test weight
enter a private room for a better viewpoint
interrupt a human to ask a clarifying question
touch another person's body/object to identify material
```

Relevant background:

- Socially intelligent task and motion planning for HRI — https://arxiv.org/abs/2001.08398
- Formalizing and Guaranteeing Human-Robot Interaction — https://arxiv.org/abs/2006.16732
- Enabling Basic Normative HRI in a Cognitive Robotic Architecture — https://arxiv.org/abs/1602.03814

These are background references, not 2026 vision-world-model results.

Stage-1 implication:

```text
physically safe probe
≠
socially permitted probe.
```

Future epistemic-action evaluation should eventually include ownership, privacy, consent, interruption cost and normative constraints when humans are present.

---

## 11. A working scientific-reasoning state schema

This is bookkeeping for Stage 1, not a proposed machine representation.

For every active hypothesis, a later Analysis report may record:

```text
HYPOTHESIS
- statement
- scope / domain
- provenance
- assumptions
- current support
- counterevidence
- predicted observations
- discriminating experiments
- safety / cost constraints
- status: active / weak / rejected / superseded / regime-specific
```

And every experiment/intervention may record:

```text
EXPERIMENT
- target uncertainty
- hypotheses discriminated
- expected outcomes
- actual outcome
- observation protocol
- side effects / disturbance
- cost / risk / permission
- posterior/model update
```

This prevents research agents from reducing model discovery to a list of current beliefs with no audit trail.

---

## 12. Candidate later diagnostics

### D-MD1 — none-of-the-above mechanism test

All supplied mechanisms are wrong. Measure whether the agent forces a choice or proposes an expanded hypothesis set.

### D-MD2 — discriminating-experiment test

Give two observationally compatible mechanisms and several possible probes. Measure whether the selected probe separates them efficiently.

### D-MD3 — misleading-information test

Construct a misspecified model where the highest nominal information-gain experiment amplifies bias. Test whether robust experiment selection avoids it.

### D-MD4 — refutation-memory test

After a hypothesis is falsified, later provide superficially similar evidence. Measure whether the agent remembers why it was rejected instead of resurrecting it without new support.

### D-MD5 — regime-specific resurrection test

A previously rejected mechanism becomes valid after a real regime change. Test whether the system can distinguish justified reactivation from forgetting the previous falsification.

### D-MD6 — recursive-belief depth test

Vary the order of belief recursion required for correct coordination; measure benefit versus compute/state cost.

### D-MD7 — permission-aware experiment test

Offer an informative but socially impermissible probe and a weaker permitted alternative. Measure whether the system distinguishes information value from action legitimacy.

---

## 13. Stage-1 questions

```text
Can a robot detect that its model class is misspecified?
Can it generate genuinely new candidate mechanisms rather than only tune parameters?
Which interventions make competing mechanisms identifiable?
How should experiments be selected when information gain itself is unreliable under misspecification?
How should hypothesis provenance, counterevidence and rejection history be stored?
When should a falsified hypothesis remain dead, and when can regime change justify revisiting it?
How does the representation objective determine which physical factors remain recoverable?
How deep does recursive other-agent belief modeling need to be for embodied coordination?
How should privacy, ownership, consent and social norms constrain epistemic actions?
```

---

## Current rule

Do not equate:

```text
high confidence
with correct model class,

active exploration
with scientific experiment design,

one successful intervention
with causal identification,

reflection
with falsification,

current best hypothesis
with permanent truth.
```

Stage 1 should preserve the possibility that the machine's current explanation of the world is structurally wrong.