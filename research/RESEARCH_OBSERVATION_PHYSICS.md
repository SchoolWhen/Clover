# Stage 1 — Observation Physics and Image-Formation Limits

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a different source of ambiguity from hidden world state:

> Even when the world state is fixed, the image formation process can hide, mix, distort or erase information before the machine sees the pixels.

The central distinction is:

```text
world-state ambiguity
≠
image-formation ambiguity
≠
sensor / camera corruption
```

A machine cannot recover a physically correct world state merely by becoming a better pattern recognizer if multiple scene configurations can generate the same visual evidence or if the imaging process destroys the relevant information.

---

## 1. Minimal image-formation view

A useful Stage-1 abstraction is:

```text
O_t = Camera(
    Geometry_t,
    Material_t,
    Illumination_t,
    Viewpoint_t,
    Motion_t,
    Medium_t,
    Exposure_t,
    Sensor_t,
    Noise_t
)
```

where the RGB observation `O_t` is the result of multiple coupled physical factors.

The inverse problem is therefore not simply:

```text
pixels → geometry
```

but more generally:

```text
pixels
→ possible combinations of
  geometry + material + lighting + motion + camera/sensor state.
```

Recent inverse-rendering literature explicitly emphasizes that many distinct geometry/material/lighting combinations can explain the same image.

Current survey:

- Recent Trends in Inverse Rendering — https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70592

Useful ambiguity analysis:

- Unveiling the Ambiguity in Neural Inverse Rendering: A Parameter Compensation Analysis — https://openaccess.thecvf.com/content/CVPR2024W/NRI/html/Kouros_Unveiling_the_Ambiguity_in_Neural_Inverse_Rendering_A_Parameter_Compensation_CVPRW_2024_paper.html
- arXiv version — https://arxiv.org/abs/2404.12819
- Diffusion Posterior Illumination for Ambiguity-aware Inverse Rendering — https://arxiv.org/abs/2310.00362

Stage-1 lesson:

```text
one plausible decomposition
≠
the uniquely correct physical decomposition.
```

---

## 2. Observation-physics map

| Observation phenomenon | What changes in pixels | What may become ambiguous | Stage-1 significance |
|---|---|---|---|
| projective viewpoint | scale, foreshortening, visibility | metric size/depth, hidden geometry | classical multi-view geometry reduces but does not eliminate all ambiguity |
| occlusion | evidence disappears | existence, identity, hidden shape/state | requires memory, uncertainty and/or active view |
| illumination change | intensity/color/shadow | material vs lighting | appearance constancy is not physical-state recovery |
| cast shadow | local darkness | geometry/material/light attribution | shadow can be evidence or nuisance depending on task |
| specular reflection | view-dependent highlight/reflection | surface color, texture, normal/shape | violates simple diffuse/Lambertian assumptions |
| transparency/refraction | background rays are displaced/mixed | surface geometry, depth, occupancy | ordinary RGB-D may also fail because depth sensors can be corrupted |
| motion blur | temporal integration within exposure | correspondence, pose, object motion | fast motion can erase spatial detail before inference |
| rolling shutter | different rows captured at different times | rigid-scene geometry vs camera-motion distortion | camera model must be part of the observation model |
| exposure / HDR saturation | clipping / missing dark detail | color, texture, feature correspondence | information may be physically lost by acquisition |
| sensor noise/compression | stochastic/quantization artifacts | fine texture and correspondence | representation robustness cannot recover information that was never recorded |
| atmospheric medium | haze/rain/fog/scatter | contrast, depth, appearance | observed radiance includes medium effects, not only object properties |

This is a working map, not a complete optics textbook.

---

## 3. Geometry, material and illumination can compensate for one another

Inverse rendering is a useful foundation because it makes explicit that vision is attempting to invert a forward image-formation process.

The 2026 inverse-rendering survey organizes work around recovering:

```text
geometry
material / reflectance
illumination
```

from images, and identifies the problem as inherently ill-posed.

A bright region may be explained by, for example:

```text
bright material
strong illumination
specular reflection
surface orientation
viewpoint-dependent effect
```

or combinations of these.

The CVPR 2024 parameter-compensation analysis demonstrates that inverse-rendering systems can compensate an error in one estimated scene property by changing another scene property while still explaining the observations.

Stage-1 implication:

> Photometric reconstruction error can be low even when the recovered physical decomposition is wrong.

This directly parallels Clover's broader distinction:

```text
reconstruct the observation
≠
recover the true world state.
```

---

## 4. Transparent and refractive objects expose a hard image-formation failure

### 4.1 Trans2Occ

**Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality**  
Primary paper: https://arxiv.org/abs/2606.01777  
Evidence: `PRIMARY_PAPER`

Transparent objects are difficult because refraction and reflection can make conventional depth sensing unreliable. Trans2Occ predicts voxel occupancy from a single RGB image using large-scale synthetic supervision and transfers the representation to real robotic grasping.

Why it matters:

```text
successful occupancy prediction from RGB
```

can depend on learned shape/material priors and synthetic training distributions; it does not imply that transparent geometry is uniquely determined by the pixels.

### 4.2 SR3D

**SR3D: Unleashing Single-view 3D Reconstruction for Transparent and Specular Object Grasping**  
Primary paper: https://arxiv.org/abs/2505.24305  
Evidence: `PRIMARY_PAPER`

SR3D combines single-view reconstruction and RGB-D scene information to recover usable transparent/specular object geometry for grasping.

Protocol warning:

It is not strict RGB-only evidence because RGB-D scene input is part of the localization/reconstruction pipeline.

Stage-2 question:

> How much transparent-object geometry comes from actual visual evidence versus category/generative shape priors?

---

## 5. Specular reflection changes the meaning of appearance

### UnReflectAnything

**UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision**  
Primary paper: https://arxiv.org/abs/2512.09583  
Project: https://alberto-rota.github.io/UnReflectAnything/  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

The work treats specular highlights as corruption that can obscure texture and hinder geometry reasoning. It trains using physically motivated synthetic highlights and predicts a reflection-free diffuse reconstruction.

Stage-1 implication:

A pixel can contain information about:

```text
object reflectance
+
illumination
+
view direction
+
surface normal
```

rather than a stable intrinsic object color.

Therefore:

```text
appearance feature
≠
intrinsic material state.
```

---

## 6. Motion blur is information integration, not just image noise

**On Motion Blur and Deblurring in Visual Place Recognition**  
Primary paper: https://arxiv.org/abs/2412.07751  
Evidence: `PRIMARY_PAPER`

The work benchmarks visual place recognition under different motion-blur intensities and studies when deblurring improves localization.

Why it matters:

Motion blur is produced because a conventional frame integrates light over a nonzero exposure interval.

Conceptually:

```text
one RGB frame
≈
integral of changing scene/camera projections over exposure time.
```

Consequently, the observation is not necessarily an instantaneous world state.

Stage-1 questions:

```text
When should the world model model exposure-time integration explicitly?
How should uncertainty grow when blur destroys correspondence evidence?
Can temporal context reconstruct information lost in one frame, or only guess it from priors?
```

---

## 7. Rolling shutter means one frame may not correspond to one camera pose

**Rolling-Shutter Modelling for Direct Visual-Inertial Odometry**  
Primary paper: https://arxiv.org/abs/1911.01015  
Evidence: `BACKGROUND_REFERENCE`

Rolling-shutter cameras capture different image rows at different times. Ignoring this effect can strongly degrade geometric state estimation.

The cited method uses IMU information and therefore is not a vision-only baseline; its value here is conceptual.

Stage-1 implication:

```text
frame timestamp
```

is not always equivalent to:

```text
all pixels observed from one pose at one instant.
```

The camera acquisition process can itself create apparent nonrigid deformation in a rigid scene.

---

## 8. Low light, overexposure and illumination shifts alter observability

**Benchmarking Visual Feature Representations for LiDAR-Inertial-Visual Odometry Under Challenging Conditions**  
Primary paper: https://arxiv.org/abs/2603.18589  
Evidence: `PRIMARY_PAPER`

The paper studies low light, overexposure, illumination changes and high-parallax conditions and reports degradation/failure of ordinary photometric visual methods under severe photometric inconsistency.

Protocol warning:

The evaluated system is LiDAR-inertial-visual, so it is evidence about visual degradation and multimodal compensation, not a strict RGB-only result.

Stage-1 implication:

A general visual brain must distinguish:

```text
world changed
```

from:

```text
lighting/exposure changed.
```

Otherwise illumination variation can be mistaken for object/material/world-state change.

---

## 9. Event cameras are an informative non-RGB counterexample

**Event-based SLAM Benchmark for High-Speed Maneuvers (EvSLAM)**  
Primary paper: https://arxiv.org/abs/2604.24033  
Evidence: `PRIMARY_PAPER`

Event cameras react asynchronously to brightness changes and are studied specifically because conventional frames struggle under high-speed motion and extreme lighting.

Event cameras are outside Clover's strict RGB target.

Their Stage-1 role is diagnostic:

> When another sensing architecture is introduced specifically to avoid motion blur / dynamic-range limitations, that reveals information limitations of ordinary frame acquisition that a vision-only RGB system must either tolerate, model or express as uncertainty.

---

## 10. Observation failure and world uncertainty should not be conflated

Suppose a robot cannot determine whether an object is present.

Possible causes include:

```text
object is behind another object
image is overexposed
object is transparent
surface is mirror-like
motion blur erased the contour
camera viewpoint is insufficient
world genuinely contains two plausible hidden states
```

These should not all collapse into one generic low-confidence scalar.

A useful later Analysis taxonomy is:

```text
EPISTEMIC-WORLD uncertainty
    multiple real-world states fit the evidence

OBSERVATION uncertainty
    image-formation/acquisition process is unreliable

MODEL uncertainty
    learner is outside its competence/data distribution
```

Stage 1 does not yet prescribe how Clover should represent these categories; it records that they are different sources of uncertainty.

---

## 11. Active vision can change the observation operator

Active perception is useful not only because another viewpoint reveals an occluded object.

Changing viewpoint can also change:

```text
parallax
specular reflection
refraction path
shadow geometry
surface visibility
scale / foreshortening
```

Therefore an active agent can choose views that make an inverse problem better conditioned.

Relevant foundational/current references:

- Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Vantage code — https://github.com/q1xiangchen/Vantage

Stage-2 question:

> Can an agent learn which viewpoint specifically disambiguates geometry/material/light explanations rather than merely collecting more images?

---

## 12. Proposed Stage-2 analysis dimensions

For methods that claim world reconstruction or persistent visual understanding, later Analysis should record:

```text
camera model
exposure model
rolling/global shutter assumption
illumination assumption
reflectance/material assumption
transparent/specular handling
occlusion handling
metric-scale source
static/dynamic scene assumption
whether image formation is explicitly modeled
whether ambiguity is represented or collapsed to one estimate
whether active viewpoint selection is supported
```

A method should not receive credit for recovering physical state when the evaluation only shows photometric reconstruction under the same observation assumptions.

---

## 13. Current open questions

1. How much of modern foundation-model robustness is true image-formation invariance versus learned dataset prior?
2. Can a general RGB world model maintain multiple physically plausible inverse-rendering hypotheses rather than one generated explanation?
3. How should the system separate illumination/material change from actual object/world change?
4. Which camera effects must be modeled explicitly, and which can safely be absorbed by learned representations?
5. When does active viewpoint control resolve transparent/specular/occlusion ambiguity?
6. Can uncertainty be calibrated according to the source of missing information: world ambiguity, observation failure or model ignorance?
7. Which downstream actions are sensitive enough that image-formation ambiguity must be preserved rather than averaged away?

---

## Stage-1 provisional conclusion

The visible image is not the real world state.

More precisely:

```text
real world
→ light transport / image formation
→ camera acquisition
→ RGB pixels
→ learned representation
```

Each arrow can discard or entangle information.

Therefore a scientifically serious answer to:

> How can a machine understand the real world through vision alone?

must study not only the latent world behind the pixels, but also the **physical and computational observation operator that produced those pixels**.

**Do not treat the camera as a transparent window onto state.**
