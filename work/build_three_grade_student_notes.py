from pathlib import Path
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(r"C:\Users\GOH\Desktop\2026年统考厨艺理论")
OUT = ROOT / "04_学生笔记重点收藏"
OUT.mkdir(exist_ok=True)

COMMON_VIDEO = "视频参考：Notion对应课页及《原创图解上传与复核清单》（上课前须检查链接与字幕）。"

G1 = [
 ("第1课｜烘焙概论", "烘焙 Baking；淀粉糊化 Starch gelatinisation；蛋白质凝固 Protein coagulation；美拉德反应 Maillard reaction", ["烘焙以干热使面团或面糊熟化，并形成体积、结构、色泽与香气。", "炉内会发生水分蒸发、气体膨胀、油脂熔化、淀粉糊化和蛋白质凝固。", "焦糖化主要是糖受热；美拉德反应需要还原糖与氨基化合物。"], "不要把蒸、炸、冷冻全部叫作烘焙，也不要把所有褐变都归为焦糖化。", "用“结构—色泽—香气”解释一件烘焙成品的变化。", "01-烘焙过程总览-v2.png", "中文：天然酵母示范｜小高姐；英文：Bakistry｜Harvard University。"),
 ("第2课｜烘焙的历史与发展", "烘焙 Baking；谷物 Cereal；磨粉 Milling；工业化 Industrialisation", ["烘焙发展与谷物栽培、磨粉技术、发酵知识及烤炉改良有关。", "从家庭手工业到机械化生产，标准配方、温度控制和卫生管理越来越重要。", "历史事件要按先后和因果理解，不只背年代。"], "不要把某一种面包或单一地区说成所有烘焙食品的唯一来源。", "列出两项技术进步，并说明它怎样改变烘焙生产。", "—", COMMON_VIDEO),
 ("第3课｜中式面食与烘焙食品分类", "面点 Chinese pastry；发酵面团 Fermented dough；水调面团 Water dough；酥皮 Laminated pastry", ["分类可依据原料、面团性质、膨松方式和熟制方法。", "中式面食可能采用蒸、煎、炸、烤等方法，不能只凭外形分类。", "同一产品可同时具有文化分类和工艺分类。"], "不要因为产品含面粉，就一律归为烘焙食品。", "任选三种中式面食，写出主要原料、膨松方式与熟制方法。", "—", COMMON_VIDEO),
 ("第4课｜西式烘焙食品分类", "面包 Bread；蛋糕 Cake；饼干 Cookie；派 Pie；塔 Tart；酥点 Pastry", ["西式烘焙常见类别包括面包、蛋糕、饼干、派塔及各类酥点。", "应比较结构来源：面筋、泡沫、油脂层次或化学膨松。", "分类服务于配方选择、搅拌方法与品质判断。"], "不要只按甜或咸分类，也不要把派与塔视为完全相同。", "说明面包、蛋糕和饼干的主要结构来源有何不同。", "—", COMMON_VIDEO),
 ("第5课｜烘焙设备", "烤箱 Oven；搅拌机 Mixer；醒发箱 Proofer；冷藏柜 Refrigerator", ["设备选择取决于产品、产量、温度范围和操作安全。", "烤箱设定温度不一定等于实际炉温，须预热并观察均匀度。", "使用前检查电源、护罩、清洁状态和紧急停机方法。"], "不要把设备“能启动”当成“安全且准确”。", "写出烤箱与搅拌机各三项使用前检查。", "—", COMMON_VIDEO),
 ("第6课｜烘焙制作器具", "电子秤 Digital scale；量杯 Measuring cup；刮刀 Scraper；打蛋器 Whisk；烤模 Baking tin", ["秤量、混合、成形、烘烤和冷却使用不同器具。", "选择器具须考虑材质、容量、耐热性与是否接触食品。", "准确工具能减少批次差异。"], "不要混用干性与液体量具，也不要用损坏器具继续操作。", "为制作蛋糕列出六件器具，并说明各自用途。", "—", COMMON_VIDEO),
 ("第7课｜器具使用、安全与维护", "清洁 Cleaning；消毒 Sanitising；维护 Maintenance；交叉污染 Cross-contamination", ["清洁先去除污物，消毒再降低微生物风险，两者不可互相代替。", "器具须按材料和制造商说明清洁、干燥及储存。", "刀具、机器、热盘和电器分别有不同危险。"], "不要用湿手碰插头，也不要在机器运转时伸手取料。", "写出“使用前—使用中—使用后”各两项安全动作。", "—", COMMON_VIDEO),
 ("第8课｜度量衡与准确秤量", "质量 Mass；体积 Volume；去皮 Tare；公制 Metric system", ["烘焙优先用质量秤量，单位须统一。", "先放容器再去皮；少量材料需使用适合精度的秤。", "换算时先看单位，再运算，最后检查答案是否合理。"], "不要把毫升与克直接视为永远相等。", "把2.5 kg换成g，并说明为什么水以外材料不能随意用mL代替g。", "—", COMMON_VIDEO),
 ("第9课｜烘焙材料的性质与功能", "建立结构 Structure building；柔化 Tenderising；保湿 Moisture retention；充气 Aeration", ["原料可能同时具有多项功能，作用取决于配方与工艺。", "面粉与蛋常帮助建立结构；糖与油脂常有柔化、保湿和风味作用。", "液体提供水合条件，搅拌与加热决定最终表现。"], "不要画成“一种原料只对应一种功能”的单线关系。", "选择面粉、糖、油脂、鸡蛋各写两项功能。", "02-烘焙原料功能关系图.png", "中文：烘焙油脂科学与应用；英文：Bakistry｜Harvard University。"),
 ("第10课｜面粉", "蛋白质 Protein；面筋 Gluten；吸水率 Water absorption；低筋粉 Cake flour；高筋粉 Bread flour", ["面粉蛋白质与水结合并经搅拌形成面筋网络。", "不同产品需要不同筋度；不是筋度越高越好。", "吸水率受面粉种类、储存及配方影响。"], "不要只用“薄膜越薄越好”判断所有面团。", "解释水合与搅拌怎样帮助形成面筋。", "03-面筋形成与面团搅拌阶段图.png", "中文：手揉面与手套膜；英文：Bakistry｜Harvard University。"),
 ("第11课｜油脂", "油脂 Fat；可塑性 Plasticity；起酥 Shortening effect；乳化 Emulsification", ["油脂能带来风味、湿润、柔化和层次，也可帮助充气。", "固体油脂的可塑性影响打发和折叠层次。", "油脂过冷、过软或加入时机错误都会改变结构。"], "不要把植物油、沙拉油、奶油和起酥油当作完全相同。", "比较液体油与固体油脂在蛋糕中的两项差异。", "02-烘焙原料功能关系图.png", "中文：烘焙油脂科学与应用；英文：Bakistry｜Harvard University。"),
 ("第12课｜糖", "蔗糖 Sucrose；吸湿性 Hygroscopicity；焦糖化 Caramelisation；柔化 Tenderising", ["糖提供甜味，也影响保湿、上色、体积、泡沫与保存。", "糖会与水竞争，延缓部分淀粉糊化和蛋白质凝固。", "糖量或颗粒改变，不能只看甜度。"], "不要认为减糖只会降低甜味而不影响结构。", "说明减少糖可能怎样影响色泽、湿润度和组织。", "02-烘焙原料功能关系图.png", COMMON_VIDEO),
 ("第13课｜鸡蛋", "蛋白 Egg white；蛋黄 Egg yolk；泡沫 Foam；卵磷脂 Lecithin；凝固 Coagulation", ["鸡蛋提供结构、乳化、充气、色泽、风味和水分。", "蛋白打发由大泡到细泡和尖峰；过度打发会粗糙、失去光泽。", "蛋黄中的卵磷脂有助油水分散。"], "不要用沾油器具打蛋白，也不要把硬性发泡当成所有配方的唯一终点。", "用尖端、光泽、细腻度判断四种蛋白霜状态。", "05-蛋白霜四种状态与失败判断图.png", "中文：如何打发蛋白；英文：The Science of Meringue。"),
 ("第14课｜乳制品", "牛奶 Milk；奶粉 Milk powder；鲜奶油 Whipping cream；乳糖 Lactose", ["乳制品提供水分、脂肪、蛋白质、乳糖与风味。", "乳糖和蛋白质会影响表面褐变。", "鲜奶油打发需要低温，并须遵守冷藏管理。"], "不要把所有乳制品按同重量直接互换。", "说明牛奶与奶粉在配方水分方面的差别。", "—", "中文：正确打发淡奶油；英文：Notion对应课页参考。"),
 ("第15课｜酵母与发酵", "酵母 Yeast；发酵 Fermentation；二氧化碳 Carbon dioxide；醒发 Proofing", ["酵母利用可发酵糖产生二氧化碳和风味物质。", "温度、时间、盐糖浓度和酵母活性影响发酵速度。", "产气速率会先变化；面团体积是气体累积与保气能力的结果。"], "不要把高温当成越快越好，也不要只按固定分钟判断发酵完成。", "比较启动期、活跃期和减缓期的产气变化。", "04-酵母发酵三阶段与产气关系图.png", "中文：天然酵母示范；英文：The Mechanics of Yeast。"),
 ("第16课｜化学膨大剂", "泡打粉 Baking powder；小苏打 Baking soda；酸碱反应 Acid-base reaction；二氧化碳 Carbon dioxide", ["小苏打需要适当酸性成分；泡打粉已含酸碱成分。", "双效泡打粉在混合及受热阶段均可能产气。", "用量过多会造成异味、粗孔或塌陷。"], "不要把泡打粉与小苏打随意等量互换。", "说明为什么小苏打必须考虑配方酸度。", "—", COMMON_VIDEO),
 ("第17课｜乳化剂与乳化作用", "乳化 Emulsification；乳化剂 Emulsifier；油相 Oil phase；水相 Water phase；分离 Curdling", ["乳化是把一种不易相溶液体以小滴分散在另一相中。", "乳化剂具有亲水与亲油部分，可帮助体系稳定。", "材料温度、加入速度和搅拌强度影响乳化成败。"], "不要假定分离后一定可以修复；先停止过度搅打并判断原因。", "用油滴大小解释成功乳化与分离。", "06-乳化成功分离与修复关系图.png", "中文：暂无直接理论片；英文：Emulsification in Baking。"),
 ("第18课｜胶冻类材料", "明胶 Gelatin；琼脂 Agar；果胶 Pectin；凝胶 Gel", ["胶冻材料通过不同机制形成三维网络并固定水分。", "明胶、琼脂和果胶的溶解、凝固温度及口感不同。", "酸、糖、酶和加热方式可能影响凝固。"], "不要把不同凝固剂直接等量互换。", "比较明胶与琼脂在来源、口感和温度表现上的差异。", "—", COMMON_VIDEO),
 ("第19课｜塔塔粉", "塔塔粉 Cream of tartar；酸性盐 Acid salt；稳定泡沫 Foam stabilisation", ["塔塔粉是酸性材料，可用于调节酸碱和帮助稳定蛋白泡沫。", "它不是奶油，也不是一般泡打粉。", "用量须依配方，不宜凭感觉增加。"], "不要把英文cream误解为乳制奶油。", "说明塔塔粉在蛋白霜中的作用及过量风险。", "—", COMMON_VIDEO),
 ("第20课｜烘焙百分比与材料用量", "烘焙百分比 Baker's percentage；基准面粉 Flour basis；配方总重 Formula weight", ["烘焙百分比以面粉总重为100%，其他原料相对面粉计算。", "原料重=面粉重×该原料百分比。", "总百分比可以超过100%，因为面粉只是比较基准。"], "不要把烘焙百分比误认为成品中各原料合计必须100%。", "面粉800 g、水60%，计算水重并写出过程。", "—", COMMON_VIDEO),
]

G2 = [
 ("第1单元｜蛋糕分类、材料与制作准备", "面糊类蛋糕 Batter cake；泡沫类蛋糕 Foam cake；乳沫类蛋糕 Chiffon cake；预热 Preheating", ["按主要充气与结构方法区分蛋糕，不只看外形。", "制作前须完成配方核对、准确秤量、材料温度和烤模准备。", "不同蛋糕依赖油脂打发、蛋泡沫或两者结合。"], "不要临时换模具或未预热就入炉。", "比较面糊类、泡沫类与乳沫类蛋糕的主要充气来源。", "—", COMMON_VIDEO),
 ("第2单元｜蛋糕搅拌法与蛋白打发", "糖油拌合法 Creaming method；全蛋打发 Whole-egg foaming；翻拌 Folding；蛋白霜 Meringue", ["搅拌法决定空气怎样进入及被结构保留。", "翻拌要均匀但避免过度消泡。", "蛋白霜状态须依配方要求判断。"], "不要用高速一直搅到“越硬越好”。", "说明糖油拌合法与全蛋打发法的充气差异。", "05-蛋白霜四种状态与失败判断图.png", "中文：如何打发蛋白；英文：The Science of Meringue。"),
 ("第3单元｜蛋糕比重与烘焙影响因素", "面糊比重 Batter specific gravity；去皮 Tare；炉温 Oven temperature", ["比重=同容积面糊重÷同容积水重。", "较低比重通常含气较多，但必须对照产品标准。", "炉温、模具、装模量、面糊温度与等待时间都会影响成品。"], "不要认为比重越低一定越好。", "水500 g、面糊420 g，计算比重并解释其限制。", "07-蛋糕面糊比重测量步骤图.png", "中文：暂无完整示范；英文：Specific Gravity｜No Bs Baking。"),
 ("第4单元｜出炉处理与蛋糕失败分析", "脱模 Demoulding；冷却 Cooling；下陷 Collapse；收缩 Shrinkage", ["出炉后须依产品决定震模、倒扣、脱模和冷却方法。", "失败诊断应写出现象、可能原因、机制与验证方法。", "中央下陷可能涉及未熟、过早开炉、配方失衡或结构不足。"], "不要看到一种现象就断定只有一个原因。", "为“中央下陷”列三项可能原因，并设计单变量验证。", "—", COMMON_VIDEO),
 ("第5单元｜奶油霜、鲜奶油霜与蛋白霜饰", "奶油霜 Buttercream；鲜奶油 Whipped cream；蛋白霜饰 Meringue frosting；稳定性 Stability", ["霜饰选择须考虑温度、甜度、结构、用途与食品安全。", "鲜奶油需低温打发与冷藏；奶油霜类型和乳化方法不同。", "过度搅打、温差或液体过多会导致粗糙和分离。"], "不要把所有“cream”视为同一种霜。", "比较三种霜饰的主要原料、稳定性和储存要求。", "06-乳化成功分离与修复关系图.png", "中文：正确打发淡奶油；英文：Emulsification in Baking。"),
 ("第6单元｜面包分类与制作流程", "直接法 Straight dough method；中种法 Sponge method；整形 Shaping；最后醒发 Final proof", ["面包可按原料、含油糖量、组织与制作法分类。", "流程包括秤量、混合、发酵、分割、整形、醒发、烘烤和冷却。", "每一阶段都为下一阶段建立条件。"], "不要把酵母活性阶段与面包生产流程阶段混为一谈。", "按顺序写出面包制作主要阶段，并说明其中两个阶段的目的。", "—", COMMON_VIDEO),
 ("第7单元｜面团搅拌阶段", "拾起阶段 Pick-up stage；发展阶段 Development stage；最终发展 Final development；过度搅拌 Overmixing", ["搅拌让原料分散、面粉水合并发展面筋。", "面团由粗糙黏附逐步变光滑、有弹性和延展性。", "过度搅拌会发热、黏软并削弱结构。"], "不要认为所有面包都必须达到同一薄膜程度。", "用外观、触感和薄膜描述发展不足、适当与过度搅拌。", "03-面筋形成与面团搅拌阶段图.png", "中文：手揉面教程；英文：Bakistry｜Harvard University。"),
 ("第8单元｜发酵阶段与判断", "基本发酵 Bulk fermentation；中间醒发 Bench rest；最后醒发 Final proof；按压测试 Poke test", ["发酵同时影响体积、风味和面团结构。", "判断须结合体积、时间、温度、触感和回弹。", "发酵不足与过度发酵都会影响炉内膨胀。"], "不要只按固定分钟或“变两倍”作为所有配方唯一标准。", "比较发酵不足、适当及过度发酵的表现。", "04-酵母发酵三阶段与产气关系图.png", "中文：天然酵母示范；英文：The Mechanics of Yeast。"),
 ("第9单元｜面包烘焙阶段", "炉内膨胀 Oven spring；糊化 Gelatinisation；凝固 Coagulation；褐变 Browning", ["入炉初期气体和蒸汽膨胀，酵母短暂继续活动。", "随后淀粉糊化、蛋白质凝固，内部结构定型。", "出炉后仍需冷却，让水分重新分布。"], "不要只看表皮颜色判断内部完全成熟。", "说明炉内膨胀、结构定型和冷却之间的关系。", "01-烘焙过程总览-v2.png", "英文：Bakistry｜Harvard University；中文参考见Notion。"),
 ("第10单元｜面糊重、面团重与损耗计算", "损耗率 Loss rate；保留率 Retention rate；成品率 Yield；倒推 Back calculation", ["保留率=1−损耗率。", "正推逐段乘保留率；倒推由目标重量逐段除以保留率。", "不同阶段损耗不能直接相加后一次处理。"], "不要用目标1 kg直接加20%再加5%。", "目标1.00 kg、烘烤保留0.80、操作保留0.95，倒推所需重量。", "10-多阶段损耗倒推计算图.png；10A-1kg成品小重量倒推计算图.png", "英文：Yield Percentage｜Culinary Math；中文由教师板书演算。"),
 ("第11单元｜西餐概论、厨房与卫生管理", "厨房分区 Kitchen zoning；个人卫生 Personal hygiene；危险温度带 Temperature danger zone；SOP", ["厨房工作讲究动线、分区、岗位和沟通。", "清洁、消毒、个人卫生及时间温度控制共同降低风险。", "食品安全以马来西亚法规、学校SOP和实际设备为准。"], "不要以外观或气味作为食品安全的唯一判断。", "写出进入厨房前、处理食品中及工作结束后的卫生重点。", "—", COMMON_VIDEO),
 ("第12单元｜西餐刀具与安全切配", "主厨刀 Chef's knife；削皮刀 Paring knife；爪形手势 Claw grip；砧板 Cutting board", ["刀具应依任务选择，并保持适当锋利。", "使用爪形手势、稳定砧板和清楚动线。", "生熟食材应分开器具或完成有效清洁消毒。"], "不要徒手接落刀，也不要把刀泡在看不见的水槽中。", "画出安全切配工作区，并标出三项控制。", "—", COMMON_VIDEO),
 ("第13单元｜食材种类、选购与验收", "验收 Receiving；规格 Specification；有效日期 Expiry date；冷链 Cold chain", ["验收检查数量、规格、包装、日期、温度与感官状态。", "不合格品应隔离、记录并按程序处理。", "价格不是唯一标准，品质和安全必须符合要求。"], "不要先收货后补检查。", "设计一份五项冷藏食材验收清单。", "—", COMMON_VIDEO),
 ("第14单元｜食材储存与香辛料", "先进先出 FIFO；交叉污染 Cross-contamination；密封储存 Covered storage；香辛料 Spice", ["熟食和即食食品在上；可能滴漏的生食密封置下，禽肉放底层接漏。", "储存须标示名称与日期，并执行FIFO。", "香辛料受光、热、湿气影响，需密封并适量使用。"], "不要把所有食品塞入冰箱就当作安全。", "说明为什么生禽肉须密封置于下层。", "11-生熟分区与冷藏架位图.png", "英文：Food Waste and Food Safety at Home；中文以学校SOP为主。"),
 ("第15单元｜食物加热方式与西式汤类", "传导 Conduction；对流 Convection；辐射 Radiation；清汤 Clear soup；浓汤 Thick soup", ["煎、烤、煮、蒸等方法有不同热传递与水分变化。", "汤类可按清澈度、稠化方法和主要原料分类。", "加热强度、时间和切割大小共同影响成熟。"], "不要认为火越大一定越快且越好。", "比较煮、炖、烤三种方法的热介质与适合食材。", "—", COMMON_VIDEO),
]

G3 = [
 ("第1单元｜饼干", "糖油拌合法 Creaming method；酥松 Shortness；摊展 Spread；回潮 Moisture pickup", ["饼干结构受面粉、糖、油脂、液体和搅拌程度影响。", "油脂与糖会影响酥松、摊展、色泽和口感。", "大小、厚度、烤盘与炉温必须一致才能公平比较。"], "不要过度搅拌加入面粉后的面团。", "分析饼干过度摊开的四项可能原因。", "—", COMMON_VIDEO),
 ("第2单元｜胶冻类西点", "凝胶 Gel；明胶 Gelatin；琼脂 Agar；果胶 Pectin；离水 Syneresis", ["不同胶冻剂需要不同溶解、凝固和储存条件。", "酸、糖、酶、浓度及加热会影响凝胶强度。", "离水、过硬或不凝固要从配方和过程共同诊断。"], "不要把明胶、琼脂和果胶直接等量互换。", "为“不凝固”列出三项原因和验证方法。", "—", COMMON_VIDEO),
 ("第3单元｜塔与派", "塔 Tart；派 Pie；盲烤 Blind baking；起酥 Shortening；回缩 Shrinkage", ["塔与派的外形、模具、皮壳和馅料组织可不同。", "控制面筋发展、油脂温度和静置可减少回缩。", "湿馅可能使底部不熟，需考虑盲烤与防潮。"], "不要过度揉搓酥皮，也不要用过多手粉掩盖黏性。", "解释塔皮回缩和底部湿软的可能原因。", "—", COMMON_VIDEO),
 ("第4单元｜泡芙", "泡芙面糊 Choux pastry；烫面 Panade；蒸汽膨胀 Steam expansion；结构定型 Structure setting", ["烫面使面粉吸水并部分糊化。", "鸡蛋须分次加入，以面糊状态为终点。", "蒸汽推动膨胀，淀粉与蛋白质随后定型并在后段干燥。"], "不要把泡芙膨胀归因于酵母，也不要未定型就开炉。", "说明泡芙由烫面到形成空腔的五阶段。", "09-泡芙空腔形成剖面时间线.png", "英文：Claire Saffitz Makes Pâte à Choux；中文以图解示范为主。"),
 ("第5单元｜松饼、比萨与道纳司", "松饼 Muffin；比萨 Pizza；道纳司 Doughnut；过度搅拌 Overmixing；油炸 Frying", ["松饼混合法强调干湿材料分别混合后短暂拌匀。", "比萨面团需要适当面筋与发酵；道纳司还要控制油温和吸油。", "三类产品虽都含面粉，但结构和加热方式不同。"], "不要把松饼面糊搅到完全无颗粒，也不要用低油温长时间炸制。", "比较三种产品的膨松方式和加热方法。", "—", COMMON_VIDEO),
 ("第6单元｜热酱与冷酱", "白酱 Béchamel；褐酱 Brown sauce；乳化酱 Emulsified sauce；油面糊 Roux；还原 Reduction", ["酱汁通过淀粉糊化、还原浓缩或乳化取得稠度。", "热酱须控制糊底、结块与保温；冷酱须控制乳化和冷藏。", "稠度、光泽、风味和平衡是品质判断重点。"], "不要用大量淀粉补救所有稀酱，也不要让含蛋乳酱汁长时间处于室温。", "比较油面糊稠化、还原浓缩与乳化三种方法。", "06-乳化成功分离与修复关系图.png", "英文：Emulsification in Baking（原理相通）；中文见Notion课页。"),
 ("第7单元｜亚洲烹调技法", "炒 Stir-frying；蒸 Steaming；煎 Pan-frying；炸 Deep-frying；焖 Braising", ["技法选择取决于食材性质、切割、目标口感和设备。", "备料顺序、锅温、油量与下料次序决定成品。", "同一技法在不同地区可能有不同名称和做法，应抓住热传递原理。"], "不要把“猛火快炒”套用到所有食材。", "选择一种食材，比较蒸、炒、炸的成品差异。", "—", COMMON_VIDEO),
 ("第8单元｜火候运用与成品判断", "火候 Heat control；余热 Carryover cooking；成熟度 Doneness；感官评价 Sensory evaluation", ["火候包含热源强度、时间、距离、锅具和食材状态。", "离火后余热仍可能继续加热成品。", "成品判断应结合中心温度、质地、色泽、香气和食品安全要求。"], "不要只凭颜色或固定时间判断熟度。", "设计一份包含温度、质地、色泽和安全的成品检查表。", "—", COMMON_VIDEO),
]

def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:fill'), fill)
    tc_pr.append(shd)

def set_cell_width(cell, dxa):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_w = tc_pr.find(qn('w:tcW'))
    if tc_w is None:
        tc_w = OxmlElement('w:tcW'); tc_pr.append(tc_w)
    tc_w.set(qn('w:w'), str(dxa)); tc_w.set(qn('w:type'), 'dxa')

def add_page_field(paragraph):
    run = paragraph.add_run()
    fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE')
    run._r.addnext(fld)

def set_font(run, size=None, bold=None, color=None):
    run.font.name = 'Calibri'
    run._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'), 'Microsoft JhengHei')
    if size: run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if color: run.font.color.rgb = RGBColor.from_string(color)

def style_doc(doc, grade):
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.top_margin, sec.bottom_margin = Mm(14), Mm(14)
    sec.left_margin, sec.right_margin = Mm(16), Mm(16)
    sec.header_distance, sec.footer_distance = Mm(7), Mm(7)
    styles = doc.styles
    for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3']:
        st=styles[name]; st.font.name='Calibri'; st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft JhengHei')
    styles['Normal'].font.size=Pt(10.5); styles['Normal'].paragraph_format.space_after=Pt(4); styles['Normal'].paragraph_format.line_spacing=1.16
    styles['Title'].font.size=Pt(25); styles['Title'].font.bold=True; styles['Title'].font.color.rgb=RGBColor(31,78,121)
    styles['Heading 1'].font.size=Pt(16); styles['Heading 1'].font.bold=True; styles['Heading 1'].font.color.rgb=RGBColor(31,78,121); styles['Heading 1'].paragraph_format.space_before=Pt(3); styles['Heading 1'].paragraph_format.space_after=Pt(6)
    styles['Heading 2'].font.size=Pt(11.5); styles['Heading 2'].font.bold=True; styles['Heading 2'].font.color.rgb=RGBColor(192,80,20); styles['Heading 2'].paragraph_format.space_before=Pt(5); styles['Heading 2'].paragraph_format.space_after=Pt(3)
    header=sec.header.paragraphs[0]; header.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    r=header.add_run(f'2026 高中厨艺（烘焙理论）｜{grade}学生笔记'); set_font(r,8.5,color='777777')
    footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=footer.add_run('学生重点收藏｜'); set_font(r,8.5,color='777777'); add_page_field(footer)

def add_bullet(doc, text):
    p=doc.add_paragraph(style='List Bullet'); p.paragraph_format.left_indent=Mm(6); p.paragraph_format.first_line_indent=Mm(-3)
    set_font(p.add_run(text),10.3); return p

def add_lesson(doc, item, first=False):
    title, terms, points, mistake, check, image, video = item
    if not first: doc.add_page_break()
    p=doc.add_paragraph(style='Heading 1'); p.paragraph_format.keep_with_next=True; set_font(p.add_run(title),16,bold=True,color='1F4E79')
    p=doc.add_paragraph(); p.paragraph_format.space_after=Pt(6)
    r=p.add_run('学习目标｜'); set_font(r,10.5,bold=True,color='C05014')
    r=p.add_run('能用正确术语说明本课原理，并能根据观察证据作出基本判断。'); set_font(r,10.5)
    doc.add_paragraph('专业词中英对照', style='Heading 2')
    table=doc.add_table(rows=1, cols=2); table.alignment=WD_TABLE_ALIGNMENT.LEFT; table.autofit=False
    tbl_w = table._tbl.tblPr.find(qn('w:tblW'))
    if tbl_w is None:
        tbl_w = OxmlElement('w:tblW'); table._tbl.tblPr.append(tbl_w)
    tbl_w.set(qn('w:w'),'9120'); tbl_w.set(qn('w:type'),'dxa')
    set_cell_width(table.cell(0,0),2000); set_cell_width(table.cell(0,1),7120)
    table.cell(0,0).text='本课术语'; table.cell(0,1).text=terms
    for c in table.rows[0].cells:
        c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; set_cell_shading(c,'EAF2F8')
        for p0 in c.paragraphs:
            for rr in p0.runs: set_font(rr,9.6,bold=True if c==table.cell(0,0) else False)
    doc.add_paragraph('必须懂的重点', style='Heading 2')
    for pt in points: add_bullet(doc,pt)
    doc.add_paragraph('常见误区', style='Heading 2')
    p=doc.add_paragraph(); p.paragraph_format.left_indent=Mm(3); r=p.add_run('⚠ ' + mistake); set_font(r,10.2,bold=True,color='9C0006')
    doc.add_paragraph('图解与视频参考', style='Heading 2')
    p=doc.add_paragraph(); set_font(p.add_run(f'图解：{image}'),9.5,color='555555')
    p=doc.add_paragraph(); set_font(p.add_run(video),9.5,color='555555')
    doc.add_paragraph('自我检查', style='Heading 2')
    p=doc.add_paragraph(); r=p.add_run('□ ' + check); set_font(r,10.3,bold=True)
    doc.add_paragraph('我的笔记', style='Heading 2')
    for _ in range(3):
        p=doc.add_paragraph('________________________________________________________________________________'); p.paragraph_format.space_after=Pt(4)
        set_font(p.runs[0],9,color='A6A6A6')

def build(grade, items, filename, intro):
    doc=Document(); style_doc(doc,grade)
    p=doc.add_paragraph(style='Title'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; set_font(p.add_run(f'{grade}｜学生笔记重点收藏'),25,bold=True,color='1F4E79')
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; set_font(p.add_run('高中厨艺（烘焙理论）2026｜可打印学习版'),12,bold=True,color='C05014')
    p=doc.add_paragraph(); p.paragraph_format.space_before=Pt(18); set_font(p.add_run(intro),11)
    doc.add_paragraph('使用方法', style='Heading 1')
    for x in ['先读“必须懂的重点”，再用专业词解释原理。','观看视频时只记录与课程有关的证据，不把食谱参数当作统一标准。','完成自我检查和笔记区；不会的内容回到Notion对应课页。','本册不含统考历届题、模拟评量或教师答案。']: add_bullet(doc,x)
    doc.add_paragraph('课程目录', style='Heading 1')
    for i,it in enumerate(items,1): add_bullet(doc,it[0])
    for i,it in enumerate(items): add_lesson(doc,it,first=False)
    props=doc.core_properties; props.title=f'{grade}学生笔记重点收藏'; props.subject='2026高中厨艺（烘焙理论）'; props.author='YU SIR'; props.keywords='烘焙理论, 学生笔记, 中英术语'
    path=OUT/filename; doc.save(path); return path

paths=[
 build('高一',G1,'高一_学生笔记重点收藏.docx','从烘焙概念、设备器具、度量衡和原料功能开始，建立解释烘焙现象的基础。'),
 build('高二',G2,'高二_学生笔记重点收藏.docx','连接蛋糕、面包、损耗计算与西餐基础，学习用数据和观察证据诊断成品。'),
 build('高三',G3,'高三_学生笔记重点收藏.docx','综合西式点心、冷热酱汁与亚洲烹调技法，强调结构控制、火候与食品安全。')]
for p in paths: print(p)
