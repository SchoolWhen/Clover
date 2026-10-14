# Embodied Reasoning

## Core question

> **Can a large multimodal reasoning model function as the high-level brain of a robot, and if it can, what is left for a dedicated worldview model to contribute?**

## Gemini Robotics ER 2

Google DeepMind describes Gemini Robotics ER 2 as an embodied reasoning VLM and a 'high-level brain for robots'. Its official model card states that it is based on Gemini 3.5 Flash and accepts text, image, video and audio inputs. The product page describes physical-world understanding, multi-step planning and handoff of motor execution to a lower-level VLA.

Primary sources:

- https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- https://deepmind.google/models/model-cards/gemini-robotics-er-2/

## Why this matters to Clover

At the system level, this resembles part of Clover's high-level decomposition:

```text
perception / reasoning
        ↓
high-level plan
        ↓
lower-level action model
```

But the scientific basis is different. ER 2 is a multimodal VLM, so its physical reasoning can potentially draw on language and large-scale multimodal pretraining rather than only visual evidence.

## The crucial confound: visual evidence vs language knowledge

For Clover's SSOT, we must distinguish:

```text
world knowledge inferred from the current visual stream
```

from:

```text
prior semantic/physical knowledge imported by text-language pretraining
```

A model can answer a physical question correctly without constructing a persistent world state from current evidence.

## Questions to investigate later

1. Does the system maintain persistent identity when an object leaves view?
2. Can it distinguish unobserved from absent without language priors filling gaps?
3. How does it update after unexpected physical change?
4. Can it expose or query a stable world state across a long task?
5. How much of its physical reasoning remains under a strict vision-only protocol?
6. Does high-level reasoning reduce failures compared with the same lower-level VLA alone?

## Implication

Clover should not compete by claiming that language reasoning is 'not real understanding'. It should define a stricter visual-evidence protocol and demonstrate which world capabilities require persistent visual grounding beyond generic multimodal reasoning.
