# Stage-1 Re-audit Summary — 2026-10-15

This note records the **second-pass audit** triggered by recent EmbodiedJev / AgentRSI / embodied-JEPA / recursive-self-improvement developments and a fresh arXiv/GitHub scan across computer vision, embodied intelligence, physical intelligence, frontier foundation-model engineering and performance optimization.

It supersedes the assumption that the earlier `STAGE1_FINAL_AUDIT_2026-10-15.md` was the last search pass. It does **not** change Clover's seven-stage lifecycle.

Detailed audits:

- [`JEPA_RSI_RUNTIME_2026-10-15.md`](JEPA_RSI_RUNTIME_2026-10-15.md)
- [`CV_EMBODIMENT_SYSTEMS_2026-10-15.md`](CV_EMBODIMENT_SYSTEMS_2026-10-15.md)
- [`REPRESENTATION_DIAGNOSTICS_2026-10-15.md`](REPRESENTATION_DIAGNOSTICS_2026-10-15.md)

---

## Re-audit conclusion

No missing foundational domain comparable to geometry, memory, causality, identifiability, world-state representation, training or deployment was found.

However, several **fast-moving cross-boundary method families** were underweighted and are now first-class comparison axes:

```text
1  embodied JEPA / latent predictive control
2  cross-embodiment latent action representations
3  test-time policy scaling: verifier / Best-of-N / search
4  WAM inference-state reuse, verification and staleness
5  fast-weight / retrieval / gradient / verifier forms of test-time adaptation
6  recursive self-improvement of model / harness / data / research process
7  embodied recursive improvement / Real2Sim2Real policy refinement
8  process-level RSI evaluation, held-out transfer and lineage
9  generative video foundation models used as perception representations
10 multi-view geometry-aware world modeling
11 morphology-conditioned world models / body schema
12 affordance foundation models / functionality representations
13 alternative visual-sensing boundary such as event cameras
14 mechanistic / causal representation diagnostics
15 manipulation-video continued pretraining as part of WAM design
16 multi-robot edge serving / SLO scheduling
17 explicit state + reusable code policy as a counter-hypothesis to always-on VLA/WAM
```

These belong to existing Stage-1 surfaces. They do not require new lifecycle stages.

---

## High-value current sources added in this pass

### Embodied JEPA / latent dynamics

- RoboJEPA — https://arxiv.org/abs/2610.10515 · https://github.com/facebookresearch/robo_jepa
- ThinkJEPA — https://arxiv.org/abs/2603.22281
- Demo-JEPA — https://arxiv.org/abs/2605.20811
- LeapBot-WA — https://arxiv.org/abs/2607.23969
- SkyJEPA — https://arxiv.org/abs/2606.23444
- Vision-Predictor-Action — https://arxiv.org/abs/2610.15556
- LeWAM (end-to-end JEPA/action) — https://arxiv.org/abs/2610.12818
- LeWAM (diffusion-steering MPC) — https://arxiv.org/abs/2610.12407

The two different `LeWAM` papers are a concrete reason to identify methods by exact title + arXiv ID + authors/version rather than acronym alone.

### Embodiment / action / body

- LAC-WM — https://arxiv.org/abs/2610.10846
- morphology-conditioned quadrupedal world model — https://arxiv.org/abs/2604.08780
- diffusion body-schema learning under actuator/body faults — https://arxiv.org/abs/2608.01029
- AFUN affordance foundation model — https://arxiv.org/abs/2606.02551

### Test-time adaptation / runtime

- DiVeR — https://arxiv.org/abs/2610.04933
- RoboTTT — https://arxiv.org/abs/2607.15275
- RA-VLA — https://arxiv.org/abs/2608.25585
- MARS — https://arxiv.org/abs/2610.17141 · https://github.com/PKU-VaLuE-Lab/MARS
- Δ Flow Matching — https://arxiv.org/abs/2610.15794
- WAMachine — https://arxiv.org/abs/2609.34608
- AsyncVLA — https://arxiv.org/abs/2602.13476
- Efficient VLA serving / Robion — https://arxiv.org/abs/2609.12075

### World-model / visual-representation boundaries

- Thinker-WM — https://arxiv.org/abs/2610.18447
- EVEWorld — https://arxiv.org/abs/2610.03374
- RLHND — https://arxiv.org/abs/2610.09455
- PAIWorld — https://arxiv.org/abs/2606.18375
- Video Prediction Policy 2 — https://arxiv.org/abs/2610.10270
- EventCV — https://arxiv.org/abs/2609.21330

### Recursive self-improvement

- AIDE² — https://arxiv.org/abs/2609.26457
- RRSI — https://arxiv.org/abs/2609.24972 · https://github.com/google-research/rrsi
- RSI-Master — https://arxiv.org/abs/2609.35561
- RSI-Forge — https://arxiv.org/abs/2610.09426
- RSIGym — https://arxiv.org/abs/2610.10310
- HELIX — https://arxiv.org/abs/2608.13951
- Harmony Harness — https://arxiv.org/abs/2610.15150
- Harness² — https://arxiv.org/abs/2610.14224
- AReaL-RSI — https://arxiv.org/abs/2610.18083
- EmbodiRSI — https://arxiv.org/abs/2609.38905
- RegenHarness — https://arxiv.org/abs/2609.27612
- Embodied Turing Machines / COAP — https://arxiv.org/abs/2610.12369

---

## GitHub projects classified separately from primary papers

### EmbodiedJev / 行知

https://github.com/FBddcz/embodied-jev

Classification: `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`.

Useful for:

```text
MuJoCo + Franka local workbench
Mac/local API experiments
controlled same-task model comparison
trajectory export/replay
pre-execution simulation checks
EV1 / EV6 validation workflow ideas
```

Do not attribute controller-provided candidates, geometry or safety checks to the model itself.

### AgentRSI

https://github.com/heng526/AgentRSI

Classification: `COMMUNITY_RESEARCH_REPOSITORY`.

Useful for:

```text
RSI literature / reproduction organization
append-only ResearchOps evidence records
robot scoring reports
research ledger / reducer workflow ideas
```

Do not treat repository organization as primary scientific evidence for an RSI method.

---

## New non-negotiable distinctions

```text
probe recoverability ≠ causal use ≠ closed-loop physical consequence
base VLA ≠ VLA + verifier/search/test-time compute
cross-embodiment state alignment ≠ cross-embodiment action alignment
history in KV/context ≠ explicit memory ≠ fast-weight memory
inference-state reuse ≠ inference-state validity
fast-path + slow-path ≠ synchronized closed-loop system
self-editing ≠ recursive self-improvement
RSI evolve-set gain ≠ held-out/OOD improvement
model RSI ≠ harness RSI ≠ data RSI ≠ research-process RSI ≠ embodied RSI
frame RGB ≠ all possible visual sensing
world dynamics ≠ robot morphology/body dynamics
object semantics ≠ affordance/function
single-robot latency ≠ fleet edge-serving SLO reliability
method acronym/name ≠ stable artifact identity
```

---

## DeepSeek / Qwen status in this re-audit

No newly verified DeepSeek/Qwen release in this pass requires replacing the current stable watch in:

- [`../foundation_models/DEEPSEEK_QWEN.md`](../foundation_models/DEEPSEEK_QWEN.md)
- [`../foundation_models/DEEPSEEK_QWEN_CURRENT_2026-10-15.md`](../foundation_models/DEEPSEEK_QWEN_CURRENT_2026-10-15.md)

The new RSI/runtime evidence **strengthens**, rather than replaces, the existing model-systems rule:

```text
checkpoint
+
post-training
+
runtime/kernel
+
harness/tools/memory
+
test-time compute
+
hardware / serving topology
→ observed system capability
```

For DeepSeek/Qwen comparisons, continue recording the exact API/checkpoint, reasoning-effort setting, harness/plugin configuration, external memory/tools and artifact date.

---

## Stage-1 status after the re-audit

Stage 1 remains **coverage-sufficient but freshness-active**.

Recommended operating mode:

```text
Stage 1: incremental frontier maintenance
Stage 2: primary method-by-method mechanism analysis
```

Future additions should change at least one of:

```text
what information is observable
what state is represented
how state is learned / updated
how action is chosen
how uncertainty/evidence is handled
how the system is trained / adapted
how the runtime changes behavior
how claims are validated
```

Otherwise, log the work as a comparator/source rather than expanding the stable ontology.
