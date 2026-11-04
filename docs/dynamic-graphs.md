# 动态图与时序/时空图工作

[返回总览](../README.md) · [静态图](static-graphs.md) · [动态图/时序图](dynamic-graphs.md) · [时间设置待核](temporal-unverified.md)

区分普通动态图链接预测、时序/时空知识图谱，以及非神经时变图指标。包含时间语义不自动表示使用 GNN，也不自动证明采用未来边外推协议。

本页共 5 条：主清单 4 条；时间边界/跟踪 1 条。纳入状态与图时间类型是两个独立标签。

## 普通动态图链接预测

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P05](catalogue.md#p05) | 2024 | **FuzzyDGL** — [Fuzzy Representation Learning on Dynamic Graphs](https://ieeexplore.ieee.org/abstract/document/10286559) | 动态图 LP | [作者代码](https://github.com/MrYaoH/FuzzyDGL) |

## 时序/时空知识图谱

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P20](catalogue.md#p20) | 2026 | **FSKGE** — [FSKGE: Fuzzy spatio-temporal knowledge graph embedding](https://www.sciencedirect.com/science/article/pii/S0925231225032096) | 时序知识图谱补全 | 未定位 |
| [P21](catalogue.md#p21) | 2026 | **Time layering + fuzzy rules** — [Temporal knowledge graph reasoning based on time layering and fuzzy logic rules](https://www.sciencedirect.com/science/article/abs/pii/S1568494626000463) | 时序知识图谱补全 | 未定位 |

## 非神经时变图指标

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [P29](catalogue.md#p29) | 2026 | **Robotic SP adaptation** — [Prominence-guided link prediction in fuzzy robotic networks](https://www.nature.com/articles/s41598-025-31705-8) | 非神经模糊图 LP | 未定位 |

## 边界与跟踪条目（不计入主清单）

| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |
|---|---|---|---|---|
| [W04](catalogue.md#w04) | 2027 | **FATKG**（待核/跟踪） — [FATKG: Fuzzy adaptive temporal knowledge graph reasoning](https://www.sciencedirect.com/science/article/pii/S0957417426024474) | 时序知识图谱补全 | 未定位 |

## 分类依据与使用边界

| ID | 分类依据 |
|---|---|
| [P05](catalogue.md#p05) | 结构与时间关联的动态图表示学习，并评估动态链接预测。 |
| [P20](catalogue.md#p20) | 时空知识图谱五元组嵌入；具有时间语义，但不据此断言使用 GNN 或完成未来边外推。 |
| [P21](catalogue.md#p21) | 时序知识图谱推理，包含时间分层和关系时间约束。 |
| [P29](catalogue.md#p29) | 按时间窗口构建机器人交互图；非神经模糊指标，具体时间外推评测协议仍待核。 |
| [W04](catalogue.md#w04) | 时序知识图谱推理；出版日期未核清，仅跟踪，不计入主清单。 |

原理、实验范围及原始来源见各 ID 的逐篇卡片。本页分类不新增原论文未报告的实验结论。
