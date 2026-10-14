# Clover Hypotheses After the Research Reset

Last updated: 2026-10-14

Strong internal ideas from pre-reset Clover and `news_answers.md`, retained **as hypotheses, not commitments**.

Filtering rule:

```text
external evidence / internal contradiction
→ identify the real problem
→ derive a Clover-native candidate
→ define falsifier
→ only later decide whether to implement
```

## H1 — Evidence Replay / Dual Memory
Compressed world state may discard evidence later needed for a new query or contradiction. Candidate: keep visual evidence memory distinct from current world state and replay selectively for local revision.

External pressure: VISTA https://arxiv.org/abs/2610.02200

Falsifier: learned recurrent/contextual state matches or exceeds long-occlusion continuity, belief revision and memory cost without replay.

## H2 — Visual World Compiler
Candidate abstraction:

```text
visual history
→ evidence / IR
→ spatial-temporal structure
→ world representation
→ query/action-facing state
```

with selective invalidation/re-analysis after new evidence. This is a dependency/provenance abstraction, not a commitment to compiler-shaped software.

Falsifier: a unified learned world model handles revision, queries and provenance more simply/robustly.

## H3 — Query-Sufficient Representation
Compression/pruning may remove information required later. Candidate principle: a transform may be lossy, but must preserve distinctions needed by the query/task family it claims to support.

Relevant evidence: V-JEPA predictive abstraction, ReWAM https://arxiv.org/abs/2609.38163, VISTA.

Falsifier: representations that fail the proposed sufficiency diagnostics nevertheless generalize and act better in full embodied evaluation.

## H4 — Query-Conditioned Temporal Persistence
Evidence, object identity, place state and task state operate at different timescales. Retention may need to depend on state/query/dynamics rather than one history window.

Compare flat history, fixed hierarchy, learned recurrent memory and adaptive persistence.

Falsifier: adaptive persistence gives no capability/memory advantage at matched compute.

## H5 — Separate Epistemic State from Verification State
Do not collapse world uncertainty, confidence, calibration, claim validity and provenance lifecycle.

Even if old Licence machinery disappears, “what the system knows” and “whether a particular assertion artifact remains valid” may need separate semantics.

Falsifier: simpler unified probabilistic state provides equal correctness, revision, refusal and planning without semantic confusion.

## H6 — Proof-Carrying / Auditable Assertions
Long-horizon robots can act on stale/origin-unknown beliefs. Candidate: important assertions carry compact evidence/state dependencies or provenance.

Compare with Bayesian belief only, calibrated confidence, event sourcing and implicit state + audit logs.

Falsifier: explicit provenance adds latency/complexity without improving recovery, safety, debugging or long-horizon correctness.

## H7 — Counter-Witness-First Causality

```text
expected world
→ observation disagrees
→ locate minimum broken dependency
→ causal candidate
→ test by prediction/intervention
```

Connects prediction error, revision and causal discovery.

Falsifier: no intervention-prediction gain over ordinary learned dynamics.

## H8 — Epistemic Compute Scheduling
Use unresolved evidence, conflict, change, query relevance and expected information gain to decide where/how much to compute — not to decide truth.

Falsifier: negligible end-to-end savings or unstable semantics.

## H9 — Sparse Visual Event IR
Keep RGB as scientific input, derive sparse change/prediction-residual evidence internally.

External evidence: https://arxiv.org/abs/2602.23204

Falsifier: loses world/query information or worsens total latency.

## H10 — Geometry as Proposal / Heuristic
World geometry should reduce downstream search/decision cost, e.g. proposal ordering or reachability heuristics, without becoming a second decision authority.

Falsifier: no planning/generalization benefit at matched correctness.

## H11 — Static / Dynamic Verification Compilation
If explicit checking survives, static invariant structure might be precompiled while current evidence supplies a small dynamic witness.

Falsifier: verification is not core or precompilation gives no meaningful benefit.

## H12 — State-Transition Affordance
Avoid category→action lookup. Compare required world change with predicted capability effect:

```text
ΔW_goal
vs
ΔW_tool
→ compatibility / affordance
```

Falsifier: direct learned policy transfers better to novel objects/tasks at equal data/compute with no explicit transformation benefit.

## H13 — Type as Transformation Equivalence
Machine type may be a reusable equivalence class over geometry, motion response, interaction, deformability and affordance rather than a human category name.

Falsifier: semantic categories or distributed features transfer better to unseen objects/actions.

## H14 — Active Perception as Unknown→Action Bridge

```text
ambiguity
→ candidate visual action
→ expected information gain
→ look/move/inspect
→ updated world
```

External pressure: Vantage https://arxiv.org/abs/2610.11810

Falsifier: passive context/memory reaches equal reliability/task success.

## H15 — Worldview Value Must Be Proven Through Action
An explicit worldview is valuable only if it improves unseen-scene transfer, sample efficiency, planning/search, world-change recovery, unjustified-action rate, long-horizon success or diagnosis/revision.

Critical eventual comparison:

```text
strong policy
vs
matched policy + Clover world representation
```

This is a required falsifier for the explicit-worldview program itself.

## Promotion rule

Before promotion, a hypothesis needs operational definitions, prior-art comparison, a discriminating experiment, kill condition, action-relevance argument, compute implications and evidence that it unifies rather than adds a side path.

The correct outcome may be to merge, transform or delete several hypotheses.
