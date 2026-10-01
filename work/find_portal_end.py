import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('进入高三专属题库')
print("After 进入高三专属题库:")
print(text[pos:pos+500])
