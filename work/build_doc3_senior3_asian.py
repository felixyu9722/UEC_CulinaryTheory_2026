# -*- coding: utf-8 -*-
"""
build_doc3_senior3_asian.py
Generates Document 3:
统考历届真题分类拆分汇编 —— 高三：亚洲及中餐烹调理论、餐饮管理与食品安全 (2020-2025年)
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
OUT_PATH = os.path.join(TARGET_DIR, '03_统考历届真题分类拆分_高三中餐理论与餐饮管理(2020-2025).docx')

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
run_sub = p_sub.add_run("【高三阶段专属】亚洲及中餐烹调理论、餐饮管理与食品安全（2020～2025 年真题全收录）")
run_sub.font.size = Pt(14)
run_sub.font.bold = True
run_sub.font.color.rgb = RGBColor(180, 83, 9)

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_meta = p_meta.add_run("适用对象：高三毕业班师生、统考全真冲刺与备考拔高 | 题型：单选题 · 罗马组合题 · 作答阐述题")
run_meta.font.size = Pt(9.5)
run_meta.font.italic = True
run_meta.font.color.rgb = RGBColor(100, 116, 139)

doc.add_paragraph() # Spacer

# ── Part 1: Blueprint & Matrix ──
h1 = doc.add_heading("第一部分：高三中餐与管理理论在独中统考中的权重与考点矩阵", level=1)
h1.style.font.color.rgb = RGBColor(120, 53, 15)

p_intro = doc.add_paragraph(
    "高三阶段的课程由【亚洲及中餐烹调艺术】、【餐饮成本与运营管理】以及【食品安全与HACCP高阶规范】构成。"
    "在统考历届试卷一中，固定作为【丙组：亚洲烹调艺术及实践】（Q51～Q60，共 10 题，占 10 分）；"
    "在试卷二（作答题）中，【甲组：必答题】（占 10 分）经常以中餐调味料、烹调基本功或世界菜系为核心出题，选答题中亦常占 10 分。统考整体权重约为 25%～35%。"
    "考题特点极其强调【传统刀工规格级差】、【中餐24种烹调技法原理】、【中国八大菜系与名菜】、【马来西亚本土风味料理】以及【餐饮卫生杀菌法定要求】。"
)

# Table: Blueprint Matrix
table_matrix = doc.add_table(rows=1, cols=4)
table_matrix.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["知识板块 (高三8单元体系)", "统考历届高频题型", "每年平均分值", "核心考察要点与命题规律"]
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
    ("中餐传统刀工刀法与几何规格级差", "单选题、配对大题", "4～6 分", "直切、平刀片、斜刀批；丝（细于条）、丁（大于粒）、粒（大于末）、末（粗于茸）；刀花雕刻与盘饰保存"),
    ("中餐火候、挂糊上浆与核心烹调技法", "单选、工艺对比作答题", "6～8 分", "滑油（三至四成温油划散上浆原料锁水）；挂糊（厚浆炸熘） vs 上浆（薄浆滑炒水汆）；炒爆熘炸烹煎贴烧焖煨炖蒸等24法；白烧 vs 红烧"),
    ("中国八大菜系与历史名肴典故", "单选题、代表作配对题", "5～7 分", "鲁菜（咸鲜浓油、葱烧）、川菜（七滋八味麻辣复合）、粤菜（原汁原味清鲜）、苏菜（甜香淮扬刀工）、浙菜（东坡肉文火慢焖）、闽菜（佛跳墙隔水蒸煨）"),
    ("亚洲与马来西亚本土风味料理", "单选题、问答题", "4～5 分", "马来西亚四大叻沙（亚参叻沙鱼汤罗望子酸辣 vs 咖喱叻沙椰奶金黄）；椰浆饭、沙爹花生酱、香辛料配搭"),
    ("调味品生化、餐饮卫生与HACCP管理", "单选、试卷二必答大题", "8～12 分", "酱油发酵与鲜味谷氨酸；白胡椒粉与酸辣汤；五大调味品（盐糖酒醋酱）作用；铁氟龙锅禁用铁铲；食品煮沸消毒（100℃≥1分钟）；HACCP控制点")
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
h2 = doc.add_heading("第二部分：2020～2025年统考历届高三中餐与管理选择题分类精选汇编", level=1)
h2.style.font.color.rgb = RGBColor(120, 53, 15)

asian_mcqs = [
    {
        "unit": "模块一：中餐刀工刀法与几何规格比较",
        "items": [
            {
                "id": "2024-Q52",
                "q": "【2024年统考真题】下列关于中餐切配刀工形态规格大小比较的叙述，何者完全正确？",
                "opts": ["A. “丝”比“条”细", "B. “丁”比“粒”小", "C. “末”比“茸”细", "D. “粒”比“末”小"],
                "ans": "A",
                "exp": "中餐刀工形态严格规格级差：①条与丝：丝（直剖面约0.2cm）比条（直剖面约0.5cm）细；②丁、粒、末、茸：丁（1~1.5cm） > 粒（0.5cm） > 末（0.2cm左右碎颗粒） > 茸（泥状/细糊状，比末更细致细腻）。故只有 A 完全正确。"
            },
            {
                "id": "2020-Q52",
                "q": "【2020年统考真题】制作宴席冷拼盘饰所用过的胡萝卜、黄瓜等雕刻盘饰材料，若想留存至隔天再次使用，应当采取哪种规范处置？",
                "opts": ["A. 直接长时间浸泡于纯清水中即可", "B. 沥干水分密封包装后置于冰箱冷藏（2～7℃）保存", "C. 必须放入冷冻库速冻结冰", "D. 放置于常温通风案台上自然晾干"],
                "ans": "B",
                "exp": "已雕刻的植物盘饰直接泡水会导致水溶性养分流失且蔬菜发胀变色腐烂；长期冷冻会导致植物细胞壁破裂化水变软失去立体造型；正确的保鲜规范是表面喷少许清水保持湿润，装入保鲜盒或密封袋，置于2~7℃冷藏室保存。"
            }
        ]
    },
    {
        "unit": "模块二：中餐烹调技法、火候与上浆挂糊",
        "items": [
            {
                "id": "2023-Q52",
                "q": "【2023年统考真题】传统中餐“白烧”与“红烧”的最本质烹调区别在于，白烧在调味时主要依靠下列哪项组合，绝不添加具有深色着色作用的酱油或糖色？",
                "opts": ["A. 精盐、料酒与高汤", "B. 蚝油与豆瓣酱", "C. 甜面酱与红曲米", "D. 香油与黑胡椒"],
                "ans": "A",
                "exp": "中餐烧菜分为红烧与白烧：红烧加入酱油、冰糖或焦糖糖色，成品红亮赤酱；白烧（如白烧蹄筋、白烧鳜鱼）要求成菜色泽清白、原汁原味，调味仅使用精盐、绍兴黄酒、高汤、白胡椒粉等无色或浅色调料，绝不使用酱油或深色酱料。"
            },
            {
                "id": "2023-Q53",
                "q": "【2023年统考真题】经典中餐名汤“传统酸辣汤”中鲜明醇厚的“辣味”，其传统正统的辣味主要来源是：",
                "opts": ["A. 红油朝天椒末", "B. 研磨纯白胡椒粉 (White Pepper)", "C. 郫县麻辣豆瓣酱", "D. 泰国指天椒丁"],
                "ans": "B",
                "exp": "正宗北方与淮扬酸辣汤讲究“酸而不烈，辣而不燥”。其酸味来自镇江香醋（出锅前沿锅边淋入避免醋酸过度挥发），辣味则纯粹依靠优质白胡椒粉（White Pepper）的辛辣芳香，而非红辣椒的辣油，口感温热通窍、回味悠长。"
            },
            {
                "id": "2021-Q52",
                "q": "【2021年统考真题】烹饪使用涂有聚四氟乙烯（铁氟龙 Teflon）的不粘涂层炒锅时，为保护涂层不被刮伤脱落，最适宜选用的翻炒器具是：",
                "opts": ["A. 尖锐铁铲", "B. 耐热木制铲或耐热硅胶铲", "C. 不锈钢炒勺", "D. 铸铁分菜铲"],
                "ans": "B",
                "exp": "铁氟龙不粘涂层质地较为娇贵，使用坚硬、边缘锋利的金属铲（铁铲、不锈钢铲、金属勺）在高温翻炒刮擦下极易划伤涂层导致脱落混入食物，因此必须选用边缘圆润柔和的耐热木质锅铲或食品级耐热硅胶铲。"
            }
        ]
    },
    {
        "unit": "模块三：八大菜系、亚洲料理与食品卫生管理",
        "items": [
            {
                "id": "2025-Q56",
                "q": "【2025年统考真题】马来西亚多元美食体系中，槟城地标名面「亚参叻沙（Asam Laksa）」最具辨识度的风味与汤底特征是？",
                "opts": ["A. 以大量鲜椰浆为主体，色泽金黄微甜带有咖喱香", "B. 以鲜鱼（甘榜鱼/鲭鱼）熬汤加入罗望子（亚参）调酸，不加椰奶，酸辣鲜爽", "C. 以潮汕沙茶酱为底，汤汁咸浓辛香", "D. 以纯清鸡汤为底，仅用白胡椒清淡提鲜"],
                "ans": "B",
                "exp": "马来西亚叻沙主要分为两大流派：一是以咖喱椰浆为底的咖喱叻沙（Curry Laksa）；二是槟城代表的亚参叻沙（Asam Laksa），以甘榜鱼或沙丁鱼熬出浓郁鲜鱼汤，加入罗望子（Asam Jawa / Tamarind）及亚参片调酸，配叻沙叶、姜花丝与黄瓜丝，完全不含椰奶，酸辣开胃。"
            },
            {
                "id": "2021-Q37",
                "q": "【2021年统考真题】在餐饮服务食品卫生规范中，对食品接触用具与毛巾布草采用“沸水煮沸消毒法”时，法定规范要求必须在 100℃ 沸水中持续加热至少多长时间？",
                "opts": ["A. 半分钟以上", "B. 持续加热 1 分钟以上", "C. 持续加热 5 分钟以上", "D. 持续加热 10 分钟以上"],
                "ans": "B",
                "exp": "食品卫生操作规范标准：物理高温煮沸杀菌法，水必须保持完全沸腾翻滚状态（100℃），用具完全浸没，持续受热时间不得少于 1 分钟（通常规范要求1~3分钟），方可完全杀灭绝大多数营养体致病细菌及常见病毒。"
            },
            {
                "id": "2021-Q53",
                "q": "【2021年统考真题】名贵药膳滋补甜品“雪蛤膏”的主要原料雪蛤，实际上取自中国林蛙（哈士蟆）体内的哪一个解剖生理部位？",
                "opts": ["A. 雄性林蛙的脑髓组织", "B. 雌性林蛙输卵管的干燥脂肪体", "C. 林蛙皮下腹部脂肪层", "D. 林蛙的背部脊髓胶质"],
                "ans": "B",
                "exp": "雪蛤（又称蛤蟆油、哈士蟆油），是取自中国东北长白山特产雌性林蛙（Rana dybowskii）越冬休眠前体内储备营养的输卵管干燥软骨组织，富含动物胶原蛋白、多种氨基酸及微量元素，经温水充分泡发后呈晶莹剔透棉絮状。"
            }
        ]
    }
]

for section in asian_mcqs:
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
h3 = doc.add_heading("第三部分：2020～2025年统考历届高三中餐作答题精选与评分细则", level=1)
h3.style.font.color.rgb = RGBColor(120, 53, 15)

asian_written = [
    {
        "year": "2025 年统考大题 (试卷二必答题 · 10%)",
        "title": "中餐五大常用基础调味料及其烹饪物理化学作用",
        "desc": "中餐烹饪讲究“五味调和，百味生香”。试详细列出中餐厨房中最常用的五项基础调味料，并分别阐述其在烹调过程中的关键作用。(10分)",
        "rubric": "【标准答案与采分细则】：(共10分，每写出一项调料得1分，阐明其烹调作用得1分)\n"
                  "① 食盐（NaCl，百味之王）：提供基础咸味；调节蛋白质保水性；促进肉类肌原纤维蛋白溶出以便上浆抱水；具有渗透杀菌与脱水去生涩味作用。(2分)\n"
                  "② 酱油（生抽/老抽）：提供醇厚鲜味（来自大豆发酵谷氨酸）；生抽提鲜增咸，老抽赋色上色（红亮焦糖色）；赋予独特的酱香复合风味。(2分)\n"
                  "③ 烹饪料酒（黄酒/绍兴酒）：利用乙醇受热挥发带走三甲胺等腥膻物质（去腥除异）；酯类物质增加菜肴芬芳香气；促进油脂溶解渗透入味。(2分)\n"
                  "④ 食醋（香醋/米醋/陈醋）：去腥解腻；促进肉质结缔组织软化分解；保持绿色蔬菜叶绿素酸性稳定；增添爽口酸香风味。(2分)\n"
                  "⑤ 白糖或冰糖：提供甜味缓和酸咸苦辛的过度刺激（调和诸味）；在高温下发生焦糖化反应赋予菜肴诱人红亮糖色；提鲜拔萃。(2分)"
    },
    {
        "year": "2023 年统考大题 (试卷二必答题 · 10%)",
        "title": "世界三大菜系与中餐烹饪四大核心技术要素",
        "desc": "问题 (a)：联合国教科文组织与国际美食界公认的“世界三大菜系”分别指哪三大烹饪流派？(3分)\n"
                "问题 (b)：中餐烹饪工艺素有“国菜四大要素”之称，试详述这四大要素在菜品制作中的具体内涵与相互关系。(7分)",
        "rubric": "【标准答案与采分细则】：(共10分)\n"
                  "问题 (a) 解答：(3分)\n"
                  "  • 世界三大菜系：中国菜系（东方烹饪代表）、法国菜系（西方现代烹饪代表）、土耳其菜系/清真伊斯兰菜系（横跨欧亚大陆的烹饪代表）。（各1分，共3分）\n"
                  "问题 (b) 解答：(7分)\n"
                  "  ① 选料（选材与初加工）：根据菜品属性严格遴选时令、部位合宜的原材料，注重原料的鲜活、纯正与质地。（2分）\n"
                  "  ② 刀工（成型与肌理处理）：根据原料质地与烹调方法，运用直、片、斜等刀法切成均匀一致的几何形状，利于受热与入味。（2分）\n"
                  "  ③ 火候（热力与时间掌控）：精确控制大火、中火、小火、微火，掌握原料在不同油温与水温下的物理化学变化节点。（2分）\n"
                  "  ④ 调味（滋味调和）：五味调和，因材施调，掌握下料次序，使主辅料滋味融为一体、百味纷呈。（1分）"
    },
    {
        "year": "2021 年统考大题 (试卷二必答题 · 10%)",
        "title": "现代餐饮管理与食品安全专有名词深度解析",
        "desc": "试结合厨房日常生产实际，详细说明下列 4 个餐饮专业术语的完整定义与操作意义：\n"
                "(1) HACCP 体系; (2) 食品危险温度带 (Food Danger Zone); (3) 滑油 (Velveting); (4) 三槽洗涤法 (3-Sink System)。",
        "rubric": "【标准答案与采分细则】：(共10分)\n"
                  "① HACCP（危害分析与关键控制点）：(3分)\n"
                  "   国际公认的预防性食品安全管理控制系统，通过对食品生产原料采购、加工、储存、出餐全流程进行生物、化学、物理危害分析，并设立关键控制点（CCP）加以监控纠偏。\n"
                  "② 食品危险温度带（Danger Zone）：(2分)\n"
                  "   温度在 5℃～60℃ 之间，是细菌繁殖速度最快的高危温度范围。高风险食品在此区间的停留总时长必须严格控制在 2 小时以内。\n"
                  "③ 滑油（Velveting / 温油划散）：(3分)\n"
                  "   将经过上浆（淀粉+蛋清+料酒等）的嫩肉片或虾仁，投入三至四成温油（100~120℃）中迅速用筷划散至六七成熟后捞出控油。薄层淀粉在低温油中瞬间糊化封闭肉质毛孔，锁住水分与肉汁，赋予极致滑嫩质感。\n"
                  "④ 三槽洗涤法（3-Sink Dishwashing System）：(2分)\n"
                  "   商业厨房人工清洗餐具的法定三步流水槽：第一槽【温水洗涤】（加清洁剂刷洗去污） ➔ 第二槽【清水冲洗】（冲净泡沫） ➔ 第三槽【高温/化学消毒】（热水烫洗或浸泡消毒水杀菌） ➔ 自然沥干。"
    }
]

for w in asian_written:
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
print(f"Generated Document 3: {OUT_PATH} ({os.path.getsize(OUT_PATH)} bytes)")
