# 04 — What Can Vision Alone Identify?

## Question

Before designing a world model, we must separate what is identifiable from visual evidence from what remains fundamentally ambiguous without assumptions, motion or intervention.

## Geometry already teaches an important lesson

A single image does not uniquely specify the physical world. Projection discards information. Monocular geometry has scale and depth ambiguities; textureless regions, occlusion and repeated structure create additional uncertainty.

Multi-view motion changes the problem because viewpoint variation creates constraints. SfM/SLAM exploits exactly this: geometry becomes better identified from multiple observations and camera motion.

## Learned priors change inference, not observability

Modern models can infer plausible depth, object category or motion from a single view using learned regularities. This is valuable, but a learned prior is not the same as direct observation.

For Clover this distinction matters:

```text
observed evidence
learned prior
inferred state
unobserved region
```

should not be silently collapsed.

## Active vision changes what is knowable

A robot is not a passive camera. If two world hypotheses are visually indistinguishable, the system can move, change viewpoint or manipulate the scene to acquire discriminating evidence.

This makes `vision alone` compatible with information-seeking action: the sensory channel stays visual even though action changes the future observations.

## Research consequence

A world-understanding system should represent not only a best estimate but also which aspects are underdetermined by current visual evidence.

This is more fundamental than a confidence score. The machine should know *what observation would resolve the ambiguity*.

## Clover implication

The future Clover state should distinguish at least conceptually:

- directly observed;
- geometrically constrained;
- prior-inferred;
- currently unobserved;
- ambiguous among multiple hypotheses.

Whether these become explicit fields or remain distributed is still open.

## Primary sources

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- DUSt3R: https://arxiv.org/abs/2312.14132
- Active Perception overview roots: Ruzena Bajcsy, "Active Perception" (1988), DOI landing page: https://doi.org/10.1109/34.8800
