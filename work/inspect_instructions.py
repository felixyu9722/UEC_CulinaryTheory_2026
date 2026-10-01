import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\exam_2020_2025_extracted.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect instructions on P.01, P.09, P.12, P.24, P.34, P.45, P.56
pages_raw = text.split('=== PAGE ')

def show_page_summary(page_indices):
    for idx in page_indices:
        p_text = pages_raw[idx]
        lines = [l.strip() for l in p_text.split('\n') if l.strip()]
        print(f"==================== PAGE {idx} ====================")
        for line in lines[:25]:
            print(line)

# Let's look at instructions for 2025 Paper 1 & 2
show_page_summary([1, 2, 8, 9, 10, 11, 12, 13, 23, 24, 25])
