# Spatial Intelligence

## Core question

> **How much of world understanding can be obtained by reconstructing and maintaining coherent geometry from vision?**

Spatial intelligence is broader than depth estimation. It includes camera/world geometry, consistent multi-view representation, reconstruction, scene completion and potentially simulation.

## Classical-to-learned transition

Traditional SfM/SLAM explicitly optimizes camera geometry and sparse/dense landmarks. Modern geometry foundation models increasingly infer camera and scene geometry directly with learned feed-forward systems.

This transition is important to Clover because it asks which parts of a world representation should be mathematically constrained and which should be learned from scale.

## VGGT

VGGT (CVPR 2025 Best Paper) is a feed-forward learned geometry model. The official repository describes direct inference of key 3D scene attributes including camera intrinsics/extrinsics, depth maps, point maps and 3D point tracks from one or many views.

Primary source:

- https://github.com/facebookresearch/vggt

### Why Clover cares

VGGT demonstrates that a large learned visual model can collapse a traditionally multi-stage geometry pipeline into one learned inference system while still outputting explicit geometric quantities.

This creates a powerful hybrid precedent:

> **learned representation does not imply that the output world state must remain implicit.**

## VGGT-Ω

VGGT-Ω extends this line to larger-scale static and dynamic reconstruction. As of September 2026 the official repository exposes training code, reproduction checkpoints and data preparation material.

Primary sources:

- https://vggt-omega.github.io/
- https://github.com/facebookresearch/vggt-omega

### Clover question

The project argues that reconstruction representations can transfer to broader spatial tasks. Clover should investigate the stronger proposition:

> **Is reconstruction sufficient as the spatial substrate of a persistent robot worldview, or does understanding require additional state for observability, object identity, dynamics, causality and task relevance?**

## DUSt3R / MASt3R family

These systems replace parts of classical multi-view correspondence and reconstruction with learned point-map style representations.

Reference:

- https://arxiv.org/abs/2312.14132

The relevant lesson is not to copy their architecture, but to understand why learned correspondences can outperform or simplify hand-engineered matching in difficult imagery.

## World Labs Atlas

World Labs introduced Atlas in September 2026 as an omni world model operating over text, images, video and 3D. Its stated scope includes generation, reconstruction, simulation and robot planning. The architecture is described as a multimodal autoregressive diffusion transformer with a shared spatial context.

Primary source:

- https://www.worldlabs.ai/blog/atlas

Atlas is not a pure-vision system, but it is a strong reference for a competing thesis:

> a generative spatial context may be enough to support multiple world functions without exposing a symbolic state.

## Key separations Clover must preserve during research

### Geometry is not yet semantics

Accurate camera pose and point maps do not automatically supply object identity or type.

### Reconstruction is not yet permanence

Reconstructing what was observed is different from representing what is currently unobserved but believed to persist.

### Novel-view consistency is not yet causality

A coherent renderer may still lack intervention-sensitive dynamics.

### 3D is not automatically the only useful space

Robots may need metric geometry, topological place structure, object-relative relations and task abstractions simultaneously.

## Open questions

1. Which world queries become trivial once strong geometry is available?
2. Does a 3D reconstruction remain stable under moving/deformable objects?
3. What is the minimum persistent spatial state required beyond a learned geometry encoder?
4. How should active camera motion update uncertainty and visibility?
5. Can explicit geometry reduce planning sample complexity compared with latent-only policies?
