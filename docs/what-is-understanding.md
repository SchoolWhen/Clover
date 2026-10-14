# What Is Understanding?

This document is a **working technical definition**, not a philosophical final answer.

A useful visual world model should support several independent capabilities.

## Persistence

The world continues when it is not visible. The system should preserve or deliberately suspend beliefs through occlusion rather than equating absence of evidence with absence of an entity.

## Identity

The system should determine when observations across time refer to the same entity, including after motion and temporary disappearance.

## Spatial structure

It should represent relative position, containment, support, visibility and other spatial relationships at the precision needed by downstream tasks.

## Temporal structure

It should distinguish transient observation from persistent state and represent change across multiple time scales.

## Dynamics and physical plausibility

It should learn or encode constraints on how the world can change and recognize violations or uncertainty.

## Causality and counterfactuals

It should reason about interventions: what changed, why, what an action may cause, and what would happen under alternatives.

## Open-world epistemics

Unknown, unobserved, contradicted and known-free states must not collapse into one value.

## Memory and revision

New evidence should be able to revise earlier world beliefs without rebuilding the entire system from scratch.

## Generalization

The representation should remain useful in new scenes, with new objects and new combinations.

## Decision usefulness

World understanding should eventually reduce errors, search, unsafe actions or recovery cost in embodied tasks.

## Evaluation stance

No single item is sufficient. Benchmarks diagnose pieces of the definition; real embodied tasks test whether the pieces compose.
