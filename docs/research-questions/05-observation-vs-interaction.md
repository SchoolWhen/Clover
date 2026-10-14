# 05 — What Requires Interaction?

## Question

How much world understanding can be learned from passive visual observation, and what knowledge requires acting in the world?

## Evidence from passive video

V-JEPA 2 is a major data point. It pretrains on more than one million hours of image/video data without actions and obtains strong motion/action understanding. This shows that a large amount of physical regularity is available from observation alone.

But robot planning is introduced by post-training an action-conditioned model with robot trajectory videos. That separation is scientifically useful: it suggests passive observation can build a broad visual prior while interaction teaches controllable transitions.

## Evidence from robot foundation models

π0.5 combines robot trajectories with web/multimodal knowledge, object detections and hierarchical semantic targets. Figure Helix 2.5 reports improved unseen-home generalization after pretraining on large-scale human behavior data. Skild reports combining human video, robot data, simulation and other physical experience.

These systems do not isolate a single causal factor, but collectively they suggest that broad physical competence benefits from heterogeneous experience.

## What interaction uniquely provides

Observation can reveal correlation and natural dynamics. Intervention gives stronger information about:

- controllability;
- action-conditioned transitions;
- object affordance;
- latent physical properties exposed by contact;
- causal direction under deliberate perturbation.

## Clover implication

The scientific question should be split:

1. What world structure can be acquired from vision-only observation?
2. What additional structure becomes identifiable when the agent acts but still receives only visual sensory evidence?

This preserves the vision-only SSOT while allowing embodied learning.

## Primary sources

- V-JEPA 2 paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 project/code: https://github.com/facebookresearch/vjepa2
- π0.5 paper: https://arxiv.org/abs/2504.16054
- π0.5 project: https://www.pi.website/blog/pi05
- Figure Helix 2.5 official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 official report: https://www.skild.ai/blogs/s1
- Skild Physical Self-Play: https://skild.ai/blogs/physical-self-play
