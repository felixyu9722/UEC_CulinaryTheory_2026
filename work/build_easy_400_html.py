import json
import os
import shutil
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'
workspace_root = r'c:\Users\GOH\Desktop\2026年统考厨艺理论'

# 1. Collect only easy questions from all 20 chapters
easy_chapters = []
total_easy_count = 0

for ch in range(1, 21):
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    easy_qs = [q for q in data.get('questions', []) if q.get('difficulty') == 'easy']
    total_easy_count += len(easy_qs)
    
    ch_copy = {
        'chapter_id': data.get('chapter_id', ch),
        'chapter_title': data.get('chapter_title', f'第{ch:02d}课'),
        'intro': data.get('intro', ''),
        'questions': easy_qs
    }
    easy_chapters.append(ch_copy)

print(f"Collected {total_easy_count} easy questions across {len(easy_chapters)} chapters.")

# 2. Read template.html and inject easy questions
template_path = os.path.join(workspace_root, 'work', 'template.html')
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

json_str = json.dumps(easy_chapters, ensure_ascii=False)
html = template.replace('__QUESTIONS_DATA_PLACEHOLDER__', json_str)

# Customize title and badges for the 400 Easy Questions Edition
html = html.replace('高一厨艺理论 · 统考全真800题精选通关总系统', '高一厨艺理论 · 全套20课400题纯容易选择题精选通关系统')
html = html.replace('董总统考教研标准 · 高一全套20课800题全量交互大满贯', '高一零基础打底通关 · 全套20课400题纯容易基础选择题特训系统')
html = html.replace('高一《烘焙理论》第01至20课全量精选分类题库', '覆盖高一烘焙原料、设备器具、操作安全与度量衡等20课最基础、最通俗核心常识')
html = html.replace('0 / 800', f'0 / {total_easy_count}')
html = html.replace('(800)', f'({total_easy_count})')
html = html.replace('(400)', f'({total_easy_count})')

# In the difficulty bar for this specific easy edition:
html = html.replace('800</span>', f'{total_easy_count}</span>')

# 3. Output files
out_root = os.path.join(workspace_root, '高一厨艺理论_全套20课_400题纯容易选择题精选通关系统.html')
with open(out_root, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Generated root HTML: {out_root}")

out_08 = os.path.join(workspace_root, '08_高一新测验题库_简易版', '高一厨艺理论_全套20课_400题纯容易选择题精选通关系统.html')
shutil.copyfile(out_root, out_08)
print(f"Copied to 08 folder: {out_08}")
