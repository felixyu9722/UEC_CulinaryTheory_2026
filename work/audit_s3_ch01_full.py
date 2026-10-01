import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open('work/data/senior3/chapter01.json', encoding='utf-8'))
print(f"Auditing Unit 1 (Total questions: {len(data['questions'])})")

for q in data['questions']:
    lens = [len(v) for v in q['options'].values()]
    diff = max(lens) - min(lens)
    print(f"Q{q['id']:02d} [ans={q['answer']}, diff={diff}]: {q['question'][:30]}...")
    if diff > 8:
        print(f"   OUTLIER! lens={lens}")
        for k, v in q['options'].items():
            print(f"     {k}. {v} ({len(v)})")
