import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find questionsContainer
pos = text.find('questionsContainer')
if pos != -1:
    print("Around questionsContainer:")
    print(text[max(0, pos-800):pos+100])
