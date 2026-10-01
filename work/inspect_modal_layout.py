import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('portal-modal')
print("Portal modal structure:")
print(text[pos:pos+500])

pos2 = text.find('portal-mini-footer')
print("\nPortal mini footer structure:")
print(text[pos2-100:pos2+400])
