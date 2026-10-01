import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    questions = data['questions']
    
    # Count current answers
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for q in questions:
        counts[q['answer']] += 1
    
    # Rebalance ONLY using single choice questions (type == 'single' and no Roman in question)
    single_qs = [q for q in questions if q.get('type') == 'single' and 'Ⅰ' not in q['question'] and 'i.' not in q['question']]
    
    iteration = 0
    while any(c != 10 for c in counts.values()) and iteration < 200:
        iteration += 1
        over_letter = max(counts, key=counts.get)
        under_letter = min(counts, key=counts.get)
        
        # Find a single question with answer == over_letter
        swapped = False
        for q in single_qs:
            if q['answer'] == over_letter:
                opts = q['options']
                tmp = opts[over_letter]
                opts[over_letter] = opts[under_letter]
                opts[under_letter] = tmp
                q['answer'] = under_letter
                counts[over_letter] -= 1
                counts[under_letter] += 1
                swapped = True
                break
        if not swapped:
            break
            
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Balanced single questions successfully without touching Roman question order!")
