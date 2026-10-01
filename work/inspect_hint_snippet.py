import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('通用单页数据架构')
print("Found snippet:")
print(text[max(0, pos-150):min(len(text), pos+300)])
