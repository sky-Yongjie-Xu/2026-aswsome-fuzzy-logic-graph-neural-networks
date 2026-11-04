# 静态图工作

[返回总览](../README.md) · [静态图](static-graphs.md) · [动态图/时序图](dynamic-graphs.md) · [时间设置待核](temporal-unverified.md)

固定图、独立图样本或没有显式时间维度的任务。静态普通图 LP、静态 KG、节点/图分类分别注明，不混比实验数值。

本页共 22 条：主清单 21 条；时间边界/跟踪 1 条。纳入状态与图时间类型是两个独立标签。

**组织层级：图时间设置 → 方法原理 → 具体论文。** 普通图 LP、KG 补全、分类等任务只作表内标签；历史边界与跟踪条目在对应原理下明确标注，不计入主清单。

## A．参数、特征与表示模糊化

将确定特征、网络参数或隐表示扩展为模糊表示，在图传播中处理不确定性。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P06](catalogue.md#p06) | 2024 | **FuzzyGCN** — [Fuzzy Neural Network for Representation Learning on Uncertain Graphs](https://doi.org/10.1109/TFUZZ.2024.3418902) | 节点分类/社区发现 | [作者代码](https://github.com/MrYaoH/FuzzyGCN) |
| [P08](catalogue.md#p08) | 2024 | **FL-GNN** — [FL-GNN: Efficient Fusion of Fuzzy Neural Network and Graph Neural Network](https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA240687) | 节点/图分类 | 未定位 |
| [P15](catalogue.md#p15) | 2026 | **HyperCFN** — [Learning fuzzy representations for hypergraph node classification](https://www.nature.com/articles/s41598-026-51027-7) | 超图节点分类 | 未定位 |
| [P16](catalogue.md#p16) | 2026 | **Uncertainty-aware FHE** — [Uncertainty-Aware Hypergraph Representation Learning for Neurodegenerative Disease Detection](https://www.sciencedirect.com/science/article/pii/S096007792600295X) | 医学分类 | 未定位 |
| [P30](catalogue.md#p30) | 2024 | **FGSCN**（历史边界） — [Fuzzy Graph Subspace Convolutional Network](https://pubmed.ncbi.nlm.nih.gov/36197860/) | 节点分类 | 未定位 |

## B．模糊关系驱动的采样与注意力

用模糊关系或隶属度控制邻域贡献、注意力或采样。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P01](catalogue.md#p01) | 2025 | **FGAT / FNS** — [Enhancing Link Prediction with Fuzzy Graph Attention Networks and Dynamic Negative Sampling](https://arxiv.org/html/2411.07482v3) | 静态普通图 LP | 未定位 |
| [P07](catalogue.md#p07) | 2025 | **DFS** — [Dynamic Fuzzy Sampler for Graph Neural Networks](https://doi.org/10.1109/TFUZZ.2024.3509018) | 节点分类 | 未定位 |
| [P14](catalogue.md#p14) | 2025 | **FHATN / HFATN** — [Hypergraph representation learning based on fuzzy attention network](https://www.sciencedirect.com/science/article/pii/S1568494625009135) | 超图节点分类 | 未定位 |

## C．可学习规则、图后件与规则解释

显式学习规则前件/后件，或以图模型优化规则和解释。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P02](catalogue.md#p02) | 2026 | **GFS-Edge** — [GFS-Edge: Graph Fuzzy System for Edge Prediction](https://doi.org/10.1109/TFUZZ.2025.3649146) | 静态普通图 LP | 未定位 |
| [P09](catalogue.md#p09) | 2024 | **GFS-Node** — [GFS-Node: Graph Fuzzy Systems for Node Prediction](https://ieeexplore.ieee.org/abstract/document/10685143) | 节点预测 | [作者代码](https://github.com/FupingHu/GFS-node) |
| [P11](catalogue.md#p11) | 2025 | **FireGNN** — [FireGNN: Neuro-Symbolic Graph Neural Networks with Trainable Fuzzy Rules for Interpretable Medical Image Classification](https://arxiv.org/html/2509.10510v1) | 节点分类 | [作者代码](https://github.com/basiralab/FireGNN) |
| [P12](catalogue.md#p12) | 2026 | **FuzzyGNN** — [FuzzyGNN: a graph neural network framework for enhanced fuzzy modeling](https://link.springer.com/article/10.1007/s00521-026-11967-7) | 表格构图分类 | [作者代码](https://github.com/cilabuniba/fuzzygnn) |
| [P13](catalogue.md#p13) | 2026 | **FGENConv** — [Explainable Fuzzy GNNs for Leak Detection in Water Distribution Networks](https://arxiv.org/html/2601.03062v1) | 节点分类 | [作者代码](https://github.com/pasqualedem/GNNLeakDetection) |
| [P22](catalogue.md#p22) | 2026 | **FGF-GAT** — [Complete Fuzzy Knowledge Representation With Knowledge Graph Embedding](https://pubmed.ncbi.nlm.nih.gov/42262954/) | 知识图谱补全 | 未定位 |

## E．模糊边界与训练目标

用模糊边界、模糊相似性等改变表示空间中的训练目标。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P10](catalogue.md#p10) | 2025 | **Fuzzy Boundary GAE** — [Mitigating Local Cohesion and Global Sparseness in Graph Contrastive Learning with Fuzzy Boundaries](https://proceedings.mlr.press/v267/lin25b.html) | 节点分类/聚类 | 未定位 |

## F．模糊语义、逻辑算子与知识推理

通过模糊语义嵌入、逻辑算子、时序规则或集合重排序完成知识推理；进一步按具体机制分组。

### 语义隶属与层次表示

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P18](catalogue.md#p18) | 2024 | **AFS hierarchical KG** — [Hierarchical knowledge graph relationship prediction leverage of axiomatic fuzzy set graph structure](https://www.sciencedirect.com/science/article/abs/pii/S0957417424009564) | 知识图谱补全 | 未定位 |

### 模糊集合候选重排序

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P19](catalogue.md#p19) | 2026 | **ReDistLP** — [Fuzzy set-based re-ranking for inductive knowledge graph completion](https://www.sciencedirect.com/science/article/pii/S156849462601152X) | 知识图谱补全 | 未定位 |

### 模糊逻辑真值组合

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P23](catalogue.md#p23) | 2024 | **UltraQuery** — [A Foundation Model for Zero-shot Logical Query Reasoning](https://arxiv.org/abs/2404.07198) | 复杂逻辑查询 | [作者代码](https://github.com/DeepGraphLearning/ULTRA) |
| [P24](catalogue.md#p24) | 2024 | **FIT** — [Rethinking Complex Queries on Knowledge Graphs with Neural Link Predictors](https://openreview.net/pdf?id=1BmveEMNbG) | 复杂逻辑查询 | 未定位 |

## G．非神经模糊图链接指标（扩展对照）

直接从模糊邻域、路径或关系强度计算分数，不依赖神经消息传递训练。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P25](catalogue.md#p25) | 2025 | **SP index** — [Strength prominence index: a link prediction method in fuzzy social network](https://link.springer.com/article/10.1007/s40747-025-01925-6) | 非神经模糊图 LP | 未定位 |
| [P26](catalogue.md#p26) | 2026 | **m-polar RMS** — [Link prediction in m-polar fuzzy environment and its application](https://link.springer.com/article/10.1007/s10791-026-09939-5) | 非神经模糊图 LP | 未定位 |
| [P27](catalogue.md#p27) | 2024 | **Fuzzy path strength** — [Link Prediction in Co-Authorship Network Under Fuzziness and Application in Biomedical Analysis](https://xplorestaging.ieee.org/document/10631879) | 非神经模糊图 LP | 未定位 |

## 分类依据与使用边界

| ID | 分类依据 |
|---|---|
| [P01](catalogue.md#p01) | dynamic 指负采样机制；已核实预印本按静态边划分评测。 |
| [P02](catalogue.md#p02) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P06](catalogue.md#p06) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P07](catalogue.md#p07) | dynamic 指模糊采样/隶属度随学习调整；已核实实验为固定图节点任务。 |
| [P08](catalogue.md#p08) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P09](catalogue.md#p09) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P10](catalogue.md#p10) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P11](catalogue.md#p11) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P12](catalogue.md#p12) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P13](catalogue.md#p13) | 按固定物理管网拓扑上的节点检测/定位组织；节点信号时间性不等于拓扑随时间变化。 |
| [P14](catalogue.md#p14) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P15](catalogue.md#p15) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P16](catalogue.md#p16) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P18](catalogue.md#p18) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P19](catalogue.md#p19) | 归纳 KG 补全中的未见实体不等于时变图；当前按无时间戳的关系补全组织。 |
| [P22](catalogue.md#p22) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P23](catalogue.md#p23) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P24](catalogue.md#p24) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P25](catalogue.md#p25) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P26](catalogue.md#p26) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P27](catalogue.md#p27) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |
| [P30](catalogue.md#p30) | 按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。 |

原理、实验范围及原始来源见各 ID 的逐篇卡片。本页分类不新增原论文未报告的实验结论。
