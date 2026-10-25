<p align="center">
  <img src="hero.svg" alt="Clover — open research into understanding the real world through vision alone." width="100%">
</p>

<p align="center">
  <a href="README.zh-CN.md">中文</a> &nbsp; / &nbsp;
  <a href="SSOT.md">Research question</a> &nbsp; / &nbsp;
  <a href="STATUS.md">Current progress</a> &nbsp; / &nbsp;
  <a href="SOURCES.md">Sources</a>
</p>

# How can a machine understand the real world through vision alone?

That is Clover’s research question. The long-term goal is a general-purpose robotic brain that forms an understanding of the real world through vision, then uses it to decide and act. **The question is fixed; the answer is open.**

**Current stage: Research.** We are mapping the problem, studying competing explanations and tracing claims to their evidence. A final representation, backbone and core algorithm remain open. Scientific progress and unresolved gaps live in [STATUS.md](STATUS.md).

## Read the project

| Start with | What you will find |
|---|---|
| [SSOT.md](SSOT.md) | The research question, meaning of understanding and evidence rules. |
| [STATUS.md](STATUS.md) | Current conclusions, remaining gaps and the next work. |
| [RESEARCH.md](RESEARCH.md) | The research landscape and where the evidence is still thin. |

## Follow a question

| Question | Living documents |
|---|---|
| What can visual evidence actually identify? | [Perception, geometry and physics](PERCEPTION.md) · [Research questions](QUESTIONS.md) |
| What should a machine remember about the world? | [State, representation and memory](REPRESENTATION.md) |
| When should it look again, intervene or revise its beliefs? | [Causality, action and open-world reasoning](ACTION.md) |
| How do data and training change capability? | [Learning and data](LEARNING.md) |
| What do foundation models and deployment systems contribute? | [Models, runtime and engineering](SYSTEMS.md) |
| What evidence would distinguish the competing answers? | [Evaluation and resources](EVALUATION.md) · [Primary sources](SOURCES.md) |
| Which Clover ideas still need to survive a test? | [Hypotheses](HYPOTHESES.md) · [Research process](PROCESS.md) |

## Keep the evidence honest

Vision at deployment and learning from vision alone are separate claims. We record both the observation protocol (`V0–V3`) and learning provenance (`L0–L4`). Prediction, reconstruction, physical identification and useful action each require their own evidence. See [SSOT.md](SSOT.md).

Research → Analysis → Synthesis → Innovation → Implementation → Evaluation → Reflection.

Each topic has one living document, updated in place. Earlier states remain in Git history. Contributors and agents should begin with [AGENTS.md](AGENTS.md), then follow [PROCESS.md](PROCESS.md).

[License](LICENSE) · [Citation metadata](CITATION.cff)
