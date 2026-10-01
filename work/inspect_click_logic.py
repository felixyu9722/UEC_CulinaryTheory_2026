import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function handleOptionClick')
print(text[pos:pos+600])

pos2 = text.find('function reset')
if pos2 != -1:
    print(text[pos2:pos2+300])
