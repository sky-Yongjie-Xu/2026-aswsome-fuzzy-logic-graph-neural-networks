# 检索与核验记录

## 范围

- 检索与核对截止日期：2026-11-04（Asia/Shanghai）。
- 主窗口：2024、2025、2026 三个自然年，以正式会议/期刊卷期年组织；已存在的预印本补充纳入。
- 首次公开日与正式卷期不同则单列，不能把正式卷期晚误写成方法首次提出晚。FuzzyDGL、FIT 等明确注明更早预印本/在线版本；FGSCN 单列为历史边界。
- 核心：模糊逻辑、模糊集/模糊数、神经模糊规则与 GNN/图表示学习。优先普通图 LP，扩展到 KG、复杂查询、超图及非神经模糊 LP。
- 排除：仅因参考文献含 fuzzy、仅会议名称含 fuzzy、将 FL（联邦学习）误作模糊逻辑、普通注意力却没有可核实模糊定义，以及仅在引言提及 LP 的分类论文被算作直接 LP 工作。

本次是定向多源研究清单，未完成所有付费全文、中文数据库或逐篇引用网络的穷尽追踪；不提供虚构的 PRISMA 流程计数。

## 检索式（实际使用的代表组）

```text
"fuzzy" "graph neural" "link prediction" 2024 2025 2026
"fuzzy graph convolutional" 2024 2025
"fuzzy" "graph neural networks" 2025 TSK
"fuzzy" "link prediction" "temporal" neural 2024 2025 2026
"GFS-Edge" / "GFS-Node"
"Dynamic Fuzzy Sampler" / "Fuzzy Representation Learning on Dynamic Graphs"
"Mitigating Local Cohesion and Global Sparseness"
"fuzzy" "graph neural" 2025 "github"
"AFGRL" github fuzzy / "AFGNN" fuzzy github
"Fuzzy set-based re-ranking" / "FGF-GAT"
```

发现候选后，继续以完整题名、DOI、作者代码仓库核对。部分宽泛查询加入 `site:ieeexplore.ieee.org` 或排除聚合站，以定位一手证据。第三方页面用于发现线索，不直接支持方法结论。

## 来源与可读性

| 来源 | 使用方式 | 本次限制 |
|---|---|---|
| 出版社提交的 Crossref 元数据 | DOI、题名、作者、卷期、发表日期核对；个别记录含摘要 | 429 已降频重试；综述 DOI 返回 404，保留该失败而不捏造记录 |
| IEEE / Springer / Wiley / World Scientific / Elsevier | 一手摘要、预览和正式发表状态 | 部分 IEEE 页面触发验证，部分 Elsevier/World Scientific 全文访问受限 |
| arXiv / PMLR / OpenReview | 预印本、正式会议全文/元数据 | 预印本与录用版本合并时保留版本差异；投稿记录不等于录用 |
| PubMed 中作者摘要 | 核对 FGF-GAT 等作者摘要和出版信息 | 不代替付费全文的方法/数据细节 |
| 作者关联 GitHub | 核对代码是否对应正确论文 | 已核对 README 与论文关联，不代表运行通过 |
| 用户已有论文 | GFS-Edge、FuzzyGCN、DFS 的相关全文部分 | 仓库不分发原 PDF 或完整提取文本 |

本会话未提供技能所列的专用 academic-search MCP；以公开检索、出版社页面和 Crossref REST 交叉核对。原始出版记录保存在 [crossref_metadata.json](../data/crossref_metadata.json)；人工审阅后的主数据为 [papers.json](../data/papers.json)。

## 证据分级

- `fulltext`：已读公开全文相关方法/实验部分，不意味着逐字精读全部附录。
- `local_fulltext`：已读用户提供全文相关部分；不分发原文。
- `abstract`：只核对一手摘要/预览，未知细节保持未知。
- `metadata_only`：只确认出版条目，放在待核表，不支撑具体方法结论。

## 日期和同名消歧

| 条目 | 核对结果 |
|---|---|
| FGAT/FNS | arXiv 首发 2024；2025-10-01 正式收入 ICMSSP 2025 会议论文集，DOI 10.1007/978-3-032-05994-9_16；去重为一条 |
| GFS-Edge | 用户全文页脚在线 2025-12-29，正式卷期 2026-03；不能只从 DOI 中的 2025 推断年份 |
| DFS | DOI 含 2024，但用户全文标在线 2025-01-06，卷期 2025-04；dynamic 不自动指时序图任务 |
| FuzzyDGL | IEEE 标在线 2023-10-17，卷期 2024-02；主表保留更早公开说明 |
| FGSCN | 在线 2022、卷期 2024；作为历史边界条目 |
| AFGRL | 2025 模糊多视图工作，与 AAAI 2022 Augmentation-Free Self-Supervised Learning on Graphs 同名不同方法；后者代码不是前者代码 |
| AFGNN | 出版社 Crossref 在线日期 2026-08-28、卷期 2026-10；第三方出现的 7 月日期不采用 |
| FL-GNN | 正式 ECAI 2024 版本 DOI 10.3233/FAIA240687；不把另一 ICLR 投稿记录称为已录用 |
| GFS-Node / GFS-Edge | 不同任务的两篇论文；仅核验 GFS-Node 源码，不冒充 GFS-Edge 源码 |
| Robotic SP | 出版社页面在线 2025-12-19、Version of record 2026-01-14、卷期 2026，全部保留 |
| FATKG | Crossref 卷期 2027-01，已有出版社预览；首次在线日未核实，因此放跟踪表，暂不计入 2024–2026 主清单 |
| EAI 综述 | 出版社公开记录可核查；Crossref 本次 404，只表明接口没有返回记录，不否认论文存在 |

## 待完成的核查

1. AFGRL、AFGNN、FGF-GAT：补读完整公式、数据划分、消融与代码声明。
2. NAFGCN、FHRLI/FHCRL、联邦 TSK 图学习：取得可读一手摘要/全文后再写具体机制和任务。
3. FATKG：核对首次在线日期与可用版本，避免将 2027 卷期记录直接写成 2026 正式论文。
4. 未确认的代码保持“本轮未定位”，不作“无源码”断言。
5. 所有直接 LP 方法的可比性最终通过统一预处理、固定划分与负采样复现核实。

## 静态与动态图分类更新（2026-11-04）

增加 `graph_setting`、`graph_setting_name` 与 `temporal_evidence_zh` 字段，JSON、CSV、逐篇卡片及独立分类页面保持一致。静态图与动态图入口分开，后者再区分普通动态图 LP、时序/时空 KG 和非神经时变图指标。未核实时间设置和跨设置综述单列；训练过程中的采样更新不作为动态图判据，时间输入也不自动证明图拓扑演化或未来边外推。

### 内部原理分类统一

静态与动态图均采用“图时间设置 → 方法原理 → 论文”的顺序，任务类型只作为表内标签。知识推理类再区分模糊语义嵌入、时序模糊规则、逻辑真值组合和候选重排序；边界/跟踪论文留在相应原理下标注。只取得元数据的条目归入“原理待核实”，不根据题名推定机制。
