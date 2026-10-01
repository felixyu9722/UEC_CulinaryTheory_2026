import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\07_统考标准复习题库与命题提示词\高三\第01单元_饼干\高三_第01单元_饼干_统考标准复习题（完整样卷含深度解析）.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['【答案与解析】', '参考答案', '答案及解析', '【答案】', '答案：', '1-5', '1.【答案】', '解析', '【参考答案']):
        print(f"Line {i+1}: {line.strip()}")
