import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to remove portal-footer div completely
pattern = r'<div class="portal-footer">\s*💡 提示：本系统已采用通用单页数据架构.*?</div>'
match = re.search(pattern, text, re.DOTALL)
if match:
    text = re.sub(pattern, '', text, flags=re.DOTALL)
    print("Matched and removed portal-footer successfully!")
else:
    print("Regex match failed, trying direct string replacement...")
    target = """      <div class="portal-footer">
        💡 提示：本系统已采用通用单页数据架构（Single HTML）。后续制作高二与高三题目时将直接加载于此，随时点击上方「切换年段」自由切换。
      </div>"""
    if target in text:
        text = text.replace(target, '')
        print("Direct string replaced successfully!")
    else:
        print("Target string not found!")

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Template updated!")
