# 0005 — Research before reproduction

**Status:** Accepted  
**Date:** 2026-10-14

## Context

After the Research Reset, an initial plan proposed quickly reproducing V-JEPA 2, VGGT, OpenVLA and benchmark suites. That would still risk moving into implementation before we understand what the major research families actually solve and where their assumptions differ.

## Decision

The current phase prioritizes **systematic research mapping before reproduction**.

We will first document:

- the representation each route uses;
- its learning objective and data assumptions;
- how it handles space, time, memory, physics and action;
- what has actually been demonstrated;
- what remains unresolved;
- what contradiction it creates for Clover's existing hypotheses.

Reproduction, benchmark comparison and paper-style ablation are deferred until the research landscape is sufficiently clear and Clover has a sharper representation hypothesis.

## Why

The project previously lost time by implementing before fully understanding the problem and prior art. Repeating that pattern with newer models would not fix the underlying research-method issue.

## Consequences

- Research Map depth is now a first-class deliverable.
- Benchmarks are catalogued but not treated as immediate optimization targets.
- Strong external models are studied as evidence and counter-hypotheses, not as components to integrate.
- Existing Clover code remains Research Prototype 1 while the next representation is reconsidered.

## Exit condition

Move into systematic reproduction when we can state, with evidence:

1. what major approaches already solve;
2. their common failure modes;
3. what unresolved capability matters for the robot-brain goal;
4. which Clover hypothesis is worth testing next and why.
