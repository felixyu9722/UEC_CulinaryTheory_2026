import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'
fpath = os.path.join(data_dir, 'chapter16.json')
d = json.load(open(fpath, encoding='utf-8-sig'))

ch16_clean = {
    31: {
        'question': '碳酸氢铵（臭粉）在烘焙加热中完全分解为氨气、水和二氧化碳，最适宜用于制作：',
        'options': {'A': '高水分大体积戚风蛋糕', 'B': '水分极低、表面干燥易排气的薄脆饼干或核桃酥', 'C': '低温冷藏慕斯蛋糕', 'D': '高含水法式布丁'}
    },
    35: {
        'question': '在烘焙制作中，若单独使用过量小苏打且配方无酸性原料中和，成品最常见的瑕疵是：',
        'options': {'A': '组织苍白且无甜味', 'B': '生成碳酸钠导致成品泛黄、带明显肥皂苦涩碱味', 'C': '质地极其轻盈松软', 'D': '面团融化成透明液体'}
    },
    36: {
        'question': '双效泡打粉（Double-acting Baking Powder）之所以被称为“双效”，是因为其产气分为：',
        'options': {'A': '常温加水时初发产气，入炉受热时第二次爆发释放大量气体', 'B': '能同时产生氧气与氢气', 'C': '能在烤箱内自动降温与升温', 'D': '能完全替代油脂与面粉'}
    },
    38: {
        'question': '商业双效泡打粉配方中，加入约30%干燥玉米淀粉的核心作用是：',
        'options': {'A': '作为填充剂隔离酸碱原料防止吸潮反应失效，并维持标准有效气体用量', 'B': '增加泡打粉甜度', 'C': '使泡打粉在常温下自然发酵', 'D': '彻底杀死面团中的杂菌'}
    },
    39: {
        'question': '碳酸氢铵（臭粉）绝对严禁用于制作大体积高含水蛋糕（如戚风或海绵蛋糕），原因在于：',
        'options': {'A': '分解释放的氨气极易溶于面糊大量水分中无法排出，导致成品残留刺鼻恶臭', 'B': '使烤箱内部瞬间爆炸', 'C': '使蛋糕在出炉后硬如铁石', 'D': '使蛋糕体变成完全透明'}
    },
    40: {
        'question': '在烘焙巧克力蛋糕或曲奇时，配方中加入微量小苏打（弱碱性），除了膨松外还能：',
        'options': {'A': '微碱性促使可可粉中的天然色素颜色加深呈浓郁红褐色，并柔和酸涩感', 'B': '彻底消除巧克力的所有香气', 'C': '让巧克力融点升至100度', 'D': '防止蛋糕受热定型'}
    }
}

applied = 0
for q in d['questions']:
    qid = q['id']
    if qid in ch16_clean:
        u = ch16_clean[qid]
        q['question'] = u['question']
        for k in ['A', 'B', 'C', 'D']:
            q['options'][k] = u['options'][k]
        applied += 1

with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Chapter 16: successfully updated {applied} questions.")
