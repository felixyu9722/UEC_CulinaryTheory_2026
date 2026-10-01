import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

roman_map = {'Ⅰ': 1, 'Ⅱ': 2, 'Ⅲ': 3, 'Ⅳ': 4, 'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'I': 1, 'II': 2, 'III': 3, 'IV': 4}

def parse_roman_items(text):
    found = []
    for m in re.finditer(r'(?:[ⅠⅡⅢⅣ]|[ivxIVX]+)', text):
        val = m.group(0)
        if val in roman_map:
            found.append(roman_map[val])
        elif val.upper() in roman_map:
            found.append(roman_map[val.upper()])
    res = []
    for x in found:
        if x not in res:
            res.append(x)
    if '皆正确' in text or '全部正确' in text or '全对' in text or set(res) == {1, 2, 3, 4}:
        return [1, 2, 3, 4]
    return sorted(res)

def roman_sort_key(opt_text):
    items = parse_roman_items(opt_text)
    if not items:
        return (99, 99, [opt_text])
    length = len(items)
    first_item = items[0]
    # If it's all 4 items, put it at the very end
    if length == 4:
        return (10, 4, items)
    # Primary: starting item (1, 2, 3...)
    # Secondary: length of items (2 items before 3 items)
    # Tertiary: the exact item tuple for tie-breaking
    return (first_item, length, items)

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

updated_roman_count = 0

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    questions = data['questions']
    for q in questions:
        is_roman = q.get('type') in ['roman', 'combination'] or 'Ⅰ' in q['question'] or 'i.' in q['question']
        if is_roman:
            opts = q['options']
            # Find which content is the correct answer
            orig_ans_letter = q['answer']
            correct_content = opts.get(orig_ans_letter, '')
            
            # Sort the 4 option texts
            all_texts = [opts['A'], opts['B'], opts['C'], opts['D']]
            sorted_texts = sorted(all_texts, key=roman_sort_key)
            
            # Reassign to A, B, C, D
            new_opts = {}
            new_ans_letter = 'A'
            for idx, text in enumerate(sorted_texts):
                letter = chr(65 + idx)
                new_opts[letter] = text
                if text == correct_content:
                    new_ans_letter = letter
            
            q['options'] = new_opts
            q['answer'] = new_ans_letter
            updated_roman_count += 1

    # Save chapter back
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully sorted options for all {updated_roman_count} Roman questions across 20 chapters!")
