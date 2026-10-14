# ADR 0007 — Survey Foundation Is the Primary Research Entry

**Date:** 2026-10-14  
**Status:** Accepted

## Context

The public Clover repository initially grew through a research map, literature notes, evaluation notes and hypothesis pages. That structure was useful for bootstrapping, but the research surface became fragmented: a new reader had to traverse many small files before seeing the full landscape.

At the same time, three substantial source documents existed outside the repository:

- the 2026-10-14 Research Reset;
- the accumulated news / frontier archive;
- the post-screening news decisions and hypotheses.

These sources contain useful research material, but they also contain historical assumptions, pre-reset commitments, secondary reports and implementation-specific decisions that should not be copied into the current SSOT unchanged.

## Decision

Create a flat, content-heavy `research/survey/` layer and make it the primary entry point for the current research phase.

The survey contains:

- a single overview README;
- frontier methods;
- papers / primary sources;
- benchmarks and embodied tasks;
- datasets and code resources;
- cross-cutting research questions;
- screened Clover hypotheses;
- screened frontier signals.

The three historical source documents are **synthesized, not raw-imported**. A statement enters the survey only after being classified as one of:

- primary scientific evidence;
- official reported result;
- research hypothesis;
- frontier signal;
- historical context.

Old `docs/research-map/` and `research/literature/` material remains available as secondary reference. It no longer needs to be the first path a reader follows.

## Why

A flatter survey layer makes it possible to answer, quickly and in one place:

1. What is already known?
2. What are the strongest current methods?
3. What evidence supports them?
4. What are the available papers, codebases, datasets and benchmarks?
5. What remains unresolved for Clover's SSOT?
6. Which old Clover ideas remain legitimate hypotheses after the Research Reset?

## Consequences

- `research/survey/` becomes the main research navigation surface.
- Root `AGENTS.md` and `SSOT.md` become mandatory orientation files for agents and contributors.
- Future frontier additions should update the survey rather than creating a new daily-fragment directory unless the raw archive itself is the object of study.
- Research notes may remain exploratory, but no note becomes current project truth without updating the relevant survey/SSOT/status material.
- Code-generation/versioning remains out of scope for this decision.
