import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\exam_2020_2025_extracted.txt', 'r', encoding='utf-8') as f:
    pages_raw = f.read().split('=== PAGE ')

print(f"Total page sections: {len(pages_raw) - 1}")

pages = []
for p in pages_raw[1:]:
    lines = p.split('\n', 1)
    page_num = lines[0].split()[0]
    content = lines[1] if len(lines) > 1 else ''
    pages.append((int(page_num), content))

# Print head of each page (first 3 lines) to map the table of contents / year boundaries
print("\n--- Page Structure Overview ---")
for num, content in pages:
    first_lines = [line.strip() for line in content.split('\n') if line.strip()][:3]
    summary = " | ".join(first_lines)
    if any(k in summary for k in ['2020', '2021', '2022', '2023', '2024', '2025', '试卷', '统考', '选择题', '作答题', '甲组', '乙组']):
        print(f"P.{num:02d}: {summary[:120]}")
