# -*- coding: utf-8 -*-
"""
Compile and unify all 3 Mock Exam Papers:
- 模拟卷A_历届高频真题精选卷.html
- 模拟卷B_2026前瞻预测试题卷.html
- 模拟卷C_2026统考短选项实战冲刺卷.html
- 模拟考场主页.html (3 cards matrix)
- index.html (entrance banner mentions A/B/C)
"""

import sys, os, json, re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r'c:\Users\GOH\Desktop\2026年统考厨艺理论'

# 1. Load questions for Paper A and Paper B
with open(r'work\build_mock_exam_html.py', 'r', encoding='utf-8') as f:
    mock_src = f.read()

def extract_js_array(varname, text):
    m = re.search(rf'const\s+{varname}\s*=\s*(\[[\s\S]*?\]);', text)
    if not m:
        raise ValueError(f"Could not find {varname}")
    return m.group(1)

paperA_mcq_code = extract_js_array('paperA_mcq', mock_src)
paperB_mcq_code = extract_js_array('paperB_mcq', mock_src)
paperA_written_code = extract_js_array('paperA_written', mock_src)
paperB_written_code = extract_js_array('paperB_written', mock_src)

# Load Paper C data from paperC_data.json
with open(r'work\paperC_data.json', 'r', encoding='utf-8') as f:
    dC = json.load(f)

paperC_mcq_code = json.dumps(dC['mcq'], ensure_ascii=False)
paperC_written_code = json.dumps(dC['written'], ensure_ascii=False)

def get_paper_template(config):
    """
    config:
      paper_id: 'A', 'B', or 'C'
      paper_title: str
      paper_subtitle: str
      paper_desc: str
      badge_text: str
      mcq_code: str
      written_code: str
      out_filename: str
      nav_links_html: str
    """
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2026统考厨艺理论 · {config['paper_title']}</title>
<meta name="description" content="2026马来西亚华文独中统考厨艺理论历届全真模拟考场 - {config['paper_title']}。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;800&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --primary: #92400E;
  --primary-light: #FDE68A;
  --primary-dark: #78350F;
  --accent: #D97706;
  --bg: #FDFBF7;
  --card-bg: #FFFFFF;
  --text: #1E293B;
  --text-muted: #64748B;
  --border: #E2E8F0;
  --correct: #10B981;
  --correct-bg: #ECFDF5;
  --correct-border: #A7F3D0;
  --wrong: #EF4444;
  --wrong-bg: #FEF2F2;
  --wrong-border: #FECACA;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 14px rgba(0,0,0,0.08);
  --shadow-lg: 0 10px 25px rgba(0,0,0,0.12);
  --radius: 14px;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: 'Noto Sans SC', system-ui, -apple-system, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.65;
  padding-bottom: 100px;
}}

/* ── HEADER ── */
header {{
  background: linear-gradient(135deg, #78350F 0%, #92400E 100%);
  color: #fff;
  padding: 12px 20px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 10px rgba(0,0,0,0.12);
}}

.hdr-wrap {{
  max-width: 1120px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}}

.hdr-left {{
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}}

.hdr-back {{
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: #FDE68A;
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 8px;
  background: rgba(255,255,255,0.12);
  transition: all 0.2s;
}}
.hdr-back:hover {{
  background: rgba(255,255,255,0.22);
  color: #fff;
}}

.hdr-title-box {{
  display: flex;
  flex-direction: column;
}}

.hdr-brand {{
  font-size: 1.05rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
}}

.hdr-paper-badge {{
  background: #FDE68A;
  color: #78350F;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 9999px;
  letter-spacing: 0.3px;
}}

.hdr-sub {{
  font-size: 0.74rem;
  color: rgba(255,255,255,0.85);
}}

/* HUD stats bar */
.hdr-hud {{
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}}

.hud-pill {{
  background: rgba(0,0,0,0.22);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 9999px;
  padding: 4px 12px;
  font-size: 0.8rem;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.hud-val {{
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  color: #FDE68A;
}}

/* Mode Switcher Buttons */
.mode-switch {{
  display: flex;
  background: rgba(0,0,0,0.25);
  border-radius: 9999px;
  padding: 2px;
  border: 1px solid rgba(255,255,255,0.15);
}}
.mode-btn {{
  background: transparent;
  border: none;
  color: rgba(255,255,255,0.8);
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 0.76rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}}
.mode-btn.active {{
  background: #fff;
  color: #78350F;
  box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}}

/* ── MAIN LAYOUT ── */
.main-wrap {{
  max-width: 1040px;
  margin: 24px auto;
  padding: 0 16px;
}}

/* Paper Banner Card */
.paper-banner {{
  background: #FFFFFF;
  border: 1.5px solid var(--border);
  border-left: 6px solid var(--accent);
  border-radius: 16px;
  padding: 24px 28px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}}
.pb-top {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  flex-wrap: wrap;
}}
.pb-title {{
  font-size: 1.45rem;
  font-weight: 800;
  color: #1E293B;
  margin-bottom: 6px;
}}
.pb-desc {{
  font-size: 0.92rem;
  color: var(--text-muted);
  line-height: 1.6;
}}
.pb-meta {{
  display: flex;
  gap: 12px;
  margin-top: 14px;
  flex-wrap: wrap;
}}
.pb-meta-item {{
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.82rem;
  color: #475569;
  background: #F8FAFC;
  padding: 4px 10px;
  border-radius: 8px;
  border: 1px solid var(--border);
}}

/* ── SECTION SWITCH TABS (试卷一 vs 试卷二) ── */
.section-nav {{
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  border-bottom: 2px solid #E2E8F0;
  padding-bottom: 2px;
}}
.sec-tab-btn {{
  background: transparent;
  border: none;
  font-size: 1.05rem;
  font-weight: 700;
  color: #64748B;
  padding: 10px 18px;
  cursor: pointer;
  position: relative;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.sec-tab-btn:hover {{
  color: #1E293B;
}}
.sec-tab-btn.active {{
  color: #92400E;
}}
.sec-tab-btn.active::after {{
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  right: 0;
  height: 4px;
  background: #92400E;
  border-radius: 4px;
}}

/* ── TOOLBAR (FILTER & ACTIONS) ── */
.control-bar {{
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px 18px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  box-shadow: var(--shadow-sm);
}}
.filter-group {{
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}}
.filter-btn {{
  background: #F1F5F9;
  border: 1px solid #CBD5E1;
  color: #475569;
  padding: 5px 12px;
  border-radius: 8px;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
}}
.filter-btn:hover {{
  background: #E2E8F0;
}}
.filter-btn.active {{
  background: #92400E;
  color: #fff;
  border-color: #92400E;
}}

.palette-toggle-btn {{
  background: #FEF3C7;
  border: 1px solid #FDE68A;
  color: #92400E;
  padding: 6px 14px;
  border-radius: 8px;
  font-size: 0.84rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
}}
.palette-toggle-btn:hover {{
  background: #FDE68A;
}}

/* ── QUESTION PALETTE ── */
.palette-card {{
  background: #FFFFFF;
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 16px 20px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}}
.palette-card.hidden {{
  display: none;
}}
.palette-header {{
  font-size: 0.9rem;
  font-weight: 700;
  color: #475569;
  margin-bottom: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.palette-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(38px, 1fr));
  gap: 8px;
}}
.pal-btn {{
  width: 38px;
  height: 38px;
  border-radius: 8px;
  border: 1.5px solid #CBD5E1;
  background: #F8FAFC;
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  font-size: 0.85rem;
  color: #475569;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
}}
.pal-btn:hover {{
  border-color: var(--accent);
  background: #FEF3C7;
  color: var(--primary);
}}
.pal-btn.answered {{
  background: #FEF3C7;
  border-color: #F59E0B;
  color: #B45309;
}}
.pal-btn.correct {{
  background: #ECFDF5;
  border-color: #10B981;
  color: #047857;
}}
.pal-btn.wrong {{
  background: #FEF2F2;
  border-color: #EF4444;
  color: #B91C1C;
}}

/* Group Divider */
.group-divider {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 32px 0 18px 0;
}}
.gd-line {{
  flex: 1;
  height: 1.5px;
  background: #E2E8F0;
}}
.gd-badge {{
  background: #FEF3C7;
  color: #78350F;
  border: 1px solid #FDE68A;
  padding: 4px 14px;
  border-radius: 9999px;
  font-size: 0.84rem;
  font-weight: 800;
}}

/* ── QUESTION CARD ── */
.question-card {{
  background: var(--card-bg);
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 24px 28px;
  margin-bottom: 22px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.03);
  transition: all 0.2s ease;
}}
.question-card:hover {{
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}}

.q-top {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
  gap: 10px;
  flex-wrap: wrap;
}}
.q-top-left {{
  display: flex;
  align-items: center;
  gap: 8px;
}}
.q-num-pill {{
  background: #78350F;
  color: #fff;
  font-family: 'Outfit', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 6px;
}}
.q-grp-pill {{
  font-size: 0.78rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 6px;
  background: #F1F5F9;
  color: #475569;
}}
.q-source-tag {{
  font-size: 0.78rem;
  font-weight: 600;
  color: #92400E;
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  padding: 2px 10px;
  border-radius: 9999px;
}}

.q-stem {{
  font-size: 1.12rem;
  font-weight: 700;
  color: #0F172A;
  margin-bottom: 18px;
  line-height: 1.65;
  white-space: pre-line;
}}

/* Options */
.options-col {{
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.opt-btn {{
  display: flex;
  align-items: center;
  min-height: 52px;
  padding: 12px 18px;
  border: 2px solid #E2E8F0;
  border-radius: 12px;
  background: #FFFFFF;
  cursor: pointer;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  user-select: none;
}}
.opt-btn:hover:not(.locked) {{
  border-color: #D97706;
  background: #FFFDF7;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(217,119,6,0.12);
}}
.opt-badge {{
  width: 34px;
  height: 34px;
  border-radius: 8px;
  background: #F1F5F9;
  font-family: 'Outfit', sans-serif;
  font-weight: 800;
  font-size: 1rem;
  color: #475569;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 14px;
  flex-shrink: 0;
  transition: all 0.15s ease;
}}
.opt-txt {{
  font-size: 1.02rem;
  font-weight: 500;
  color: #1E293B;
  flex: 1;
}}

/* Option states */
.opt-btn.selected-exam {{
  border-color: #D97706;
  background: #FEF3C7;
}}
.opt-btn.selected-exam .opt-badge {{
  background: #D97706;
  color: #fff;
}}

.opt-btn.correct {{
  border-color: #10B981;
  background: #ECFDF5;
}}
.opt-btn.correct .opt-badge {{
  background: #10B981;
  color: #fff;
}}

.opt-btn.wrong {{
  border-color: #EF4444;
  background: #FEF2F2;
}}
.opt-btn.wrong .opt-badge {{
  background: #EF4444;
  color: #fff;
}}

/* Explanation Box */
.exp-box {{
  margin-top: 16px;
  padding: 16px 20px;
  border-radius: 12px;
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-left: 4px solid var(--correct);
  display: none;
  animation: fadeIn 0.25s ease-out;
}}
.exp-box.visible {{
  display: block;
}}
.exp-top {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}}
.exp-ans-badge {{
  background: #10B981;
  color: #fff;
  font-weight: 800;
  font-size: 0.8rem;
  padding: 2px 10px;
  border-radius: 6px;
}}
.exp-title {{
  font-size: 0.88rem;
  font-weight: 700;
  color: #0F172A;
}}
.exp-body {{
  font-size: 0.92rem;
  color: #334155;
  line-height: 1.65;
}}

/* ── SECTION 2: WRITTEN QUESTIONS ── */
.written-section {{
  display: none;
}}
.written-section.active {{
  display: block;
}}

.written-tip {{
  background: #FFFBEB;
  border: 1.5px solid #FDE68A;
  border-radius: 14px;
  padding: 18px 22px;
  margin-bottom: 24px;
  color: #78350F;
  font-size: 0.92rem;
  line-height: 1.6;
}}

.written-card {{
  background: #FFFFFF;
  border: 1.5px solid var(--border);
  border-radius: 16px;
  padding: 26px 30px;
  margin-bottom: 24px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.03);
}}
.wc-head {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  gap: 12px;
  flex-wrap: wrap;
}}
.wc-label {{
  font-size: 1rem;
  font-weight: 800;
  color: #78350F;
  background: #FEF3C7;
  padding: 4px 12px;
  border-radius: 8px;
}}
.wc-pts {{
  font-size: 0.85rem;
  font-weight: 700;
  color: #475569;
  background: #F1F5F9;
  padding: 4px 12px;
  border-radius: 8px;
}}
.wc-stem {{
  font-size: 1.1rem;
  font-weight: 700;
  color: #0F172A;
  line-height: 1.65;
  margin-bottom: 16px;
  white-space: pre-line;
}}

/* Table in written question */
.w-table {{
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0 20px 0;
  font-size: 0.92rem;
}}
.w-table th, .w-table td {{
  border: 1px solid #CBD5E1;
  padding: 8px 14px;
  text-align: center;
}}
.w-table th {{
  background: #F1F5F9;
  font-weight: 700;
  color: #1E293B;
}}
.w-table tr:nth-child(even) td {{
  background: #F8FAFC;
}}

/* Draft Box */
.draft-box {{
  margin: 16px 0;
}}
.draft-label {{
  font-size: 0.82rem;
  font-weight: 700;
  color: #64748B;
  margin-bottom: 6px;
  display: flex;
  justify-content: space-between;
}}
.draft-area {{
  width: 100%;
  height: 90px;
  border: 1.5px solid #CBD5E1;
  border-radius: 10px;
  padding: 10px 14px;
  font-family: inherit;
  font-size: 0.92rem;
  line-height: 1.5;
  resize: vertical;
  background: #FFFDF9;
}}
.draft-area:focus {{
  outline: none;
  border-color: #D97706;
  box-shadow: 0 0 0 3px rgba(217,119,6,0.15);
}}

/* Answer Accordion Button */
.wc-ans-btn {{
  width: 100%;
  padding: 12px 18px;
  background: #FFFBEB;
  border: 1.5px solid #FDE68A;
  border-radius: 10px;
  color: #92400E;
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s;
  margin-top: 14px;
}}
.wc-ans-btn:hover {{
  background: #FDE68A;
}}
.wc-ans-panel {{
  margin-top: 12px;
  padding: 20px 24px;
  border-radius: 12px;
  background: #F0FDF4;
  border: 1.5px solid #A7F3D0;
  display: none;
}}
.wc-ans-panel.visible {{
  display: block;
}}
.wc-ans-text {{
  font-size: 0.95rem;
  color: #064E3B;
  line-height: 1.7;
  white-space: pre-line;
}}

/* ── EXAM MODE SUBMISSION MODAL ── */
.modal-overlay {{
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(4px);
  z-index: 1000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}}
.modal-overlay.visible {{
  display: flex;
}}
.modal-card {{
  background: #FFFFFF;
  border-radius: 20px;
  max-width: 520px;
  width: 100%;
  padding: 32px 30px;
  box-shadow: var(--shadow-lg);
  text-align: center;
  animation: scaleIn 0.2s ease-out;
}}
.modal-emoji {{
  font-size: 3rem;
  margin-bottom: 12px;
}}
.modal-title {{
  font-size: 1.5rem;
  font-weight: 800;
  color: #1E293B;
  margin-bottom: 8px;
}}
.modal-score-box {{
  margin: 18px 0;
  padding: 16px;
  background: #FFFBEB;
  border-radius: 14px;
  border: 1.5px solid #FDE68A;
}}
.modal-score-num {{
  font-family: 'Outfit', sans-serif;
  font-size: 2.8rem;
  font-weight: 800;
  color: #92400E;
  line-height: 1;
}}
.modal-score-sub {{
  font-size: 0.9rem;
  color: #78350F;
  margin-top: 6px;
  font-weight: 600;
}}
.modal-btn-row {{
  display: flex;
  gap: 12px;
  justify-content: center;
  margin-top: 24px;
}}
.modal-btn {{
  padding: 12px 22px;
  border-radius: 12px;
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
}}
.modal-btn-primary {{
  background: #92400E;
  color: #fff;
}}
.modal-btn-primary:hover {{
  background: #78350F;
}}
.modal-btn-sec {{
  background: #F1F5F9;
  color: #475569;
}}
.modal-btn-sec:hover {{
  background: #E2E8F0;
}}

/* Floating Submit Button for Exam Mode */
.floating-submit-bar {{
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: #FFFFFF;
  border: 1.5px solid var(--border);
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  border-radius: 9999px;
  padding: 8px 18px;
  display: flex;
  align-items: center;
  gap: 14px;
  z-index: 90;
}}
.floating-submit-bar.hidden {{
  display: none;
}}
.fs-btn {{
  background: linear-gradient(135deg, #059669, #10B981);
  color: #fff;
  border: none;
  font-size: 0.92rem;
  font-weight: 700;
  padding: 8px 18px;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 3px 8px rgba(16,185,129,0.3);
}}
.fs-btn:hover {{
  filter: brightness(1.08);
  transform: translateY(-1px);
}}

/* Footer */
footer {{
  margin-top: 60px;
  text-align: center;
  color: var(--text-muted);
  font-size: 0.85rem;
  padding: 24px 16px;
  border-top: 1px solid var(--border);
}}
footer a {{
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}}
footer a:hover {{
  text-decoration: underline;
}}

@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes scaleIn {{
  from {{ opacity: 0; transform: scale(0.95); }}
  to {{ opacity: 1; transform: scale(1); }}
}}

.hide-mobile {{ display: inline; }}
.show-mobile-only {{ display: none; }}

@media (max-width: 640px) {{
  .hide-mobile {{ display: none !important; }}
  .show-mobile-only {{ display: inline !important; }}

  header {{
    padding: 6px 10px;
  }}
  .hdr-wrap {{
    gap: 4px;
  }}
  .hdr-left {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 4px;
    width: 100%;
  }}
  .hdr-back {{
    padding: 2px 6px;
    font-size: 0.70rem;
    border-radius: 6px;
    gap: 2px;
  }}
  .hdr-title-box {{
    width: 100%;
    margin-top: 2px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }}
  .hdr-brand {{
    font-size: 0.86rem;
    font-weight: 800;
    gap: 6px;
  }}
  .hdr-paper-badge {{
    font-size: 0.62rem;
    padding: 1px 6px;
  }}
  .hdr-sub {{
    display: none !important;
  }}

  .hdr-hud {{
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 3px;
    margin-top: 2px;
  }}
  .mode-switch {{
    padding: 1px;
  }}
  .mode-btn {{
    padding: 2px 6px;
    font-size: 0.68rem;
  }}
  .hud-pill {{
    padding: 2px 6px;
    font-size: 0.70rem;
    gap: 3px;
  }}
  .hud-val {{
    font-size: 0.80rem;
  }}

  /* Main & Paper Banner */
  .main-wrap {{
    margin: 10px auto;
    padding: 0 10px;
  }}
  .paper-banner {{
    padding: 12px 14px;
    margin-bottom: 12px;
    border-radius: 12px;
  }}
  .pb-title {{
    font-size: 1.08rem;
    margin-bottom: 4px;
  }}
  .pb-desc {{
    font-size: 0.80rem;
    line-height: 1.45;
  }}
  .pb-meta {{
    margin-top: 8px;
    gap: 4px;
  }}
  .pb-meta-item {{
    font-size: 0.70rem;
    padding: 2px 6px;
  }}

  /* Section Nav */
  .section-nav {{
    margin-bottom: 14px;
    gap: 6px;
  }}
  .sec-tab-btn {{
    font-size: 0.90rem;
    padding: 6px 12px;
  }}

  /* Question Palette */
  .palette-card {{
    padding: 12px 10px;
    margin-bottom: 12px;
    border-radius: 12px;
  }}
  .palette-grid {{
    grid-template-columns: repeat(auto-fill, minmax(32px, 1fr));
    gap: 4px;
  }}
  .pal-btn {{
    width: 32px;
    height: 32px;
    font-size: 0.75rem;
    border-radius: 6px;
  }}

  /* Question Card */
  .question-card {{
    padding: 14px 12px;
    margin-bottom: 12px;
    border-radius: 12px;
  }}
  .q-top {{
    margin-bottom: 8px;
    gap: 4px;
  }}
  .q-num-pill {{
    font-size: 0.72rem;
    padding: 2px 7px;
  }}
  .q-group-tag {{
    font-size: 0.68rem;
    padding: 2px 6px;
  }}
  .q-title {{
    font-size: 1.02rem;
    line-height: 1.45;
    margin-bottom: 12px;
  }}
  .opt-btn {{
    min-height: 42px;
    padding: 8px 10px;
    margin-bottom: 7px;
    border-radius: 10px;
    gap: 8px;
  }}
  .opt-badge {{
    width: 26px;
    height: 26px;
    font-size: 0.82rem;
    margin-right: 6px;
  }}
  .opt-txt {{
    font-size: 0.92rem;
    line-height: 1.38;
  }}
  .exp-box {{
    margin-top: 10px;
    padding: 12px 14px;
  }}
  .exp-title {{
    font-size: 0.85rem;
  }}
  .exp-body {{
    font-size: 0.86rem;
    line-height: 1.55;
  }}
}}
</style>
</head>
<body>

<header>
  <div class="hdr-wrap">
    <div class="hdr-left">
      <a class="hdr-back" href="模拟考场主页.html">← <span class="hide-mobile">模拟考场</span>总览</a>
      {config['nav_links_html']}
      <a class="hdr-back" href="index.html">🏠 <span class="hide-mobile">练习系统</span>主页</a>
      <div class="hdr-title-box">
        <div class="hdr-brand">
          <span>{config['paper_title']}</span>
          <span class="hdr-paper-badge hide-mobile">{config['badge_text']}</span>
        </div>
        <div class="hdr-sub hide-mobile">{config['paper_subtitle']}</div>
      </div>
    </div>

    <div class="hdr-hud">
      <!-- Mode Switch -->
      <div class="mode-switch">
        <button class="mode-btn active" id="btnModeInstant" onclick="setMode('instant')">⚡ <span class="hide-mobile">随刷</span>即查</button>
        <button class="mode-btn" id="btnModeExam" onclick="setMode('exam')">⏱️ 模考<span class="hide-mobile">计时</span></button>
      </div>

      <div class="hud-pill" id="hudTimerBox" style="display:none;">
        <span>⏳</span><span class="hud-val" id="hudTimer">80:00</span>
      </div>

      <div class="hud-pill">
        <span>已答</span><span class="hud-val" id="hudAnswered">0 / 60</span>
      </div>

      <div class="hud-pill">
        <span>正确率</span><span class="hud-val" id="hudAccuracy">0%</span>
      </div>

      <button class="hdr-back" onclick="resetAll()" title="重置本卷答题记录" style="cursor:pointer;border:none;">🔄 <span class="hide-mobile">重置</span></button>
    </div>
  </div>
</header>

<main class="main-wrap">

  <!-- Banner Card -->
  <div class="paper-banner">
    <div class="pb-top">
      <div>
        <h1 class="pb-title">{config['paper_title']}</h1>
        <p class="pb-desc">{config['paper_desc']}</p>
      </div>
    </div>
    <div class="pb-meta">
      <div class="pb-meta-item"><span>⏱️</span> 建议作答时间：80 分钟</div>
      <div class="pb-meta-item"><span>📝</span> 试卷一：60 题单选题（全答 · 60分）</div>
      <div class="pb-meta-item"><span>✍️</span> 试卷二：作答题（甲组必答 + 乙组选答 · 40分）</div>
      <div class="pb-meta-item"><span>📊</span> 历届真题短选项对标 · 董总命题标准</div>
    </div>
  </div>

  <!-- Section Nav Tabs -->
  <div class="section-nav">
    <button class="sec-tab-btn active" id="tabBtn1" onclick="switchSection(1)">
      📝 试卷一：选择题 (60题 · 60分)
    </button>
    <button class="sec-tab-btn" id="tabBtn2" onclick="switchSection(2)">
      ✍️ 试卷二：作答题 (综合题 · 40分)
    </button>
  </div>

  <!-- ── SECTION 1: MCQ ── -->
  <div id="sectionMcq">

    <!-- Control Bar -->
    <div class="control-bar">
      <div class="filter-group">
        <button class="filter-btn active" id="fAll" onclick="setFilter('all')">全部 (60)</button>
        <button class="filter-btn" id="fUnans" onclick="setFilter('unans')">未作答</button>
        <button class="filter-btn" id="fAns" onclick="setFilter('ans')">已作答</button>
        <button class="filter-btn" id="fWrong" onclick="setFilter('wrong')">错题本</button>
      </div>

      <button class="palette-toggle-btn" onclick="togglePalette()">
        <span>🔢</span> 展开 / 收起答题卡题号
      </button>
    </div>

    <!-- Question Palette -->
    <div class="palette-card hidden" id="paletteBox">
      <div class="palette-header">
        <span>快速定位题号</span>
        <span style="font-size:0.75rem;color:#64748B;">点击题号直接平滑跳转至对应题目</span>
      </div>
      <div class="palette-grid" id="paletteGrid"></div>
    </div>

    <!-- Questions Container -->
    <div id="questionsContainer"></div>

  </div>

  <!-- ── SECTION 2: WRITTEN ── -->
  <div class="written-section" id="sectionWritten">
    <div class="written-tip">
      <strong>📌 统考作答须知：</strong><br>
      试卷二（作答题）满分为 40 分。<br>
      • <strong>甲组（必答题，10分）</strong>：必须全答，重点考查烘焙计算与基础操作原理。<br>
      • <strong>乙组（选答题，30分）</strong>：共 7 题选答 3 题，每题 10 分。建议先在草稿区整理要点，再点击展开核对参考答案与评分要点。
    </div>

    <div id="writtenContainer"></div>
  </div>

</main>

<!-- Floating Bar for Exam Mode -->
<div class="floating-submit-bar hidden" id="floatingBar">
  <span style="font-size:0.86rem;font-weight:700;color:#1E293B;">模考进行中</span>
  <span style="font-size:0.82rem;color:#64748B;" id="fsAnsweredInfo">已答 0/60</span>
  <button class="fs-btn" onclick="submitExam()">📋 交卷评测</button>
</div>

<!-- Modal Dialog for Exam Submission Results -->
<div class="modal-overlay" id="examModal">
  <div class="modal-card">
    <div class="modal-emoji" id="modalEmoji">🎉</div>
    <div class="modal-title">模考评测报告</div>
    <div class="modal-score-box">
      <div class="modal-score-num" id="modalScore">0 / 60</div>
      <div class="modal-score-sub" id="modalGrade">等级：评测中</div>
    </div>
    <div id="modalBreakdown" style="font-size:0.88rem;color:#475569;margin-bottom:18px;line-height:1.6;"></div>
    <div class="modal-btn-row">
      <button class="modal-btn modal-btn-primary" onclick="closeModalAndReview()">🔍 查看全卷解析</button>
      <button class="modal-btn modal-btn-sec" onclick="resetAll()">🔄 重新模考</button>
    </div>
  </div>
</div>

<footer>
  <p style="margin-bottom:6px;">
    <a href="模拟考场主页.html">← 返回模拟考场总览</a> &nbsp;|&nbsp; 
    <a href="index.html">返回高中厨艺理论互动答题总系统</a>
  </p>
  <p>2026年马来西亚华文独中统一考试厨艺理论 · 历届全真模拟考场 &nbsp;|&nbsp; <em style="color:var(--accent)">v2026.10-Build.04</em></p>
</footer>

<script>
// 1. Data Injection
const mcqData = {config['mcq_code']};
const writtenData = {config['written_code']};

// 2. Application State
let currentMode = 'instant'; // 'instant' or 'exam'
let currentFilter = 'all';   // 'all', 'unans', 'ans', 'wrong'
let userAnswers = {{}};        // qId: selectedOption ('A','B','C','D')
let examSubmitted = false;
let timerSeconds = 80 * 60;  // 80 minutes
let timerInterval = null;

// Group definitions
const groupNames = {{
  'A': '甲组 · 烘焙理论与实务 (Q01~Q40)',
  'B': '乙组 · 西餐烹调艺术 (Q41~Q50)',
  'C': '丙组 · 亚洲烹调艺术 (Q51~Q60)'
}};

// 3. Render Functions
function renderMCQ() {{
  const container = document.getElementById('questionsContainer');
  container.innerHTML = '';

  let lastGroup = null;

  mcqData.forEach(q => {{
    // Group divider
    if (q.g !== lastGroup) {{
      lastGroup = q.g;
      const div = document.createElement('div');
      div.className = 'group-divider';
      div.innerHTML = `<div class="gd-line"></div>
        <div class="gd-badge">${{groupNames[q.g] || '组别'}}</div>
        <div class="gd-line"></div>`;
      container.appendChild(div);
    }}

    const card = document.createElement('div');
    card.className = 'question-card';
    card.id = `qCard_${{q.id}}`;
    card.dataset.qid = q.id;
    card.dataset.group = q.g;

    const answered = userAnswers[q.id] !== undefined;
    const isCorrect = answered && userAnswers[q.id] === q.ans;
    const isWrong = answered && !isCorrect;

    // Filter visibility
    if (currentFilter === 'unans' && answered) card.style.display = 'none';
    else if (currentFilter === 'ans' && !answered) card.style.display = 'none';
    else if (currentFilter === 'wrong' && (!answered || isCorrect)) card.style.display = 'none';
    else card.style.display = 'block';

    const numStr = q.id < 10 ? '0' + q.id : q.id;
    const groupLabel = q.g === 'A' ? '甲组·烘焙' : (q.g === 'B' ? '乙组·西餐' : '丙组·亚洲');

    let optionsHtml = '';
    ['A', 'B', 'C', 'D'].forEach(letter => {{
      const text = q.opts[letter] || '';
      let optClass = 'opt-btn';
      if (currentMode === 'instant' || examSubmitted) {{
        if (answered) {{
          optClass += ' locked';
          if (letter === q.ans) optClass += ' correct';
          else if (userAnswers[q.id] === letter && letter !== q.ans) optClass += ' wrong';
        }}
      }} else {{
        if (userAnswers[q.id] === letter) optClass += ' selected-exam';
      }}

      optionsHtml += `
        <div class="${{optClass}}" onclick="handleSelectOption(${{q.id}}, '${{letter}}')">
          <div class="opt-badge">${{letter}}</div>
          <div class="opt-txt">${{text}}</div>
        </div>`;
    }});

    const showExp = (currentMode === 'instant' && answered) || examSubmitted;

    card.innerHTML = `
      <div class="q-top">
        <div class="q-top-left">
          <span class="q-num-pill">第 ${{numStr}} 题</span>
          <span class="q-grp-pill">${{groupLabel}}</span>
        </div>
        <span class="q-source-tag">${{q.src || '统考真题'}}</span>
      </div>
      <div class="q-stem">${{q.q}}</div>
      <div class="options-col">${{optionsHtml}}</div>
      <div class="exp-box ${{showExp ? 'visible' : ''}}" id="exp_${{q.id}}">
        <div class="exp-top">
          <span class="exp-ans-badge">正确答案：${{q.ans}}</span>
          <span class="exp-title">💡 深度考点解析</span>
        </div>
        <div class="exp-body">${{q.exp || '暂无详细机理解析'}}</div>
      </div>
    `;

    container.appendChild(card);
  }});

  renderPalette();
  updateHUD();
}}

function renderPalette() {{
  const grid = document.getElementById('paletteGrid');
  grid.innerHTML = '';

  mcqData.forEach(q => {{
    const btn = document.createElement('button');
    btn.className = 'pal-btn';
    btn.textContent = q.id;
    btn.onclick = () => scrollToQuestion(q.id);

    if (userAnswers[q.id] !== undefined) {{
      if (currentMode === 'instant' || examSubmitted) {{
        if (userAnswers[q.id] === q.ans) btn.classList.add('correct');
        else btn.classList.add('wrong');
      }} else {{
        btn.classList.add('answered');
      }}
    }}

    grid.appendChild(btn);
  }});
}}

function renderWritten() {{
  const container = document.getElementById('writtenContainer');
  container.innerHTML = '';

  writtenData.forEach((sec, idx) => {{
    if (sec.type === 'mandatory') {{
      const card = document.createElement('div');
      card.className = 'written-card';
      
      let subqsHtml = '';
      if (sec.subqs) {{
        sec.subqs.forEach(sq => {{
          let tblHtml = '';
          if (sq.table) {{
            tblHtml = `<table class="w-table">
              <thead><tr><th>原料材料名称</th><th>烘焙百分比(%)</th><th>实际重量(g)</th></tr></thead>
              <tbody>` + sq.table.map(r => `<tr><td><strong>${{r.m}}</strong></td><td>${{r.p}}</td><td>${{r.w}}</td></tr>`).join('') +
              `</tbody></table>`;
          }}
          subqsHtml += `<div style="margin-bottom:12px;">
            <div style="font-weight:700;color:#1E293B;">${{sq.label}} ${{sq.text}}</div>
            ${{tblHtml}}
          </div>`;
        }});
      }}

      card.innerHTML = `
        <div class="wc-head">
          <span class="wc-label">${{sec.label}}</span>
          <span class="wc-pts">满分 10 分 · 必答</span>
        </div>
        <div class="wc-stem">${{sec.stem}}</div>
        ${{subqsHtml}}
        <div class="draft-box">
          <div class="draft-label"><span>✍️ 考生作答思考草稿区：</span><span>(本地实时输入，不计分)</span></div>
          <textarea class="draft-area" placeholder="请在此输入您的作答提纲或计算步骤..."></textarea>
        </div>
        <button class="wc-ans-btn" onclick="toggleWrittenAns('ans_mand_${{idx}}')">
          <span>👁️ 查看标准参考答案与评分要点</span>
          <span>▼</span>
        </button>
        <div class="wc-ans-panel" id="ans_mand_${{idx}}">
          <div class="wc-ans-text">${{sec.answer}}</div>
        </div>
      `;
      container.appendChild(card);
    }} else if (sec.type === 'optional') {{
      const header = document.createElement('div');
      header.className = 'group-divider';
      header.innerHTML = `<div class="gd-line"></div>
        <div class="gd-badge">${{sec.label}}</div>
        <div class="gd-line"></div>`;
      container.appendChild(header);

      if (sec.questions) {{
        sec.questions.forEach(q => {{
          const card = document.createElement('div');
          card.className = 'written-card';
          card.innerHTML = `
            <div class="wc-head">
              <span class="wc-label">乙组选答 · 第 ${{q.id}} 题</span>
              <span class="wc-pts">10 分</span>
            </div>
            <div class="wc-stem">${{q.stem}}</div>
            <div class="draft-box">
              <div class="draft-label"><span>✍️ 考生作答思考草稿区：</span><span>(本地实时输入，不计分)</span></div>
              <textarea class="draft-area" placeholder="请在此输入您的作答提纲或核心考点..."></textarea>
            </div>
            <button class="wc-ans-btn" onclick="toggleWrittenAns('ans_opt_${{q.id}}')">
              <span>👁️ 查看标准参考答案与评分细则</span>
              <span>▼</span>
            </button>
            <div class="wc-ans-panel" id="ans_opt_${{q.id}}">
              <div class="wc-ans-text">${{q.answer}}</div>
            </div>
          `;
          container.appendChild(card);
        }});
      }}
    }}
  }});
}}

// 4. Interactive Logics
function handleSelectOption(qid, letter) {{
  if (currentMode === 'instant' && userAnswers[qid] !== undefined) {{
    return; // Already answered in instant mode
  }}
  if (examSubmitted) return;

  userAnswers[qid] = letter;
  renderMCQ();
}}

function scrollToQuestion(qid) {{
  const el = document.getElementById(`qCard_${{qid}}`);
  if (el) {{
    if (el.style.display === 'none') {{
      setFilter('all');
    }}
    el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
  }}
}}

function togglePalette() {{
  const p = document.getElementById('paletteBox');
  p.classList.toggle('hidden');
}}

function toggleWrittenAns(panelId) {{
  const panel = document.getElementById(panelId);
  if (panel) {{
    panel.classList.toggle('visible');
  }}
}}

function switchSection(secNum) {{
  const t1 = document.getElementById('tabBtn1');
  const t2 = document.getElementById('tabBtn2');
  const sMcq = document.getElementById('sectionMcq');
  const sWritten = document.getElementById('sectionWritten');

  if (secNum === 1) {{
    t1.classList.add('active');
    t2.classList.remove('active');
    sMcq.style.display = 'block';
    sWritten.classList.remove('active');
  }} else {{
    t2.classList.add('active');
    t1.classList.remove('active');
    sMcq.style.display = 'none';
    sWritten.classList.add('active');
  }}
}}

function setFilter(filterType) {{
  currentFilter = filterType;
  ['fAll', 'fUnans', 'fAns', 'fWrong'].forEach(id => {{
    const btn = document.getElementById(id);
    if (btn) btn.classList.remove('active');
  }});
  const activeBtn = document.getElementById(
    filterType === 'all' ? 'fAll' : (filterType === 'unans' ? 'fUnans' : (filterType === 'ans' ? 'fAns' : 'fWrong'))
  );
  if (activeBtn) activeBtn.classList.add('active');

  renderMCQ();
}}

function setMode(mode) {{
  currentMode = mode;
  const b1 = document.getElementById('btnModeInstant');
  const b2 = document.getElementById('btnModeExam');
  const tBox = document.getElementById('hudTimerBox');
  const fBar = document.getElementById('floatingBar');

  if (mode === 'instant') {{
    b1.classList.add('active');
    b2.classList.remove('active');
    tBox.style.display = 'none';
    fBar.classList.add('hidden');
    stopTimer();
  }} else {{
    b2.classList.add('active');
    b1.classList.remove('active');
    tBox.style.display = 'flex';
    fBar.classList.remove('hidden');
    startTimer();
  }}
  renderMCQ();
}}

function updateHUD() {{
  const answeredCount = Object.keys(userAnswers).length;
  let correctCount = 0;
  Object.keys(userAnswers).forEach(qid => {{
    const q = mcqData.find(item => item.id == qid);
    if (q && userAnswers[qid] === q.ans) correctCount++;
  }});

  document.getElementById('hudAnswered').textContent = `${{answeredCount}} / ${{mcqData.length}}`;
  const accuracy = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;
  document.getElementById('hudAccuracy').textContent = `${{accuracy}}%`;
  
  const fsInfo = document.getElementById('fsAnsweredInfo');
  if (fsInfo) fsInfo.textContent = `已答 ${{answeredCount}} / ${{mcqData.length}}`;
}}

function startTimer() {{
  stopTimer();
  timerInterval = setInterval(() => {{
    if (timerSeconds <= 0) {{
      stopTimer();
      alert('考试时间到！系统正在自动为您交卷结算。');
      submitExam();
      return;
    }}
    timerSeconds--;
    const m = Math.floor(timerSeconds / 60);
    const s = timerSeconds % 60;
    const mStr = m < 10 ? '0' + m : m;
    const sStr = s < 10 ? '0' + s : s;
    document.getElementById('hudTimer').textContent = `${{mStr}}:${{sStr}}`;
  }}, 1000);
}}

function stopTimer() {{
  if (timerInterval) clearInterval(timerInterval);
  timerInterval = null;
}}

function submitExam() {{
  examSubmitted = true;
  stopTimer();

  let correctCount = 0;
  let grpScores = {{ 'A': {{ c: 0, t: 40 }}, 'B': {{ c: 0, t: 10 }}, 'C': {{ c: 0, t: 10 }} }};

  mcqData.forEach(q => {{
    if (userAnswers[q.id] === q.ans) {{
      correctCount++;
      if (grpScores[q.g]) grpScores[q.g].c++;
    }}
  }});

  const pct = Math.round((correctCount / mcqData.length) * 100);
  let grade = 'A1 (极优)';
  let emoji = '🏆';
  if (pct >= 85) {{ grade = 'A1 (优等第一级)'; emoji = '🏆'; }}
  else if (pct >= 80) {{ grade = 'A2 (优等第二级)'; emoji = '🌟'; }}
  else if (pct >= 75) {{ grade = 'B3 (良好)'; emoji = '✨'; }}
  else if (pct >= 70) {{ grade = 'B4 (良好)'; emoji = '👍'; }}
  else if (pct >= 60) {{ grade = 'B5/B6 (及格)'; emoji = '📈'; }}
  else {{ grade = '需加强巩固'; emoji = '💪'; }}

  document.getElementById('modalEmoji').textContent = emoji;
  document.getElementById('modalScore').textContent = `${{correctCount}} / ${{mcqData.length}}`;
  document.getElementById('modalGrade').textContent = `得分率：${{pct}}% · 统考预估：${{grade}}`;
  document.getElementById('modalBreakdown').innerHTML = `
    <strong>各模块答题详情：</strong><br>
    🥐 甲组·烘焙理论：${{grpScores['A'].c}} / 40 (${{Math.round(grpScores['A'].c/40*100)}}%)<br>
    🥩 乙组·西餐烹调：${{grpScores['B'].c}} / 10 (${{Math.round(grpScores['B'].c/10*100)}}%)<br>
    🥢 丙组·亚洲烹调：${{grpScores['C'].c}} / 10 (${{Math.round(grpScores['C'].c/10*100)}}%)
  `;

  document.getElementById('examModal').classList.add('visible');
  document.getElementById('floatingBar').classList.add('hidden');
  renderMCQ();
}}

function closeModalAndReview() {{
  document.getElementById('examModal').classList.remove('visible');
}}

function resetAll() {{
  if (confirm('确定要清空本卷的作答记录重新开始吗？')) {{
    userAnswers = {{}};
    examSubmitted = false;
    timerSeconds = 80 * 60;
    document.getElementById('hudTimer').textContent = '80:00';
    document.getElementById('examModal').classList.remove('visible');
    renderMCQ();
    if (currentMode === 'exam') {{
      startTimer();
      document.getElementById('floatingBar').classList.remove('hidden');
    }}
  }}
}}

// Initialize
renderMCQ();
renderWritten();
</script>
</body>
</html>
"""

# 2. Build Paper A
configA = {
    'paper_id': 'A',
    'paper_title': '模拟卷 A · 历届高频真题精选重组卷',
    'paper_subtitle': '严格精选 2020~2025 年统考高频复现考点 · 稳固基础盘 50 分以上',
    'paper_desc': '本卷试题均精选自 2020~2025 年六届统考真题中复现率最高的核心考题（含搅拌六阶段、酵母换算、五大母酱、蛋糕三大类、中餐刀工规范等），配齐详细评分解析与作答要点。',
    'badge_text': '真题精选 · 稳固基础',
    'mcq_code': paperA_mcq_code,
    'written_code': paperA_written_code,
    'out_filename': '模拟卷A_历届高频真题精选卷.html',
    'nav_links_html': '<a class="hdr-back" href="模拟卷B_2026前瞻预测试题卷.html">🔮 <span class="hide-mobile">模拟</span>卷 B</a><a class="hdr-back" href="模拟卷C_2026统考短选项实战冲刺卷.html">⚡ <span class="hide-mobile">模拟</span>卷 C</a>'
}
pathA = os.path.join(ROOT_DIR, configA['out_filename'])
with open(pathA, 'w', encoding='utf-8') as f:
    f.write(get_paper_template(configA))
print(f"Generated {configA['out_filename']}: {os.path.getsize(pathA)} bytes")

# 3. Build Paper B
configB = {
    'paper_id': 'B',
    'paper_title': '模拟卷 B · 2026统考前瞻预测试题卷',
    'paper_subtitle': '融合现代烹饪前沿趋势 · 模拟拔尖考题 · 冲刺 A1 / A2 优等等级',
    'paper_desc': '本卷紧扣 2026 年统考最新命题动向与行业趋势，重点考查低温慢煮（Sous-vide）、天然酸种酵母（Sourdough）、第四种红宝石巧克力（Ruby chocolate）、过敏原与HACCP高阶应用，助推优等生冲刺卓越成绩。',
    'badge_text': '前瞻预测 · 冲刺卓越',
    'mcq_code': paperB_mcq_code,
    'written_code': paperB_written_code,
    'out_filename': '模拟卷B_2026前瞻预测试题卷.html',
    'nav_links_html': '<a class="hdr-back" href="模拟卷A_历届高频真题精选卷.html">📄 <span class="hide-mobile">模拟</span>卷 A</a><a class="hdr-back" href="模拟卷C_2026统考短选项实战冲刺卷.html">⚡ <span class="hide-mobile">模拟</span>卷 C</a>'
}
pathB = os.path.join(ROOT_DIR, configB['out_filename'])
with open(pathB, 'w', encoding='utf-8') as f:
    f.write(get_paper_template(configB))
print(f"Generated {configB['out_filename']}: {os.path.getsize(pathB)} bytes")

# 4. Build Paper C (Short-sentence options UEC simulation)
configC = {
    'paper_id': 'C',
    'paper_title': '模拟卷 C · 2026统考短选项实战冲刺卷',
    'paper_subtitle': '100% 仿真董总统考真实“短选项/专有名词/数值速断”命题风格 · 训练 80 分钟实战秒杀节奏',
    'paper_desc': '本卷严格针对真实统考考场中 75% 以上考题为“短词汇、专有名词、分类术语、温度参数、化学原料”的命题实战特征，彻底摆脱冗长题干与长选项干扰，全真训练学生在 80 分钟内对核心知识点的秒杀反应速度！',
    'badge_text': '短词秒杀 · 全真实战',
    'mcq_code': paperC_mcq_code,
    'written_code': paperC_written_code,
    'out_filename': '模拟卷C_2026统考短选项实战冲刺卷.html',
    'nav_links_html': '<a class="hdr-back" href="模拟卷A_历届高频真题精选卷.html">📄 <span class="hide-mobile">模拟</span>卷 A</a><a class="hdr-back" href="模拟卷B_2026前瞻预测试题卷.html">🔮 <span class="hide-mobile">模拟</span>卷 B</a>'
}
pathC = os.path.join(ROOT_DIR, configC['out_filename'])
with open(pathC, 'w', encoding='utf-8') as f:
    f.write(get_paper_template(configC))
print(f"Generated {configC['out_filename']}: {os.path.getsize(pathC)} bytes")

print("All 3 standalone mock exam papers successfully compiled!")
