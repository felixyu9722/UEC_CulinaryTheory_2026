import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')

for grade in ['senior2', 'senior3']:
    print(f"\n==================== {grade.upper()} AUDIT ====================")
    for f in sorted(glob.glob(f'work/data/{grade}/*.json')):
        d = json.load(open(f, encoding='utf-8'))
        ch_title = d.get('chapter_title', f)
        mismatches = []
        for q in d['questions'][:35]:
            q_text = q['question']
            opts = q['options']
            # Check obvious mismatches
            # 1. stem asks "被称为：" or "称为：" but opts don't have terms or definitions
            if ("被称为：" in q_text or "称为：" in q_text) and not any(len(v) < 15 or "（" in v for v in opts.values()):
                mismatches.append((q['id'], q_text[:20], "looks like term Q but opts are long sentences"))
            # 2. stem asks "温度" or "比例" but opts have no numbers or % or ℃
            if ("温度" in q_text or "比例" in q_text or "比重" in q_text) and not any(any(c in v for c in '0123456789%℃') for v in opts.values()):
                mismatches.append((q['id'], q_text[:20], "asks temp/ratio/sg but no numbers in opts"))
        if mismatches:
            print(f"\n[{ch_title}] has {len(mismatches)} suspicious questions:")
            for m in mismatches:
                print(f"  Q{m[0]}: {m[1]}... -> {m[2]}")
