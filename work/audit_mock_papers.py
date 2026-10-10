import re, json, sys

sys.stdout.reconfigure(encoding='utf-8')

for path in ['模拟卷A_历届高频真题精选卷.html', '模拟卷B_2026前瞻预测试题卷.html', '模拟卷C_2026统考短选项实战冲刺卷.html']:
    txt = open(path, encoding='utf-8').read()
    # find array of questions
    m = re.search(r'const\s+([A-Za-z0-9_]+)\s*=\s*(\[\s*\{\s*"id":[\s\S]*?\}\s*\]);', txt)
    if m:
        var_name = m.group(1)
        qs = json.loads(m.group(2))
        opt_lens = [len(v) for q in qs for v in q['options'].values()]
        avg_len = sum(opt_lens) / len(opt_lens)
        max_opt = max(opt_lens)
        min_opt = min(opt_lens)
        print(f"=== {path} ({var_name}) ===")
        print(f"  Count: {len(qs)} Qs")
        print(f"  Avg Option Length: {avg_len:.1f} chars (min={min_opt}, max={max_opt})")
        # count questions where options are long
        long_qs = [q for q in qs if any(len(v) >= 25 for v in q['options'].values())]
        print(f"  Qs with any option >= 25 chars: {len(long_qs)}")
        if long_qs:
            print("  Sample long Q:", long_qs[0]['id'], long_qs[0]['question'][:30], "...")
            print("  Options:", long_qs[0]['options'])
    else:
        print(f"Not matched in {path}")
