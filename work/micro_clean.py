import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

micro_fixes = {
    9: {
        28: {
            'options': {
                'A': '饼干无法通过黄油打发充气，缺乏酥松多孔感，口感偏油硬或油腻易碎',
                'B': '饼干在烤箱中膨胀过大炸裂',
                'C': '饼干完全无法烤干成型',
                'D': '表皮呈完全透明状'
            }
        }
    },
    11: {
        1: {
            'options': {
                'A': '大豆植物油',
                'B': '优质新鲜牛奶的天然乳脂（Milk Fat）',
                'C': '深海粗盐提取物',
                'D': '氢化棕榈油'
            }
        },
        9: {
            'options': {
                'A': '纯猪油（Lard）',
                'B': '纯植物大豆油',
                'C': '低度起酥油',
                'D': '变性淀粉糖浆'
            }
        },
        39: {
            'options': {
                'A': '食用维生素E（生育酚 / Tocopherol）',
                'B': '精制细砂糖',
                'C': '纯清水',
                'D': '小麦淀粉'
            }
        }
    },
    12: {
        21: {
            'options': {
                'A': '加入少量柠檬酸（或塔塔粉）促使蔗糖水解，熬煮时避免剧烈搅拌锅壁',
                'B': '在糖浆中倒入大量生冷清水',
                'C': '用铁勺在锅内飞速剧烈画圈搅拌',
                'D': '向糖浆中倒入大量干面粉'
            }
        },
        28: {
            'options': {
                'A': '面包内部质地坚硬紧密',
                'B': '高糖过度软化面筋骨架，出炉冷却后严重缩腰塌陷变软瘫',
                'C': '面包膨胀十倍高',
                'D': '面包完全不上色'
            }
        },
        29: {
            'options': {
                'A': '天然糖枫树树干中流出的汁液经浓缩熬制',
                'B': '人工合成香精加红糖水调配',
                'C': '深海海藻提取液',
                'D': '甜菜根熬汁浓缩'
            }
        },
        33: {
            'options': {
                'A': '耐高温烘烤不轻易融化，保持颗粒完整酥脆咀嚼感',
                'B': '在常温下迅速挥发消失',
                'C': '含有高浓度精制盐',
                'D': '遇热瞬间变成液体油'
            }
        }
    },
    13: {
        22: {
            'options': {
                'A': '烤箱内部产生明火',
                'B': '高温导致蛋奶蛋白质过热剧烈凝固收缩，内部产生蜂窝粗糙孔洞并出水',
                'C': '布丁过度膨胀溢出烤盘',
                'D': '焦糖变甜'
            }
        },
        34: {
            'options': {
                'A': '完全不含一滴蛋黄与任何油脂，全靠大量纯蛋白打发充气与热凝固支撑骨架',
                'B': '加入大量食用白色素',
                'C': '使用特高筋面包粉',
                'D': '使用大量动物猪油'
            }
        }
    }
}

for ch, q_dict in micro_fixes.items():
    fpath = os.path.join(data_dir, f'chapter{ch:02d}.json')
    d = json.load(open(fpath, encoding='utf-8-sig'))
    for q in d['questions']:
        if q['id'] in q_dict:
            entry = q_dict[q['id']]
            if 'options' in entry:
                for k, v in entry['options'].items():
                    q['options'][k] = v
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

print("Micro-clean successfully applied!")
