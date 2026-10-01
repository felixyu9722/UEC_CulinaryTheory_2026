import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

bias_count = 0
for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for q in data['questions']:
        opts = q['options']
        lens = [len(opts[k]) for k in ['A', 'B', 'C', 'D']]
        max_l = max(lens)
        min_l = min(lens)
        ans_l = len(opts[q['answer']])
        
        # If difference > 10 chars, or correct ans is far longer than others
        if max_l - min_l > 10:
            bias_count += 1
            print(f"Ch{ch:02d} Q{q['id']:02d}: diff={max_l - min_l}, lens={lens}, ans={q['answer']}(len {ans_l})")
            print(f"   A: {opts['A']}")
            print(f"   B: {opts['B']}")
            print(f"   C: {opts['C']}")
            print(f"   D: {opts['D']}")
            print()

print(f"Total options with length difference > 10 chars: {bias_count}")
