import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Paper A
with open('work/build_mock_exam_html.py', 'r', encoding='utf-8') as f:
    src = f.read()

m_a = re.search(r'const\s+paperA_mcq\s*=\s*(\[[\s\S]*?\]);', src)
js_text = m_a.group(1)
q_matches = re.findall(r'opts:\s*\{([^}]+)\}', js_text)
paperA_data = []
for qm in q_matches:
    opts = {}
    for opt_m in re.finditer(r'([ABCD]):\s*[\'"]([^\'"]+)[\'"]', qm):
        opts[opt_m.group(1)] = opt_m.group(2)
    paperA_data.append({'options': opts})

lens_a = [len(v) for q in paperA_data for v in q['options'].values() if v]
print(f"=== 模拟卷 A · 历届高频真题精选卷 (60题) ===")
print(f"  选项总数: {len(lens_a)}")
print(f"  选项平均字数: {sum(lens_a)/len(lens_a):.1f} 字符")
print(f"  极短选项（<=8字）占比: {len([x for x in lens_a if x <= 8])/len(lens_a)*100:.1f}%")
print(f"  长选项（>=20字）数量: {len([x for x in lens_a if x >= 20])} 个")

# 2. Paper B
paperB_data = json.load(open('work/paperB_balanced.json', encoding='utf-8'))
lens_b = [len(v) for q in paperB_data for v in (q.get('options') or q.get('opts')).values() if v]
print(f"\n=== 模拟卷 B · 2026前瞻预测试题卷 (60题) ===")
print(f"  选项总数: {len(lens_b)}")
print(f"  选项平均字数: {sum(lens_b)/len(lens_b):.1f} 字符")
print(f"  极短选项（<=8字）占比: {len([x for x in lens_b if x <= 8])/len(lens_b)*100:.1f}%")
print(f"  长选项（>=20字）数量: {len([x for x in lens_b if x >= 20])} 个")

# 3. Paper C
paperC_data = json.load(open('work/paperC_data.json', encoding='utf-8'))['mcq']
lens_c = [len(v) for q in paperC_data for v in (q.get('options') or q.get('opts')).values() if v]
print(f"\n=== 模拟卷 C · 2026短选项实战冲刺卷 (60题) ===")
print(f"  选项总数: {len(lens_c)}")
print(f"  选项平均字数: {sum(lens_c)/len(lens_c):.1f} 字符")
print(f"  极短选项（<=8字）占比: {len([x for x in lens_c if x <= 8])/len(lens_c)*100:.1f}%")
print(f"  长选项（>=20字）数量: {len([x for x in lens_c if x >= 20])} 个")
