import json, os, sys

sys.stdout.reconfigure(encoding='utf-8')
data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch in range(1, 21):
    fpath = f"{data_dir}/chapter{ch:02d}.json"
    d = json.load(open(fpath, encoding='utf-8-sig'))
    qs = d['questions']
    long_qs = []
    for q in qs:
        lens = [len(v) for v in q['options'].values()]
        if max(lens) >= 22:
            long_qs.append(q['id'])
    print(f"Chapter {ch:02d} ({d.get('chapter_title')}): {len(long_qs)} long questions -> {long_qs}")
