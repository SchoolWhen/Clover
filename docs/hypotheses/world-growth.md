# Hypothesis — World Growth

**Status:** `OPEN`

## Question

Can the robot's world representation grow and revise during operation rather than remaining a frozen ontology learned only offline?

## Desired operations

- add;
- merge;
- split;
- revise;
- retire;
- forget;
- consolidate.

## Key requirement

Growth is not simply accumulating memory. New evidence must be capable of correcting an earlier wrong belief or abstraction.

## Competing approaches

- continual neural fine-tuning;
- episodic retrieval without ontology change;
- frozen foundation model + external memory;
- Bayesian state/model adaptation.

## Falsifier

If online growth introduces instability or catastrophic corruption without measurable gains in novel-object/world adaptation, the current growth mechanism is not sufficient.
