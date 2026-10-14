# Clover Status

Last updated: **2026-10-15**  
Stage-1 freshness checked through: **2026-10-15**

## Research question

> **How can a machine understand the real world through vision alone?**

## Long-term goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

Immediate objective: **coverage before commitment**. No Clover core representation or algorithm is frozen.

## Read first

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)
9. [`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md)
10. [`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)
11. [`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md)
12. [`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md)
14. [`research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)
15. [`research/RESEARCH_TRAINING_POSTTRAINING.md`](research/RESEARCH_TRAINING_POSTTRAINING.md)
16. [`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md)
17. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
18. [`research/README.md`](research/README.md)

Supporting watches:

- [`research/foundation_models/DEEPSEEK_QWEN.md`](research/foundation_models/DEEPSEEK_QWEN.md)
- [`research/engineering/DEPLOYMENT_LIFECYCLE.md`](research/engineering/DEPLOYMENT_LIFECYCLE.md)
- [`research/engineering/VALIDATION_RESOURCES.md`](research/engineering/VALIDATION_RESOURCES.md)

## Current Stage-1 surfaces

```text
1  broad research inventory
2  world-state variables
3  identifiability / information limits
4  observation physics
5  hidden physical properties / irreversible change
6  minimum sufficient world state
7  state aliasing / representation failure
8  adaptive abstraction / state granularity
9  value of information / probing actions
10 open-world epistemics / model mismatch / epistemic safety
11 model discovery / experiment design / falsification / provenance
12 foundation-model architecture / multimodal / data / inference systems
13 training / post-training / embodied learning regimes
14 engineering / edge deployment / simulation / validation
15 current frontier
```

## Newly added surface: training and post-training

[`research/RESEARCH_TRAINING_POSTTRAINING.md`](research/RESEARCH_TRAINING_POSTTRAINING.md) makes training procedure a first-class research variable rather than an implementation footnote.

It tracks:

```text
TR0  base pretraining
TR1  continued/domain pretraining
TR2  SFT / behavior cloning
TR3  co-training / auxiliary objectives
TR4  preference / conservative offline alignment
TR5  verifier/reward RL
TR6  online embodied RL
TR7  on-policy distillation
TR8  strong-to-weak distillation
TR9  simulated/world-model post-training
TR10 deployment-rollout/self-improvement
TR11 continual/test-time adaptation
```

Central rule:

```text
architecture
× data
× objective
× update scope
× interaction regime
× runtime
→ observed capability
```

Do not attribute a result to architecture alone when training recipe changed.

### Why robot post-training is not simply LLM post-training

Language-model outputs are tokens. Robot-policy outputs alter the physical world and therefore change future observations and reachable states.

Robot post-training must additionally handle:

```text
covariate shift
continuous / multimodal actions
control frequency and latency
embodiment-specific semantics
expensive or impossible resets
sparse / delayed rewards
contact dynamics
safety / irreversibility
sim2real mismatch
operator / demonstration quality
```

So:

```text
LLM SFT → RL
≠ directly reusable robot recipe
```

### Current high-value training references

- DeepSeek-R1 — https://arxiv.org/abs/2501.12948
- DeepSeek-V4.1-Flash — https://www.deepseek.com/en/news/deepseek-v4-1-flash/
- Qwen3 — https://qwenlm.github.io/blog/qwen3/
- Qwen3-VL — https://arxiv.org/abs/2511.21631
- Text-Centric Post-Training for Omni-Modal Reasoning — https://arxiv.org/abs/2610.02819
- OpenVLA-OFT — https://arxiv.org/abs/2502.19645
- π0 / π0.5 — https://www.physicalintelligence.company/download/pi0.pdf · https://www.physicalintelligence.company/download/pi05.pdf
- Qwen-RobotManip — https://arxiv.org/abs/2606.17846
- VLAFlow — https://arxiv.org/abs/2607.01586
- VLA-OPD — https://arxiv.org/abs/2603.26666
- TEMPO — https://arxiv.org/abs/2608.07314
- RehearseVLA — https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html
- LoopWAM — https://arxiv.org/abs/2610.18873

## Foundation-model systems / DeepSeek-Qwen watch

[`research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md) and [`research/foundation_models/DEEPSEEK_QWEN.md`](research/foundation_models/DEEPSEEK_QWEN.md) track:

```text
dense vs MoE / total vs active parameters
full / sparse / linear / hybrid attention
multimodal fusion and visual/video tokenization
long context and KV/cache hierarchy
streaming perception
training-data mixture / alignment / curriculum
precision / quantization
kernel/compiler/runtime co-design
agent harness / tools / external memory
small-proxy → frontier scaling validity
```

Critical distinctions:

```text
scientific world-state hypothesis
≠ foundation-model backbone
≠ training recipe
≠ inference runtime
≠ agent harness

long context ≠ persistent grounded world memory
serving KV cache ≠ epistemic world memory
base model ≠ model + harness ≠ model + tools/memory
hosted product ≠ open-weight checkpoint
```

## Current practical development reference

```text
Mac mini with Apple M4
```

Use it for measured proxy work:

```text
small/medium open multimodal models
frozen-backbone + state/action heads
LoRA / adapter experiments
MLX / Core AI / Core ML
visual-token / frame-rate ablations
context vs explicit-memory experiments
behavior cloning / flow-diffusion action heads
small MuJoCo RL
teacher distillation
quantization / cache experiments
streaming state prototypes
```

Do **not** treat frontier DeepSeek/Qwen scale as a local-M4 target. Validate important small-model effects on larger remote checkpoints when needed.

## 2026-10-15 latest validation sweep

Stage 1 also tracks:

- WorldOracle — https://arxiv.org/abs/2610.18826
- RoboSimStudio — https://arxiv.org/abs/2610.18835
- LIBERO-RIG — https://arxiv.org/abs/2610.18843
- LoopWAM — https://arxiv.org/abs/2610.18873
- ForceWAM — https://arxiv.org/abs/2610.18852
- RoboFQE — https://arxiv.org/abs/2610.18699
- Grid or Nodes? — https://arxiv.org/abs/2610.18637
- LADDER — https://arxiv.org/abs/2610.18053
- GreenWAM — https://arxiv.org/abs/2610.18774

## Validation evidence ladder while no target robot exists

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single-simulator test
EV2 randomized in-simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data / offline policy evaluation
EV5 real-to-sim / digital-twin validation
EV6 deployment-runtime / compute hardware in the loop
EV7 proxy physical hardware
EV8 target real robot
```

## Current non-goals

We are not currently:

- freezing a final representation, backbone or training recipe;
- choosing DeepSeek or Qwen as Clover architecture by default;
- assuming one post-training method is universally best;
- assuming RL improvement preserves perception, calibration, memory or semantics;
- assuming more robot data is automatically useful without alignment;
- assuming long context replaces persistent memory;
- attributing hosted-agent performance entirely to a base model;
- treating synthetic or simulator data as observed physical evidence;
- designing the science around Mac mini M4;
- claiming sim2real success without real hardware;
- treating one benchmark as the definition of understanding.

## Remaining collection gaps

The remaining gaps are narrower and should be filled only with strong evidence:

```text
visual-token budget vs physical-state retention
video frame-rate / token sampling vs fast dynamics
byte-matched long-context vs explicit-memory comparison
KV precision vs uncertainty / epistemic calibration
MoE expert specialization for spatial / physical variables
small-proxy → frontier-model scaling validity
frozen-backbone vs adapter vs partial/full adaptation
post-training effect on uncertainty / memory / persistence / physical reasoning
reward design for partial success / safety / epistemic correctness
failure/recovery trajectory sampling
human-video / robot / sim data-mixture attribution
language-prior contamination in physical reasoning
streaming multimodal prefill / incremental visual encoding
fast controller + slow reasoner synchronization
harness / tool / external-memory contribution to benchmark scores
runtime/kernel version drift and cross-hardware numerical divergence
API/hosted vs open-weight artifact equivalence
synthetic-data error amplification
representation reversibility after compression
safe irreversible exploration / social permission
sim2sim → sim2real predictive correlation
formal persistent-state rollback / world-state poisoning benchmarks
```

## Stage-1 exit condition

Stage 2 Analysis becomes primary when a new agent can identify:

1. major competing scientific directions and strongest representatives;
2. source/evidence and learning provenance;
3. observation assumptions and world variables represented;
4. identifiability and sufficiency assumptions;
5. likely state-aliasing and abstraction failures;
6. information-gathering / open-world epistemic behavior;
7. hypothesis/model-class and falsification assumptions;
8. exact foundation backbone/artifact when used;
9. architecture/token/context/cache assumptions where material;
10. pretraining, post-training stages, data, on/off-policy regime and reward/teacher provenance;
11. which modules were frozen/updated and action representation where relevant;
12. runtime/kernel/harness/tool assumptions;
13. deployment/runtime hardware constraints;
14. validation evidence level (`EV0–EV8`);
15. datasets/benchmarks that discriminate claims;
16. methods deserving one-method-one-report Analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, final foundation-model backbone, final training recipe, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.
