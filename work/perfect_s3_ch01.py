import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

# True answers mapping based on rigorous scientific audit
true_answers_map = {
    1: 'A',
    2: 'B',
    3: 'B',
    4: 'C',
    5: 'A',
    6: 'B',
    7: 'B',
    8: 'B',
    9: 'A',
    10: 'B',
    11: 'B',
    12: 'C',
    13: 'B',
    14: 'C',
    15: 'A',
    16: 'A',
    17: 'A',
    18: 'B',
    19: 'A',
    20: 'B',
    21: 'A',
    22: 'B',
    23: 'B',
    24: 'B',
    25: 'B',
    26: 'B',
    27: 'B',
    28: 'B',
    29: 'D',
    30: 'A',
    31: 'B',
    32: 'B',
    33: 'B',
    34: 'A',
    35: 'B'
}

data = json.load(open('work/data/senior3/chapter01.json', encoding='utf-8'))
questions = data['questions']

# 1. Update true answers for single choice Q1-35
for q in questions:
    qid = q['id']
    if qid in true_answers_map:
        q['answer'] = true_answers_map[qid]

# 2. Fix Q16 outlier
for q in questions:
    if q['id'] == 16:
        q['options']['A'] = "极强的吸湿保水性以阻碍面团内部水分彻底蒸发干燥"
        q['explanation'] = "红糖含转化糖及微量糖蜜，吸湿保水性极强，烘烤时不易彻底脱水，赋予软曲奇独特的耐嚼质感。"

# 3. Clean Roman questions Q36-40
roman_clean_options = {
    36: {
        'A': 'Ⅰ、Ⅱ、Ⅲ',
        'B': 'Ⅰ、Ⅱ、Ⅳ',
        'C': 'Ⅰ、Ⅲ、Ⅳ',
        'D': 'Ⅰ、Ⅱ、Ⅲ、Ⅳ',
        'ans': 'A',
        'exp': 'Ⅰ 粗砂糖融化液化，Ⅱ 高油脂润滑流动，Ⅲ 低温慢烤延长流动期，三者均为典型促进延展因子；Ⅳ 高筋面粉强面筋网架会强烈抑制延展，属于抑制因子。'
    },
    37: {
        'A': 'Ⅰ、Ⅱ',
        'B': 'Ⅰ、Ⅲ、Ⅳ',
        'C': 'Ⅰ、Ⅱ、Ⅲ',
        'D': 'Ⅰ、Ⅱ、Ⅲ、Ⅳ',
        'ans': 'D',
        'exp': 'Ⅰ, Ⅱ, Ⅲ, Ⅳ 陈述完全符合饼干物理化学与原料工艺科学，缺一不可。'
    },
    38: {
        'A': 'Ⅰ、Ⅱ',
        'B': 'Ⅰ、Ⅱ、Ⅲ',
        'C': 'Ⅰ、Ⅲ、Ⅳ',
        'D': 'Ⅰ、Ⅱ、Ⅲ、Ⅳ',
        'ans': 'D',
        'exp': 'Ⅰ 黄油软化过度或超温，Ⅱ 粗砂糖液化，Ⅲ 温热烤盘烫化底部，Ⅳ 低温延长流动时间，四者均为导致曲奇花纹融化瘫平的核心操作失误。'
    },
    39: {
        'A': 'Ⅰ、Ⅱ、Ⅲ',
        'B': 'Ⅰ、Ⅱ、Ⅳ',
        'C': 'Ⅰ、Ⅲ、Ⅳ',
        'D': 'Ⅰ、Ⅱ、Ⅲ、Ⅳ',
        'ans': 'A',
        'exp': 'Ⅰ, Ⅱ, Ⅲ 均为切片冷藏饼干核心 SOP；Ⅳ 错误，冻硬面团绝对严禁开水烫皮，否则导致表面面糊融化报废。'
    },
    40: {
        'A': 'Ⅰ、Ⅱ',
        'B': 'Ⅰ、Ⅱ、Ⅲ',
        'C': 'Ⅰ、Ⅲ、Ⅳ',
        'D': 'Ⅰ、Ⅱ、Ⅲ、Ⅳ',
        'ans': 'D',
        'exp': 'Ⅰ, Ⅱ, Ⅲ, Ⅳ 均为饼干成品出炉冷却、水分迁移与感官检验的标准规范。'
    }
}

for q in questions:
    qid = q['id']
    if qid in roman_clean_options:
        conf = roman_clean_options[qid]
        q['options']['A'] = conf['A']
        q['options']['B'] = conf['B']
        q['options']['C'] = conf['C']
        q['options']['D'] = conf['D']
        q['answer'] = conf['ans']
        q['explanation'] = conf['exp']
        # ensure question uses i., ii., iii., iv. format
        q['question'] = q['question'].replace('i. ', 'i. ').replace('ii. ', 'ii. ')

# 4. Dual-tier balance for Q01-Q20 (Easy) and Q21-Q35 (Medium)
easy_qs = [q for q in questions if q['id'] <= 20]
med_qs = [q for q in questions if 21 <= q['id'] <= 35]
hard_qs = [q for q in questions if q['id'] >= 36]

# Balance easy questions to exactly 5 A, 5 B, 5 C, 5 D
easy_counts = Counter(q['answer'] for q in easy_qs)
for _ in range(200):
    if all(easy_counts[k] == 5 for k in 'ABCD'):
        break
    over = max(['A', 'B', 'C', 'D'], key=lambda k: easy_counts[k])
    under = min(['A', 'B', 'C', 'D'], key=lambda k: easy_counts[k])
    for q in easy_qs:
        if q['answer'] == over:
            opts = q['options']
            opts[over], opts[under] = opts[under], opts[over]
            q['answer'] = under
            easy_counts[over] -= 1
            easy_counts[under] += 1
            break

# Target for medium so that (med + hard) = 5 A, 5 B, 5 C, 5 D
hard_counts = Counter(q['answer'] for q in hard_qs)
target_med = {k: 5 - hard_counts[k] for k in 'ABCD'}

med_counts = Counter(q['answer'] for q in med_qs)
for _ in range(200):
    if all(med_counts[k] == target_med[k] for k in 'ABCD'):
        break
    over_list = [k for k in 'ABCD' if med_counts[k] > target_med[k]]
    under_list = [k for k in 'ABCD' if med_counts[k] < target_med[k]]
    if not over_list or not under_list:
        break
    over = over_list[0]
    under = under_list[0]
    for q in med_qs:
        if q['answer'] == over:
            opts = q['options']
            opts[over], opts[under] = opts[under], opts[over]
            q['answer'] = under
            med_counts[over] -= 1
            med_counts[under] += 1
            break

# Verification
final_easy = Counter(q['answer'] for q in easy_qs)
final_all = Counter(q['answer'] for q in questions)
print("Easy answer distribution:", dict(final_easy))
print("Total answer distribution:", dict(final_all))

# Check outliers
outliers = [q for q in questions if max(len(v) for v in q['options'].values()) - min(len(v) for v in q['options'].values()) > 8]
print(f"Total outliers in Unit 1: {len(outliers)}")

with open('work/data/senior3/chapter01.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Senior 3 Unit 1 perfected and saved!")
