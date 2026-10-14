# Decision 0002 — Hardware Is a Design Variable

**Date:** 2026-10-14  
**Status:** Accepted

## Context

Earlier Clover work emphasized CPU-first execution. That emphasis risked turning a hardware preference into a scientific prior.

## Decision

CPU, GPU, Metal and other accelerators are design variables selected after understanding the computation required by the research mechanism.

The project will use Apple Silicon M4 as a useful unified-memory research platform, but will not constrain the scientific answer to CPU-only or GPU-only methods.

## Why

The history of modern vision shows that representation learning and scalable computation changed what was possible. Clover should understand that history before deciding which computations belong on which hardware.

## Consequences

- no `CPU > GPU` project claim;
- no separate scientific algorithm solely to fit one device;
- later hardware co-design should map sparse/branch-heavy and dense/batched computation to appropriate processors;
- external GPU resources remain valid for research baselines if needed.
