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
            for opt_k, opt_v in opts.items():
                if '项叙述正确' in opt_v:
                    print(f"{f} Q{q['id']}: opt={opt_k} -> {opt_v}")
                    print(f"   question: {q['question'][:60]}")
                    break
