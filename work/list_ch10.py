import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

for ch in [10]:
    with open(rf'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\chapter{ch}.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    print(f"=== Chapter {ch} Questions List ===")
    for q in data['questions']:
        print(f"Q{q['id']:02d} [{q.get('type','single')}]: {q['question'][:45]}...")
