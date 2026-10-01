import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['index.html', '高一厨艺理论_全套第01至20课_800题互动答题总系统.html', '高一厨艺理论_全套20课_400题纯容易选择题精选通关系统.html']:
    with open(rf'c:\Users\GOH\Desktop\2026年统考厨艺理论\{fname}', 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"{fname}: has prompt = {'通用单页数据架构' in text}")
