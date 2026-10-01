import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch in range(10, 16):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    questions = data['questions']
    
    # In each chapter of 10-15:
    # There are 10 questions with 'medium-high' at indices [2, 6, 10, 14, 18, 22, 26, 30, 34, 38] (ids 3, 7, 11, 15, 19, 23, 27, 31, 35, 39).
    # Roman combination questions are at ids 5, 13, 21, 29, 37.
    # We want: exactly 20 easy, 15 medium, 5 hard.
    
    # 5 Hard: The most in-depth theoretical questions among the 10 advanced ones (e.g. indices 10, 14, 22, 26, 38 -> ids 11, 15, 23, 27, 39)
    hard_ids = {11, 15, 23, 27, 39}
    
    # 15 Medium:
    # - The other 5 advanced questions (ids 3, 7, 19, 31, 35)
    # - The 5 Roman combination questions (ids 5, 13, 21, 29, 37)
    # - Plus 5 deeper practical single questions (ids 8, 25, 28, 36, 38)
    medium_ids = {3, 7, 19, 31, 35, 5, 13, 21, 29, 37, 8, 25, 28, 36, 38}
    
    # The remaining 20 questions are pure Easy (life intuition, visual judging, basic kitchen common sense):
    # ids: 1, 2, 4, 6, 9, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 30, 32, 33, 34, 40 (exactly 20 questions!)
    
    easy_count = 0
    med_count = 0
    hard_count = 0
    
    for q in questions:
        qid = q['id']
        if qid in hard_ids:
            q['difficulty'] = 'hard'
            hard_count += 1
        elif qid in medium_ids:
            q['difficulty'] = 'medium'
            med_count += 1
        else:
            q['difficulty'] = 'easy'
            easy_count += 1
    
    print(f"Chapter {ch:02d}: easy={easy_count}, medium={med_count}, hard={hard_count} (Total={len(questions)})")
    
    # Save back
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("\nAll chapters 10-15 standardized successfully!")
