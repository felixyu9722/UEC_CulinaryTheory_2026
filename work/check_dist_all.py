import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for q in data['questions']:
        ans = q.get('answer')
        counts[ans] = counts.get(ans, 0) + 1
    print(f"Chapter {ch:02d}: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']} (Total={sum(counts.values())})")
