# Stage 1 — State Aliasing and Representation Failure

Last updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a failure mode that can remain hidden even when a learned representation looks compact, predictive or useful on average:

> Two physically or decision-relevantly different world histories may be mapped to the same internal state.

That failure is called **state aliasing** or **perceptual aliasing** in different literatures.

---

## 1. Minimal formulation

Let the history available to the agent be

```text
H_t = (O_1, A_1, O_2, ..., O_t)
```

and let a learned state encoder construct

```text
Z_t = F(H_t).
```

Aliasing occurs when two histories

```text
H_t^a ≠ H_t^b
```

map to approximately the same internal state

```text
F(H_t^a) ≈ F(H_t^b)
```

although they differ in something that matters for a required future function, for example:

```text
future observation distribution
action consequence
reward/value
object identity
hidden physical parameter
causal response
uncertainty
correct information-gathering action
```

The key point is task dependence:

```text
same latent state may be sufficient for task A
but aliased for task B.
```

State aliasing is therefore directly connected to [`RESEARCH_SUFFICIENT_STATE.md`](RESEARCH_SUFFICIENT_STATE.md).

---

## 2. Historical active-perception definition

**Learning to Perceive and Act by Trial and Error / Active Perception and Reinforcement Learning**  
Primary/background source: https://doi.org/10.1023/A:1022619109594  
Conference version: https://doi.org/10.1016/B978-1-55860-141-3.50025  
Evidence: `BACKGROUND_REFERENCE`

Whitehead and Ballard explicitly describe perceptual aliasing as a consequence of an internal representation that confounds external world states and show why this can destabilize decision learning.

The historical relevance for Clover is strong:

```text
representation failure
can create the need for
active information collection.
```

The agent may need to look again, move, or otherwise collect discriminating evidence before acting.

---

## 3. Markov-state failure can be detected without seeing true hidden state

### λ-discrepancy

**Mitigating Partial Observability in Sequential Decision Processes via the Lambda Discrepancy**  
NeurIPS 2024: https://papers.nips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html  
ArXiv: https://arxiv.org/abs/2407.07333  
Project: https://lambda-discrepancy.github.io/  
Evidence: `PRIMARY_PAPER`

The paper introduces the λ-discrepancy between temporal-difference estimates with different λ values. Because TD(0) assumes a Markov state while TD(1) can retain longer temporal dependence, disagreement is used as a signal that the current representation is non-Markovian.

Stage-1 interpretation:

```text
if giving the learner more history changes the correct value estimate,
the current state representation has discarded decision-relevant history.
```

This is useful because it does not require direct access to the true hidden state.

What it does **not** establish:

- that zero λ-discrepancy proves universal world understanding;
- that the representation is sufficient for every downstream task;
- that the missing variable is physically interpretable;
- that the learned memory is optimal for open-world transfer.

---

## 4. Partial observability can be discovered from visual inconsistency

### PO-PDDL

**PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty**  
Primary paper: https://arxiv.org/abs/2606.15654  
Evidence: `PRIMARY_PAPER`

PO-PDDL reconstructs latent symbolic state trajectories from real-robot execution videos and identifies partial observability through inconsistencies between inferred symbolic state and visible observations. It then learns stochastic transition and observation models for belief-space planning.

Why it matters:

This is a structured example of treating aliasing as a model mismatch:

```text
current visual observation
is insufficient to decide
which latent symbolic state is true.
```

It provides a useful explicit-state baseline even if Clover later uses a very different representation.

---

## 5. Observable equivalence is not the same as physical equality

### Observable quotient world models

**Observable quotient world models for knowledge-state abstraction under partial observability**  
Journal page: https://www.sciencedirect.com/science/article/pii/S0950705126014942  
DOI: https://doi.org/10.1016/j.knosys.2026.116768  
Evidence: `PRIMARY_PAPER`

This 2026 work defines quotients from action-conditioned observation laws, builds quotient beliefs/filtering/dynamics and explicitly studies which world distinctions are supported by observation.

Stage-1 value:

It sharpens an important distinction:

```text
physically different states
may be observationally equivalent
under the current sensor/action protocol.
```

A world representation should not be punished for failing to distinguish states that the available evidence cannot distinguish. Instead it should preserve uncertainty or equivalence until new evidence breaks the tie.

---

## 6. Bisimulation gives a behavior-based abstraction criterion

### Classical/control representation perspective

**Invariant Representations for Reinforcement Learning without Reconstruction**  
OpenReview: https://openreview.net/forum?id=kmaPnFKCuq  
Evidence: `PRIMARY_PAPER`

Bisimulation-based representation learning groups states when they have equivalent reward and transition behavior, deliberately removing visually different but behaviorally irrelevant information.

### 2026 state-abstraction theory

**Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning**  
PMLR: https://proceedings.mlr.press/v306/zhang26dy.html  
ArXiv: https://arxiv.org/abs/2606.25357  
Evidence: `PRIMARY_PAPER`

This work develops a general framework for reasoning about what behavioral properties are preserved under abstraction, including invariants, bisimulation relations and behavioral metrics.

### 2026 visual bisimulation geometry

**PAMD: Structured Adaptive Distances for Bisimulation Representations in Visual Reinforcement Learning**  
PMLR: https://proceedings.mlr.press/v306/roh26a.html  
Evidence: `PRIMARY_PAPER`

PAMD shows that even after choosing bisimulation as the abstraction principle, the metric used to compare latent states matters: fixed global norms can be too restrictive, while unconstrained distances can become degenerate.

Stage-1 implication:

```text
abstraction criterion
and
latent geometry
are separate research choices.
```

---

## 7. Aliasing taxonomy for Clover research

Stage 1 should distinguish at least:

### A1 — perceptual aliasing

Different external states produce similar/currently indistinguishable visual observations.

Examples:

```text
occluded object present vs removed
same-looking containers with different contents
same surface appearance with different friction
```

### A2 — history aliasing

The current frame is the same, but different histories imply different correct beliefs.

Examples:

```text
object was moved while previously visible
switch was toggled earlier
container was filled earlier
```

### A3 — representation aliasing

The observation/history contains the information, but the learned encoder discards it.

### A4 — action aliasing

Different embodiments/controllers map numerically similar actions to different physical consequences.

Related source: SyncWorld — https://arxiv.org/abs/2609.09155

### A5 — causal aliasing

Two states look similar under passive observation but respond differently to intervention.

### A6 — task aliasing

A representation deliberately merges states because they are equivalent for the current task, although another future task would need the distinction.

This is not necessarily an error; it becomes an error when the task distribution changes.

---

## 8. Candidate diagnostics for later stages

Stage 1 records these only as future evaluation ideas.

### Diagnostic D-A1 — history-rescue test

```text
performance with Z_t
vs
performance with Z_t + additional history
```

If history reliably improves the relevant prediction/control query, `Z_t` is not sufficient for that function.

### Diagnostic D-A2 — intervention split

Construct two histories that are visually similar now but differ in hidden causal state. Apply the same probe action and measure whether predicted outcomes diverge correctly.

### Diagnostic D-A3 — counterfactual nearest neighbors

Search latent nearest neighbors for states with different valid action consequences. High collision rate indicates action-relevant aliasing.

### Diagnostic D-A4 — belief calibration under unresolved aliases

When two worlds remain observationally compatible, measure whether the model preserves uncertainty rather than collapsing to one guess.

### Diagnostic D-A5 — task transfer after compression

Train/construct a compact state for task A, then evaluate whether task B exposes information that the representation irreversibly discarded.

---

## 9. Adjacent gaps discovered

State aliasing connects directly to several additional Stage-1 areas:

```text
structured memory
multi-timescale dynamics
belief-state calibration
non-stationarity / world change
active information gathering
open-world task transfer
```

Important 2026 references include:

- Flow Equivariant World Models — https://proceedings.mlr.press/v306/lillemark26a.html — structured latent memory aligned with self-motion/external motion under partial observability.
- HiMe — https://proceedings.mlr.press/v306/ji26k.html — hierarchical working/long-term memory for non-Markovian long-horizon VLA tasks.
- OASIS-Map — https://arxiv.org/abs/2607.14899 — world change across sessions.
- R4DSG — https://arxiv.org/abs/2608.11017 — persistent relative 4D object/change memory.

---

## 10. Stage-1 questions

```text
When do two physically different worlds become observationally indistinguishable?
When is that ambiguity removable by history?
When is it removable only by action?
When does a learned representation discard information that was actually available?
Which state distinctions are necessary for prediction, action, memory, causality and open-world transfer?
Can we detect aliasing without privileged ground-truth state?
How should a system represent unresolved aliases: one latent point, a distribution, a set, particles, hypotheses, or something else?
```

---

## Current rule

Do not demand that a representation distinguish states that the available evidence cannot distinguish.

Do demand that it avoid collapsing states that differ in a capability the system claims to support.

```text
indistinguishable from available evidence
≠
representation failure

information was available but discarded
=
potential representation failure
```
