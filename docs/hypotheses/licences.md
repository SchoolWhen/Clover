# Hypothesis — Epistemic Licences

**Status:** `RESEARCH_PROTOTYPE`

## Question

Can machine-verifiable authority envelopes make world assertions safer to consume, easier to invalidate and easier to audit without becoming a second notion of confidence?

## Current idea

A licence binds a claim to evidence/dependencies/version/proof so downstream modules can distinguish an authoritative assertion from stale or revoked state.

## Important semantic boundary

Licence is **not** probability, confidence or uncertainty. If evidence is insufficient for a claim, the clean design may be to refuse to mint the claim rather than encode uncertainty as a licence state.

## Why it may matter

- dependency-scoped invalidation;
- auditability;
- stale propagation;
- reproducible decision premises.

## Competing explanation

Ordinary typed state + provenance + calibrated uncertainty may provide equivalent value with lower complexity.

## Falsifier

If licences do not improve correctness under stale/contradictory state, auditability or decision safety enough to justify their runtime/engineering cost, they should be simplified or removed.
