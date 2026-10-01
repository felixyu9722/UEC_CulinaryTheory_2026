import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find all occurrences of "通用单页数据架构"
matches = [m.start() for m in re.finditer(r'通用单页数据架构', text)]
print(f"Found {len(matches)} occurrences at indices: {matches}")

# Let's inspect each occurrence
for idx in matches:
    start_pos = max(0, idx - 100)
    end_pos = min(len(text), idx + 200)
    print("--- Occur ---")
    print(text[start_pos:end_pos])
