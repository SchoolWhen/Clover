# Learned Visual Representations

## What problem does this area solve?

Classical vision depends on variables and features chosen by humans. Self-supervised representation learning asks whether useful visual structure can emerge from large unlabeled image collections instead.

For Clover the central question is not image classification. It is:

> **What world-relevant structure is already present in generic learned visual features before temporal or action learning is added?**

## Representative work: DINOv2

DINOv2 learns general-purpose visual features without manual labels. Meta's model card describes ViT backbones whose class and patch tokens can support downstream classification, depth estimation, segmentation and retrieval with lightweight heads. The original work trained on LVD-142M images.

Primary sources:

- https://github.com/facebookresearch/dinov2
- https://arxiv.org/abs/2304.07193

### Representation

A distributed transformer feature space: global class token plus spatial patch tokens, optionally with register tokens.

### Learning signal

The released model card lists self-distillation, masked-image modeling and feature regularization components.

### What it demonstrates

A large amount of transferable visual structure can be learned without semantic labels, and useful geometry-related signals such as depth can be extracted with small downstream heads.

### What it does not demonstrate

DINOv2 by itself does not establish:

- persistent identity through long occlusion;
- a stable world state across time;
- physical dynamics;
- causal intervention reasoning;
- action-conditioned world change.

It is therefore a strong **perceptual representation baseline**, not a complete answer to Clover's question.

## Clover questions

1. Which Clover world queries are linearly or cheaply readable from a strong static visual representation?
2. Which queries fundamentally require temporal learning?
3. Does an explicit world state add information, or only make existing latent information easier to query?
4. Can a learned visual backbone preserve fine geometric detail needed for physical reasoning without task-specific supervision?
5. How much of apparent world knowledge is inherited from dataset regularities rather than physical understanding?

## Research value

This area prevents Clover from reinventing low-level feature learning unnecessarily. If modern self-supervised features already provide robust object/geometry cues, Clover's novel contribution should begin where those representations become insufficient: persistence, observability, dynamics, causal revision and action-useful world state.
