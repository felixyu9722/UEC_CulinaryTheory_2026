import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

roman_issues = []
length_bias_issues = []

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    for q in data.get('questions', []):
        opts = q.get('options', {})
        opt_texts = [opts[k] for k in ['A', 'B', 'C', 'D']]
        lengths = [len(t) for t in opt_texts]
        max_len = max(lengths)
        min_len = min(lengths)
        ans_len = len(opts.get(q.get('answer', 'A'), ''))
        
        # Check Roman questions
        is_roman = q.get('type') in ['roman', 'combination'] or any('Ⅰ' in q['question'] or 'i.' in q['question'] for _ in [1])
        if is_roman:
            roman_issues.append((ch, q['id'], q['question'][:40], opts))
            
        # Check Length Bias (difference >= 10 chars, or correct ans is outlier)
        if max_len - min_len >= 12:
            length_bias_issues.append((ch, q['id'], q.get('answer'), max_len - min_len, lengths))

print(f"Total Roman Questions Found: {len(roman_issues)}")
print(f"Total Length Bias Issues Found: {len(length_bias_issues)}")

print("\n--- Sample Roman Questions Options ---")
for issue in roman_issues[:6]:
    print(f"Ch{issue[0]:02d} Q{issue[1]:02d}:")
    for k in ['A', 'B', 'C', 'D']:
        print(f"   {k}: {issue[3].get(k)}")

print("\n--- Sample Length Bias Questions ---")
for issue in length_bias_issues[:6]:
    print(f"Ch{issue[0]:02d} Q{issue[1]:02d}: ans={issue[2]}, diff={issue[3]}, lengths={issue[4]}")
