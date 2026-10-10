import json, sys

sys.stdout.reconfigure(encoding='utf-8')

for grade, path, title in [
    ('Senior 1 (高一)', 'work/data/chapter10.json', '高一第10课面粉'),
    ('Senior 2 (高二)', 'work/data/senior2/chapter01.json', '高二第1单元蛋糕'),
    ('Senior 3 (高三)', 'work/data/senior3/chapter01.json', '高三第1单元饼干')
]:
    d = json.load(open(path, encoding='utf-8'))
    print(f"==================== {grade} - {title} ====================")
    for q in d['questions'][:3]:
        print(f"Q{q['id']} [ans={q['answer']}]: {q['question']}")
        for k in 'ABCD':
            print(f"  {k}. {q['options'][k]}")
        print()
