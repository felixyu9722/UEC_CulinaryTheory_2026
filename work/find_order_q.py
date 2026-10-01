import os, json, sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'
for f in os.listdir(data_dir):
    if f.startswith('chapter') and f.endswith('.json'):
        fpath = os.path.join(data_dir, f)
        with open(fpath, 'r', encoding='utf-8-sig') as jf:
            data = json.load(jf)
        for q in data.get('questions', []):
            opts = q.get('options', {})
            vals = list(opts.values())
            if any('Ⅰ、Ⅱ、Ⅲ、Ⅳ 皆正确' in v for v in vals) and any('Ⅲ、Ⅳ 正确' in v for v in vals):
                print(f"{f} Q{q['id']}: answer={q['answer']}")
                for k, v in opts.items():
                    print(f"   {k}: {v}")
