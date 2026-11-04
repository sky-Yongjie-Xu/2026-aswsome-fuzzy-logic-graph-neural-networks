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

def group(p):
    if p['id']=='P22':return 'C'
    if p['category']=='hypergraph':return 'B' if p['id']=='P14' else 'A'
    return MAP[p['category']]

def esc(s):return str(s).replace('|',' / ').replace('\n',' ')
def row(p):
    code=f"[作者代码]({p['code_url']})" if p['code_url'] else '未定位'
    return f"| [{p['id']}](docs/catalogue.md#{p['id'].lower()}) | {p['year']} | **{p['method']}** — [{esc(p['title'])}]({p['sources'][0]}) | {TASKS[p['task']]} | {code} |"

tables=[]
for key,label in GROUPS.items():
    papers=[p for p in P if p['scope']=='main' and group(p)==key]
    if not papers:continue
    tables.extend([f'### {key}．{label}', '', '| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |', '|---|---|---|---|---|'])
    tables.extend(row(p) for p in papers)
    tables.append('')
tables.extend(['### 时间边界文献', '', '| ID | 年份 | 方法与论文 | 已核实任务范围 | 代码 |','|---|---|---|---|---|'])
tables.extend(row(p) for p in P if p['scope']=='historical_boundary')
tables.extend(['','### 待补一手证据 / 时间待核', '', '| ID | 条目 | 状态 |','|---|---|---|'])
tables.extend(f"| [{p['id']}](docs/catalogue.md#{p['id'].lower()}) | [{p['title']}]({p['sources'][0]}) | {p['limitation_zh']} |" for p in P if p['scope']=='watchlist')

readme=(ROOT/'README.md').read_text()
start='<!-- CATALOGUE:START -->';end='<!-- CATALOGUE:END -->'
prefix,rest=readme.split(start,1);_,suffix=rest.split(end,1)
(ROOT/'README.md').write_text(prefix+start+'\n\n'+'\n'.join(tables)+'\n\n'+end+suffix)

cards=['# 逐篇方法与证据卡片','', '核对日期：2026-11-04。分类是本仓库的整理；“借鉴点”是分析建议，不是原论文已证明的结论。',
 '代码“未定位”只表示本轮检索未确认，不能理解为作者没有公开代码。','', '[返回总览](../README.md) · [分类原理](taxonomy.md) · [链接预测与 FL-NCNC](link-prediction.md)','']
for p in P:
    cards += [f"<a id=\"{p['id'].lower()}\"></a>",f"## {p['id']}．{p['method']}",'',
       f"**{p['title']}**",'',f"作者：{'; '.join(p['authors'])}",
       f"发表：{p['venue']}，{p['year']}。{p['date_notes']}",
       f"任务：{TASKS[p['task']]}。纳入状态：{p['scope']}。",
       f"阅读证据：{LEVEL[p['evidence']]}。",'',
       f"**方法原理：** {p['mechanism_zh']}",
       f"**实验/数据范围：** {p['datasets']}",
       f"**限制与区分：** {p['limitation_zh']}",
       f"**对 FL-NCNC 的借鉴：** {p['takeaway_zh']}",'',
       '来源：'+' · '.join(f'[来源 {i+1}]({u})' for i,u in enumerate(p['sources'])),
       f"代码：{p['code_url'] or '本轮未定位到已核验作者代码'}。{p['code_status']}。",'']
(ROOT/'docs/catalogue.md').write_text('\n'.join(cards).rstrip()+'\n')

fields=['id','method','title','year','venue','doi','arxiv','principle','principle_name','category','task','scope','evidence','code_url','date_notes','mechanism_zh','limitation_zh','takeaway_zh']
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
