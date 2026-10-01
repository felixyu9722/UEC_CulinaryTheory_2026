import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

raw_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\07_统考标准复习题库与命题提示词\高三\第01单元_饼干\高三_第01单元_饼干_统考标准复习题（完整样卷含深度解析）.txt'

with open(raw_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Parse answer keys
answers = {}
# Single choice: 01-05: A, B, C, D, A
ans_block = re.search(r'【标准答案】：\s*(.*?)\s*【答案分布', text, re.DOTALL)
if ans_block:
    for line in ans_block.group(1).strip().split('\n'):
        m = re.match(r'(\d+)-(\d+):\s*([A-D,\s]+)', line)
        if m:
            start_num = int(m.group(1))
            letters = [l.strip() for l in m.group(3).split(',') if l.strip()]
            for offset, letter in enumerate(letters):
                answers[start_num + offset] = letter

# Roman choice: 36. 【答案】A ...
for m in re.finditer(r'(\d+)\.\s*【答案】([A-D])', text):
    answers[int(m.group(1))] = m.group(2)

print(f"Total answers extracted: {len(answers)}")

# Parse explanations
exps = {}
# Roman exps: 36. 【答案】A（...）
for m in re.finditer(r'(\d+)\.\s*【答案】[A-D]（(.*?)）', text):
    exps[int(m.group(1))] = m.group(2).strip()

# Single exps: • 第 01 题：饼干分类依据。...
for m in re.finditer(r'•\s*第\s*0?(\d+)\s*题[：:](.*?)(?=(?:•\s*第\s*\d+\s*题|二、|三、|$))', text, re.DOTALL):
    qid = int(m.group(1))
    exps[qid] = m.group(2).strip()

print(f"Total explanations extracted: {len(exps)}")

# Parse questions
# Questions 1 to 35
# Pattern: \n(\d+)\.\s*(.*?)\nA\.\s*(.*?)\nB\.\s*(.*?)\nC\.\s*(.*?)\nD\.\s*(.*?)(?=\n\d+\.|\n-{10,}|\n二、|\n乙组|$)
q_pattern = re.compile(r'(?:^|\n)(\d+)\.\s*(.*?)\n\s*A\.\s*(.*?)\n\s*B\.\s*(.*?)\n\s*C\.\s*(.*?)\n\s*D\.\s*(.*?)(?=(?:\n\s*\d+\.|\n-{10,}|\n二、|\n乙组|\n【参考答案|$))', re.DOTALL)

parsed_qs = []
for m in q_pattern.finditer(text):
    qid = int(m.group(1))
    if qid > 40:
        continue
    q_text = m.group(2).strip()
    opt_a = m.group(3).strip()
    opt_b = m.group(4).strip()
    opt_c = m.group(5).strip()
    opt_d = m.group(6).strip()
    
    # difficulty: 1..20 easy, 21..35 medium, 36..40 hard
    diff = 'easy' if qid <= 20 else ('medium' if qid <= 35 else 'hard')
    q_type = 'roman' if qid >= 36 else 'single'
    
    ans = answers.get(qid, 'A')
    exp = exps.get(qid, f"本题考查第01单元饼干核心工艺与物理化学变化，正确答案为 {ans}。")
    
    parsed_qs.append({
        'id': qid,
        'difficulty': diff,
        'type': q_type,
        'question': q_text,
        'options': {
            'A': opt_a,
            'B': opt_b,
            'C': opt_c,
            'D': opt_d
        },
        'answer': ans,
        'explanation': exp
    })

print(f"Total parsed questions: {len(parsed_qs)}")
parsed_qs.sort(key=lambda x: x['id'])

ch1_data = {
    'chapter_id': 1,
    'chapter_title': '第01单元 饼干制作工艺与延展率控制',
    'intro': '本单元深入探讨西式饼干四大分类（挤出、切片、擀压、滴落）、流变学塑性、延展率（Spread Ratio）影响因素（糖粒粗细、油脂配比、面筋抑制与炉温升降曲线）以及后厨常见缺陷纠偏。',
    'questions': parsed_qs
}

out_path = 'work/data/senior3/chapter01.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(ch1_data, f, ensure_ascii=False, indent=2)

print(f"Saved to {out_path}")
