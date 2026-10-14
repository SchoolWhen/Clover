# 09 — What Is Causal Understanding?

## Question

When does a model move from predicting correlation to understanding how interventions change the world?

## Prediction is not yet causation

A video model can predict likely futures from observational regularities. This is valuable but does not by itself identify what variable caused the transition or what intervention would change the outcome.

## Causal evidence becomes stronger with interventions

For a robot, action provides natural interventions:

```text
observe state
→ apply controlled action
→ observe visual consequence
```

Repeated interventions can expose action-conditioned dynamics and affordances that passive video cannot uniquely identify.

## Counterfactual reasoning

A stronger world model should answer questions of the form:

- What if the support were removed?
- What if the object were pushed in another direction?
- Which action would make a desired state occur?

CausalVQA provides a useful video-reasoning diagnostic, but language QA is weaker evidence than interaction-grounded intervention prediction.

## Planning-oriented world models

PlaNet, DreamerV3, TD-MPC2 and V-JEPA 2-AC all use learned dynamics to support action selection. They show that predictive dynamics can be operationally useful without necessarily exposing a human-readable causal graph.

This is another Clover tension: explicit causal structure may aid revision and transfer, but it must demonstrate value beyond a strong latent dynamics model.

## Clover implication

Future causal claims should be tied to intervention-sensitive tests, not just next-frame or next-state accuracy.

## Primary sources

- CausalVQA official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- V-JEPA 2 / V-JEPA 2-AC: https://arxiv.org/abs/2506.09985
- DreamerV3: https://arxiv.org/abs/2301.04104
- TD-MPC2: https://arxiv.org/abs/2310.16828
