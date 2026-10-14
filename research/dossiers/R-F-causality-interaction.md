# R-F — Causality, Counterfactuals and Interaction

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

> **Can passive visual observation identify the causal structure needed for robust prediction and action, or does a machine need interventions and interaction to learn what changes what?**

Correlation, prediction and causality are not equivalent:

```text
correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Clover must not call a visual feature “causal” merely because it predicts well in-distribution.

## 2. Causal representation learning is underconstrained

### Interventional Causal Representation Learning

- ICML 2023: https://proceedings.mlr.press/v202/ahuja23a.html

This work shows that interventional data can provide identification guarantees for latent causal factors under stated assumptions.

**Clover relevance:** interaction can carry qualitatively different information from passive observation because it changes the data-generating process.

### General Identifiability and Achievability for Causal Representation Learning

- AISTATS 2024: https://proceedings.mlr.press/v238/varici24a.html

The paper establishes identifiability/achievability results using interventions under a broad nonlinear setting.

**Research consequence:** if Clover wants latent variables to correspond to causal state, it must state what assumptions or interventions make those variables identifiable.

### Partially Observable Causal Representation Learning

- ICML 2024: https://proceedings.mlr.press/v235/xu24ac.html

The work explicitly handles causal representation learning when observations reveal only subsets of the latent state.

**Clover significance:** visual causality is doubly difficult because the causal state itself may be partially hidden by viewpoint and occlusion.

## 3. Real-video causal reasoning remains difficult

### CausalVQA

- Paper: https://arxiv.org/abs/2506.09943
- Official Meta page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- Code/data: https://github.com/facebookresearch/CausalVQA

CausalVQA covers:

```text
counterfactual
hypothetical
anticipation
planning
descriptive
```

in real-world video scenarios.

**Demonstrates:** current frontier multimodal models still trail human performance substantially, especially on anticipation and hypothetical questions.

**Limit:** natural-language multiple-choice causal reasoning can still mix visual evidence with language/world priors and does not itself prove a learned causal state representation.

## 4. Intervention twins should be a core Clover diagnostic

A strong causal diagnostic should construct:

```text
same or near-same visual prefix
+ different controlled intervention
→ different valid consequence
```

The model should not only choose the correct outcome; it should be sensitive to the variable or relation actually changed by the intervention.

Suggested measurements:

- consequence accuracy;
- affected-state identification;
- false causal attribution;
- confidence/refusal when intervention effect is not visually identifiable;
- recovery when prediction fails.

## 5. Passive video and interaction provide different evidence

Passive internet video offers:

```text
broad diversity
natural dynamics
many object interactions
large scale
```

but usually lacks controlled interventions and action labels.

Interaction adds:

```text
controllability
cause/effect asymmetry
action-conditioned transition evidence
affordance evidence
active information gathering
```

V-JEPA 2 provides a concrete passive→action-conditioned research path:

- Paper: https://arxiv.org/abs/2506.09985

Large action-free video pretraining is followed by much smaller action-conditioned robot training for planning.

**Question:** what causal/action information appears only after action-conditioned data is introduced?

## 6. Counterfactual reasoning must be grounded in state

A model may produce a linguistically plausible answer to:

> “What would happen if X?”

without representing the changed physical state correctly.

Therefore a stronger counterfactual test should require:

```text
intervention specification
→ changed state / relation
→ predicted consequence
→ downstream action choice
```

and score each stage separately where possible.

## 7. Causal surprise and belief revision

Historical Clover's Counter-Witness-First idea remains a hypothesis:

```text
expected world
→ observation disagrees
→ locate broken dependency
→ causal candidate
→ test by future prediction / intervention
```

This is interesting because it connects causality to state revision, but it is not established by the causal-learning literature.

It should only survive if it improves intervention-sensitive prediction or diagnosis beyond standard predictive-error baselines.

## 8. Operational research questions

1. What causal structure is identifiable from passive V0/V1 video alone?
2. Which causal variables require intervention or action-conditioned data?
3. Can a predictive latent support correct counterfactuals without explicit causal factors?
4. Does an explicit causal graph improve novel-intervention generalization?
5. How should hidden/confounded causes be represented under visual partial observability?
6. Can the system distinguish “correlated visual cue” from “intervention-sensitive cause”?
7. Does causal representation improve recovery when the world behaves unexpectedly?

## 9. Baseline families

| Family | Comparator | What it tests |
|---|---|---|
| Passive predictive representation | V-JEPA 2/2.1 | predictive dependence from observation |
| VLM reasoning | CausalVQA-capable VLM | language-mediated counterfactual reasoning |
| Action-conditioned world model | WAM / robot predictive model | intervention/action-conditioned transitions |
| Causal representation learner | CRL baselines under intervention | identifiable latent causal factors |
| Explicit causal candidate | Clover historical mechanisms | whether explicit dependency adds independent value |

## 10. Discriminating experiments

### T-F-01 — Intervention twins

Hold scene, camera and history constant as much as possible; alter one controlled physical intervention.

Measure consequence sensitivity and false causal edges.

### T-F-02 — Observational shortcut test

Train/evaluate on correlated cues, then intervene on the cue while holding the true mechanism constant.

A causal model should retain the correct prediction when the spurious correlate is changed.

### T-F-03 — Passive vs interactive learning

Same base model/data budget:

```text
passive video only
vs
passive video + action-conditioned trajectories
```

Measure:

- intervention prediction;
- counterfactual accuracy;
- novel-object affordance transfer;
- action success.

### T-F-04 — Causal factor explicitness

Compare:

```text
distributed latent predictor
vs
latent + identifiable alignment
vs
explicit causal state
```

at matched prediction and compute.

### T-F-05 — Causal recovery

Introduce an unexpected world change during a task and evaluate whether a system can identify the relevant changed dependency and replan efficiently.

## 11. Kill conditions

A named causal mechanism should be removed if it cannot outperform ordinary predictive representation on:

- intervention-sensitive prediction;
- spurious-correlation robustness;
- novel-intervention transfer;
- diagnosis/recovery;
- action success.

Likewise, do not require explicit causal variables if a distributed or identifiable latent obtains the same causal generalization more simply.

## 12. Clover landing

Current conclusion:

> **Causality should be operationalized through interventions, counterfactual state changes and action consequences. Passive visual prediction is important evidence, but the causal structure required for general robot behavior may need interaction or explicit identifiability assumptions.**
