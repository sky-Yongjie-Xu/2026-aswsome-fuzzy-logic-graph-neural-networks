# 逐篇方法与证据卡片

核对日期：2026-11-04。分类是本仓库的整理；“借鉴点”是分析建议，不是原论文已证明的结论。
代码“未定位”只表示本轮检索未确认，不能理解为作者没有公开代码。

[返回总览](../README.md) · [分类原理](taxonomy.md) · [链接预测与 FL-NCNC](link-prediction.md)

## 静态图工作

### A．参数、特征与表示模糊化

<a id="p06"></a>
#### P06．FuzzyGCN

**Fuzzy Neural Network for Representation Learning on Uncertain Graphs**

作者：Yue-Na Lin; Hai-Chun Cai; Chun-Yang Zhang; Hong-Yu Yao; C. L. Philip Chen
发表：IEEE Transactions on Fuzzy Systems，2024。全文：在线 2024-06-25；卷期 2024-09。
任务：节点分类/社区发现。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：用户提供全文已读相关部分（不分发全文）。

**方法原理：** 将网络权重和偏置表示为模糊数，经模糊传播获得表示，再解模糊得到输出。
**实验/数据范围：** Cora、CiteSeer、Pubmed 等 7 个图数据集；任务为节点分类/社区发现。
**限制与区分：** 全文主要验证节点分类与社区发现；无独立链接预测结果不能声称其优于 NCNC。
**对 FL-NCNC 的借鉴：** 提供传播参数模糊化路线，与候选边层面的 TSK 权重修正不同。

来源：[来源 1](https://doi.org/10.1109/TFUZZ.2024.3418902) · [来源 2](https://github.com/MrYaoH/FuzzyGCN)
代码：https://github.com/MrYaoH/FuzzyGCN。作者关联仓库已核验；未运行复现。

<a id="p08"></a>
#### P08．FL-GNN

**FL-GNN: Efficient Fusion of Fuzzy Neural Network and Graph Neural Network**

作者：Boyu Du; Jingya Zhou; Ling Liu; Xiaolong She
发表：Frontiers in Artificial Intelligence and Applications; ECAI 2024，2024。ECAI 2024 正式论文，2024-10-16。
任务：节点/图分类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 在图局部信息聚合中引入模糊神经网络和结构化模糊规则，并用消息传递视角优化计算。
**实验/数据范围：** Cora、CiteSeer、Pubmed、ogbn-proteins、Reddit 等节点任务及图级任务；非直接 LP 基线。
**限制与区分：** 正式版本为 ECAI 2024；不能将另一条 ICLR 投稿记录当作 ICLR 已录用。
**对 FL-NCNC 的借鉴：** 检查规则是否真正进入消息传递，并用规则屏蔽/忠实性分析支持解释。

来源：[来源 1](https://ebooks.iospress.nl/pdf/doi/10.3233/FAIA240687)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p15"></a>
#### P15．HyperCFN

**Learning fuzzy representations for hypergraph node classification**

作者：Zhishu Sun; Ruijing Geng; Ge Zhang
发表：Scientific Reports，2026。2026-05-02。
任务：超图节点分类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 在协同节点—超边编码器中加入模糊表示，联合节点、超边、隶属关系三级对比以及结构重建。
**实验/数据范围：** 未核实
**限制与区分：** 论文实验为超图节点分类；重建损失不能自动视为独立链接预测实验。
**对 FL-NCNC 的借鉴：** 借鉴模糊表示、跨视图一致性与结构保持的联合训练。

来源：[来源 1](https://www.nature.com/articles/s41598-026-51027-7) · [来源 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC13323706/)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p16"></a>
#### P16．Uncertainty-aware FHE

**Uncertainty-Aware Hypergraph Representation Learning for Neurodegenerative Disease Detection**

作者：Manman Yuan; Can Yin; Junlin Li; Jun Hu; Huijia Li; Matjaž Perc
发表：Chaos, Solitons &amp; Fractals，2026。
任务：医学分类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 用模糊推理构建不确定脑超图，以模糊规则与超图消息传递编码，并设计语义一致的对比增强。
**实验/数据范围：** 未核实
**限制与区分：** 神经退行性疾病检测；不属于普通图 LP。当前主要依据出版社摘要。
**对 FL-NCNC 的借鉴：** 借鉴不确定关系建模和增强一致性，不直接迁移医学分类指标。

来源：[来源 1](https://www.sciencedirect.com/science/article/pii/S096007792600295X) · [来源 2](https://www.matjazperc.com/publications/ChaosSolitonsFractals_208_118154.pdf)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p30"></a>
#### P30．FGSCN

**Fuzzy Graph Subspace Convolutional Network**

作者：Jianhang Zhou; Qi Zhang; Shaoning Zeng; Bob Zhang
发表：IEEE Transactions on Neural Networks and Learning Systems，2024。2022 在线；TNNLS 35(4):5641–5655 (2024)。
任务：节点分类。纳入状态：historical_boundary。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 将高维邻近图与低秩子空间亲和图融合为模糊子空间图，在该图上传播局部与全局信息。
**实验/数据范围：** 未核实
**限制与区分：** 2024 是卷期年，工作已在 2022 在线；应作为较早基础工作，不能称为近三年新提出。
**对 FL-NCNC 的借鉴：** 提供模糊构图路线，对照仅在补全阶段增加规则的设计。

来源：[来源 1](https://pubmed.ncbi.nlm.nih.gov/36197860/)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### B．模糊关系驱动的采样与注意力

<a id="p01"></a>
#### P01．FGAT / FNS

**Enhancing Link Prediction with Fuzzy Graph Attention Networks and Dynamic Negative Sampling**

作者：Jinming Xing; Ruilin Xing; Chang Xue; Dongwen Luo
发表：Lecture Notes in Networks and Systems; Proceedings of the 2025 10th International Conference on Multimedia Systems and Signal Processing，2025。预印本 2024-11-12；v3 为 2025-02-01；正式章节 2025-10-01。合并为一条。
任务：静态普通图 LP。纳入状态：main。
图时间设置：静态图。dynamic 指负采样机制；已核实预印本按静态边划分评测。
阅读证据：公开全文已读相关部分。

**方法原理：** 用模糊粗糙集下近似评价候选负边，选择负样本，并将模糊关系融入 GAT 聚合。
**实验/数据范围：** Ca-netscience、Ca-sandi-auths；预印本表中 70/10/20 边划分，表标有向图。
**限制与区分：** 核对的预印本仅测试两个小型合作网络；不能把该结果当作 Cora 或大规模 OGB 上的证据。
**对 FL-NCNC 的借鉴：** 优先借鉴补全候选分布上的困难负样本训练，单独验证采样与聚合的贡献。

来源：[来源 1](https://arxiv.org/html/2411.07482v3) · [来源 2](https://link.springer.com/chapter/10.1007/978-3-032-05994-9_16)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p07"></a>
#### P07．DFS

**Dynamic Fuzzy Sampler for Graph Neural Networks**

作者：Jia Wei; Xingjun Zhang; Witold Pedrycz; Weiping Ding
发表：IEEE Transactions on Fuzzy Systems，2025。全文：在线 2025-01-06；卷期 2025-04。DOI 中的 2024 不是正式发表年。
任务：节点分类。纳入状态：main。
图时间设置：静态图。dynamic 指模糊采样/隶属度随学习调整；已核实实验为固定图节点任务。
阅读证据：用户提供全文已读相关部分（不分发全文）。

**方法原理：** 学习高斯模糊集，动态计算邻居对目标节点的隶属度，并聚合隶属度加权的邻居表示。
**实验/数据范围：** Cora、CiteSeer、PubMed、Reddit、PPI；监督/自监督节点任务。
**限制与区分：** dynamic 指采样/隶属度随学习变化；不能据此归为时间动态图链接预测。
**对 FL-NCNC 的借鉴：** 可迁移到潜在共同邻居的采样和贡献分配，但必须新增链接预测实验证据。

来源：[来源 1](https://doi.org/10.1109/TFUZZ.2024.3509018)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p14"></a>
#### P14．FHATN / HFATN

**Hypergraph representation learning based on fuzzy attention network**

作者：Liyan Zhang; Yifan Li; Xinghui Hao; Qinyu Zhang; Aimin Yang; Jingfeng Guo; Lei Zhang
发表：Applied Soft Computing，2025。
任务：超图节点分类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 分别在顶点到超边、超边到顶点的聚合中计算模糊隶属度，用它调节注意力贡献。
**实验/数据范围：** Cora、20Newsgroups、Pubmed；超图节点分类。
**限制与区分：** 原文预览的缩写存在 FHATN/HFATN 不一致；按同一 DOI 合并。只核实超图节点分类。
**对 FL-NCNC 的借鉴：** 双向隶属关系可以分别表达证据贡献，但超边集合预测不等于普通二元边预测。

来源：[来源 1](https://www.sciencedirect.com/science/article/pii/S1568494625009135)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### C．可学习规则、图后件与规则解释

<a id="p02"></a>
#### P02．GFS-Edge

**GFS-Edge: Graph Fuzzy System for Edge Prediction**

作者：Fuping Hu; Zhaohong Deng; Kup-Sze Choi; Shitong Wang
发表：IEEE Transactions on Fuzzy Systems，2026。全文页脚：在线 2025-12-29；卷期 2026-03，34(3):816–827。
任务：静态普通图 LP。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：用户提供全文已读相关部分（不分发全文）。

**方法原理：** 以边聚类产生模糊规则前件，由线性变分图自编码器承担边后件处理；按规则激活程度组合预测。
**实验/数据范围：** Cora、Citeseer、Pubmed、Power、NS、Yeast、USAir、Celegans、Router、GRQ、BUP、ZWL；正文设置 80/10/10，重复 10 次。
**限制与区分：** 是完整图模糊边预测系统；与 NCNC 的潜在共同邻居补全位置不同。论文也报告大图资源限制。
**对 FL-NCNC 的借鉴：** 学习数据驱动的规则前件，区分规则激活、图后件和最终边分数，避免仅套用 TSK 名称。

来源：[来源 1](https://doi.org/10.1109/TFUZZ.2025.3649146)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p09"></a>
#### P09．GFS-Node

**GFS-Node: Graph Fuzzy Systems for Node Prediction**

作者：Fuping Hu; Zhaohong Deng; Zhenping Xie; Te Zhang; Kup-Sze Choi; Fan Zhang; Shitong Wang
发表：IEEE Transactions on Fuzzy Systems，2024。在线 2024-09-20；卷期 2024-12。
任务：节点预测。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 以核 K 虚拟中心节点聚类生成规则前件，以线性消息传递网络学习规则后件。
**实验/数据范围：** 未核实
**限制与区分：** 节点预测系统，与 GFS-Edge 是不同论文；不得用其源码冒充边预测源码。
**对 FL-NCNC 的借鉴：** 规则前件与图消息传递后件分工明确，适合研究规则原型和局部图证据的对应关系。

来源：[来源 1](https://ieeexplore.ieee.org/abstract/document/10685143) · [来源 2](https://github.com/FupingHu/GFS-node)
代码：https://github.com/FupingHu/GFS-node。作者关联仓库已核验；未运行复现。

<a id="p11"></a>
#### P11．FireGNN

**FireGNN: Neuro-Symbolic Graph Neural Networks with Trainable Fuzzy Rules for Interpretable Medical Image Classification**

作者：Prajit Sengupta; Islem Rekik
发表：arXiv; 作者仓库标注 NeurIPS 2025 Workshops，2025。
任务：节点分类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 对度、聚类系数、两跳标签一致性等描述量构造可学习模糊条件，再与 GNN 表示融合。
**实验/数据范围：** MedMNIST、MorphoMNIST 图像构图分类。
**限制与区分：** 图中节点是图像；标签相关规则迁移到 LP 时不能使用验证/测试标签。Workshop 不等于 NeurIPS 主会论文。
**对 FL-NCNC 的借鉴：** 借鉴可学习规则阈值和结构描述量，同时核查标签来源及解释忠实性。

来源：[来源 1](https://arxiv.org/html/2509.10510v1) · [来源 2](https://github.com/basiralab/FireGNN)
代码：https://github.com/basiralab/FireGNN。作者关联仓库已核验；未运行复现。

<a id="p12"></a>
#### P12．FuzzyGNN

**FuzzyGNN: a graph neural network framework for enhanced fuzzy modeling**

作者：Gianluca Zaza; Raffaele Scaringi; Gennaro Vessio; Giovanna Castellano
发表：Neural Computing and Applications，2026。在线 2026-05-09。
任务：表格构图分类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 把每个表格样本的原始特征和模糊集构成图，用 GNN 建模交互，结合解释驱动剪枝提取精简规则。
**实验/数据范围：** 未核实
**限制与区分：** 图是样本内部构造的特征—模糊集图；不是社交/引文网络链接预测。
**对 FL-NCNC 的借鉴：** 借鉴规则剪枝、复杂度和解释评估，不把表格分类准确率当 LP 证据。

来源：[来源 1](https://link.springer.com/article/10.1007/s00521-026-11967-7) · [来源 2](https://github.com/cilabuniba/fuzzygnn)
代码：https://github.com/cilabuniba/fuzzygnn。作者关联仓库已核验；未运行复现。

<a id="p13"></a>
#### P13．FGENConv

**Explainable Fuzzy GNNs for Leak Detection in Water Distribution Networks**

作者：Qusai Khaled; Pasquale De Marinis; Moez Louati; David Ferras; Laura Genga; Uzay Kaymak
发表：arXiv preprint，2026。预印本 2026-01-06。
任务：节点分类。纳入状态：main。
图时间设置：静态图。按固定物理管网拓扑上的节点检测/定位组织；节点信号时间性不等于拓扑随时间变化。
阅读证据：公开全文已读相关部分。

**方法原理：** 在 GENConv 漏水检测/定位模型中加入模糊机制，形成面向节点预测的规则解释。
**实验/数据范围：** 未核实
**限制与区分：** 摘要明确报告模糊版本的检测与定位 F1 低于 crisp GENConv；可解释性和性能需要分别评估。
**对 FL-NCNC 的借鉴：** 提供反例：加入模糊逻辑不自动提高预测性能。

来源：[来源 1](https://arxiv.org/html/2601.03062v1) · [来源 2](https://github.com/pasqualedem/GNNLeakDetection)
代码：https://github.com/pasqualedem/GNNLeakDetection。作者关联仓库已核验；未运行复现。

<a id="p22"></a>
#### P22．FGF-GAT

**Complete Fuzzy Knowledge Representation With Knowledge Graph Embedding**

作者：Haoning Li; Qinghua Huang
发表：IEEE Transactions on Pattern Analysis and Machine Intelligence，2026。TPAMI 48(10):12758–12775，2026-10；首次在线日期本轮未核实。
任务：知识图谱补全。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 以 ANFIS 式参数化和轻量 TSK 规则将元素隶属度转换为可靠性信号，调节 GAT 邻域聚合；解码器注入隶属信息。
**实验/数据范围：** 摘要报告 4 个基准、实体预测和关系预测；具体名称待全文核实。
**限制与区分：** 仅核对作者摘要与出版元数据；依赖细粒度模糊 KG 的元素级隶属信息，普通 Cora 不直接具备这些输入。
**对 FL-NCNC 的借鉴：** 与可靠性调节补全贡献最相关；必须说明 FL-NCNC 的不确定性来源和信息条件有何不同。

来源：[来源 1](https://pubmed.ncbi.nlm.nih.gov/42262954/) · [来源 2](https://doi.org/10.1109/TPAMI.2026.3701743)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### E．模糊边界与训练目标

<a id="p10"></a>
#### P10．Fuzzy Boundary GAE

**Mitigating Local Cohesion and Global Sparseness in Graph Contrastive Learning with Fuzzy Boundaries**

作者：Yuena Lin; Haichun Cai; Jun-Yi Hang; Haobo Wang; Zhen Yang; Gengyu Lyu
发表：ICML 2025; PMLR 267:37745–37761，2025。
任务：节点分类/聚类。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 通过模糊边界扩张连接局部小群，再收缩边界促进全局聚集，改善图对比学习的表示分布。
**实验/数据范围：** Cora、Citeseer、Pubmed、DBLP、ogbn-arxiv、AmazonPhoto、AmazonComputers；节点分类/聚类。
**限制与区分：** 公开会议全文实验为节点分类与节点聚类；不能将表示改善当作已经验证的链接预测收益。
**对 FL-NCNC 的借鉴：** 模糊机制可以改变优化目标，而不只是在预测后对分数加权。

来源：[来源 1](https://proceedings.mlr.press/v267/lin25b.html) · [来源 2](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lin25b/lin25b.pdf)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### F．模糊语义、逻辑算子与知识推理

<a id="p18"></a>
#### P18．AFS hierarchical KG

**Hierarchical knowledge graph relationship prediction leverage of axiomatic fuzzy set graph structure**

作者：Yan Fang; Qi Lang; Wei Lu; Xiaodong Liu; Jianhua Yang
发表：Expert Systems with Applications，2024。
任务：知识图谱补全。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 以公理模糊集刻画实体间潜在语义，构建层次图表示与实体/关系注意力，再用解码器预测关系。
**实验/数据范围：** 未核实
**限制与区分：** 任务包含关系类型，不能与 Cora 无类型二元边预测直接比较。全文细节未完全核实。
**对 FL-NCNC 的借鉴：** 借鉴语义隶属关系与结构表示结合，但要控制额外关系/语义信息的使用。

来源：[来源 1](https://www.sciencedirect.com/science/article/abs/pii/S0957417424009564)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p19"></a>
#### P19．ReDistLP

**Fuzzy set-based re-ranking for inductive knowledge graph completion**

作者：Yuki Iwamoto; Ken Kaneiwa
发表：Applied Soft Computing，2026。期刊卷期 2026-09；关联预印本 2024，未假设各版本模糊机制完全一致。
任务：知识图谱补全。纳入状态：main。
图时间设置：静态图。归纳 KG 补全中的未见实体不等于时变图；当前按无时间戳的关系补全组织。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 利用不同规则长度下预测差异构造重排序，以模糊集合处理候选集和截断的不确定性。
**实验/数据范围：** 出版社预览涉及 FB15k-237、NELL-995、WN18RR。
**限制与区分：** 知识图谱归纳补全；模糊重排序本身不等于 GNN 消息传递。预印本和期刊版本须区分。
**对 FL-NCNC 的借鉴：** 提醒补全排序、候选截断与最终预测是不同层面，应分开诊断。

来源：[来源 1](https://www.sciencedirect.com/science/article/pii/S156849462601152X) · [来源 2](https://arxiv.org/abs/2405.16902)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p23"></a>
#### P23．UltraQuery

**A Foundation Model for Zero-shot Logical Query Reasoning**

作者：Mikhail Galkin; Jincheng Zhou; Bruno Ribeiro; Jian Tang; Zhaocheng Zhu
发表：NeurIPS 2024，2024。预印本 2024-04-10；作者代码提供 NeurIPS 2024 引用。
任务：复杂逻辑查询。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 以可跨实体/关系词表迁移的图推理模型执行关系投影，再以非参数模糊逻辑算子组合查询结果。
**实验/数据范围：** 未核实
**限制与区分：** 核心任务是复杂逻辑查询回答；不能把查询 MRR 当作普通 LP 指标。
**对 FL-NCNC 的借鉴：** 关系投影与模糊逻辑组合分工明确，可启发补全证据的组合设计。

来源：[来源 1](https://arxiv.org/abs/2404.07198) · [来源 2](https://github.com/DeepGraphLearning/ULTRA)
代码：https://github.com/DeepGraphLearning/ULTRA。作者关联仓库已核验；未运行复现。

<a id="p24"></a>
#### P24．FIT

**Rethinking Complex Queries on Knowledge Graphs with Neural Link Predictors**

作者：Hang Yin; Zihao Wang; Yangqiu Song
发表：ICLR 2024，2024。正式会议 2024；预印本已于 2023 公开，属于时间边界文献。
任务：复杂逻辑查询。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 把神经链接预测器输出作为原子真值，再用模糊逻辑计算复合查询，支持端到端学习。
**实验/数据范围：** 未核实
**限制与区分：** 模糊逻辑加链接预测器不意味着该预测器一定是 GNN；任务为复杂查询。
**对 FL-NCNC 的借鉴：** 区分逻辑真值、预测概率和补全权重，明确组合规则及适用条件。

来源：[来源 1](https://openreview.net/pdf?id=1BmveEMNbG) · [来源 2](https://arxiv.org/abs/2304.07063)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### G．非神经模糊图链接指标（扩展对照）

<a id="p25"></a>
#### P25．SP index

**Strength prominence index: a link prediction method in fuzzy social network**

作者：Sakshi Dev Pandey; Sovan Samanta; A. S. Ranadive; Leo Mrsic; Antonios Kalampakas; Tofigh Allahviranloo
发表：Complex &amp; Intelligent Systems，2025。在线 2025-05-29。
任务：非神经模糊图 LP。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 以节点显著性和连接强度设计模糊图相似度，分别处理有共同邻居与无共同邻居的节点对。
**实验/数据范围：** Facebook 数据，具体预处理与边划分待统一。
**限制与区分：** 属于非神经启发式，依赖节点/边隶属定义；不能称为模糊 GNN。
**对 FL-NCNC 的借鉴：** 适合低成本结构基线，检验神经模糊规则是否超越简单模糊邻居指标。

来源：[来源 1](https://link.springer.com/article/10.1007/s40747-025-01925-6)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p26"></a>
#### P26．m-polar RMS

**Link prediction in m-polar fuzzy environment and its application**

作者：Tanmoy Mahapatra; Rupkumar Mahapatra; Sovan Samanta; J. G. Lee; Madhumangal Pal
发表：Discover Computing，2026。2026-02-06。
任务：非神经模糊图 LP。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：公开全文已读相关部分。

**方法原理：** 在多极模糊图中用多维隶属度和 RMS 指标刻画共同邻居的不同影响。
**实验/数据范围：** 未核实
**限制与区分：** 以理论、算法和应用示例为主；非 GNN，也不能视为标准 Cora 基准结果。
**对 FL-NCNC 的借鉴：** 启发将不同证据分别建模，而不是把所有不确定性压成一个分数。

来源：[来源 1](https://link.springer.com/article/10.1007/s10791-026-09939-5)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p27"></a>
#### P27．Fuzzy path strength

**Link Prediction in Co-Authorship Network Under Fuzziness and Application in Biomedical Analysis**

作者：Kousik Das; Ananta Maity; Kajal De; Sukumar Mondal; Sovan Samanta; Tofigh Allahviranloo
发表：Fuzzy Information and Engineering，2024。Fuzzy Information and Engineering 16(2):155–174，2024-06。
任务：非神经模糊图 LP。纳入状态：main。
图时间设置：静态图。按固定图/图样本或无显式时间维度的任务组织；不意味着图来自现实静止系统。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 定义连接和路径强度，为最短距离 3–5 的节点对设计模糊链接评分。
**实验/数据范围：** 未核实
**限制与区分：** 是路径启发式而非训练得到的 GNN；数值例子不等同统一基准评测。
**对 FL-NCNC 的借鉴：** 可作零共同邻居场景的结构证据对照。

来源：[来源 1](https://xplorestaging.ieee.org/document/10631879)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

## 动态图与时序/时空图工作

### A．参数、特征与表示模糊化

<a id="p05"></a>
#### P05．FuzzyDGL

**Fuzzy Representation Learning on Dynamic Graphs**

作者：Hong-Yu Yao; Yuan-Long Yu; Chun-Yang Zhang; Yue-Na Lin; Shang-Jia Li
发表：IEEE Transactions on Systems, Man, and Cybernetics: Systems，2024。在线 2023-10-17，正式卷期 2024-02；属于按卷期纳入的边界文献，并非 2024 首次公开。
任务：动态图 LP。纳入状态：main。
图时间设置：动态图/时序与时空图。结构与时间关联的动态图表示学习，并评估动态链接预测。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 将模糊表示学习与连续时间动态图表示结合，建模特征模糊性，同时利用结构与时间关联。
**实验/数据范围：** 论文摘要：8 个真实数据集；代码 README 给出 CollegeMsg 示例，其余数据集和时间划分未逐项核实。
**限制与区分：** 这是动态图任务；Cora 静态随机边划分不能直接复现其时间外推结论。
**对 FL-NCNC 的借鉴：** 借鉴模糊表示与结构/时间证据结合；静态 NCNC 需单独设计补全任务适配。

来源：[来源 1](https://ieeexplore.ieee.org/abstract/document/10286559) · [来源 2](https://github.com/MrYaoH/FuzzyDGL)
代码：https://github.com/MrYaoH/FuzzyDGL。作者关联仓库已核验；未运行复现。

### F．模糊语义、逻辑算子与知识推理

<a id="p20"></a>
#### P20．FSKGE

**FSKGE: Fuzzy spatio-temporal knowledge graph embedding**

作者：Xinhai Hu; Ming Sun; Chao Yang
发表：Neurocomputing，2026。卷期 2026-03；DOI 含 2025。
任务：时序知识图谱补全。纳入状态：main。
图时间设置：动态图/时序与时空图。时空知识图谱五元组嵌入；具有时间语义，但不据此断言使用 GNN 或完成未来边外推。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 以复合向量空间中的几何操作表示时空五元组，通过元素级模糊嵌入协调模糊语义和连续时空信息。
**实验/数据范围：** 未核实
**限制与区分：** 属于知识图谱嵌入路线；摘要没有证明其依赖 GNN。
**对 FL-NCNC 的借鉴：** 可借鉴元素级不确定性区分；不作为普通图 GNN 的直接对照。

来源：[来源 1](https://www.sciencedirect.com/science/article/pii/S0925231225032096)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p21"></a>
#### P21．Time layering + fuzzy rules

**Temporal knowledge graph reasoning based on time layering and fuzzy logic rules**

作者：Luyi Bai; Qianwen Xiao; Tongji Liu; Kejie Guo
发表：Applied Soft Computing，2026。
任务：时序知识图谱补全。纳入状态：main。
图时间设置：动态图/时序与时空图。时序知识图谱推理，包含时间分层和关系时间约束。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 结合时间分层与关系谓词的模糊隶属语义进行时序知识图谱推理，避免完全刚性的时间约束。
**实验/数据范围：** 未核实
**限制与区分：** 当前依据出版社摘要/预览；是否采用 GNN 编码器和完整训练细节未核实。
**对 FL-NCNC 的借鉴：** 时间有效性与语义相关性可以分别建模，静态 Cora 无法验证这部分贡献。

来源：[来源 1](https://www.sciencedirect.com/science/article/abs/pii/S1568494626000463)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="w04"></a>
#### W04．FATKG

**FATKG: Fuzzy adaptive temporal knowledge graph reasoning**

作者：Wenjuan Yang; Guozheng Rao; Chunlei Xie; Ming Yan; Congcong Chen; Li Zhang; Shiyong Miao; Wei Qing; Changliang Yu
发表：Expert Systems with Applications，2027。DOI 含 2026，但出版卷期为 2027；不可据 DOI 断言 2026。
任务：时序知识图谱补全。纳入状态：watchlist。
图时间设置：动态图/时序与时空图。时序知识图谱推理；出版日期未核清，仅跟踪，不计入主清单。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 出版社预览介绍模糊时间隶属度、关系特定时间窗口及时间/语义贡献分离。
**实验/数据范围：** 未核实
**限制与区分：** Crossref 正式卷期为 2027-01；虽已存在出版社预览，首次在线日期未核实，暂不计入 2024–2026 主清单。
**对 FL-NCNC 的借鉴：** 作为时间模糊性路线的跟踪条目，核实时间后再决定纳入。

来源：[来源 1](https://www.sciencedirect.com/science/article/pii/S0957417426024474)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### G．非神经模糊图链接指标（扩展对照）

<a id="p29"></a>
#### P29．Robotic SP adaptation

**Prominence-guided link prediction in fuzzy robotic networks**

作者：D. Joseph Jeyakumar; V. Rajkumar; T. P. Dayana Peter; N. Gomathi
发表：Scientific Reports，2026。出版社页面：Published 2025-12-19；Version of record 2026-01-14；Sci Rep 16 (2026)。
任务：非神经模糊图 LP。纳入状态：main。
图时间设置：动态图/时序与时空图。按时间窗口构建机器人交互图；非神经模糊指标，具体时间外推评测协议仍待核。
阅读证据：公开全文已读相关部分。

**方法原理：** 将 SP 指标迁移到机器人交互图，以通信质量、资源状态等定义节点和边的模糊隶属度。
**实验/数据范围：** 未核实
**限制与区分：** 应用扩展而非 GNN 新架构；真实通信隶属输入与 Cora 二值边不同。
**对 FL-NCNC 的借鉴：** 借鉴可观测的可靠性信号，避免将模糊隶属度无依据地称为概率。

来源：[来源 1](https://www.nature.com/articles/s41598-025-31705-8)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

## 时间设置待核实

### D．神经模糊多视图融合

<a id="p03"></a>
#### P03．AFGRL（模糊多视图）

**Adaptive Deep Fuzzy Neural Network With Multi‐Headed Self‐Attention for Improving Performance of Social Network Representation Learning and Link Prediction**

作者：Linh Nguyen Thi My; Vu Nguyen; Tham Vo
发表：Concurrency and Computation: Practice and Experience，2025。在线 2025-06-17。
任务：普通图 LP；时间协议待核。纳入状态：main。
图时间设置：图时间设置待核实。现有一手证据不足以确认图结构随时间演化及评测设置；标题 dynamic、归纳泛化或多视图本身不足以判定。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 将多个 GNN 视图表示输入带多头自注意力的深层模糊神经网络，融合结构视角并处理噪声。
**实验/数据范围：** 未核实
**限制与区分：** 目前核对出版社摘要；具体隶属函数、数据划分、损失及时间外推协议未核实。不要与 AAAI 2022 同缩写模型混用。
**对 FL-NCNC 的借鉴：** 作为模糊融合对照，检查收益来自多视图、注意力还是模糊推理。

来源：[来源 1](https://onlinelibrary.wiley.com/doi/10.1002/cpe.70165)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="p04"></a>
#### P04．AFGNN

**Adaptive Inference Neuro-Fuzzy Driven Embedding Fusion for Improving Link Prediction Through Graph Neural Network**

作者：Phu Pham
发表：International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems，2026。Crossref：在线 2026-08-28、卷期 2026-10；不采用第三方页面的 7 月日期。
任务：普通图 LP；时间协议待核。纳入状态：main。
图时间设置：图时间设置待核实。现有一手证据不足以确认图结构随时间演化及评测设置；标题 dynamic、归纳泛化或多视图本身不足以判定。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 在多视图 GNN 表示之间使用自适应神经模糊推理调节融合，抑制视图融合产生的不确定性。
**实验/数据范围：** 未核实
**限制与区分：** 依据出版社提交至 Crossref 的摘要；全文规则形式、实验协议与源码仍待核实。
**对 FL-NCNC 的借鉴：** 适合对照通用模糊融合；不能仅以模糊融合本身作为 FL-NCNC 新颖性依据。

来源：[来源 1](https://www.worldscientific.com/doi/10.1142/S0218488526500340) · [来源 2](https://api.crossref.org/works/10.1142/S0218488526500340)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### G．非神经模糊图链接指标（扩展对照）

<a id="p28"></a>
#### P28．Generalized fuzzy hypergraph

**Generalized fuzzy hypergraph for link prediction and identification of influencers in dynamic social media networks**

作者：Narjes Firouzkouhi; Abbas Amini; Ahmed Bani-Mustafa; Arash Mehdizadeh; Sadeq Damrah; Ahmad Gholami; Chun Cheng; Bijan Davvaz
发表：Expert Systems with Applications，2024。ESWA 238 Part A (2024)，DOI 含 2023；首次在线日未核实。
任务：非神经模糊图 LP。纳入状态：main。
图时间设置：图时间设置待核实。现有一手证据不足以确认图结构随时间演化及评测设置；标题 dynamic、归纳泛化或多视图本身不足以判定。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 用广义 n 元模糊关系刻画多方交互，定义 FLP 链接指标及 SIR 交互指标。
**实验/数据范围：** 未核实
**限制与区分：** 是模糊超图理论/指标，不是超图神经网络；标题 dynamic 不代表已核实时间外推协议。
**对 FL-NCNC 的借鉴：** 可用于高阶关系概念对照，避免把超图指标和二元边 GNN 混为一类。

来源：[来源 1](https://researchers.westernsydney.edu.au/en/publications/generalized-fuzzy-hypergraph-for-link-prediction-and-identificati/) · [来源 2](https://doi.org/10.1016/j.eswa.2023.121736)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### U．原理待核实（仅出版元数据）

<a id="w01"></a>
#### W01．NAFGCN

**Neighborhood-Aware Fuzzy Graph Convolutional Networks for Improved Information Fusion**

作者：Bin Yu; Changzheng Zhou; Xu Tan; Zeshui Xu; Weiping Ding
发表：IEEE Transactions on Fuzzy Systems，2026。
任务：任务待核。纳入状态：watchlist。
图时间设置：图时间设置待核实。现有一手证据不足以确认图结构随时间演化及评测设置；标题 dynamic、归纳泛化或多视图本身不足以判定。
阅读证据：仅出版元数据，方法待核。

**方法原理：** 题名指向邻域感知模糊卷积；详细机制不在本轮已核验一手证据范围内。
**实验/数据范围：** 未核实
**限制与区分：** 已核对 Crossref 题名、作者、卷期；出版社全文/摘要受访问限制。暂不采信第三方长摘要中的细节。
**对 FL-NCNC 的借鉴：** 取得一手全文后重点核对模糊邻接、邻域阈值及任务。

来源：[来源 1](https://doi.org/10.1109/TFUZZ.2026.3667580)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="w02"></a>
#### W02．FHRLI / FHCRL

**Investigating All Uncertainties in Hypergraph Representation Learning and Inference**

作者：Hong-Yu Yao; Chun-Yang Zhang; Qian-Xi Tang; C. L. Philip Chen
发表：IEEE Transactions on Fuzzy Systems，2025。
任务：任务待核。纳入状态：watchlist。
图时间设置：图时间设置待核实。现有一手证据不足以确认图结构随时间演化及评测设置；标题 dynamic、归纳泛化或多视图本身不足以判定。
阅读证据：仅出版元数据，方法待核。

**方法原理：** 题名涉及超图表示与推理过程中的不确定性；暂不写入未经一手核验的公式。
**实验/数据范围：** 未核实
**限制与区分：** 已核对出版元数据；第三方摘要可发现线索，但不作为本清单技术结论依据。
**对 FL-NCNC 的借鉴：** 补全文后核实输入、传播、推理三个阶段如何分别模糊化。

来源：[来源 1](https://doi.org/10.1109/TFUZZ.2025.3573914)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

<a id="w03"></a>
#### W03．Fuzzy federated TSK

**Fuzzy Federated Graph Learning via TSK Message Passing and Contrastive Uncertainty Learning**

作者：Zhengyang Liu; Hang Yu; Yusheng Liao; Xiangfeng Luo
发表：IEEE Transactions on Fuzzy Systems，2026。
任务：任务待核。纳入状态：watchlist。
图时间设置：图时间设置待核实。现有一手证据不足以确认图结构随时间演化及评测设置；标题 dynamic、归纳泛化或多视图本身不足以判定。
阅读证据：仅出版元数据，方法待核。

**方法原理：** 题名涉及 TSK 消息传递与对比不确定性学习，并处于联邦图学习场景。
**实验/数据范围：** 未核实
**限制与区分：** 本轮只核对出版社提交元数据，未取得可读的一手方法或实验说明；不能因 FL 缩写认为与 FL-NCNC 同任务。
**对 FL-NCNC 的借鉴：** 后续核对 TSK 在消息传递中的位置和联邦任务设置。

来源：[来源 1](https://doi.org/10.1109/TFUZZ.2026.3713494)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

## 跨设置综述与其他任务

### C．可学习规则、图后件与规则解释

<a id="p17"></a>
#### P17．TSKG

**EEG-based TSK fuzzy graph neural network for driver drowsiness estimation**

作者：Haotian Chen; Jialiang Xie
发表：Information Sciences，2024。
任务：回归。纳入状态：main。
图时间设置：不适用/跨设置。EEG 疲劳程度回归与规则图学习；输入信号有时间性，不直接归为时变图学习。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 将 TSK 模糊规则视作图结构数据，利用 GCN 优化规则，并以互信息最小化和迁移学习处理 EEG 个体差异。
**实验/数据范围：** 未核实
**限制与区分：** 这里主要是 GNN 帮助优化模糊规则；任务是疲劳程度回归。
**对 FL-NCNC 的借鉴：** 区分用模糊逻辑改 GNN 与用 GNN 改模糊系统，二者可形成不同设计路线。

来源：[来源 1](https://www.sciencedirect.com/science/article/pii/S0020025524010156)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。

### R．领域综述

<a id="p31"></a>
#### P31．FGNN review

**Fuzzy Graph Neural Networks: A Comprehensive Review of Uncertainty-Aware Graph Learning**

作者：Ngoc Dan Tran; Thi Nhung Tong; Thi Kim Phung Nguyen; Thi Hong Tu Nguyen
发表：EAI Endorsed Transactions on Context-aware Systems and Applications，2025。出版社：2025-07-16。
任务：综述。纳入状态：main。
图时间设置：不适用/跨设置。领域综述跨越多种图设置，不分配到静态/动态图研究模型。
阅读证据：一手摘要/预览；完整方法和实验未逐项核验。

**方法原理：** 综述模糊 GNN 的方法、应用、不确定性处理和未来问题。
**实验/数据范围：** 未核实
**限制与区分：** 综述用作检索入口；方法与性能判断回到原论文核实。Crossref 本轮返回 404，保留出版社记录。
**对 FL-NCNC 的借鉴：** 用于扩展关键词和追踪引用，不作为单个模型有效性的直接证据。

来源：[来源 1](https://eudl.eu/doi/10.4108/eetcasa.9483) · [来源 2](https://publications.eai.eu/index.php/casa/article/view/9483)
代码：本轮未定位到已核验作者代码。本轮未定位到已核验作者代码。
