# -*- coding: utf-8 -*-
"""
build_doc1_senior1_baking.py
Generates Document 1:
统考历届真题分类拆分汇编 —— 高一：烘焙基础理论与实务 (2020-2025年)
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
OUT_PATH = os.path.join(TARGET_DIR, '01_统考历届真题分类拆分_高一烘焙理论与实务(2020-2025).docx')

doc = create_styled_document()

# ── Title & Meta ──
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("马来西亚华文独中统一考试（UEC）厨艺理论与实务\n历届真题分类拆分与考点深度剖析")
run_title.font.size = Pt(18)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(120, 53, 15) # #78350F

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = p_sub.add_run("【高一阶段专属】烘焙基础理论与实务（2020～2025 年真题全收录）")
run_sub.font.size = Pt(14)
run_sub.font.bold = True
run_sub.font.color.rgb = RGBColor(180, 83, 9) # #B45309

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_meta = p_meta.add_run("适用对象：高一厨艺/烘焙班师生、统考备战冲刺复习 | 题型：单选题 · 罗马组合题 · 作答计算题")
run_meta.font.size = Pt(9.5)
run_meta.font.italic = True
run_meta.font.color.rgb = RGBColor(100, 116, 139)

doc.add_paragraph() # Spacer

# ── Part 1: Examination Blueprint & Weight Analysis ──
h1 = doc.add_heading("第一部分：高一烘焙理论在独中统考中的权重与考点矩阵", level=1)
h1.style.font.color.rgb = RGBColor(120, 53, 15)

p_intro = doc.add_paragraph(
    "在马来西亚华文独中统一考试《厨艺理论与实务》（SY26）中，高一阶段对应的【烘焙基础理论与实务】是全卷分值占比最大、考察范围最广的核心模块。"
    "历届试卷一（选择题 60%）中，甲组固定为 40 道烘焙题（占 40 分）；试卷二（作答题 40%）中，烘焙类必答题或选答题每年稳定占 10～20 分。"
    "高一烘焙理论在统考总分（100分）中的实际权重高达 50%～60%，堪称统考决胜的基石！"
)

# Table: Blueprint Matrix
table_matrix = doc.add_table(rows=1, cols=4)
table_matrix.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["知识板块 (高一20课体系)", "统考历届高频题型", "每年平均分值", "核心考察要点与命题规律"]
hdr_cells = table_matrix.rows[0].cells
for i, h in enumerate(headers):
    hdr_cells[i].text = h
    set_cell_background(hdr_cells[i], "FEF3C7") # Warm light amber
    set_cell_margins(hdr_cells[i], top=120, bottom=120, left=150, right=150)
    for p in hdr_cells[i].paragraphs:
        p.runs[0].font.bold = True
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = RGBColor(120, 53, 15)

matrix_data = [
    ("烘焙原料学 (粉/糖/油/蛋/乳/膨大剂)", "单选、罗马组合题、作答题", "18～22 分", "面粉吸水量与蛋白质、糖的焦糖化与梅纳反应、反式脂肪与起酥油、酵母种类及活性、天然 vs 碱化可可粉、泡打粉与小苏打"),
    ("度量衡与烘焙百分比计算", "选择题、试卷二必答大题", "10～12 分", "以面粉为100%基准计算各材料净重；烤盘容积计算；面团分割滚圆机产能与耗时换算"),
    ("面包制作法与发酵工艺流程", "单选、罗马题、工艺分析作答题", "12～15 分", "直接法 vs 中种法 vs 自解法（Autolyse）；基本发酵、中间松弛与最后发酵温湿度；排气与面筋扩展"),
    ("三大类蛋糕制作与打发机理", "单选、罗马组合题、综合分析题", "10～14 分", "面糊类（磅蛋糕）、乳沫类（海绵/天使）、戚风类；蛋黄乳化与蛋白打发；塔塔粉作用；出炉收缩塌陷原因"),
    ("西点派塔、泡芙、开酥与饼干", "单选题、罗马组合题", "6～8 分", "千层酥与可颂开酥水蒸气原理；泡芙（空心饼）烫面糊化与喷水；饼干糖粒径对脆软质感的影响"),
    ("烘焙设备器具与食品卫生安全", "单选题、案例排查题", "4～6 分", "危险温度带（5～60℃）；拌打器类型（钩/球/桨）；旋转烤炉与对流蒸烤箱；交叉污染与器具杀菌")
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
h2 = doc.add_heading("第二部分：2020～2025年统考历届高一烘焙选择题分类精选汇编", level=1)
h2.style.font.color.rgb = RGBColor(120, 53, 15)

p_mcq_note = doc.add_paragraph("本部分严格按照独中考纲知识单元归类，精选近 5 年最具代表性的真实考题，包含常规单选题与统考标志性的【罗马数字组合选择题】，并逐题提供权威解析：")
p_mcq_note.runs[0].font.italic = True

baking_mcqs = [
    # 原料学
    {
        "unit": "模块一：烘焙原料学 (面粉、糖、油脂、膨大剂、添加剂)",
        "items": [
            {
                "id": "2025-Q3",
                "q": "【2025年统考真题】2017年，比利时巧克力生产商推出一款巧克力新品种，入口甘甜并能尝到天然树莓果香，色泽呈粉红。此巧克力的名称为何？",
                "opts": ["A. 红宝石巧克力 (Ruby Chocolate)", "B. 单品巧克力 (Single Origin Chocolate)", "C. 免调温巧克力 (Compound Chocolate)", "D. 圣多诺黑巧克力 (Saint-Honoré Chocolate)"],
                "ans": "A",
                "exp": "红宝石巧克力（Ruby Chocolate）是百利嘉利宝于2017年研发推出的第四种巧克力（前三种为黑、白、牛奶），由特选红宝石可可豆通过独特加工制成，具备天然粉红色泽与清新莓果微酸，无需人工添加色素或香精。"
            },
            {
                "id": "2024-Q19",
                "q": "【2024年统考真题】烘焙产品使用下列哪一种糖类，在烘焙受热时最容易且剧烈产生梅纳反应（Maillard Reaction）？",
                "opts": ["A. 果糖 (Fructose)", "B. 砂糖 (Sucrose)", "C. 乳糖 (Lactose)", "D. 麦芽糖 (Maltose)"],
                "ans": "A",
                "exp": "梅纳反应（美拉德反应）是还原糖与氨基酸/蛋白质在受热时产生的褐变与香气反应。单糖中的还原糖活性显著高于双糖，其中果糖（还原单糖）的反应活性最强、着色温度最低（约130℃即开始剧烈发生），因此最易上色。"
            },
            {
                "id": "2023-Q5",
                "q": "【2023年统考真题 · 罗马组合题】关于烘焙常用可可粉的分类与应用，下列叙述何者正确？\n"
                       "   I. 天然可可粉呈微酸性 (pH 5.2～5.8)，颜色较浅，需搭配小苏打使用\n"
                       "   II. 碱化可可粉呈中性或微碱性 (pH 6.6～7.6)，溶解度高，需搭配泡打粉使用\n"
                       "   III. 最高级可可粉的可可脂含量通常在 24% 以上\n"
                       "   IV. 天然可可粉遇水极易溶解，无需过筛即可直接加入面糊",
                "opts": ["A. I, II, III", "B. I, III, IV", "C. II, III, IV", "D. I, II, IV"],
                "ans": "A",
                "exp": "天然可可粉酸度较高（pH 5.2~5.8），必须用碱性苏打粉中和并辅助膨胀；碱化（荷兰式加工）降低了酸度使色泽变深且易溶于水，需改用双效泡打粉；可可脂>24%属最高级可可粉。IV错误：可可粉易结块，必须与面粉共同过筛。"
            },
            {
                "id": "2022-Q18",
                "q": "【2022年统考真题】将固体油脂切成小丁块与面粉拌匀（搓沙法），然后再加入冰水拌合成团，是指下列哪一种烘焙产品的典型开酥工艺？",
                "opts": ["A. 海绵蛋糕 (Sponge Cake)", "B. 派皮与酥皮 (Pie Crust / Flaky Pastry)", "C. 吐司面包 (Toast Bread)", "D. 戚风蛋糕 (Chiffon Cake)"],
                "ans": "B",
                "exp": "将冷硬固体油脂（黄油或起酥油）切丁与面粉用手或派皮刮刀搓成豆粒状碎屑（Rub-in / Sablage 搓沙法），油脂包覆面粉颗粒阻断面筋，烘烤时油脂受热熔化留出空隙、所含水分蒸发产生片状分层，是典型美式派皮与英式司康的制法。"
            },
            {
                "id": "2020-Q1",
                "q": "【2020年统考真题】下列哪一种烘焙产品在配方中一定必须使用高筋面粉作为主要骨架支撑？",
                "opts": ["A. 海绵蛋糕 (Sponge Cake)", "B. 意式比萨饼皮与白吐司", "C. 天使蛋糕 (Angel Food Cake)", "D. 酥脆曲奇饼干 (Cookies)"],
                "ans": "B",
                "exp": "高筋面粉（含粗蛋白 11.5%～14%）面筋含量高、筋力强、持气性好，是膨胀体积大、需要拉丝与弹性组织的面包、白吐司及比萨饼皮的核心原料；蛋糕与饼干则主要使用低筋面粉（蛋白7%~9%）。"
            },
            {
                "id": "2020-Q36",
                "q": "【2020年统考真题】在下列各类烹饪与烘焙用油脂中，哪一种因氢化加工工艺而最可能含有对人体心血管不利的反式脂肪酸（Trans Fat）？",
                "opts": ["A. 天然无盐黄油 (Butter)", "B. 纯猪油 (Lard)", "C. 人造起酥油与人造植物黄油 (Shortening / Margarine)", "D. 初榨橄榄油 (Olive Oil)"],
                "ans": "C",
                "exp": "植物油在工业部分氢化（Partial Hydrogenation）以提高熔点和固态稳定性的过程中，部分不饱和双键异构化为反式脂肪酸。传统起酥油、人造植物黄油在过去常含有较高反式脂肪酸。"
            }
        ]
    },
    # 面包制作与发酵
    {
        "unit": "模块二：面包制作法与发酵工艺流程",
        "items": [
            {
                "id": "2024-Q8",
                "q": "【2024年统考真题】在面包配方调整中，若因特定风味需求增加了鸡蛋的使用量，为保持面团标准软硬稠度，应相应酌量减少哪一项材料的用量？",
                "opts": ["A. 配方中的水 (Water)", "B. 配方中的细砂糖 (Sugar)", "C. 配方中的食盐 (Salt)", "D. 配方中的干酵母 (Yeast)"],
                "ans": "A",
                "exp": "全蛋液中平均含有约 75% 的水分与 25% 的固形物（蛋白质及蛋黄脂肪）。因此增加鸡蛋实际上带入了大量液体水分，必须扣除相应比例的水量（每增100g全蛋，需减约75g水），否则面团会过湿黏手无法操作。"
            },
            {
                "id": "2023-Q37",
                "q": "【2023年统考真题】下列哪一种经典面包品种在完成最后发酵后，入炉烘烤前会先放入添加麦芽糖的水锅中每面汆烫烫煮约 1 分钟？",
                "opts": ["A. 可颂羊角包 (Croissant)", "B. 法式长棍面包 (Baguette)", "C. 贝果面包 (Bagel)", "D. 意式夏巴塔 (Ciabatta)"],
                "ans": "C",
                "exp": "贝果（Bagel）的标志性特色工艺是在最后发酵完成后、入炉烘烤前，放入接近沸腾（约90℃）的糖水或麦芽糖水中正反面各煮30~60秒。表皮淀粉瞬间预糊化形成坚韧致密的凝胶外层，烘烤后表皮光亮光泽、内部组织扎实耐嚼。"
            },
            {
                "id": "2022-Q1",
                "q": "【2022年统考真题】制作油炸酵母道纳司（甜甜圈 Yeast Doughnuts）品尝时发现成品带有明显酸味，其最可能的技术工艺失误是？",
                "opts": ["A. 基本发酵或面团发酵时间过度 (Over-fermentation)", "B. 中间松弛时间严重不足", "C. 油炸时油温过高表面快速焦黑", "D. 配方中面粉的筋度过高"],
                "ans": "A",
                "exp": "酵母面团在长时间过度发酵或高温发酵下，酵母菌产气消耗完可发酵糖，杂菌（如乳酸菌、醋酸菌）大量繁殖代谢产出过量乳酸与醋酸，导致面团 pH 显著下降，成品出锅后带有刺鼻不悦的酸味。"
            },
            {
                "id": "2021-Q17",
                "q": "【2021年统考真题】利用中种法（Sponge and Dough Method）制作吐司面包时，下列哪一项原料绝不可放入第一阶段的“中种面团”中搅拌？",
                "opts": ["A. 盐和油脂（黄油/酥油）", "B. 部分高筋面粉", "C. 水或鲜奶", "D. 酵母"],
                "ans": "A",
                "exp": "中种法第一阶段中种面团（Sponge）通常仅由 70%~80% 的面粉、适量水和全部酵母混合简单慢速搅拌，不加油脂（油脂包覆面筋阻碍面筋水化）和糖盐（盐的高渗透压会抑制酵母早期繁殖），油脂与糖盐留待第二阶段主面团加入。"
            },
            {
                "id": "2020-Q7",
                "q": "【2020年统考真题】在面包制作标准工序中，“醒面”或“中间发酵（Bench Time）”的主要技术意义是指什么？",
                "opts": ["A. 搅拌完成后的第一阶段发酵", "B. 烘烤前在发酵箱中的最后产气膨胀", "C. 分割滚圆后静置10～15分钟使面筋松弛便于成型", "D. 出炉后在晾网上的冷却过程"],
                "ans": "C",
                "exp": "面团经过机械切割与滚圆揉搓后，面筋网络处于高度紧张紧缩状态。中间发酵（松弛 / Bench Time）通过常温静置 10～15 分钟，让面筋张力得以缓解放松，恢复柔软的延展性，从而在下一步擀卷整型时不会回弹或破皮。"
            }
        ]
    },
    # 蛋糕制作工艺
    {
        "unit": "模块三：三大类蛋糕制作工艺、打发与事故排查",
        "items": [
            {
                "id": "2025-Q8",
                "q": "【2025年统考真题 · 罗马组合题】在制作重巧克力海绵蛋糕时，主要促使蛋糕出炉后整体组织结构挺立、防止塌陷的“干性强韧材料”有哪些？\n"
                       "   I. 低筋面粉与直链淀粉\n"
                       "   II. 可可粉中固形物\n"
                       "   III. 鸡蛋中蛋白质\n"
                       "   IV. 植物色拉油与液体黄油",
                "opts": ["A. I, II, III", "B. II, III, IV", "C. I, III, IV", "D. I, II, IV"],
                "ans": "A",
                "exp": "烘焙材料按结构作用分为：韧性/强韧材料（面粉、蛋蛋白、可可粉，受热凝固提供骨架支撑力）；柔性/弱性材料（糖、油脂、蛋黄，起润滑软化作用使蛋糕松软）。油脂是纯柔性材料，会削弱结构；I、II、III 均提供结构支撑。"
            },
            {
                "id": "2024-Q3",
                "q": "【2024年统考真题】制作天使蛋糕（Angel Food Cake）在打发纯蛋清时，配方中通常必须加入少量塔塔粉（酒石酸氢钾），其核心科学作用是？",
                "opts": ["A. 调节蛋白碱性至偏酸性，使蛋白泡沫微细稳定并使蛋糕体洁白", "B. 充当强力化学膨大剂受热释放二氧化碳", "C. 增加面糊粘稠度以替代低筋面粉的骨架", "D. 提高甜度并促进表皮焦糖化快速上色"],
                "ans": "A",
                "exp": "蛋清呈碱性（pH 8.8~9.2），加入酸性盐塔塔粉降低 pH 至微酸性（接近蛋白质等电点），使打发产生的蛋白气泡更细密强韧、不易消泡；同时酸性环境使面粉中天然黄酮类色素脱色呈纯白色，保证天使蛋糕纯洁白皙。"
            },
            {
                "id": "2021-Q5",
                "q": "【2021年统考真题】海绵蛋糕烘烤出炉后出现严重过度收缩（Shrinkage）甚至塌陷，下列哪一项不是造成该故障的可能原因？",
                "opts": ["A. 出炉后未立即在台面上轻震排气，或未立即脱模倒扣晾凉", "B. 配方中水分与液体用量过高，导致内部湿气过大", "C. 面粉中适度用一部分玉米淀粉取代以降低筋度", "D. 烤盘底部涂擦过多油脂导致面糊攀爬附着力不足"],
                "ans": "C",
                "exp": "用适量玉米粉（无筋面粉）取代部分面粉能有效降低筋度，使海绵蛋糕组织更松软化口，这是标准配方改良手段，不会导致塌陷。A（未震气）、B（水分过高）、D（擦油过多无法附着爬高）均会导致严重塌陷收缩。"
            },
            {
                "id": "2020-Q5",
                "q": "【2020年统考真题】为改善传统全蛋海绵蛋糕组织的过度韧性（Toughness），在配方调制中可以通过添加下列哪一种材料来增加滑顺柔嫩度？",
                "opts": ["A. 增加蛋清的比例", "B. 增加低筋面粉用量", "C. 加入适量蛋黄或少许融化黄油 (Liquid Fat)", "D. 增加食盐用量"],
                "ans": "C",
                "exp": "全蛋海绵蛋糕韧性主要来自面筋与蛋清受热凝固。蛋黄富含天然卵磷脂与脂肪，液体黄油是柔性材料，加入面糊能包覆部分淀粉颗粒与蛋白质分子，阻断面筋过分紧密结合，从而有效减弱韧性、提升细腻化口口感。"
            }
        ]
    },
    # 计量与计算
    {
        "unit": "模块四：度量衡、烤盘容积换算与设备操作",
        "items": [
            {
                "id": "2022-Q8",
                "q": "【2022年统考真题】一个标准圆形蛋糕烤盘的直径为 22 公分（半径 r = 11 公分）、高为 5 公分，则其几何容积最接近多少立方公分？(圆周率 π 取 3.1416)",
                "opts": ["A. 7,598.8 立方公分", "B. 1,899.7 立方公分", "C. 380.1 立方公分", "D. 110.0 立方公分"],
                "ans": "B",
                "exp": "圆柱体烤盘容积公式：V = π × r² × h。半径 r = 22 ÷ 2 = 11 公分，容积 V = 3.1416 × 11 × 11 × 5 = 3.1416 × 121 × 5 ≈ 1,899.7 立方公分。故选 B。"
            },
            {
                "id": "2021-Q1",
                "q": "【2021年统考真题】烘焙工场若使用全自动分割滚圆机分割甜面包面团，设定每分钟可分割 50 粒、每粒 60 克。现有 60 公斤面团，需要多少时间方可全部分割完成？",
                "opts": ["A. 20 分钟", "B. 30 分钟", "C. 40 分钟", "D. 50 分钟"],
                "ans": "A",
                "exp": "60公斤面团 = 60,000 克。总面团粒数 = 60,000 ÷ 60 = 1,000 粒。每分钟可分割 50 粒，总耗时 = 1,000 ÷ 50 = 20 分钟。故选 A。"
            },
            {
                "id": "2024-Q1",
                "q": "【2024年统考真题】在食品安全与卫生标准中，下列哪一个温度区间被正式定义为“食品危险温度带（Danger Zone）”，需严格限制食品暴露时间？",
                "opts": ["A. 0℃ ～ 4℃ 之间", "B. 5℃ ～ 60℃ 之间", "C. 65℃ ～ 100℃ 之间", "D. 零下 18℃ 以下"],
                "ans": "B",
                "exp": "食品安全法规定：5℃～60℃为细菌极易大量快速繁殖或代谢释放毒素的危险温度带（尤以35℃~37℃繁殖最快）。高风险烘焙馅料（卡士达酱、打发鲜奶油）在此温度带存放不得超过 2 小时。"
            }
        ]
    }
]

for section in baking_mcqs:
    h_sec = doc.add_heading(section["unit"], level=2)
    h_sec.style.font.color.rgb = RGBColor(180, 83, 9)
    
    for item in section["items"]:
        # Question paragraph
        p_q = doc.add_paragraph()
        run_qid = p_q.add_run(f"{item['id']} ")
        run_qid.bold = True
        run_qid.font.color.rgb = RGBColor(120, 53, 15)
        run_qtext = p_q.add_run(item["q"])
        run_qtext.bold = True
        
        # Options
        for opt in item["opts"]:
            p_opt = doc.add_paragraph(opt)
            p_opt.paragraph_format.left_indent = Inches(0.25)
            p_opt.paragraph_format.space_after = Pt(2)
        
        # Answer & Explanation Callout Box
        tbl_exp = doc.add_table(rows=1, cols=1)
        tbl_exp.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_exp = tbl_exp.rows[0].cells[0]
        set_cell_background(c_exp, "F8FAFC") # Soft light blue-gray
        set_cell_margins(c_exp, top=80, bottom=80, left=120, right=120)
        
        p_ans = c_exp.paragraphs[0]
        r_ans = p_ans.add_run(f"【标准答案】：{item['ans']}      ")
        r_ans.bold = True
        r_ans.font.color.rgb = RGBColor(16, 185, 129) # Emerald Green
        
        r_exp_title = p_ans.add_run("【考点深入解析】：\n")
        r_exp_title.bold = True
        r_exp_title.font.color.rgb = RGBColor(71, 85, 105)
        
        r_exp_body = p_ans.add_run(item["exp"])
        r_exp_body.font.size = Pt(9.5)
        r_exp_body.font.color.rgb = RGBColor(51, 65, 85)
        
        set_table_borders(tbl_exp, color="CBD5E1")
        doc.add_paragraph() # Spacer

# ── Part 3: Written Questions (Paper 2) ──
h3 = doc.add_heading("第三部分：2020～2025年统考历届高一烘焙作答题精选与评分细则", level=1)
h3.style.font.color.rgb = RGBColor(120, 53, 15)

written_cases = [
    {
        "year": "2024 / 2025 年统考大题 (试卷二必答题 · 10%)",
        "title": "烘焙百分比标准计算题 (配方净重换算)",
        "desc": "已知某烘焙工场制作低糖甜面包配方，其低筋面粉（或高筋面粉）重量为 312g，各材料烘焙百分比如下表所示。请按统考规范重抄表格，并准确计算填入各个别材料的实际使用重量（单位：g，四舍五入保留整数）以及配方面团总重量。",
        "table": [
            ["材料名称", "烘焙百分比 (%)", "实际重量 (g) [题目]", "参考答案及算式计算过程"],
            ["低筋面粉", "100.0 % (基准)", "312 g", "面粉为基准100%，实际重量 = 312 g (已知)"],
            ["细砂糖", "100.0 %", "(a) ____ g", "312 g × 100% = 312 g (给2分)"],
            ["全蛋液", "167.0 %", "(b) ____ g", "312 g × 167% = 312 × 1.67 = 521.04 ≈ 521 g (给2分)"],
            ["双效泡打粉", "1.0 %", "(c) ____ g", "312 g × 1.0% = 3.12 ≈ 3.1 g (给2分)"],
            ["配方总重量", "268.0 %", "(d) ____ g", "312 + 312 + 521 + 3.1 = 837.1 ≈ 837 g (给2分)"]
        ],
        "rubric": "【评分标准与命题规律总结】：\n"
                  "1. 核心定义踩分点：在烘焙百分比中，面粉（Flour）永远固定为 100% 基准！其他任何材料的实际重量 = 面粉重量 × 该材料烘焙百分比。\n"
                  "2. 该大题在 2024、2025 年统考连续作为试卷二甲组必答题（10分）出现，数字虽然简单，但考生极易将全蛋 167% 算错或忘记将面粉作为 100% 除数，属于送分必拿题！"
    },
    {
        "year": "2023 年统考大题 (试卷二选答题 · 10%)",
        "title": "三大类蛋糕分类、油脂含量对比与打发机理",
        "desc": "问题 (a)：写出市面上植物性鲜奶油与动物性鲜奶油的理想保存方法及使用温度差异。(4分)\n"
                "问题 (b)：写出西点三大类蛋糕中，哪一类蛋糕的配方油脂含量最高？并列举出市面上最常见的两种属于该类别的蛋糕名称。(6分)",
        "table": None,
        "rubric": "【参考答案与评分要点】：\n"
                  "问题 (a) 解答：(4分)\n"
                  "  • 植物性鲜奶油保存：通常置于冷冻库（-18℃）长期保存，使用前24小时移至冷藏室（2~7℃）充分退冰解冻，最佳打发温度为 4~7℃。（2分）\n"
                  "  • 动物性鲜奶油保存：必须冷藏（2~7℃），绝对严禁冷冻，冷冻会导致乳脂球冰晶破裂发生油水分离；打发最佳温度为 4~8℃。（2分）\n"
                  "问题 (b) 解答：(6分)\n"
                  "  • 油脂含量最高的类别：面糊类蛋糕（Shortened Cake / Butter Cake），配方中黄油或起酥油占面粉重量通常在 50%～100%。（2分）\n"
                  "  • 常见两种蛋糕名称：重奶油蛋糕（Butter Cake）、磅蛋糕（Pound Cake）、水果蛋糕（Fruit Cake）、布朗尼（Brownie）。（任意写出两种各得2分，共4分）"
    },
    {
        "year": "2022 年统考大题 (试卷二选答题 · 10%)",
        "title": "可可粉与巧克力调温（Tempering）科学机理",
        "desc": "问题 (a)：烘焙中常使用天然可可粉与碱化可可粉，试说明两者在酸碱度、色泽以及所搭配膨大剂上的三项核心区别。(6分)\n"
                "问题 (b)：纯纯黑巧克力在制作手工巧克力排块前为何必须经过“调温（Tempering）”？简述调温成功的感官标志与判断方法。(4分)",
        "table": None,
        "rubric": "【参考答案与评分要点】：\n"
                  "问题 (a) 解答：(6分)\n"
                  "  ① 酸碱性区别：天然可可粉呈微酸性（pH 5.2~5.8）；碱化可可粉经碳酸钾碱化处理呈中性或微碱性（pH 6.6~7.6）。（2分）\n"
                  "  ② 色泽区别：天然可可粉呈浅红褐色；碱化可可粉呈深红褐色至深咖啡色，碱性越高颜色越深。（2分）\n"
                  "  ③ 搭配膨大剂区别：天然可可粉因具酸性必须搭配小苏打粉（碱性中和）；碱化可可粉不具酸性需搭配两倍用量的泡打粉。（2分）\n"
                  "问题 (b) 解答：(4分)\n"
                  "  • 调温目的：促使可可脂分子形成最稳定、熔点适中（约34℃）的第V型（β晶型）结晶。（2分）\n"
                  "  • 成功标志：在铲刀上室内静置约3~5分钟即能快速凝固；凝固后表面具有光亮镜面光泽、触手不粘、折断时声清脆（Snap）、室温不易起白霜脱模容易。（2分）"
    }
]

for w in written_cases:
    p_yr = doc.add_paragraph()
    r_yr = p_yr.add_run(f"📅 {w['year']} —— {w['title']}")
    r_yr.bold = True
    r_yr.font.size = Pt(11)
    r_yr.font.color.rgb = RGBColor(120, 53, 15)
    
    p_desc = doc.add_paragraph(w['desc'])
    p_desc.paragraph_format.left_indent = Inches(0.2)
    
    if w['table']:
        tbl = doc.add_table(rows=len(w['table']), cols=4)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        for r_idx, r_data in enumerate(w['table']):
            row_cells = tbl.rows[r_idx].cells
            for c_idx, text in enumerate(r_data):
                row_cells[c_idx].text = text
                set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=100, right=100)
                if r_idx == 0:
                    set_cell_background(row_cells[c_idx], "FEF3C7")
                    row_cells[c_idx].paragraphs[0].runs[0].font.bold = True
                    row_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(9)
                else:
                    row_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(8.5)
        set_table_borders(tbl)
        doc.add_paragraph() # Spacer
        
    p_rub = doc.add_paragraph()
    p_rub.paragraph_format.left_indent = Inches(0.2)
    p_rub.paragraph_format.space_after = Pt(12)
    r_rub = p_rub.add_run(w['rubric'])
    r_rub.font.size = Pt(9.5)
    r_rub.font.color.rgb = RGBColor(71, 85, 105)

# Save Document
doc.save(OUT_PATH)
print(f"Generated Document 1: {OUT_PATH} ({os.path.getsize(OUT_PATH)} bytes)")
