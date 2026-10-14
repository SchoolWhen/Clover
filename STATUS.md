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
13. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
14. [`research/README.md`](research/README.md)

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
11 current frontier
```

### Open-world epistemics now explicitly includes

[`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)

```text
E1 observation uncertainty
E2 state uncertainty
E3 parameter uncertainty
E4 model-structure uncertainty
E5 hypothesis-set incompleteness
E6 regime change / model invalidation
E7 social / intentional uncertainty
E8 epistemic-action safety
```

Current primary/reference anchors include:

- HUME open-world model expansion — https://arxiv.org/abs/2607.06501 · https://open-world-planning.github.io/
- Changepoint-Aware World Models — https://arxiv.org/abs/2609.18950
- Feedback World Model — https://arxiv.org/abs/2605.15705
- Sirius-Fleet deployment monitoring — https://proceedings.mlr.press/v270/liu25g.html
- Diffusion-Based Body Schema — https://arxiv.org/abs/2608.01029
- Embodiment Gap survey — https://arxiv.org/abs/2608.18433
- Splat-CBF safe next-best-view — https://arxiv.org/abs/2609.23100
- ATOM-CBF — https://proceedings.mlr.press/v331/yun26a.html
- hidden-goal human–robot coordination — https://arxiv.org/abs/2608.04309

Central new distinctions:

```text
uncertainty over known hypotheses
≠
correct hypothesis missing entirely

uncertain current state
≠
world model itself is wrong / stale

information-seeking action
≠
safe information-seeking action

external world state
≠
self / embodiment state

visible behavior of another agent
≠
that agent's hidden goal / belief
```

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
- assuming the robot body/controller/camera is permanently fixed;
- treating one benchmark as the definition of understanding;
- optimizing hardware before the scientific mechanism.

## Remaining collection gaps

Stage 1 still needs stronger primary evidence for:

```text
unknown-unknown detection
open-set mechanism discovery
model-class selection / nonparametric world models
persistent provenance for hypotheses and refutations
scientific experiment design / falsification
slow long-horizon model drift
representation reversibility after compression
human-query / escalation cost models
social permission / consent for probing actions
multi-agent belief recursion
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
11. datasets/benchmarks that discriminate claims;
12. methods deserving one-method-one-report Analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, a final representation, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, a validated original algorithm, or a final hardware mapping.

These remain research targets.
