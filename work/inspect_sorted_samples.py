import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

check_targets = [
    (1, 5), (1, 13), (1, 21), (6, 5), (7, 37), (8, 37), (10, 5), (14, 5)
]

for ch, qid in check_targets:
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for q in data['questions']:
        if q['id'] == qid:
            print(f"=== Ch{ch:02d} Q{qid:02d} (ans={q['answer']}) ===")
            print(q['question'][:80])
            for k in ['A', 'B', 'C', 'D']:
                print(f"   {k}: {q['options'][k]}")
            print()
