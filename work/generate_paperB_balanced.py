# -*- coding: utf-8 -*-
"""
generate_paperB_balanced.py
Generates 60 high-quality, professional culinary exam questions for Paper B with:
1. Strict sentence length balance (span between min and max option length <= 4 characters).
2. Parallel sentence structure & plausible culinary distractors (eliminating naive giveaways).
3. Exact mathematical balance:
   Group A (Q1-40): 10 A, 10 B, 10 C, 10 D
   Group B (Q41-50): 3 A, 2 B, 3 C, 2 D
   Group C (Q51-60): 2 A, 3 B, 2 C, 3 D
   Total (Q1-60): Exactly 15 A, 15 B, 15 C, 15 D
"""

import json, sys

sys.stdout.reconfigure(encoding='utf-8')

# Load the original paper B data to preserve all IDs, group, src, and explanations
with open('work/paperB_parsed.json', 'r', encoding='utf-8') as f:
    old_qs = {q['id']: q for q in json.load(f)}

# We define the balanced questions
balanced_data = []

# ==========================================
# Group A: 烘焙基础理论 (Q1 ~ Q40)
# Target Keys: 10 A, 10 B, 10 C, 10 D
# ==========================================

# Q1: 天然酸种酵母（Sourdough Starter）的主要膨胀原理是？
# Ans: C
balanced_data.append({
    'id': 1,
    'ans': 'C',
    'opts': {
        'A': '商业酵母快速产生二氧化碳气体膨胀',
        'B': '化学泡打粉遇水受热释放二氧化碳',
        'C': '野生酵母与乳酸菌共生发酵产酸产气',
        'D': '面团内部水分受热气化形成高压蒸汽'
    }
})

# Q2: 低温慢煮（Sous-Vide）在烘焙与甜品领域的主要应用是？
# Ans: B
balanced_data.append({
    'id': 2,
    'ans': 'B',
    'opts': {
        'A': '快速高温烘烤欧包形成焦脆厚硬外壳',
        'B': '真空密封后以恒温水浴精准熟化内馅',
        'C': '急速冷冻面团以抑制酵母细胞的活性',
        'D': '利用高压蒸汽喷射使面糊瞬间受热膨胀'
    }
})

# Q3: 对流蒸汽烤炉（Combi Oven）与普通热风炉的最主要区别是？
# Ans: D
balanced_data.append({
    'id': 3,
    'ans': 'D',
    'opts': {
        'A': '仅能使用单一微波辐射进行快速加热',
        'B': '依靠纯导热铁板自下而上单向传递热量',
        'C': '炉腔内保持绝对干燥状态无法注入水分',
        'D': '结合热风与蒸汽可精准调控温度与湿度'
    }
})

# Q4: 「折叠面团（Laminated Dough）」中裹入油脂后的折叠层数，主要决定了产品的哪个特性？
# Ans: A
balanced_data.append({
    'id': 4,
    'ans': 'A',
    'opts': {
        'A': '烘烤成品的酥脆层次质感与膨胀高度',
        'B': '酵母在面团内部进行无氧发酵的速率',
        'C': '面团在常温搅拌过程中的最终含水量',
        'D': '焦糖化反应在表皮所呈现的深浅色泽'
    }
})

# Q5: 糖（Sugar）在面包发酵过程中的主要功能是？
# Ans: C
balanced_data.append({
    'id': 5,
    'ans': 'C',
    'opts': {
        'A': '完全作为结构支撑原料以增加面筋韧性',
        'B': '降低面团黏度并防止油脂在发酵中氧化',
        'C': '提供酵母发酵碳源并促进烘烤褐变着色',
        'D': '抑制杂菌繁殖且彻底阻断淀粉的水化过程'
    }
})

# Q6: 以下关于奶油（Butter）在饼干（Cookies）中的功能，哪项叙述错误？
# Ans: B
balanced_data.append({
    'id': 6,
    'ans': 'B',
    'opts': {
        'A': '阻断面筋网络形成赋予饼干酥脆口感',
        'B': '充当主要膨大剂促使饼干体积剧烈膨胀',
        'C': '烘烤时散发浓郁奶香并增进成品的风味',
        'D': '打发充入空气使面团具有良好的延展性'
    }
})

# Q7: 黑麦（Rye）面包与小麦面包最主要的面筋差异是？
# Ans: A
balanced_data.append({
    'id': 7,
    'ans': 'A',
    'opts': {
        'A': '缺乏醇溶谷蛋白无法形成连续网状面筋',
        'B': '含有极高活性面筋蛋白导致弹性特别强',
        'C': '面筋完全无法吸收水分形成均质的面团',
        'D': '加热后蛋白质迅速溶解失去保气支撑力'
    }
})

# Q8: 制作可颂（Croissant）时，裹入黄油的理想操作温度范围是？
# Ans: D
balanced_data.append({
    'id': 8,
    'ans': 'D',
    'opts': {
        'A': '0℃～4℃（刚出冷藏库质地坚硬）',
        'B': '8℃～10℃（略带微凉且韧性较足）',
        'C': '26℃～28℃（室温偏软极易渗出）',
        'D': '16℃～18℃（可塑性适中与面相近）'
    }
})

# Q9: 食品安全中「危险温度带（Danger Zone）」的正确温度范围是？
# Ans: B
balanced_data.append({
    'id': 9,
    'ans': 'B',
    'opts': {
        'A': '0℃～30℃之间',
        'B': '5℃～60℃之间',
        'C': '10℃～70℃之间',
        'D': '15℃～50℃之间'
    }
})

# Q10: 天使蛋糕（Angel Food Cake）在打发蛋白时加入塔塔粉的主要原因是？
# Ans: A
balanced_data.append({
    'id': 10,
    'ans': 'A',
    'opts': {
        'A': '降低酸碱度以稳定蛋白泡沫并保持纯白',
        'B': '充当化学膨大剂受热释放大量二氧化碳',
        'C': '代替部分低筋面粉提供坚固的支撑骨架',
        'D': '分解多余油脂以防止面糊产生消泡离析'
    }
})

# Q11: 调温黑巧克力（Tempering）的核心物理目的是什么？
# Ans: C
balanced_data.append({
    'id': 11,
    'ans': 'C',
    'opts': {
        'A': '彻底蒸发可可豆残余水分以防止发霉',
        'B': '促使糖粉完全溶解以提高成品的甜度',
        'C': '诱导可可脂形成稳定的第五型晶体结构',
        'D': '破坏可可脂结晶使巧克力保持常温液态'
    }
})

# Q12: 酵母发酵面团中「基本发酵」与「最终发酵」的最主要工艺区别是？
# Ans: D
balanced_data.append({
    'id': 12,
    'ans': 'D',
    'opts': {
        'A': '基本发酵需高温高湿，最终发酵需低温干燥',
        'B': '基本发酵完全不产气，最终发酵才开始膨胀',
        'C': '基本发酵由细菌主导，最终发酵由酵母完成',
        'D': '基本发酵在分割前进行，最终发酵在整型后'
    }
})

# Q13: 面包烘焙中的「自解法（Autolyse）」其核心操作机制是？
# Ans: A
balanced_data.append({
    'id': 13,
    'ans': 'A',
    'opts': {
        'A': '仅混合粉水静置促使淀粉水化与面筋自然形成',
        'B': '将面粉在干锅中翻炒至金黄微焦以激发麦香',
        'C': '加入大量商业干酵母置于温室快速催生酒香',
        'D': '成品出炉后倒扣在铁网架上利用余温慢慢自熟'
    }
})

# Q14: 以下关于蛋清打发的物理化学特性，哪项叙述正确？
# Ans: C
balanced_data.append({
    'id': 14,
    'ans': 'C',
    'opts': {
        'A': '容器内残留少量油脂完全不影响打发效率',
        'B': '必须先将生蛋白加热至沸腾方可形成泡沫',
        'C': '铜质器皿释放的铜离子能显著稳定蛋白霜',
        'D': '混入少许富含卵磷脂的蛋黄利于起泡膨胀'
    }
})

# Q15: 面包制作中「直接法」与「中种法」的最主要工序差异是？
# Ans: B
balanced_data.append({
    'id': 15,
    'ans': 'B',
    'opts': {
        'A': '直接法需添加酸种酵头，中种法仅用化学膨松剂',
        'B': '直接法材料一次性拌匀，中种法分两次发酵搅拌',
        'C': '直接法需经历三天冷藏，中种法可在半小时出炉',
        'D': '直接法成品柔软抗老化，中种法组织紧密易掉渣'
    }
})

# Q16: 面包配方中的「水合率（Hydration Percentage）」通常是指？
# Ans: D
balanced_data.append({
    'id': 16,
    'ans': 'D',
    'opts': {
        'A': '面团从搅拌完成到烘烤出炉的蒸发水分比例',
        'B': '出炉面包表皮与面包心之间的相对水分梯度',
        'C': '面团吸收空气中环境相对湿度的最大饱和度',
        'D': '配方中总加水量占面粉总重量的烘焙百分比'
    }
})

# Q17: 制作法式卡士达酱（Crème Pâtissière）时，蛋黄的关键作用是？
# Ans: A
balanced_data.append({
    'id': 17,
    'ans': 'A',
    'opts': {
        'A': '提供天然卵磷脂乳化增稠并在受热变性后定型',
        'B': '完全分解面粉中的直链淀粉以保持透明质感',
        'C': '使酱料质地呈透明胶状并大幅度降低热量值',
        'D': '充当天然化学膨大剂在冷藏时释放微小气泡'
    }
})

# Q18: 下列哪种蛋糕在分类上明确属于「油脂蛋糕类（Shortened Cake）」？
# Ans: B
balanced_data.append({
    'id': 18,
    'ans': 'B',
    'opts': {
        'A': '天使蛋糕（Angel Food Cake）',
        'B': '重奶油磅蛋糕（Pound Cake）',
        'C': '日式轻乳酪（Soufflé Cheese）',
        'D': '分蛋戚风蛋糕（Chiffon Cake）'
    }
})

# Q19: 优质吐司面包切面呈现明显的「拉丝」口感，其微观成因是？
# Ans: C
balanced_data.append({
    'id': 19,
    'ans': 'C',
    'opts': {
        'A': '配方中添加了过量未融化的固态起酥油脂',
        'B': '内部淀粉在烘烤中未充分糊化保留生粉性',
        'C': '充分扩展的面筋薄膜网络经定向延展定向排列',
        'D': '由于多次冷冻复温导致的蛋白质水分子脱离'
    }
})

# Q20: 开心果粉（Pistachio Meal）在现代高级法式甜点中的主要功能是？
# Ans: D
balanced_data.append({
    'id': 20,
    'ans': 'D',
    'opts': {
        'A': '替代面粉中的强力面筋以支撑戚风蛋糕骨架',
        'B': '充当天然酸味中和剂以稳定新鲜水果的酸度',
        'C': '在甘纳许中作为强效吸油剂防止可可脂析出',
        'D': '赋予马卡龙或内馅独特的天然绿色与醇厚坚果香'
    }
})

# Q21: 冻干草莓粉（Freeze-Dried Strawberry Powder）相比热风干燥果粉的核心优势是？
# Ans: A
balanced_data.append({
    'id': 21,
    'ans': 'A',
    'opts': {
        'A': '低温升华脱水完整保留天然果香、色泽与热敏营养',
        'B': '含有极高比例的自由水分能直接替代配方中的鲜奶',
        'C': '经过高温瞬间焦糖化后具备天然的焦糖烘烤香气',
        'D': '在面团中能产生类似酵母的持续发酵产气膨胀功能'
    }
})

# Q22: 法式千层酥（Puff Pastry）在烘烤中产生数百层酥皮的物理膨胀原理是？
# Ans: B
balanced_data.append({
    'id': 22,
    'ans': 'B',
    'opts': {
        'A': '配方中添加了高比例的双重反应型化学泡打粉',
        'B': '黄油层间水分受热急剧汽化产生高压蒸汽顶开面层',
        'C': '耐高糖活性干酵母在高温下进行超高速爆裂产气',
        'D': '面粉中高筋蛋白在遇热收缩时产生强烈反弹推力'
    }
})

# Q23: 制作法式甘纳许（Ganache）的基础原料组合是？
# Ans: C
balanced_data.append({
    'id': 23,
    'ans': 'C',
    'opts': {
        'A': '无盐黄油搭配高细度白砂糖粉',
        'B': '打发蛋白霜混合无糖纯可可粉',
        'C': '煮沸液体鲜奶油与优质纯巧克力',
        'D': '脱脂纯牛奶与高熔点氢化植物油'
    }
})

# Q24: 在工业与手工冰淇淋中加入食品稳定剂（如刺槐豆胶）的主要作用是？
# Ans: D
balanced_data.append({
    'id': 24,
    'ans': 'D',
    'opts': {
        'A': '大幅提高成品的甜度以降低糖的用量',
        'B': '彻底杀灭原料乳中可能存留的嗜冷细菌',
        'C': '在冷冻过程中加速冰晶的快速聚集粗化',
        'D': '结合游离水抑制粗大冰晶生成并延缓融化'
    }
})

# Q25: 古斯米（Couscous）起源于哪个区域，其传统原料是什么？
# Ans: A
balanced_data.append({
    'id': 25,
    'ans': 'A',
    'opts': {
        'A': '北非地区，以硬质杜兰小麦粗粒粉加水搓粒蒸制',
        'B': '意大利北部，以软质低筋白面粉加鲜蛋揉捏成团',
        'C': '东南亚地区，以长粒籼米蒸熟后经日光自然晒干',
        'D': '南美洲山区，以去皮印第安马铃薯经捣泥烘干制成'
    }
})

# Q26: 经典法式甜点「松露巧克力（Truffles）」的命名直接来源于？
# Ans: B
balanced_data.append({
    'id': 26,
    'ans': 'B',
    'opts': {
        'A': '制作配方中必须浸泡昂贵的法国黑松露菌切片',
        'B': '外形凹凸且滚满可可粉酷似出土的新鲜黑松露',
        'C': '最早由盛产名贵菌类的法国南部松露猎人发明',
        'D': '入口带有浓烈的天然林地泥土气味与菌菇芳香'
    }
})

# Q27: 法式拿破仑酥「Mille-feuille」的字面原始含义是指？
# Ans: C
balanced_data.append({
    'id': 27,
    'ans': 'C',
    'opts': {
        'A': '拿破仑皇帝在战地常备的特制口粮',
        'B': '蕴含着一千种馥郁风味的经典甜品',
        'C': '由如同层叠千片轻盈树叶构成的酥皮',
        'D': '经过一千次手工反复捶打折叠的面团'
    }
})

# Q28: 制作巧克力的可可豆初加工标准工序流程，正确的是？
# Ans: D
balanced_data.append({
    'id': 28,
    'ans': 'D',
    'opts': {
        'A': '烘焙→发酵→干燥→研磨→去壳',
        'B': '研磨→去壳→发酵→烘焙→干燥',
        'C': '去壳→干燥→研磨→发酵→烘焙',
        'D': '发酵→干燥→烘焙→去壳→研磨'
    }
})

# Q29: 制作法式焦糖布丁时，采用「水浴隔水烘烤（Bain-Marie）」的核心考量是？
# Ans: A
balanced_data.append({
    'id': 29,
    'ans': 'A',
    'opts': {
        'A': '利用水温恒定温和传热防止蛋液过热沸腾产生蜂窝孔洞',
        'B': '使烤箱内部充满水蒸气以大幅度加速模具内蛋液凝固',
        'C': '稀释模具内部糖液浓度以防止布丁底部焦糖过快焦黑',
        'D': '促使布丁表面迅速结皮形成类似法式脆皮的厚硬外壳'
    }
})

# Q30: 澳新代表性名点「帕夫洛娃（Pavlova）」的典型结构特征是？
# Ans: B
balanced_data.append({
    'id': 30,
    'ans': 'B',
    'opts': {
        'A': '底层为坚硬黄油挞皮，中间填入浓稠酸甜柠檬乳酪酱',
        'B': '外壳酥脆内部如棉花糖般轻柔的蛋白霜顶覆新鲜水果',
        'C': '层层相间的多层巧克力海绵蛋糕刷满樱桃利口酒糖浆',
        'D': '以大量焦化黄油与未打发蛋白烤制的金黄色长条小点'
    }
})

# Q31: 糖在硬脆饼干与松软小西点中的不同物理表现，主要是由于？
# Ans: C
balanced_data.append({
    'id': 31,
    'ans': 'C',
    'opts': {
        'A': '白砂糖在常温搅拌过程中极易氧化导致面筋过快硬化',
        'B': '糖粉能够完全抑制油脂融合促使饼干产生极厚酥脆层',
        'C': '粗砂糖未完全溶解形成脆裂晶体，糖粉溶解度高质地细腻',
        'D': '细砂糖遇热分解出大量天然水分使饼干变得湿润且绵软'
    }
})

# Q32: 「乳化现象（Emulsification）」在烘焙搅拌工艺中的本质作用是？
# Ans: D
balanced_data.append({
    'id': 32,
    'ans': 'D',
    'opts': {
        'A': '彻底排空面团内部多余空气以增强烘烤成品的紧实密度',
        'B': '促使蛋白质快速水解成单体氨基酸以提升面团的柔软度',
        'C': '降低面糊整体温度防止黄油中的天然乳脂过早发生融化',
        'D': '借助表面活性剂使互不相溶的水相与油相形成均质分散系'
    }
})

# Q33: 现代商业面包酵母与传统天然酸种酵头相比，最突出的工艺区别是？
# Ans: A
balanced_data.append({
    'id': 33,
    'ans': 'A',
    'opts': {
        'A': '单一纯种酿酒酵母产气迅速稳定，酸种含共生菌群发酵慢风味繁复',
        'B': '商业酵母发酵需要添加大量醋酸，酸种酵头完全依赖天然中性发酵',
        'C': '商业酵母仅能在真空环境中产气，酸种酵头可在有氧常压自由呼吸',
        'D': '商业酵母烘烤后具有强烈麦香，酸种酵头成品则完全没有酸味特征'
    }
})

# Q34: 瑞士卷蛋糕片出炉后为何通常需在尚存温热状态下预卷或脱模？
# Ans: B
balanced_data.append({
    'id': 34,
    'ans': 'B',
    'opts': {
        'A': '趁热快速卷起可以最大程度加速蛋糕中心热量向外散逸',
        'B': '温热状态下淀粉与面筋结构柔韧延展性好，冷却硬化后易断裂',
        'C': '高温能使内馅涂抹的打发纯鲜奶油保持高度稳定不发生融化',
        'D': '趁热受力能迫使表皮毛孔完全闭合防止蛋糕内部的水分散失'
    }
})

# Q35: 传统中式名点「蛋黄酥」外皮酥脆分明的关键开酥工艺是？
# Ans: C
balanced_data.append({
    'id': 35,
    'ans': 'C',
    'opts': {
        'A': '纯粹依赖法式冷藏裹入黄油进行多次四折的开酥手法',
        'B': '将水油面团油炸熟透后再包入豆沙蛋黄馅进行二次烘烤',
        'C': '以具延展性的水油皮包裹纯油酥经擀卷形成明暗交替酥层',
        'D': '面粉中加入大量重碳酸氢铵在高温烘烤下剧烈崩解分层'
    }
})

# Q36: 蛋糕切层组装前涂刷「糖浆（Punch Syrup）」的主要工艺目的不包含？
# Ans: D
balanced_data.append({
    'id': 36,
    'ans': 'D',
    'opts': {
        'A': '增加蛋糕胚体湿润度防止在冷藏陈列中失水变干',
        'B': '增添酒香或果香提升甜品整体层次丰富的风味',
        'C': '降低局部水分活度在一定程度上延缓微生物滋生',
        'D': '充当天然化学膨大剂使蛋糕在冷藏期间继续膨胀'
    }
})

# Q37: 法式传统点心「费南雪（Financier）」的核心标志性原料工艺是？
# Ans: A
balanced_data.append({
    'id': 37,
    'ans': 'A',
    'opts': {
        'A': '焦化榛果黄油与大量杏仁粉及未经打发的纯蛋白',
        'B': '全蛋高速打发至浓稠羽毛状后拌入高筋强韧面粉',
        'C': '新鲜重质酸奶油混合大量融化纯白巧克力与蛋黄',
        'D': '发酵面种加入大量黑麦粉与浸泡朗姆酒的葡萄干'
    }
})

# Q38: 关于乳酪在烘焙糕点中的经典应用配对，下列哪项明显错误？
# Ans: B
balanced_data.append({
    'id': 38,
    'ans': 'B',
    'opts': {
        'A': '奶油乳酪（Cream Cheese）是重芝士蛋糕主体原料',
        'B': '里科塔乳酪（Ricotta）是制作传统可颂的开酥油脂',
        'C': '马斯卡彭（Mascarpone）是传统提拉米苏的核心基底',
        'D': '帕玛森乳酪（Parmesan）常用于法式咸味泡芙调香'
    }
})

# Q39: 百香果（Passion Fruit）在现代精品法式烘焙中常作为重要原料，主要原因是？
# Ans: C
balanced_data.append({
    'id': 39,
    'ans': 'C',
    'opts': {
        'A': '富含极强油脂成分能直接替代配方中的固体可可脂',
        'B': '其籽粒提取物具有强效防腐杀菌功能延长保质期',
        'C': '高酸度与强烈热带芳香能完美平衡甘纳许与奶油甜腻',
        'D': '在面糊中充当纯天然膨松剂以促使蛋糕体积膨胀'
    }
})

# Q40: 在烘焙百分比计算中，配方以面粉重量312g为基准（100%），若鸡蛋比例为167%，则鸡蛋实际需用量约为？
# Ans: D
balanced_data.append({
    'id': 40,
    'ans': 'D',
    'opts': {
        'A': '187g',
        'B': '312g',
        'C': '468g',
        'D': '521g'
    }
})


# ==========================================
# Group B: 西餐烹饪理论 (Q41 ~ Q50)
# Target Keys: 3 A, 2 B, 3 C, 2 D
# ==========================================

# Q41: 西餐后厨工作准则中常强调的「Mise en Place」核心含义是？
# Ans: D
balanced_data.append({
    'id': 41,
    'ans': 'D',
    'opts': {
        'A': '每位厨师必须在出餐结束后彻底清点冷库的所有剩余存货',
        'B': '严格按照欧洲古典宫廷菜肴标准进行毫无改动的传统复刻',
        'C': '使用标准电子秤严格称量并精确计算每道菜品的食材成本',
        'D': '在正式烹调开单前将所有工器具与食材预先处理定位就绪'
    }
})

# Q42: 真空低温慢煮（Sous-Vide）烹调高档牛排的核心技术优势是？
# Ans: A
balanced_data.append({
    'id': 42,
    'ans': 'A',
    'opts': {
        'A': '精准水浴使肉质内外均匀达到目标熟度再快煎上色',
        'B': '完全省略高温煎烤步骤从真空袋取出即可直接切盘',
        'C': '通过超高压蒸气使结缔组织在数分钟之内彻底融化',
        'D': '能在零下低温环境中彻底杀灭肉品表面的一切细菌'
    }
})

# Q43: 法国普罗旺斯地标名菜「马赛鱼汤（Bouillabaisse）」的经典用料组合是？
# Ans: C
balanced_data.append({
    'id': 43,
    'ans': 'C',
    'opts': {
        'A': '北西洋大西洋鲑鱼搭配浓厚重奶油及马铃薯炖煮',
        'B': '鲜活澳洲龙虾搭配黑松露菌片及意大利红酒焖烧',
        'C': '多种地中海杂鱼贝类加番红花、茴香与番茄慢熬成汤',
        'D': '高档牛里脊肉块搭配洋葱头、西芹与白葡萄酒清炖'
    }
})

# Q44: 牛肉「菲力（Tenderloin）」部位的肌理特点与最适烹饪手法是？
# Ans: B
balanced_data.append({
    'id': 44,
    'ans': 'B',
    'opts': {
        'A': '结缔组织极其粗硬耐嚼，必须通过长时间文火砂锅炖煮',
        'B': '肌肉运动极少纤维最嫩脂肪低，适宜高温快煎或快烤',
        'C': '肌间脂肪雪花密布油分极重，最适宜长时间烟熏脱脂',
        'D': '富含大量骨胶原蛋白，只适合切块用于慢炖浓稠高汤'
    }
})

# Q45: 制作经典西班牙烩饭（Paella）的灵魂食材与传统烹饪器具是？
# Ans: A
balanced_data.append({
    'id': 45,
    'ans': 'A',
    'opts': {
        'A': '高吸水短粒米（Bomba）与专用浅底双耳宽口平底铁锅',
        'B': '细长型印度香米（Basmati）与高深度带盖圆形砂锅',
        'C': '意大利长粒高淀粉米与传统厚底带柄不锈钢深口炒锅',
        'D': '泰国茉莉香米与带有密集小孔的传统竹制圆形蒸笼'
    }
})

# Q46: 制作正统法式吐司（French Toast）时，面包浸润与烹制的规范工序是？
# Ans: C
balanced_data.append({
    'id': 46,
    'ans': 'C',
    'opts': {
        'A': '先在热干锅中两面烤焦再迅速淋入冰镇未打散的生全蛋液',
        'B': '面包单面沾裹纯牛奶后立刻放入高温深油锅中炸至金黄',
        'C': '将厚切面包充分浸泡蛋奶香草混合液再用黄油双面温煎',
        'D': '先将面包均匀滚满干面包糠后再浸入高浓度纯枫糖浆中'
    }
})

# Q47: 西餐冷开胃菜「塔塔生牛肉（Steak Tartare）」的典型制作特征是？
# Ans: B
balanced_data.append({
    'id': 47,
    'ans': 'B',
    'opts': {
        'A': '整块牛排用喷枪炙烤至三分熟后切成厚片冷藏上桌',
        'B': '新鲜极嫩牛肉细致手切拌入生蛋黄酸豆洋葱全生食用',
        'C': '牛肉末用红酒与香草腌渍入味后置于烤箱中烤至全熟',
        'D': '将牛绞肉煮熟挤干水分后再加入大量美乃滋搅拌冷食'
    }
})

# Q48: 法式焦糖布丁（Crème Brûlée）出餐前在表层形成硬脆焦糖层的专业工具是？
# Ans: D
balanced_data.append({
    'id': 48,
    'ans': 'D',
    'opts': {
        'A': '微波炉高火转动加热十秒钟',
        'B': '家用热风电吹风持续近距离强吹',
        'C': '炉灶高压大火直接熏烤碗体外部',
        'D': '手持专业喷枪或顶部上火焗炉'
    }
})

# Q49: 法式传统烹饪技法「油封（Confit）」的定义与工艺特征是？
# Ans: A
balanced_data.append({
    'id': 49,
    'ans': 'A',
    'opts': {
        'A': '腌渍肉类完全浸入自身油脂中低温慢烹熟化并隔绝空气保存',
        'B': '将生鲜食材置于高温深油锅中瞬间炸至外壳金黄酥脆脱水',
        'C': '将肉类表面刷满植物油后挂在炭火上方利用冷烟长时间慢熏',
        'D': '利用饱和纯水蒸气在密闭压力舱内将禽肉完全蒸至软烂脱骨'
    }
})

# Q50: 西餐熟食冷肉冷盘类制品「Charcuterie」主要涵盖的经典品类包括？
# Ans: C
balanced_data.append({
    'id': 50,
    'ans': 'C',
    'opts': {
        'A': '仅包括未经过任何发酵处理的纯深海生鱼片与贝类',
        'B': '仅包括纯蔬菜类经天然乳酸发酵脱水制成的酸渍泡菜',
        'C': '风干香肠、肉酱、肉冻、生火腿等腌制或风干熟肉制品',
        'D': '仅涵盖经过高温烘烤后立即切片食用的全熟热牛排拼盘'
    }
})


# ==========================================
# Group C: 亚洲与中餐烹饪理论 (Q51 ~ Q60)
# Target Keys: 2 A, 3 B, 2 C, 3 D
# ==========================================

# Q51: 中餐滑炒菜肴前对主料进行的「滑油（温油划散）」核心工艺目的是？
# Ans: B
balanced_data.append({
    'id': 51,
    'ans': 'B',
    'opts': {
        'A': '用八成热烈油使食材外皮瞬间炸脆焦黄并完全收干肉汁',
        'B': '使上浆原料在三至四成温油中划散定型并锁住内部水分',
        'C': '彻底排出原料内部所吸收的油脂以降低菜品的总热量',
        'D': '利用高温油脂瞬间杀灭食材深处可能潜伏的致病细菌'
    }
})

# Q52: 中餐烹调中「挂糊」与「上浆」在工艺形态与用途上的核心区别是？
# Ans: D
balanced_data.append({
    'id': 52,
    'ans': 'D',
    'opts': {
        'A': '挂糊专门用于低温水煮菜肴，上浆专门用于明火炭烤菜肴',
        'B': '挂糊仅适用于淡水活鱼，上浆则严格限制于禽肉与红肉类',
        'C': '两者配料完全一样，仅因不同地域方言产生叫法上的差异',
        'D': '挂糊浆层较厚常用于炸熘，上浆浆层极薄多用于滑炒水汆'
    }
})

# Q53: 传统川菜理论中所称的「七滋」，完整规范的内容是？
# Ans: A
balanced_data.append({
    'id': 53,
    'ans': 'A',
    'opts': {
        'A': '酸、甜、苦、辣、咸、鲜、香',
        'B': '麻、辣、酸、甜、鲜、苦、涩',
        'C': '咸、鲜、焦、香、甜、酸、辣',
        'D': '麻、香、咸、淡、苦、滑、脆'
    }
})

# Q54: 浙菜代表名作「东坡肉」的标准成菜工艺与发源地是？
# Ans: B
balanced_data.append({
    'id': 54,
    'ans': 'B',
    'opts': {
        'A': '猪瘦肉经裹糊油炸后浇淋酸甜糖醋芡汁，发源于北京',
        'B': '带皮五花肉块加黄酒酱油冰糖文火慢焖，发源于杭州',
        'C': '整只猪肘经高压大火清炖后淋上麻辣红油，发源于成都',
        'D': '排骨经长时间炭火烤制后刷上甜面酱汁，发源于广州'
    }
})

# Q55: 闽菜顶级名馔「佛跳墙」的主要工艺特征与用料结构是？
# Ans: C
balanced_data.append({
    'id': 55,
    'ans': 'C',
    'opts': {
        'A': '以新鲜活鱼头搭配老豆腐文火快熬成奶白色汤羹',
        'B': '以整只填鸭经挂炉果木烘烤后片皮搭配甜面酱卷饼',
        'C': '鲍参翅肚等名贵干货汇聚坛中加绍酒高汤文火慢煨',
        'D': '选用优质牛羊杂碎投入麻辣牛油锅底中长时间翻滚'
    }
})

# Q56: 马来西亚风味面食「亚参叻沙（Asam Laksa）」最具辨识度的风味与汤底特征是？
# Ans: D
balanced_data.append({
    'id': 56,
    'ans': 'D',
    'opts': {
        'A': '以大量浓厚新鲜椰浆为底，色泽金黄温润且微辣',
        'B': '以醇厚牛骨高汤为底，加入大量沙茶酱与花生碎',
        'C': '以清甜鸡汤为底，仅用白胡椒粉与新鲜豆芽调味',
        'D': '以鲜鱼熬汤加罗望子调酸，不加椰奶呈现酸辣鲜爽'
    }
})

# Q57: 中餐上浆技术中，最基础的「水粉浆」主要原料配比是？
# Ans: A
balanced_data.append({
    'id': 57,
    'ans': 'A',
    'opts': {
        'A': '淀粉与适量清水（常配合少许精盐与料酒）',
        'B': '全蛋液与优质细面包糠（常搭配辣椒粉）',
        'C': '高筋面粉与双效泡打粉（需常温发酵两小时）',
        'D': '纯蛋黄与大量熟猪油（需隔水完全加热乳化）'
    }
})

# Q58: 中餐经典技法「清蒸」的工艺特点与最适宜原料属性是？
# Ans: B
balanced_data.append({
    'id': 58,
    'ans': 'B',
    'opts': {
        'A': '利用低温干燥热风长久烘烤，适宜油脂丰腴的整禽',
        'B': '利用纯饱和水蒸气温和加热，适宜新鲜质嫩的原汁食材',
        'C': '利用沸腾红油翻滚浸炸，适宜筋膜粗壮的红肉块',
        'D': '利用冷水浸泡慢炖，适宜坚硬耐煮的草本根茎干货'
    }
})

# Q59: 传统天然酿造酱油在发酵熟化中产生浓郁「鲜味（Umami）」的核心生化物质是？
# Ans: C
balanced_data.append({
    'id': 59,
    'ans': 'C',
    'opts': {
        'A': '氯化钠晶体在水溶液中电离出的大量纯钠离子',
        'B': '烘炒小麦粉在高温焦糖化过程中产生的焦糖色素',
        'C': '大豆蛋白质在酶解中释放出的游离谷氨酸及氨基酸',
        'D': '醋酸菌在有氧呼吸发酵过程中所代谢产生的高浓度乙酸'
    }
})

# Q60: 历来作为中国古典宫廷盛宴典范的「满汉全席」，其核心美学代表特征不包含？
# Ans: D
balanced_data.append({
    'id': 60,
    'ans': 'D',
    'opts': {
        'A': '汇聚南北珍馐百味的海量佳肴品类',
        'B': '融合满汉传统烹调精华的高超烹饪技艺',
        'C': '讲究金银玉石与景泰蓝搭配的精致器皿',
        'D': '故意拖延用餐节奏的虚伪繁复繁文缛节'
    }
})

print(f"Total balanced questions created: {len(balanced_data)}")

# Verify answer distribution
keys = {}
group_keys = {'A': {}, 'B': {}, 'C': {}}

for q in balanced_data:
    qid = q['id']
    ans = q['ans']
    keys[ans] = keys.get(ans, 0) + 1
    
    g = 'A' if qid <= 40 else ('B' if qid <= 50 else 'C')
    group_keys[g][ans] = group_keys[g].get(ans, 0) + 1

print("\n=== ANSWER KEY DISTRIBUTION ===")
print("Total Keys (Target: 15 A, 15 B, 15 C, 15 D):", keys)
print("Group A (Target: 10 A, 10 B, 10 C, 10 D):", group_keys['A'])
print("Group B (Target: 3 A, 2 B, 3 C, 2 D):", group_keys['B'])
print("Group C (Target: 2 A, 3 B, 2 C, 3 D):", group_keys['C'])

# Verify option length span
print("\n=== AUDITING OPTION LENGTHS ===")
max_span_allowed = 4
imbalanced = []

for q in balanced_data:
    qid = q['id']
    opts = q['opts']
    lens = {k: len(v) for k, v in opts.items()}
    min_len = min(lens.values())
    max_len = max(lens.values())
    span = max_len - min_len
    if span > max_span_allowed:
        imbalanced.append((qid, span, lens, q))

if imbalanced:
    print(f"FAILED: {len(imbalanced)} questions have span > {max_span_allowed}:")
    for qid, span, lens, q in imbalanced:
        print(f"Q{qid}: span={span}, lens={lens}")
        for k, v in q['opts'].items():
            print(f"  {k}: {v} ({len(v)})")
else:
    print(f"SUCCESS: All 60 questions have option length span <= {max_span_allowed} characters!")

# Combine with old question metadata (g, src, exp)
final_questions = []
for q in balanced_data:
    qid = q['id']
    old_q = old_qs[qid]
    final_questions.append({
        'id': qid,
        'g': old_q['g'],
        'src': old_q['src'],
        'q': old_q['q'],
        'opts': q['opts'],
        'ans': q['ans'],
        'exp': old_q['exp']
    })

with open('work/paperB_balanced.json', 'w', encoding='utf-8') as f:
    json.dump(final_questions, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(final_questions)} balanced questions to work/paperB_balanced.json!")
