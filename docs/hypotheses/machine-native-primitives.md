# Hypothesis — Machine-Native World Primitives

**Status:** `OPEN`

## Question

Is there a small primitive family that can compose from local visual evidence into entities, regions and task-relevant world structure while remaining efficient and queryable?

## Motivation

Traditional systems often change representation at every level: pixels → points → voxels → objects → scene graph → task state. A unified primitive family could reduce semantic impedance and improve update efficiency.

## Candidate properties

A candidate primitive may need some subset of:

- spatiotemporal support;
- extent/scale;
- evidence/belief;
- observability;
- local dynamics;
- identity/lineage;
- authority/provenance handle.

No field list is frozen.

## Competing explanations

- dense learned latent representation;
- explicit geometry + semantic layers;
- object slots;
- scene graphs;
- generative spatial world models.

## Falsifier

If unification requires growing special-case fields or performs worse than specialized representations on query expressibility, update cost and generalization, the unified-primitive hypothesis should be rejected.
