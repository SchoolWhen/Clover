# 08 — What Is Physical Understanding?

## Question

What evidence is sufficient to say a machine understands physical behavior rather than recognizing visual patterns correlated with it?

## Levels of evidence

### Level 1 — visual regularity

The model distinguishes common from unusual motion or appearance.

### Level 2 — violation of expectation

Benchmarks such as IntPhys 2 test principles including permanence, immutability, spatiotemporal continuity and solidity.

### Level 3 — state-variable accessibility

A representation makes quantities such as motion, depth or trajectories reliably decodable.

### Level 4 — intervention stability

The model predicts how outcomes change under controlled interventions.

### Level 5 — action usefulness

Physical knowledge improves planning and recovery in real or simulated interaction.

The higher levels are stronger evidence than benchmark recognition alone.

## Why shortcut controls matter

MVPBench uses minimal video pairs to reduce the chance that a model succeeds from superficial cues. This experimental idea is important for Clover: if the intended physical distinction can be solved by background or static-frame shortcuts, the result is weak evidence of understanding.

## Modern world models

V-JEPA 2 reports strong motion/action understanding and planning after action-conditioned post-training. Cosmos 3 combines multimodal understanding, world generation and action generation. New embodied-world-model evaluations such as RoboPhys-3D explicitly argue that perceptual realism can disagree with state- and execution-grounded correctness.

## Clover implication

Clover should eventually claim physical understanding only when evidence spans controlled diagnostics, counterfactual/intervention tests and downstream action.

## Primary sources

- IntPhys 2 official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVPBench official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- Cosmos 3: https://arxiv.org/abs/2606.02800
- RoboPhys-3D: https://arxiv.org/abs/2608.28718
