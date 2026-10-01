import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

for ch in range(10, 16):
    with open(rf'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\chapter{ch}.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    print(f"\n--- Chapter {ch} ---")
    for q in data['questions']:
        diff = q.get('difficulty', 'NONE')
        if diff != 'NONE':
            print(f"Q{q['id']:02d}: diff={diff}")
