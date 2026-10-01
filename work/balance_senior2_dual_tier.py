import json
import os
import glob
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\senior2'
files = sorted(glob.glob(os.path.join(data_dir, 'chapter*.json')))

print("Starting Dual-Tier Balancing for Senior 2 (Easy=5x4, Total=10x4)...")

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    questions = data['questions']
    easy_qs = [q for q in questions if q['difficulty'] == 'easy'] # Q1..20
    med_qs = [q for q in questions if q['difficulty'] == 'medium'] # Q21..35
    hard_qs = [q for q in questions if q['difficulty'] == 'hard'] # Q36..40 (Roman, locked)
    
    # 1. Balance Easy questions to exactly 5 A, 5 B, 5 C, 5 D
    easy_counts = Counter(q['answer'] for q in easy_qs)
    iter_easy = 0
    while any(easy_counts[k] != 5 for k in 'ABCD') and iter_easy < 200:
        iter_easy += 1
        over = max(['A', 'B', 'C', 'D'], key=lambda k: easy_counts[k])
        under = min(['A', 'B', 'C', 'D'], key=lambda k: easy_counts[k])
        swapped = False
        for q in easy_qs:
            if q['answer'] == over:
                opts = q['options']
                opts[over], opts[under] = opts[under], opts[over]
                q['answer'] = under
                easy_counts[over] -= 1
                easy_counts[under] += 1
                swapped = True
                break
        if not swapped:
            break
            
    # 2. Determine target for Medium questions so that (Medium + Hard) = 5 A, 5 B, 5 C, 5 D
    hard_counts = Counter(q['answer'] for q in hard_qs)
    target_med = {k: 5 - hard_counts[k] for k in 'ABCD'}
    
    med_counts = Counter(q['answer'] for q in med_qs)
    iter_med = 0
    while any(med_counts[k] != target_med[k] for k in 'ABCD') and iter_med < 200:
        iter_med += 1
        # Find letter where med_counts[k] > target_med[k]
        over_list = [k for k in 'ABCD' if med_counts[k] > target_med[k]]
        under_list = [k for k in 'ABCD' if med_counts[k] < target_med[k]]
        if not over_list or not under_list:
            break
        over = over_list[0]
        under = under_list[0]
        swapped = False
        for q in med_qs:
            if q['answer'] == over:
                opts = q['options']
                opts[over], opts[under] = opts[under], opts[over]
                q['answer'] = under
                med_counts[over] -= 1
                med_counts[under] += 1
                swapped = True
                break
        if not swapped:
            break
            
    # Verification
    final_easy = Counter(q['answer'] for q in easy_qs)
    final_all = Counter(q['answer'] for q in questions)
    ch_id = data.get('chapter_id')
    ok_easy = all(final_easy[k] == 5 for k in 'ABCD')
    ok_all = all(final_all[k] == 10 for k in 'ABCD')
    print(f"Chapter {ch_id:02d}: Easy={dict(final_easy)} ({'OK' if ok_easy else 'ERR'}), Total={dict(final_all)} ({'OK' if ok_all else 'ERR'})")
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("\nDual-Tier Balancing finished successfully!")
