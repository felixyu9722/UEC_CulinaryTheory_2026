import json
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_root = r'c:\Users\GOH\Desktop\2026年统考厨艺理论'
s1_dir = os.path.join(workspace_root, 'work', 'data')
s2_dir = os.path.join(workspace_root, 'work', 'data', 'senior2')
s3_dir = os.path.join(workspace_root, 'work', 'data', 'senior3')
template_path = os.path.join(workspace_root, 'work', 'template.html')

print("=== 1. Loading Question Banks ===")
print("Loading Senior 1 data (20 chapters)...")
s1_chapters = []
for ch in range(1, 21):
    fpath = os.path.join(s1_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        s1_chapters.append(json.load(f))
s1_q_count = sum(len(c['questions']) for c in s1_chapters)
print(f"-> Senior 1 loaded: {len(s1_chapters)} chapters, {s1_q_count} questions.")

print("Loading Senior 2 data (15 chapters)...")
s2_chapters = []
for ch in range(1, 16):
    fpath = os.path.join(s2_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        s2_chapters.append(json.load(f))
s2_q_count = sum(len(c['questions']) for c in s2_chapters)
print(f"-> Senior 2 loaded: {len(s2_chapters)} chapters, {s2_q_count} questions.")

print("Loading Senior 3 data (8 chapters)...")
s3_chapters = []
for ch in range(1, 9):
    fpath = os.path.join(s3_dir, f'chapter{ch:02d}.json')
    with open(fpath, 'r', encoding='utf-8') as f:
        s3_chapters.append(json.load(f))
s3_q_count = sum(len(c['questions']) for c in s3_chapters)
print(f"-> Senior 3 loaded: {len(s3_chapters)} chapters, {s3_q_count} questions.")

total_system_questions = s1_q_count + s2_q_count + s3_q_count
print(f"\n[SUMMARY] Total System Questions: {total_system_questions} (S1: {s1_q_count} + S2: {s2_q_count} + S3: {s3_q_count})")
assert total_system_questions == 1720, f"Expected 1,720 questions, got {total_system_questions}"

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

s1_json_str = json.dumps(s1_chapters, ensure_ascii=False)
s2_json_str = json.dumps(s2_chapters, ensure_ascii=False)
s3_json_str = json.dumps(s3_chapters, ensure_ascii=False)

print("\n=== 2. Compiling Master Triple-Grade index.html ===")
master_html = template.replace('__QUESTIONS_DATA_PLACEHOLDER__', s1_json_str)
master_html = master_html.replace('__SENIOR2_QUESTIONS_DATA_PLACEHOLDER__', s2_json_str)
master_html = master_html.replace('__SENIOR3_QUESTIONS_DATA_PLACEHOLDER__', s3_json_str)

index_path = os.path.join(workspace_root, 'index.html')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(master_html)
print(f"[OK] Master Index HTML compiled: {index_path} ({len(master_html):,} bytes)")

print("\n=== 3. Compiling Standalone Senior 3 Master System (320 Questions) ===")
# Build standalone where default grade is senior3 and portal is hidden initially
s3_master_html = master_html.replace("selectGrade('senior1');", "selectGrade('senior3');")
s3_master_html = s3_master_html.replace(
    "document.getElementById('gradePortal').classList.remove('hidden');",
    "document.getElementById('gradePortal').classList.add('hidden');"
)
s3_master_html = s3_master_html.replace(
    "<title>2026年统考厨艺理论 全套1,720题互动答题总系统（高一+高二+高三完整统考版）</title>",
    "<title>2026年统考厨艺（西式点心·母酱·亚洲烹调）高三全套8单元·320题互动答题总系统</title>"
)

s3_root_file = os.path.join(workspace_root, '高三厨艺理论_全套8单元_320题互动答题总系统.html')
with open(s3_root_file, 'w', encoding='utf-8') as f:
    f.write(s3_master_html)
print(f"[OK] Senior 3 Standalone HTML compiled: {s3_root_file}")

s3_folder = os.path.join(workspace_root, '14_高三_第01至08单元_全套320题精选题库与互动答题总系统')
os.makedirs(s3_folder, exist_ok=True)
s3_in_folder = os.path.join(s3_folder, '高三厨艺理论_第01至08单元_全套320题_互动答题总系统.html')
with open(s3_in_folder, 'w', encoding='utf-8') as f:
    f.write(s3_master_html)
print(f"[OK] Senior 3 Folder Deliverable compiled: {s3_in_folder}")

print("\n=== 4. Compiling Standalone Senior 3 Easy Pass System (160 Questions) ===")
s3_easy_chapters = []
for ch in s3_chapters:
    easy_qs = [q for q in ch['questions'] if q['difficulty'] == 'easy']
    ch_copy = dict(ch)
    ch_copy['questions'] = easy_qs
    s3_easy_chapters.append(ch_copy)

s3_easy_count = sum(len(c['questions']) for c in s3_easy_chapters)
print(f"Senior 3 Easy questions count: {s3_easy_count}")
assert s3_easy_count == 160, f"Expected 160 easy questions, got {s3_easy_count}"

s3_easy_json_str = json.dumps(s3_easy_chapters, ensure_ascii=False)

s3_easy_html = template.replace('__QUESTIONS_DATA_PLACEHOLDER__', '[]')
s3_easy_html = s3_easy_html.replace('__SENIOR2_QUESTIONS_DATA_PLACEHOLDER__', '[]')
s3_easy_html = s3_easy_html.replace('__SENIOR3_QUESTIONS_DATA_PLACEHOLDER__', s3_easy_json_str)
s3_easy_html = s3_easy_html.replace("selectGrade('senior1');", "selectGrade('senior3');")
s3_easy_html = s3_easy_html.replace(
    "document.getElementById('gradePortal').classList.remove('hidden');",
    "document.getElementById('gradePortal').classList.add('hidden');"
)
s3_easy_html = s3_easy_html.replace(
    "<title>2026年统考厨艺理论 全套1,720题互动答题总系统（高一+高二+高三完整统考版）</title>",
    "<title>2026年统考厨艺（西式点心·母酱·亚洲烹调）高三全套8单元·160题纯容易选择题精选通关系统</title>"
)
s3_easy_html = s3_easy_html.replace('全套320题·统考全覆盖', '全套8单元160题·纯容易基础通关版')

s3_easy_root_file = os.path.join(workspace_root, '高三厨艺理论_全套8单元_160题纯容易选择题精选通关系统.html')
with open(s3_easy_root_file, 'w', encoding='utf-8') as f:
    f.write(s3_easy_html)
print(f"[OK] Senior 3 Easy 160 Questions HTML compiled: {s3_easy_root_file}")

easy_s3_in_folder = os.path.join(s3_folder, '高三厨艺理论_全套8单元_160题纯容易选择题精选通关系统.html')
with open(easy_s3_in_folder, 'w', encoding='utf-8') as f:
    f.write(s3_easy_html)
print(f"[OK] Senior 3 Easy Folder Deliverable compiled: {easy_s3_in_folder}")

print("\n=== Triple-Grade & Senior 3 Compilation Complete Successfully! ===")
