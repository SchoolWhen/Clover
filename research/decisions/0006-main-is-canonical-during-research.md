# ADR 0006 — `main` Is the Canonical Research Branch During the Mapping Phase

**Status:** Accepted  
**Date:** 2026-10-14

## Context

Clover is currently in a research-mapping phase rather than a multi-team implementation phase. Keeping long-lived research branches creates unnecessary divergence between the public record and the current research conclusions.

## Decision

During the current phase:

- `main` is the canonical public research record;
- temporary branches may be used for atomic edits or review;
- once merged, temporary branches should contain no unique research content and should be deleted;
- important changes are preserved through commits, PR history and ADRs rather than long-lived branches.

## Consequence

Research readers should treat `main` as current unless a document explicitly states that it is historical or superseded.
