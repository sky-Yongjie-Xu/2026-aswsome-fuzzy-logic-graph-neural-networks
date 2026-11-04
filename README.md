# Fuzzy Logic × Graph Neural Networks（2024–2026）

面向模糊逻辑与图神经网络的分类文献清单，重点关注**链接预测，以及对 NCNC 内部邻居补全的启发**。

核对截止：**2026-11-04**。主清单 30 条（29 篇研究工作、1 篇综述），另列 1 篇较早在线发表的时间边界文献、4 条待补证据/日期条目；确认 7 个作者关联代码仓库。按正式会议/卷期年覆盖 2024–2026，同时单列首次在线/预印本时间。不是穷尽性系统综述，也不是统一设置的性能排行榜。

## 阅读导航

- **[静态图工作](docs/static-graphs.md)**：普通图 LP、静态 KG 与静态图表征/分类，按原理再分类。
- **[动态图与时序/时空图工作](docs/dynamic-graphs.md)**：内部按模糊表示、模糊语义/时序规则、非神经模糊指标等原理分类；任务单独标注。
- [时间设置待核实](docs/temporal-unverified.md) / [跨设置综述与其他任务](docs/other-settings.md)：不强行归入静态或动态。
- [方法分类与通用原理图](docs/taxonomy.md)：模糊机制进入模型的哪个位置？
- [链接预测重点对照与 FL-NCNC 研究建议](docs/link-prediction.md)：任务、数据、实验可比性和创新边界。
- [35 条逐篇卡片](docs/catalogue.md)：原理、证据范围、局限、借鉴点与来源。
- [检索过程和核验规则](docs/search-log.md)：检索式、来源、日期冲突、待补证据。
- [JSON](data/papers.json) / [CSV](data/papers.csv) / [BibTeX](references.bib)：可筛选数据与引用导出。

## 先读哪些

1. **GFS-Edge（P02）**：直接静态边预测，图模糊规则系统；本地全文已核对。
2. **FGAT/FNS（P01）**：模糊粗糙集用于负采样和聚合；正式会议 2025，预印本 2024。
3. **AFGRL（P03）与 AFGNN（P04）**：普通图 LP 的神经模糊多视图融合；目前仅核对一手摘要。
4. **FGF-GAT（P22）**：2026 年模糊可靠性调节 GAT 的知识图谱工作；与 NCNC 补全不同任务，但需优先核查新颖性重叠。
5. **DFS（P07）、FL-GNN（P08）**：邻域采样/传播内部融合；当前不是直接 LP 结果。
6. **FuzzyDGL（P05）**：动态图 LP，在线 2023、卷期 2024，不能和静态随机划分混比。

## 先区分静态图与动态图，再按方法原理分类

统一采用 **静态图／动态图 → 方法原理 → 具体论文** 的层级，总览、独立页面与逐篇卡片保持一致。知识推理类进一步区分语义嵌入、模糊逻辑组合、时序规则及候选重排序。任务类型与纳入状态独立标注；DFS 的动态采样不当作动态图，归纳 KG 补全也不等同时间外推。尚未核实时间协议的条目单列。完整方法分类说明见 [方法原理](docs/taxonomy.md)。

<!-- CATALOGUE:START -->

### [静态图工作](docs/static-graphs.md)

固定图、独立图样本或没有显式时间维度的任务。静态普通图 LP、静态 KG、节点/图分类分别注明，不混比实验数值。 共 22 条，其中主清单 21 条。

#### A．参数、特征与表示模糊化

将确定特征、网络参数或隐表示扩展为模糊表示，在图传播中处理不确定性。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P06](docs/catalogue.md#p06) | 2024 | **FuzzyGCN** — [Fuzzy Neural Network for Representation Learning on Uncertain Graphs](https://doi.org/10.1109/TFUZZ.2024.3418902) | 节点分类/社区发现 | [作者代码](https://github.com/MrYaoH/FuzzyGCN) |
| [P08](docs/catalogue.md#p08) | 2024 | **FL-GNN** — [FL-GNN: Efficient Fusion of Fuzzy Neural Network and Graph Neural Network](https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA240687) | 节点/图分类 | 未定位 |
| [P15](docs/catalogue.md#p15) | 2026 | **HyperCFN** — [Learning fuzzy representations for hypergraph node classification](https://www.nature.com/articles/s41598-026-51027-7) | 超图节点分类 | 未定位 |
| [P16](docs/catalogue.md#p16) | 2026 | **Uncertainty-aware FHE** — [Uncertainty-Aware Hypergraph Representation Learning for Neurodegenerative Disease Detection](https://www.sciencedirect.com/science/article/pii/S096007792600295X) | 医学分类 | 未定位 |
| [P30](docs/catalogue.md#p30) | 2024 | **FGSCN**（历史边界） — [Fuzzy Graph Subspace Convolutional Network](https://pubmed.ncbi.nlm.nih.gov/36197860/) | 节点分类 | 未定位 |

#### B．模糊关系驱动的采样与注意力

用模糊关系或隶属度控制邻域贡献、注意力或采样。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P01](docs/catalogue.md#p01) | 2025 | **FGAT / FNS** — [Enhancing Link Prediction with Fuzzy Graph Attention Networks and Dynamic Negative Sampling](https://arxiv.org/html/2411.07482v3) | 静态普通图 LP | 未定位 |
| [P07](docs/catalogue.md#p07) | 2025 | **DFS** — [Dynamic Fuzzy Sampler for Graph Neural Networks](https://doi.org/10.1109/TFUZZ.2024.3509018) | 节点分类 | 未定位 |
| [P14](docs/catalogue.md#p14) | 2025 | **FHATN / HFATN** — [Hypergraph representation learning based on fuzzy attention network](https://www.sciencedirect.com/science/article/pii/S1568494625009135) | 超图节点分类 | 未定位 |

#### C．可学习规则、图后件与规则解释

显式学习规则前件/后件，或以图模型优化规则和解释。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P02](docs/catalogue.md#p02) | 2026 | **GFS-Edge** — [GFS-Edge: Graph Fuzzy System for Edge Prediction](https://doi.org/10.1109/TFUZZ.2025.3649146) | 静态普通图 LP | 未定位 |
| [P09](docs/catalogue.md#p09) | 2024 | **GFS-Node** — [GFS-Node: Graph Fuzzy Systems for Node Prediction](https://ieeexplore.ieee.org/abstract/document/10685143) | 节点预测 | [作者代码](https://github.com/FupingHu/GFS-node) |
| [P11](docs/catalogue.md#p11) | 2025 | **FireGNN** — [FireGNN: Neuro-Symbolic Graph Neural Networks with Trainable Fuzzy Rules for Interpretable Medical Image Classification](https://arxiv.org/html/2509.10510v1) | 节点分类 | [作者代码](https://github.com/basiralab/FireGNN) |
| [P12](docs/catalogue.md#p12) | 2026 | **FuzzyGNN** — [FuzzyGNN: a graph neural network framework for enhanced fuzzy modeling](https://link.springer.com/article/10.1007/s00521-026-11967-7) | 表格构图分类 | [作者代码](https://github.com/cilabuniba/fuzzygnn) |
| [P13](docs/catalogue.md#p13) | 2026 | **FGENConv** — [Explainable Fuzzy GNNs for Leak Detection in Water Distribution Networks](https://arxiv.org/html/2601.03062v1) | 节点分类 | [作者代码](https://github.com/pasqualedem/GNNLeakDetection) |
| [P22](docs/catalogue.md#p22) | 2026 | **FGF-GAT** — [Complete Fuzzy Knowledge Representation With Knowledge Graph Embedding](https://pubmed.ncbi.nlm.nih.gov/42262954/) | 知识图谱补全 | 未定位 |

#### E．模糊边界与训练目标

用模糊边界、模糊相似性等改变表示空间中的训练目标。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P10](docs/catalogue.md#p10) | 2025 | **Fuzzy Boundary GAE** — [Mitigating Local Cohesion and Global Sparseness in Graph Contrastive Learning with Fuzzy Boundaries](https://proceedings.mlr.press/v267/lin25b.html) | 节点分类/聚类 | 未定位 |

#### F．模糊语义、逻辑算子与知识推理

通过模糊语义嵌入、逻辑算子、时序规则或集合重排序完成知识推理；进一步按具体机制分组。

##### 语义隶属与层次表示

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P18](docs/catalogue.md#p18) | 2024 | **AFS hierarchical KG** — [Hierarchical knowledge graph relationship prediction leverage of axiomatic fuzzy set graph structure](https://www.sciencedirect.com/science/article/abs/pii/S0957417424009564) | 知识图谱补全 | 未定位 |

##### 模糊集合候选重排序

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P19](docs/catalogue.md#p19) | 2026 | **ReDistLP** — [Fuzzy set-based re-ranking for inductive knowledge graph completion](https://www.sciencedirect.com/science/article/pii/S156849462601152X) | 知识图谱补全 | 未定位 |

##### 模糊逻辑真值组合

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P23](docs/catalogue.md#p23) | 2024 | **UltraQuery** — [A Foundation Model for Zero-shot Logical Query Reasoning](https://arxiv.org/abs/2404.07198) | 复杂逻辑查询 | [作者代码](https://github.com/DeepGraphLearning/ULTRA) |
| [P24](docs/catalogue.md#p24) | 2024 | **FIT** — [Rethinking Complex Queries on Knowledge Graphs with Neural Link Predictors](https://openreview.net/pdf?id=1BmveEMNbG) | 复杂逻辑查询 | 未定位 |

#### G．非神经模糊图链接指标（扩展对照）

直接从模糊邻域、路径或关系强度计算分数，不依赖神经消息传递训练。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P25](docs/catalogue.md#p25) | 2025 | **SP index** — [Strength prominence index: a link prediction method in fuzzy social network](https://link.springer.com/article/10.1007/s40747-025-01925-6) | 非神经模糊图 LP | 未定位 |
| [P26](docs/catalogue.md#p26) | 2026 | **m-polar RMS** — [Link prediction in m-polar fuzzy environment and its application](https://link.springer.com/article/10.1007/s10791-026-09939-5) | 非神经模糊图 LP | 未定位 |
| [P27](docs/catalogue.md#p27) | 2024 | **Fuzzy path strength** — [Link Prediction in Co-Authorship Network Under Fuzziness and Application in Biomedical Analysis](https://xplorestaging.ieee.org/document/10631879) | 非神经模糊图 LP | 未定位 |

### [动态图与时序/时空图工作](docs/dynamic-graphs.md)

区分普通动态图链接预测、时序/时空知识图谱，以及非神经时变图指标。包含时间语义不自动表示使用 GNN，也不自动证明采用未来边外推协议。 共 5 条，其中主清单 4 条。

#### A．参数、特征与表示模糊化

将确定特征、网络参数或隐表示扩展为模糊表示，在图传播中处理不确定性。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P05](docs/catalogue.md#p05) | 2024 | **FuzzyDGL** — [Fuzzy Representation Learning on Dynamic Graphs](https://ieeexplore.ieee.org/abstract/document/10286559) | 动态图 LP | [作者代码](https://github.com/MrYaoH/FuzzyDGL) |

#### F．模糊语义、逻辑算子与知识推理

通过模糊语义嵌入、逻辑算子、时序规则或集合重排序完成知识推理；进一步按具体机制分组。

##### 时空元素模糊嵌入

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P20](docs/catalogue.md#p20) | 2026 | **FSKGE** — [FSKGE: Fuzzy spatio-temporal knowledge graph embedding](https://www.sciencedirect.com/science/article/pii/S0925231225032096) | 时序知识图谱补全 | 未定位 |

##### 时间分层与模糊规则

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P21](docs/catalogue.md#p21) | 2026 | **Time layering + fuzzy rules** — [Temporal knowledge graph reasoning based on time layering and fuzzy logic rules](https://www.sciencedirect.com/science/article/abs/pii/S1568494626000463) | 时序知识图谱补全 | 未定位 |

##### 模糊时间隶属与贡献建模

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [W04](docs/catalogue.md#w04) | 2027 | **FATKG**（待核/跟踪） — [FATKG: Fuzzy adaptive temporal knowledge graph reasoning](https://www.sciencedirect.com/science/article/pii/S0957417426024474) | 时序知识图谱补全 | 未定位 |

#### G．非神经模糊图链接指标（扩展对照）

直接从模糊邻域、路径或关系强度计算分数，不依赖神经消息传递训练。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P29](docs/catalogue.md#p29) | 2026 | **Robotic SP adaptation** — [Prominence-guided link prediction in fuzzy robotic networks](https://www.nature.com/articles/s41598-025-31705-8) | 非神经模糊图 LP | 未定位 |

### [时间设置待核实](docs/temporal-unverified.md)

一手证据不足时不强行归类。多视图、训练中动态采样、归纳预测以及题名中的 dynamic 都不能单独证明图结构随时间演化。 共 6 条，其中主清单 3 条。

#### D．神经模糊多视图融合

以神经模糊推理调节不同图视图或编码器表示之间的融合。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P03](docs/catalogue.md#p03) | 2025 | **AFGRL（模糊多视图）** — [Adaptive Deep Fuzzy Neural Network With Multi‐Headed Self‐Attention for Improving Performance of Social Network Representation Learning and Link Prediction](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70165) | 普通图 LP；时间协议待核 | 未定位 |
| [P04](docs/catalogue.md#p04) | 2026 | **AFGNN** — [Adaptive Inference Neuro-Fuzzy Driven Embedding Fusion for Improving Link Prediction Through Graph Neural Network](https://www.worldscientific.com/doi/10.1142/S0218488526500340) | 普通图 LP；时间协议待核 | 未定位 |

#### G．非神经模糊图链接指标（扩展对照）

直接从模糊邻域、路径或关系强度计算分数，不依赖神经消息传递训练。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P28](docs/catalogue.md#p28) | 2024 | **Generalized fuzzy hypergraph** — [Generalized fuzzy hypergraph for link prediction and identification of influencers in dynamic social media networks](https://researchers.westernsydney.edu.au/en/publications/generalized-fuzzy-hypergraph-for-link-prediction-and-identificati/) | 非神经模糊图 LP | 未定位 |

#### U．原理待核实（仅出版元数据）

尚无可读的一手方法证据，不根据题名补写具体机制。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [W01](docs/catalogue.md#w01) | 2026 | **NAFGCN**（待核/跟踪） — [Neighborhood-Aware Fuzzy Graph Convolutional Networks for Improved Information Fusion](https://doi.org/10.1109/TFUZZ.2026.3667580) | 任务待核 | 未定位 |
| [W02](docs/catalogue.md#w02) | 2025 | **FHRLI / FHCRL**（待核/跟踪） — [Investigating All Uncertainties in Hypergraph Representation Learning and Inference](https://doi.org/10.1109/TFUZZ.2025.3573914) | 任务待核 | 未定位 |
| [W03](docs/catalogue.md#w03) | 2026 | **Fuzzy federated TSK**（待核/跟踪） — [Fuzzy Federated Graph Learning via TSK Message Passing and Contrastive Uncertainty Learning](https://doi.org/10.1109/TFUZZ.2026.3713494) | 任务待核 | 未定位 |

### [跨设置综述与其他任务](docs/other-settings.md)

综述和不能直接按静态/动态图任务解释的规则图回归工作单列。 共 2 条，其中主清单 2 条。

#### C．可学习规则、图后件与规则解释

显式学习规则前件/后件，或以图模型优化规则和解释。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P17](docs/catalogue.md#p17) | 2024 | **TSKG** — [EEG-based TSK fuzzy graph neural network for driver drowsiness estimation](https://www.sciencedirect.com/science/article/pii/S0020025524010156) | 回归 | 未定位 |

#### R．领域综述

跨方法的文献综述。

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P31](docs/catalogue.md#p31) | 2025 | **FGNN review** — [Fuzzy Graph Neural Networks: A Comprehensive Review of Uncertainty-Aware Graph Learning](https://eudl.eu/doi/10.4108/eetcasa.9483) | 综述 | 未定位 |


<!-- CATALOGUE:END -->

## 收录与复现说明

本仓库保存书目信息、原创中文简述和来源链接，不上传用户本地论文 PDF、付费全文、未发表实验结果或第三方完整代码。作者代码链接已核验不代表已复现。只有摘要的条目不补写未知公式、数据集或性能数字。

`data/papers.json` 是人工核验后的主数据。修改后运行：

```bash
python3 scripts/export_catalog.py
python3 scripts/validate.py
```

需要刷新出版元数据时，可运行 `python3 scripts/fetch_crossref.py`。Crossref 元数据不能代替阅读全文；IEEE 卷期日期、在线日期及 DOI 年份可能不同，应保留人工核对的日期说明。
