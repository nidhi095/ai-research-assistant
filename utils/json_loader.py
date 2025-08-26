import requests
import json
import os

def fetch_json(url, out='data/remote.json'):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return out
