import json, sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch in [10, 12, 14, 15, 19]:
    fpath = f"{data_dir}/chapter{ch:02d}.json"
    d = json.load(open(fpath, encoding='utf-8-sig'))
    print(f"\n==================== Chapter {ch}: {d.get('chapter_title')} ====================")
    for q in d['questions']:
        lens = [len(v) for v in q['options'].values()]
        if max(lens) >= 30:
            print(f"\n[Q{q['id']} - Diff: {q['difficulty']}, Max Len: {max(lens)}]")
            print(f"题干: {q['question']}")
            for k in ['A', 'B', 'C', 'D']:
                print(f"  {k}. ({len(q['options'][k])}字) {q['options'][k]}")
            break
