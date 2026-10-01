# -*- coding: utf-8 -*-
import re, json

with open(r'work\build_mock_exam_html.py', 'r', encoding='utf-8') as f:
    src = f.read()

m = re.search(r'const\s+paperB_mcq\s*=\s*(\[[\s\S]*?\]);', src)
if not m:
    print('Not found')
    exit()

items = json.loads(m.group(1))
print(f'Total Paper B questions: {len(items)}')

outliers = []
for q in items:
    ans = q['answer']
    opts = q['options']
    lens = {k: len(v) for k, v in opts.items()}
    ans_len = lens[ans]
    other_lens = [lens[k] for k in opts if k != ans]
    avg_other = sum(other_lens) / len(other_lens)
    max_len = max(lens.values())
    min_len = min(lens.values())
    span = max_len - min_len
    
    # Check if answer is clearly the longest or options have large span
    is_ans_longest = (ans_len == max_len and ans_len - avg_other >= 6)
    is_ans_shortest = (ans_len == min_len and avg_other - ans_len >= 6)
    is_span_huge = (span >= 10)
    
    if is_ans_longest or is_ans_shortest or is_span_huge:
        outliers.append({
            'id': q['id'],
            'ans': ans,
            'lens': lens,
            'span': span,
            'question': q['question'],
            'options': opts,
            'explanation': q.get('explanation', ''),
            'reason': 'longest_ans' if is_ans_longest else ('shortest_ans' if is_ans_shortest else 'span_huge')
        })

print(f'Found {len(outliers)} questions needing length balancing in Paper B:')
for o in outliers[:15]:
    print(f"Q{o['id']} [{o['reason']}]: Ans={o['ans']} (lens: {o['lens']}, span={o['span']})")
    print(f"  Q: {o['question'][:45]}")
    for k in ['A', 'B', 'C', 'D']:
        mark = '*' if k == o['ans'] else ' '
        print(f"   {mark}{k}: {o['options'][k]} ({len(o['options'][k])})")
