import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\GOH\Desktop\2026年统考厨艺理论\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Has system-footer:', 'system-footer' in html)
print('Has localStorage:', 'localStorage' in html)
print('Has 尤老师:', '尤老师' in html)
print('Has 新民独中:', '新民独中' in html)
print('Has v2026.10-Build.01:', 'v2026.10-Build.01' in html)
