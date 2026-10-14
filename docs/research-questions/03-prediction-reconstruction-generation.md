# 03 — Prediction vs Reconstruction vs Generation

## Question

Which learning objective best creates a representation useful for understanding a persistent physical world?

## Reconstruction

Classical multi-view geometry and modern models such as DUSt3R, VGGT and VGGT-Ω ask the system to recover spatial structure from visual observations.

Reconstruction strongly constrains geometry because multiple views must agree on cameras, depth or point structure.

What it does not guarantee: understanding dynamics, causality, object purpose or task relevance.

## Prediction

V-JEPA 2 predicts in representation space rather than directly generating pixels. The key idea is that useful latent structure can be learned by predicting missing/future representations while avoiding the burden of modeling every pixel detail.

V-JEPA 2.1 strengthens dense and temporal grounding with dense predictive loss, deep self-supervision and unified image/video training.

Prediction provides a natural test of temporal regularity, but prediction accuracy alone does not establish causal understanding.

## Generation / simulation

NeRF and 3D Gaussian Splatting show how visual observations can parameterize scenes for novel-view rendering. Atlas and Cosmos 3 go further toward learned world generation and simulation.

Generation can demonstrate rich spatial/temporal coherence, but photorealistic output can still be wrong at the state or action level.

## Planning-oriented latent world models

PlaNet, DreamerV3 and TD-MPC2 demonstrate another criterion: a world model can be useful even if it is optimized primarily to support control in latent space rather than reconstructing a human-readable world.

This creates a central Clover tension:

> Is the best representation the one that reconstructs reality most faithfully, predicts future representations most accurately, or supports decisions most efficiently?

## Current synthesis

These objectives supervise different invariants:

- reconstruction → spatial consistency;
- prediction → temporal/statistical consistency;
- generation → distributional/world continuation;
- control/world-action learning → action-relevant dynamics.

A future Clover objective may need a combination, but combining losses without a principled reason would be framework stacking. The research task is to identify which invariant is necessary for which capability.

## Primary sources

- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- NeRF: https://arxiv.org/abs/2003.08934
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- Cosmos 3: https://arxiv.org/abs/2606.02800
- DreamerV3: https://arxiv.org/abs/2301.04104
- TD-MPC2: https://arxiv.org/abs/2310.16828
