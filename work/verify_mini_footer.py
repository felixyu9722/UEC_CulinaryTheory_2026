import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('portal-mini-footer')
print("Found portal-mini-footer pos:", pos)
if pos != -1:
    print(text[pos:pos+600])
