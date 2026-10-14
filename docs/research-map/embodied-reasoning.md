# Embodied Reasoning and VLA

## What problem does this area solve?

Connect visual understanding and language/knowledge to robot decisions and actions.

## Embodied reasoning

### Gemini Robotics ER 2

Google DeepMind positions ER 2 as a high-level embodied reasoning brain for physical understanding and multi-step planning.

- Overview: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/

Clover should investigate whether this kind of embodied reasoning maintains a persistent independent world model or primarily reasons within a multimodal language context.

## Vision-Language-Action

### RT-2

A landmark vision-language-to-action formulation.

- https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/

### OpenVLA

An important open baseline for modern VLA systems.

- https://github.com/openvla/openvla

### π0.5

An important open-world robot policy/generalization result.

- https://www.pi.website/blog/pi05

## Clover questions

- When does direct action mapping outperform a persistent world state?
- Which failures require explicit memory, intervention tracking or belief revision?
- Does language provide world understanding or external semantic prior knowledge?
- Can a world model improve recovery and long-horizon planning beyond a strong VLA?
