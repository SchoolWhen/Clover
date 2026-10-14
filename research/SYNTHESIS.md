# Stage 3 — Synthesis
## Comparative Summary, Trade-offs and Research Gaps

Last updated: 2026-10-14

**Status:** DEFINED, DOWNSTREAM OF SUFFICIENT ANALYSIS.

Synthesis combines many Stage 2 method reports into a field-level view.

## Core outputs

### Capability matrix

Compare methods across common capabilities:

```text
geometry
identity
object permanence
temporal consistency
observability / unknown
memory
revision
physics
causality
counterfactual reasoning
active perception
open-world generalization
action utility
recovery
compute
```

### Mechanism matrix

Compare how methods achieve capability:

```text
explicit geometry
dense features
predictive latent
slots/entities
graph state
external memory
generative simulation
joint world-action prediction
direct policy
hybrid / identifiable state
```

### Pros / cons summary

For every family, summarize:

```text
what it is genuinely good at
what it systematically misses
where evidence is strong
where evidence is weak
where evaluation may contain shortcuts
which assumptions it relies on
what it costs computationally
what is reproducible
```

### Failure matrix

Do not collapse failures into one score. Record them separately.

### Gap map

A gap is interesting only if:

1. multiple strong methods share it, or
2. solving it would materially improve real world understanding/action, and
3. current evidence does not already show a simpler solution.

## Synthesis questions

- Which research problems are already mostly solved?
- Which capabilities remain weak across method families?
- Which apparent disagreements are only terminology differences?
- Which methods have complementary strengths?
- Which trade-offs appear fundamental rather than engineering accidents?
- Which results depend heavily on language, privileged state, simulation or action supervision?
- Which benchmarks fail to distinguish competing hypotheses?
- Which strong direct-policy systems challenge the need for an explicit worldview?
- Which generative systems challenge the need for explicit state?
- Which memory failures challenge long-context approaches?
- Which causal results show that interaction is necessary?

## Output gate to Innovation

Stage 4 Innovation should not start from “I like this architecture.”

It starts from:

```text
well-supported unresolved gap
+ comparison of existing solutions
+ reason existing mechanisms are insufficient
+ discriminating test
```

Synthesis is where Clover earns the right to propose something new.
