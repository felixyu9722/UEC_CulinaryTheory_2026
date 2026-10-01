import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\exam_2020_2025_extracted.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages_raw = text.split('=== PAGE ')

# Extract Paper 2 (written questions) for all years
print("=================== 历届作答题汇总（2020-2025） ===================")
# 2025 Paper 2: P.09 - P.11
# 2020 Paper 2: P.20 - P.23
# 2021 Paper 2: P.32 - P.33
# 2022 Paper 2: P.42 - P.44
# 2023 Paper 2: P.53 - P.55
# 2024 Paper 2: P.64 - P.66

paper2_ranges = [
    ("2025", 9, 11),
    ("2020", 21, 23),
    ("2021", 32, 33),
    ("2022", 42, 44),
    ("2023", 53, 55),
    ("2024", 64, 66)
]

for year, start_p, end_p in paper2_ranges:
    print(f"\n******************** 【{year} 年 统考试卷二 作答题】 ********************")
    for p in range(start_p, end_p + 1):
        if p < len(pages_raw):
            print(f"--- P.{p} ---")
            print(pages_raw[p].strip())
