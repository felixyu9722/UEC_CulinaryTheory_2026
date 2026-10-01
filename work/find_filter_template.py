import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('mistakes')
if idx != -1:
    print(text[max(0, idx-300):min(len(text), idx+500)])
