# 12 — Why Did Classical Computer Vision Not Naturally Scale Into World Understanding?

## Question

Why did decades of CPU-era computer vision produce strong geometry, features and task-specific systems without naturally turning into the kind of broad visual intelligence now associated with large learned models?

This question matters because Clover originally treated CPU-first computation as a major prior. Hardware history alone does not explain the scientific transition.

## 1. Classical vision solved important invariance and geometry problems

SIFT engineered local features robust to scale, rotation and a meaningful range of viewpoint/illumination change. HOG engineered gradient statistics that were highly effective for human detection. SfM/SLAM developed explicit geometric estimation for cameras, maps and motion.

These methods were not primitive failures. Many remain mathematically strong baselines.

The limitation was usually the *scope of representation*: the designer chose what information should be represented and which task it should solve.

## 2. The deep-learning transition changed representation learning

AlexNet's 2012 ImageNet result is historically important for two linked reasons:

- a deep CNN learned hierarchical visual features from large labeled data rather than relying primarily on hand-designed descriptors;
- GPU implementation made training a 60M-parameter convolutional model on ImageNet practical enough to demonstrate the scaling advantage.

The scientific shift was therefore not simply `GPU > CPU`. It was:

```text
learned hierarchical representation
+ large data
+ scalable optimization
+ hardware able to execute the training
```

## 3. Architecture made scale usable

ResNet addressed optimization barriers that made very deep networks difficult to train. Vision Transformers later showed that, with large-scale pretraining, a comparatively generic attention architecture could compete with or exceed convolution-specific inductive biases.

The trend is important for Clover: architectures that look inefficient or under-constrained at small scale can become powerful once data, optimization and compute expose a better scaling regime.

## 4. Supervision broadened

ImageNet classification still learned a fixed label space. Later systems broadened supervision:

- CLIP used hundreds of millions of image-text pairs to create transferable visual-language representations;
- DINOv2 demonstrated strong transferable image features with self-supervision;
- V-JEPA 2/2.1 moves the learning signal into video prediction and temporal structure.

This progression reduces dependence on manually enumerated visual concepts.

## 5. What classical methods still do better conceptually

Modern learned systems do not invalidate classical insights. Geometry provides exact structure and identifiable variables when its assumptions hold. Bayesian filtering and POMDP theory distinguish state, belief, observation and action more clearly than many end-to-end networks. These distinctions may still be necessary in a general robot brain.

The research opportunity is therefore not to return to old CPU CV or to accept end-to-end scaling uncritically.

It is to ask:

> **Which structures should remain explicit because mathematics already characterizes them, and which structures should be learned because hand-designed representations fail to scale to open-ended visual experience?**

## 6. Hardware should follow the computation

The history suggests a co-design conclusion:

- GPUs won many deep-learning workloads because dense tensor operations parallelize extremely well;
- CPUs remain strong for irregular, sparse, branching and control-heavy computation;
- Apple Silicon unified memory makes heterogeneous CPU/GPU execution especially interesting for a future Clover implementation;
- but none of these hardware facts decide the representation scientifically.

## Clover implication

Clover should avoid two symmetric mistakes:

1. **nostalgia error** — assuming classical/CPU methods are more principled and therefore sufficient;
2. **scaling error** — assuming larger learned models automatically constitute world understanding.

The next Clover architecture should inherit mathematical structure where it is genuinely known and use learning where the world is too open-ended to hand-code.

## Primary sources

- SIFT — David Lowe, *Distinctive Image Features from Scale-Invariant Keypoints* (IJCV 2004): https://doi.org/10.1023/B:VISI.0000029664.99615.94
- SIFT author-hosted PDF: https://www-inst.eecs.berkeley.edu/~ee225b/sp11/readings/sift-lowe.pdf
- HOG — Dalal & Triggs, CVPR 2005: https://doi.org/10.1109/CVPR.2005.177
- AlexNet — Krizhevsky, Sutskever & Hinton, NeurIPS 2012: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- AlexNet PDF: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet: https://arxiv.org/abs/1512.03385
- Vision Transformer: https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020
- DINOv2: https://arxiv.org/abs/2304.07193
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
