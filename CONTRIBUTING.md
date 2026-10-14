# Contributing to Clover

Clover is a research project, so a contribution can be code, an experiment, a literature synthesis, a falsifier, a benchmark analysis or a correction to the project model.

## Before proposing a mechanism

Please state:

1. **Research contradiction** — what problem prevents progress on the central question?
2. **Existing work** — what has already been tried?
3. **Hypothesis** — what new claim are you making?
4. **Operational definition** — what exactly changes in the system?
5. **Falsifier** — what result would make us reject the mechanism?
6. **Expected capability impact** — which world-understanding ability should improve?
7. **Complexity / hardware impact** — what computation and memory does it introduce?

## Scientific claims

Do not turn implementation status into scientific status. Use the vocabulary in `STATUS.md` and provide evidence for claims such as SOTA, real-world generalization, physical consistency or causal understanding.

## External frameworks

Do not propose `Clover + framework X` as the contribution. Explain what contradiction X solves and whether a simpler Clover-native formulation is possible.

## Experiments

An experiment should record:

- research question;
- frozen protocol;
- baselines;
- success criterion;
- kill criterion;
- result;
- interpretation;
- limitations of the measurement.

## Code

Prefer inspectable, testable code. Avoid duplicated semantic authority, hidden side channels and unnecessary abstraction in hot paths.

## Documentation

Update relevant research, architecture and status documents when a change alters a claim or project direction.
