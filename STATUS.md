# Clover Status

Last updated: 2026-10-14  
Stage-1 freshness checked through: **2026-10-14**

## Research question

> **How can a machine understand the real world through vision alone?**

## Long-term goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

Immediate objective: **coverage before commitment**. No new Clover core representation or algorithm is frozen.

## Read first

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)
9. [`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md)
10. [`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)
11. [`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md)
12. [`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md)
14. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
15. [`research/README.md`](research/README.md)

## Current Stage-1 surfaces

```text
1  broad research inventory
2  world-state variables
3  identifiability / information limits
4  observation physics
5  hidden physical properties / irreversible change
6  minimum sufficient world state
7  state aliasing / representation failure
8  adaptive abstraction / state granularity
9  value of information / probing actions
10 open-world epistemics / model mismatch / epistemic safety
11 model discovery / experiment design / falsification / provenance
12 current frontier
```

## Newly strengthened surface: model discovery

[`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md) now separates:

```text
state estimation
parameter estimation
model selection
mechanism / causal-structure discovery
open-world model expansion
falsification
model replacement / regime-specific reuse
```

Current anchors include:

- HUME — https://arxiv.org/abs/2607.06501 · https://github.com/threefruits/HUME
- Unknown Unknowns / Model Misspecification — https://arxiv.org/abs/2608.13633
- intervention-only causal discovery — https://proceedings.mlr.press/v337/mazaheri26b.html
- Causal Discovery in Action — https://proceedings.mlr.press/v323/panayiotou26a.html
- Bayesian Experimental Design via Score Matching — https://proceedings.mlr.press/v337/phillips26a.html
- robust BOED under model misspecification — https://proceedings.mlr.press/v300/tang26d.html
- constrained Bayesian experimental design — https://proceedings.mlr.press/v306/guo26g.html
- SAGE — https://arxiv.org/abs/2606.31478 · https://github.com/JieMaMagic/SAGE
- Socratic autonomous scientific discovery — https://arxiv.org/abs/2606.26722
- Mental-Models — https://arxiv.org/abs/2610.12453 · https://github.com/hananshafi/Mental-Models
- Recursive ToM — https://arxiv.org/abs/2606.11724

Central distinctions:

```text
confidence inside a model
≠ model-class correctness

active exploration
≠ scientific experiment design

reflection
≠ falsification

one failed prediction
≠ proof that the representation is wrong

current best hypothesis
≠ permanent truth
```

## Current frontier refresh

[`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md) is now a thin current-edge table rather than a second survey.

Important current additions include:

- SpecWM — https://arxiv.org/abs/2610.15429 — representation objective controls which world variables remain recoverable;
- DR-WM — https://arxiv.org/abs/2610.17630 — action-response calibrates hidden physical parameters;
- Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/ — strong multimodal reasoner/tool baseline;
- Mental-Models — https://arxiv.org/abs/2610.12453 — explicit first/second-order partner-state modeling;
- Identifiable World Models — https://arxiv.org/abs/2610.07028 — hybrid distributed + identifiable-state route;
- RobotWorld — https://arxiv.org/abs/2610.10409 — composition/state/recovery failures;
- Video2World — https://arxiv.org/abs/2610.04432 — functional correctness beyond visual similarity;
- Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html — active probing ↔ task-sufficient state discovery;
- HUME — https://arxiv.org/abs/2607.06501 — open-world hypothesis expansion and verification;
- robust experimental design under misspecification — https://proceedings.mlr.press/v300/tang26d.html.

These are research materials and comparators, not Clover components.

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- choosing explicit vs latent vs hybrid state;
- treating compact state as automatically superior;
- treating hierarchy as automatically superior;
- treating information gain as the final control objective;
- treating a world-model prediction as ground truth;
- assuming the correct hypothesis/model class is always known;
- treating language-generated hypotheses as physical truth;
- assuming the robot body/controller/camera is permanently fixed;
- treating one benchmark as the definition of understanding;
- optimizing hardware before the scientific mechanism.

## Remaining collection gaps

Stage 1 still needs stronger primary embodied evidence for:

```text
unknown-unknown diagnostics in real environments
nonparametric / open-set mechanism discovery
persistent hypothesis provenance and refutation-memory benchmarks
slow drift versus abrupt changepoint detection
representation reversibility after compression
self-model ↔ external-world-model coupling
safe exploration under irreversible actions
human-query / escalation cost models
social permission / consent for probing actions
multi-agent recursive belief from embodied observations
correlated uncertainty / model-ensemble collapse
```

## Stage-1 exit condition

Stage 2 Analysis becomes primary only when a new agent can identify:

1. major competing directions and strongest representatives;
2. source/evidence provenance;
3. observation assumptions;
4. world variables represented;
5. identifiability assumptions;
6. sufficiency target;
7. likely state-aliasing failure;
8. abstraction/granularity/timescale assumptions;
9. information-gathering strategy and cost;
10. open-world epistemic failure mode (`E1–E8`) where relevant;
11. hypothesis/model class and falsification assumptions where relevant;
12. datasets/benchmarks that discriminate claims;
13. methods deserving one-method-one-report Analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, a final representation, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, a validated original algorithm, or a final hardware mapping.

These remain research targets.