import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'
out_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\09_高一_第10至15课_生活常识版选择题库'
out_html = os.path.join(out_dir, '高一厨艺理论_第10至15课_互动答题练习系统.html')

chapters = []
for ch in range(10, 16):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    chapters.append(json.load(open(fpath, encoding='utf-8-sig')))

# Read existing html to extract template
if os.path.exists(out_html):
    with open(out_html, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace rawData
    import re
    # Look for const rawData = [...];
    new_json = json.dumps(chapters, ensure_ascii=False)
    updated = re.sub(r'const rawData = \[[\s\S]*?\];\s*// State', f'const rawData = {new_json};\n\n    // State', content)
    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(updated)
    print("Successfully updated 10-15 interactive HTML!")
else:
    print("Target HTML not found.")
