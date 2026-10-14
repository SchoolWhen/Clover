# R-D — Persistence, Memory and Belief Revision

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

> **How should a vision-only machine preserve and revise knowledge about a world that is only intermittently visible?**

Memory is not one thing. Candidate forms include:

```text
raw visual evidence
compressed perceptual history
persistent object/world state
episodic events
semantic memory
policy hidden state
external retrieval memory
hybrids
```

The project must distinguish remembering evidence from maintaining a world hypothesis.

## 2. Seeing is not remembering

### PersistBench / Can 4D Foundation Models Remember?

- Paper: https://arxiv.org/abs/2609.20819
- Project / dataset / code: https://guangzhaohe.com/persistbench

PersistBench uses 360° video as an omniscient reference while evaluating ordinary limited-field-of-view models on:

- object permanence;
- motion continuity;
- appearance preservation.

**Demonstrates:** current 4D reconstruction/video models can be strong while an object is observed yet degrade substantially once it leaves the field of view.

**Clover implication:**

```text
reconstruction consistency while visible
≠ persistent world memory
```

Any claim of a world model should therefore report out-of-FOV behavior, not only clip reconstruction or tracking.

## 3. Streaming episodic memory is different from offline long-context QA

### S-EMBER

- Paper: https://arxiv.org/abs/2607.02689
- Official publication index: https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

S-EMBER contains long egocentric streams and requires grounded retrieval with temporal localization of visual evidence.

**Demonstrates:** answering a question and locating the supporting past event are separable capabilities; current models show a substantial grounded-recall gap.

**Clover implication:** a long context window is not equivalent to reliable episodic world memory.

## 4. The memory harness itself can change capability

### VISTA

- Paper: https://arxiv.org/abs/2610.02200
- Project: https://vista-research.github.io/
- Code: https://github.com/joshhhhhan/VISTA

VISTA maintains a lossless archive of visual observations and lets the model actively retrieve and reorganize past visual evidence.

**Demonstrates:** with the same general-purpose reasoning backend, changing the visual-memory/inspection harness can strongly change long-horizon interactive performance.

**Important limitation:** its strongest results are on visual games and interactive environments, not proof that lossless replay is the optimal memory architecture for real robots.

**Clover implication:** memory architecture is an independent research variable; capability is not determined only by model weights.

## 5. Memory must support revision, not only recall

A useful world model must handle:

```text
old evidence
→ old belief
→ world changes
→ partial new evidence
→ contradiction detected
→ affected state revised
→ downstream queries/plans updated
```

A system that remembers everything but cannot revise stale beliefs is not maintaining a usable world model.

## 6. Evidence memory vs world state

A critical distinction:

```text
Evidence memory = what visual observations can be re-examined?
World state      = what does the system currently believe / represent about the world?
```

They may be implemented together or separately, but experiments must not conflate them.

Historical Clover's Evidence Replay idea remains a hypothesis because VISTA and similar results establish the value of retrievable evidence, not the necessity of a specific Clover replay compiler.

## 7. Forgetting is also a research problem

Unlimited retention is not a scalable answer.

A realistic system must decide what to:

- keep at full fidelity;
- compress;
- summarize;
- retain as persistent state;
- discard;
- reload when a query or contradiction demands it.

Therefore memory should be evaluated by a Pareto frontier over:

```text
capability
retention bytes
retrieval latency
update latency
compute
```

not by recall score alone.

## 8. Operational research questions

1. Is object permanence best represented in world state, recurrent latent memory, or external evidence memory?
2. When should an object become `unknown` rather than remain confidently predicted?
3. How long should different state types persist?
4. Can memory support a query that was not known when the evidence was first observed?
5. Does retaining raw evidence materially improve belief revision over compressed latent history?
6. What is the right forgetting policy under bounded storage?
7. How should memory distinguish the world changing from the system merely observing a different viewpoint?
8. Can stale downstream decisions be invalidated when an upstream world belief changes?

## 9. Baseline families

| Family | Baseline / example | Isolates |
|---|---|---|
| Fixed context | standard video/VLM context | no explicit long-term memory architecture |
| Recurrent/predictive latent | V-JEPA-like / recurrent policy | compressed temporal state |
| Visible tracker memory | SAM 3.1 | persistence while detectable/trackable |
| Reconstruction memory | 4D foundation models | geometric temporal consistency |
| External visual archive | VISTA-style harness | re-access to original visual evidence |
| Episodic retrieval | S-EMBER-style systems | retrieval/localization from streaming history |
| Explicit world state | historical Clover candidate / classical map | persistent queryable state |

## 10. Discriminating experiments

### T-D-01 — Long out-of-FOV persistence

Occlusion/out-of-view durations:

```text
4 / 8 / 16 / 32 / 64 / 128 frames
```

Measure:

- identity continuity;
- motion continuity;
- appearance consistency;
- uncertainty during absence;
- recovery at reappearance;
- memory bytes.

### T-D-02 — New-query replay

Observe a long sequence without knowing the later question.

After the sequence, ask a query that requires an old visual detail not represented in the current task state.

Compare:

```text
fixed compressed context
recurrent state
external replay/retrieval
hybrid state + replay
```

### T-D-03 — World change / stale belief

Move an object while it is unobserved, then reveal only partial evidence.

Measure:

- stale-state detection;
- time to revision;
- locality of revision;
- dependent planning errors;
- recovery.

### T-D-04 — Retention Pareto

At matched task correctness, compare:

```text
storage bytes
retrieval p50/p99
update p50/p99
energy where measurable
```

### T-D-05 — Evidence versus state ablation

Four conditions:

```text
world state only
raw/retrievable evidence only
world state + evidence
long-context latent only
```

This isolates whether each memory type contributes independent value.

## 11. Kill conditions

A dedicated evidence-replay mechanism should be demoted if it does not independently improve:

- new-query retrieval;
- belief revision;
- long-occlusion recovery;
- grounded verification;

at a defensible storage/latency cost.

A persistent explicit world state should also be rejected if a recurrent/latent memory reaches equal capability, revision quality and task success more simply.

## 12. Clover landing

Current conclusion:

> **Persistent world understanding requires more than a long context or visible tracking, but the correct architecture — recurrent latent, persistent state, retrievable evidence, or hybrid — remains open and must be decided by out-of-FOV, revision and new-query experiments.**
