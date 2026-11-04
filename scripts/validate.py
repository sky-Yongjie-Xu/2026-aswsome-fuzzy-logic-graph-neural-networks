"""Validate reviewed metadata, export consistency and local document links."""
import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT=Path(__file__).resolve().parents[1]
papers=json.loads((ROOT/'data/papers.json').read_text())
metadata=json.loads((ROOT/'data/crossref_metadata.json').read_text())
errors=[]

def check(condition,message):
    if not condition:errors.append(message)

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD',text).casefold() if c.isalnum())

for field in ['id','doi','arxiv']:
    values=[p[field].lower() for p in papers if p.get(field)]
    check(len(values)==len(set(values)),f'duplicate {field}')
for p in papers:
    check(bool(p['authors']) and p['title']!='待核实',f'{p["id"]}: missing bibliography')
    check(bool(p['sources']),f'{p["id"]}: missing evidence link')
    check(p['checked_on']=='2026-11-04',f'{p["id"]}: unexpected audit date')
    check(p['scope']!='main' or 2024<=p['year']<=2026,f'{p["id"]}: outside main date window')
    check(p['evidence']!='metadata_only' or p['scope']=='watchlist',f'{p["id"]}: metadata-only in main catalogue')
    check(p['scope']=='watchlist' or p.get('principle') in 'ABCDEFGR',f'{p["id"]}: missing principle category')
    check(p.get('graph_setting') in {'static','dynamic','unverified','not_applicable'},f'{p["id"]}: missing graph time setting')
    check(bool(p.get('temporal_evidence_zh')),f'{p["id"]}: missing temporal classification rationale')
    if p['task'] in {'dynamic_lp','temporal_kg_completion'}:
        check(p['graph_setting']=='dynamic',f'{p["id"]}: temporal task in wrong section')
    for url in p['sources']+([p['code_url']] if p['code_url'] else []):
        parsed=urlparse(url)
        check(parsed.scheme=='https' and bool(parsed.netloc),f'{p["id"]}: invalid URL {url}')
    if p['doi']:
        m=metadata.get(p['doi'].lower(),{})
        if m.get('title'):
            check(normalize(p['title'])==normalize(m['title'][0]),f'{p["id"]}: title differs from Crossref')
        else:
            check(p['id']=='P31',f'{p["id"]}: DOI metadata unavailable without documented exception')
    for field in ['mechanism_zh','limitation_zh','takeaway_zh']:
        check(bool(p[field]),f'{p["id"]}: empty {field}')

with (ROOT/'data/papers.csv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))
check([p['id'] for p in rows]==[p['id'] for p in papers],'CSV IDs differ from JSON')
check([p['graph_setting'] for p in rows]==[p['graph_setting'] for p in papers],'CSV graph settings differ from JSON')
setting_pages={'static':'static-graphs.md','dynamic':'dynamic-graphs.md','unverified':'temporal-unverified.md','not_applicable':'other-settings.md'}
for setting,filename in setting_pages.items():
    page=(ROOT/'docs'/filename).read_text()
    ids=set(re.findall(r'\[([PW]\d{2})\]\(catalogue.md#',page))
    check(ids=={p['id'] for p in papers if p['graph_setting']==setting},f'{filename}: missing or misplaced papers')
bib=(ROOT/'references.bib').read_text()
check(bib.count('@')==len(papers),'BibTeX record count mismatch')
for p in papers:
    check('fuzzygnn_'+p['id'].lower()+',' in bib,f'{p["id"]}: BibTeX missing')

for path in [ROOT/'README.md',*sorted((ROOT/'docs').glob('*.md'))]:
    text=path.read_text()
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if urlparse(target).scheme:continue
        file,_,anchor=unquote(target).partition('#')
        resolved=(path.parent/file).resolve() if file else path
        check(resolved.is_file(),f'{path.name}: broken local link {target}')
        if anchor and resolved.is_file() and resolved.name=='catalogue.md':
            check(f'id="{anchor}"' in resolved.read_text(),f'{path.name}: missing anchor {target}')

report={'checked_on':'2026-11-04','records':len(papers),
    'scopes':dict(Counter(p['scope'] for p in papers)),
    'graph_settings':dict(Counter(p['graph_setting'] for p in papers)),
    'evidence_levels':dict(Counter(p['evidence'] for p in papers)),
    'verified_code_links':sum(bool(p['code_url']) for p in papers),
    'errors':errors,
    'limitations':'Offline structural checks; not full-text scientific peer review or live external-link validation.'}
(ROOT/'data/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
