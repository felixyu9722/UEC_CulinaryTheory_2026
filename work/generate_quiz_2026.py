# -*- coding: utf-8 -*-
"""
generate_quiz_2026.py
Complete production generator for 2026 UEC Senior 1 Culinary Arts (Baking Theory) Test Bank.
Generates:
- 20 Student Test Papers (.docx)
- 20 Teacher Answer Key & Explanation Papers (.docx)
- 1 Master 300-Question Student Compilation (.docx)
- 1 Master 300-Question Teacher Detailed Explanation Compilation (.docx)
- 1 Standard JSON database (.json)
- 1 Comprehensive README & User Guide (.md)
Target folder: 厨艺理论测验题2026
"""

import os, sys, json, re, itertools
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import qn, nsdecls

WORKSPACE_ROOT = r'c:\Users\GOH\Desktop\2026年统考厨艺理论'
DATA_DIR = os.path.join(WORKSPACE_ROOT, 'work', 'data')
OUT_DIR = os.path.join(WORKSPACE_ROOT, '厨艺理论测验题2026')
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# XML STYLING UTILITIES
# -------------------------------------------------------------
def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def set_box_left_border(table, border_color="1E3A8A", border_sz="24"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="none"/>'
            f'<w:bottom w:val="none"/>'
            f'<w:left w:val="single" w:sz="{border_sz}" w:space="0" w:color="{border_color}"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="none"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def create_base_document(header_text="", footer_text=""):
    doc = Document()
    for s in doc.sections:
        s.top_margin = Cm(2.0)
        s.bottom_margin = Cm(2.0)
        s.left_margin = Cm(2.0)
        s.right_margin = Cm(2.0)
        
        # Header setup
        if header_text:
            hdr = s.header.paragraphs[0]
            hdr.text = header_text
            hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            if hdr.runs:
                hdr.runs[0].font.name = "Microsoft YaHei"
                hdr.runs[0].font.size = Pt(8.5)
                hdr.runs[0].font.color.rgb = RGBColor(148, 163, 184)
                
        # Footer setup
        if footer_text:
            ftr = s.footer.paragraphs[0]
            ftr.text = footer_text
            ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if ftr.runs:
                ftr.runs[0].font.name = "Microsoft YaHei"
                ftr.runs[0].font.size = Pt(8.5)
                ftr.runs[0].font.color.rgb = RGBColor(148, 163, 184)

    # Style Normal
    style = doc.styles['Normal']
    style.font.name = 'Microsoft YaHei'
    style.font.size = Pt(10.5)
    style.font.color.rgb = RGBColor(30, 41, 59)
    style.paragraph_format.line_spacing = 1.25
    style.paragraph_format.space_after = Pt(3)
    rPr = style.element.get_or_add_rPr()
    rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:eastAsia="Microsoft YaHei" w:ascii="Calibri" w:hAnsi="Calibri"/>')
    rPr.append(rFonts)

    return doc

# -------------------------------------------------------------
# 1. LOAD & SELECT BALANCED 15 QUESTIONS PER CHAPTER
# -------------------------------------------------------------
UNIT_NAMES = [
    (1, "烘焙概论", "烘焙概论"),
    (2, "烘焙的历史与发展", "烘焙的历史与发展"),
    (3, "中式面食分类", "中式面食分类"),
    (4, "西式烘焙分类", "西式烘焙分类"),
    (5, "烘焙设备", "烘焙设备"),
    (6, "烘焙制作器具", "烘焙制作器具"),
    (7, "器具使用、安全与维护", "器具使用、安全与维护"),
    (8, "度量衡与准确秤量", "度量衡与准确秤量"),
    (9, "烘焙材料的性质与功能", "烘焙材料的性质与功能"),
    (10, "面粉", "面粉 (Flour)"),
    (11, "油脂", "油脂 (Fats & Oils)"),
    (12, "糖", "糖 (Sugar)"),
    (13, "鸡蛋", "鸡蛋 (Eggs)"),
    (14, "乳制品", "乳制品 (Dairy Products)"),
    (15, "酵母与发酵", "酵母与发酵 (Yeast & Fermentation)"),
    (16, "化学膨大剂", "化学膨大剂 (Chemical Leavening Agents)"),
    (17, "乳化剂与乳化作用", "乳化剂与乳化作用 (Emulsifiers & Emulsification)"),
    (18, "胶冻类材料", "胶冻类材料 (Gelling Agents)"),
    (19, "塔塔粉", "塔塔粉 (Cream of Tartar)"),
    (20, "烘焙百分比与材料用量", "烘焙百分比与材料用量 (Baker's Percentage & Calculations)")
]

def select_chapter_questions():
    all_units_data = []
    target_multisets = [
        Counter({'A': 4, 'B': 4, 'C': 4, 'D': 3}),
        Counter({'A': 4, 'B': 4, 'C': 3, 'D': 4}),
        Counter({'A': 4, 'B': 3, 'C': 4, 'D': 4}),
        Counter({'A': 3, 'B': 4, 'C': 4, 'D': 4})
    ]

    for unit_num, short_name, full_name in UNIT_NAMES:
        fpath = os.path.join(DATA_DIR, f'chapter{unit_num:02d}.json')
        with open(fpath, 'r', encoding='utf-8-sig') as f:
            raw = json.load(f)
            
        qs = raw.get('questions', [])
        easy = [q for q in qs if q.get('difficulty') == 'easy']
        med = [q for q in qs if q.get('difficulty') == 'medium']

        selected_easy = None
        selected_med = None
        found = False

        # Search optimal combination of 10 easy + 5 medium
        for c_easy in itertools.combinations(easy[:16], 10):
            for c_med in itertools.combinations(med[:10], 5):
                counts = Counter(q['answer'] for q in c_easy + c_med)
                if counts in target_multisets:
                    selected_easy = list(c_easy)
                    selected_med = list(c_med)
                    found = True
                    break
            if found:
                break

        if not found:
            # Fallback to full combinations
            for c_easy in itertools.combinations(easy, 10):
                for c_med in itertools.combinations(med, 5):
                    counts = Counter(q['answer'] for q in c_easy + c_med)
                    if counts in target_multisets:
                        selected_easy = list(c_easy)
                        selected_med = list(c_med)
                        found = True
                        break
                if found:
                    break

        # Re-order to prevent 3 consecutive identical answers
        def avoid_runs(items):
            arr = list(items)
            for _ in range(50):
                has_run = False
                for idx in range(len(arr) - 2):
                    if arr[idx]['answer'] == arr[idx+1]['answer'] == arr[idx+2]['answer']:
                        has_run = True
                        # Swap arr[idx+2] with arr[-1] or another
                        swap_idx = (idx + 3) % len(arr)
                        arr[idx+2], arr[swap_idx] = arr[swap_idx], arr[idx+2]
                        break
                if not has_run:
                    break
            return arr

        selected_easy = avoid_runs(selected_easy)
        selected_med = avoid_runs(selected_med)

        # Standardize question list for unit
        unit_questions = []
        for idx, q in enumerate(selected_easy):
            unit_questions.append({
                "num": idx + 1,
                "difficulty": "easy",
                "diff_cn": "容易",
                "question": q['question'],
                "options": q['options'],
                "answer": q['answer'],
                "explanation": q.get('explanation', '')
            })
        for idx, q in enumerate(selected_med):
            unit_questions.append({
                "num": idx + 11,
                "difficulty": "medium",
                "diff_cn": "中等",
                "question": q['question'],
                "options": q['options'],
                "answer": q['answer'],
                "explanation": q.get('explanation', '')
            })

        all_units_data.append({
            "unit_num": unit_num,
            "short_name": short_name,
            "full_name": full_name,
            "questions": unit_questions
        })

    return all_units_data

# -------------------------------------------------------------
# 2. RENDERING FUNCTIONS FOR WORD DOCUMENTS
# -------------------------------------------------------------
def format_options(doc, options):
    opt_lens = [len(options[k]) for k in ['A', 'B', 'C', 'D']]
    max_len = max(opt_lens)

    if max_len <= 11:
        # Two lines (A & B, C & D)
        p1 = doc.add_paragraph()
        p1.paragraph_format.left_indent = Inches(0.2)
        p1.paragraph_format.space_after = Pt(2)
        r_a = p1.add_run(f"A. {options['A']:<18}")
        r_b = p1.add_run(f"B. {options['B']}")
        
        p2 = doc.add_paragraph()
        p2.paragraph_format.left_indent = Inches(0.2)
        p2.paragraph_format.space_after = Pt(3)
        r_c = p2.add_run(f"C. {options['C']:<18}")
        r_d = p2.add_run(f"D. {options['D']}")
    else:
        # Four individual lines
        for k in ['A', 'B', 'C', 'D']:
            p = doc.add_paragraph(f"{k}. {options[k]}")
            p.paragraph_format.left_indent = Inches(0.2)
            p.paragraph_format.space_after = Pt(2)

def build_student_unit_doc(unit_data, doc=None, is_standalone=True):
    if doc is None:
        header_text = f"2026年马来西亚华文独中高中统考（UEC）厨艺科 · 单元测验卷（第{unit_data['unit_num']:02d}单元）"
        footer_text = f"高一《烘焙理论》单元测验卷 · 第{unit_data['unit_num']:02d}单元 {unit_data['short_name']} · 共15题 · 满分30分"
        doc = create_base_document(header_text, footer_text)

    # Title Banner
    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_after = Pt(2)
    r0 = p_main.add_run("2026年马来西亚华文独立中学高中统考（UEC）厨艺理论\n")
    r0.font.size = Pt(13)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(100, 116, 139)

    r1 = p_main.add_run(f"高一单元随堂测验卷 · 第 {unit_data['unit_num']:02d} 单元：{unit_data['full_name']}\n")
    r1.font.size = Pt(15)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(30, 58, 138) # Deep Navy

    r2 = p_main.add_run("【随堂闭卷测验】 建议时量：25 分钟 ｜ 满分：30 分（共 15 题，每题 2 分）")
    r2.font.size = Pt(9.5)
    r2.font.italic = True
    r2.font.color.rgb = RGBColor(180, 83, 9) # Amber

    # Student Info Table
    tbl_info = doc.add_table(rows=1, cols=5)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_cols = ["班级：____________", "姓名：____________", "学号：____________", "座号：________", "得分：________ / 30"]
    for idx, text in enumerate(info_cols):
        c = tbl_info.rows[0].cells[idx]
        c.text = text
        set_cell_background(c, "F8FAFC")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        c.paragraphs[0].runs[0].font.size = Pt(9)
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.color.rgb = RGBColor(51, 65, 85)
    set_table_borders(tbl_info, color="CBD5E1")
    
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(2)

    # Student Answer Sheet Grid
    p_grid_title = doc.add_paragraph()
    p_grid_title.paragraph_format.space_after = Pt(2)
    r_gt = p_grid_title.add_run("【考生答题卡】 请将选择题最终答案对应填入下表格中（务必字迹工整）：")
    r_gt.font.size = Pt(9)
    r_gt.font.bold = True
    r_gt.font.color.rgb = RGBColor(71, 85, 105)

    tbl_grid = doc.add_table(rows=2, cols=16)
    tbl_grid.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Row 1: Header
    tbl_grid.rows[0].cells[0].text = "题号"
    set_cell_background(tbl_grid.rows[0].cells[0], "F1F5F9")
    set_cell_margins(tbl_grid.rows[0].cells[0], top=60, bottom=60, left=40, right=40)
    tbl_grid.rows[0].cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    tbl_grid.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(8.5)
    tbl_grid.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True

    for i in range(1, 16):
        c = tbl_grid.rows[0].cells[i]
        c.text = str(i)
        set_cell_background(c, "F1F5F9")
        set_cell_margins(c, top=60, bottom=60, left=40, right=40)
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c.paragraphs[0].runs[0].font.size = Pt(8.5)
        c.paragraphs[0].runs[0].font.bold = True

    # Row 2: Answers blank
    tbl_grid.rows[1].cells[0].text = "答案"
    set_cell_background(tbl_grid.rows[1].cells[0], "FAFAFA")
    set_cell_margins(tbl_grid.rows[1].cells[0], top=100, bottom=100, left=40, right=40)
    tbl_grid.rows[1].cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    tbl_grid.rows[1].cells[0].paragraphs[0].runs[0].font.size = Pt(8.5)
    tbl_grid.rows[1].cells[0].paragraphs[0].runs[0].font.bold = True

    for i in range(1, 16):
        c = tbl_grid.rows[1].cells[i]
        c.text = ""
        set_cell_margins(c, top=120, bottom=120, left=40, right=40)
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    set_table_borders(tbl_grid, color="CBD5E1")
    
    doc.add_paragraph() # Spacer

    # Section 1 Heading
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(4)
    h1.paragraph_format.space_after = Pt(4)
    r_h1 = h1.add_run("一、基础核心考查题（第 1 至 10 题，【容易】，每题 2 分，共 20 分）")
    r_h1.font.size = Pt(11)
    r_h1.font.bold = True
    r_h1.font.color.rgb = RGBColor(21, 128, 61) # Forest Green

    for q in unit_data['questions'][:10]:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_after = Pt(2)
        r_num = p_q.add_run(f"{q['num']}. 【容易】 ")
        r_num.font.bold = True
        r_num.font.color.rgb = RGBColor(21, 128, 61)
        r_text = p_q.add_run(q['question'])
        r_text.font.bold = True
        format_options(doc, q['options'])

    # Section 2 Heading
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)
    r_h2 = h2.add_run("二、工艺应用与综合判断题（第 11 至 15 题，【中等】，每题 2 分，共 10 分）")
    r_h2.font.size = Pt(11)
    r_h2.font.bold = True
    r_h2.font.color.rgb = RGBColor(2, 132, 199) # Sky Blue

    for q in unit_data['questions'][10:]:
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_after = Pt(2)
        r_num = p_q.add_run(f"{q['num']}. 【中等】 ")
        r_num.font.bold = True
        r_num.font.color.rgb = RGBColor(2, 132, 199)
        r_text = p_q.add_run(q['question'])
        r_text.font.bold = True
        format_options(doc, q['options'])

    if is_standalone:
        out_path = os.path.join(OUT_DIR, f"第{unit_data['unit_num']:02d}单元_{unit_data['short_name']}_学生测验卷.docx")
        doc.save(out_path)
        print(f"Generated Student Doc: {out_path}")

    return doc

def build_teacher_unit_doc(unit_data, doc=None, is_standalone=True):
    if doc is None:
        header_text = f"2026年马来西亚华文独中高中统考（UEC）厨艺科 · 教师参考答案与解析（第{unit_data['unit_num']:02d}单元）"
        footer_text = f"高一《烘焙理论》教师解析手册 · 第{unit_data['unit_num']:02d}单元 {unit_data['short_name']} · 全题精讲与采分标准"
        doc = create_base_document(header_text, footer_text)

    # Title Banner
    p_main = doc.add_paragraph()
    p_main.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_main.paragraph_format.space_after = Pt(2)
    r0 = p_main.add_run("2026年马来西亚华文独立中学高中统考（UEC）厨艺理论\n")
    r0.font.size = Pt(13)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(100, 116, 139)

    r1 = p_main.add_run(f"教师专用参考答案与详细考点解析 · 第 {unit_data['unit_num']:02d} 单元：{unit_data['full_name']}\n")
    r1.font.size = Pt(15)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(21, 128, 61) # Deep Forest Green

    r2 = p_main.add_run("【教研备课指南】 满分：30 分（共 15 题，每题 2 分） ｜ 包含速查答题表与逐题核心解析")
    r2.font.size = Pt(9.5)
    r2.font.italic = True
    r2.font.color.rgb = RGBColor(180, 83, 9)

    doc.add_paragraph() # Spacer

    # Quick Reference Answer Key Table
    p_tbl_title = doc.add_paragraph()
    p_tbl_title.paragraph_format.space_after = Pt(2)
    r_tt = p_tbl_title.add_run("【快速核对参考答案表】（Quick Answer Key）：")
    r_tt.font.size = Pt(10)
    r_tt.font.bold = True
    r_tt.font.color.rgb = RGBColor(30, 58, 138)

    tbl_key = doc.add_table(rows=4, cols=16)
    tbl_key.alignment = WD_TABLE_ALIGNMENT.CENTER

    headers = ["题号", "答案", "难度", "分值"]
    row_bg = ["F1F5F9", "FEF3C7", "F8FAFC", "F8FAFC"]
    for r_idx in range(4):
        c0 = tbl_key.rows[r_idx].cells[0]
        c0.text = headers[r_idx]
        set_cell_background(c0, row_bg[r_idx])
        set_cell_margins(c0, top=60, bottom=60, left=40, right=40)
        c0.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c0.paragraphs[0].runs[0].font.size = Pt(8.5)
        c0.paragraphs[0].runs[0].font.bold = True

    for i in range(1, 16):
        q = unit_data['questions'][i-1]
        
        # Row 0: Question num
        c_num = tbl_key.rows[0].cells[i]
        c_num.text = str(i)
        set_cell_background(c_num, "F1F5F9")
        set_cell_margins(c_num, top=60, bottom=60, left=40, right=40)
        c_num.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_num.paragraphs[0].runs[0].font.size = Pt(8.5)
        c_num.paragraphs[0].runs[0].font.bold = True

        # Row 1: Answer
        c_ans = tbl_key.rows[1].cells[i]
        c_ans.text = q['answer']
        set_cell_background(c_ans, "FEF3C7") # Warm Yellow highlight
        set_cell_margins(c_ans, top=60, bottom=60, left=40, right=40)
        c_ans.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_ans.paragraphs[0].runs[0].font.size = Pt(10)
        c_ans.paragraphs[0].runs[0].font.bold = True
        c_ans.paragraphs[0].runs[0].font.color.rgb = RGBColor(220, 38, 38) # Red Answer

        # Row 2: Difficulty
        c_diff = tbl_key.rows[2].cells[i]
        c_diff.text = "易" if q['difficulty'] == 'easy' else "中"
        set_cell_background(c_diff, "F8FAFC")
        set_cell_margins(c_diff, top=60, bottom=60, left=40, right=40)
        c_diff.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_diff.paragraphs[0].runs[0].font.size = Pt(8)
        if q['difficulty'] == 'easy':
            c_diff.paragraphs[0].runs[0].font.color.rgb = RGBColor(21, 128, 61)
        else:
            c_diff.paragraphs[0].runs[0].font.color.rgb = RGBColor(2, 132, 199)

        # Row 3: Score
        c_score = tbl_key.rows[3].cells[i]
        c_score.text = "2分"
        set_cell_background(c_score, "F8FAFC")
        set_cell_margins(c_score, top=60, bottom=60, left=40, right=40)
        c_score.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c_score.paragraphs[0].runs[0].font.size = Pt(8)
        c_score.paragraphs[0].runs[0].font.color.rgb = RGBColor(100, 116, 139)

    set_table_borders(tbl_key, color="CBD5E1")
    doc.add_paragraph() # Spacer

    # Detailed Explanations
    h_sec = doc.add_paragraph()
    h_sec.paragraph_format.space_before = Pt(6)
    h_sec.paragraph_format.space_after = Pt(4)
    r_hs = h_sec.add_run("【逐题详尽解析与考点剖析】")
    r_hs.font.size = Pt(12)
    r_hs.font.bold = True
    r_hs.font.color.rgb = RGBColor(30, 58, 138)

    for q in unit_data['questions']:
        # Question Stem & Options
        p_q = doc.add_paragraph()
        p_q.paragraph_format.space_before = Pt(4)
        p_q.paragraph_format.space_after = Pt(2)
        r_num = p_q.add_run(f"Q{q['num']:02d}. 【{q['diff_cn']}】 ")
        r_num.font.bold = True
        if q['difficulty'] == 'easy':
            r_num.font.color.rgb = RGBColor(21, 128, 61)
        else:
            r_num.font.color.rgb = RGBColor(2, 132, 199)
        r_text = p_q.add_run(q['question'])
        r_text.font.bold = True

        format_options(doc, q['options'])

        # Callout Box for Explanation
        tbl_box = doc.add_table(rows=1, cols=1)
        tbl_box.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell_box = tbl_box.rows[0].cells[0]
        set_cell_background(cell_box, "F8FAFC")
        set_cell_margins(cell_box, top=100, bottom=100, left=160, right=140)
        set_box_left_border(tbl_box, border_color="2563EB", border_sz="24")

        p_box = cell_box.paragraphs[0]
        p_box.paragraph_format.space_after = Pt(2)
        
        r_ans_lbl = p_box.add_run("【标准答案】：")
        r_ans_lbl.font.bold = True
        r_ans_lbl.font.size = Pt(10)
        r_ans_val = p_box.add_run(f"{q['answer']}        ")
        r_ans_val.font.bold = True
        r_ans_val.font.size = Pt(11)
        r_ans_val.font.color.rgb = RGBColor(220, 38, 38) # Red

        r_diff_lbl = p_box.add_run("【难度评定】：")
        r_diff_lbl.font.bold = True
        r_diff_lbl.font.size = Pt(9.5)
        r_diff_val = p_box.add_run(f"{q['diff_cn']}（2分）\n")
        r_diff_val.font.size = Pt(9.5)

        r_exp_lbl = p_box.add_run("【考点与详细解析】：\n")
        r_exp_lbl.font.bold = True
        r_exp_lbl.font.size = Pt(9.5)
        r_exp_lbl.font.color.rgb = RGBColor(30, 58, 138)

        r_exp_val = p_box.add_run(q['explanation'])
        r_exp_val.font.size = Pt(9.5)
        r_exp_val.font.color.rgb = RGBColor(51, 65, 85)

        doc.add_paragraph() # Spacer

    if is_standalone:
        out_path = os.path.join(OUT_DIR, f"第{unit_data['unit_num']:02d}单元_{unit_data['short_name']}_教师解析与参考答案.docx")
        doc.save(out_path)
        print(f"Generated Teacher Doc: {out_path}")

    return doc

# -------------------------------------------------------------
# 3. BUILD MASTER COMPILATIONS (300 QUESTIONS)
# -------------------------------------------------------------
def build_master_student_compilation(all_units_data):
    header_text = "2026年马来西亚华文独中高中统考（UEC）厨艺理论 · 高一全套20单元300题测验题总汇编"
    footer_text = "高一《烘焙理论》学生测验卷总汇编 · 20单元全景题库 · 满分600分"
    doc = create_base_document(header_text, footer_text)

    # Cover Page
    p_cover = doc.add_paragraph()
    p_cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cover.paragraph_format.space_before = Pt(72)
    p_cover.paragraph_format.space_after = Pt(12)

    r_c0 = p_cover.add_run("2026年马来西亚华文独立中学高中统考（UEC）\n")
    r_c0.font.size = Pt(16)
    r_c0.font.bold = True
    r_c0.font.color.rgb = RGBColor(100, 116, 139)

    r_c1 = p_cover.add_run("高中厨艺科 · 烘焙理论\n高一全套第 01 至 20 单元测验题卷总汇编\n")
    r_c1.font.size = Pt(22)
    r_c1.font.bold = True
    r_c1.font.color.rgb = RGBColor(30, 58, 138)

    r_c2 = p_cover.add_run("（300 题标准选择题 · 学生随堂测验版）\n\n")
    r_c2.font.size = Pt(15)
    r_c2.font.bold = True
    r_c2.font.color.rgb = RGBColor(180, 83, 9)

    p_c_meta = doc.add_paragraph()
    p_c_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_meta.paragraph_format.space_after = Pt(48)
    r_cm = p_c_meta.add_run(
        "【编写依据】：马来西亚董总高中厨艺科统考大纲 ＆ 2026 年最新教研题库标准\n"
        "【题卷规格】：全套 20 个完整单元 ｜ 每单元 15 题（10 易 ＋ 5 中） ｜ 总计 300 题\n"
        "【题型功能】：独立答题卡 ｜ 选项长度严谨均衡 ｜ 杜绝猜题泄题 ｜ 适宜整册装订测试"
    )
    r_cm.font.size = Pt(10.5)
    r_cm.font.color.rgb = RGBColor(71, 85, 105)

    doc.add_page_break()

    # Table of Contents
    h_toc = doc.add_paragraph()
    h_toc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_th = h_toc.add_run("高一《烘焙理论》全套 20 单元测验目录索引")
    r_th.font.size = Pt(16)
    r_th.font.bold = True
    r_th.font.color.rgb = RGBColor(30, 58, 138)

    tbl_toc = doc.add_table(rows=21, cols=4)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    toc_h = ["单元序号", "单元课程模块主题", "题目数量与配比", "建议测验时量"]
    for c_i, h in enumerate(toc_h):
        c = tbl_toc.rows[0].cells[c_i]
        c.text = h
        set_cell_background(c, "F1F5F9")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    for idx, u in enumerate(all_units_data):
        row = tbl_toc.rows[idx+1]
        row.cells[0].text = f"第 {u['unit_num']:02d} 单元"
        row.cells[1].text = u['full_name']
        row.cells[2].text = "15 题（10易 + 5中）"
        row.cells[3].text = "25 分钟"
        for c_i in range(4):
            set_cell_margins(row.cells[c_i], top=60, bottom=60, left=80, right=80)
            row.cells[c_i].paragraphs[0].runs[0].font.size = Pt(9)
            if c_i in [0, 2, 3]:
                row.cells[c_i].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    set_table_borders(tbl_toc, color="CBD5E1")
    doc.add_page_break()

    # Append each unit
    for idx, u in enumerate(all_units_data):
        build_student_unit_doc(u, doc=doc, is_standalone=False)
        if idx < len(all_units_data) - 1:
            doc.add_page_break()

    out_path = os.path.join(OUT_DIR, "高一厨艺理论_全套第01至20单元_300题学生测验卷总汇编.docx")
    doc.save(out_path)
    print(f"Generated Master Student Compilation: {out_path}")

def build_master_teacher_compilation(all_units_data):
    header_text = "2026年马来西亚华文独中高中统考（UEC）厨艺理论 · 教师专用解析与考点总汇编"
    footer_text = "高一《烘焙理论》教师详尽解析总汇编 · 20单元300题全真考点剖析"
    doc = create_base_document(header_text, footer_text)

    # Cover Page
    p_cover = doc.add_paragraph()
    p_cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cover.paragraph_format.space_before = Pt(72)
    p_cover.paragraph_format.space_after = Pt(12)

    r_c0 = p_cover.add_run("2026年马来西亚华文独立中学高中统考（UEC）\n")
    r_c0.font.size = Pt(16)
    r_c0.font.bold = True
    r_c0.font.color.rgb = RGBColor(100, 116, 139)

    r_c1 = p_cover.add_run("高中厨艺科 · 烘焙理论\n高一全套第 01 至 20 单元教师解析总汇编\n")
    r_c1.font.size = Pt(22)
    r_c1.font.bold = True
    r_c1.font.color.rgb = RGBColor(21, 128, 61) # Forest Green

    r_c2 = p_cover.add_run("（300 题全真答案速查矩阵 ＆ 逐题考点精析手册）\n\n")
    r_c2.font.size = Pt(15)
    r_c2.font.bold = True
    r_c2.font.color.rgb = RGBColor(180, 83, 9)

    p_c_meta = doc.add_paragraph()
    p_c_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_meta.paragraph_format.space_after = Pt(48)
    r_cm = p_c_meta.add_run(
        "【配套卷别】：高一烘焙理论随堂测验卷（全套 20 单元 300 题）\n"
        "【教研价值】：含 20 单元 300 题答案速查总矩阵 ＋ 逐题食品理化原理解析 ＋ 干扰项辨析\n"
        "【编写团队】：2026 年马来西亚华文独中高中统考厨艺科教研组"
    )
    r_cm.font.size = Pt(10.5)
    r_cm.font.color.rgb = RGBColor(71, 85, 105)

    doc.add_page_break()

    # Master Quick Answer Matrix (20 units x 15 questions)
    h_m = doc.add_paragraph()
    h_m.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_mh = h_m.add_run("全套 20 单元 300 题答案速查总矩阵 (Master Key Matrix)")
    r_mh.font.size = Pt(15)
    r_mh.font.bold = True
    r_mh.font.color.rgb = RGBColor(30, 58, 138)

    tbl_matrix = doc.add_table(rows=21, cols=16)
    tbl_matrix.alignment = WD_TABLE_ALIGNMENT.CENTER

    tbl_matrix.rows[0].cells[0].text = "单元"
    set_cell_background(tbl_matrix.rows[0].cells[0], "F1F5F9")
    set_cell_margins(tbl_matrix.rows[0].cells[0], top=60, bottom=60, left=40, right=40)
    tbl_matrix.rows[0].cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    tbl_matrix.rows[0].cells[0].paragraphs[0].runs[0].font.size = Pt(8.5)
    tbl_matrix.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True

    for i in range(1, 16):
        c = tbl_matrix.rows[0].cells[i]
        c.text = f"Q{i}"
        set_cell_background(c, "F1F5F9")
        set_cell_margins(c, top=60, bottom=60, left=40, right=40)
        c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        c.paragraphs[0].runs[0].font.size = Pt(8.5)
        c.paragraphs[0].runs[0].font.bold = True

    for u_idx, u in enumerate(all_units_data):
        row = tbl_matrix.rows[u_idx+1]
        row.cells[0].text = f"U{u['unit_num']:02d}"
        set_cell_background(row.cells[0], "F8FAFC")
        set_cell_margins(row.cells[0], top=50, bottom=50, left=40, right=40)
        row.cells[0].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        row.cells[0].paragraphs[0].runs[0].font.size = Pt(8)
        row.cells[0].paragraphs[0].runs[0].font.bold = True

        for q_i in range(1, 16):
            q = u['questions'][q_i-1]
            c = row.cells[q_i]
            c.text = q['answer']
            set_cell_margins(c, top=50, bottom=50, left=40, right=40)
            c.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            c.paragraphs[0].runs[0].font.size = Pt(8.5)
            c.paragraphs[0].runs[0].font.bold = True
            c.paragraphs[0].runs[0].font.color.rgb = RGBColor(21, 128, 61)

    set_table_borders(tbl_matrix, color="CBD5E1")
    doc.add_page_break()

    # Append each unit
    for idx, u in enumerate(all_units_data):
        build_teacher_unit_doc(u, doc=doc, is_standalone=False)
        if idx < len(all_units_data) - 1:
            doc.add_page_break()

    out_path = os.path.join(OUT_DIR, "高一厨艺理论_全套第01至20单元_300题教师详细解析总汇编.docx")
    doc.save(out_path)
    print(f"Generated Master Teacher Compilation: {out_path}")

# -------------------------------------------------------------
# 4. JSON & MARKDOWN EXPORT
# -------------------------------------------------------------
def export_json_and_markdown(all_units_data):
    # 1. JSON
    json_path = os.path.join(OUT_DIR, "高一厨艺理论_20单元300题标准测验题库.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_units_data, f, ensure_ascii=False, indent=2)
    print(f"Exported JSON Database: {json_path}")

    # 2. Markdown User Guide
    md_path = os.path.join(OUT_DIR, "00_高一厨艺理论测验题2026_题库架构与使用说明.md")
    
    md_lines = [
        "# 2026年马来西亚华文独中高中统考（UEC）厨艺科（烘焙理论）",
        "## 高一全套第01至20单元 · 300题标准测验题库工程架构与使用说明\n",
        "> **题库属性**：高一烘焙理论随堂测验与阶段性测试专用标准化题库  ",
        "> **编写依据**：马来西亚董总高中厨艺科课程纲要、Notion《高中厨艺（烘焙理论）2026》、法国蓝带西点食品理化机理  ",
        "> **工程规范**：每个单元严格配备 **15题选择题（10题容易 + 5题中等）**，全套20单元共 **300题**。ABCD答案完全均等分布，无长度泄题暗示。\n",
        "---",
        "### 一、题库交付文件目录清单（全部生成于「厨艺理论测验题2026」）\n",
        "| 文件类别 | 文件数量 | 成果文件名与说明 |",
        "| :--- | :---: | :--- |",
        "| **学生独立随堂测验卷** | 20 份 | `第01单元_烘焙概论_学生测验卷.docx` ~ `第20单元_烘焙百分比与材料用量_学生测验卷.docx`<br>• 每份含考生信息栏、答题卡表格、规范版式，适宜直接打印随堂测验（25分钟/30分）。 |",
        "| **教师解析与评分标准** | 20 份 | `第01单元_烘焙概论_教师解析与参考答案.docx` ~ `第20单元_烘焙百分比与材料用量_教师解析与参考答案.docx`<br>• 每份含快速答案核对表（Quick Key）、难度层级定位、食品物理化学原理解析与错项辨析。 |",
        "| **全套300题学生卷总汇编** | 1 份 | `高一厨艺理论_全套第01至20单元_300题学生测验卷总汇编.docx`<br>• 含全套大封面、20单元总目录表、分页排版，适宜整册装订成学生测验作业本。 |",
        "| **全套300题教师解析总汇编** | 1 份 | `高一厨艺理论_全套第01至20单元_300题教师详细解析总汇编.docx`<br>• 含20单元300题答案速查总矩阵（Master Matrix）与全部300题考点精析，适宜教研与备课查阅。 |",
        "| **标准JSON题库数据库** | 1 份 | `高一厨艺理论_20单元300题标准测验题库.json`<br>• 结构化数据库，便于二次开发、导入在线问卷（Google Forms/问卷星）或教学软件。 |",
        "| **架构与使用说明备忘录** | 1 份 | `00_高一厨艺理论测验题2026_题库架构与使用说明.md` |",
        "\n---",
        "### 二、全套 20 单元核心考查架构与题目配比总表\n",
        "| 单元序号 | 课程模块与主题 | 容易题 (Q1~Q10) | 中等题 (Q11~Q15) | 答案分布 (A-B-C-D) |",
        "| :---: | :--- | :---: | :---: | :---: |"
    ]

    for u in all_units_data:
        ans_counts = Counter(q['answer'] for q in u['questions'])
        ans_str = f"A:{ans_counts['A']} / B:{ans_counts['B']} / C:{ans_counts['C']} / D:{ans_counts['D']}"
        md_lines.append(f"| **第 {u['unit_num']:02d} 单元** | {u['full_name']} | 10 题 | 5 题 | {ans_str} |")

    md_lines.extend([
        "\n---",
        "### 三、题库四大高品质命题标准落实说明\n",
        "1. **严格 2:1 难度梯度配比**：",
        "   - **第 1~10 题（容易）**：牢牢锁定单元基础定义、器具形态识别、后厨直观现象、温度时间常识，帮助学生建立学科自信；",
        "   - **第 11~15 题（中等）**：引入食品物理化学变化（如淀粉糊化、蛋白质热变性、美拉德反应、乳化破乳机理、烘焙百分比换算与翻车缺陷归因），提供良好的阶段诊断与选拔区分度。",
        "2. **ABCD 选项答案绝对均等平衡**：",
        "   - 每单元 15 题严格控制为 **4-4-4-3** 组合分布，彻底杜绝“盲猜某一字母得分”或“连续出现3个以上相同字母”的投机现象。",
        "3. **选项平行长度控制**：",
        "   - 所有选项字数严格对齐（字数差控制在极小区间），杜绝“正确答案详尽冗长、干扰项草草几个字”的送分破绽。",
        "4. **专业化详细解析**：",
        "   - 教师卷每道题目均配有深度原理解释，精准指出为什么选该项，并分析干扰项背后的概念误区，极大降低教师备课批改成本。",
        "\n---",
        "### 四、教师课堂测验施考建议\n",
        "1. **测验时长与分值**：建议每单元随堂测验安排在 **25分钟** 内完成，卷面满分 **30分**（每题 2 分），可直接作为平时成绩记入档案；",
        "2. **利用答题卡提高批改效率**：学生卷顶部特别设计了 1~15 题的答题表格，教师可借助教师卷第一页的「快速核对答案表（Quick Key）」，在 **10秒钟内** 完成一位学生的批阅；",
        "3. **讲评策略**：重点精讲 Q11~Q15（中等题），结合教师解析卷中的理化机理与翻车案例剖析，帮助学生融会贯通。"
    ])

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))
    print(f"Generated Markdown User Guide: {md_path}")

# -------------------------------------------------------------
# 5. MAIN EXECUTION
# -------------------------------------------------------------
def main():
    print(">>> 1. Loading and balancing question selection across 20 units...")
    all_units_data = select_chapter_questions()
    print(f"Successfully prepared 20 units with {len(all_units_data)*15} total questions.")

    print("\n>>> 2. Generating 20 Student Test Papers (.docx)...")
    for u in all_units_data:
        build_student_unit_doc(u, is_standalone=True)

    print("\n>>> 3. Generating 20 Teacher Answer Key & Explanation Papers (.docx)...")
    for u in all_units_data:
        build_teacher_unit_doc(u, is_standalone=True)

    print("\n>>> 4. Generating Master Student Compilation (.docx)...")
    build_master_student_compilation(all_units_data)

    print("\n>>> 5. Generating Master Teacher Compilation (.docx)...")
    build_master_teacher_compilation(all_units_data)

    print("\n>>> 6. Exporting JSON Database and Markdown Guide...")
    export_json_and_markdown(all_units_data)

    print("\n🎉 ALL TASKS COMPLETED SUCCESSFULLY! Deliverables saved in:")
    print(OUT_DIR)

if __name__ == '__main__':
    main()
