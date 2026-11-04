"""Refresh publisher-deposited bibliographic metadata; Python standard library only."""
import concurrent.futures
import json
import time
import urllib.parse
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOIS = [
    '10.1109/TFUZZ.2025.3649146', '10.1007/978-3-032-05994-9_16',
    '10.1002/cpe.70165', '10.1142/S0218488526500340',
    '10.1109/TSMC.2023.3320749', '10.1109/TFUZZ.2024.3418902',
    '10.1109/TFUZZ.2024.3509018', '10.3233/FAIA240687',
    '10.1109/TFUZZ.2024.3465557', '10.1109/TFUZZ.2026.3667580',
    '10.1016/j.asoc.2025.113602', '10.1038/s41598-026-51027-7',
    '10.1007/s00521-026-11967-7', '10.1016/j.chaos.2026.118154',
    '10.1016/j.eswa.2024.124090', '10.1016/j.asoc.2026.115704',
    '10.1016/j.neucom.2025.132537', '10.1016/j.eswa.2026.133538',
    '10.1016/j.asoc.2026.114598', '10.1007/s40747-025-01925-6',
    '10.1007/s10791-026-09939-5', '10.26599/FIE.2024.9270039',
    '10.1016/j.eswa.2023.121736', '10.1038/s41598-025-31705-8',
    '10.1109/TNNLS.2022.3208557', '10.1016/j.ins.2024.121101',
    '10.1109/TFUZZ.2025.3573914', '10.1109/TFUZZ.2026.3713494',
    '10.4108/eetcasa.9483',
    '10.1109/TPAMI.2026.3701743',
]

FIELDS = ['DOI', 'title', 'author', 'container-title', 'type', 'publisher',
          'published', 'published-online', 'published-print', 'created',
          'volume', 'issue', 'page', 'article-number', 'URL', 'resource', 'link', 'error']

def bibliographic_fields(item):
    # Exclude full abstracts and reference lists; retain bibliographic evidence only.
    return {key:item[key] for key in FIELDS if key in item}

def fetch(doi):
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'FuzzyGNNSurvey/1.0 (bibliographic verification)'})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=35) as response:
                    item = json.load(response)['message']
                break
            except urllib.error.HTTPError as error:
                if error.code != 429 or attempt == 2:
                    raise
                time.sleep(2 * (attempt + 1))
        return doi.lower(), bibliographic_fields(item)
    except Exception as error:
        return doi.lower(), {'error': str(error)}

if __name__ == '__main__':
    destination = ROOT / 'data' / 'crossref_metadata.json'
    records = json.loads(destination.read_text()) if destination.exists() else {}
    records = {doi:bibliographic_fields(item) for doi,item in records.items()}
    missing = [doi for doi in DOIS if not records.get(doi.lower(), {}).get('title')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        records.update(pool.map(fetch, missing))
    destination.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    for doi, item in records.items():
        print(doi, json.dumps({key:item.get(key) for key in ['title', 'published', 'published-online', 'published-print', 'error']}, ensure_ascii=False))
