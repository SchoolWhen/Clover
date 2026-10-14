# Clover Status

Last updated: 2026-10-14

## Research Question

> **How can a machine understand the real world through vision alone?**

## Product Goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current Phase

**Survey / Research Foundation — ACTIVE.**

The immediate priority is not model reproduction, benchmark optimization or new architecture implementation. It is to establish a sufficiently deep account of what prior work already solves, what it fails to solve, what evidence is trustworthy, and what technical questions remain before the next Clover architecture is selected.

Start with [`SSOT.md`](SSOT.md) and [`research/survey/README.md`](research/survey/README.md).

## Public Research Foundation — IMPLEMENTED / EXPANDING

The repository now contains:

- root SSOT and agent rules;
- research principles and public status;
- a flat Survey layer with detailed frontier methods;
- a curated primary-paper/source catalogue;
- benchmark and real-task maps;
- datasets and code resources;
- cross-cutting research questions;
- screened post-reset Clover hypotheses;
- filtered frontier/news signals;
- older map-style literature, evaluation and architecture references;
- research decision records.

## Existing Clover Prototype — RESEARCH_PROTOTYPE

A substantial pre-reset Research Prototype 1 exists outside the current public codebase, exploring field-based visual evidence, persistent entities/spacetime support, typed world queries, epistemic licences, decision, tool-use and execution loops.

Those mechanisms are **candidate hypotheses**, not architectural commitments. Public code migration and the naming/versioning scheme for future code generations will be handled separately after the survey foundation is mature enough to inform the next architecture.

## Active Research Questions — OPEN

The current Survey explicitly investigates, among others:

- what a world representation must contain;
- explicit vs distributed state;
- geometry vs learned representation;
- prediction vs reconstruction vs generation;
- what vision alone can and cannot identify;
- passive observation vs interaction;
- object-, field- and geometry-centric representations;
- persistent memory and belief revision;
- intuitive physics and causal understanding;
- uncertainty, observability and refusal;
- language as knowledge and as a confound;
- active perception;
- whether a persistent worldview measurably improves action;
- embodiment-invariant abstractions;
- hardware/software co-design after the scientific mechanism is known.

## Evaluation — MAPPED, NOT YET THE OBJECTIVE

Public benchmarks and robot tasks are catalogued as measurement instruments. Current work is not a leaderboard campaign.

The eventual evidence hierarchy is:

1. controlled cognitive/physical diagnostics;
2. world-model / representation diagnostics;
3. embodied tasks in unfamiliar physical environments;
4. real-world generalization and recovery;
5. efficiency and hardware co-design once scientific capability is established.

## Not Yet Demonstrated

Clover has not yet publicly demonstrated:

- general real-world visual world understanding;
- comprehensive positive-result SOTA;
- robust open-world generalization;
- persistent long-horizon real-robot world state;
- general causal understanding;
- long-horizon autonomous robot-brain capability;
- an empirically established final representation;
- a final CPU/GPU/Metal allocation.

These are research targets. They do not justify lowering the research question.
