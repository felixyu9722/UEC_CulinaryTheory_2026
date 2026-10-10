import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

for grade in ['senior2', 'senior3']:
    print(f"\n==================== {grade.upper()} AUDIT ====================")
    for f in sorted(glob.glob(f'work/data/{grade}/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        ch_id = d.get('chapter_id', f)
        for q in d['questions'][:35]:
            # check if option mentions something completely unrelated to question stem
            q_text = q['question']
            opts = q['options']
            # e.g. stem asks about temperature, but opts are actions
            # stem asks about Pâte à Bombe, opts talk about whipping machine
            # let's flag suspicious stems
            if "Pâte à Bombe" in q_text and not any("蛋黄" in v or "全蛋" in v for v in opts.values()):
                print(f"[{ch_id}] Q{q['id']} SUSPICIOUS: Stem mentions Pâte à Bombe but opts do not mention egg yolk!")
            if "植物性鲜奶油" in q_text and not any("植" in v or "人造" in v or "耐热" in v or "成本" in v or "稳定" in v for v in opts.values()):
                print(f"[{ch_id}] Q{q['id']} SUSPICIOUS: Stem mentions 植物性鲜奶油 but opts do not match!")
            if "瑞式蛋白霜" in q_text and not any("温" in v or "热" in v or "隔水" in v or "Swiss" in v for v in opts.values()):
                print(f"[{ch_id}] Q{q['id']} SUSPICIOUS: Stem mentions 瑞式蛋白霜 but opts do not match!")
            if "豆腐渣" in q_text and not any("过度" in v or "破乳" in v or "分离" in v or "黄油" in v for v in opts.values()):
                print(f"[{ch_id}] Q{q['id']} SUSPICIOUS: Stem mentions 豆腐渣 but opts do not match!")
