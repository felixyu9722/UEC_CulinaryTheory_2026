import json
import os
import glob
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\senior2'

files = sorted(glob.glob(os.path.join(data_dir, 'chapter*.json')))
print(f"Balancing answer keys for {len(files)} chapters in Senior 2...")

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = data['questions']
    counts = Counter(q['answer'] for q in questions)
    
    # Only swap single-choice questions (Q1 to Q35)
    single_qs = [q for q in questions if q['id'] < 36]
    
    iteration = 0
    while any(counts[k] != 10 for k in 'ABCD') and iteration < 500:
        iteration += 1
        over_letter = max(['A', 'B', 'C', 'D'], key=lambda k: counts[k])
        under_letter = min(['A', 'B', 'C', 'D'], key=lambda k: counts[k])
        
        swapped = False
        for q in single_qs:
            if q['answer'] == over_letter:
                opts = q['options']
                # swap options text
                opts[over_letter], opts[under_letter] = opts[under_letter], opts[over_letter]
                q['answer'] = under_letter
                counts[over_letter] -= 1
                counts[under_letter] += 1
                swapped = True
                break
        
        if not swapped:
            print(f"Warning: could not find question to swap in {fpath}")
            break
            
    # Verify final counts
    final_counts = Counter(q['answer'] for q in questions)
    ch_id = data.get('chapter_id', os.path.basename(fpath))
    print(f"Chapter {ch_id:02d}: {dict(final_counts)} - {'PERFECT 10x4' if all(final_counts[k] == 10 for k in 'ABCD') else 'FAILED'}")
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSenior 2 answer balancing complete!")
