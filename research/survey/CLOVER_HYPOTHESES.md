# Clover Hypotheses After the Research Reset

Last updated: 2026-10-14

This file preserves the strongest internal ideas from pre-reset Clover and `news_answers.md` **as hypotheses, not commitments**.

The filtering rule is:

```text
external evidence / internal contradiction
→ identify the real problem
→ derive a Clover-native candidate
→ specify what would falsify it
→ only later decide whether to implement
```

No item in this file is part of the SSOT merely because it originated inside Clover.

---

## H1 — Evidence Replay / Dual Memory

### Problem

A compressed world state is useful for efficient reasoning, but compression can discard visual evidence that becomes important later when:

- a new query appears;
- a belief is contradicted;
- a verifier challenges a claim;
- an earlier ambiguous observation becomes interpretable after later evidence.

### Candidate

Maintain two conceptually different things:

```text
visual evidence memory
        ↓ compile / infer
current world state
```

The world state is not identical to memory. Historical evidence can be selectively replayed when a local part of the world must be reconsidered.

### External pressure

VISTA demonstrates that visual-memory organization and retrieval can unlock long-horizon reasoning without changing the underlying base model.

- Paper: https://arxiv.org/abs/2610.02200

### Falsifier

If a learned recurrent/contextual state achieves equal or better:

- long-occlusion continuity;
- belief revision;
- new-query recovery;
- memory cost;

without evidence replay, this hypothesis loses its justification.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H2 — Visual World Compiler

### Problem

Clover historically accumulated frontend transforms, evidence primitives, world state, queries, licences and update logic. Treating each as an independent module risks duplicate semantics.

### Candidate abstraction

Treat world formation as a compilation process:

```text
visual history
→ evidence / intermediate representation
→ spatial-temporal structure
→ world representation
→ query/action-facing state
```

with reverse operations:

```text
new query → selective re-analysis
counter-evidence → dependency invalidation
belief revision → local recompile
```

### Why it remains useful after reset

This is not a proposal to imitate LLVM. It is an abstraction for:

- staged information transforms;
- dependency tracking;
- local invalidation;
- provenance;
- query-sufficiency.

### Falsifier

If a unified learned recurrent/world model handles these functions more simply and robustly without explicit staged compilation/dependency machinery, the compiler abstraction should remain documentation only or be removed.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H3 — Query-Sufficient Representation

### Problem

Compression, token pruning, downsampling, projection and latent bottlenecks can make the system faster while silently deleting information needed for later world questions.

### Candidate principle

Every authoritative transform should be evaluated relative to the query/task family it claims to support:

```text
before transform: query distinction exists
        ↓ transform
required distinction must remain recoverable
```

The claim is not that every representation must be lossless. It is that information loss must be aligned with declared downstream capability.

### Related prior art

- V-JEPA 2/2.1: predictive representations intentionally discard raw-pixel detail while preserving useful structure.
- ReWAM: reconstruction fidelity alone does not imply control usefulness.
- VISTA: discarded historical visual evidence can matter later.

### Falsifier

If a representation that fails the proposed query-sufficiency test nevertheless generalizes and acts better on the full embodied evaluation hierarchy, the test is incomplete or wrong.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H4 — Query-Conditioned Temporal Persistence

### Problem

Different world structures operate on different temporal scales:

- texture/motion evidence can change rapidly;
- object identity may persist through occlusion;
- room/place structure may persist much longer;
- task state can span minutes.

A single fixed memory horizon is unlikely to be optimal.

### Candidate

For representation level or state component `l` and query family `q`:

```text
H_l(q) = effective temporal support required for that state/query
```

The horizon should depend on evidence persistence, dynamics, query dependency and world change rather than fixed hand-written frame counts.

### Competing baselines

1. flat history window;
2. fixed hierarchical windows;
3. learned recurrent memory;
4. query-conditioned persistence.

### Falsifier

If adaptive persistence does not improve long-occlusion/place/task reasoning at matched compute/memory, remove it.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H5 — Epistemic State Must Be Separate from Authority / Verification State

### Problem

Several concepts are easy to collapse incorrectly:

```text
world uncertainty
model confidence
statistical calibration
claim validity
proof / verification lifecycle
```

### Candidate distinction

A world may be:

```text
observed
inferred
unobserved
ambiguous
conflicted
```

while a particular issued claim/proof could separately be:

```text
valid
stale
revoked
```

Historical example: `Underdetermined` should not automatically become a lifecycle state of a previously issued licence.

### Why it matters independent of the old Licence design

Even if the old proof-carrying licence mechanism is replaced, separating *what the system knows* from *whether a particular artifact is valid* remains conceptually important.

### Falsifier

If a simpler unified probabilistic representation supports equal correctness, revision, refusal and planning without semantic confusion, the separate authority abstraction may be unnecessary.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H6 — Proof-Carrying / Auditable World Assertions

### Problem

A robot can act on a belief that was once correct but is now stale, or on an assertion whose evidence source is unknown.

### Candidate

Important world/decision assertions may carry machine-checkable provenance such as:

```text
evidence dependency
world version / state dependency
claim identity
validity / stale status
```

Historical Clover implemented a richer licence idea; the reset asks whether the useful essence can be retained without over-engineering the representation.

### Competing alternatives

- Bayesian belief state only;
- confidence calibration;
- event-sourced state history;
- proof-carrying claims;
- learned implicit state with external audit logs.

### Falsifier

If explicit proof/provenance adds meaningful latency/complexity without improving recovery, safety, debugging or long-horizon correctness, it should not be core architecture.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H7 — Counter-Witness-First Causality

### Problem

Learning temporal correlations does not necessarily reveal causal structure.

### Candidate

Start from violated expectation:

```text
predicted / expected world
→ new observation disagrees
→ locate minimum broken dependency
→ propose causal explanation
→ test through future prediction/intervention
```

This makes causal learning a form of structured model revision rather than an isolated graph-learning module.

### External context

CausalVQA and action-conditioned world models reinforce the need to distinguish prediction from counterfactual/intervention competence.

### Falsifier

If counter-witness localization does not improve intervention prediction beyond ordinary learned dynamics at matched data/compute, reject the mechanism.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H8 — Epistemic Compute Scheduling

### Problem

A robot should not spend equal computation everywhere.

Potential demand signals include:

```text
unresolved evidence
world change
conflict
staleness
query/task dependency
expected information gain
```

### Candidate

Use epistemic state to decide **where/how much to compute**, not to decide truth directly.

```text
uncertain / relevant region → deeper or higher-resolution computation
stable / irrelevant region  → reuse / skip / coarsen
```

### Related frontier signals

- dynamic computation in VLA systems;
- sparse event processing;
- active view selection (Vantage).

### Falsifier

If dynamic allocation causes unstable semantics or saves negligible compute at equal capability, use uniform computation.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H9 — Sparse Visual Event IR

### Problem

Consecutive visual frames contain large redundant regions, while physically meaningful change can be sparse.

### Candidate

Standard RGB remains the scientific input, but internal evidence could use an event-like representation:

```text
RGB history
→ change / prediction residual
→ sparse signed event evidence
→ world update
```

This avoids binding Clover to event-camera hardware while testing the computational value of sparsity.

### External evidence

Motion-aware Event Suppression demonstrates high-speed sparse event processing and downstream token reduction:
https://arxiv.org/abs/2602.23204

### Falsifier

If eventization loses query/world information or total system latency is worse than dense processing, reject it.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H10 — Geometry as an Admissible Proposal / Heuristic

### Problem

A world representation should make downstream reasoning easier, not merely answer descriptive queries.

### Candidate

Use spatial/geometry structure to reduce search or prioritize proposals while keeping final decision legality/verification separate.

```text
world geometry
→ proposal ordering / reachability heuristic
→ decision search
```

This is more conservative than creating a second geometry-specific planner.

### Falsifier

If geometry does not reduce planning cost or improve generalization under matched correctness, it is not carrying useful decision structure.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H11 — Static / Dynamic Verification Compilation

### Problem

If future Clover uses explicit verification, repeatedly checking invariant structure at runtime may be wasteful.

### Candidate

Separate what is static from what depends on current visual evidence:

```text
static schema / invariant / program structure
→ precompiled proof/check structure

current evidence / state
→ small dynamic witness
```

### Falsifier

If verification is not a core architecture or compiled checking does not materially reduce latency without weakening semantics, remove this mechanism.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H12 — State-Transition Affordance Instead of Category-to-Action Lookup

### Problem

A general robot cannot rely on rules such as:

```text
ball → push
block → grasp
```

because novel objects and tasks break category-action tables.

### Candidate

Represent action/tool usefulness through expected world transformation:

```text
required world change ΔW_goal
vs
predicted capability effect ΔW_tool
→ compatibility / affordance
```

The object's name is secondary.

### Related prior art

ReWAM/HWAM/world-action models all emphasize task-relevant or action-conditioned state.

### Falsifier

If learned direct policy transfer outperforms explicit transformation matching on novel-object/generalization tasks at equal data/compute, the explicit affordance state may be unnecessary.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H13 — Type as a Dynamical / Transformation Equivalence Class

### Problem

Human category names may not be the most useful ontology for robot action.

### Candidate

A machine type can be induced from reusable behavior:

```text
entities with similar predicted transformations / interactions
→ same internal type family
```

Possible dimensions:

- geometry;
- motion response;
- support/contact behavior;
- deformability;
- affordance.

### Falsifier

If semantic categories or distributed features transfer better to unseen objects/tasks, do not preserve an explicit dynamical type system.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H14 — Active Perception as Unknown-to-Action Bridge

### Problem

Some world questions are not identifiable from the current view.

### Candidate

Represent missing evidence well enough to select an information-gaining visual action:

```text
current ambiguity
→ candidate visual action
→ expected information gain
→ look/move/inspect
→ world update
```

### External pressure

Vantage demonstrates that evidence/view selection can improve spatial reasoning:
https://arxiv.org/abs/2610.11810

### Falsifier

If passive context/memory reaches equivalent reliability and task success without active view selection, active perception is not universally required.

**Status:** `INTERNAL_HYPOTHESIS`

---

## H15 — Worldview Value Must Be Proven Through Action

### Problem

An explicit world representation can be interpretable yet unnecessary for competent behavior.

### Candidate scientific criterion

Clover's worldview is valuable only if it produces measurable benefit such as:

- lower sample complexity;
- better unseen-scene transfer;
- lower planning/search cost;
- stronger world-change recovery;
- fewer unjustified actions;
- better long-horizon task success;
- better diagnosis/revision.

### Critical comparison

```text
strong policy
vs
same/similar policy + Clover world representation
```

with matched data, compute and task protocol.

This is a central falsifier for the entire explicit-worldview program.

**Status:** `INTERNAL_HYPOTHESIS / REQUIRED_TEST`

---

# Hypothesis policy

These ideas survived screening because they address durable contradictions. They are **not** the next architecture by default.

Before promotion, each hypothesis needs:

1. clear operational variables;
2. prior-art comparison;
3. a discriminating experiment;
4. a kill condition;
5. an action-relevance argument;
6. compute/hardware implications;
7. evidence that it unifies rather than adds another side path.

The correct outcome may be to merge, transform or delete several of them.
