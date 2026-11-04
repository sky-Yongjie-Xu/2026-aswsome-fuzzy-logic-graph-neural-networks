"""Generate the catalogue, CSV, and BibTeX from the reviewed papers.json."""
import csv
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P=json.loads((ROOT/'data/papers.json').read_text())
GROUPS={
 'A':'参数、特征与表示模糊化',
 'B':'模糊关系驱动的采样与注意力',
 'C':'可学习规则、图后件与规则解释',
 'D':'神经模糊多视图融合',
 'E':'模糊边界与训练目标',
 'F':'模糊语义、逻辑算子与知识推理',
 'G':'非神经模糊图链接指标（扩展对照）',
 'R':'领域综述',
}
MAP={'fuzzy_representation':'A','sampling':'B','rule_consequent':'C',
 'interpretable_rules':'C','fusion':'D','objective':'E','kg_reasoning':'F',
 'non_neural':'G','review':'R'}
TASKS={
 'static_lp':'静态普通图 LP', 'graph_lp_protocol_unverified':'普通图 LP；时间协议待核',
 'dynamic_lp':'动态图 LP', 'node_community':'节点分类/社区发现',
 'node_classification':'节点分类', 'node_clustering':'节点分类/聚类', 'node_graph_classification':'节点/图分类',
 'node_prediction':'节点预测', 'representation_learning':'表示学习；LP 协议待核',
 'tabular_classification':'表格构图分类', 'hypergraph_node_classification':'超图节点分类',
 'medical_classification':'医学分类', 'regression':'回归', 'kg_completion':'知识图谱补全',
 'temporal_kg_completion':'时序知识图谱补全', 'complex_query':'复杂逻辑查询',
 'fuzzy_graph_lp':'非神经模糊图 LP', 'review':'综述', 'unverified':'任务待核',
}
LEVEL={'fulltext':'公开全文已读相关部分','local_fulltext':'用户提供全文已读相关部分（不分发全文）',
 'abstract':'一手摘要/预览；完整方法和实验未逐项核验','metadata_only':'仅出版元数据，方法待核'}
SETTINGS={
 'static':('静态图工作','static-graphs.md','固定图、独立图样本或没有显式时间维度的任务。静态普通图 LP、静态 KG、节点/图分类分别注明，不混比实验数值。'),
 'dynamic':('动态图与时序/时空图工作','dynamic-graphs.md','区分普通动态图链接预测、时序/时空知识图谱，以及非神经时变图指标。包含时间语义不自动表示使用 GNN，也不自动证明采用未来边外推协议。'),
 'unverified':('时间设置待核实','temporal-unverified.md','一手证据不足时不强行归类。多视图、训练中动态采样、归纳预测以及题名中的 dynamic 都不能单独证明图结构随时间演化。'),
 'not_applicable':('跨设置综述与其他任务','other-settings.md','综述和不能直接按静态/动态图任务解释的规则图回归工作单列。'),
}

def group(p):
    if p['id']=='P22':return 'C'
    if p['category']=='hypergraph':return 'B' if p['id']=='P14' else 'A'
    return MAP[p['category']]

def esc(s):return str(s).replace('|',' / ').replace('\n',' ')
def row(p, prefix='docs/'):
    code=f"[作者代码]({p['code_url']})" if p['code_url'] else '未定位'
    status={'historical_boundary':'（历史边界）','watchlist':'（待核/跟踪）'}.get(p['scope'],'')
    return f"| [{p['id']}]({prefix}catalogue.md#{p['id'].lower()}) | {p['year']} | **{p['method']}**{status} — [{esc(p['title'])}]({p['sources'][0]}) | {TASKS[p['task']]} | {code} |"

def block(papers,prefix):
    lines=['| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |','|---|---|---|---|---|']
    return lines+[row(p,prefix) for p in papers]+['']

tables=[]
for setting,(name,filename,intro) in SETTINGS.items():
    papers=[p for p in P if p['graph_setting']==setting]
    main=[p for p in papers if p['scope']=='main']
    tables += [f'### [{name}](docs/{filename})','',f'{intro} 共 {len(papers)} 条，其中主清单 {len(main)} 条。','']
    tables += block(papers,'docs/')
    page=[f'# {name}','','[返回总览](../README.md) · [静态图](static-graphs.md) · [动态图/时序图](dynamic-graphs.md) · [时间设置待核](temporal-unverified.md)','',intro,'',
          f'本页共 {len(papers)} 条：主清单 {len(main)} 条；时间边界/跟踪 {len(papers)-len(main)} 条。纳入状态与图时间类型是两个独立标签。','']
    if setting=='dynamic':
        sections=[('普通动态图链接预测',lambda p:p['task']=='dynamic_lp'),
                  ('时序/时空知识图谱',lambda p:p['task']=='temporal_kg_completion'),
                  ('非神经时变图指标',lambda p:p['task']=='fuzzy_graph_lp')]
    else:
        sections=[(f'{key}．{label}',lambda p,key=key:group(p)==key) for key,label in GROUPS.items()]
    for heading,predicate in sections:
        selected=[p for p in main if predicate(p)]
        if selected:page += [f'## {heading}','']+block(selected,'')
    extra=[p for p in papers if p['scope']!='main']
    if extra:page += ['## 边界与跟踪条目（不计入主清单）','']+block(extra,'')
    page += ['## 分类依据与使用边界','','| ID | 分类依据 |','|---|---|']
    page += [f"| [{p['id']}](catalogue.md#{p['id'].lower()}) | {p['temporal_evidence_zh']} |" for p in papers]
    page += ['', '原理、实验范围及原始来源见各 ID 的逐篇卡片。本页分类不新增原论文未报告的实验结论。','']
    (ROOT/'docs'/filename).write_text('\n'.join(page))

readme=(ROOT/'README.md').read_text()
start='<!-- CATALOGUE:START -->';end='<!-- CATALOGUE:END -->'
prefix,rest=readme.split(start,1);_,suffix=rest.split(end,1)
(ROOT/'README.md').write_text(prefix+start+'\n\n'+'\n'.join(tables)+'\n\n'+end+suffix)

cards=['# 逐篇方法与证据卡片','', '核对日期：2026-11-04。分类是本仓库的整理；“借鉴点”是分析建议，不是原论文已证明的结论。',
 '代码“未定位”只表示本轮检索未确认，不能理解为作者没有公开代码。','', '[返回总览](../README.md) · [分类原理](taxonomy.md) · [链接预测与 FL-NCNC](link-prediction.md)','']
ordered=sorted(P,key=lambda p:list(SETTINGS).index(p['graph_setting']))
last_setting=None
for p in ordered:
    if p['graph_setting']!=last_setting:
        last_setting=p['graph_setting']
        cards += [f"## {SETTINGS[last_setting][0]}",'']
    cards += [f"<a id=\"{p['id'].lower()}\"></a>",f"### {p['id']}．{p['method']}",'',
       f"**{p['title']}**",'',f"作者：{'; '.join(p['authors'])}",
       f"发表：{p['venue']}，{p['year']}。{p['date_notes']}",
       f"任务：{TASKS[p['task']]}。纳入状态：{p['scope']}。",
       f"图时间设置：{p['graph_setting_name']}。{p['temporal_evidence_zh']}",
       f"阅读证据：{LEVEL[p['evidence']]}。",'',
       f"**方法原理：** {p['mechanism_zh']}",
       f"**实验/数据范围：** {p['datasets']}",
       f"**限制与区分：** {p['limitation_zh']}",
       f"**对 FL-NCNC 的借鉴：** {p['takeaway_zh']}",'',
       '来源：'+' · '.join(f'[来源 {i+1}]({u})' for i,u in enumerate(p['sources'])),
       f"代码：{p['code_url'] or '本轮未定位到已核验作者代码'}。{p['code_status']}。",'']
(ROOT/'docs/catalogue.md').write_text('\n'.join(cards).rstrip()+'\n')

fields=['id','method','title','year','venue','doi','arxiv','graph_setting','graph_setting_name','temporal_evidence_zh','principle','principle_name','category','task','scope','evidence','code_url','date_notes','mechanism_zh','limitation_zh','takeaway_zh']
with (ROOT/'data/papers.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');writer.writeheader()
    for p in P:writer.writerow({k:p.get(k) for k in fields})

def tex(s):
    return str(s).replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#')
bib=[]
for p in P:
    kind='misc' if p['arxiv'] and not p['doi'] else 'article'
    if p['id'] in ['P01','P08','P10','P23','P24']:kind='inproceedings'
    venue_key='booktitle' if kind=='inproceedings' else ('journal' if kind=='article' else 'howpublished')
    data={'title':'{'+tex(p['title'])+'}', 'author':tex(' and '.join(p['authors'])),
       'year':str(p['year']),venue_key:tex(p['venue']),'url':p['sources'][0]}
    if p['doi']:data['doi']=p['doi']
    if p['arxiv']:data.update(eprint=p['arxiv'],archivePrefix='arXiv')
    if p['date_notes']:data['note']=tex(p['date_notes'])
    bib += ['@'+kind+'{fuzzygnn_'+p['id'].lower()+',']
    bib += ['  '+k+' = {'+v+'},' for k,v in data.items()]
    bib += ['}','']
(ROOT/'references.bib').write_text('\n'.join(bib))
print(f'Exported {len(P)} records; main={sum(p["scope"]=="main" for p in P)}; code={sum(bool(p["code_url"]) for p in P)}')
