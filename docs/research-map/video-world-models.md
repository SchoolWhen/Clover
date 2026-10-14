# Video Representation and World Models

## Core question

> **Can a machine learn useful physical world structure largely by observing video, and what representation emerges when it does?**

This is one of the closest modern research families to Clover's SSOT.

## V-JEPA 2

Meta describes V-JEPA 2 as a self-supervised video model for understanding, prediction and planning. It is pretrained action-free on more than one million hours of internet video. Meta reports strong motion understanding and action anticipation results, then post-trains an action-conditioned model (V-JEPA 2-AC) with a much smaller amount of robot trajectory data for robot planning.

Primary sources:

- https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- https://github.com/facebookresearch/vjepa2
- https://arxiv.org/abs/2506.09985

### Representation

A learned latent video representation. JEPA-style training predicts representations rather than reconstructing raw pixels.

### Scientific importance for Clover

V-JEPA 2 directly challenges the assumption that world understanding needs a hand-designed explicit world language. It asks whether prediction in latent space can induce enough temporal and physical structure for planning.

### Observation versus interaction

The separation between very large action-free video pretraining and comparatively limited robot interaction data creates a useful research question:

> What physical regularities can be learned from passive observation, and what only becomes identifiable through action?

Clover should treat this as a first-class theoretical question rather than assuming either passive video or interaction is sufficient.

## V-JEPA 2.1

The official repository states that V-JEPA 2.1 focuses on high-quality, temporally consistent dense features. Its training recipe adds dense predictive loss, deep self-supervision, image/video tokenization and scaling.

Primary source:

- https://github.com/facebookresearch/vjepa2
- https://arxiv.org/abs/2603.14482

For Clover, the key issue is whether dense temporal consistency can provide a stronger substrate for identity, motion, boundary persistence and world-state formation than global video representations alone.

## Mechanistic interpretation: physics in video world models

Meta's 2026 work **Interpreting Physics in Video World Models** studies how physical variables are represented inside video encoders. The reported finding that some variables become increasingly linearly accessible while other structure is distributed across high-dimensional populations is an important counterexample to a naive explicit-variable assumption.

Source:

- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### Clover consequence

The research question is no longer:

> Can we design a compact set of explicit variables?

It is:

> **When does explicit state improve generalization, causal revision, queryability and control over a distributed representation, and when does it discard useful information?**

## World-model taxonomy relevant to Clover

Video/world models can serve different roles:

- **encoder** — produce representations;
- **predictor** — predict future latent state;
- **renderer/generator** — generate observations;
- **simulator** — roll a world forward under conditions/actions;
- **planner substrate** — score or search action consequences.

A system should not be called a complete world model merely because it performs one of these functions.

## What this family has demonstrated

- large-scale video SSL can learn strong temporal/motion representations;
- latent predictive models can support downstream robot planning after action conditioning;
- temporal consistency can be learned densely rather than only at a global clip level;
- physical variables can be present in representations without explicit hand-designed state variables.

## What remains unresolved for Clover

- persistent object identity beyond the video context window;
- explicit distinction between unobserved, unknown and absent;
- belief revision after contradictory evidence;
- long-term world memory;
- causal identification rather than predictive correlation;
- whether latent prediction helps real robot recovery under unexpected world changes;
- whether language alignment imports non-visual knowledge into a supposedly visual understanding evaluation.
