import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_snippet = """            <p style="color:#64748B; font-size:1.02rem; max-width:620px; margin:0 auto 24px; line-height:1.7;">
              本系统已采用通用单页数据架构，为 <strong>${gradeData.grade_name}</strong> 预留了完全独立的题库数据接口。<br>
              后续制作高二/高三题目时，直接录入数据即可无缝在此页面刷题与互动。
            </p>"""

new_snippet = """            <p style="color:#64748B; font-size:1.02rem; max-width:620px; margin:0 auto 24px; line-height:1.7;">
              <strong>${gradeData.grade_name}</strong> 专属题库正在系统编排整理中，敬请期待！
            </p>"""

if old_snippet in text:
    text = text.replace(old_snippet, new_snippet)
    print("Replaced successfully!")
else:
    print("Exact snippet not matched, replacing by regex...")
    import re
    text = re.sub(r'本系统已采用通用单页数据架构.*?无缝在此页面刷题与互动。', '<strong>${gradeData.grade_name}</strong> 专属题库正在系统编排整理中，敬请期待！', text, flags=re.DOTALL)
    print("Regex replaced!")

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Template updated clean!")
