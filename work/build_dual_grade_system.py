import json
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_root = r'c:\Users\GOH\Desktop\2026年统考厨艺理论'
s1_dir = os.path.join(workspace_root, 'work', 'data')
s2_dir = os.path.join(workspace_root, 'work', 'data', 'senior2')
template_path = os.path.join(workspace_root, 'work', 'template.html')

print("Loading Senior 1 data (20 chapters)...")
s1_chapters = []
for ch in range(1, 21):
    fpath = os.path.join(s1_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        s1_chapters.append(json.load(f))
print(f"Senior 1 loaded: {len(s1_chapters)} chapters, {sum(len(c['questions']) for c in s1_chapters)} questions.")

print("Loading Senior 2 data (15 chapters)...")
s2_chapters = []
for ch in range(1, 16):
    fpath = os.path.join(s2_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        s2_chapters.append(json.load(f))
print(f"Senior 2 loaded: {len(s2_chapters)} chapters, {sum(len(c['questions']) for c in s2_chapters)} questions.")

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

s1_json_str = json.dumps(s1_chapters, ensure_ascii=False)
s2_json_str = json.dumps(s2_chapters, ensure_ascii=False)

# 1. Master index.html (Holds both Senior 1 & Senior 2, total 1,400 questions)
master_html = template.replace('__QUESTIONS_DATA_PLACEHOLDER__', s1_json_str)
master_html = master_html.replace('__SENIOR2_QUESTIONS_DATA_PLACEHOLDER__', s2_json_str)

index_path = os.path.join(workspace_root, 'index.html')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(master_html)
print(f"\n[OK] Master Index HTML compiled: {index_path} ({len(master_html):,} bytes)")

# 2. Standalone Senior 2 Master (600 Questions)
# In this standalone, default grade is senior2 and portal is hidden by default
s2_master_html = master_html.replace("selectGrade('senior1');", "selectGrade('senior2');")
s2_master_html = s2_master_html.replace(
    "document.getElementById('gradePortal').classList.remove('hidden');",
    "document.getElementById('gradePortal').classList.add('hidden');"
)
s2_master_html = s2_master_html.replace(
    "<title>2026年统考厨艺（烘焙理论与西餐）全套1,400题互动答题总系统（高一+高二完整版）</title>",
    "<title>2026年统考厨艺（蛋糕·面包·西餐）高二全套15单元·600题互动答题总系统</title>"
)

s2_root_file = os.path.join(workspace_root, '高二厨艺理论_全套15单元_600题互动答题总系统.html')
with open(s2_root_file, 'w', encoding='utf-8') as f:
    f.write(s2_master_html)
print(f"[OK] Senior 2 Standalone HTML compiled: {s2_root_file}")

s2_folder = os.path.join(workspace_root, '13_高二_第01至15单元_全套600题精选题库与互动答题总系统')
os.makedirs(s2_folder, exist_ok=True)
s2_in_folder = os.path.join(s2_folder, '高二厨艺理论_第01至15单元_全套600题_互动答题总系统.html')
with open(s2_in_folder, 'w', encoding='utf-8') as f:
    f.write(s2_master_html)
print(f"[OK] Senior 2 Folder Deliverable compiled: {s2_in_folder}")

# 3. Standalone Senior 2 Easy (300 Questions)
s2_easy_chapters = []
for ch in s2_chapters:
    easy_qs = [q for q in ch['questions'] if q['difficulty'] == 'easy']
    ch_copy = dict(ch)
    ch_copy['questions'] = easy_qs
    s2_easy_chapters.append(ch_copy)

s2_easy_json_str = json.dumps(s2_easy_chapters, ensure_ascii=False)

s2_easy_html = template.replace('__QUESTIONS_DATA_PLACEHOLDER__', '[]')
s2_easy_html = s2_easy_html.replace('__SENIOR2_QUESTIONS_DATA_PLACEHOLDER__', s2_easy_json_str)
s2_easy_html = s2_easy_html.replace("selectGrade('senior1');", "selectGrade('senior2');")
s2_easy_html = s2_easy_html.replace(
    "document.getElementById('gradePortal').classList.remove('hidden');",
    "document.getElementById('gradePortal').classList.add('hidden');"
)
s2_easy_html = s2_easy_html.replace(
    "<title>2026年统考厨艺（烘焙理论与西餐）全套1,400题互动答题总系统（高一+高二完整版）</title>",
    "<title>2026年统考厨艺（蛋糕·面包·西餐）高二全套15单元·300题纯容易选择题精选通关系统</title>"
)
s2_easy_html = s2_easy_html.replace('全套600题·统考全覆盖', '全套15单元300题·纯容易基础通关版')
s2_easy_html = s2_easy_html.replace('0 / 800', '0 / 300')

s2_easy_root_file = os.path.join(workspace_root, '高二厨艺理论_全套15单元_300题纯容易选择题精选通关系统.html')
with open(s2_easy_root_file, 'w', encoding='utf-8') as f:
    f.write(s2_easy_html)
print(f"[OK] Senior 2 Easy 300 Questions HTML compiled: {s2_easy_root_file}")

easy_s2_in_folder = os.path.join(s2_folder, '高二厨艺理论_全套15单元_300题纯容易选择题精选通关系统.html')
with open(easy_s2_in_folder, 'w', encoding='utf-8') as f:
    f.write(s2_easy_html)
print(f"[OK] Senior 2 Easy Folder Deliverable compiled: {easy_s2_in_folder}")

print("\nAll deliverables compiled successfully!")
