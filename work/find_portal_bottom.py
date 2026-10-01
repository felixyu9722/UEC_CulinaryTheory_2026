import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('进入高一练习')
print("Snippet around 进入高一练习:")
print(text[pos-100:pos+1200])
