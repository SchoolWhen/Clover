# Robot Foundation Models

## Core question

> **Can sufficiently broad physical experience produce a general-purpose robot brain without first committing to an explicit human-designed world representation?**

This research family is especially important because it measures success in real embodied behavior rather than only perception benchmarks.

## Figure Helix 2.5

Figure reports that Helix 2.5 was pretrained on its Index dataset of human behavior and evaluated zero-shot across 30 unseen homes on three long-horizon whole-body behaviors. Figure reports no data collection, fine-tuning or adaptation in those evaluation homes, and an ablation in which Index pretraining increased full-task success from 9% to 56% while task-specific data and training conditions were held fixed.

Primary source:

- https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

### Evidence status

This is a company-reported real-robot result rather than an independently reproduced open benchmark result. It is still highly relevant as a capability target.

### Clover lesson

Broad human-experience pretraining can materially improve transfer to unseen physical environments. Any Clover theory that relies mostly on hand-designed physical rules must explain how it will acquire the enormous diversity of everyday visual/behavioral regularities seen in such data.

## Skild Brain and S1

Skild frames its goal as an omni-bodied general-purpose robotic brain. Its public technical material describes hierarchical high/low-level policies trained across simulation, internet/human video, teleoperation and robot data.

S1 (August 2026) is presented as an in-context robot model: a video demonstration specifies a task, and the model adapts behavior from context. Skild reports recovery and task transfer under distribution shifts and examples of common-sense substitution behavior.

Primary sources:

- https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- https://www.skild.ai/blogs/s1
- https://skild.ai/blogs/learning-by-watching

### Physical self-play

In September 2026 Skild reported a self-play post-training system in simulation for humanoid soccer, followed by transfer to a physical robot. The important idea is not soccer itself: it is that robot intelligence may need self-generated interaction experience in addition to human demonstrations.

Source:

- https://skild.ai/blogs/physical-self-play

## Data-scale lesson

Modern robot foundation models increasingly combine:

```text
human video
+ robot demonstrations
+ teleoperation
+ simulation
+ cross-embodiment experience
+ self-generated interaction
```

This suggests that the learning problem for a general robot brain is not equivalent to fitting a single perception dataset.

## Open questions for Clover

1. Which abilities reported by these systems come from visual world representation versus action-policy scale?
2. Can a persistent worldview improve data efficiency or recovery compared with pure policy scaling?
3. How much can human video contribute when human and robot embodiments differ?
4. Does cross-embodiment training force the model to learn more abstract physical structure?
5. Which capabilities truly require interaction and self-play rather than observation?
6. How should a vision-only scientific claim be isolated inside a robot brain that may use language and proprioceptive/action information elsewhere?
