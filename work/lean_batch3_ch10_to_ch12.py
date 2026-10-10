import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

# Load original files
def load_ch(ch):
    return json.load(open(os.path.join(data_dir, f'chapter{ch:02d}.json'), encoding='utf-8-sig'))

def save_ch(ch, data):
    with open(os.path.join(data_dir, f'chapter{ch:02d}.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Batch 3 processor ready.")
