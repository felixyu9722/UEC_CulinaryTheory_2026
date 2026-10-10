# -*- coding: utf-8 -*-
"""
build_doc2_senior2_western.py
Generates Document 2:
统考历届真题分类拆分汇编 —— 高二：西餐烹调理论与实务 (2020-2025年)
"""

import sys, os
sys.stdout.reconfigure(encoding='utf-8')

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx_helper import create_styled_document, set_cell_background, set_cell_margins, set_table_borders

TARGET_DIR = r'统考历届考题拆分与高一测验卷_Word'
os.makedirs(TARGET_DIR, exist_ok=True)
OUT_PATH = os.path.join(TARGET_DIR, '02_统考历届真题分类拆分_高二西餐烹调理论与实务(2020-2025).docx')

doc = create_styled_document()

# ── Title & Meta ──
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("马来西亚华文独中统一考试（UEC）厨艺理论与实务\n历届真题分类拆分与考点深度剖析")
run_title.font.size = Pt(18)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(120, 53, 15)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run("【高二阶段专属】西餐烹调理论与实务（2020～2025 年真题全收录）")
run_sub.font.size = Pt(14)
run_sub.font.bold = True
run_sub.font.color.rgb = RGBColor(180, 83, 9)

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_meta = p_meta.add_run("适用对象：高二餐饮班师生、统考专题冲刺复习 | 题型：单选题 · 罗马组合题 · 作答分析题")
run_meta.font.size = Pt(9.5)
run_meta.font.italic = True
run_meta.font.color.rgb = RGBColor(100, 116, 139)

doc.add_paragraph() # Spacer

# ── Part 1: Blueprint & Matrix ──
h1 = doc.add_heading("第一部分：高二西餐理论在独中统考中的权重与考点矩阵", level=1)
h1.style.font.color.rgb = RGBColor(120, 53, 15)

p_intro = doc.add_paragraph(
    "高二学年的【西餐烹调理论与实务】在统考中占有鲜明独立的考查地位。在试卷一（选择题）中，固定作为【乙组：西餐烹调艺术及实践】（Q41～Q50，共 10 题，占 10 分）；"
    "在试卷二（作答题）中，每年均有 1～2 道核心大题（占 10～20 分）围绕西餐出题。统考总权重约占 20%～30%。"
    "考题特点极其强调【法式厨房古典分工术语】、【西式五大母酱】、【热处理烹调温度】与【牛肉及禽类部位分割】。"
)

# Table: Blueprint Matrix
table_matrix = doc.add_table(rows=1, cols=4)
table_matrix.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["知识板块 (高二15单元体系)", "统考历届高频题型", "每年平均分值", "核心考察要点与命题规律"]
hdr_cells = table_matrix.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    set_cell_background(hdr_cells[i], "FEF3C7")
    set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
    for p in hdr_cells[i].paragraphs:
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = RGBColor(120, 53, 15)

matrix_data = [
    ("西餐厨房组织架构与法语岗位职能", "单选题、专有名词解释", "3～4 分", "Chef de Cuisine (行政总厨), Sous Chef (副主厨), Saucier (少司厨师), Pâtissier (糕点师), Garde-Manger (冷菜厨师), Poissonier (鱼类厨师)"),
    ("西式刀具应用与砧板卫生色标", "单选题、作答题", "4～6 分", "去骨刀 (Boning Knife), 厨刀, 面包锯刀；蓝红绿白四色砧板用途区分；三槽洗法与食品卫生准则"),
    ("食物热处理烹调技法与精准温度", "单选、作答问答题", "6～8 分", "湿热烹调 (Poaching 71~82℃, Simmering 85~96℃, Steaming 100℃)；干热烹调 (Roasting, Pan-fry)；复合烹调 (Braising, Stewing)；真空低温慢煮 Sous-Vide"),
    ("西式基础高汤与法式五大母酱", "单选、配对填空大题", "6～8 分", "白高汤、褐高汤、香料包 (Bouquet Garni)；澄清汤 (Consommé) 蛋清吸附原理；五大母酱：Béchamel, Velouté, Espagnole, Tomato, Hollandaise 及其对应 Roux"),
    ("红肉、家禽与海鲜部位及烹调适性", "单选、看图填部位大题", "6～10 分", "牛肉部位：Tenderloin (菲力), Sirloin (西冷), Ribeye (肋眼), Flank (牛腩)；家禽熟度与沙门氏菌预防；鱼类鲜度判定与三道裹粉法 (Breaded)")
]

for row_data in matrix_data:
    row = table_matrix.add_row()
    for i, val in enumerate(row_data):
        cell = row.cells[i]
        cell.text = val
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        for p in cell.paragraphs:
            p.runs[0].font.size = Pt(9)
            p.runs[0].font.color.rgb = RGBColor(51, 65, 85)

set_table_borders(table_matrix)
doc.add_paragraph() # Spacer

# ── Part 2: Categorized MCQs with Solutions ──
h2 = doc.add_heading("第二部分：2020～2025年统考历届高二西餐选择题分类精选汇编", level=1)
h2.style.font.color.rgb = RGBColor(120, 53, 15)

western_mcqs = [
    {
        "unit": "模块一：西餐厨房组织架构与专业术语",
        "items": [
            {
                "id": "2025-Q1",
                "q": "【2025年统考真题】在传统法式餐厅厨房职务编制中，专门负责制作各式糕点、面包与甜品的餐饮专业从业人员，法文称为什么？",
                "opts": ["A. Saucier", "B. Pâtissier", "C. Poissonier", "D. Chef Garde-Manger"],
                "ans": "B",
                "exp": "法式传统厨房岗位：Pâtissier（西点/糕点主厨）；Saucier（沙司/少司厨师，负责热前菜、酱汁及肉类，通常是后厨地位仅次于副主厨的核心岗位）；Poissonier（鱼类专门厨师）；Chef Garde-Manger（冷菜房主厨，负责冷盘、沙拉及肉酱）。"
            },
            {
                "id": "2025-Q43",
                "q": "【2025年统考真题】下列哪一种香草植物在欧洲古代被推崇为“胜利与荣耀的象征”，同时也是经典法式香料束（Bouquet Garni）中不可或缺的主材？",
                "opts": ["A. 迷迭香 (Rosemary)", "B. 罗勒 (Basil)", "C. 月桂叶 (Bay Leaf / Laurel)", "D. 鼠尾草 (Sage)"],
                "ans": "C",
                "exp": "月桂（Laurel）自古希腊与罗马时期起即被编织为月桂花环冠冕以象征“胜利、荣耀与桂冠”。在法式烹饪中，月桂叶带有清新草木微香，是香料束（Bouquet Garni）的核心主角，通常与百里香（Thyme）、欧芹茎（Parsley Stems）捆扎熬制高汤。"
            },
            {
                "id": "2021-Q41",
                "q": "【2021年统考真题】在法式西餐后厨管理中，常提及的工作核心术语「Mise en Place」其本义指的是什么？",
                "opts": ["A. 每日营业结束后的全场彻底消杀清洁", "B. 严格控制每道菜肴的食材克数与出品毛利率", "C. 一切准备就绪——在正式烹调出单前将所有工器具与食材预先处理定位", "D. 仅指主厨对新晋员工的现场烹饪考核"],
                "ans": "C",
                "exp": "Mise en Place（法语：就位/各就各位）：指厨师在出餐开始前，将所有必需的调料、切配好的食材、酱汁、量具与烹饪刀具等完全备齐并放置于专属操作工位，以保障高压出餐过程行云流水、不出纰漏。"
            }
        ]
    },
    {
        "unit": "模块二：西式高汤、五大母酱与清汤澄清",
        "items": [
            {
                "id": "2024-Q42",
                "q": "【2024年统考真题】在法式经典料理体系中，下列哪一个“母酱（Mother Sauce）”是由“白高汤 (White Stock) ＋ 白面糊 (White Roux)”的标准组合调制而成？",
                "opts": ["A. 荷兰酱 (Hollandaise Sauce)", "B. 白汁母酱 (Béchamel Sauce)", "C. 天鹅绒母酱 (Velouté Sauce)", "D. 褐色母酱 (Espagnole Sauce)"],
                "ans": "C",
                "exp": "法式五大母酱配方：①Velouté（天鹅绒白酱）= 白高汤（鸡/鱼/小牛骨高汤）+ White/Blond Roux；②Béchamel（白汁少司）= 牛奶 + White Roux；③Espagnole（褐色母酱）= 褐色小牛高汤 + Brown Roux；④Hollandaise（荷兰酱）= 蛋黄 + 澄清黄油乳化；⑤Tomato（番茄少司）。"
            },
            {
                "id": "2023-Q42",
                "q": "【2023年统考真题 · 罗马组合题】制作顶级法式澄清汤（Consommé）时，下列关于汤体澄清原理与操作要点的叙述，何者完全正确？\n"
                       "   I. 必须在冷高汤中加入富含白蛋白的生蛋清与碎瘦肉末搅拌\n"
                       "   II. 缓慢升温过程中，蛋清变性凝固形成浮渣滤网（Raft）以吸附微细悬浮微粒\n"
                       "   III. 汤汁一旦沸腾必须立即加盖并用大火猛烈翻滚以加速沉淀\n"
                       "   IV. 必须开小孔微沸慢熬，绝对不可搅拌破坏表层蛋清滤网",
                "opts": ["A. I, II, IV", "B. I, II, III", "C. II, III, IV", "D. I, III, IV"],
                "ans": "A",
                "exp": "法式澄清汤（Consommé）：利用冷高汤起步，蛋清受热在约62℃开始变性浮聚成浮筏（Raft），吸附杂质使汤色清澈如琥珀茶汤。微沸时必须保持小火轻微冒泡，严禁大火翻滚或搅拌，大火会冲碎蛋清网导致汤体永远浑浊。III错误，故选 A。"
            },
            {
                "id": "2022-Q45",
                "q": "【2022年统考真题】经典中欧名菜匈牙利牛肉汤（Hungarian Goulash Soup）在热气腾腾供餐出盘时，传统上最常搭配并浮于汤面作为装饰增味的是哪一种乳制品？",
                "opts": ["A. 酸奶油 (Sour Cream)", "B. 帕玛森硬芝士碎 (Parmesan)", "C. 纯鲜牛奶 (Whole Milk)", "D. 融化的马苏里拉奶酪 (Mozzarella)"],
                "ans": "A",
                "exp": "匈牙利牛肉汤（Goulash / Gulyás）富含红椒粉（Paprika）、番茄与炖牛肉的微辣浓郁滋味，出餐时在正中央舀入一勺冰凉微酸的酸奶油（Sour Cream），红白相映，冷热交融，能极大柔和辛香料的刺激，提升醇厚回甘。"
            }
        ]
    },
    {
        "unit": "模块三：肉类家禽、海鲜分割与刀工器具",
        "items": [
            {
                "id": "2020-Q45",
                "q": "【2020年统考真题】在西餐厨房生鲜原料处理中，专门用来沿骨缝剔除家禽或红肉中骨骼的专业刀具是：",
                "opts": ["A. 厨师主厨刀 (Chef's Knife)", "B. 西式剔骨刀 (Boning Knife)", "C. 锯齿面包刀 (Bread Knife)", "D. 西式片肉刀 (Carving Knife)"],
                "ans": "B",
                "exp": "剔骨刀（Boning Knife）刀身细窄、坚韧（有软刃与硬刃之分），刀尖尖锐，能极其灵活地紧贴骨骼肌理进行游走切割，最大程度剔净骨上残肉且不伤骨髓。"
            },
            {
                "id": "2020-Q44",
                "q": "【2020年统考真题】野生大西洋鲑鱼（Salmon）在自然生长周期中，通常长至生长发育的哪一个阶段或年份时，其肌间脂肪丰美、肉质最鲜嫩？",
                "opts": ["A. 二至三年", "B. 四至五年", "C. 六至七年", "D. 八年以上"],
                "ans": "A",
                "exp": "鲑鱼通常在海洋中生长 2～3 年达到性成熟前体格健壮、洄游蓄积了最丰沛的鱼油与Omega-3脂肪酸，此时捕捞肉质最为细嫩鲜红且无衰老土腥味。"
            },
            {
                "id": "2024-Q45",
                "q": "【2024年统考真题】关于西餐牛排部位「菲力（Tenderloin）」的肌纤维特点，下列叙述何者最为准确？",
                "opts": ["A. 属于腹部常运动肌肉，筋膜厚硬，必须长时间文火红酒煨炖", "B. 位于脊椎内侧运动极少，肌纤维最纤细嫩柔、脂肪含量极低，最宜高温快煎快烤", "C. 拥有粗大的大理石花纹雪花油脂，适合长时间烟熏烧烤", "D. 骨胶原蛋白含量全牛最高，仅适合慢熬浓汤"],
                "ans": "B",
                "exp": "Tenderloin（腰内肉/里脊/菲力）：位于牛腰部脊椎下方内侧，几乎不参与行走支撑，因此肌纤维最细嫩、结缔组织极少，是全牛最嫩的部位。适宜三分熟（Medium Rare）至五分熟快煎，切忌久煮或长时间炖煮，久煮会干柴流失汁水。"
            }
        ]
    }
]

for section in western_mcqs:
    h_sec = doc.add_heading(section["unit"], level=2)
    h_sec.style.font.color.rgb = RGBColor(180, 83, 9)
    
    for item in section["items"]:
        p_q = doc.add_paragraph()
        run_qid = p_q.add_run(f"{item['id']} ")
        run_qid.bold = True
        run_qid.font.color.rgb = RGBColor(120, 53, 15)
        run_qtext = p_q.add_run(item["q"])
        run_qtext.bold = True
        
        for opt in item["opts"]:
            p_opt = doc.add_paragraph(opt)
            p_opt.paragraph_format.left_indent = Inches(0.25)
            p_opt.paragraph_format.space_after = Pt(2)
        
        tbl_exp = doc.add_table(rows=1, cols=1)
        tbl_exp.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_exp = tbl_exp.rows[0].cells[0]
        set_cell_background(c_exp, "F8FAFC")
        set_cell_margins(c_exp, top=80, bottom=80, left=120, right=120)
        
        p_ans = c_exp.paragraphs[0]
        r_ans = p_ans.add_run(f"【标准答案】：{item['ans']}      ")
        r_ans.bold = True
        r_ans.font.color.rgb = RGBColor(16, 185, 129)
        
        r_exp_title = p_ans.add_run("【考点深入解析】：\n")
        r_exp_title.bold = True
        r_exp_title.font.color.rgb = RGBColor(71, 85, 105)
        
        r_exp_body = p_ans.add_run(item["exp"])
        r_exp_body.font.size = Pt(9.5)
        r_exp_body.font.color.rgb = RGBColor(51, 65, 85)
        
        set_table_borders(tbl_exp, color="CBD5E1")
        doc.add_paragraph() # Spacer

# ── Part 3: Written Questions (Paper 2) ──
h3 = doc.add_heading("第三部分：2020～2025年统考历届高二西餐作答题精选与评分细则", level=1)
h3.style.font.color.rgb = RGBColor(120, 53, 15)

western_written = [
    {
        "year": "2025 年统考大题 (试卷二选答题 · 10%)",
        "title": "西式牛肉部位解剖图与烹调技法综合分析",
        "desc": "题目要求：试写出西餐厨房常见以下 5 个牛肉部位的标准中文名称及英语/法语名称，并指明其最适合的高温快煮或低温慢炖烹调法：\n"
                "(1) Tenderloin; (2) Sirloin; (3) Ribeye; (4) Brisket; (5) Shank。",
        "rubric": "【标准答案与采分细则】：(共10分，每项2分)\n"
                  "① Tenderloin (牛里脊/菲力)：全牛最嫩、无筋膜无韧带，最适宜：快速煎 (Pan-Fry)、铁板烧烤 (Grill) 至 Medium Rare。(2分)\n"
                  "② Sirloin (西冷/沙朗/腰脊肉)：外缘带有一圈标志性白色油筋，肉质扎实肉香浓郁，最适宜：高温炭烤 (Broil)、香煎牛排。(2分)\n"
                  "③ Ribeye (肋眼/肉眼牛排)：中心有明显的油脂油眼，大理石花纹油花丰富多汁，最适宜：平底铁锅高温煎烤。(2分)\n"
                  "④ Brisket (牛前胸肉/牛胸肉)：结缔组织结实坚韧，富含胶原蛋白，最适宜：长时间低温慢烤 (BBQ Smoked) 或红酒慢炖 (Stewing)。(2分)\n"
                  "⑤ Shank (牛腱/牛小腿肉)：肌腱密布、活动量巨大，最适宜：慢炖 (Braising) 或熬制浓厚牛骨清汤 (如意式慢炖牛膝 Osso Buco)。(2分)"
    },
    {
        "year": "2024 年统考大题 (试卷二选答题 · 10%)",
        "title": "西餐湿热烹调法（Moist-Heat Cooking）标准温度与适用食材",
        "desc": "不同的烹调方法会显著影响菜肴的最终成色与质感。试回答以下 4 个西餐湿热烹调法的规范温度及适用食材要求：\n"
                "(a) 水波煮 (Poaching) 的烹调水温约为摄氏几度？最适合烹调何种食材？(3分)\n"
                "(b) 文火慢煮 (Simmering) 的烹调温度约为摄氏几度？(2分)\n"
                "(c) 蒸气烹调 (Steaming) 的温度约为摄氏几度？有何优势？(3分)\n"
                "(d) 滚水沸煮 (Boiling) 的温度为几度？(2分)",
        "rubric": "【标准答案与采分细则】：(共10分)\n"
                  "(a) Poaching (水波煮)：温度严格控制在 71℃～82℃ 之间（水面只有微小细浪，绝不沸腾冒大泡）。最适食材：去壳水波蛋（班尼迪克蛋）、极其娇嫩的深海鱼柳或贝类。（3分）\n"
                  "(b) Simmering (文火慢煮)：温度在 85℃～96℃ 之间（水底缓慢间歇性产生微小气泡）。用于慢熬高汤、浓汤及大块根茎蔬菜。（2分）\n"
                  "(c) Steaming (蒸气烹)：标准常压饱和蒸气温度为 100℃。核心优势：食材不浸泡于水中，水溶性维生素、矿物质及鲜味成分流失最少，成品质地鲜嫩清爽。（3分）\n"
                  "(d) Boiling (沸腾煮)：标准常压沸水温度为 100℃（水面翻滚剧烈）。用于汆煮意大利面（Pasta）或硬质蔬菜去皮。（2分）"
    },
    {
        "year": "2022 年统考大题 (试卷二选答题 · 10%)",
        "title": "西餐后厨砧板颜色卫生标示与废弃物分类管理",
        "desc": "问题 (a)：现代化西餐厨房为防止交叉污染，切配案板（砧板）采用严格的颜色区分管理。试详细写出【蓝色】、【红色】、【绿色】及【白色】砧板的法定专职用途。(4分)\n"
                "问题 (b)：西餐后厨废弃物处理区可分为“液态垃圾”与“固态垃圾”。试说明两者的收集处理流程与隔油池（Grease Trap）的功能。(6分)",
        "rubric": "【标准答案与采分细则】：(共10分)\n"
                  "问题 (a) 解答：(4分，每色1分)\n"
                  "  • 蓝色砧板：专用于切配【生海鲜水产与生鱼类】（Raw Seafood/Fish）。\n"
                  "  • 红色砧板：专用于切配【生红肉类】（牛、羊、猪生肉 Raw Red Meat）。\n"
                  "  • 绿色砧板：专用于切配【蔬菜、水果与沙拉新鲜沙拉生食】（Produce & Salad）。\n"
                  "  • 白色砧板：专用于切配【即食熟食、乳酪奶酪、面包及熟肉】（Dairy, Cooked Food & Bakery）。\n"
                  "问题 (b) 解答：(6分)\n"
                  "  • 废弃物管理：固态垃圾入带盖脚踏垃圾桶，内衬厚塑料袋，每日定时清理封口；液态含油污水必须排入专用沉淀隔油池（Grease Trap）。（3分）\n"
                  "  • 隔油池功能：利用油与水比重不同的物理原理，将冲洗餐具产生的油脂阻隔在上浮层，防止凝固油脂堵塞公共下水管道并防止环境重度污染。（3分）"
    },
    {
        "year": "2020 年统考大题 (试卷二必答题 · 10%)",
        "title": "西式裹粉炸制食物（Breaded / Standard Breading）三道挂衣程序",
        "desc": "试详细列出西餐中对肉排或海鲜进行标准粉炸（Breaded）的三道裹衣标准程序及其各自的核心技术目的。(10分)",
        "rubric": "【标准答案与采分细则】：(共10分)\n"
                  "标准裹粉裹衣程序（Standard Breading Procedure，按由左至右流水线布置）：\n"
                  "① 第一道工序：裹拍面粉（All-purpose Flour）。(3分)\n"
                  "   目的：吸收食材（如鸡排、猪排、鱼排）表面的多余游离水分，提供微干燥黏着层，并防止下一步蛋液滑脱流失；拍去多余干粉保持轻薄。\n"
                  "② 第二道工序：浸沾全蛋液或蛋奶混合液（Egg Wash）。(3分)\n"
                  "   目的：提供强大的湿性液体胶水结合层，紧密贴附内层干粉并粘住外层面包糠，同时受热凝固提供金黄底色。\n"
                  "③ 第三道工序：滚压面包糠或干面包屑（Breadcrumbs / Panko）。(4分)\n"
                  "   目的：形成均匀完整、致密酥脆的防护外壳。在高温油炸时水分瞬间向外蒸发形成无数硬脆多孔气室，锁住肉汁不外溢，赋予金黄诱人的嘎吱酥脆外衣。"
    }
]

for w in western_written:
    p_yr = doc.add_paragraph()
    r_yr = p_yr.add_run(f"📅 {w['year']} —— {w['title']}")
    r_yr.bold = True
    r_yr.font.size = Pt(11)
    r_yr.font.color.rgb = RGBColor(120, 53, 15)
    
    p_desc = doc.add_paragraph(w['desc'])
    p_desc.paragraph_format.left_indent = Inches(0.2)
    
    p_rub = doc.add_paragraph()
    p_rub.paragraph_format.left_indent = Inches(0.2)
    p_rub.paragraph_format.space_after = Pt(12)
    r_rub = p_rub.add_run(w['rubric'])
    r_rub.font.size = Pt(9.5)
    r_rub.font.color.rgb = RGBColor(71, 85, 105)

# Save Document
doc.save(OUT_PATH)
print(f"Generated Document 2: {OUT_PATH} ({os.path.getsize(OUT_PATH)} bytes)")
