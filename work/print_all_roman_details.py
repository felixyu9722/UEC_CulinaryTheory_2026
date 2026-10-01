import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch in range(10, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for q in data.get('questions', []):
        if q.get('type') in ['roman', 'combination'] or 'i.' in q['question'] or 'Ⅰ' in q['question']:
            print(f"=== Ch{ch:02d} Q{q['id']:02d} ===")
            print(q['question'])
            print("ANS:", q.get('answer'))
            print("EXP:", q.get('explanation')[:80])
            print()
