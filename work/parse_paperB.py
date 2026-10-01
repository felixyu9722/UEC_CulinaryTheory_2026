# -*- coding: utf-8 -*-
import sys, os, re, json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'work\build_mock_exam_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const\s+paperB_mcq\s*=\s*(\[[\s\S]*?\]);', text)
b_text = m.group(1)

# Match individual question blocks: {id: ..., exp: '...'}
# To handle \' inside strings, we can use (?:\\.|[^\'])*
str_pat = r"'(?:\\.|[^'])*'"

q_pat = re.compile(
    rf"\{{\s*id:\s*(\d+)\s*,\s*g:\s*({str_pat})\s*,\s*src:\s*({str_pat})\s*,\s*q:\s*({str_pat})\s*,\s*opts:\s*\{{\s*A:\s*({str_pat})\s*,\s*B:\s*({str_pat})\s*,\s*C:\s*({str_pat})\s*,\s*D:\s*({str_pat})\s*\}}\s*,\s*ans:\s*({str_pat})\s*,\s*exp:\s*({str_pat})\s*\}}"
)

def clean_str(s):
    # remove leading/trailing single quotes and unescape \'
    if s.startswith("'") and s.endswith("'"):
        s = s[1:-1]
    return s.replace(r"\'", "'")

matches = q_pat.findall(b_text)
print(f"Total matched questions in Paper B: {len(matches)}")

questions = []
for m in matches:
    qid, g, src, q, optA, optB, optC, optD, ans, exp = m
    questions.append({
        'id': int(qid),
        'g': clean_str(g),
        'src': clean_str(src),
        'q': clean_str(q),
        'opts': {
            'A': clean_str(optA),
            'B': clean_str(optB),
            'C': clean_str(optC),
            'D': clean_str(optD)
        },
        'ans': clean_str(ans),
        'exp': clean_str(exp)
    })

with open(r'work\paperB_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved {len(questions)} questions to work/paperB_parsed.json")

# Now audit length bias
print("\n=== AUDITING LENGTH BIAS IN PAPER B ===")
severe_bias = []
for q in questions:
    ans = q['ans']
    opts = q['opts']
    lens = {k: len(v) for k, v in opts.items()}
    ans_len = lens[ans]
    other_lens = [lens[k] for k in opts if k != ans]
    avg_other = sum(other_lens) / len(other_lens)
    max_len = max(lens.values())
    min_len = min(lens.values())
    span = max_len - min_len

    is_longest = (ans_len == max_len and ans_len - avg_other >= 6)
    is_shortest = (ans_len == min_len and avg_other - ans_len >= 6)
    huge_span = span >= 10

    if is_longest or is_shortest or huge_span:
        severe_bias.append(q)
        print(f"Q{q['id']} [Ans: {ans}, Span: {span}]: AnsLen={ans_len}, AvgOthers={avg_other:.1f}")
        print(f"  Q: {q['q']}")
        for k in ['A', 'B', 'C', 'D']:
            mark = '👉(CORRECT)' if k == ans else '          '
            print(f"   {mark} {k}: {opts[k]} [长度: {lens[k]}]")
        print()

print(f"Total questions with length imbalance: {len(severe_bias)} / 60")
