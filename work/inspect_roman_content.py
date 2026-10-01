import json, sys
sys.stdout.reconfigure(encoding='utf-8')

for ch in [10, 11, 12, 13, 14, 15]:
    with open(rf'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\chapter{ch}.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    print(f"\n==================== CHAPTER {ch} ====================")
    for q in data['questions']:
        if q['id'] in [5, 13, 21, 29, 37]:
            print(f"--- Q{q['id']:02d} ---")
            print(q['question'])
            print(f"Answer: {q['answer']}")
            print(f"Options: {q['options']}")
            print(f"Explanation: {q['explanation'][:100]}...\n")
