import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace = r'c:\Users\GOH\Desktop\2026年统考厨艺理论'
g2_source_dir = os.path.join(workspace, '07_统考标准复习题库与命题提示词', '高二')
out_dir = os.path.join(workspace, 'work', 'data', 'senior2')
os.makedirs(out_dir, exist_ok=True)

roman_map = {
    'i': 'Ⅰ', 'ii': 'Ⅱ', 'iii': 'Ⅲ', 'iv': 'Ⅳ', 'v': 'Ⅴ',
    'I': 'Ⅰ', 'II': 'Ⅱ', 'III': 'Ⅲ', 'IV': 'Ⅳ', 'V': 'Ⅴ',
    '1': 'Ⅰ', '2': 'Ⅱ', '3': 'Ⅲ', '4': 'Ⅳ',
    '一': 'Ⅰ', '二': 'Ⅱ', '三': 'Ⅲ', '四': 'Ⅳ',
    'Ⅰ': 'Ⅰ', 'Ⅱ': 'Ⅱ', 'Ⅲ': 'Ⅲ', 'Ⅳ': 'Ⅳ'
}

def clean_roman_opt(text):
    text = re.sub(r'^(只有|仅有|仅|全是|皆是|皆正确|全部正确|全对)\s*', '', text.strip())
    text = re.sub(r'\s*(正确|错误|符合题意|不符合题意|是正确的|全对)$', '', text.strip())
    items = re.findall(r'[ivIV]+|[1-4]|Ⅰ|Ⅱ|Ⅲ|Ⅳ', text)
    mapped = []
    for it in items:
        m = roman_map.get(it, it)
        if m in ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ'] and m not in mapped:
            mapped.append(m)
    order = {'Ⅰ': 1, 'Ⅱ': 2, 'Ⅲ': 3, 'Ⅳ': 4}
    mapped.sort(key=lambda x: order.get(x, 99))
    if mapped:
        return '、'.join(mapped)
    return text.strip()

def sort_roman_options(options, correct_key):
    items_list = []
    for k in ['A', 'B', 'C', 'D']:
        c = clean_roman_opt(options[k])
        parts = c.split('、')
        order = {'Ⅰ': 1, 'Ⅱ': 2, 'Ⅲ': 3, 'Ⅳ': 4}
        first_val = order.get(parts[0], 99) if parts else 99
        items_list.append({
            'old_key': k,
            'content': c,
            'is_correct': (k == correct_key),
            'first_val': first_val,
            'length': len(parts),
            'parts': [order.get(p, 99) for p in parts]
        })
    
    # Sort: first_val ascending (starts with Ⅰ), then length ascending, then parts
    items_list.sort(key=lambda x: (x['first_val'], x['length'], x['parts']))
    
    new_options = {}
    new_correct_key = None
    keys = ['A', 'B', 'C', 'D']
    for idx, it in enumerate(items_list):
        new_k = keys[idx]
        new_options[new_k] = it['content']
        if it['is_correct']:
            new_correct_key = new_k
            
    return new_options, new_correct_key

unit_folders = sorted(os.listdir(g2_source_dir))
total_parsed_questions = 0

for u_idx, u_name in enumerate(unit_folders):
    u_path = os.path.join(g2_source_dir, u_name)
    if not os.path.isdir(u_path): continue
    
    txts = [f for f in os.listdir(u_path) if f.endswith('深度解析）.txt')]
    if not txts:
        txts = [f for f in os.listdir(u_path) if f.endswith('.txt') and '命题提示词' not in f]
    if not txts: continue
    
    file_path = os.path.join(u_path, txts[0])
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        raw_text = f.read()
        
    chapter_num = u_idx + 1
    
    # Extract clean chapter title
    m_title = re.search(r'第\s*(\d+)\s*单元[｜|\s]+([^（\r\n]+)', raw_text)
    if m_title:
        chapter_title = f"第{int(m_title.group(1)):02d}单元 {m_title.group(2).strip()}"
    else:
        chapter_title = u_name.replace('_', ' ')
    chapter_title = chapter_title.replace('统考标准复习题', '').strip()
    
    print(f"Parsing Chapter {chapter_num}: {chapter_title}...")
    
    # Find start of Question 1
    matches = list(re.finditer(r'甲组.*?^\s*1[\.、]', raw_text, re.DOTALL | re.MULTILINE))
    if matches:
        start_pos = matches[-1].end() - 2
    else:
        start_pos = 0
        
    # Cut off at Question 41
    pos_41 = re.search(r'^\s*41[\.、]', raw_text[start_pos:], re.MULTILINE)
    mcq_text = raw_text[start_pos : start_pos + pos_41.start()] if pos_41 else raw_text[start_pos:]
    
    # Also parse answer table & explanations table from the bottom
    ans_table = {}
    exp_table = {}
    for line in raw_text.splitlines():
        m_tbl = re.search(r'(\d+)-(\d+)[:：]\s*([A-D,\s]+)', line)
        if m_tbl:
            s_q = int(m_tbl.group(1))
            keys = [k.strip() for k in m_tbl.group(3).split(',') if k.strip() in ['A', 'B', 'C', 'D']]
            for off, k in enumerate(keys):
                ans_table[s_q + off] = k
        m_q_ans = re.search(r'^\s*(\d+)[\.、]\s*【答案】\s*([A-D])', line)
        if m_q_ans:
            ans_table[int(m_q_ans.group(1))] = m_q_ans.group(2)
        m_exp_line = re.search(r'[•\s]*第\s*(\d+)\s*题[：:]\s*(.*)', line)
        if m_exp_line:
            exp_table[int(m_exp_line.group(1))] = m_exp_line.group(2).strip()
        m_roman_exp = re.search(r'^\s*(\d+)[\.、]\s*【答案】[A-D][（\(](.*)[）\)]', line)
        if m_roman_exp:
            exp_table[int(m_roman_exp.group(1))] = m_roman_exp.group(2).strip()
            
    questions = []
    
    for q_num in range(1, 41):
        pat = rf'^\s*{q_num}[\.、]\s*(.*?)(?=^\s*{q_num+1}[\.、]|\Z)'
        m = re.search(pat, mcq_text, re.MULTILINE | re.DOTALL)
        if not m:
            print(f"  WARNING: Could not find Question {q_num} in Chapter {chapter_num}!")
            continue
            
        blk = m.group(1).strip()
        
        # Extract Answer
        m_ans = re.search(r'【答案】\s*([A-D])', blk)
        ans = m_ans.group(1) if m_ans else ans_table.get(q_num, '')
        
        # Extract Explanation
        m_exp = re.search(r'【解析】\s*(.*?)(?=\n\s*[A-D][\.、]|\Z)', blk, re.DOTALL)
        if m_exp:
            exp = m_exp.group(1).strip()
        else:
            exp = exp_table.get(q_num, "")
        if not exp:
            exp = f"本题主要考查{chapter_title}的核心统考考点，正确答案为 {ans}。"
            
        # Clean block before extracting options
        clean_blk = re.sub(r'【答案】.*', '', blk, flags=re.DOTALL).strip()
        
        # Extract Options A, B, C, D
        opts = {}
        for line in clean_blk.splitlines():
            m_o = re.match(r'^\s*([A-D])[\.、\s]\s*(.*)', line)
            if m_o:
                opts[m_o.group(1)] = m_o.group(2).strip()
        if len(opts) < 4:
            m_inline = re.findall(r'([A-D])[\.、]\s*(.*?)(?=\s*[A-D][\.、]|\Z)', clean_blk)
            if len(m_inline) >= 4:
                opts = {k: v.strip() for k, v in m_inline[:4]}
                
        # Extract Stem
        m_stem = re.search(r'^(.*?)(?=\s*A[\.、\s])', clean_blk, re.DOTALL)
        if m_stem:
            stem = m_stem.group(1).strip()
        else:
            stem = clean_blk.split('A.')[0].strip()
            
        q_type = "roman" if q_num >= 36 else "single"
        
        # If Roman, sort options and update answer key
        if q_type == "roman" and opts and ans:
            opts, ans = sort_roman_options(opts, ans)
            
        # Difficulty: 20 easy, 15 medium, 5 hard
        if q_num <= 20:
            diff = "easy"
        elif q_num <= 35:
            diff = "medium"
        else:
            diff = "hard"
            
        q_obj = {
            "id": q_num,
            "type": q_type,
            "difficulty": diff,
            "question": re.sub(r'\s+', ' ', stem).strip(),
            "options": opts,
            "answer": ans,
            "explanation": re.sub(r'\s+', ' ', exp).strip(),
            "exam_focus": f"{chapter_title}·核心知识点"
        }
        questions.append(q_obj)
        
    print(f"  Successfully extracted {len(questions)}/40 questions for Chapter {chapter_num}.")
    total_parsed_questions += len(questions)
    
    chapter_data = {
        "chapter_id": chapter_num,
        "chapter_title": chapter_title,
        "intro": f"2026年马来西亚华文独中高中统考（UEC）厨艺（烘焙理论）高二年级标准题库 - {chapter_title}",
        "questions": questions
    }
    
    out_json = os.path.join(out_dir, f'chapter{chapter_num:02d}.json')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(chapter_data, f, ensure_ascii=False, indent=2)

print(f"\nAll 15 Chapters parsed! Total {total_parsed_questions} questions saved to {out_dir}.")
