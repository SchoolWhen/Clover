# Decision 0001 — Research Reset

**Date:** 2026-10-14  
**Status:** Accepted

## Context

Clover had accumulated increasingly detailed architecture, performance and benchmark work. The highest question remained valuable, but implementation preferences were beginning to function as assumptions that the research was trying to prove.

## Decision

Reset the project around one stable question:

> **How can a machine understand the real world through vision alone?**

The long-term product goal is a general-purpose robotic brain that forms a visual understanding of the world and uses it to decide and act.

Current mechanisms become hypotheses to be tested against classical and modern prior work.

## Why

Research should search for the best answer to the problem rather than protect an early answer.

## Consequences

- architecture-first development pauses as the organizing principle;
- research map and open questions become first-class assets;
- benchmarks become diagnostic instruments;
- current Clover code is Research Prototype 1;
- future architecture may preserve, transform or remove existing mechanisms.
