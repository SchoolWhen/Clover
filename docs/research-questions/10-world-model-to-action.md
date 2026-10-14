# 10 — Why Should a Worldview Help Action?

## Question

If a direct policy can act successfully from vision, what additional value must a persistent world model provide?

## Direct-policy evidence

RT-2 established the modern VLA framing by representing robot actions in the same token space as language outputs and transferring web-scale vision-language knowledge into control.

OpenVLA provides an open-source VLA baseline trained on large-scale robot demonstrations.

π0.5 demonstrates that heterogeneous co-training can produce long-horizon behavior and meaningful generalization to new homes.

Figure Helix 2.5 and Skild S1 provide further vendor-reported evidence that broad pretraining can yield strong real-world robot behavior without exposing a classical explicit world state.

## Hierarchical reasoning evidence

Gemini Robotics ER 2 takes a more separated approach: a high-level embodied reasoning VLM handles spatial/temporal/physical reasoning, tool orchestration and success detection, while lower-level robotic models perform control.

This resembles the motivation behind Clover's Worldview → Decision → Tool Use → Execution decomposition, but similarity of decomposition is not evidence that Clover's specific internal representation is useful.

## What an explicit worldview must earn

A persistent worldview should provide measurable gains in at least some of:

- fewer unnecessary actions;
- better recovery after unexpected world change;
- longer-horizon consistency;
- safer refusal when evidence is insufficient;
- lower planning/search cost;
- transfer across tasks without retraining perception;
- better debugging or verification.

If it does not, direct/hierarchical policy learning remains the stronger engineering answer.

## Clover implication

The final paper should not argue for Worldview philosophically. It should demonstrate that the representation improves embodied performance under controlled comparisons.

## Primary sources

- RT-2 paper: https://arxiv.org/abs/2307.15818
- RT-2 PMLR publication: https://proceedings.mlr.press/v229/zitkovich23a.html
- OpenVLA paper: https://arxiv.org/abs/2406.09246
- OpenVLA code: https://github.com/openvla/openvla
- π0.5 paper: https://arxiv.org/abs/2504.16054
- π0.5 project: https://www.pi.website/blog/pi05
- Gemini Robotics ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Figure Helix 2.5: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1: https://www.skild.ai/blogs/s1
