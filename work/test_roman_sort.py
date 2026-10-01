import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

roman_map = {'Ⅰ': 1, 'Ⅱ': 2, 'Ⅲ': 3, 'Ⅳ': 4, 'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'I': 1, 'II': 2, 'III': 3, 'IV': 4}

def parse_roman_items(text):
    # Find all roman numerals in text
    # Match standard uppercase or lowercase
    found = []
    # Standardize text
    t = text.replace('皆正确', '').replace('全部正确', '').replace('正确', '').replace('仅', '')
    for m in re.finditer(r'(?:[ⅠⅡⅢⅣ]|[ivxIVX]+)', text):
        val = m.group(0)
        if val in roman_map:
            found.append(roman_map[val])
        elif val.upper() in roman_map:
            found.append(roman_map[val.upper()])
    # Remove duplicates preserving order
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
        return (99, 99, opt_text)
    first_item = items[0]
    length = len(items)
    # Special: full [1, 2, 3, 4] often goes to the very end (D)
    if length == 4:
        return (10, 4, items)
    return (first_item, length, items)

# Test sample from user screenshot
sample = [
    "Ⅰ、Ⅱ、Ⅲ、Ⅳ 皆正确",
    "仅 Ⅲ、Ⅳ 正确",
    "仅 Ⅰ、Ⅱ、Ⅲ 正确",
    "仅 Ⅰ、Ⅱ 正确"
]

sorted_sample = sorted(sample, key=roman_sort_key)
print("Before:")
for s in sample: print("  ", s)
print("\nAfter sorting by pedagogical Roman order:")
for idx, s in enumerate(sorted_sample):
    print(f"   {chr(65+idx)}. {s}")
