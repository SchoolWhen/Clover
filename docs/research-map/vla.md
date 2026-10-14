# Vision-Language-Action Models

## Core question

> **How far can a model go by mapping observations and instructions directly to actions without exposing a persistent explicit world model?**

VLA systems are a critical counter-hypothesis to Clover. If sufficiently strong VLA policies can generalize, recover and act in unfamiliar physical settings, Clover must show what additional value a persistent worldview provides.

## RT-2

RT-2 helped establish the VLA framing: web-scale vision-language knowledge is adapted to robotic control by representing robot actions within the model's token/action interface.

Primary source:

- https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/

## OpenVLA

OpenVLA is an open-source 7B vision-language-action model and ecosystem for robotic manipulation. The repository exposes pretrained models, fine-tuning and evaluation tooling; subsequent updates include faster fine-tuning/inference recipes.

Primary source:

- https://github.com/openvla/openvla
- https://arxiv.org/abs/2406.09246

OpenVLA is especially valuable to Clover because it is a public, inspectable representative of the VLA paradigm rather than a closed demo.

## π0.5

Physical Intelligence describes π0.5 as a VLA for open-world generalization. Its training combines robot data, web/multimodal data, object detections, semantic subtask prediction and low-level actions. It uses the same model for high-level textual actions and lower-level continuous motor commands, and reports long-horizon tasks in homes excluded from training.

Primary source:

- https://www.pi.website/blog/pi05
- https://www.pi.website/download/pi05.pdf

### Why π0.5 matters

It is a strong challenge to the proposition that a separately exposed world representation is necessary for generalization. A learned policy can acquire substantial semantic and behavioral structure by co-training across data sources and abstraction levels.

### But it is not a pure-vision comparison

Language, object detections, web data and robot actions are part of the training/interface. Its results therefore should not be interpreted as evidence that vision alone is sufficient.

## What VLAs demonstrate

- large multimodal priors can transfer into robot control;
- cross-embodiment and multi-environment data improve generalization;
- hierarchical behavior can emerge inside one trained model;
- long-horizon real-world manipulation is possible without an externally exposed symbolic world state.

## What remains a Clover research question

- Does an explicit persistent worldview improve recovery when the environment changes unexpectedly?
- Can it reduce data requirements by reusing geometric/physical structure?
- Can it provide reliable unknown/unobserved semantics?
- Can it support counterfactual planning and audit without regenerating latent reasoning each time?
- Can it make long tasks computationally cheaper by maintaining reusable world state?

## Fair future comparison

Clover should eventually compare against strong VLA systems on **shared embodied tasks**, not merely on internal representation quality. The key test is whether explicit world understanding yields measurable capability or efficiency advantages.
