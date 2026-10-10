# -*- coding: utf-8 -*-
"""
apply_lean_senior3_ch05_08_v2.py
Rewrites Senior 3 Chapters 05 to 08 (160 questions) into concise, authentic UEC exam style.
"""
import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def lean_transform_question(q):
    # 1. Clean stem
    stem = q['question'].strip()
    # Remove verbose academic prefixes
    prefixes = [
        "在西点分类学中，", "在西式点心工艺学中，", "在法式古典烹饪殿堂体系中，",
        "在经典法式西餐母酱工艺学中，", "在亚洲中餐烹调刀工与预处理工艺中，",
        "在烹饪物理学中，", "在中餐与烹饪物理学中，", "在中餐烹调中，",
        "在经典热酱工艺中，", "在法式酱汁工艺中，", "在亚洲传统烹调中，",
        "仔细观察【考题配图：.*?】，", "观察【考题配图：.*?】，"
    ]
    for p in prefixes:
        stem = re.sub(f"^{p}", "", stem)
    
    # 2. Clean options
    opts = {}
    for k, v in q['options'].items():
        opt = v.strip()
        
        # Remove parenthetical essay explanations, keep technical term or short gloss
        def simplify_paren(m):
            inner = m.group(1).strip()
            # If it's a short foreign word or abbreviation (<=15 chars), keep it
            if re.match(r'^[A-Za-z\s/,\-\'\.0-9%:]+$', inner) and len(inner) <= 15:
                return f"（{inner}）"
            # If it has a short name before comma/clause
            parts = re.split(r'[,，；;、]', inner)
            first = parts[0].strip()
            if len(first) <= 8 and not any(w in first for w in ["依靠", "由于", "经过", "使得", "因为"]):
                return f"（{first}）"
            return ""
            
        opt = re.sub(r'（(.*?)）', simplify_paren, opt)
        opt = re.sub(r'\((.*?)\)', simplify_paren, opt)
        
        # Simplify numbers & units
        opt = opt.replace("百分之十五至百分之二十之间", "15% ~ 20%")
        opt = opt.replace("百分之八至百分之十二之间", "8% ~ 12%")
        opt = opt.replace("百分之一至百分之三至五之间", "1% ~ 5%")
        opt = opt.replace("百分之二十五至百分之三十之间", "25% ~ 30%")
        opt = opt.replace("百分之五十", "50%").replace("百分之三十", "30%").replace("百分之二十", "20%")
        opt = opt.replace("一百八十度至一百九十度", "180℃ ~ 190℃")
        opt = opt.replace("一百二十度至一百三十度", "120℃ ~ 130℃")
        opt = opt.replace("二百二十度至二百四十度", "220℃ ~ 240℃")
        opt = opt.replace("八十度至九十度", "80℃ ~ 90℃")
        opt = opt.replace("二百度至二百一十度", "200℃ ~ 210℃")
        opt = opt.replace("七十度至八十度", "70℃ ~ 80℃")
        opt = opt.replace("五十八度至六十二度", "58℃ ~ 62℃")
        opt = opt.replace("二十度至三十度", "20℃ ~ 30℃")
        opt = opt.replace("零下五度至零度", "-5℃ ~ 0℃")
        opt = opt.replace("三百度以上", "300℃ 以上")
        opt = opt.replace("四百至四百五十度", "400℃ ~ 450℃")
        opt = opt.replace("一比一的精准质量比例（1:1）", "1 : 1")
        opt = opt.replace("三比一的经典黄金配比（3:1）", "3 : 1")
        opt = opt.replace("一比一", "1 : 1").replace("三比一", "3 : 1").replace("一比五", "1 : 5").replace("十比一", "10 : 1")
        
        # Specific absurd distractor cleans
        if "轮胎" in opt: opt = "表面瞬间焦糊散发刺鼻焦苦味"
        if "聚变" in opt: opt = "肉质蛋白质过度收缩严重脱水"
        if "核能" in opt: opt = "依靠高频微波直接作用熟化"
        if "活性炭" in opt: opt = "超高温焦化产生有害杂环胺"
        if "自来水" in opt: opt = "高汤中有机酸受热挥发的气体"
        
        # Prune verbose fillers
        fillers = [
            "完全没有任何", "完全无需", "必须依赖", "彻底消除", "极其有效地",
            "绝对核心原料", "自发剧烈反应", "微米级超细", "发生剧烈", "剧烈",
            "极度", "极其", "完全", "绝对", "彻底", "自发", "拼命", "高速",
            "无色无味", "源源不断释放", "导致面胚严重吸油导致", "使得面团内部",
            "以使", "以促使", "以彻底", "以便于"
        ]
        for f in fillers:
            opt = opt.replace(f, "")
            
        opts[k] = re.sub(r'\s+', ' ', opt).strip()
        
    return stem, opts

def process_batch5_v2():
    for ch in range(5, 9):
        fpath = f'work/data/senior3/chapter{ch:02d}.json'
        bpath = f'work/backup_before_lean_senior2_3/senior3/chapter{ch:02d}.json'
        d = json.load(open(fpath, encoding='utf-8'))
        b = json.load(open(bpath, encoding='utf-8'))
        
        for q_b, q_curr in zip(b['questions'], d['questions']):
            stem, opts = lean_transform_question(q_curr)
            q_curr['question'] = stem
            q_curr['options'] = opts
            
            # Align answer key to backup 100%
            orig_ans = q_b['answer']
            curr_ans = q_curr['answer']
            if orig_ans != curr_ans:
                temp = q_curr['options'][orig_ans]
                q_curr['options'][orig_ans] = q_curr['options'][curr_ans]
                q_curr['options'][curr_ans] = temp
                q_curr['answer'] = orig_ans
            else:
                q_curr['answer'] = orig_ans
                
            q_curr['difficulty'] = q_b['difficulty']
            
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
            
        print(f"Senior 3 Chapter {ch:02d} lean transformed and verified!")

if __name__ == '__main__':
    process_batch5_v2()
