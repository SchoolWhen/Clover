# Clover Hypotheses After the Research Reset

Last updated: 2026-10-14

This file preserves the strongest internal ideas from pre-reset Clover and `news_answers.md` **as hypotheses, not commitments**.

Filtering rule:

```text
external evidence / internal contradiction
→ identify the real problem
→ derive a Clover-native candidate
→ specify what would falsify it
→ only later decide whether to implement
```

## H1 — Evidence Replay / Dual Memory

**Problem:** compressed world state can discard evidence that later becomes relevant to a new query, contradiction or reinterpretation.

**Candidate:** keep evidence memory conceptually distinct from current world state.

```text
visual evidence memory
→ compile / infer
current world state
```

Historical evidence can be selectively replayed for local revision.

**External pressure:** VISTA shows that visual-memory organization/retrieval can unlock long-horizon reasoning without changing the base model. Paper: https://arxiv.org/abs/2610.02200

**Falsifier:** learned recurrent/contextual state matches or exceeds long-occlusion continuity, belief revision and memory cost without replay.

**Status:** `INTERNAL_HYPOTHESIS`

## H2 — Visual World Compiler

**Problem:** staged evidence transforms, state, queries and revision can develop duplicate semantics if treated as unrelated modules.

**Candidate abstraction:**

```text
visual history
→ evidence / IR
→ spatial-temporal structure
→ world representation
→ query/action-facing state
```

with selective invalidation/re-analysis after new evidence or queries.

This is an abstraction for dependency/provenance, not a commitment to compiler-style software architecture.

**Falsifier:** a unified learned recurrent/world model handles revision, queries and provenance more simply and robustly.

## H3 — Query-Sufficient Representation

**Problem:** compression, projection, pruning or downsampling can silently delete information required later.

**Candidate principle:** information may be discarded, but a transform should preserve distinctions needed by the downstream query/task family it claims to support.

Related evidence:
- V-JEPA shows useful representation can intentionally discard raw-pixel detail.
- ReWAM shows reconstruction fidelity is not the same as control usefulness: https://arxiv.org/abs/2609.38163
- VISTA shows discarded historical evidence may matter later.

**Falsifier:** representations that violate proposed sufficiency diagnostics consistently generalize and act better on full embodied evaluation.

## H4 — Query-Conditioned Temporal Persistence

**Problem:** evidence, object identity, place state and task state live on different time scales.

**Candidate:** effective retention should depend on state/query/dynamics rather than one fixed history window.

```text
H_l(q) = temporal support required by state level l for query/task q
```

Compare flat history, fixed hierarchy, learned recurrent memory and adaptive/query-conditioned persistence.

**Falsifier:** adaptive persistence gives no capability/memory advantage at matched compute.

## H5 — Separate Epistemic State from Verification / Validity State

Do not collapse:

```text
world uncertainty
model confidence
statistical calibration
claim validity
proof/provenance lifecycle
```

A world hypothesis can be observed/inferred/unobserved/ambiguous/conflicted while a previously issued claim artifact can independently be valid/stale/revoked.

This distinction may remain useful even if the old Licence implementation disappears.

**Falsifier:** a simpler unified probabilistic representation provides equal correctness, revision, refusal and planning without semantic confusion.

## H6 — Proof-Carrying / Auditable World Assertions

**Problem:** long-horizon robots can act on stale or origin-unknown beliefs.

**Candidate:** important world/decision assertions may carry compact machine-checkable dependencies/provenance.

Possible alternatives to compare:
- Bayesian belief only;
- calibrated confidence;
- event-sourced history;
- proof/provenance-bearing claim;
- implicit state + audit log.

**Falsifier:** explicit provenance adds complexity/latency without improving recovery, safety, debugging or long-horizon correctness.

## H7 — Counter-Witness-First Causality

**Problem:** temporal correlation is weaker than causal structure.

**Candidate:** begin from violated expectation.

```text
expected world
→ new observation disagrees
→ locate minimum broken dependency
→ causal candidate
→ test through future prediction/intervention
```

This connects prediction error, model revision and causal discovery.

**Falsifier:** does not improve intervention prediction over ordinary learned dynamics at matched data/compute.

## H8 — Epistemic Compute Scheduling

**Problem:** equal computation everywhere wastes resources.

Potential demand signals:

```text
unresolved evidence
world change
conflict
staleness
query/task dependency
expected information gain
```

Use epistemic state to decide **where/how much to compute**, not to decide truth directly.

**Falsifier:** dynamic allocation saves negligible end-to-end compute or destabilizes semantics.

## H9 — Sparse Visual Event IR

**Problem:** consecutive frames contain high redundancy; meaningful physical change may be sparse.

**Candidate:** keep RGB as scientific input, derive sparse event-like internal evidence from change/prediction residuals.

External evidence: Motion-aware Event Suppression demonstrates high-rate sparse processing and downstream compute savings: https://arxiv.org/abs/2602.23204

**Falsifier:** eventization loses world/query information or worsens total latency.

## H10 — Geometry as Proposal / Heuristic

**Problem:** a useful world representation should reduce downstream reasoning cost.

**Candidate:** geometry informs proposal ordering, reachability or lower-bound heuristics without becoming a separate decision authority.

**Falsifier:** geometry does not reduce planning cost or improve generalization at matched correctness.

## H11 — Static / Dynamic Verification Compilation

If future Clover retains explicit checking, invariant/static structure could be precompiled while current evidence produces a small dynamic witness.

**Falsifier:** explicit verification is not core, or precompilation gives no meaningful latency benefit.

## H12 — State-Transition Affordance Instead of Category→Action Lookup

A general robot should not depend on rules like `ball → push`.

Candidate:

```text
required world change ΔW_goal
vs predicted capability effect ΔW_tool
→ compatibility / affordance
```

The object's human name becomes secondary.

ReWAM/HWAM/world-action models reinforce the importance of action-conditioned/task-relevant state.

**Falsifier:** direct learned policies transfer better to novel objects/tasks at equal data/compute with no benefit from explicit transformation matching.

## H13 — Type as Dynamical / Transformation Equivalence

Candidate internal type is a reusable equivalence class of geometry, motion response, interaction, deformability or affordance rather than only a human category name.

**Falsifier:** semantic categories or distributed features consistently transfer better to unseen objects/actions.

## H14 — Active Perception as Unknown→Action Bridge

When current view is insufficient:

```text
ambiguity
→ candidate visual action
→ expected information gain
→ look/move/inspect
→ updated world
```

External pressure: Vantage shows view/evidence selection can improve spatial reasoning: https://arxiv.org/abs/2610.11810

**Falsifier:** passive context/memory reaches equal reliability/task success without active evidence acquisition.

## H15 — Worldview Value Must Be Proven Through Action

An explicit world representation is scientifically valuable only if it produces measurable benefit such as:

- better unseen-scene transfer;
- lower sample complexity;
- faster planning/search;
- stronger world-change recovery;
- fewer unjustified actions;
- better long-horizon success;
- better diagnosis/revision.

Critical eventual comparison:

```text
strong policy
vs
matched policy + Clover world representation
```

This is a required falsifier for the explicit-worldview program itself.

---

# Promotion rule

Before any hypothesis becomes next-generation Clover architecture, it needs:

1. operational variables/definitions;
2. prior-art comparison;
3. discriminating experiment;
4. kill condition;
5. action-relevance argument;
6. compute/hardware implications;
7. evidence that it unifies rather than adds a side path.

The correct outcome may be to merge, transform or delete several hypotheses.
