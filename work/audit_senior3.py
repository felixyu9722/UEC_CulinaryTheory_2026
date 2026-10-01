import json
import os
from collections import Counter

s3_dir = r"c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\senior3"
files = [f"chapter{i:02d}.json" for i in range(1, 9)]

total_questions = 0
all_diff_ok = True
all_balance_ok = True
all_roman_ok = True

print("=== SENIOR 3 FULL AUDIT (UNITS 01 - 08) ===")

for fname in files:
    path = os.path.join(s3_dir, fname)
    if not os.path.exists(path):
        print(f"ERROR: {fname} does not exist!")
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = json.load(f)
    
    data = content["questions"] if isinstance(content, dict) and "questions" in content else content
    
    count = len(data)
    total_questions += count
    
    easy = [q['answer'] for q in data[:20]]
    med_hard = [q['answer'] for q in data[20:]]
    total_cnt = Counter([q['answer'] for q in data])
    easy_cnt = Counter(easy)
    med_hard_cnt = Counter(med_hard)
    
    # Check diffs
    diff_issues = []
    for q in data:
        lens = [len(opt) for opt in q['options'].values()]
        if max(lens) - min(lens) > 8:
            diff_issues.append((q['id'], max(lens) - min(lens)))
            
    # Check Romans
    roman_issues = []
    for q in data[35:]:
        for opt in q['options'].values():
            if not opt.startswith('Ⅰ'):
                roman_issues.append((q['id'], opt))
                
    status = "OK"
    if count != 40 or diff_issues or roman_issues or easy_cnt != Counter({'A':5,'B':5,'C':5,'D':5}) or total_cnt != Counter({'A':10,'B':10,'C':10,'D':10}):
        status = "FAIL"
        all_diff_ok = all_diff_ok and not diff_issues
        all_balance_ok = False
        all_roman_ok = all_roman_ok and not roman_issues
        
    print(f"[{status}] {fname}: Qs={count}, Diff>8={len(diff_issues)}, RomanBad={len(roman_issues)}, Easy={dict(easy_cnt)}, Total={dict(total_cnt)}")
    if diff_issues:
        print(f"    Diff issues: {diff_issues}")
    if roman_issues:
        print(f"    Roman issues: {roman_issues}")

print("-------------------------------------------")
print(f"Total Senior 3 Questions: {total_questions} / 320")
if total_questions == 320 and all_diff_ok and all_balance_ok and all_roman_ok:
    print(">>> ALL 8 UNITS OF SENIOR 3 PASSED 100% RIGOROUS AUDIT! <<<")
else:
    print(">>> AUDIT HAD FAILURES, REVIEW ABOVE <<<")
