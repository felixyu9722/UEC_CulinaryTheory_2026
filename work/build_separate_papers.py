# -*- coding: utf-8 -*-
"""
Build standalone Paper A and Paper B HTML files.
Aesthetic strictly aligned with index.html (warm cream #FDFBF7, brown #92400E, amber #D97706, white cards #FFFFFF).
"""
import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')

# Read questions from build_mock_exam_html.py
with open(r'work\build_mock_exam_html.py', 'r', encoding='utf-8') as f:
    mock_src = f.read()

def extract_js_array(varname, text):
    m = re.search(rf'const\s+{varname}\s*=\s*(\[[\s\S]*?\]);', text)
    if not m:
        raise ValueError(f"Could not find {varname}")
    return m.group(1)

paperA_mcq_raw = extract_js_array('paperA_mcq', mock_src)
paperB_mcq_raw = extract_js_array('paperB_mcq', mock_src)
paperA_written_raw = extract_js_array('paperA_written', mock_src)
paperB_written_raw = extract_js_array('paperB_written', mock_src)

print(f"Extracted Paper A MCQ: {len(paperA_mcq_raw)} chars")
print(f"Extracted Paper B MCQ: {len(paperB_mcq_raw)} chars")
print(f"Extracted Paper A Written: {len(paperA_written_raw)} chars")
print(f"Extracted Paper B Written: {len(paperB_written_raw)} chars")
