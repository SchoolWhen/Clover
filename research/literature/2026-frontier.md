# 2026 Frontier Watch — Physical World Models and Embodied Intelligence

Last updated: 2026-10-14

This note tracks 2026 work that materially changes the research landscape around Clover's SSOT. It is not a module shopping list. Each item is included because it sharpens a research contradiction.

## 1. Cosmos 3 — omnimodal world model

**Paper:** https://arxiv.org/abs/2606.02800  
**Project:** https://research.nvidia.com/labs/cosmos-lab/cosmos3  
**Code:** https://github.com/nvidia/cosmos

Cosmos 3 jointly processes/generates language, image, video, audio and action sequences in one mixture-of-transformers family. Its relevance to Clover is conceptual: the boundary between `world model`, `VLM`, `simulator` and `policy backbone` is becoming less clean.

### Research tension

If one model can jointly represent observation and action distributions, does a separately materialized worldview still provide unique value? Clover eventually has to answer this with persistence, revision, causal/action utility or efficiency evidence — not by architectural preference.

---

## 2. RoboPhys-3D — world-model evaluation grounded in 3D state and execution

**Paper:** https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates embodied video world models using a shared 3D reconstruction pipeline and separates pixel fidelity, 3D consistency, state understanding and task completeness. Its key message for Clover is methodological: perceptual or VLM judgments can miss failures that become obvious when evaluated against reconstructed state and executable task outcomes.

### Research tension

A world model should not be accepted because its generated video looks plausible. Evaluation must reach state and action consequences.

This directly supports Clover's multi-level Understanding Battery.

---

## 3. Hy-Embodied-VLM-1.0 — action-centric physical-world reasoning taxonomy

**Paper:** https://arxiv.org/abs/2607.12894

The work organizes embodied capability into three progressive dimensions:

1. action-relevant state understanding;
2. action-transition reasoning;
3. sequential and adaptive reasoning.

### Research tension

This is useful because it connects perception to action without collapsing them into one accuracy number. Clover can compare its own future capability taxonomy against this decomposition while retaining its stronger vision-only causal-attribution requirement.

---

## 4. RBench / RoVid-X — evaluate physical realism of robot video generation

**Paper:** https://arxiv.org/abs/2601.15282

RBench evaluates robot-oriented video generation across multiple tasks/embodiments with metrics for structural consistency, physical plausibility and action completeness. RoVid-X provides a large open robotic video-generation dataset.

### Research tension

Video generation is becoming an embodied data engine, but generative quality and world understanding are not interchangeable. Clover should track which evaluation dimensions correlate with actual executable state correctness.

---

## 5. ABot-PhysWorld — physics-aligned interactive video world model

**Paper:** https://arxiv.org/abs/2603.23376

ABot-PhysWorld targets a known failure of generic video generation: visually plausible but physically impossible robot interactions such as penetration or anti-gravity motion. It adds physics-aware data/post-training and an action-control mechanism.

### Research tension

This supports a central question for Clover: should physical structure be encoded in the representation/transition model itself, or corrected statistically during post-training? These are different scientific hypotheses.

---

## 6. Xiaomi-Robotics-U0 — world foundation models as embodied data engines

**Paper:** https://arxiv.org/abs/2607.11643  
**Project/code:** https://robotics.xiaomi.com/xiaomi-robotics-u0.html

U0 treats embodied synthesis as an extension of large image/video generation and targets multi-view consistency, embodiment transfer and robot-video generation.

### Research tension

This is another route where `world model` primarily acts as a scalable data/simulation engine rather than an explicit persistent robot worldview. Clover should keep these roles distinct when comparing approaches.

---

## 7. Figure Helix 2.5 — unseen-home real-robot generalization

**Official reported result:** https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Figure reports zero-shot whole-body behavior in 30 unseen homes after pretraining on its Index human-behavior dataset.

### Evidence label

**Official company-reported real-robot result.** No independent reproduction is implied here.

### Research tension

Large-scale human behavior experience may provide a strong prior for physical generalization without exposing an explicit world state. This is a direct challenge to any claim that explicit representation is inherently necessary.

---

## 8. Skild S1 / Physical Self-Play — broad experience and self-generated interaction

**S1 official report:** https://www.skild.ai/blogs/s1  
**Physical Self-Play:** https://skild.ai/blogs/physical-self-play

Skild represents the hypothesis that broad robot competence can emerge from heterogeneous physical experience plus in-context specification, with self-play extending experience beyond imitation.

### Evidence label

**Official company-reported results.** Treat capability claims as reported until independent evidence exists.

### Research tension

The learning problem may be as important as the representation problem: passive visual observation, demonstrations, simulation and self-generated interventions provide different information.

---

# Cross-cutting conclusion

The 2026 frontier increasingly separates into four roles that are often all called `world model`:

1. **representation model** — extract state/features from observation;
2. **predictive dynamics model** — forecast latent/state transitions;
3. **generative simulator/data engine** — synthesize plausible futures or training data;
4. **decision-coupled model** — directly support planning/action.

Clover should not use the term `world model` without specifying which role is meant.

The strongest open question remains:

> **What internal structure is necessary for a robot to maintain, revise and use an understanding of the real world from visual evidence — and which apparent capabilities can instead be obtained from large distributed models without such explicit structure?**
