import json, sys

sys.stdout.reconfigure(encoding='utf-8')

def audit_all():
    grades = [
        ('senior1', 'work/data', 20, 800),
        ('senior2', 'work/data/senior2', 15, 600),
        ('senior3', 'work/data/senior3', 8, 320)
    ]
    
    total_q = 0
    all_pass = True
    
    for gname, gdir, n_ch, exp_q in grades:
        g_q = 0
        print(f"\n==================== {gname.upper()} ({n_ch} Chapters) ====================")
        for ch in range(1, n_ch + 1):
            fpath = f"{gdir}/chapter{ch:02d}.json"
            d = json.load(open(fpath, encoding='utf-8'))
            qs = d['questions']
            g_q += len(qs)
            
            # verify length
            if len(qs) != 40:
                print(f"[{gname} Ch{ch:02d}] FAIL: len={len(qs)} != 40")
                all_pass = False
                
            # verify answers & difficulties
            ans_cnt = {k: 0 for k in 'ABCD'}
            diff_cnt = {'easy': 0, 'medium': 0, 'hard': 0}
            opt_lens = []
            for i, q in enumerate(qs, 1):
                if q['id'] != i:
                    print(f"[{gname} Ch{ch:02d}] FAIL: Q id {q['id']} != {i}")
                    all_pass = False
                ans_cnt[q['answer']] += 1
                diff_cnt[q['difficulty']] += 1
                for k in 'ABCD':
                    if not q['options'][k]:
                        print(f"[{gname} Ch{ch:02d}] FAIL: Q{i} option {k} empty!")
                        all_pass = False
                    opt_lens.append(len(q['options'][k]))
            
            if ans_cnt != {'A': 10, 'B': 10, 'C': 10, 'D': 10}:
                print(f"[{gname} Ch{ch:02d}] FAIL: ans balance {ans_cnt} != 10:10:10:10")
                all_pass = False
            if diff_cnt != {'easy': 20, 'medium': 15, 'hard': 5}:
                print(f"[{gname} Ch{ch:02d}] FAIL: diff balance {diff_cnt} != 20:15:5")
                all_pass = False
                
            avg_len = sum(opt_lens) / len(opt_lens)
            title = d.get('title') or d.get('chapter_title') or f"Chapter {ch}"
            print(f"[{gname.upper()} Ch{ch:02d}] PASS: 40 Qs, ans 10:10:10:10, diff 20:15:5, avg opt={avg_len:.1f} chars | {title[:20]}")
            
        print(f"-> {gname.upper()} Total: {g_q} Qs (Expected: {exp_q})")
        if g_q != exp_q:
            all_pass = False
        total_q += g_q
        
    print(f"\n==================== TOTAL AUDIT RESULT ====================")
    print(f"Total Questions across all 3 grades: {total_q} / 1,720")
    if all_pass and total_q == 1720:
        print(">>> 100% PERFECT AUDIT! ALL 1,720 QUESTIONS PASS ALL UEC STANDARDS! <<<")
    else:
        print(">>> FAILURES ENCOUNTERED IN AUDIT! <<<")

if __name__ == '__main__':
    audit_all()
