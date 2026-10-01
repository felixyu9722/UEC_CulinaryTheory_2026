import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

data_dir = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\data'

# Fix Ch02 Q38
f2 = os.path.join(data_dir, 'chapter02.json')
with open(f2, 'r', encoding='utf-8-sig') as f:
    d2 = json.load(f)
for q in d2['questions']:
    if q['id'] == 38:
        q['options'] = {
            "A": "从天然大豆中大规模提取卵磷脂作为高HLB值乳化剂的生产工艺",
            "B": "利用深海海藻提取可替代吉利丁的高强度纯植物性琼脂提取工艺",
            "C": "利用石油化工副产品人工合成高纯度烘焙人造香草精提取技术",
            "D": "从甜菜（Sugar Beet）中大规模提纯高结晶度精制白砂糖工业技术"
        }
        break
with open(f2, 'w', encoding='utf-8') as f:
    json.dump(d2, f, ensure_ascii=False, indent=2)

# Fix Ch09 Q32
f9 = os.path.join(data_dir, 'chapter09.json')
with open(f9, 'r', encoding='utf-8-sig') as f:
    d9 = json.load(f)
for q in d9['questions']:
    if q['id'] == 32:
        q['options'] = {
            "A": "油脂过早乳化会导致酵母细胞吸水膨胀过度引起发酵剧烈失控",
            "B": "过早加入油脂会促使麦谷蛋白过度交联导致面团产生过强韧性",
            "C": "油脂在高速搅拌下会使面粉中的淀粉酶活性异常升高而分解淀粉",
            "D": "油脂形成油膜过早包裹面粉颗粒阻断水分浸润推迟面筋充分扩展"
        }
        break
with open(f9, 'w', encoding='utf-8') as f:
    json.dump(d9, f, ensure_ascii=False, indent=2)

# Fix Ch12 Q19
f12 = os.path.join(data_dir, 'chapter12.json')
with open(f12, 'r', encoding='utf-8-sig') as f:
    d12 = json.load(f)
for q in d12['questions']:
    if q['id'] == 19:
        q['options'] = {
            "A": "初级融化期（Melting Stage），糖颗粒刚开始微弱溶解保持清澈流动态",
            "B": "坚硬焦糖期（Hard Caramel），颜色深黑且散发出浓厚刺鼻焦苦烧焦气味",
            "C": "大裂期（Hard Crack Stage），糖滴入冷水形成脆硬易碎玻璃状硬糖丝",
            "D": "软球期（Soft Ball Stage），滴入冷水能用手指捏成柔软有弹性的小糖球"
        }
        break
with open(f12, 'w', encoding='utf-8') as f:
    json.dump(d12, f, ensure_ascii=False, indent=2)

# Fix Ch15 Q19
f15 = os.path.join(data_dir, 'chapter15.json')
with open(f15, 'r', encoding='utf-8-sig') as f:
    d15 = json.load(f)
for q in d15['questions']:
    if q['id'] == 19:
        q['options'] = {
            "A": "通过充气气泡膨胀测定面团内部双向拉伸阻力、弹性与三维延伸破裂形变量的吹泡仪（Alveograph）",
            "B": "高精度动态测定面粉淀粉在加热降温过程中糊化峰值黏度与老化衰退值的快速黏度分析仪（RVA）",
            "C": "模拟工业揉面测定生面团抗机械剪切搅拌吸水率与面团稳定时间的标准物理面团粉质仪（Farinograph）",
            "D": "连续测定面团发酵全周期产气动力学与面筋持气能力的流变发酵仪（Rheofermentometer）"
        }
        break
with open(f15, 'w', encoding='utf-8') as f:
    json.dump(d15, f, ensure_ascii=False, indent=2)

# Fix Ch18 Q36
f18 = os.path.join(data_dir, 'chapter18.json')
with open(f18, 'r', encoding='utf-8-sig') as f:
    d18 = json.load(f)
for q in d18['questions']:
    if q['id'] == 36:
        q['options'] = {
            "A": "将明胶与改性多糖胶体复配，抑制大冰晶生长并阻断交联结节脱水收缩",
            "B": "大幅提高冷冻慕斯配方中游离水分添加比例并延长零下三十度冷冻时间",
            "C": "在慕斯面糊中额外加入大剂量强酸性果汁以促使明胶分子彻底水解为氨基酸",
            "D": "取消配方中所有的天然蛋黄与乳脂肪以降低慕斯内部脂肪球的乳化稳定度"
        }
        break
with open(f18, 'w', encoding='utf-8') as f:
    json.dump(d18, f, ensure_ascii=False, indent=2)

print("Fixed the 5 outlier questions with professional bilingual options and balanced lengths!")
