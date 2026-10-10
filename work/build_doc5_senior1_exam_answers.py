# -*- coding: utf-8 -*-
"""
build_doc5_senior1_exam_answers.py
Generates Document 5:
高一烘焙基础理论全真模拟测验题卷 (教师详细评分参考答案与采分细则)
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
OUT_PATH = os.path.join(TARGET_DIR, '05_高一烘焙基础理论全真模拟测验题卷(教师详细评分参考答案).docx')

doc = create_styled_document()

# ── Title & Meta ──
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("2026年度马来西亚华文独立中学高中统考备战模拟测验\n高一餐饮管理与厨艺专业 · 烘焙基础理论与实务")
run_title.font.size = Pt(16)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(120, 53, 15)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run("【教师专用参考答案 · 逐题深入考点剖析 · 统考标准评分细则】")
run_sub.font.size = Pt(13)
run_sub.font.bold = True
run_sub.font.color.rgb = RGBColor(180, 83, 9)

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_meta = p_meta.add_run("适用：备课教研、期中/期末模拟测验阅卷、中考统考冲刺评分基准 | 全卷满分：100分")
run_meta.font.size = Pt(9.5)
run_meta.font.italic = True
run_meta.font.color.rgb = RGBColor(100, 116, 139)

doc.add_paragraph() # Spacer

# ── Part 1: Quick Answer Key Table ──
h1 = doc.add_heading("第一部分：试卷一 选择题标准答案速查表 (共 30 题，每题 2 分，满分 60 分)", level=1)
h1.style.font.color.rgb = RGBColor(120, 53, 15)

# Fast lookup table: 3 rows of 10
tbl_key = doc.add_table(rows=4, cols=11)
tbl_key.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_k = ["题号"] + [f"Q{i}" for i in range(1, 11)]
for c_idx, h in enumerate(headers_k):
    c = tbl_key.rows[0].cells[c_idx]
    c.text = h
    set_cell_background(c, "FEF3C7")
    set_cell_margins(c, top=60, bottom=60, left=60, right=60)
    c.paragraphs[0].runs[0].font.bold = True
    c.paragraphs[0].runs[0].font.size = Pt(9)

answers_row1 = ["答案 (1-10)", "B", "B", "B", "B", "A", "B", "A", "B", "B", "B"]
answers_row2 = ["答案 (11-20)", "B", "D", "B", "A", "B", "B", "A", "B", "A", "B"]
answers_row3 = ["答案 (21-30)", "B", "B", "A", "B", "B", "A", "B", "A", "A", "B"]

for r_idx, r_data in enumerate([answers_row1, answers_row2, answers_row3]):
    row = tbl_key.rows[r_idx+1]
    for c_idx, val in enumerate(r_data):
        c = row.cells[c_idx]
        c.text = val
        set_cell_margins(c, top=60, bottom=60, left=60, right=60)
        p = c.paragraphs[0]
        p.runs[0].font.size = Pt(9)
        if c_idx > 0:
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(16, 185, 129) # Emerald Green

set_table_borders(tbl_key)
doc.add_paragraph() # Spacer

# ── Detailed MCQ Explanations ──
h2 = doc.add_heading("试卷一：选择题逐题考点定位与深度解析", level=2)
h2.style.font.color.rgb = RGBColor(180, 83, 9)

mcq_exps = [
    (1, "B", "考点：面粉分类。高筋面粉（含粗蛋白 11.5%～14%）、中筋面粉（9.5%～11.5%）、低筋面粉（7.0%～9.0%），蛋白质含量决定了面筋筋力与吸水量。"),
    (2, "B", "考点：烘焙百分比定义。烘焙百分比是以配方中“面粉总净重”为 100% 作为除数基准计算各材料的相对比例，便于配方放大缩小与对比。"),
    (3, "B", "考点：塔塔粉作用。蛋清偏碱性（pH 8.8~9.2），加入酸性盐塔塔粉（酒石酸氢钾）降低 pH 至微酸性，使蛋白泡沫微细强韧不易消泡，且使蛋糕洁白。"),
    (4, "B", "考点：糖的物理吸湿保润性。蜂蜜与转化糖浆富含极易吸湿的单糖（果糖和葡萄糖），保水性极强，能阻断淀粉重结晶，延缓老化。"),
    (5, "A", "考点：双效泡打粉产气机理。双效（Double-acting）指第一阶段在搅拌加入液体冷水时，低温酸性盐（酒石酸）快速反应释放部分CO₂；第二阶段进炉加热超过60℃时，高温酸性盐（焦磷酸钠或硫酸铝钠）持续产气顶起面糊。"),
    (6, "B", "考点：糖油拌和法。固态黄油具有可塑性，砂糖结晶在摩擦搅打时刮入微细空气，形成大量微气室，烘烤时受热膨胀使重奶油蛋糕组织细腻蓬松。"),
    (7, "A", "考点：自解法（Autolyse）。仅将面粉与水混合，不加酵母与盐（盐会使面筋收缩，酵母会产酸变硬），静置20~60分钟让淀粉充分水化，面筋蛋白自然交联，减少机械搅拌时间。"),
    (8, "B", "考点：盐在面包中的作用。盐强化面筋蛋白质（增强筋力防面团黏烂），同时通过高渗透压抑制酵母过快发酵，避免面团发酸。"),
    (9, "B", "考点：开酥黄油操作温度。黄油在 16℃～18℃ 时具有与冷藏面团最吻合的可塑性（Plasticity），擀压折叠时黄油不会因太硬折裂刺破面皮，也不会因太软化油流出。"),
    (10, "B", "考点：食品危险温度带。5℃～60℃为细菌繁殖最活跃区（最适繁殖温度 35℃～37℃），高风险含蛋奶食品在此温度带暴露总时长严禁超过 2 小时。"),
    (11, "B", "考点：天然可可粉特性。天然可可粉未经加碱处理，呈微酸性（pH 5.2~5.8），色泽浅红褐，必须用碱性小苏打中和，避免蛋糕发酸且能使组织变黑变松。"),
    (12, "D", "考点：海绵蛋糕收缩原因排查。掺入 10% 玉米淀粉是降低面筋筋度、增加松软化口性的常规配方手段，不会导致塌陷。A、B、C 均为严重失误。"),
    (13, "B", "考点：面筋扩展阶段检验。面筋充分扩展时形成坚韧的连续网状薄膜，手撑开能拉出半透明手套膜，戳破时破洞边缘呈光滑圆形裂口。"),
    (14, "A", "考点：油脂起酥性（Shortening Value）。油脂涂覆在面粉微粒表面，阻隔面粉与水充分结合形成连续强韧面筋，烘烤后使产品酥脆易断。"),
    (15, "B", "考点：泡芙膨胀物理原理。泡芙先经高温烫面使淀粉糊化吸收巨量水分（水合达100%以上），烘烤时大量游离水急速汽化形成高压水蒸气，顶开面糊形成巨大空洞。"),
    (16, "B", "考点：面包工序。分割滚圆后，面筋受到机械强力揉搓高度紧绷，必须静置松弛 10～15 分钟（中间发酵 / Bench Time），面筋放松后方能顺利整型成型。"),
    (17, "A", "考点：几何容积计算。长方体容积 V = 长 × 宽 × 高 = 30 × 20 × 5 = 3,000 立方公分。"),
    (18, "B", "考点：糖的粒径对饼干质感影响。细砂糖颗粒粗在搅拌中不完全溶解，烘烤留有脆硬晶体使饼干更脆；糖粉颗粒极细完全溶解，使面糊更均质，成品更松软细腻化口。"),
    (19, "A", "考点：卡士达酱凝固原理。玉米淀粉在 85℃ 左右糊化形成粘稠凝胶，同时蛋黄蛋白质在 75℃～80℃ 变性凝固，两者协同形成顺滑浓稠的卡士达凝乳。"),
    (20, "B", "考点：搅拌器选型。搅拌面包面团因筋度强韧阻力极大，必须使用钩状搅拌器（Dough Hook）；打发蛋白全蛋用球状（Wire Whip）；打发黄油面糊用桨状（Flat Beater）。"),
    (21, "B", "考点：最后发酵温湿度。发酵箱标准控制在 35℃～38℃（酵母最活跃产气温区），相对湿度 75%～85%（防止面团表皮干裂结皮结壳硬化）。"),
    (22, "B", "考点：天使蛋糕分类。天使蛋糕属乳沫类中纯蛋白类蛋糕，配方绝不添加蛋黄与油脂，完全依靠蛋清打发充入空气与淀粉凝固支撑，热量极低。"),
    (23, "A", "考点：巧克力调温科学。调温是通过精确降温回温诱导可可脂形成最稳定的第V型（β-5晶型，熔点约34℃），使成品表面光亮、折断声脆、不易泛白霜、容易脱模。"),
    (24, "B", "考点：烘焙两大褐变反应。美拉德反应（还原糖与蛋白质在130℃以上反应赋予焦香）；焦糖化反应（纯糖在160℃以上受热脱水热解赋予金黄褐色）。"),
    (25, "B", "考点：罗马题（化学膨大剂）。I（小苏打残留碱味泛黄）正确；II（碳酸氢铵挥发性好适合薄脆饼干）正确；IV（酵母为生物真菌发酵）正确；III错误（双效泡打粉进炉受热持续产气）。故选 B。"),
    (26, "A", "考点：罗马题（酵母环境）。I（温湿度）、II（盐糖渗透压）、III（pH值）均为直接调控酵母生命活性的核心因素；IV（反光折射率）毫无关联。故选 A。"),
    (27, "B", "考点：罗马题（戚风蛋糕操作）。I（工具无水无油无蛋黄）、II（蛋白中性偏干发泡）、IV（切拌翻拌手法）均正确；III错误（高速画圈久拌会造成严重消泡且面粉起筋导致死面）。故选 B。"),
    (28, "A", "考点：罗马题（油脂功能）。I（起酥性）、II（打发充气蓬松）、III（风味与润滑）均正确；IV错误（油脂是弱性柔性原料，削弱骨架而非支撑骨架）。故选 A。"),
    (29, "A", "考点：罗马题（海绵蛋糕收缩原因）。I（未震热气倒扣）、II（配方水分过高）、III（模具涂油过厚无法爬升）均是导致塌陷收缩的典型操作失误；IV（熟透中心达标）是成功要素而非失误。故选 A。"),
    (30, "B", "考点：罗马题（食品卫生规范）。I（危险温度带限2小时）、II（沸水消毒不少于1分钟）、IV（化脓伤口严禁接触即食食品防葡萄球菌）均正确；III错误（刚出炉面包热气腾腾，立即密封塑料袋会积聚大量冷凝水使表皮软烂霉变）。故选 B。")
]

for q_num, ans, exp in mcq_exps:
    p = doc.add_paragraph()
    r_n = p.add_run(f"Q{q_num:02d}. 【答案：{ans}】 ")
    r_n.bold = True
    r_n.font.color.rgb = RGBColor(16, 185, 129)
    r_e = p.add_run(exp)
    r_e.font.size = Pt(9.5)
    r_e.font.color.rgb = RGBColor(51, 65, 85)

doc.add_paragraph() # Spacer

# ── Part 2: Written Questions Rubric & Scoring Guide ──
h3 = doc.add_heading("第二部分：试卷二 作答题标准采分点与评分细则 (满分 40 分)", level=1)
h3.style.font.color.rgb = RGBColor(120, 53, 15)

# Compulsory Calculation Rubric
p_w1 = doc.add_paragraph()
r_w1_t = p_w1.add_run("甲组：必答题（第 1 题 · 烘焙百分比计算题 · 满分 10 分）")
r_w1_t.bold = True
r_w1_t.font.size = Pt(11)
r_w1_t.font.color.rgb = RGBColor(180, 83, 9)

# Standard Answer Table
tbl_ans1 = doc.add_table(rows=8, cols=4)
tbl_ans1.alignment = WD_TABLE_ALIGNMENT.CENTER
calc_ans_hdr = ["材料名称", "烘焙百分比 (%)", "标准演算式与精确重量 (g)", "采分点与得分权重"]
for i, h in enumerate(calc_ans_hdr):
    c = tbl_ans1.rows[0].cells[i]
    c.text = h
    set_cell_background(c, "FEF3C7")
    set_cell_margins(c, top=80, bottom=80, left=100, right=100)
    c.paragraphs[0].runs[0].font.bold = True
    c.paragraphs[0].runs[0].font.size = Pt(9)

ans_rows_data = [
    ("高筋面粉 (基准)", "100.0 %", "500 g  (已知作为基准 100%)", "对照基准 (不计分)"),
    ("清水", "62.0 %", "500 g × 62.0% = 310 g", "算式正确填入 310g 得 1.5 分"),
    ("细砂糖", "18.0 %", "500 g × 18.0% = 90 g", "算式正确填入 90g 得 1.5 分"),
    ("全蛋液", "12.0 %", "500 g × 12.0% = 60 g", "算式正确填入 60g 得 1.5 分"),
    ("无盐黄油", "10.0 %", "500 g × 10.0% = 50 g", "算式正确填入 50g 得 1.5 分"),
    ("耐高糖干酵母", "1.5 %", "500 g × 1.5% = 7.5 g", "算式正确填入 7.5g 得 1.5 分"),
    ("食盐", "1.2 %", "500 g × 1.2% = 6.0 g", "算式正确填入 6.0g 得 1.0 分")
]

for idx, r_data in enumerate(ans_rows_data):
    row_cells = tbl_ans1.rows[idx+1].cells
    for c_idx, val in enumerate(r_data):
        row_cells[c_idx].text = val
        set_cell_margins(row_cells[c_idx], top=70, bottom=70, left=100, right=100)
        row_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(8.5)

set_table_borders(tbl_ans1)

p_w1_sub = doc.add_paragraph("\n【总重量与总分给分要点】：\n"
                             "• 面团总重量（Total Dough Weight）计算：\n"
                             "  总重量 = 500g + 310g + 90g + 60g + 50g + 7.5g + 6.0g = 1,023.5 g（或四舍五入记为 1,024 g）。(正确计算得 1.5 分)\n"
                             "• 批改提示：考生若未列出 500g × % 的算式但填入数字完全正确，扣 1 分书写分；若面粉除数弄错为面团总重，全题重度失分。")
p_w1_sub.paragraph_format.left_indent = Inches(0.2)
p_w1_sub.runs[0].font.size = Pt(9.5)
p_w1_sub.runs[0].font.color.rgb = RGBColor(71, 85, 105)

# Optional Questions Rubrics
p_opt_head = doc.add_paragraph()
r_opth = p_opt_head.add_run("乙组：选答题详细采分细则（4 选 3，每题 10 分，共 30 分）")
r_opth.bold = True
r_opth.font.size = Pt(11)
r_opth.font.color.rgb = RGBColor(180, 83, 9)

written_rubrics = [
    {
        "q_num": "第 2 题：蛋糕三大分类体系与工艺机理分析题 (10分)",
        "content": (
            "【问题 (a) 评分细则】(满分 6 分)\n"
            "① 面糊类蛋糕（Shortened Cake）：(2分)\n"
            "   • 膨大机制：主要依靠固体油脂（黄油/起酥油）与细砂糖在打发过程中裹入微细空气，并常辅以化学膨大剂（泡打粉/小苏打）在受热时释放气体共同膨胀。(1分)\n"
            "   • 代表蛋糕：磅蛋糕（Pound Cake）、重奶油蛋糕（Butter Cake）、水果蛋糕。(写出任意一种得1分)\n"
            "② 乳沫类蛋糕（Foam Cake）：(2分)\n"
            "   • 膨大机制：主要依靠大量鸡蛋的蛋白质（全蛋或纯蛋白）经过机械高速搅打形成坚韧的泡沫网络，烘烤时气泡内空气膨胀并锁住结构，完全不含或含极少量油脂。(1分)\n"
            "   • 代表蛋糕：海绵蛋糕（Sponge Cake）、天使蛋糕（Angel Food Cake）。(写出任意一种得1分)\n"
            "③ 戚风类蛋糕（Chiffon Cake）：(2分)\n"
            "   • 膨大机制：综合了面糊类与乳沫类的特长。采用分蛋打发法，蛋清单独加糖打发成强韧蛋白霜作为主体膨大动力，蛋黄与液体植物油、液体原料调成面糊，两者切拌结合。(1分)\n"
            "   • 代表蛋糕：香草戚风蛋糕、斑兰戚风蛋糕、瑞士卷蛋糕胚。(写出任意一种得1分)\n\n"
            "【问题 (b) 评分细则】(满分 4 分)\n"
            "• 塔塔粉的作用：(2分) 塔塔粉为酸性盐（酒石酸氢钾）。蛋清呈碱性，加入塔塔粉调节蛋白溶液 pH 接近微酸性（等电点），使蛋白分子间电荷中和、变性泡沫更细密稳定不易消泡；同时中和蛋清中天然黄酮类色素，使天使蛋糕保持纯白洁净。\n"
            "• 替代天然原料：(2分) 可使用新鲜柠檬汁（Lemon Juice）或天然白醋（White Vinegar）替代。通常用量约为塔塔粉用量的 2～3 倍即可。"
        )
    },
    {
        "q_num": "第 3 题：面包发酵阶段控制与自解法（Autolyse）工艺题 (10分)",
        "content": (
            "【问题 (a) 评分细则】(满分 6 分，三项对比各 2 分)\n"
            "① 操作时机区别：(2分) 基本发酵在面团搅拌完成之后、分割整型之前进行，属整块大面团的整体发酵；最后发酵在面团完成分割、滚圆、中间松弛与最终整型入模入盘之后、入炉烘烤之前进行。\n"
            "② 主要工艺目的区别：(2分) 基本发酵的核心目的是让酵母充分繁殖产气，促使面团熟成（Fermentation ripening），产生丰富的有机酸、酯类等芳香风味物质，建立面包的灵魂风味；最后发酵的核心目的是让成型后的面团在入炉前最大限度产气充气，恢复因整型排气而失去的体积，使面包达到标准饱满高度与松软孔洞。\n"
            "③ 温湿度环境区别：(2分) 基本发酵通常在常温或基础发酵室进行，温度约 26℃～28℃，湿度约 75%；最后发酵在专用发酵箱进行，温度显著较高（约 35℃～38℃，最适酵母产气温区），相对湿度约 80%～85%（高温促膨胀，高湿防表皮干燥结皮裂开）。\n\n"
            "【问题 (b) 评分细则】(满分 4 分)\n"
            "• 自解法标准操作步骤：(2分) 将配方中的面粉与全部（或大部分）水投入搅拌缸中，仅用低速混合至无干粉颗粒的粗糙面团即可停机，严禁加入酵母和盐，加盖静置 20～45 分钟。\n"
            "• 生化机理优势：(2分) ①在没有盐的阻碍下，面粉中的天然麦胶蛋白与麦谷蛋白在静置过程中充分吸水膨胀，面筋自然交联成网，大幅度缩短机械高速搅拌时间（减少面团氧化）；②天然淀粉酶将受损淀粉水解为麦芽糖，改善面团延展性与保气性，使出炉面包孔洞开放、麦香更醇厚。"
        )
    },
    {
        "q_num": "第 4 题：烘焙化学反应与油脂起酥机理题 (10分)",
        "content": (
            "【问题 (a) 评分细则】(满分 6 分，三维度对比各 2 分)\n"
            "① 触发反应的核心原料：(2分) 美拉德反应必须同时具备【还原糖】与【氨基酸 / 蛋白质】共同受热发生复杂缩合；焦糖化反应纯粹是【单一种类的糖类（如蔗糖、葡萄糖、果糖）】单独在无水或少水高温下受热降解脱水聚合物，不涉及蛋白质。\n"
            "② 反应起始温度：(2分) 美拉德反应起始温度较低，通常在 130℃～140℃ 即可明显加速发生；焦糖化反应所需温度较高，蔗糖通常在 160℃～180℃ 左右才开始发生熔化与剧烈焦糖化。\n"
            "③ 风味与色泽特征：(2分) 美拉德反应产生浓郁的烤面包香、肉香、坚果香与金黄至棕红焦褐色；焦糖化反应产生特有的焦糖甜香、太妃糖香、微苦风味及深琥珀至深褐色光泽。\n\n"
            "【问题 (b) 评分细则】(满分 4 分)\n"
            "黄油在曲奇饼干中的 2 个核心工艺功能：(每点 2 分)\n"
            "① 起酥与软化作用（Shortening & Tenderness）：黄油中固态乳脂包覆在面粉微粒表面，形成微细油脂薄膜，物理阻断面筋蛋白质与水分结合形成坚硬网络，烘烤后赋予曲奇饼干酥脆、化口性好、不易干硬的酥脆口感。(2分)\n"
            "② 充气蓬松与芳香风味（Creaming & Flavor）：黄油在打发（糖油拌和）时充入大量微细空气泡，在烘烤中受热膨胀使饼干体质蓬松均匀；同时天然乳脂受热挥发出高档而不可替代的浓郁天然黄油奶香。(2分)"
        )
    },
    {
        "q_num": "第 5 题：烘焙故障排查与食品安全卫生题 (10分)",
        "content": (
            "【问题 (a) 评分细则】(满分 6 分，排查出 3 个失误各得 2 分)\n"
            "考生从以下三个方面中任意列出 3 项合理失误即可得满分 6 分：\n"
            "① 打发与搅拌操作方面：全蛋打发程度不足（气泡粗大未形成细密划八字不消失状态）或打发过度消泡；面粉过筛后加入蛋糊时采用画圈方式长时间搅拌，导致严重消泡且面粉起筋。(2分)\n"
            "② 配方平衡方面：配方中水分、液体油或砂糖用量过高，导致蛋糕组织含水过多、整体支撑骨架承重不足；或者低筋面粉用量不足导致蛋白质骨架单薄。(2分)\n"
            "③ 烘烤与出炉处置方面：烘烤温度过高使表皮过早结硬上色而内部未完全熟透即出炉；出炉后未立即在操作台上轻震模具震出底部热气；未立即脱模或倒扣冷却导致水汽回流使中心下陷发黏。(2分)\n\n"
            "【问题 (b) 评分细则】(满分 4 分)\n"
            "• 严防危险温度带原因：(2分) 5℃～60℃ 为细菌极易超速繁殖的危险温度带。卡士达酱富含水分、蛋黄蛋白质与牛奶乳糖，属于微生物最喜爱的极高风险易腐营养基质，温室暴露极易滋生沙门氏菌或金黄色葡萄球菌释放耐热肠毒素引发食物中毒。\n"
            "• 急速降温与保存标准工序：(2分) ①卡士达酱刚离火出锅趁热，立即平铺倒入浅盘或冰水浴大不锈钢盆中以扩大散热面积；②立即使用食品级保鲜膜紧贴卡士达酱表面紧密覆盖（贴面包裹，严禁留有空气间隙，以防冷凝水滴落及表面风干结皮）；③立即移入速冷机或急冷库迅速降至 5℃ 以下，随后置于 2℃～7℃ 冷藏库密封保存并在 48 小时内使用完毕。"
        )
    }
]

for item in written_rubrics:
    p_rh = doc.add_paragraph()
    r_rht = p_rh.add_run(item["q_num"])
    r_rht.bold = True
    r_rht.font.size = Pt(10.5)
    r_rht.font.color.rgb = RGBColor(120, 53, 15)
    
    p_rc = doc.add_paragraph(item["content"])
    p_rc.paragraph_format.left_indent = Inches(0.2)
    p_rc.paragraph_format.space_after = Pt(10)
    p_rc.runs[0].font.size = Pt(9.5)
    p_rc.runs[0].font.color.rgb = RGBColor(51, 65, 85)

# Save Document
doc.save(OUT_PATH)
print(f"Generated Document 5: {OUT_PATH} ({os.path.getsize(OUT_PATH)} bytes)")
