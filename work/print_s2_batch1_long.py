import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for ch in range(1, 6):
    fpath = f'work/data/senior2/chapter{ch:02d}.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"==================== CH{ch:02d}: {d['chapter_title']} ====================")
    for q in d['questions'][:35]:
        max_len = max(len(v) for v in q['options'].values())
        if max_len >= 20:
            print(f"\nQ{q['id']} (Ans: {q['answer']}, Diff: {q['difficulty']}): {q['question']}")
            for k, v in q['options'].items():
                print(f"  {k}: {v}")
