import json
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

# Target Distribution:
# Easy Q01-Q20: 5 A, 5 B, 5 C, 5 D
# Med+Hard Q21-Q40: 5 A, 5 B, 5 C, 5 D
# Total Q01-Q40: 10 A, 10 B, 10 C, 10 D

questions = [
  # Easy Q01-Q20
  {
    "id": 1,
    "difficulty": "easy",
    "type": "single",
    "question": "在法式古典烹饪殿堂体系中，五大母酱（Mother Sauces）的正式法文统称是：",
    "options": {
      "A": "Grandes Sauces（奠定现代西餐酱汁根基的法式古典五大母酱）",
      "B": "Petites Sauces（由母酱进一步调味派生出的丰富次级佐餐小酱）",
      "C": "Vinaigrettes（以橄榄油与果醋调配的传统冷拌沙拉专用油醋汁）",
      "D": "Coulis（选用新鲜果蔬未经浓缩熬煮直接过滤而成的纯净原汁）"
    },
    "answer": "A",
    "explanation": "五大母酱在法餐中统称 Grandes Sauces（或 Sauces Mères），是法式烹饪大师埃斯科菲耶（Escoffier）系统化分类的核心基石。"
  },
  {
    "id": 2,
    "difficulty": "easy",
    "type": "single",
    "question": "制作法式白酱（Sauce Béchamel）时，核心的基础液体原料与增稠剂是：",
    "options": {
      "A": "澄清牛骨高汤配合大火炒制十五分钟的深褐油面糊",
      "B": "温热牛奶配合小火轻炒去生粉味的纯白油面糊",
      "C": "新鲜番茄纯果泥配合发酵熟化的高浓度红葡萄醋",
      "D": "纯蛋黄配合澄清脱水处理的纯乳脂液态澄清黄油"
    },
    "answer": "B",
    "explanation": "白酱（Béchamel）由温热纯牛奶注入白油面糊（Roux blanc）微沸熬煮而成，常加入肉豆蔻（Nutmeg）与白胡椒调味。"
  },
  {
    "id": 3,
    "difficulty": "easy",
    "type": "single",
    "question": "制作法式丝绒酱（Sauce Velouté）时，标准采用的液体基底是：",
    "options": {
      "A": "经过八小时重度烤骨熬制的深黑色重口味西班牙烤牛骨原汤",
      "B": "纯鲜牛奶配合动物淡奶油以等比例混合调制的浓稠白奶汁",
      "C": "白高汤（鸡骨、小牛肉骨或鱼骨熬制的清澈高汤）搭配黄面糊",
      "D": "初榨橄榄油与红葡萄酒醋按三比一调配的冷调和乳化乳液"
    },
    "answer": "C",
    "explanation": "Velouté（丝绒酱）采用白高汤（White stock，如小牛骨、鸡骨或鱼高汤）与金黄油面糊（Roux blond）熬制而成，质感如丝绒般顺滑。"
  },
  {
    "id": 4,
    "difficulty": "easy",
    "type": "single",
    "question": "五大母酱中唯一的【温热乳化型】母酱（Warm Emulsion Sauce）是：",
    "options": {
      "A": "西班牙褐酱（Sauce Espagnole传统浓稠深棕色烤牛骨褐酱）",
      "B": "番茄母酱（Sauce Tomate添加新鲜芳香蔬菜慢炖番茄酱汁）",
      "C": "法式白酱（Sauce Béchamel牛奶配合纯白油面糊之奶香白酱）",
      "D": "荷兰酱（Sauce Hollandaise澄清黄油与温热蛋黄温热乳化酱）"
    },
    "answer": "D",
    "explanation": "荷兰酱（Hollandaise）完全不依靠面糊增稠，而是依靠温热蛋黄中的卵磷脂与澄清黄油在58~62℃温浴下形成温热水包油（O/W）乳化体系。"
  },
  {
    "id": 5,
    "difficulty": "easy",
    "type": "single",
    "question": "法式传统油面糊（Roux）在配方中的标准用料比例（质量比）是：",
    "options": {
      "A": "纯澄清黄油与小麦面粉按一比一的精准质量比例（1:1）",
      "B": "纯白砂糖与低筋蛋糕粉按三比一的大比例混合加热炒制",
      "C": "玉米淀粉与纯冷水按一比五的稀薄比例直接兑开调匀使用",
      "D": "植物起酥油与纯食盐按十比一的超咸比例进行高温熬煮"
    },
    "answer": "A",
    "explanation": "制作经典法式油面糊（Roux）的基准比例为油脂（通常为澄清黄油）与中筋或低筋面粉质量比 1:1。"
  },
  {
    "id": 6,
    "difficulty": "easy",
    "type": "single",
    "question": "制作荷兰酱时使用的“澄清黄油（Clarified Butter）”，其主要工艺目的是：",
    "options": {
      "A": "使黄油中水分含量提升至百分之五十以上以增加流动延展度",
      "B": "去除黄油中的水分与酪蛋白乳固体，获得纯度超99%的纯乳脂",
      "C": "通过高温炭化使其产生如同深黑色黑巧克力般的烟熏苦焦味",
      "D": "使黄油中的饱和脂肪酸彻底转化为能够永久不凝固的植物酸"
    },
    "answer": "B",
    "explanation": "普通黄油含约80~82%乳脂、16~18%水及1~2%牛奶固体。澄清黄油去除了水和乳清蛋白杂质，乳脂纯度>99%，乳化性能稳定且烟点显著提高。"
  },
  {
    "id": 7,
    "difficulty": "easy",
    "type": "single",
    "question": "制作荷兰酱时，隔水温浴加热（Bain-marie）的安全操作温度区间严格锁定在：",
    "options": {
      "A": "二十度至三十度的常温冷凉温区",
      "B": "八十度至九十度的微沸剧烈温区",
      "C": "五十八度至六十二度的温和乳化温区",
      "D": "零下五度至零度的冰冻低温温区"
    },
    "answer": "C",
    "explanation": "荷兰酱温控极为严苛：低于55℃澄清黄油会重新凝固结晶导致析油；高于65℃蛋黄受热变性凝固成“炒蛋颗粒”导致破乳。最佳安全窗口为58~62℃。"
  },
  {
    "id": 8,
    "difficulty": "easy",
    "type": "single",
    "question": "在白酱（Béchamel）中融入格吕耶尔（Gruyère）芝士碎与蛋黄所派生出的经典名酱是：",
    "options": {
      "A": "千岛酱（Thousand Island经典沙拉冷拌冷酱）",
      "B": "鞑靼酱（Tartar Sauce搭配炸海鲜之酸甜冷酱）",
      "C": "贝亚恩斯酱（Sauce Béarnaise牛排专用温热酱）",
      "D": "莫奈酱（Sauce Mornay经典焗烤专用浓郁芝士酱）"
    },
    "answer": "D",
    "explanation": "Sauce Mornay（莫奈酱）是白酱最负盛名的衍生酱，加入格吕耶尔奶酪或车达奶酪融化并拌入蛋黄，用于各种焗烤菜肴（Gratin）。"
  },
  {
    "id": 9,
    "difficulty": "easy",
    "type": "single",
    "question": "以荷兰酱为基础，加入新鲜茵陈蒿（Tarragon）、红葱头及白葡萄酒醋浓缩液调制的经典牛排排酱是：",
    "options": {
      "A": "贝亚恩斯酱（Sauce Béarnaise香草酸香温热酱）",
      "B": "西班牙褐酱（Sauce Espagnole法式传统经典大酱）",
      "C": "美式烤肉酱（BBQ Sauce烟熏甜辣美洲传统酱汁）",
      "D": "热那亚青酱（Pesto Genovese松子罗勒冷拌坚果酱）"
    },
    "answer": "A",
    "explanation": "Sauce Béarnaise（贝亚恩斯酱）是荷兰酱的孪生姐妹酱，以茵陈蒿、红葱头和醋还原液调味，与烤牛排、煎牛柳是天作之合。"
  },
  {
    "id": 10,
    "difficulty": "easy",
    "type": "single",
    "question": "经典冷酱美乃滋（Mayonnaise）在物理化学胶体分类中，属于哪种乳化体系：",
    "options": {
      "A": "水包油型（O/W型）永久性冷乳化胶体分散体系",
      "B": "油包水型（W/O型）非均相固态结晶油蜡保护体系",
      "C": "气包水型（W/A型）轻质微孔发泡海绵泡沫悬浮体系",
      "D": "固液复合型（S/L型）粗颗粒沉淀过滤悬浊分离体系"
    },
    "answer": "A",
    "explanation": "美乃滋是由蛋黄中的卵磷脂作为乳化剂，将大量的植物油微滴分散包裹在少量水相（醋/柠檬汁/蛋黄水分）中形成的高稠度水包油（O/W）乳化体系。"
  },
  {
    "id": 11,
    "difficulty": "easy",
    "type": "single",
    "question": "调配经典法式油醋汁（French Vinaigrette）时，色拉油与食醋的标准传统体积配比通常为：",
    "options": {
      "A": "油与醋按一比一的等量混合激烈摇晃配比",
      "B": "油与醋按一比五的极重酸度超强开胃配比",
      "C": "油与醋按三比一的经典黄金配比（3:1）",
      "D": "油与醋按十比一的几乎不含酸味的清淡配比"
    },
    "answer": "C",
    "explanation": "经典油醋汁的标准配比为 3份油 : 1份醋（3:1），加盐、黑胡椒及少许第戎芥末酱（Dijon mustard）辅助乳化。"
  },
  {
    "id": 12,
    "difficulty": "easy",
    "type": "single",
    "question": "若制作法式白酱时，热面糊冲入沸腾热牛奶搅拌不匀，成品最容易产生的物理缺陷是：",
    "options": {
      "A": "液体瞬间彻底结晶硬化为如坚硬岩石般的透明结晶块",
      "B": "酱汁完全变成像矿泉水一样纯清澈透明的流动低黏度液",
      "C": "局部淀粉瞬间剧烈糊化，形成难以化开的面粉疙瘩结块",
      "D": "酱汁内部自然发酵生成大量高浓度酒精散发陈年酒香"
    },
    "answer": "C",
    "explanation": "当热面糊遇到沸腾牛奶时，局部淀粉瞬间糊化成胶团包裹生粉形成结块（Lumps）。标准SOP应遵循“热液体入温凉面糊”或“温热液体分次冲入面糊”，并用蛋抽高速抽打混匀。"
  },
  {
    "id": 13,
    "difficulty": "easy",
    "type": "single",
    "question": "制作美乃滋时，在色拉油加入前，常加入一小勺“第戎芥末酱（Dijon Mustard）”，其核心工艺功能是：",
    "options": {
      "A": "使原本纯白的美乃滋酱汁完全炭化变成纯黑色的墨鱼汁色",
      "B": "利用芥末中的黏多糖与辛辣物质辅助稳定乳化界面防止分层",
      "C": "使蛋黄中的蛋白质瞬间脱水变性沉淀以便彻底滤除蛋黄",
      "D": "中和油脂中的全部甘油三酯使其完全转化为可燃生物柴油"
    },
    "answer": "B",
    "explanation": "第戎芥末酱不仅能赋予温和微辣风味，其含有的植物胶质黏多糖还能充当辅助乳化剂，降低水油界面张力，大幅提升美乃滋乳化稳定性。"
  },
  {
    "id": 14,
    "difficulty": "easy",
    "type": "single",
    "question": "将西班牙褐酱（Sauce Espagnole）与等量棕色小牛骨高汤混合，慢火微沸慢炖浓缩一半后制得的顶级浓缩精华母酱是：",
    "options": {
      "A": "白高汤丝绒浓缩纯清汤（Consommé）",
      "B": "法式传统普罗旺斯杂烩炖菜酱汁（Ratatouille）",
      "C": "热那亚坚果冷拌青酱（Salsa Verde）",
      "D": "半釉汁（Demi-glace香浓红亮法式半糖色调味汁）"
    },
    "answer": "D",
    "explanation": "Demi-glace（半釉汁）是由等量西班牙褐酱和褐色高汤慢火慢煨、浓缩50%制成的镜面光泽浓稠高档西餐母酱精华。"
  },
  {
    "id": 15,
    "difficulty": "easy",
    "type": "single",
    "question": "在法式烹饪中，用黄油与新鲜面粉未经加热揉和而成的软面团小球，用于在出餐最后关头紧急增稠酱汁的秘密武器是：",
    "options": {
      "A": "白面糊（Roux blanc经过小火慢炒三分钟的成熟熟油面糊）",
      "B": "黄面糊（Roux blond经过翻炒带有浓郁坚果麦香的淡金面糊）",
      "C": "曼尼黄油面团（Beurre Manié揉捏冷生黄油面粉球）",
      "D": "澄清黄油（Clarified Butter已去除水分乳固体的纯纯油脂）"
    },
    "answer": "C",
    "explanation": "Beurre Manié（曼尼黄油）是将等量生软黄油和面粉用手揉捏成的小球。油脂包覆面粉颗粒，投入滚烫汤汁中慢慢化开，淀粉均匀糊化增稠且绝不起疙瘩。"
  },
  {
    "id": 16,
    "difficulty": "easy",
    "type": "single",
    "question": "西餐主厨在熬煮褐高汤与西班牙褐酱时，加入经深度烘烤上色的芳香蔬菜组合，该法式蔬菜底料被称为：",
    "options": {
      "A": "香草束（Bouquet Garni用韭葱叶捆扎的百里香与月桂叶）",
      "B": "炒蔬菜粒（Mirepoix洋葱、胡萝卜与西芹经典二比一比一比例）",
      "C": "杜卡调味碎（Dukkah坚果与香料研磨混合的中东复合粉）",
      "D": "酸豆刺山柑碎粒（Capers经过盐渍带有刺激酸味的浆果）"
    },
    "answer": "B",
    "explanation": "Mirepoix（法式芳香蔬菜底料）由洋葱50%、胡萝卜25%、西芹25%（2:1:1比例）组成，烤至微焦棕黄后为高汤与褐酱赋予浓郁底味。"
  },
  {
    "id": 17,
    "difficulty": "easy",
    "type": "single",
    "question": "制作丝绒酱衍生出的高级“艾曼纽酱（Sauce Allemande）”时，用于最后勾芡增稠提质的核心增稠乳液（Liaison）配方是：",
    "options": {
      "A": "纯白砂糖与蒸馏纯净水按一比一调制的浓缩饱和糖浆液",
      "B": "纯蛋黄配合高脂动物鲜奶油（Liaison混合液）",
      "C": "食用明胶片搭配热红葡萄酒彻底融化调和的红亮凝胶汁",
      "D": "纯柠檬浓缩原汁搭配工业食用双效发酵泡打粉酸碱泡沫"
    },
    "answer": "B",
    "explanation": "Liaison为法餐经典增稠修饰乳液，由蛋黄与鲜奶油按比例搅匀调成，在离火微温（约70℃）时缓缓搅入酱汁中，带来极其丝滑丰润的质感。"
  },
  {
    "id": 18,
    "difficulty": "easy",
    "type": "single",
    "question": "在美乃滋中加入切碎的酸黄瓜、水瓜柳（酸豆）、洋葱碎与煮熟碎鸡蛋，调配出的搭配炸鱼薯条的经典英式冷酱是：",
    "options": {
      "A": "千岛沙拉酱（Thousand Island沙拉专用酸甜粉红冷酱）",
      "B": "凯撒沙拉酱（Caesar Dressing含银鱼柳与帕玛森芝士酱）",
      "C": "法式红酒油醋汁（Red Wine Vinaigrette冷头盘调味冷汁）",
      "D": "鞑靼酱（Sauce Tartare经典酸爽解腻炸鱼海鲜伴侣酱）"
    },
    "answer": "D",
    "explanation": "Sauce Tartare（鞑靼酱）以美乃滋为基底，加入水瓜柳（Capers）、酸黄瓜粒、香葱、欧芹等酸香小料拌成，是炸鱼排和炸海鲜的经典灵魂伴侣。"
  },
  {
    "id": 19,
    "difficulty": "easy",
    "type": "single",
    "question": "检验法餐酱汁浓度是否达标的经典流变学标准“挂勺测试（Nappe test）”，其判定标准是：",
    "options": {
      "A": "将金属勺浸入酱汁，取出后酱汁薄薄附着于勺背，手指划过留有一道清晰不合拢的线条",
      "B": "酱汁像水一样瞬间从勺背滑落干净且在金属表面完全不留任何半透明微薄痕迹",
      "C": "酱汁凝结成如同橡皮糖般的坚硬胶体能够将金属勺牢牢粘在锅底完全无法拔出",
      "D": "勺子浸入酱汁中由于发生强烈化学剧烈反应而在五秒内冒烟完全被腐蚀熔化掉"
    },
    "answer": "A",
    "explanation": "Nappe（挂勺）：酱汁浓缩至能均匀附着在勺背上，用手指划过一道线，线条边缘整齐、两侧酱汁不合拢，即为完美的母酱浓稠度。"
  },
  {
    "id": 20,
    "difficulty": "easy",
    "type": "single",
    "question": "在制作经典荷兰酱时，若操作不慎油温超过65℃导致破乳分层，表面漂浮大量清澈黄油，其微观破乳机理是：",
    "options": {
      "A": "澄清黄油中的纯乳脂受热彻底分解挥发成不可见的易燃可燃气体",
      "B": "加入的食盐与黑胡椒颗粒发生强力物理研磨切削破坏了所有液体分子",
      "C": "白葡萄酒醋中的醋酸与水分子结合形成不溶于任何液体的固态石霜层",
      "D": "蛋黄中的蛋白质受热变性凝固结块，失去对油滴的包裹保护与乳化能力"
    },
    "answer": "D",
    "explanation": "温度超65℃会使蛋黄卵磷脂保护蛋白彻底热变性凝固成“熟蛋花碎”，水油界面膜瞬间碎裂瓦解，原本被乳化的微细黄油滴重新汇聚分离出油。"
  },

  # Medium Q21-Q35 (Target Med+Hard: 5A, 5B, 5C, 5D. Med: 4A, 4B, 4C, 3D; Hard: 1A, 1B, 1C, 2D)
  {
    "id": 21,
    "difficulty": "medium",
    "type": "single",
    "question": "在油面糊（Roux）制作中，随着炒制时间延长与颜色加深（白面糊->黄面糊->褐面糊），其增稠能力产生反直觉下降的微观机理是：",
    "options": {
      "A": "澄清黄油在持续加热中完全转化为水分导致面糊整体含水量极度超标",
      "B": "面粉中的麦胶蛋白与麦谷蛋白受热交联生成如同石头般的坚硬不溶物",
      "C": "高温使淀粉大分子热解断链为低分子糊精（Dextrin），丧失吸水网架",
      "D": "空气中的二氧化碳被面糊剧烈吸收生成碳酸钙沉淀物破坏了黏性胶体"
    },
    "answer": "C",
    "explanation": "淀粉在高温翻炒中经历热解糊精化（Dextrinization），长链淀粉分子断裂成短链糊精，吸水膨胀网膜能力大幅退化，褐面糊的增稠力仅为白面糊的50%左右。"
  },
  {
    "id": 22,
    "difficulty": "medium",
    "type": "single",
    "question": "因为褐面糊（Roux brun）增稠力因糊精化下降50%，西点主厨制作等量浓稠度的西班牙褐酱时，规范的工艺应对策略是：",
    "options": {
      "A": "将高汤的加热温度强行提升至三百度以迫使糊精分子重新接合聚合成链",
      "B": "在出锅前加入大量未经稀释的工业高浓度双效化学泡打粉产生酸性凝块",
      "C": "将整锅褐酱倒入高速脱水甩干机中脱去百分之九十的水分以实现被动浓缩",
      "D": "将褐面糊的用量提升至白面糊的一点五至两倍（1.5~2x），以补足增稠力"
    },
    "answer": "D",
    "explanation": "由于深色褐面糊增稠能力严重减损，为了达到与白酱相同的浓稠度（Nappe），制作褐酱时使用的Roux量必须增加1.5~2倍，以麦香与焦香弥补物理黏稠度。"
  },
  {
    "id": 23,
    "difficulty": "medium",
    "type": "single",
    "question": "制作冷酱美乃滋时，如果刚开始加植物油就倾倒过快，乳化体系最容易发生：",
    "options": {
      "A": "油滴瞬间被完全消化吸收形成超高弹性的果冻状固体半透明透明胶块",
      "B": "面糊中温度瞬间下降至零下二十度导致液体发生结冰晶冻结冰硬化现象",
      "C": "油滴无法被蛋黄充分分散包裹，油水界面崩溃出现油水分离破乳出油",
      "D": "液体发生剧烈氧化自燃反应并释放出大量的刺激性二氧化硫黄色气体"
    },
    "answer": "C",
    "explanation": "美乃滋制作初期必须“滴状（Drop by drop）”加入植物油并快速抽打，让蛋黄卵磷脂充分分散油滴。若倒油过快，油滴瞬间超载汇聚成大油滴，造成破乳分离。"
  },
  {
    "id": 24,
    "difficulty": "medium",
    "type": "single",
    "question": "若后厨制作美乃滋发生严重破乳分层，主厨标准抢救方案（Rescue SOP）的操作是：",
    "options": {
      "A": "将破乳液体直接倒进微波炉以最高火持续加热半小时直至完全蒸干水分",
      "B": "加入大量高纯度工业食用酒精剧烈摇晃以强行使未乳化油脂彻底挥发掉",
      "C": "往分离油液中倒入十倍量的干生面粉用打蛋器打成坚硬干燥的面粉团块",
      "D": "另取一干净碗加一茶匙温水或生蛋黄，将分离破乳液以细流缓慢抽打混入"
    },
    "answer": "D",
    "explanation": "破乳急救SOP：在洁净新碗中放一蛋黄或1勺温水搅散建立初始水相界面，然后将油水分离的破乳酱汁如细线般缓慢淋入，高速抽打重新建立乳化网络。"
  },
  {
    "id": 25,
    "difficulty": "medium",
    "type": "single",
    "question": "荷兰酱保温出餐的保质期限在现代西餐食品卫生规范中极其严苛，其核心原因是：",
    "options": {
      "A": "酱汁所散发出的浓郁柠檬酸香气会在常温空气中吸引大量害虫飞蚁叮咬",
      "B": "保温温度（58~62℃）极度接近沙门氏菌等病原微生物滋生的高危险温度区",
      "C": "黄油在微温保温超过两小时后会彻底转化为剧毒的重金属氧化物晶体",
      "D": "酱汁在空气中长期静置会自然吸收大量放射性元素导致物理辐射超标"
    },
    "answer": "B",
    "explanation": "荷兰酱蛋黄未达全熟杀菌温度，保温温度（58~62℃）处于危险温区（Food Danger Zone 5~60℃）临界线，极易滋生沙门氏菌，国际卫生规范要求最多保温2小时必须废弃。"
  },
  {
    "id": 26,
    "difficulty": "medium",
    "type": "single",
    "question": "在制作法式番茄母酱（Sauce Tomate）时，传统法餐通常选用生咸猪肉（Salt pork）与猪油炒香蔬菜底料，其主要工艺目的是：",
    "options": {
      "A": "借助动物脂肪与美拉德产物软化番茄高酸涩味，赋予圆润厚重的复合肉香",
      "B": "使番茄红素在极高饱和脂肪酸作用下瞬间转化为纯白色的半透明果胶质",
      "C": "将番茄酱汁的酸碱度强行中和至极碱性状态以阻断任何天然酶的水解反应",
      "D": "防止番茄表皮在长时间小火慢炖熬煮中发生任何软化瓦解以便捞出弃用"
    },
    "answer": "A",
    "explanation": "传统古典法式番茄母酱以培根或咸五花肉出油起锅，利用动物油脂的丰润脂香包裹平衡番茄天然强烈的果酸味，使酱汁层次丰满圆润。"
  },
  {
    "id": 27,
    "difficulty": "medium",
    "type": "single",
    "question": "在西式沙拉调味中，普通油醋汁（Vinaigrette）属于“暂时性乳化（Temporary Emulsion）”，其物理特征表现为：",
    "options": {
      "A": "静置后油与醋会在几分钟内迅速重新分层，使用前必须再次用力剧烈摇匀",
      "B": "一旦调和混合即可在常温密封条件下保持完全均一稳定状态长达十年以上",
      "C": "混合瞬间油与醋会发生剧烈的放热中和反应并迅速凝结成坚硬琥珀色固体",
      "D": "油分子会彻底包裹水分子使得整体密度变得比水更重并沉降在容器底部"
    },
    "answer": "A",
    "explanation": "油醋汁不含强力永久乳化剂，剧烈摇晃或抽打只是将油微滴机械分散在醋中，静置数分钟后界面张力使油滴聚并重新分层，属于典型的暂时性乳化液。"
  },
  {
    "id": 28,
    "difficulty": "medium",
    "type": "single",
    "question": "主厨在熬制西班牙褐高汤与褐酱时，严禁使用大火长时间剧烈翻滚沸腾，其核心科学机理是：",
    "options": {
      "A": "大火翻滚沸腾会使面粉中的所有淀粉分子发生剧烈核裂变释放放射性核素",
      "B": "剧烈翻滚会将熔化的油脂与蛋白质残渣强制乳化，使原本清澈纯亮酱汁浑浊暗淡发苦",
      "C": "剧烈大火沸腾会导致烤牛骨中的胶原蛋白瞬间转化为不溶于水的粗糙砂石",
      "D": "大火加热会促使高汤内部的液态水分完全消失导致锅体瞬间在灶台上熔融"
    },
    "answer": "B",
    "explanation": "大火剧烈翻滚会将浮游的变性蛋白质凝块和脂肪微滴打碎并强行乳化，导致原本应红亮清澈的汤汁变得浑浊晦暗、发灰发腻，且带有焦苦杂味。"
  },
  {
    "id": 29,
    "difficulty": "medium",
    "type": "single",
    "question": "制作丝绒酱衍生小酱“极品白酱（Sauce Suprême）”时，其标准调配公式为：",
    "options": {
      "A": "鱼丝绒酱加入大量纯黑胡椒碎与老陈醋长时间大火浓缩熬制成的黑酸酱",
      "B": "西班牙褐酱加入浓缩番茄膏与大量煎炸香脆洋葱圈慢炖调和的红褐酱汁",
      "C": "鸡肉丝绒酱（Chicken Velouté）加入厚鲜奶油与少许柠檬汁浓缩而成",
      "D": "白酱加入整块蓝纹奶酪与新鲜薄荷碎叶调配出的高酸咸味浓郁奶酪酱汁"
    },
    "answer": "C",
    "explanation": "Sauce Suprême（至尊白酱）是法餐最经典的丝绒小酱之一，以鸡高汤丝绒酱为底，调入厚鲜奶油（Crème fraîche或Heavy cream）与数滴柠檬汁，丝滑光洁。"
  },
  {
    "id": 30,
    "difficulty": "medium",
    "type": "single",
    "question": "制作经典法式白酱（Sauce Béchamel）时，传统法式大厨在热牛奶中浸泡煮香的特制香料洋葱被称为：",
    "options": {
      "A": "洋葱皮粉末浸泡液（Onion Ash纯天然黑色天然调色剂）",
      "B": "丁香洋葱（Onion Piqué用丁香将月桂叶钉在去皮洋葱上）",
      "C": "焦糖洋葱泥（Caramelized Onion慢炒四十分钟的焦糖酱）",
      "D": "珍珠小洋葱醋渍颗粒（Pickled pearl onions爽口配菜）"
    },
    "answer": "B",
    "explanation": "Onion Piqué（丁香月桂洋葱）：在去皮半个洋葱上用整粒丁香（Cloves）将月桂叶（Bay leaf）钉住，放入牛奶中慢火浸煮，赋予白酱优雅草本丁香风味且捞出方便。"
  },
  {
    "id": 31,
    "difficulty": "medium",
    "type": "single",
    "question": "将热白酱（Béchamel）盛出静置冷却时，为防止其表面因水分蒸发结出一层坚韧硬皮（Skin formation），标准的后厨处理是：",
    "options": {
      "A": "在表面紧贴一层耐热保鲜膜（Cartouche贴面密封）或抹一薄层融化黄油",
      "B": "使用工业大功率鼓风机对准酱汁表面持续高速吹冷风加速表面脱水结壳",
      "C": "往冷却中的白酱表面倒满两厘米厚的干燥生淀粉颗粒吸收空气全部湿气",
      "D": "将白酱放入冷冻库快速深度冷冻至零下三十度彻底冻裂表皮坚硬结晶块"
    },
    "answer": "A",
    "explanation": "含淀粉和乳蛋白的酱汁遇空气冷却极易在表面失水形成硬皮（Skin）。用保鲜膜紧贴酱汁表面（Cartouche）或在表层刷一层薄黄油隔绝空气，是标准防结皮操作。"
  },
  {
    "id": 32,
    "difficulty": "medium",
    "type": "single",
    "question": "制作法式猎人酱（Sauce Chasseur）时，以半釉汁（Demi-glace）为基底，标准搭配的主要辅料原料包括：",
    "options": {
      "A": "鲜草莓果肉、蓝莓果酱搭配浓缩新鲜蜂蜜慢火熬制",
      "B": "嫩豆腐丁、四川青花椒配合香浓水磨麻酱冷拌调和",
      "C": "新鲜口蘑（洋菇片）、红葱头、白葡萄酒与番茄丁及细香葱",
      "D": "生海胆黄、高浓度芥末酱配合新鲜薄荷叶慢炖浸出"
    },
    "answer": "C",
    "explanation": "Sauce Chasseur（猎人酱）是野禽和猎物菜肴经典酱汁，由黄油炒香蘑菇片、红葱头，加白葡萄酒和番茄浓缩，再与半釉汁熬煮并撒欧芹/龙蒿叶制成。"
  },
  {
    "id": 33,
    "difficulty": "medium",
    "type": "single",
    "question": "关于白面糊（Roux blanc）、黄面糊（Roux blond）与褐面糊（Roux brun）的炒制温度与时间控制，下列说法正确的是：",
    "options": {
      "A": "白面糊需大火爆炒半小时，褐面糊只需小火加热十秒钟即可出锅成型",
      "B": "三种面糊在炒制过程中面粉淀粉的增稠能力随时间延长而大幅度剧增",
      "C": "炒制褐面糊时必须加入人工黑巧克力酱调色而绝不能依靠面粉自身热解",
      "D": "白面糊小炒去生味无上色，褐面糊需小火慢炒十五至二十分钟呈深坚果褐色"
    },
    "answer": "D",
    "explanation": "Roux blanc小炒2~3分钟保持白亮无生味；Roux blond炒5~6分钟至浅金黄微带坚果香；Roux brun需全程极小火耐心慢炒15~20分钟，面粉深层焦糖化与糊精化呈深坚果褐色。"
  },
  {
    "id": 34,
    "difficulty": "medium",
    "type": "single",
    "question": "在调制冷酱油醋汁时，常加入少量第戎芥末或少许蛋黄，其在物理化学层面的主要目的是：",
    "options": {
      "A": "降低油醋两相之间的界面张力，减缓分层速度，形成半永久稳定乳化",
      "B": "彻底中和食醋中的所有乙酸分子使其完全丧失所有酸味呈现纯甜口感",
      "C": "促使植物油中的不饱和脂肪酸在低温下迅速结晶析出形成透明白色固体",
      "D": "使油醋汁在与空气接触时释放大量刺激性白色烟雾以增强上菜视觉效果"
    },
    "answer": "A",
    "explanation": "第戎芥末中的多糖黏液和蛋黄中的卵磷脂能充当表面活性剂，包覆油滴降低界面张力，大幅延长油醋汁的乳化悬浮时间，改善挂菜包裹性。"
  },
  {
    "id": 35,
    "difficulty": "medium",
    "type": "single",
    "question": "制作高档法式牛排黑胡椒酱（Sauce au Poivre）时，烹入白兰地（Cognac）或威士忌后进行“灼烧起火（Flambé）”的工艺作用是：",
    "options": {
      "A": "将锅内所有黑胡椒颗粒与牛肉残渣彻底烧成黑色无味木炭沉淀物",
      "B": "完全挥发刺鼻乙醇酒精，留下纯粹酒香与橡木桶陈酿芳香物质",
      "C": "使锅内高汤温度瞬间升高至一千度以彻底熔化锅底的不锈钢金属板",
      "D": "破坏黑胡椒中的胡椒碱使其完全转化为带有强烈甜味的纯果糖分子"
    },
    "answer": "B",
    "explanation": "Flambé（法式焰烧）利用酒精燃烧的高温瞬间带走高浓度刺激性酒精分子，同时触发焦糖化与微量热裂解，将白兰地中浓郁的果香、橡木酯香牢固浓缩锁定在锅底汁液中。"
  },

  # Hard Roman Q36-Q40 (Answer distribution needed: 1A, 1B, 1C, 2D -> Med+Hard = 5A, 5B, 5C, 5D)
  {
    "id": 36,
    "difficulty": "hard",
    "type": "single",
    "question": "关于法式五大古典母酱（Grandes Sauces）与其基础原料的对应，下列组合正确的有：\nⅠ. 白酱（Béchamel）——纯牛奶 + 白油面糊（Roux blanc）\nⅡ. 丝绒酱（Velouté）——白高汤（鸡/小牛/鱼清汤）+ 黄油面糊（Roux blond）\nⅢ. 西班牙褐酱（Espagnole）——烤牛骨高汤 + 烤芳香蔬菜 + 褐油面糊（Roux brun）\nⅣ. 荷兰酱（Hollandaise）——澄清黄油 + 温热蛋黄液 + 柠檬/醋浓缩还原液",
    "options": {
      "A": "Ⅰ、Ⅱ、Ⅲ",
      "B": "Ⅰ、Ⅱ、Ⅳ",
      "C": "Ⅰ、Ⅲ、Ⅳ",
      "D": "Ⅰ、Ⅱ、Ⅲ、Ⅳ"
    },
    "answer": "D",
    "explanation": "Ⅰ、Ⅱ、Ⅲ、Ⅳ四项完全符合现代法式西方烹饪大宗宗师埃斯科菲耶确立的经典五大母酱权威定义。"
  },
  {
    "id": 37,
    "difficulty": "hard",
    "type": "single",
    "question": "关于油面糊（Roux）在热酱汁制作中的热力学与生化机理，下列分析正确的有：\nⅠ. 传统配比为澄清黄油与面粉按1:1质量比调配小火慢炒\nⅡ. 炒制时间越长淀粉糊精化程度越深，褐面糊增稠能力相比白面糊大幅下降\nⅢ. 制作褐酱时因面糊增稠力受损，需按比例增加面糊投放用量\nⅣ. 为防结块，将滚烫沸腾的高温牛奶一口气全倒入极热的生面糊中最为稳妥",
    "options": {
      "A": "Ⅰ、Ⅱ、Ⅲ",
      "B": "Ⅰ、Ⅱ、Ⅳ",
      "C": "Ⅰ、Ⅲ、Ⅳ",
      "D": "Ⅰ、Ⅱ、Ⅲ、Ⅳ"
    },
    "answer": "A",
    "explanation": "Ⅳ错误：热液冲极热面糊会瞬间局部暴聚糊化形成无法化开的面粉结块（Lumps），必须分次冲入并用蛋抽高速打匀。"
  },
  {
    "id": 38,
    "difficulty": "hard",
    "type": "single",
    "question": "关于荷兰酱（Hollandaise）温热乳化操作红线与事故抢救，下列说法正确的有：\nⅠ. 隔水温浴操作温度应严格保持在58℃~62℃的安全温区内\nⅡ. 温度若超过65℃会使蛋黄蛋白质热变性凝结成颗粒导致彻底破乳出油\nⅢ. 温度若低于55℃会导致澄清黄油重新结晶析出凝固引起分层\nⅣ. 发生破乳时可在洁净温碗中加一茶匙温水或生蛋黄，将油水分离液细流打入挽救",
    "options": {
      "A": "Ⅰ、Ⅱ、Ⅲ",
      "B": "Ⅰ、Ⅱ、Ⅳ",
      "C": "Ⅰ、Ⅲ、Ⅳ",
      "D": "Ⅰ、Ⅱ、Ⅲ、Ⅳ"
    },
    "answer": "D",
    "explanation": "Ⅰ、Ⅱ、Ⅲ、Ⅳ均是西餐厨房关于荷兰酱制作温控红线（58~62℃）与破乳救治的最核心SOP规范。"
  },
  {
    "id": 39,
    "difficulty": "hard",
    "type": "single",
    "question": "关于经典法式衍生小酱（Small Sauces）的配方脉络，下列对应关系正确的有：\nⅠ. 莫奈酱（Sauce Mornay）= 白酱 + 磨碎干酪（格吕耶尔/车达）+ 蛋黄\nⅡ. 贝亚恩斯酱（Sauce Béarnaise）= 荷兰酱体系 + 茵陈蒿 + 红葱头白醋浓缩还原液\nⅢ. 至尊白酱（Sauce Suprême）= 鸡肉丝绒酱 + 厚鲜奶油 + 少许柠檬汁\nⅣ. 美乃滋（Mayonnaise）= 番茄母酱加入大量红酒与大蒜粒大火熬煮成的冷酱",
    "options": {
      "A": "Ⅰ、Ⅱ、Ⅳ",
      "B": "Ⅰ、Ⅲ、Ⅳ",
      "C": "Ⅰ、Ⅱ、Ⅲ",
      "D": "Ⅰ、Ⅱ、Ⅲ、Ⅳ"
    },
    "answer": "C",
    "explanation": "Ⅳ错误：美乃滋是纯正的冷乳化酱（蛋黄+植物油+芥末+醋），与番茄母酱毫无渊源关系。"
  },
  {
    "id": 40,
    "difficulty": "hard",
    "type": "single",
    "question": "在现代高级西餐厅厨房中，关于冷热酱汁的保鲜、储运与安全控管，下列规程合理的有：\nⅠ. 自制生蛋黄冷乳化美乃滋必须密闭冷藏于4℃以下并在48~72小时内使用\nⅡ. 荷兰酱必须现做现用，在保温箱中保存严禁超过两小时，超时必须废弃\nⅢ. 含有牛奶与淀粉的白酱出锅后若需储存，应贴面覆盖保鲜膜防起皮并速冷\nⅣ. 为延长高档酱汁保质期，可将已破乳出油变质的荷兰酱室温久置次日复用",
    "options": {
      "A": "Ⅰ、Ⅱ、Ⅳ",
      "B": "Ⅰ、Ⅱ、Ⅲ",
      "C": "Ⅰ、Ⅲ、Ⅳ",
      "D": "Ⅰ、Ⅱ、Ⅲ、Ⅳ"
    },
    "answer": "B",
    "explanation": "Ⅳ错误：变质破乳的荷兰酱含有大量滋生的致病微生物，绝对严禁隔夜复用，必须严格执行两小时废弃红线。"
  }
]

# Validation
print(f"Total questions: {len(questions)}")
assert len(questions) == 40

diff_issues = []
for q in questions:
    lens = {opt: len(text) for opt, text in q['options'].items()}
    max_l = max(lens.values())
    min_l = min(lens.values())
    diff = max_l - min_l
    if diff > 8:
        diff_issues.append((q['id'], diff, lens))

print(f"Diff > 8 count: {len(diff_issues)}")
for item in diff_issues:
    print(f"Q{item[0]:02d} diff={item[1]}: {item[2]}")

easy_answers = [q['answer'] for q in questions[:20]]
med_answers = [q['answer'] for q in questions[20:35]]
hard_answers = [q['answer'] for q in questions[35:40]]
med_hard_answers = med_answers + hard_answers
all_answers = [q['answer'] for q in questions]

print("Easy balance:", Counter(easy_answers))
print("Med balance:", Counter(med_answers))
print("Hard balance:", Counter(hard_answers))
print("Med+Hard balance:", Counter(med_hard_answers))
print("Total balance:", Counter(all_answers))

# Roman checks
for q in questions[35:]:
    opts = list(q['options'].values())
    for opt in opts:
        if not opt.startswith('Ⅰ'):
            print(f"Warning: Q{q['id']} option does not start with Ⅰ: {opt}")

if not diff_issues and Counter(easy_answers) == Counter({'A':5, 'B':5, 'C':5, 'D':5}) and Counter(med_hard_answers) == Counter({'A':5, 'B':5, 'C':5, 'D':5}) and Counter(all_answers) == Counter({'A':10, 'B':10, 'C':10, 'D':10}):
    out_file = r"c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data\senior3\chapter06.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print("SUCCESS: Unit 06 questions generated and saved to", out_file)
else:
    print("FAILED VALIDATION!")
