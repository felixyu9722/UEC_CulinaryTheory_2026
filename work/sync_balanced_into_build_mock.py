# -*- coding: utf-8 -*-
import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'work\paperB_balanced.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

# Build JS array representation of paperB_mcq
lines = ["const paperB_mcq = ["]
lines.append("  // ── BAKERY Q1-40 (均衡版) ──")
for q in qs[:40]:
    q_str = f"  {{id:{q['id']},g:'{q['g']}',src:'{q['src']}',q:'{q['q']}',opts:{{A:'{q['opts']['A']}',B:'{q['opts']['B']}',C:'{q['opts']['C']}',D:'{q['opts']['D']}'}},ans:'{q['ans']}',exp:'{q['exp']}'}},"
    lines.append(q_str)

lines.append("  // ── WESTERN Q41-50 (均衡版) ──")
for q in qs[40:50]:
    q_str = f"  {{id:{q['id']},g:'{q['g']}',src:'{q['src']}',q:'{q['q']}',opts:{{A:'{q['opts']['A']}',B:'{q['opts']['B']}',C:'{q['opts']['C']}',D:'{q['opts']['D']}'}},ans:'{q['ans']}',exp:'{q['exp']}'}},"
    lines.append(q_str)

lines.append("  // ── ASIAN Q51-60 (均衡版) ──")
for q in qs[50:]:
    q_str = f"  {{id:{q['id']},g:'{q['g']}',src:'{q['src']}',q:'{q['q']}',opts:{{A:'{q['opts']['A']}',B:'{q['opts']['B']}',C:'{q['opts']['C']}',D:'{q['opts']['D']}'}},ans:'{q['ans']}',exp:'{q['exp']}'}},"
    lines.append(q_str)

lines.append("];")
new_js = "\n".join(lines)

with open(r'work\build_mock_exam_html.py', 'r', encoding='utf-8') as f:
    orig = f.read()

# Replace const paperB_mcq = [...];
pat = re.compile(r'const\s+paperB_mcq\s*=\s*\[[\s\S]*?\];', re.MULTILINE)
if not pat.search(orig):
    print("Error: Could not match paperB_mcq in build_mock_exam_html.py")
    sys.exit(1)

updated = pat.sub(new_js, orig, count=1)

with open(r'work\build_mock_exam_html.py', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Successfully updated paperB_mcq in work/build_mock_exam_html.py!")
