import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'work\data\senior2'
total_questions = 0
total_easy = 0
total_roman = 0

print("=== SENIOR 2 (高二) 15 CHAPTERS QUALITY AUDIT ===")
for ch in range(1, 16):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    qs = data['questions']
    total_questions += len(qs)
    
    ans_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    roman_count = 0
    easy_count = 0
    outliers = []
    
    for q in qs:
        ans = q.get('answer', '')
        if ans in ans_counts:
            ans_counts[ans] += 1
        if q.get('type') == 'roman':
            roman_count += 1
            total_roman += 1
        if q.get('difficulty') == 'easy':
            easy_count += 1
            total_easy += 1
            
        opts = q.get('options', {})
        if len(opts) == 4:
            lens = [len(str(v)) for v in opts.values()]
            if max(lens) - min(lens) > 10 and q.get('type') != 'roman':
                outliers.append(q['id'])
                
    title = data.get('chapter_title', f'Chapter {ch}')
    print(f"Ch{ch:02d} ({title[:18]}): Questions={len(qs)}, Ans={ans_counts}, Roman={roman_count}, Easy={easy_count}, Length Outliers={len(outliers)}")

print(f"\nAudit Summary: Total Questions={total_questions}, Total Easy={total_easy}, Total Roman={total_roman}")
