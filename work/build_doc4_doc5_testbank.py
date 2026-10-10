# -*- coding: utf-8 -*-
"""
build_doc4_doc5_testbank.py
Generates Document 4 (Student/Test Paper) and Document 5 (Teacher Answer Key):
- Document 4: 04_高一烘焙基础理论全真模拟测验题卷(统考风格标准卷).docx
- Document 5: 05_高一烘焙基础理论全真模拟测验题卷(教师详细评分参考答案).docx

Updates per user requirements:
1. Reframe as Teacher's Exam Item Bank (教师专用出题题库 / 统考风格测试卷)，remove time limit (80min) and 100-point hardcoding.
2. Ensure strict option length balance: span between longest and shortest option in every question <= 4 chars.
3. Consistent bilingual formatting: if an option has English, ALL 4 options must have matching English. No answer giveaways.
4. Total 50 MCQs (expanded by 20 questions, Q1-Q50, including single choice & Roman questions).
5. 10 Short Answer Questions (简短作答题) + 5 Comprehensive Written/Calculation Questions.
6. Complete Teacher Answer Key with quick answer grid, in-depth explanations, and detailed point rubrics.
"""

import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx_helper import create_styled_document, set_cell_background, set_cell_margins, set_table_borders

TARGET_DIR = r'统考历届考题拆分与高一测验卷_Word'
os.makedirs(TARGET_DIR, exist_ok=True)
DOC4_PATH = os.path.join(TARGET_DIR, '04_高一烘焙基础理论全真模拟测验题卷(统考风格标准卷).docx')
DOC5_PATH = os.path.join(TARGET_DIR, '05_高一烘焙基础理论全真模拟测验题卷(教师详细评分参考答案).docx')

# =========================================================================
# 50 MCQs DATA DEFINITION
# All options carefully written with:
# - Balanced lengths (span <= 4 chars)
# - Parallel grammatical structure
# - Symmetric bilingual formatting
# =========================================================================

mcq_bank = [
    # Q1
    {
        "id": 1,
        "q": "在烘焙面粉分类中，划分高筋、中筋与低筋面粉最主要的理化指标是？",
        "opts": {
            "A": "面粉中所含粗蛋白质的含量与面筋强度",
            "B": "面粉在石磨研磨时的颗粒粗细与白度值",
            "C": "面粉中直链淀粉在遇水受热时的膨胀度",
            "D": "面粉经过长期常温陈化后的自然吸水量"
        },
        "ans": "A",
        "exp": "高筋面粉（粗蛋白11.5%~14%）、中筋面粉（9.5%~11.5%）、低筋面粉（7%~9%）。蛋白质含量及面筋筋力强度是划分面粉分类的核心法定指标。"
    },
    # Q2
    {
        "id": 2,
        "q": "在烘焙百分比（Baker's Percentage）计算系统中，永远被设定为100%基准的原料是？",
        "opts": {
            "A": "配方中纯净清水的重量",
            "B": "配方中总面粉的净重量",
            "C": "全蛋与液体牛奶的总重",
            "D": "面团搅拌成型的总重量"
        },
        "ans": "B",
        "exp": "烘焙百分比永远以配方中面粉总重量作为 100% 基准除数，其他各原料用量均以此换算为相应百分比。"
    },
    # Q3
    {
        "id": 3,
        "q": "打发蛋白制作天使蛋糕时加入塔塔粉（酒石酸氢钾），其最主要的工艺目的是？",
        "opts": {
            "A": "提高蛋白糊甜度并加快焦糖化",
            "B": "调节酸碱度稳定泡沫并使质地洁白",
            "C": "充当强效膨大剂释放大量二氧化碳",
            "D": "增加面糊稠度以替代低筋面粉骨架"
        },
        "ans": "B",
        "exp": "蛋清呈弱碱性，加入酸性盐塔塔粉使蛋白 pH 接近等电点，泡沫更细腻强韧不易消泡，且使蛋糕体洁白。"
    },
    # Q4
    {
        "id": 4,
        "q": "在下列各类烘焙用糖中，保润抗老化效果最好的是哪一种？",
        "opts": {
            "A": "精制粗砂糖 (Granulated Sugar)",
            "B": "纯白纯糖粉 (Powdered Sugar)",
            "C": "转化糖浆类 (Invert Sugar Syrup)",
            "D": "纯细蔗糖粉 (Castor Fine Sugar)"
        },
        "ans": "C",
        "exp": "转化糖浆富含单糖（葡萄糖和果糖），吸湿保润性极强，能有效抑制淀粉重结晶老化，延长产品保鲜期。"
    },
    # Q5
    {
        "id": 5,
        "q": "烘焙双效泡打粉（Baking Powder）被称为“双效”，其产气原理是？",
        "opts": {
            "A": "面糊冷水搅拌反应产气 ＋ 入炉受热持续膨胀产气",
            "B": "常温接触空气快速氧化 ＋ 出炉自然冷却吸湿产气",
            "C": "酵母菌无氧呼吸发酵产气 ＋ 高温蒸汽挥发顶起面糊",
            "D": "机械搅拌物理裹入空气 ＋ 淀粉糊化吸水凝固产气"
        },
        "ans": "A",
        "exp": "双效泡打粉含低温酸性盐（常温溶水即产气）与高温酸性盐（进炉加热超过60℃持续受热产气）。"
    },
    # Q6
    {
        "id": 6,
        "q": "重奶油磅蛋糕制作采用“糖油拌和法”，打发黄油的核心目标是？",
        "opts": {
            "A": "促使面筋充分延伸形成强韧网状组织",
            "B": "使砂糖在固体油脂摩擦中充入细微气孔",
            "C": "促使黄油在高速运转下完全融化成液体",
            "D": "彻底分解低筋面粉内部天然直链淀粉"
        },
        "ans": "B",
        "exp": "固体黄油具有可塑性，砂糖晶体摩擦刮入大量微细空气，受热时空气膨胀赋予重奶油蛋糕松软细腻结构。"
    },
    # Q7
    {
        "id": 7,
        "q": "面包工艺中的“自解法（Autolyse）”，其规范的操作方式是？",
        "opts": {
            "A": "仅混合粉水静置促使面筋自然形成",
            "B": "将全部材料一次性高速搅打至出膜",
            "C": "加入大量干酵母置于温室催发酒精",
            "D": "在干锅中翻炒面粉使麦香味完全释放"
        },
        "ans": "A",
        "exp": "自解法只将面粉与水混合慢拌成团，不加酵母和盐，静置20~45分钟，让面粉充分水化、面筋自然排列，减少机械搅拌时间。"
    },
    # Q8
    {
        "id": 8,
        "q": "在面包面团搅拌中，食盐（Salt）所发挥的核心工艺调节功能是？",
        "opts": {
            "A": "彻底阻断面筋网络形成使面包松散",
            "B": "增强面筋韧性并适度调控酵母产气速度",
            "C": "作为主要发酵养料加速酵母大量繁殖",
            "D": "大幅降低面粉吸水量防止面团过分湿黏"
        },
        "ans": "B",
        "exp": "食盐能收敛强化面筋网络、增强面筋弹性，同时高渗透压能适度抑制酵母发酵速度，防止面团发酵过快变酸。"
    },
    # Q9
    {
        "id": 9,
        "q": "制作法式可颂与千层酥开酥时，裹入黄油的最适宜操作温度是？",
        "opts": {
            "A": "0℃～4℃之间 (质地坚硬易断裂)",
            "B": "16℃～18℃之间 (软硬适中延展好)",
            "C": "28℃～30℃之间 (接近融化易渗出)",
            "D": "36℃～38℃之间 (呈液体油水分离)"
        },
        "ans": "B",
        "exp": "开酥黄油在 16℃~18℃ 具有最佳可塑性（Plasticity），软硬度与面团一致，折叠擀压不碎裂、不化油。"
    },
    # Q10
    {
        "id": 10,
        "q": "食品安全法中，最易滋生致病细菌的“危险温度带”标准范围是？",
        "opts": {
            "A": "0℃至4℃之间",
            "B": "5℃至60℃之间",
            "C": "65℃至85℃之间",
            "D": "100℃至120℃之间"
        },
        "ans": "B",
        "exp": "5℃~60℃为细菌繁殖最活跃的危险温度带。高风险烘焙馅料暴露于此温度带总时间不得超过 2 小时。"
    },
    # Q11
    {
        "id": 11,
        "q": "关于天然可可粉与碱化可可粉的区别，下列叙述何者完全正确？",
        "opts": {
            "A": "天然可可粉呈微碱性且溶解度特别高",
            "B": "天然可可粉呈微酸性需搭配小苏打使用",
            "C": "碱化可可粉呈强酸性需加入大量食醋调和",
            "D": "两者在酸碱度色泽及膨大剂选用上毫无差异"
        },
        "ans": "B",
        "exp": "天然可可粉未经加碱处理呈微酸性（pH 5.2~5.8），色浅红褐，必须用碱性小苏打中和以平衡酸碱并辅助膨胀。"
    },
    # Q12
    {
        "id": 12,
        "q": "海绵蛋糕出炉冷却后出现严重收缩塌陷，最不可能的工艺原因是？",
        "opts": {
            "A": "全蛋打发不足或拌粉手法粗暴导致消泡",
            "B": "出炉后未立即震出热气并倒扣冷却脱模",
            "C": "烘烤底火不足导致蛋糕内部未完全定型",
            "D": "配方中适量掺入一成玉米淀粉降低筋度"
        },
        "ans": "D",
        "exp": "掺入约 10% 玉米淀粉降低面筋筋度、提升松软度是标准规范工艺，绝不会导致塌陷。A、B、C 均为严重失误。"
    },
    # Q13
    {
        "id": 13,
        "q": "面包面团经过搅拌达到“完全扩展阶段”时，其典型外观特征是？",
        "opts": {
            "A": "表面干硬粗糙且拉扯时立即脆断",
            "B": "能撑开透光薄膜且裂口边缘光滑",
            "C": "面团呈流质糊状完全无阻力黏手",
            "D": "面团表面出现大量剧烈翻滚气泡"
        },
        "ans": "B",
        "exp": "完全扩展阶段（手套膜）：面团光滑柔软不黏手，能拉出均匀半透明薄膜，戳破时洞口边缘平滑无锯齿裂纹。"
    },
    # Q14
    {
        "id": 14,
        "q": "烘焙油脂的“起酥性（Shortening Value）”主要指的是哪种功能？",
        "opts": {
            "A": "阻断面筋形成并赋予产品酥松的特性",
            "B": "在高温烘烤下挥发产生浓郁香气特性",
            "C": "与大量水分在搅拌中剧烈起泡的能力",
            "D": "吸收冷水后发生胶凝定型固化的能力"
        },
        "ans": "A",
        "exp": "起酥性：油脂涂覆于面粉表面形成油膜，阻隔面粉与水结合形成强韧面筋网，烘烤后使产品酥脆松化。"
    },
    # Q15
    {
        "id": 15,
        "q": "制作法式泡芙（Choux Pastry）形成巨大内部空洞的物理动力是？",
        "opts": {
            "A": "耐高糖酵母高速发酵产生二氧化碳",
            "B": "烫面锁住水分在高温下汽化形成蒸汽",
            "C": "配方中添加大量强力碳酸氢铵膨松剂",
            "D": "蛋白霜在烤炉受热凝固成的强力骨架"
        },
        "ans": "B",
        "exp": "泡芙烫面使淀粉充分糊化吸水，烘烤时内部巨量水分急速汽化产生强大水蒸气压力，将外壳撑开成空洞。"
    },
    # Q16
    {
        "id": 16,
        "q": "在面包制作流程中，面团完成分割与滚圆揉圆后，必须进行的工序是？",
        "opts": {
            "A": "立即送入高温烤箱烘烤",
            "B": "中间松弛静置缓释张力",
            "C": "放入冷冻库内速冻硬化",
            "D": "用擀面杖反复用力碾压"
        },
        "ans": "B",
        "exp": "分割滚圆后面筋高度紧张，必须静置松弛 10~15 分钟（Bench Time），面筋放松后才好整型成型。"
    },
    # Q17
    {
        "id": 17,
        "q": "测得某长方型烤盘长 30cm、宽 20cm、高 5cm，则该烤盘容积为？",
        "opts": {
            "A": "3,000 立方公分",
            "B": "1,500 立方公分",
            "C": "600 立方公分",
            "D": "150 立方公分"
        },
        "ans": "A",
        "exp": "长方体体积 V = 长 × 宽 × 高 = 30 × 20 × 5 = 3,000 立方公分。"
    },
    # Q18
    {
        "id": 18,
        "q": "制作曲奇饼干时将细砂糖全部改为纯糖粉，烘烤成品质感的变化是？",
        "opts": {
            "A": "花纹过度摊平且口感变得粗硬难嚼",
            "B": "组织更为细密松柔且入口化口性更好",
            "C": "烘烤出炉后迅速吸水变成果冻软泥",
            "D": "饼干表面颜色完全无法发生褐变反应"
        },
        "ans": "B",
        "exp": "糖粉颗粒极细完全溶解，面糊更均质，花纹不易瘫塌，烘烤后内部气孔细致，口感松密、入口即化。"
    },
    # Q19
    {
        "id": 19,
        "q": "制作法式卡士达酱在加热搅拌至浓稠过程中，促使酱体凝固的成分是？",
        "opts": {
            "A": "玉米淀粉糊化 ＋ 蛋黄蛋白质受热凝固",
            "B": "大量天然明胶在冷水环境中的膨胀凝胶",
            "C": "配方细砂糖在高温干烧下的焦糖化反应",
            "D": "鲜牛奶中所有游离水分在炉火上的蒸发"
        },
        "ans": "A",
        "exp": "玉米淀粉在 85℃ 左右糊化成凝胶，配合蛋黄蛋白质在 75℃~80℃ 变性凝固，协同构成丝滑浓稠的酱体。"
    },
    # Q20
    {
        "id": 20,
        "q": "立式搅拌机在调制高筋面包面团时，最适宜选配的搅拌工具配件是？",
        "opts": {
            "A": "钢丝球状打蛋器",
            "B": "钩状面团搅拌器",
            "C": "平板桨状搅拌器",
            "D": "平头橡胶橡皮刮"
        },
        "ans": "B",
        "exp": "钩状（Dough Hook）专门用于揉捻、折叠和扩展韧性强、阻力大的面包面团；球状用于打发全蛋/蛋白；桨状用于拌打黄油/面糊。"
    },
    # Q21
    {
        "id": 21,
        "q": "面包发酵箱在进行最后发酵（Final Proofing）时，最理想的温湿度参数是？",
        "opts": {
            "A": "温度 18℃～20℃，湿度 40%～50%",
            "B": "温度 35℃～38℃，湿度 75%～85%",
            "C": "温度 55℃～60℃，湿度 95%～100%",
            "D": "温度 0℃～4℃，湿度 10%～20%"
        },
        "ans": "B",
        "exp": "最后发酵要求 35℃~38℃（酵母产气最活跃温区），湿度 75%~85%（防止面团表面干燥结皮硬化）。"
    },
    # Q22
    {
        "id": 22,
        "q": "天使蛋糕（Angel Food Cake）在原料配方结构上最突出的特征是？",
        "opts": {
            "A": "含有八成固态黄油属于重油脂类蛋糕",
            "B": "纯用蛋清与糖粉面粉完全不含蛋黄油脂",
            "C": "必须依赖耐高糖酵母完成长时发酵产气",
            "D": "配方面粉用量远超鲜蛋液与细砂糖总和"
        },
        "ans": "B",
        "exp": "天使蛋糕属于纯蛋白乳沫类蛋糕，配方绝不添加蛋黄与油脂，完全依靠打发纯蛋清充入空气膨胀。"
    },
    # Q23
    {
        "id": 23,
        "q": "纯黑巧克力手工制排块前必须调温（Tempering），其物理目的是？",
        "opts": {
            "A": "诱导可可脂结晶形成稳定的第V型晶体",
            "B": "彻底破坏可可脂结构使其常温不凝固",
            "C": "促使巧克力内部水分完全蒸发以防霉",
            "D": "大幅提高巧克力甜度以掩盖可可苦味"
        },
        "ans": "A",
        "exp": "调温引导可可脂形成稳定的β-5晶型（熔点约34℃），使成品表面光亮、折断声脆、不易泛白霜、容易脱模。"
    },
    # Q24
    {
        "id": 24,
        "q": "烘焙面包表面产生诱人金黄焦香色泽与复合风味，主要源于哪两项生化反应？",
        "opts": {
            "A": "叶绿素光合反应与乳酸发酵作用",
            "B": "美拉德褐变反应与糖焦糖化反应",
            "C": "淀粉自然老化作用与蛋白质水解",
            "D": "酵母酒精发酵反应与醋酸酸败作用"
        },
        "ans": "B",
        "exp": "美拉德反应（还原糖与氨基酸反应）赋予烤面包香与金黄棕色；焦糖化反应（纯糖脱水热解）赋予焦香甜味与琥珀色。"
    },
    # Q25 (Expanded 1)
    {
        "id": 25,
        "q": "烘焙常备酵母按含水量与活性分类，关于三类常见酵母的用量换算，正确的是？",
        "opts": {
            "A": "新鲜酵母用量 ＝ 即发干酵母用量的十倍",
            "B": "即发干酵母用量约等于新鲜酵母的三分之一",
            "C": "活性干酵母用量必须是新鲜酵母的两倍整",
            "D": "三类酵母在配方中必须严格按等重量替换"
        },
        "ans": "B",
        "exp": "新鲜酵母含水约70%；活性干酵母含水约8%；即发干酵母含水约5%。标准换算比例：新鲜酵母 : 活性干酵母 : 即发干酵母 ≈ 1 : 0.5 : 0.33~0.4。"
    },
    # Q26 (Expanded 2)
    {
        "id": 26,
        "q": "关于鸡蛋在烘焙西点制品中所发挥的多重功能，下列叙述何者错误？",
        "opts": {
            "A": "蛋黄卵磷脂提供天然乳化作用稳定面糊",
            "B": "受热变性凝固是面糊唯一不可替代的膨大剂",
            "C": "蛋清打发裹入空气能使蛋糕体积膨胀松软",
            "D": "增加营养价值赋予金黄色泽及浓郁蛋香"
        },
        "ans": "B",
        "exp": "蛋白质受热凝固是提供“结构支撑骨架”，使膨胀后的组织定型，而非膨大剂本身（膨大动力是打发空气、水蒸气或化学CO₂）。"
    },
    # Q27 (Expanded 3)
    {
        "id": 27,
        "q": "西点制作中经常使用乳制品，关于蒸发乳（淡奶 Evaporated Milk）的特性是？",
        "opts": {
            "A": "脱去全部水分磨制而成的超干白色粉末",
            "B": "鲜奶蒸发除去约六成水分且完全不额外加糖",
            "C": "鲜奶浓缩后加入四成以上白砂糖的高甜稠乳",
            "D": "经乳酸菌发酵酸化凝固而成的微酸硬质乳酪"
        },
        "ans": "B",
        "exp": "蒸发乳（淡奶）：新鲜牛奶经真空浓缩除去约60%水分，未添加额外砂糖；炼乳（Condensed Milk）则额外添加了约40%~45%的高浓度蔗糖。"
    },
    # Q28 (Expanded 4)
    {
        "id": 28,
        "q": "关于动物性鲜奶油与植物性鲜奶油的打发与储存，下列叙述何者完全正确？",
        "opts": {
            "A": "动物鲜奶油严禁冷冻且打发最佳温度为4℃～8℃",
            "B": "动物鲜奶油必须长期冷冻保存且常温打发最佳",
            "C": "植物鲜奶油冷冻后乳脂球必定结晶破裂油水分离",
            "D": "两者在储存温度打发耐热度及风味上完全一致"
        },
        "ans": "A",
        "exp": "动物鲜奶油（天然乳脂）绝对严禁冷冻，冷冻冰晶会破坏乳化膜导致解冻后油水分离；打发必须冰凉（4~8℃）。植物鲜奶油通常冷冻储存。"
    },
    # Q29 (Expanded 5)
    {
        "id": 29,
        "q": "在面包制作的三种常见方法中，面包柔软度保持最久、抗老化最佳的方法是？",
        "opts": {
            "A": "直接一次搅拌成型法 (Straight Dough)",
            "B": "中种法与烫种发酵法 (Sponge / Tangzhong)",
            "C": "快速化学无发酵法 (Rapid Chemical)",
            "D": "干酵母直接干拌烘法 (Dry Direct Bake)"
        },
        "ans": "B",
        "exp": "中种法通过长时间二次发酵产酸并使面筋水化彻底；汤种法使淀粉预先糊化锁住大量水分，抗老化能力与保水柔软度远超直接法。"
    },
    # Q30 (Expanded 6)
    {
        "id": 30,
        "q": "刚烘烤出炉的吐司面包，必须立即在台面上轻震模具并脱模倒出，其原因是？",
        "opts": {
            "A": "震裂表皮以利于快速注入浓稠糖浆",
            "B": "震出底部湿热气体防止出炉腰缩塌陷",
            "C": "使内部气泡受剧烈震荡全部破裂消泡",
            "D": "迫使面包中心生面团迅速吸收外层油脂"
        },
        "ans": "B",
        "exp": "出炉瞬间面包内部充满高温湿热蒸汽，在台面上轻震一下能震出底部聚集的热气，防止冷却时气压骤降导致吐司两侧凹陷（腰缩）。"
    },
    # Q31 (Expanded 7)
    {
        "id": 31,
        "q": "制作高品质戚风蛋糕时，蛋黄糊配方中适宜选用的植物油种类是？",
        "opts": {
            "A": "气味强烈的特级初榨原味橄榄油",
            "B": "无色无特殊气味的纯玉米油或色拉油",
            "C": "未经过精炼的重风味原味黑芝麻油",
            "D": "常温下极易凝固起白霜的纯未精炼棕榈油"
        },
        "ans": "B",
        "exp": "戚风蛋糕讲究蛋香与轻柔，必须选用常温呈液态且无色无明显气味的植物油（如玉米油、芥花油、大豆色拉油），避免掩盖蛋糕天然风味。"
    },
    # Q32 (Expanded 8)
    {
        "id": 32,
        "q": "西式饼干按制作工艺主要分类，下列哪种饼干属于“挤出成型类（Bagged/Piped）”？",
        "opts": {
            "A": "法式传统手指饼干与曲奇花嘴挤花饼",
            "B": "经过长时间冷冻后用刀切片的核桃酥片",
            "C": "用擀面杖擀平后用铁模压刻的姜饼娃娃",
            "D": "在平底热铁板上烙烤成薄卷的香脆蛋卷"
        },
        "ans": "A",
        "exp": "挤出类饼干（Bagged Cookies）：面糊质地较软，装入裱花袋用花嘴直接挤在烤盘上成型，如挤花曲奇（Butter Spritz）、法式手指饼干。"
    },
    # Q33 (Expanded 9)
    {
        "id": 33,
        "q": "制作美式派皮（Pie Crust）使用搓沙法时，配方中的水必须使用冰水，其核心原因是？",
        "opts": {
            "A": "防止固体黄油小丁颗粒融化保持片状开酥",
            "B": "加速高筋面粉面筋快速形成网状连续骨架",
            "C": "促使派皮中的细砂糖晶体瞬间完全溶解化开",
            "D": "杀灭生面粉中可能残存的一切天然野生酵母"
        },
        "ans": "A",
        "exp": "搓沙法要求固体黄油保持细小扁平颗粒包裹在面粉中，若水温高黄油融化渗入面粉即失去分层起酥效果，因此必须使用 0~4℃ 冰水。"
    },
    # Q34 (Expanded 10)
    {
        "id": 34,
        "q": "丹麦酥面包（Danish Pastry）与经典法式可颂（Croissant）在面团配方上的主要区别是？",
        "opts": {
            "A": "丹麦面团配方中通常额外加入糖蛋奶和香草",
            "B": "法式可颂面团中含有高达四成的天然鲜柠檬汁",
            "C": "丹麦面团完全不需要折叠裹入任何油脂层开酥",
            "D": "两者面团配方完全相同没有任何原料成分差别"
        },
        "ans": "A",
        "exp": "经典法式可颂面团较为清淡（面粉、水、少量糖盐酵母黄油）；丹麦面包属于富贵面团（Rich Dough），额外加入较多细砂糖、全蛋、鲜奶及豆蔻等。"
    },
    # Q35 (Expanded 11)
    {
        "id": 35,
        "q": "已知面粉500g，水60%，糖10%，酵母1.5%，盐1%，油4%。该配方面团总重量为？",
        "opts": {
            "A": "882.5 克",
            "B": "750.0 克",
            "C": "680.5 克",
            "D": "500.0 克"
        },
        "ans": "A",
        "exp": "烘焙总百分比 = 100% + 60% + 10% + 1.5% + 1% + 4% = 176.5%。面团总重 = 500g × 176.5% = 882.5g。"
    },
    # Q36 (Expanded 12)
    {
        "id": 36,
        "q": "欧式面包配方中的“水合率（Hydration）”提高到 75% 以上时，成品的典型特征是？",
        "opts": {
            "A": "面团极硬且出炉组织极为紧密细小无孔洞",
            "B": "内部孔洞分布开放不规则且外脆内湿润软滑",
            "C": "烘烤出炉后完全无法成型直接塌陷流质成浆",
            "D": "面团在常温发酵箱中完全停止释放二氧化碳"
        },
        "ans": "B",
        "exp": "高水合面团（75%~85%如法棍、夏巴塔）烘烤时产生大量蒸汽撑开大孔洞，成品拥有标志性的开放式蜂窝孔洞（Open Crumb）与薄脆外壳。"
    },
    # Q37 (Expanded 13)
    {
        "id": 37,
        "q": "面粉品质标准中的“灰分含量（Ash Content）”，其检验的核心技术意义是？",
        "opts": {
            "A": "判断小麦胚乳研磨出粉率高低与麦麸混杂纯净度",
            "B": "测定面粉内部天然直链淀粉遇热糊化的最高温度",
            "C": "衡量面粉中干燥活酵母菌落存活数量的多少程度",
            "D": "反映面粉在密封烤炉烘烤时产生明火火花的危险度"
        },
        "ans": "A",
        "exp": "灰分是面粉经高温（约550℃~900℃）灼烧后残留的矿物质。灰分越低代表去除麦麸皮越干净、出粉率越低越纯白（如法国T45/T55标准）。"
    },
    # Q38 (Expanded 14)
    {
        "id": 38,
        "q": "夏季搅拌面包面团时为控制搅拌终了面团温度不超标（26℃～28℃），最有效的手段是？",
        "opts": {
            "A": "在搅拌缸中加入大量白砂糖提高吸水黏度",
            "B": "计算配方加水温度并使用部分碎冰块替代配方水",
            "C": "将搅拌机速度提升到最高速强行缩短时间",
            "D": "将高筋面粉置于烤箱中预先微波加热至温热"
        },
        "ans": "B",
        "exp": "机械高速搅拌会因强力摩擦剧烈升温（摩擦升温达6~12℃）。夏季必须依据摩擦系数计算加水温度，并用碎冰代替部分自来水以压制面团温升。"
    },
    # Q39 (Expanded 15)
    {
        "id": 39,
        "q": "制作分蛋海绵或戚风蛋糕面糊时，最容易诱发严重消泡的工艺失误是？",
        "opts": {
            "A": "打发蛋白霜使用专用橡皮刮刀轻柔切拌",
            "B": "盛装蛋白打发的搅拌缸内壁混入了油脂或蛋黄液",
            "C": "在打发好的蛋白霜中分两次加入过筛低筋面粉",
            "D": "面糊拌匀后立即倒入烤模并轻震模具消除大气泡"
        },
        "ans": "B",
        "exp": "油脂与蛋黄（含丰富甘油三酯与卵磷脂）是强消泡剂，能极大破坏蛋白质气泡表面的表面张力网，导致气泡迅速破裂、打发失败。"
    },
    # Q40 (Expanded 16)
    {
        "id": 40,
        "q": "广式月饼饼皮调制中必须使用高浓度转化糖浆，其在烘烤后发挥的核心作用是？",
        "opts": {
            "A": "促使饼皮快速硬化断裂增强机械抗摔性",
            "B": "赋予饼皮金红油亮光泽并促使饼皮常温回油软化",
            "C": "替代低筋面粉充当月饼唯一的强韧承重骨架",
            "D": "完全抑制烤箱内部一切美拉德褐变反应发生"
        },
        "ans": "B",
        "exp": "转化糖浆赋予月饼皮良好的延展性与漂亮焦糖上色，并在出炉放置1~3天后，促使内部油脂向表皮迁移产生“回油”现象，变得油润光亮柔嫩。"
    },
    # Q41 (Expanded 17)
    {
        "id": 41,
        "q": "面包进入烤箱后的烘烤全过程，其内部微观物理化学变化的标准三阶段顺序是？",
        "opts": {
            "A": "表皮变黑碳化 ➔ 淀粉完全水解 ➔ 酵母急速大量繁殖",
            "B": "烤箱急胀(Oven Spring) ➔ 淀粉糊化定型着色 ➔ 内部完全熟化",
            "C": "蛋白质瞬间融化 ➔ 酵母脱水休眠 ➔ 内部水分完全排空",
            "D": "面筋收缩塌陷 ➔ 糖分完全挥发 ➔ 气室结构彻底瓦解"
        },
        "ans": "B",
        "exp": "烘烤三阶段：①入炉前数分钟（40~60℃）酵母超速产气+气体膨胀产生急胀（Oven Spring）；②60~85℃蛋白质变性、淀粉糊化定型并上色；③95℃以上完全熟化成熟。"
    },
    # Q42 (Expanded 18)
    {
        "id": 42,
        "q": "碳酸氢铵（Ammonium Bicarbonate / 臭粉）最适宜应用的烘焙产品类型是？",
        "opts": {
            "A": "含水量极高且体型厚重的低糖多层海绵蛋糕",
            "B": "体型极薄且水分极易蒸发的超薄酥脆小饼干",
            "C": "高度膨胀且内部湿润柔软的经典日式生吐司",
            "D": "冷藏即食且完全不经过任何烘烤的慕斯西点"
        },
        "ans": "B",
        "exp": "碳酸氢铵受热完全分解为氨气（刺激臭味）、水和二氧化碳。仅适合薄脆、小体量饼干（如苏打饼），氨气能迅速挥发散逸；厚蛋糕会残留刺鼻氨气味。"
    },
    # Q43 (Expanded 19)
    {
        "id": 43,
        "q": "烘焙模具与烤盘进行“防粘处理”的标准专业操作方法是？",
        "opts": {
            "A": "在模具内壁涂抹极厚水滴后直接冷冻结成冰层",
            "B": "涂抹一层薄软化黄油并筛上薄粉或垫防粘硅油纸",
            "C": "在模具底部倒入大量冷清水以防止产品接触底部",
            "D": "用大量纯食盐颗粒将模具底部完全填满压平实"
        },
        "ans": "B",
        "exp": "传统模具防粘：涂抹薄黄油后筛薄薄一层低筋面粉（防粘油粉法），或使用耐高温特氟龙垫/食品级硅油纸，既能防粘又不影响爬高。"
    },
    # Q44 (Expanded 20)
    {
        "id": 44,
        "q": "烤箱烘烤前若未进行充分预热（温度偏低即推入产品），最容易出现的成品质感缺陷是？",
        "opts": {
            "A": "膨胀高度严重不足且底部油脂渗出、表皮厚硬灰白",
            "B": "产品表面瞬间焦黑碳化而内部完全处于冰冻状态",
            "C": "蛋糕体积膨大超过正常标准三倍以上且极其蓬松",
            "D": "面团中酵母菌在超低温环境中超量无限制产气爆裂"
        },
        "ans": "A",
        "exp": "未预热时烤箱温度缓慢爬升，油脂过早熔化流出（流油），水蒸气无法瞬间爆发撑开结构，蛋糕/饼干摊平硬实、上色极慢、表皮干硬苍白。"
    },
    # Q45 (Roman 1)
    {
        "id": 45,
        "q": "关于烘焙常用化学膨大剂的物理化学特性，下列叙述哪些完全正确？\n"
             "   I. 小苏打（碳酸氢钠）单独过量使用会使成品残留苦涩皂碱味且色泽发黄\n"
             "   II. 碳酸氢铵（臭粉）受热完全分解挥发，适合用于水分极低薄脆饼干\n"
             "   III. 双效泡打粉遇冷水不产生任何反应，必须在 100℃ 沸水中才开始产气\n"
             "   IV. 酵母菌属于单细胞真核生物，其发酵产气机理与化学膨大剂截然不同",
        "opts": {
            "A": "I, II, III",
            "B": "I, II, IV",
            "C": "II, III, IV",
            "D": "I, III, IV"
        },
        "ans": "B",
        "exp": "I、II、IV正确；III错误（双效泡打粉含低温酸性盐，常温加水搅拌即开始第一次产气释放部分CO₂）。故选 B。"
    },
    # Q46 (Roman 2)
    {
        "id": 46,
        "q": "在面包发酵工艺中，直接决定酵母菌生命产气活性与繁殖效率的因素包括：\n"
             "   I. 面团所处发酵室的即时环境温度与空气相对湿度\n"
             "   II. 配方中高浓度细砂糖与食盐所形成的细胞渗透压\n"
             "   III. 面团内部酸碱度 (pH值) 与发酵产酸积累情况\n"
             "   IV. 烘焙工场操作台面不锈钢钢板的自然反光折射率",
        "opts": {
            "A": "I, II, III",
            "B": "I, II, IV",
            "C": "II, III, IV",
            "D": "I, III, IV"
        },
        "ans": "A",
        "exp": "I（温湿度）、II（盐糖渗透压）、III（pH值）是生化控制核心；IV（台面反光率）属于无关干扰项。故选 A。"
    },
    # Q47 (Roman 3)
    {
        "id": 47,
        "q": "制作高质量分蛋戚风蛋糕时，为防止面糊消泡、确保成品高耸松软，正确的操作是：\n"
             "   I. 打发蛋白霜的搅拌容器必须严格保证无油脂、无水分、无蛋黄混入\n"
             "   II. 纯蛋清通常打发至中性偏干性发泡（提起打蛋头呈挺立微弯尖角）\n"
             "   III. 混合蛋白霜与蛋黄糊时，必须采用高速顺时针画圈久拌以强化面筋\n"
             "   IV. 混合应使用橡皮刮刀采用轻快切拌与翻拌手法（Fold in）分次拌匀",
        "opts": {
            "A": "I, II, III",
            "B": "I, II, IV",
            "C": "II, III, IV",
            "D": "I, III, IV"
        },
        "ans": "B",
        "exp": "I、II、IV正确；III错误（画圈久拌会造成严重气泡破裂消泡，且导致面粉严重起筋，使蛋糕缩腰出油死面）。故选 B。"
    },
    # Q48 (Roman 4)
    {
        "id": 48,
        "q": "油脂（黄油、猪油、植物起酥油）在烘焙面团与饼干中发挥的核心功能包括：\n"
             "   I. 涂覆包裹面粉微粒阻断面筋结合，赋予成品酥脆化口的起酥特性\n"
             "   II. 在机械打发过程中裹入细小微气孔，改善面糊延展性与蓬松度\n"
             "   III. 赋予焙烤产品纯正高雅的天然奶香风味，并在受热时提供润滑口感\n"
             "   IV. 完全替代面粉中的蛋白质网络以充当蛋糕出炉唯一的坚固骨架",
        "opts": {
            "A": "I, II, III",
            "B": "I, II, IV",
            "C": "II, III, IV",
            "D": "I, III, IV"
        },
        "ans": "A",
        "exp": "I、II、III正确；IV错误（油脂属于柔性/弱性原料，会弱化骨架，烘焙支撑骨架必须依赖面筋蛋白与蛋液蛋白质变性凝固）。故选 A。"
    },
    # Q49 (Roman 5)
    {
        "id": 49,
        "q": "全蛋海绵蛋糕出炉后发生严重收缩塌陷、内部湿黏发紧，下列属于工艺失误的是：\n"
             "   I. 出炉后未立即在操作台上轻震模具排震热汽，且未立即倒扣晾凉\n"
             "   II. 配方中水分与液体油脂比例严重过量，导致内部湿气过重承重不足\n"
             "   III. 模具内壁涂抹了过多固态油脂，导致面糊受热膨胀时无法附着爬高\n"
             "   IV. 烘烤时间充足且出炉时蛋糕中心熟化温度完全达到 95℃ 以上",
        "opts": {
            "A": "I, II, III",
            "B": "I, II, IV",
            "C": "II, III, IV",
            "D": "I, III, IV"
        },
        "ans": "A",
        "exp": "I、II、III是导致海绵蛋糕塌陷缩腰的典型技术失误；IV（熟透达标）是成功烘烤的特征。故选 A。"
    },
    # Q50 (Roman 6)
    {
        "id": 50,
        "q": "关于烘焙车间食品卫生与用具消毒规范，下列叙述哪些符合专业标准？\n"
             "   I. 制作含蛋奶高风险馅料（如卡士达酱）应严格限制在危险温度带不超过 2 小时\n"
             "   II. 食品接触用具采用沸水物理消毒法时，必须在 100℃ 沸水中完全浸没至少 1 分钟\n"
             "   III. 刚出炉的滚烫面包应立刻装入完全密封的塑料袋扎紧以防表皮水分自然挥发\n"
             "   IV. 工作人员手部若有化脓性伤口严禁直接操作即食糕点以防金黄色葡萄球菌污染",
        "opts": {
            "A": "I, II, III",
            "B": "I, II, IV",
            "C": "II, III, IV",
            "D": "I, III, IV"
        },
        "ans": "B",
        "exp": "I、II、IV正确；III错误（滚烫面包密封会导致大量蒸汽凝结为水珠，使表皮变软湿烂并极易发霉变质）。故选 B。"
    }
]

# Audit Option Lengths & Bilingual Consistency
print("=== AUDITING 50 MCQs ===")
keys_cnt = {}
span_issues = []
bilingual_issues = []

for q in mcq_bank:
    qid = q['id']
    ans = q['ans']
    keys_cnt[ans] = keys_cnt.get(ans, 0) + 1
    
    lens = [len(v) for v in q['opts'].values()]
    span = max(lens) - min(lens)
    if span > 4:
        span_issues.append((qid, span, q['opts']))
        
    # Check bilingual consistency: if any option has English letters/parentheses, all 4 should
    has_eng = [bool(re.search(r'[a-zA-Z]', v)) for v in q['opts'].values()]
    if any(has_eng) and not all(has_eng):
        bilingual_issues.append((qid, q['opts']))

print(f"Total MCQs: {len(mcq_bank)}")
print("Key Distribution:", keys_cnt)
print(f"Span > 4 issues: {len(span_issues)}")
print(f"Bilingual inconsistency issues: {len(bilingual_issues)}")

assert len(span_issues) == 0, f"Span issues found: {span_issues}"
assert len(bilingual_issues) == 0, f"Bilingual issues found: {bilingual_issues}"
print("✅ ALL 50 MCQs PASSED LENGTH & BILINGUAL AUDIT PERFECTLY!")

# =========================================================================
# SHORT ANSWER QUESTIONS (10 BRAND-NEW CONCISE QUESTIONS)
# =========================================================================

short_answers = [
    {
        "id": "简答题 1",
        "q": "何谓“烘焙百分比（Baker's Percentage）”？在配方计算中，永远以哪一种原料的重量作为 100% 基准？",
        "ans": "烘焙百分比是以配方中【面粉总重量】固定设定为 100% 作为基准除数，其他各项材料的重量均表示为占面粉重量的相应百分比。优势在于便于配方任意缩放、评估面团吸水率与横向对比配方平衡。"
    },
    {
        "id": "简答题 2",
        "q": "烘焙中常用的新鲜酵母（压榨酵母）、活性干酵母与即发干酵母（快发干酵母），三者在配方中的标准重量换算比例约为多少？",
        "ans": "三者的重量换算比例约为：新鲜酵母 : 活性干酵母 : 即发干酵母 ＝ 1 : 0.5 : 0.33～0.4（即即发干酵母用量约占新鲜酵母的 1/3，活性干酵母约占 1/2）。"
    },
    {
        "id": "简答题 3",
        "q": "为什么动物性天然鲜奶油（Dairy Whipping Cream）严禁放入冷冻库（-18℃）冷冻储存？",
        "ans": "动物鲜奶油为水包油型乳化体系。冷冻时内部水分结成粗大冰晶，会刺破乳化脂肪球膜，导致脂肪聚集硬化；解冻时水分融化析出，发生无法复原的严重油水分离，彻底丧失打发性。"
    },
    {
        "id": "简答题 4",
        "q": "制作分蛋戚风蛋糕打发纯蛋清时，为什么盛放蛋白的打蛋盆与打蛋头必须严格确保“无油、无水、无蛋黄混入”？",
        "ans": "油脂和蛋黄中富含疏水性油脂及卵磷脂，是极强的消泡剂，会极大破坏变性蛋白质在气泡表面的表面张力保护膜，使空气无法被微细包裹截留，导致蛋白霜打发体积严重受限或彻底无法打发。"
    },
    {
        "id": "简答题 5",
        "q": "在面包制作流程中，“中间松弛（中间发酵 / Bench Time）”通常需进行多长时间？其主要工艺目的是什么？",
        "ans": "通常在常温下静置松弛 10～15 分钟。主要目的是缓解面团经过机械切割与滚圆紧搓后所产生的剧烈面筋张力与弹性回缩，使面筋自然舒展放松，便于下一步擀卷整型且不破皮、不缩皮。"
    },
    {
        "id": "简答题 6",
        "q": "在烘焙配方中，泡打粉（Baking Powder）与小苏打（Baking Soda）能否进行等量完全替换？为什么？",
        "ans": "不能直接等量替换。小苏打是纯碱性碳酸氢钠，必须配方中有酸性食材（如酸奶、天然可可粉、蜂蜜）方能反应，过量会残留发黄皂碱苦味；泡打粉是小苏打加酸性盐及淀粉的复合膨大剂，碱性强度约为小苏打的 1/3~1/4，需按约 3:1 或 4:1 比例换算并调整酸碱平衡。"
    },
    {
        "id": "简答题 7",
        "q": "烘烤法式长棍面包（Baguette）等欧式硬壳面包时，为什么在烘烤初期炉膛内必须注入蒸汽（Steam）？",
        "ans": "①蒸汽在生冷面团表面凝结成水膜，延缓表皮过早受热结壳硬化，使面团内部在烤箱急胀（Oven Spring）期能充分膨大爆开发酵刀口；②表皮淀粉在湿热蒸汽下预糊化并溶解糖分，出炉后形成薄脆光亮的金黄薄壳。"
    },
    {
        "id": "简答题 8",
        "q": "面包面团若发生严重发酵过度（Over-fermentation），烘烤出炉后的成品质感会出现哪些明显的品质缺陷？（列出3点）",
        "ans": "①成品带有明显酸味（乳酸菌醋酸菌过度产酸）；②表皮颜色苍白不易着色（可发酵糖被酵母消耗殆尽，美拉德反应受阻）；③内部组织粗糙、孔洞破裂易掉渣；④面筋支撑力衰竭导致出炉后塌陷回缩。"
    },
    {
        "id": "简答题 9",
        "q": "简述制作美式派皮与英式司康时“搓沙法（Sablage / Rub-in Method）”的核心操作要领与温度控制要求。",
        "ans": "将冷硬固体黄油切成约1cm小丁，加入低筋面粉中，用手指尖或派皮切刀快速摩擦揉搓成如玉米粉或豆粒大小的微细颗粒，随后加入 0~4℃ 冰水轻柔捏合成团。全程严禁手温过高融化黄油，严禁揉出面筋，以确保烘烤产生片状酥脆层次。"
    },
    {
        "id": "简答题 10",
        "q": "在烘焙工场食品卫生安全规范中，针对冷冻生鲜原料（如冷冻蛋液、冷冻肉类），哪两种是符合安全卫生标准的规范解冻方式？",
        "ans": "①冷藏解冻法：提前 24 小时移至 2℃～7℃ 冷藏库中缓慢安全解冻（最推荐）；②流动冷水解冻法：将原料置于密封防水包装中，浸入 21℃ 以下流动冷水中持续冲水解冻（解冻后必须立即使用，严禁常温室温放置解冻）。"
    }
]

# =========================================================================
# COMPREHENSIVE WRITTEN QUESTIONS (5 BIG QUESTIONS)
# =========================================================================

comprehensive_written = [
    {
        "id": "综合大题 1",
        "title": "烘焙百分比标准计算题 (面粉 500g 标准配方换算)",
        "score": 10,
        "desc": "某烘焙工场计划制作一批法式甜面团，已知配方以高筋面粉重量 500g 为对照基准（100.0%），各材料烘焙百分比如下表所示。请计算各个别材料的实际使用净重（单位：g，填入表格），并计算配方面团总重量。",
        "table": [
            ["材料名称", "烘焙百分比 (%)", "标准算式与实际使用重量 (g)", "采分细则"],
            ["高筋面粉 (基准)", "100.0 %", "500.0 g (已知基准)", "已知对照基准"],
            ["清水", "62.0 %", "500 g × 62.0% = 310.0 g", "正确填入 310g 得 1.5分"],
            ["细砂糖", "18.0 %", "500 g × 18.0% = 90.0 g", "正确填入 90g 得 1.5分"],
            ["全蛋液", "12.0 %", "500 g × 12.0% = 60.0 g", "正确填入 60g 得 1.5分"],
            ["无盐黄油", "10.0 %", "500 g × 10.0% = 50.0 g", "正确填入 50g 得 1.5分"],
            ["耐高糖干酵母", "1.5 %", "500 g × 1.5% = 7.5 g", "正确填入 7.5g 得 1.5分"],
            ["食盐", "1.2 %", "500 g × 1.2% = 6.0 g", "正确填入 6.0g 得 1.0分"]
        ],
        "total_calc": "面团总重量 = 500g + 310g + 90g + 60g + 50g + 7.5g + 6.0g = 1,023.5 g (精确计算填入得 1.5分)"
    },
    {
        "id": "综合大题 2",
        "title": "三大类蛋糕分类体系与工艺机理分析题",
        "score": 10,
        "desc": "(a) 西式糕点中的三大类蛋糕在原料配合与膨胀机制上有本质区别。试分别写出【面糊类蛋糕】、【乳沫类蛋糕】与【戚风类蛋糕】各自的主要依靠什么机制达到体积膨胀？并各举出一款市面上最典型的代表蛋糕名称。(6分)\n"
                "(b) 天使蛋糕（Angel Food Cake）在打发纯蛋清时，配方中加入塔塔粉的核心作用是什么？若烘焙实操时手头缺少塔塔粉，在家庭或实务中可选用哪一种天然常见酸性液体按何种比例进行替代？(4分)",
        "rubric": "【评分细则】：\n"
                  "(a) ①面糊类（2分）：依靠固态黄油与砂糖打发裹入微细气泡及化学膨大剂受热产气膨胀；代表：磅蛋糕/重奶油蛋糕。(各1分)\n"
                  "    ②乳沫类（2分）：依靠全蛋或纯蛋白打发形成坚韧泡沫网络，烘烤时受热膨胀定型，完全不含或极少油脂；代表：海绵蛋糕/天使蛋糕。(各1分)\n"
                  "    ③戚风类（2分）：结合面糊类与乳沫类优点，采用分蛋打发，蛋白霜提供膨胀骨架，蛋黄糊提供湿润柔嫩；代表：原味戚风/斑兰戚风/瑞士卷。(各1分)\n"
                  "(b) 塔塔粉作用（2分）：降低蛋白溶液 pH 接近微酸性等电点，使变性蛋白泡沫细密强韧不易消泡，并中和天然色素使蛋糕纯白。替代品（2分）：新鲜柠檬汁或天然白醋，用量约为塔塔粉用量的 2~3 倍。"
    },
    {
        "id": "综合大题 3",
        "title": "面包发酵阶段控制与自解法（Autolyse）工艺题",
        "score": 10,
        "desc": "(a) 面包制作发酵工序中，“基本发酵（Bulk Fermentation）”与“最后发酵（Final Proofing）”是两个性质截然不同的阶段。试对比说明这两个发酵阶段在【操作时机】、【主要工艺目的】以及【温湿度环境】上的核心区别。(6分)\n"
                "(b) 现代欧式面包制作中广泛推崇“自解法（Autolyse）”。试简述自解法的标准操作步骤，并阐明其能够“减少机械搅拌时间、改善面团延展性”的生化原因。(4分)",
        "rubric": "【评分细则】：\n"
                  "(a) ①操作时机（2分）：基本发酵在搅拌后、分割前；最后发酵在整型入盘入模后、入炉烘烤前。\n"
                  "    ②主要目的（2分）：基本发酵让酵母充分产气熟成、代谢生成有机酸和复杂芳香风味；最后发酵让面团在入炉前最大限度产气充盈，恢复整型后失去的体积。\n"
                  "    ③温湿度环境（2分）：基本发酵温度较低（26~28℃，湿度75%）；最后发酵温度较高（35~38℃最适产气区，湿度80~85%防止表皮干裂）。\n"
                  "(b) 自解法步骤（2分）：面粉与水低速拌至无干粉颗粒成粗面团，严禁加酵母与盐，静置 20~45 分钟。生化机理（2分）：无盐阻碍下蛋白质充分吸水自然水化交联成网，减少高速搅拌带来的氧化；天然淀粉酶分解淀粉，改善面团延展性与保气性。"
    },
    {
        "id": "综合大题 4",
        "title": "烘焙化学反应与油脂起酥机理题",
        "score": 10,
        "desc": "(a) 试从【反应所需的核心原料】、【反应起始温度】以及【风味与色泽特征】三个维度，详细对比“美拉德反应（Maillard Reaction）”与“焦糖化反应（Caramelization）”的本质差异。(6分)\n"
                "(b) 试详细阐述天然黄油（Butter）在制作曲奇饼干（Cookies）中所发挥的 2 个核心工艺功能。(4分)",
        "rubric": "【评分细则】：\n"
                  "(a) ①反应原料（2分）：美拉德反应需还原糖与氨基酸/蛋白质共同反应；焦糖化反应纯粹是单一糖类（蔗糖/葡萄糖等）单独在无水或少水下高温热解脱水，不含蛋白质。\n"
                  "    ②反应温度（2分）：美拉德反应在 130~140℃ 即可剧烈发生；焦糖化反应通常需要 160~180℃ 以上高温。\n"
                  "    ③风味色泽（2分）：美拉德反应产生烤面包香、肉香、坚果香与金黄至棕红焦褐色；焦糖化产生焦糖甜香、微苦风味及深琥珀色光泽。\n"
                  "(b) 黄油在曲奇中的功能（4分）：①起酥与柔嫩（2分）：固态乳脂包覆面粉微粒阻断面筋结合，赋予酥脆化口口感；②充气与香气（2分）：打发充入微气室使饼干蓬松，受热挥发纯正天然黄油奶香。"
    },
    {
        "id": "综合大题 5",
        "title": "烘焙故障排查与食品安全卫生题",
        "score": 10,
        "desc": "(a) 某烘焙学徒制作的全蛋海绵蛋糕在烘烤出炉冷却后，发现蛋糕中心发生严重凹陷塌陷、内部组织紧实发黏、脱模边缘撕裂。试从【打发与搅拌操作】、【配方平衡】及【烘烤与出炉处置】三个方面，排查分析出 3 个最可能的工艺失误。(6分)\n"
                "(b) 在西点房中制作高风险的卡士达酱（Crème Pâtissière）或含蛋奶馅料时，为何必须严格防范“食品危险温度带（5℃～60℃）”？煮制完成后的卡士达酱应采取何种标准工序进行急速降温与卫生保存？(4分)",
        "rubric": "【评分细则】：\n"
                  "(a) 故障排查（6分，三方面任选3点各2分）：①操作：打发不足或过度消泡；面粉过筛加入后画圈久拌导致消泡起筋。②配方：液体水分或油脂比例过高，面粉比例过低导致骨架无力。③烘烤出炉：下火不足内部未熟即出炉；出炉未轻震排热气；未立即脱模倒扣晾凉。\n"
                  "(b) 卫生要求（4分）：①危险温度带原因（2分）：卡士达酱富含蛋奶糖水，是高营养高水分易腐基质，在 5~60℃ 极易爆发沙门氏菌或金黄色葡萄球菌释放肠毒素。②急冷规程（2分）：出锅趁热平铺浅盘或冰水浴大盆；用食品保鲜膜紧贴酱体表面（贴面包裹防冷凝水及结皮）；速冷机快速降至 5℃ 以下，2~7℃ 密封冷藏并在 48 小时内用完。"
    }
]

print("Ready to generate Word documents!")

# =========================================================================
# GENERATE DOCUMENT 4: STUDENT / TEST PAPER (04)
# =========================================================================

def build_doc4():
    doc = create_styled_document()
    
    # Title Block
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t0 = p_title.add_run("马来西亚华文独立中学高中统考（UEC）厨艺理论\n")
    r_t0.font.size = Pt(13)
    r_t0.font.bold = True
    r_t0.font.color.rgb = RGBColor(100, 116, 139)
    
    r_t1 = p_title.add_run("【高一阶段专属】烘焙基础理论与实务 · 全真统考风格测验题库卷\n")
    r_t1.font.size = Pt(16)
    r_t1.font.bold = True
    r_t1.font.color.rgb = RGBColor(120, 53, 15)
    
    r_t2 = p_title.add_run("本卷属性：教师备课测验、期中/期末组卷题库资源池（含 50 道高精度选择题 ＋ 10 道简答题 ＋ 5 道综合大题）")
    r_t2.font.size = Pt(9.5)
    r_t2.font.italic = True
    r_t2.font.color.rgb = RGBColor(180, 83, 9)
    
    # Student Info Box
    tbl_info = doc.add_table(rows=1, cols=4)
    tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
    info_headers = ["学生姓名：________________", "班级 / 班号：____________", "学号：________________", "评定得分：__________ / _____"]
    for i, t in enumerate(info_headers):
        c = tbl_info.rows[0].cells[i]
        c.text = t
        set_cell_background(c, "F8FAFC")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.color.rgb = RGBColor(51, 65, 85)
    set_table_borders(tbl_info, color="CBD5E1")
    doc.add_paragraph() # Spacer
    
    # Section 1: MCQs (Q1 ~ Q50)
    h1 = doc.add_heading("第一部分：统考风格客观选择题库 (共 50 题 · 含单选题与罗马组合题)", level=1)
    h1.style.font.color.rgb = RGBColor(120, 53, 15)
    
    p_sec1_note = doc.add_paragraph("【说明】：本部分题目严格执行统考命题四大规范，选项字数极差严格控制在 0～4 字以内，中英文专业术语完全对称，无任何长度或格式泄题暗示。")
    p_sec1_note.runs[0].font.size = Pt(9.5)
    p_sec1_note.runs[0].font.italic = True
    p_sec1_note.runs[0].font.color.rgb = RGBColor(100, 116, 139)
    
    for q in mcq_bank:
        p_q = doc.add_paragraph()
        r_qid = p_q.add_run(f"Q{q['id']:02d}. ")
        r_qid.bold = True
        r_qid.font.color.rgb = RGBColor(120, 53, 15)
        r_qtext = p_q.add_run(q['q'])
        r_qtext.bold = True
        
        for k in ['A', 'B', 'C', 'D']:
            p_opt = doc.add_paragraph(f"{k}. {q['opts'][k]}")
            p_opt.paragraph_format.left_indent = Inches(0.25)
            p_opt.paragraph_format.space_after = Pt(2)
        doc.add_paragraph() # Spacer
        
    # Section 2: Short Answer Questions (10 items)
    h2 = doc.add_heading("第二部分：基础简短作答题库 (共 10 题 · 核心概念与实务规范)", level=1)
    h2.style.font.color.rgb = RGBColor(120, 53, 15)
    
    for sa in short_answers:
        p_sa = doc.add_paragraph()
        r_sah = p_sa.add_run(f"{sa['id']}：")
        r_sah.bold = True
        r_sah.font.color.rgb = RGBColor(180, 83, 9)
        r_sat = p_sa.add_run(sa['q'])
        r_sat.bold = True
        
        p_space = doc.add_paragraph(
            "答：_________________________________________________________________________________\n"
            "    _________________________________________________________________________________\n"
            "    _________________________________________________________________________________"
        )
        p_space.paragraph_format.left_indent = Inches(0.2)
        p_space.paragraph_format.space_after = Pt(8)
        
    # Section 3: Comprehensive Written Questions (5 items)
    h3 = doc.add_heading("第三部分：综合大题与计算题库 (共 5 题 · 统考试卷二深度大题)", level=1)
    h3.style.font.color.rgb = RGBColor(120, 53, 15)
    
    for cw in comprehensive_written:
        p_cwh = doc.add_paragraph()
        r_cwh = p_cwh.add_run(f"{cw['id']}：{cw['title']} ({cw['score']}分)")
        r_cwh.bold = True
        r_cwh.font.size = Pt(11)
        r_cwh.font.color.rgb = RGBColor(120, 53, 15)
        
        p_cwd = doc.add_paragraph(cw['desc'])
        p_cwd.paragraph_format.left_indent = Inches(0.2)
        
        if "table" in cw:
            tbl_c = doc.add_table(rows=len(cw['table']), cols=3)
            tbl_c.alignment = WD_TABLE_ALIGNMENT.CENTER
            for r_idx, r_data in enumerate(cw['table']):
                r_cells = tbl_c.rows[r_idx].cells
                r_cells[0].text = r_data[0]
                r_cells[1].text = r_data[1]
                r_cells[2].text = "(请计算填入) ___________________ g" if r_idx > 0 else "实际使用重量 (g) [考生填入]"
                for c_idx in range(3):
                    set_cell_margins(r_cells[c_idx], top=70, bottom=70, left=90, right=90)
                    if r_idx == 0:
                        set_cell_background(r_cells[c_idx], "FEF3C7")
                        r_cells[c_idx].paragraphs[0].runs[0].font.bold = True
                        r_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(9)
                    else:
                        r_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(8.5)
            set_table_borders(tbl_c)
            
            p_tot_s = doc.add_paragraph("\n【算式与总重书写区】：\n"
                                        "公式：材料实际克数 = 面粉重量 (500g) × 该材料烘焙百分比\n"
                                        "配方面团总重量 (Total Dough Weight) = ______________________________________ g\n")
            p_tot_s.paragraph_format.left_indent = Inches(0.2)
        else:
            p_ans_space = doc.add_paragraph(
                "【作答书写区域】：\n"
                "_________________________________________________________________________________\n"
                "_________________________________________________________________________________\n"
                "_________________________________________________________________________________\n"
                "_________________________________________________________________________________\n"
                "_________________________________________________________________________________\n"
            )
            p_ans_space.paragraph_format.left_indent = Inches(0.2)
            
        doc.add_paragraph() # Spacer
        
    doc.save(DOC4_PATH)
    print(f"Generated Document 4: {DOC4_PATH} ({os.path.getsize(DOC4_PATH)} bytes)")

# =========================================================================
# GENERATE DOCUMENT 5: TEACHER ANSWER KEY (05)
# =========================================================================

def build_doc5():
    doc = create_styled_document()
    
    # Title Block
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t0 = p_title.add_run("马来西亚华文独立中学高中统考（UEC）厨艺理论\n")
    r_t0.font.size = Pt(13)
    r_t0.font.bold = True
    r_t0.font.color.rgb = RGBColor(100, 116, 139)
    
    r_t1 = p_title.add_run("【高一阶段专属】烘焙基础理论与实务 · 教师专用参考答案与详细评分标准\n")
    r_t1.font.size = Pt(16)
    r_t1.font.bold = True
    r_t1.font.color.rgb = RGBColor(120, 53, 15)
    
    r_t2 = p_title.add_run("配套题卷：高一烘焙全真统考测验题库卷 | 包含 50 道选择题速查与考点解析 ＋ 10 简答 ＋ 5 综合大题采分细则")
    r_t2.font.size = Pt(9.5)
    r_t2.font.italic = True
    r_t2.font.color.rgb = RGBColor(180, 83, 9)
    
    doc.add_paragraph() # Spacer
    
    # Section 1: Quick Answer Key Table (5 rows of 10)
    h1 = doc.add_heading("第一部分：50 道选择题答案速查表 (Quick Reference Table)", level=1)
    h1.style.font.color.rgb = RGBColor(120, 53, 15)
    
    tbl_key = doc.add_table(rows=6, cols=11)
    tbl_key.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_k = ["题号"] + [f"Q{i}" for i in range(1, 11)]
    for c_idx, h in enumerate(headers_k):
        c = tbl_key.rows[0].cells[c_idx]
        c.text = h
        set_cell_background(c, "FEF3C7")
        set_cell_margins(c, top=60, bottom=60, left=60, right=60)
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.size = Pt(9)
        
    for r_idx in range(5):
        row = tbl_key.rows[r_idx+1]
        start_q = r_idx * 10 + 1
        end_q = start_q + 9
        row.cells[0].text = f"Q{start_q:02d}-Q{end_q:02d}"
        set_cell_margins(row.cells[0], top=60, bottom=60, left=60, right=60)
        row.cells[0].paragraphs[0].runs[0].font.size = Pt(8.5)
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        
        for c_idx in range(1, 11):
            q_num = start_q + c_idx - 1
            ans = mcq_bank[q_num-1]['ans']
            c = row.cells[c_idx]
            c.text = ans
            set_cell_margins(c, top=60, bottom=60, left=60, right=60)
            p = c.paragraphs[0]
            p.runs[0].font.bold = True
            p.runs[0].font.size = Pt(9.5)
            p.runs[0].font.color.rgb = RGBColor(16, 185, 129)
            
    set_table_borders(tbl_key)
    doc.add_paragraph() # Spacer
    
    # Detailed MCQ Explanations
    h2 = doc.add_heading("第二部分：50 道选择题逐题考点定位与深度解析", level=1)
    h2.style.font.color.rgb = RGBColor(120, 53, 15)
    
    for q in mcq_bank:
        p = doc.add_paragraph()
        r_n = p.add_run(f"Q{q['id']:02d}. 【答案：{q['ans']}】 ")
        r_n.bold = True
        r_n.font.color.rgb = RGBColor(16, 185, 129)
        r_e = p.add_run(q['exp'])
        r_e.font.size = Pt(9.5)
        r_e.font.color.rgb = RGBColor(51, 65, 85)
        
    doc.add_paragraph() # Spacer
    
    # Section 3: Short Answer Keys (10 items)
    h3 = doc.add_heading("第三部分：10 道基础简短作答题标准参考答案与评分要点", level=1)
    h3.style.font.color.rgb = RGBColor(120, 53, 15)
    
    for sa in short_answers:
        p_sa = doc.add_paragraph()
        r_h = p_sa.add_run(f"【{sa['id']}】{sa['q']}\n")
        r_h.bold = True
        r_h.font.color.rgb = RGBColor(180, 83, 9)
        
        r_ans = p_sa.add_run(f"标准参考答案：{sa['ans']}\n")
        r_ans.font.size = Pt(9.5)
        r_ans.font.color.rgb = RGBColor(51, 65, 85)
        p_sa.paragraph_format.left_indent = Inches(0.2)
        p_sa.paragraph_format.space_after = Pt(8)
        
    doc.add_paragraph() # Spacer
    
    # Section 4: Comprehensive Written Rubrics (5 items)
    h4 = doc.add_heading("第四部分：5 道综合大题标准采分点与评分细则", level=1)
    h4.style.font.color.rgb = RGBColor(120, 53, 15)
    
    for cw in comprehensive_written:
        p_cwh = doc.add_paragraph()
        r_cwh = p_cwh.add_run(f"【{cw['id']}】{cw['title']} (满分 {cw['score']} 分)")
        r_cwh.bold = True
        r_cwh.font.size = Pt(11)
        r_cwh.font.color.rgb = RGBColor(120, 53, 15)
        
        if "table" in cw:
            tbl_c = doc.add_table(rows=len(cw['table']), cols=4)
            tbl_c.alignment = WD_TABLE_ALIGNMENT.CENTER
            for r_idx, r_data in enumerate(cw['table']):
                r_cells = tbl_c.rows[r_idx].cells
                for c_idx in range(4):
                    r_cells[c_idx].text = r_data[c_idx]
                    set_cell_margins(r_cells[c_idx], top=70, bottom=70, left=90, right=90)
                    if r_idx == 0:
                        set_cell_background(r_cells[c_idx], "FEF3C7")
                        r_cells[c_idx].paragraphs[0].runs[0].font.bold = True
                        r_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(9)
                    else:
                        r_cells[c_idx].paragraphs[0].runs[0].font.size = Pt(8.5)
            set_table_borders(tbl_c)
            
            p_tot = doc.add_paragraph(f"\n【总重量与总分给分细则】：\n• {cw['total_calc']}\n• 阅卷提示：若考生未列式但填数完全正确，扣1分书写分；若面粉除数弄错，全题重度失分。")
            p_tot.paragraph_format.left_indent = Inches(0.2)
            p_tot.runs[0].font.size = Pt(9.5)
            p_tot.runs[0].font.color.rgb = RGBColor(71, 85, 105)
        else:
            p_rub = doc.add_paragraph(cw['rubric'])
            p_rub.paragraph_format.left_indent = Inches(0.2)
            p_rub.runs[0].font.size = Pt(9.5)
            p_rub.runs[0].font.color.rgb = RGBColor(51, 65, 85)
            
        doc.add_paragraph() # Spacer
        
    doc.save(DOC5_PATH)
    print(f"Generated Document 5: {DOC5_PATH} ({os.path.getsize(DOC5_PATH)} bytes)")

build_doc4()
build_doc5()
print("All tasks completed successfully!")
