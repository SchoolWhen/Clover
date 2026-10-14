# Data, Experience and Interaction

## Core question

> **What kinds of experience are actually required for a machine to build a world model from vision?**

The modern robotics literature suggests that data source is part of the algorithmic question, not merely an engineering detail.

## Passive video

Strengths:

- enormous diversity;
- natural human/object/environment interactions;
- cheap relative to robot data;
- useful for learning visual and temporal regularities.

Limitation:

The model often does not know the agent's exact action/intervention, so some causal variables are not identifiable.

V-JEPA 2 is an important case: large-scale action-free video pretraining is followed by comparatively small action-conditioned robot post-training.

## Human egocentric video

Strengths:

- first-person viewpoint;
- long natural task sequences;
- dense hand-object interactions;
- scalable collection.

Limitations:

- human morphology differs from robots;
- action/force/proprioceptive signals may be absent;
- language narration can introduce non-visual supervision.

Ego4D and recent robot-foundation-model efforts make this a major research direction.

## Robot demonstrations / teleoperation

Strengths:

- explicit actions and consequences;
- robot embodiment matched to deployment;
- direct control supervision.

Limitations:

- expensive;
- limited environment diversity;
- often biased toward successful demonstrations.

DROID and Open X-Embodiment are important public resources.

## Simulation

Strengths:

- unlimited interventions;
- exact world state;
- controlled counterfactuals;
- scalable self-play / exploration.

Limitations:

- sim-to-real gap;
- simulator assumptions can become hidden supervision;
- visual realism is not equivalent to physical realism.

## Self-generated interaction

Self-play and autonomous exploration add a different source of evidence: the model can choose interventions specifically to reveal dynamics or improve skills.

For Clover this may connect directly to active perception and causal identification.

## Working hypothesis

A general robot brain may eventually require a curriculum combining:

```text
passive visual observation
+ egocentric human experience
+ robot action/consequence data
+ simulation/intervention
+ autonomous exploration
```

This is a research hypothesis. The contribution of each source should be measured rather than assumed.
