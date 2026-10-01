import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('.portal-modal {')
if pos != -1:
    print(text[pos:pos+800])
else:
    print("Not found .portal-modal {")
    for l in text.split('\n'):
        if 'portal' in l and '{' in l:
            print(l)
