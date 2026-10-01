import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

def clean_roman_opt(text):
    # If the option is already a pure roman combination like 'Ⅰ、Ⅱ'
    # Remove words: '仅', '皆正确', '全部正确', '全对', '正确', '项叙述', '项'
    t = text
    for word in ['皆正确', '全部正确', '全对', '项叙述正确', '项正确', '叙述正确', '正确', '仅', '项']:
        t = t.replace(word, '')
    t = t.strip()
    # Normalize spaces around commas
    t = re.sub(r'\s*([、,，])\s*', '、', t)
    # Ensure roman numerals are uppercase standard
    # e.g. i -> Ⅰ, ii -> Ⅱ, etc.
    roman_sub = {'i': 'Ⅰ', 'ii': 'Ⅱ', 'iii': 'Ⅲ', 'iv': 'Ⅳ', 'I': 'Ⅰ', 'II': 'Ⅱ', 'III': 'Ⅲ', 'IV': 'Ⅳ'}
    # Replace letters if needed
    parts = t.split('、')
    clean_parts = []
    for p in parts:
        p = p.strip()
        if p in roman_sub:
            clean_parts.append(roman_sub[p])
        else:
            clean_parts.append(p)
    return '、'.join(clean_parts)

cleaned_count = 0

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    questions = data['questions']
    for q in questions:
        is_roman = q.get('type') in ['roman', 'combination'] or 'Ⅰ' in q['question'] or 'i.' in q['question']
        if is_roman:
            opts = q['options']
            for k in ['A', 'B', 'C', 'D']:
                old_val = opts[k]
                new_val = clean_roman_opt(old_val)
                if old_val != new_val:
                    opts[k] = new_val
                    cleaned_count += 1
                    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully cleaned {cleaned_count} options across all Roman questions in 20 chapters!")
