import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('portal-mini-footer')
print("Snippet in index.html:")
print(text[pos:pos+550])

print("\nHas 2026年10月统考真题对齐版 in mini-footer:", '2026年10月统考真题对齐版' in text[pos:pos+550])
print("Has 手机离线进度自动保存 in mini-footer:", '手机离线进度自动保存' in text[pos:pos+550])
