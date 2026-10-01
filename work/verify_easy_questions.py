import os
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

easy_by_chapter = []
total_easy = 0

for ch in range(1, 21):
    fname = f'chapter{ch:02d}.json'
    fpath = os.path.join(data_dir, fname)
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        ch_data = json.load(f)
    
    ch_id = ch_data.get('chapter_id', ch)
    ch_title = ch_data.get('chapter_title', f'第{ch:02d}课')
    questions = ch_data.get('questions', [])
    
    easy_q = [q for q in questions if q.get('difficulty') == 'easy']
    total_easy += len(easy_q)
    print(f"Chapter {ch:02d} ({ch_title}): total={len(questions)}, easy={len(easy_q)}")
    easy_by_chapter.append({
        'chapter_id': ch_id,
        'chapter_title': ch_title,
        'questions': easy_q
    })

print(f"\n>>> Total Easy Questions Across 20 Chapters: {total_easy}")
