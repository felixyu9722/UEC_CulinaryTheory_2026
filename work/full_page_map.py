import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\exam_2020_2025_extracted.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages_raw = text.split('=== PAGE ')

# Let's inspect the headers and questions across all 66 pages
exam_map = []
for idx in range(1, len(pages_raw)):
    p_text = pages_raw[idx]
    lines = [l.strip() for l in p_text.split('\n') if l.strip()]
    first_few = " | ".join(lines[:3])
    exam_map.append((idx, first_few))

for item in exam_map:
    print(f"P.{item[0]:02d}: {item[1][:100]}")
