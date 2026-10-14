# Causality and Counterfactual World Understanding

## Core question

> **Does predicting what happens next amount to understanding why it happens?**

No. A predictor can exploit correlation without identifying interventions or mechanisms.

## Levels of evidence

A useful hierarchy is:

1. **co-occurrence** — A and B appear together;
2. **temporal prediction** — A helps predict B;
3. **action-conditioned prediction** — under action `a`, B is predicted;
4. **intervention sensitivity** — changing a specific factor changes the predicted consequence;
5. **counterfactual support** — the model can compare what happened with what would have happened under a different intervention.

Clover should avoid calling levels 1–2 causal understanding.

## Relevant modern direction

Action-conditioned world models, robot interaction data and physically grounded video reasoning provide stronger evidence than passive next-frame prediction alone.

CausalVQA is useful as a diagnostic for counterfactual/hypothetical/anticipatory questions in video, but language QA performance is not sufficient evidence for an internal causal world model.

Primary reference:

- https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

## Clover hypothesis worth preserving for study

A promising idea from earlier Clover work is **counter-witness-driven revision**:

```text
expected world transition
        ↓
new observation contradicts expectation
        ↓
identify minimal broken dependency
        ↓
propose causal explanation
        ↓
revise local world model
```

This remains a hypothesis, not a validated mechanism.

## What a strong causal test should eventually require

- matched or near-matched visual prefixes;
- controlled intervention difference;
- predicted consequence difference;
- correct identification of the affected world variables;
- resistance to background shortcuts;
- ability to revise after an unexpected intervention.

## Open questions

1. How much causal structure is identifiable from passive visual observation?
2. Which variables only become identifiable through intervention?
3. Can causal abstraction emerge without human semantic labels?
4. Is a compact causal graph useful, or is a distributed action-conditioned latent enough?
5. How should causal structure persist and revise over a robot's lifetime?
