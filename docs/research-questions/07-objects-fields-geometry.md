# 07 — Objects vs Fields vs Geometry

## Question

What are the basic units of a machine's world model: objects, continuous fields, geometric primitives, or something else?

## Object-centric view

Slot Attention argues that a scene can be decomposed into exchangeable slots that bind to entities and support compositional generalization.

SAM 2 demonstrates that object-like visual regions can be maintained over video with streaming memory.

Object representations are attractive for identity, relation and manipulation, but object boundaries can be ambiguous for fluids, articulated structures, crowds, shadows or changing topology.

## Geometric view

SLAM, DUSt3R and VGGT represent structure through cameras, points, depth and tracks. Geometry is strong for where things are and how views relate.

But pure geometry says little about which structure should count as an entity, what it can do, or why a change matters.

## Field/continuous view

NeRF represents a scene as a continuous radiance/density function. 3D Gaussian-style representations and generative spatial models offer other continuous or distributed scene substrates.

Old Clover field-crystallization hypotheses belong here, but they must be compared against these established continuous representations rather than treated as a unique category by default.

## Current synthesis

The world may require multiple scales of description:

```text
continuous spatial support
→ persistent structures
→ entities
→ relations / task abstractions
```

The research question is whether these need separate ontologies or can emerge from one representation family.

## Clover implication

The next Clover representation proposal should explain what happens in edge cases where `object` is not cleanly defined, while still making object-level action efficient when object structure is useful.

## Primary sources

- Slot Attention: https://arxiv.org/abs/2006.15055
- SAM 2: https://arxiv.org/abs/2408.00714
- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- NeRF: https://arxiv.org/abs/2003.08934
