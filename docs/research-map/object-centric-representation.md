# Object-Centric Representation

## Core question

> **Should a machine represent the world as persistent entities, or can object-like structure remain implicit inside a distributed representation?**

Objects are tempting primitives because robot tasks are often described in terms of things that persist, move, interact and can be acted upon. But treating objects as pre-given may bake human ontology into the system too early.

## Slot Attention

Slot Attention introduced a mechanism that maps perceptual features into a set of exchangeable slots through iterative competitive attention. The original work showed object-centric representations that generalize to unseen compositions in object-discovery/property-prediction settings.

Primary source:

- https://arxiv.org/abs/2006.15055

## Video segmentation and tracking as a lower-level baseline

SAM 2 extends promptable segmentation to image and video and adds streaming memory for maintaining target masks through a sequence. Meta describes memory that carries target-object context across frames, including temporary disappearance.

Primary source:

- https://ai.meta.com/research/sam2/
- https://github.com/facebookresearch/sam2

SAM 2 is not a world model. It is useful because it isolates a concrete subproblem:

> how well can a strong modern vision system maintain a visually specified entity through time?

## Competing hypotheses

### H1 — Object as primitive

The world state directly contains entity records with identity and state.

**Advantage:** simple queries, planning and relation construction.

**Risk:** premature segmentation and brittle ontology.

### H2 — Object as emergent structure

Objects emerge from lower-level spatial/temporal structure, field coherence or predictive equivalence.

**Advantage:** can adapt to unfamiliar entities and scales.

**Risk:** may be difficult to stabilize and query.

### H3 — Distributed latent only

No explicit object record is required; object information is decoded when needed.

**Advantage:** representation is not forced through an information bottleneck.

**Risk:** persistence, revision, provenance and planning may be hard to make reliable.

## What Clover needs from an entity representation

A useful entity mechanism should support:

- identity across viewpoint change;
- occlusion and reappearance;
- split/merge/deformation when appropriate;
- object-relative dynamics;
- relations and contact;
- uncertainty over identity;
- local belief revision;
- efficient queries for decision making.

## Critical question

Clover should not ask only:

> Can we segment objects?

It should ask:

> **Does explicit entity structure produce capabilities that a strong dense/video representation cannot provide as reliably or efficiently?**
