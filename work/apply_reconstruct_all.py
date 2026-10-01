import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Import our reconstructed definitions
sys.path.append(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work')
from reconstruct_part1 import reconstructed_roman
from reconstruct_part2 import reconstructed_roman_part2

all_reconstructed = {}
all_reconstructed.update(reconstructed_roman)
all_reconstructed.update(reconstructed_roman_part2)

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

for ch, q_list in all_reconstructed.items():
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        ch_data = json.load(f)
    
    questions = ch_data.get('questions', [])
    q_map = {q['id']: q for q in q_list}
    
    for i, orig_q in enumerate(questions):
        qid = orig_q['id']
        if qid in q_map:
            new_q = q_map[qid]
            orig_q['type'] = 'combination'
            orig_q['question'] = new_q['question']
            orig_q['options'] = new_q['options']
            orig_q['answer'] = new_q['answer']
            orig_q['explanation'] = new_q['explanation']
            orig_q['difficulty'] = orig_q.get('difficulty', 'medium')
    
    # Save back
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(ch_data, f, ensure_ascii=False, indent=2)
    print(f"Chapter {ch:02d} updated with 5 reconstructed professional Roman questions.")

print("\nAll chapters 10-20 updated successfully!")
