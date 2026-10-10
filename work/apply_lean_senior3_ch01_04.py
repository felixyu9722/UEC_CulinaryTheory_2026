# -*- coding: utf-8 -*-
"""
apply_lean_senior3_ch01_04.py
Applies lean de-padding to Senior 3 Chapters 01 to 04 (160 questions).
"""
import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

from test_advanced_s3_cleaner import clean_s3_option_advanced

def process_batch4():
    for ch in range(1, 5):
        fpath = f'work/data/senior3/chapter{ch:02d}.json'
        bpath = f'work/backup_before_lean_senior2_3/senior3/chapter{ch:02d}.json'
        d = json.load(open(fpath, encoding='utf-8'))
        b = json.load(open(bpath, encoding='utf-8'))
        
        for q_b, q_curr in zip(b['questions'], d['questions']):
            q_curr['answer'] = q_b['answer']
            q_curr['difficulty'] = q_b['difficulty']
            for k in 'ABCD':
                q_curr['options'][k] = clean_s3_option_advanced(q_curr['options'][k])
                
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"Senior 3 Chapter {ch:02d} updated successfully!")

if __name__ == '__main__':
    process_batch4()
