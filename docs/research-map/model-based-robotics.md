# Model-Based Robotics

## Why this matters

Long before modern world models, robotics formalized the separation among hidden world state, uncertain belief, observation, action and control. Clover should learn from that theory instead of reinventing its vocabulary.

## Core abstractions

### State estimation

Estimate a latent physical state from noisy observations, often with an explicit uncertainty model.

### Bayesian filtering

Alternates prediction and measurement update:

```text
belief_t
  ↓ dynamics
predicted belief_{t+1}
  ↓ observation
updated belief_{t+1}
```

This is conceptually close to any Clover mechanism that distinguishes evidence from belief.

### POMDP

A Partially Observable Markov Decision Process explicitly represents that the true state is not fully observed. Decision making occurs over beliefs rather than pretending unobserved facts are known.

### Model Predictive Control

Predicts candidate future trajectories under actions, optimizes a finite horizon, executes part of the plan, then replans from new observations.

### Belief-space planning

Plans not only how the world may change, but how actions may reduce uncertainty.

## Clover relevance

Several Clover ideas have classical analogues:

| Clover concern | Existing robotics concept |
|---|---|
| unobserved vs known | partial observability |
| evidence/belief separation | Bayesian filtering |
| stale world state | belief update after new observation |
| active perception | information-gathering action |
| prediction under action | transition model / MPC |
| decision with uncertainty | POMDP / belief-space planning |

The purpose of studying these analogues is not to collapse Clover into a POMDP implementation. It is to avoid claiming novelty for distinctions that robotics already formalized well.

## Where classical model-based robotics is still limited

- state variables are usually chosen in advance;
- object/type ontology is usually task-specific;
- perception and state definition are often separate engineering stages;
- broad semantic priors and open-world learning are limited;
- scaling to unconstrained everyday visual worlds remains difficult.

## Central research question

> **Can Clover learn the state representation itself from visual experience while retaining the rigor of partial observability, belief revision and model-based decision making?**

That question is more substantive than simply replacing a neural policy with a hand-written state machine.
