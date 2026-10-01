
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

OUTPUT_FILE = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\2026年统考厨艺理论_历届全真模拟考场(双卷全真模考系统).html'

html = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2026年统考厨艺理论 · 历届全真模拟考场（双卷）</title>
<meta name="description" content="2026马来西亚华文独中统考厨艺理论历届全真模拟考场，含模拟卷A（历届高频真题精选）与模拟卷B（2026前瞻预测），选择题+作答题全格式。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ═══════════════════════════════════════════════════
   DESIGN SYSTEM – MOCK EXAM PORTAL
   色调：深焙褐金 × 暗夜学院风
══════════════════════════════════════════════════ */
:root {
  --bg-deep:      #0f0c09;
  --bg-card:      #1a1510;
  --bg-hover:     #221c14;
  --gold:         #c9922c;
  --gold-light:   #e8b84b;
  --gold-dim:     #8a6020;
  --cream:        #f5ead5;
  --cream-dim:    #c0b090;
  --accent-A:     #d47a3a;
  --accent-B:     #4a7fb5;
  --correct:      #3a9e6f;
  --wrong:        #c04040;
  --warn:         #c08030;
  --border:       #3a2e1e;
  --border-gold:  #6a5020;
  --text-main:    #e8dcc8;
  --text-dim:     #9a8870;
  --tag-A:        #8b3a1a;
  --tag-B:        #1a4a6b;
  --tag-C:        #1a5a2a;
  --radius:       12px;
  --shadow:       0 4px 24px rgba(0,0,0,0.6);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg-deep);
  color: var(--text-main);
  font-family: 'Inter', 'Noto Serif SC', sans-serif;
  min-height: 100vh;
  line-height: 1.7;
}

/* ── TOP HEADER ── */
.site-header {
  background: linear-gradient(135deg, #1a1208 0%, #0f0c09 50%, #120e08 100%);
  border-bottom: 1px solid var(--border-gold);
  padding: 0;
  position: sticky; top: 0; z-index: 100;
  backdrop-filter: blur(10px);
}
.header-inner {
  max-width: 1200px; margin: 0 auto;
  padding: 16px 24px;
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
}
.site-title {
  font-family: 'Noto Serif SC', serif;
  font-size: clamp(14px, 2vw, 18px);
  font-weight: 700;
  color: var(--gold-light);
  letter-spacing: 0.04em;
}
.site-badge {
  font-size: 11px; color: var(--text-dim);
  border: 1px solid var(--border); border-radius: 20px;
  padding: 3px 10px; white-space: nowrap;
}

/* ── HERO SECTION ── */
.hero {
  max-width: 1200px; margin: 0 auto;
  padding: 48px 24px 32px;
  text-align: center;
}
.hero-eyebrow {
  font-size: 12px; letter-spacing: 0.2em;
  color: var(--gold-dim); text-transform: uppercase;
  margin-bottom: 12px;
}
.hero-title {
  font-family: 'Noto Serif SC', serif;
  font-size: clamp(24px, 4vw, 38px);
  font-weight: 700;
  background: linear-gradient(135deg, var(--gold-light), var(--gold), var(--accent-A));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 16px; line-height: 1.3;
}
.hero-subtitle {
  font-size: 14px; color: var(--text-dim); max-width: 600px; margin: 0 auto 32px;
}

/* ── DATA ANALYSIS SECTION ── */
.analysis-section {
  max-width: 1200px; margin: 0 auto; padding: 0 24px 48px;
}
.section-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 20px; font-weight: 700;
  color: var(--gold-light);
  display: flex; align-items: center; gap: 10px;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}
.section-title::before {
  content: '';
  display: block; width: 4px; height: 24px;
  background: linear-gradient(to bottom, var(--gold), var(--accent-A));
  border-radius: 2px;
}

/* Analysis Cards Grid */
.analysis-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 32px;
}
.analysis-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  transition: border-color 0.2s;
}
.analysis-card:hover { border-color: var(--border-gold); }
.analysis-card h3 {
  font-size: 14px; font-weight: 600;
  color: var(--gold); margin-bottom: 16px;
  display: flex; align-items: center; gap: 8px;
}

/* Frequency Bar Chart */
.freq-chart { display: flex; flex-direction: column; gap: 10px; }
.freq-row { display: flex; align-items: center; gap: 10px; }
.freq-label {
  font-size: 12px; color: var(--text-main);
  min-width: 110px; text-align: right;
}
.freq-bar-wrap {
  flex: 1; background: rgba(255,255,255,0.05);
  border-radius: 4px; height: 20px; overflow: hidden;
}
.freq-bar {
  height: 100%; border-radius: 4px;
  background: linear-gradient(90deg, var(--gold-dim), var(--gold));
  transition: width 1s ease;
  display: flex; align-items: center; justify-content: flex-end;
  padding-right: 6px;
}
.freq-bar span { font-size: 10px; color: #0f0c09; font-weight: 700; }
.freq-bar.rank1 { background: linear-gradient(90deg, #b8860b, var(--gold-light)); }
.freq-bar.rank2 { background: linear-gradient(90deg, #a07010, #e8a030); }
.freq-bar.rank3 { background: linear-gradient(90deg, #8a6020, #c09020); }

/* Topic Distribution Table */
.dist-table { width: 100%; border-collapse: collapse; font-size: 13px; }
.dist-table th {
  background: rgba(201,146,44,0.15);
  color: var(--gold); font-weight: 600;
  padding: 8px 12px; text-align: left;
  border-bottom: 1px solid var(--border-gold);
}
.dist-table td {
  padding: 8px 12px; border-bottom: 1px solid var(--border);
  color: var(--text-main);
}
.dist-table tr:hover td { background: var(--bg-hover); }
.badge {
  display: inline-block; padding: 2px 8px; border-radius: 10px;
  font-size: 11px; font-weight: 600;
}
.badge-A { background: rgba(139,58,26,0.4); color: #ff9966; }
.badge-B { background: rgba(26,74,107,0.4); color: #66aaff; }
.badge-C { background: rgba(26,90,42,0.4); color: #66cc88; }

/* Year Timeline */
.timeline-wrap { display: flex; flex-direction: column; gap: 8px; }
.timeline-row {
  display: grid; grid-template-columns: 50px 1fr;
  align-items: center; gap: 12px;
}
.t-year {
  font-size: 12px; font-weight: 600; color: var(--gold);
  text-align: center;
}
.t-topics { display: flex; flex-wrap: wrap; gap: 4px; }
.t-chip {
  font-size: 10px; padding: 2px 7px; border-radius: 8px;
  background: rgba(201,146,44,0.12); border: 1px solid var(--border-gold);
  color: var(--cream-dim);
}

/* ── PAPER TAB NAV ── */
.paper-nav {
  max-width: 1200px; margin: 0 auto;
  padding: 0 24px 0;
  display: flex; gap: 8px;
  border-bottom: 2px solid var(--border);
  margin-bottom: 0;
}
.paper-tab {
  padding: 14px 28px;
  background: none; border: none; cursor: pointer;
  font-family: 'Noto Serif SC', serif;
  font-size: 14px; font-weight: 600;
  color: var(--text-dim);
  border-bottom: 3px solid transparent;
  margin-bottom: -2px; transition: all 0.2s;
  display: flex; align-items: center; gap: 8px;
}
.paper-tab:hover { color: var(--cream); }
.paper-tab.active-A { color: var(--accent-A); border-bottom-color: var(--accent-A); }
.paper-tab.active-B { color: var(--accent-B); border-bottom-color: var(--accent-B); }
.tab-dot {
  width: 8px; height: 8px; border-radius: 50%;
}
.dot-A { background: var(--accent-A); }
.dot-B { background: var(--accent-B); }

/* ── PAPER PANEL ── */
.paper-panel { display: none; max-width: 1200px; margin: 0 auto; padding: 32px 24px 48px; }
.paper-panel.active { display: block; }

.paper-header {
  background: var(--bg-card);
  border: 1px solid var(--border); border-radius: var(--radius);
  padding: 28px 32px; margin-bottom: 28px;
  position: relative; overflow: hidden;
}
.paper-header::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
}
.paper-header.hdr-A::before { background: linear-gradient(90deg, var(--accent-A), var(--gold)); }
.paper-header.hdr-B::before { background: linear-gradient(90deg, var(--accent-B), #6aabdf); }

.paper-title {
  font-family: 'Noto Serif SC', serif;
  font-size: 20px; font-weight: 700;
  margin-bottom: 8px;
}
.paper-title-A { color: var(--accent-A); }
.paper-title-B { color: #6aabdf; }
.paper-meta {
  font-size: 13px; color: var(--text-dim);
  display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 16px;
}
.paper-meta span { display: flex; align-items: center; gap: 5px; }

/* Mode Toggle */
.mode-row {
  display: flex; gap: 10px; align-items: center;
  flex-wrap: wrap; margin-top: 16px;
}
.mode-btn {
  padding: 8px 18px; border-radius: 20px; border: 1px solid var(--border);
  background: none; color: var(--text-dim); font-size: 13px;
  cursor: pointer; transition: all 0.2s;
}
.mode-btn:hover { border-color: var(--gold); color: var(--cream); }
.mode-btn.active { background: var(--gold-dim); border-color: var(--gold); color: #fff; }

/* Timer Display */
.timer-display {
  display: none; align-items: center; gap: 8px;
  padding: 8px 16px; background: rgba(201,146,44,0.1);
  border: 1px solid var(--border-gold); border-radius: 20px;
  font-size: 18px; font-weight: 700; color: var(--gold-light);
  font-family: 'Inter', monospace;
}
.timer-display.active { display: flex; }
.timer-display.urgent { color: #ff6666; border-color: #ff4444; animation: pulse 1s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.6} }

/* Score Board */
.score-board {
  display: none;
  background: var(--bg-card); border: 1px solid var(--border-gold);
  border-radius: var(--radius); padding: 24px; margin-bottom: 24px;
}
.score-board.visible { display: block; }
.score-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 16px; }
.score-item { text-align: center; }
.score-num { font-size: 36px; font-weight: 700; font-family: 'Inter', sans-serif; }
.score-num.main { color: var(--gold-light); }
.score-num.grp-A { color: var(--accent-A); }
.score-num.grp-B { color: var(--accent-B); }
.score-num.grp-C { color: #66cc88; }
.score-label { font-size: 12px; color: var(--text-dim); margin-top: 4px; }

/* ── EXAM SECTION HEADER ── */
.exam-section-hdr {
  font-family: 'Noto Serif SC', serif;
  font-size: 16px; font-weight: 700;
  color: var(--gold);
  padding: 16px 20px;
  background: rgba(201,146,44,0.08);
  border: 1px solid var(--border-gold);
  border-radius: var(--radius);
  margin-bottom: 16px;
  margin-top: 28px;
  display: flex; align-items: center; justify-content: space-between;
}
.exam-section-hdr:first-child { margin-top: 0; }
.section-tag {
  font-size: 11px; color: var(--text-dim);
  background: rgba(0,0,0,0.3); padding: 3px 10px; border-radius: 10px;
}

/* ── QUESTION CARD ── */
.q-card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  margin-bottom: 14px;
  overflow: hidden;
  transition: border-color 0.2s;
}
.q-card:hover { border-color: var(--border-gold); }
.q-card.answered-correct { border-color: var(--correct); }
.q-card.answered-wrong { border-color: var(--wrong); }

.q-header {
  padding: 16px 20px 0;
  display: flex; align-items: flex-start; gap: 12px;
}
.q-num {
  min-width: 32px; height: 32px;
  background: rgba(201,146,44,0.15);
  border: 1px solid var(--border-gold);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; font-weight: 700; color: var(--gold);
  flex-shrink: 0;
}
.q-num.correct-num { background: rgba(58,158,111,0.2); border-color: var(--correct); color: var(--correct); }
.q-num.wrong-num { background: rgba(192,64,64,0.2); border-color: var(--wrong); color: var(--wrong); }

.q-meta-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
.q-source-tag {
  font-size: 10px; padding: 2px 8px; border-radius: 8px;
  background: rgba(201,146,44,0.12); border: 1px solid var(--border-gold);
  color: var(--gold-dim);
}
.q-source-tag.src-A { background: rgba(139,58,26,0.2); border-color: #8b3a1a; color: #ffaa77; }
.q-source-tag.src-B { background: rgba(26,74,107,0.2); border-color: #1a4a6b; color: #88bbff; }
.q-source-tag.src-predict { background: rgba(80,40,100,0.3); border-color: #6a3a8a; color: #cc88ff; }

.q-stem {
  font-size: 14px; line-height: 1.8; color: var(--text-main);
  padding: 0 20px 14px 64px;
  white-space: pre-wrap;
}
.q-options {
  padding: 0 20px 16px 64px;
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 8px;
}
@media (max-width: 640px) { .q-options { grid-template-columns: 1fr; } }

.q-opt {
  padding: 10px 14px;
  border: 1px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  font-size: 13px; color: var(--text-main);
  transition: all 0.15s;
  display: flex; align-items: flex-start; gap: 10px;
}
.q-opt:hover { border-color: var(--gold-dim); background: rgba(201,146,44,0.08); }
.q-opt.selected { border-color: var(--gold); background: rgba(201,146,44,0.12); }
.q-opt.correct-opt { border-color: var(--correct)!important; background: rgba(58,158,111,0.15)!important; color: #7de8aa!important; }
.q-opt.wrong-opt { border-color: var(--wrong)!important; background: rgba(192,64,64,0.15)!important; color: #ff9999!important; }
.q-opt.disabled { cursor: default; pointer-events: none; }

.opt-letter {
  min-width: 22px; height: 22px; border-radius: 50%;
  background: rgba(255,255,255,0.08);
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; color: var(--text-dim);
  flex-shrink: 0;
}
.q-opt.correct-opt .opt-letter { background: var(--correct); color: #fff; }
.q-opt.wrong-opt .opt-letter { background: var(--wrong); color: #fff; }

/* Explanation Box */
.q-explain {
  display: none;
  margin: 0 20px 16px 64px;
  padding: 14px 16px;
  background: rgba(201,146,44,0.06);
  border-left: 3px solid var(--gold-dim);
  border-radius: 0 8px 8px 0;
  font-size: 13px; line-height: 1.8; color: var(--cream-dim);
}
.q-explain.visible { display: block; }
.explain-title {
  font-size: 11px; font-weight: 600; color: var(--gold);
  letter-spacing: 0.1em; margin-bottom: 6px;
  text-transform: uppercase;
}

/* ── WRITTEN SECTION ── */
.written-section {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  margin-bottom: 14px;
  overflow: hidden;
}
.written-header {
  padding: 20px 24px;
  background: rgba(201,146,44,0.06);
  border-bottom: 1px solid var(--border);
  font-family: 'Noto Serif SC', serif;
  font-size: 15px; font-weight: 700; color: var(--gold-light);
}
.written-body { padding: 20px 24px; }
.written-stem {
  font-size: 14px; color: var(--text-main);
  line-height: 1.9; margin-bottom: 16px;
  white-space: pre-wrap;
}
.written-sub {
  background: rgba(0,0,0,0.2);
  border: 1px solid var(--border);
  border-radius: 8px; padding: 16px 18px;
  margin-bottom: 12px;
}
.sub-label {
  font-size: 13px; font-weight: 600; color: var(--gold);
  margin-bottom: 8px;
}
.sub-text { font-size: 13px; color: var(--text-main); line-height: 1.8; white-space: pre-wrap; }

/* Baking percentage table */
.baking-table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; }
.baking-table th {
  background: rgba(201,146,44,0.15); color: var(--gold);
  padding: 8px 12px; border: 1px solid var(--border-gold);
}
.baking-table td {
  padding: 8px 12px; border: 1px solid var(--border);
  color: var(--text-main); text-align: center;
}
.baking-table tr.total td { background: rgba(201,146,44,0.08); font-weight: 600; }

/* Reveal Answer Button */
.reveal-btn {
  padding: 10px 20px;
  background: none;
  border: 1px solid var(--border-gold);
  border-radius: 8px;
  color: var(--gold);
  font-size: 13px; cursor: pointer;
  transition: all 0.2s;
  display: flex; align-items: center; gap: 6px; margin-top: 12px;
}
.reveal-btn:hover { background: rgba(201,146,44,0.1); border-color: var(--gold); }
.answer-box {
  display: none; margin-top: 14px;
  padding: 16px; background: rgba(58,158,111,0.08);
  border: 1px solid rgba(58,158,111,0.3);
  border-radius: 8px;
  font-size: 13px; color: #99ddbb; line-height: 1.9;
  white-space: pre-wrap;
}
.answer-box.visible { display: block; }
.answer-label {
  font-size: 11px; font-weight: 600;
  color: var(--correct); letter-spacing: 0.1em;
  text-transform: uppercase; margin-bottom: 8px;
  display: block;
}

/* ── EXAM MODE OVERLAY ── */
.exam-submit-btn {
  display: block; width: 100%;
  padding: 16px 32px; margin-top: 28px;
  background: linear-gradient(135deg, var(--gold-dim), var(--gold));
  border: none; border-radius: var(--radius);
  font-family: 'Noto Serif SC', serif;
  font-size: 16px; font-weight: 700;
  color: #1a1208; cursor: pointer;
  transition: all 0.2s; letter-spacing: 0.05em;
}
.exam-submit-btn:hover { filter: brightness(1.15); transform: translateY(-1px); }

/* Progress Bar */
.progress-wrap {
  height: 4px; background: var(--border);
  border-radius: 2px; margin: 12px 0; overflow: hidden;
}
.progress-fill {
  height: 100%; border-radius: 2px;
  background: linear-gradient(90deg, var(--gold-dim), var(--gold-light));
  transition: width 0.3s;
}

/* ── FOOTER ── */
.site-footer {
  border-top: 1px solid var(--border);
  padding: 32px 24px;
  text-align: center;
  color: var(--text-dim);
  font-size: 12px; line-height: 2;
}
.site-footer em { color: var(--gold-dim); font-style: italic; }

/* Responsive */
@media (max-width: 768px) {
  .q-options { padding: 0 14px 14px; grid-template-columns: 1fr; }
  .q-stem { padding: 0 14px 12px; }
  .q-header { padding: 14px 14px 0; }
  .written-body { padding: 14px; }
  .paper-tab { padding: 10px 14px; font-size: 12px; }
}
</style>
</head>
<body>

<!-- ── TOP HEADER ── -->
<header class="site-header">
  <div class="header-inner">
    <div class="site-title">📚 2026年统考厨艺理论 · 全真模拟考场</div>
    <div class="site-badge">v2026.10-Build.04</div>
  </div>
</header>

<!-- ── HERO ── -->
<div class="hero">
  <div class="hero-eyebrow">马来西亚华文独中统一考试 · SY26</div>
  <h1 class="hero-title">历届全真模拟考场<br>双卷全真模考系统</h1>
  <p class="hero-subtitle">基于2020~2025年六届真实统考试题深度剖析，精心构建全格式模拟体验（选择题＋作答题）</p>
</div>

<!-- ══════════════════════════════════════════
     SECTION 1: DATA ANALYSIS
════════════════════════════════════════════ -->
<div class="analysis-section">
  <h2 class="section-title">📊 2020~2025 历届统考大数据分析</h2>

  <div class="analysis-grid">

    <!-- Chart 1: Frequency Chart -->
    <div class="analysis-card" style="grid-column: span 2;">
      <h3>🔥 高频必考考点（2020~2025 年出现频次）</h3>
      <div class="freq-chart" id="freqChart"></div>
    </div>

    <!-- Chart 2: Topic Distribution -->
    <div class="analysis-card">
      <h3>📋 试卷一命题配比（历年固定格式）</h3>
      <table class="dist-table">
        <thead>
          <tr><th>组别</th><th>题量</th><th>占比</th><th>核心考查内容</th></tr>
        </thead>
        <tbody>
          <tr><td><span class="badge badge-A">甲组</span></td><td>40题</td><td>67%</td><td>烘焙理论与实务</td></tr>
          <tr><td><span class="badge badge-B">乙组</span></td><td>10题</td><td>17%</td><td>西餐烹调艺术</td></tr>
          <tr><td><span class="badge badge-C">丙组</span></td><td>10题</td><td>17%</td><td>亚洲烹调艺术</td></tr>
          <tr style="border-top:2px solid var(--border-gold)"><td colspan="2"><strong style="color:var(--gold)">合计 60题</strong></td><td>100%</td><td>80分钟完成</td></tr>
        </tbody>
      </table>
    </div>

    <!-- Chart 3: Year Timeline -->
    <div class="analysis-card">
      <h3>📅 历届考题主题年度对照</h3>
      <div class="timeline-wrap">
        <div class="timeline-row"><div class="t-year">2025</div><div class="t-topics"><span class="t-chip">搅拌阶段</span><span class="t-chip">Ruby巧克力</span><span class="t-chip">中餐调味料</span><span class="t-chip">Maillard</span><span class="t-chip">意式蛋白霜</span></div></div>
        <div class="timeline-row"><div class="t-year">2024</div><div class="t-topics"><span class="t-chip">烘焙百分比计算</span><span class="t-chip">荷兰酱</span><span class="t-chip">水波煮</span><span class="t-chip">牛排熟度</span><span class="t-chip">沙门氏菌</span></div></div>
        <div class="timeline-row"><div class="t-year">2023</div><div class="t-topics"><span class="t-chip">马卡龙</span><span class="t-chip">五大母酱</span><span class="t-chip">法式洋葱汤</span><span class="t-chip">勾芡</span><span class="t-chip">花刀</span></div></div>
        <div class="timeline-row"><div class="t-year">2022</div><div class="t-topics"><span class="t-chip">蛋白霜三种</span><span class="t-chip">酵母换算</span><span class="t-chip">拔丝</span><span class="t-chip">刀工尺寸</span><span class="t-chip">Salamander</span></div></div>
        <div class="timeline-row"><div class="t-year">2021</div><div class="t-topics"><span class="t-chip">蛋糕三大类</span><span class="t-chip">吉利丁</span><span class="t-chip">法式道纳司</span><span class="t-chip">派皮</span><span class="t-chip">炖火候</span></div></div>
        <div class="timeline-row"><div class="t-year">2020</div><div class="t-topics"><span class="t-chip">比萨分类</span><span class="t-chip">煮沸杀菌</span><span class="t-chip">吐司烘烤</span><span class="t-chip">果胶特性</span><span class="t-chip">安全贮藏</span></div></div>
      </div>
    </div>

    <!-- Chart 4: Paper 2 Past Questions -->
    <div class="analysis-card" style="grid-column: span 2;">
      <h3>📝 试卷二（作答题）历届出题规律</h3>
      <table class="dist-table">
        <thead>
          <tr><th>年份</th><th>甲组必答题（10%）</th><th>乙组选答常见考点</th></tr>
        </thead>
        <tbody>
          <tr><td>2025</td><td>中餐调味料五项及作用</td><td>Maillard反应、意式蛋白霜、麸质(Gluten)、搅拌机三大配件、法式洋葱汤、牛肉部位、中餐刀工五法、粮食制品储存</td></tr>
          <tr><td>2024</td><td>烘焙百分比计算（蛋糕配方）</td><td>菜肴盛盘要求、厨房卫生四大原则、马铃薯挑选、烹调方法温度、牛排熟度四级、食材中英对照</td></tr>
          <tr><td>2023</td><td>（无原文，推测为五大母酱）</td><td>搅拌机配件、高汤类型、刀工五法、食品安全HACCP</td></tr>
          <tr><td>2022</td><td>（无原文）</td><td>烤箱使用三大注意、巧克力蛋糕配方计算、宴会小点三重点、法国菜城市、菜肴起源省份</td></tr>
          <tr><td>2021</td><td>专有名词解释（Paprika/Salami/Striped sandwich）</td><td>蛋糕三大分类、烤箱三重点、烘焙百分比计算、宴会小点、法国菜、菜肴起源省份、麒麟蒸鱼</td></tr>
          <tr><td>2020</td><td>（推测题型类似）</td><td>香草知识、高汤储存、西餐技法、中餐刀工</td></tr>
        </tbody>
      </table>
    </div>

  </div><!-- /analysis-grid -->
</div><!-- /analysis-section -->

<!-- ══════════════════════════════════════════
     PAPER TAB NAV
════════════════════════════════════════════ -->
<nav class="paper-nav" style="max-width:1200px;margin:0 auto;padding:0 24px;">
  <button class="paper-tab active-A" onclick="switchTab('A')">
    <span class="tab-dot dot-A"></span> 模拟卷 A · 历届高频真题精选卷
  </button>
  <button class="paper-tab" onclick="switchTab('B')">
    <span class="tab-dot dot-B"></span> 模拟卷 B · 2026前瞻预测试题卷
  </button>
</nav>

<!-- ══════════════════════════════════════════
     PAPER A PANEL
════════════════════════════════════════════ -->
<div class="paper-panel active" id="panelA">

  <!-- Paper Header -->
  <div class="paper-header hdr-A">
    <div class="paper-title paper-title-A">📄 模拟卷 A · 历届高频真题精选重组卷</div>
    <div class="paper-meta">
      <span>🕐 建议时间：80分钟</span>
      <span>📝 题型：试卷一（60题选择）+ 试卷二（作答题）</span>
      <span>🎯 定位：真题原型熟悉 · 稳固基础盘</span>
    </div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:12px;">
      ⭐ 严格对标 40烘焙＋10西餐＋10亚洲格式；题目标注历届真题年份来源
    </div>
    <div class="mode-row">
      <button class="mode-btn active" id="modeA-practice" onclick="setMode('A','practice')">✏️ 随刷即查模式</button>
      <button class="mode-btn" id="modeA-exam" onclick="setMode('A','exam')">🕐 全真模考模式（80分钟）</button>
      <div class="timer-display" id="timerA">⏱ <span id="timerA-text">80:00</span></div>
    </div>
    <div class="progress-wrap" style="margin-top:14px;">
      <div class="progress-fill" id="progressA" style="width:0%"></div>
    </div>
    <div style="font-size:12px;color:var(--text-dim);margin-top:4px;" id="progressLabelA">答题进度：0 / 60</div>
  </div>

  <!-- Score Board -->
  <div class="score-board" id="scoreBoardA">
    <div class="section-title" style="margin-bottom:16px;">🏆 模考成绩单</div>
    <div class="score-grid">
      <div class="score-item"><div class="score-num main" id="totalScoreA">—</div><div class="score-label">总得分 / 60</div></div>
      <div class="score-item"><div class="score-num grp-A" id="scoreA-g1">—</div><div class="score-label">甲组·烘焙 / 40</div></div>
      <div class="score-item"><div class="score-num grp-B" id="scoreA-g2">—</div><div class="score-label">乙组·西餐 / 10</div></div>
      <div class="score-item"><div class="score-num grp-C" id="scoreA-g3">—</div><div class="score-label">丙组·亚洲 / 10</div></div>
    </div>
  </div>

  <!-- ─ PAPER A SECTION 1: MCQ ─ -->
  <div class="exam-section-hdr">
    试卷一 · 选择题（60%）<span class="section-tag">60题 · 全答</span>
  </div>

  <div class="exam-section-hdr" style="background:rgba(139,58,26,0.1);border-color:#8b3a1a;color:var(--accent-A);">
    甲组 · 烘焙理论与实务 <span class="section-tag" style="color:var(--accent-A)">第1~40题</span>
  </div>
  <div id="A-mcq-group1"></div>

  <div class="exam-section-hdr" style="background:rgba(26,74,107,0.1);border-color:#1a4a6b;color:#6aabdf;">
    乙组 · 西餐烹调艺术及实践 <span class="section-tag" style="color:#6aabdf">第41~50题</span>
  </div>
  <div id="A-mcq-group2"></div>

  <div class="exam-section-hdr" style="background:rgba(26,90,42,0.1);border-color:#1a5a2a;color:#66cc88;">
    丙组 · 亚洲烹调艺术及实践 <span class="section-tag" style="color:#66cc88">第51~60题</span>
  </div>
  <div id="A-mcq-group3"></div>

  <!-- Submit Button (Exam Mode) -->
  <button class="exam-submit-btn" id="submitA" style="display:none;" onclick="submitPaper('A')">
    📋 交卷 · 生成成绩单
  </button>

  <!-- ─ PAPER A SECTION 2: WRITTEN ─ -->
  <div class="exam-section-hdr" style="margin-top:36px;">
    试卷二 · 作答题（40%）<span class="section-tag">甲组必答1题 ＋ 乙组选答3题（共7题选3）</span>
  </div>
  <div style="font-size:13px;color:var(--text-dim);margin-bottom:20px;padding:12px 16px;background:rgba(0,0,0,0.2);border-radius:8px;border:1px solid var(--border);">
    💡 作答提示：本试卷二为全真作答格式。请在纸张上认真作答后，再点击「查看参考答案」逐点核对得分。每题参考答案均按评分点拆解，与真实董总改卷标准对应。
  </div>
  <div id="A-written"></div>

</div><!-- /panelA -->

<!-- ══════════════════════════════════════════
     PAPER B PANEL
════════════════════════════════════════════ -->
<div class="paper-panel" id="panelB">

  <!-- Paper Header -->
  <div class="paper-header hdr-B">
    <div class="paper-title paper-title-B">📄 模拟卷 B · 2026统考前瞻预测试题卷</div>
    <div class="paper-meta">
      <span>🕐 建议时间：80分钟</span>
      <span>📝 题型：试卷一（60题选择）+ 试卷二（作答题）</span>
      <span>🎯 定位：新趋势考点 · 冲刺A1/A2高分</span>
    </div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:12px;">
      🔮 融入现代烹饪科学新趋势：低温慢煮(Sous-vide)、天然酸种酵母、对流蒸汽烤炉、Ruby巧克力新工艺
    </div>
    <div class="mode-row">
      <button class="mode-btn active" id="modeB-practice" onclick="setMode('B','practice')">✏️ 随刷即查模式</button>
      <button class="mode-btn" id="modeB-exam" onclick="setMode('B','exam')">🕐 全真模考模式（80分钟）</button>
      <div class="timer-display" id="timerB">⏱ <span id="timerB-text">80:00</span></div>
    </div>
    <div class="progress-wrap" style="margin-top:14px;">
      <div class="progress-fill" id="progressB" style="width:0%;background:linear-gradient(90deg,#1a4a6b,#4a8abf)"></div>
    </div>
    <div style="font-size:12px;color:var(--text-dim);margin-top:4px;" id="progressLabelB">答题进度：0 / 60</div>
  </div>

  <div class="score-board" id="scoreBoardB">
    <div class="section-title" style="margin-bottom:16px;">🏆 模考成绩单</div>
    <div class="score-grid">
      <div class="score-item"><div class="score-num main" id="totalScoreB">—</div><div class="score-label">总得分 / 60</div></div>
      <div class="score-item"><div class="score-num grp-A" id="scoreB-g1">—</div><div class="score-label">甲组·烘焙 / 40</div></div>
      <div class="score-item"><div class="score-num grp-B" id="scoreB-g2">—</div><div class="score-label">乙组·西餐 / 10</div></div>
      <div class="score-item"><div class="score-num grp-C" id="scoreB-g3">—</div><div class="score-label">丙组·亚洲 / 10</div></div>
    </div>
  </div>

  <div class="exam-section-hdr">
    试卷一 · 选择题（60%）<span class="section-tag">60题 · 全答</span>
  </div>
  <div class="exam-section-hdr" style="background:rgba(139,58,26,0.1);border-color:#8b3a1a;color:var(--accent-A);">
    甲组 · 烘焙理论与实务 <span class="section-tag" style="color:var(--accent-A)">第1~40题</span>
  </div>
  <div id="B-mcq-group1"></div>
  <div class="exam-section-hdr" style="background:rgba(26,74,107,0.1);border-color:#1a4a6b;color:#6aabdf;">
    乙组 · 西餐烹调艺术及实践 <span class="section-tag" style="color:#6aabdf">第41~50题</span>
  </div>
  <div id="B-mcq-group2"></div>
  <div class="exam-section-hdr" style="background:rgba(26,90,42,0.1);border-color:#1a5a2a;color:#66cc88;">
    丙组 · 亚洲烹调艺术及实践 <span class="section-tag" style="color:#66cc88">第51~60题</span>
  </div>
  <div id="B-mcq-group3"></div>

  <button class="exam-submit-btn" id="submitB" style="display:none;background:linear-gradient(135deg,#1a4a6b,#4a7fb5);" onclick="submitPaper('B')">
    📋 交卷 · 生成成绩单
  </button>

  <div class="exam-section-hdr" style="margin-top:36px;">
    试卷二 · 作答题（40%）<span class="section-tag">甲组必答1题 ＋ 乙组选答3题</span>
  </div>
  <div style="font-size:13px;color:var(--text-dim);margin-bottom:20px;padding:12px 16px;background:rgba(0,0,0,0.2);border-radius:8px;border:1px solid var(--border);">
    💡 作答提示：请先在纸张上认真作答，再点击「查看参考答案」核对。
  </div>
  <div id="B-written"></div>

</div><!-- /panelB -->

<!-- ── FOOTER ── -->
<footer class="site-footer">
  <em>2026年马来西亚华文独中统一考试厨艺理论 · 历届全真模拟考场</em><br>
  本系统基于2020~2025年六届真实统考试题深度剖析构建，仅供备考学习参考使用。<br>
  <span style="color:var(--gold-dim);">v2026.10-Build.04</span> &nbsp;|&nbsp; UEC Culinary Theory Mock Exam System
</footer>

<script>
// ═══════════════════════════════════════════════
// EXAM DATA — PAPER A (Historical High-Frequency)
// ═══════════════════════════════════════════════
const paperA_mcq = [
  // ── BAKERY Q1-40 ──
  {id:1,g:'A',src:'2025真题',q:'在餐厅厨房负责制作糕点的餐饮从业人员，法文称为什么？',opts:{A:'Saucier',B:'Patissier',C:'Poissonnier',D:'Chef Gardenmanger'},ans:'B',exp:'Patissier 专指糕点师（Pastry Chef）。Saucier 为酱汁厨师，Poissonnier 为鱼类厨师，Gardenmanger 为冷食厨师。'},
  {id:2,g:'A',src:'2025真题',q:'依照世界卫生组织定义，正确的洗手流程一般需多长时间？',opts:{A:'5秒',B:'10秒',C:'20秒以下',D:'20秒以上'},ans:'D',exp:'WHO 建议以流动清水与肥皂搓洗至少 20 秒以上，方可有效去除手部致病菌，保障食品安全。'},
  {id:3,g:'A',src:'2025真题',q:'2017年推出的新品巧克力，天然呈粉红色、有树莓风味，称为？',opts:{A:'红宝石巧克力（Ruby）',B:'单品巧克力（Single Origin）',C:'免调温巧克力（Compound）',D:'黑牌巧克力（Couverture）'},ans:'A',exp:'红宝石巧克力（Ruby Chocolate）由嘉利宝（Callebaut）于2017年推出，天然粉红色，具树莓酸甜风味，无须添加色素。'},
  {id:4,g:'A',src:'2024真题',q:'下列哪种材料不可贮存在冷冻柜，以避免油水分离？',opts:{A:'无水奶油（Butter）',B:'坚果油',C:'鲜奶油（Cream）',D:'棕榈油'},ans:'C',exp:'鲜奶油是脂肪与水的乳化液，冷冻后解冻时乳化结构破坏，导致油水分离，无法再次打发。'},
  {id:5,g:'A',src:'2024真题',q:'烘焙百分比（Baker\'s Percentage）中，以哪种原料的重量为100%基准？',opts:{A:'总面团重量',B:'鸡蛋重量',C:'面粉重量',D:'油脂总重量'},ans:'C',exp:'烘焙百分比永远以面粉总重量为100%基准，其他原料均以占面粉重量的百分比表示。'},
  {id:6,g:'A',src:'2023真题',q:'面团可拉出均匀薄透薄膜、破口呈平滑圆弧形，此为哪个搅拌阶段？',opts:{A:'扩展阶段',B:'完全扩展阶段',C:'拾起阶段',D:'卷起阶段'},ans:'B',exp:'完全扩展阶段（Final Stage）：面团极光滑有光泽，薄膜破口平滑圆弧（无锯齿），是吐司、软式面包的最佳搅拌终点。'},
  {id:7,g:'A',src:'2023真题',q:'面团搅拌过度后，面筋断裂，面团表面发黏渗水，此现象称为？',opts:{A:'断筋（Over-mixing）',B:'水化（Hydration）',C:'老化（Staling）',D:'糊化（Gelatinization）'},ans:'A',exp:'断筋：面团在完全扩展阶段后继续高速搅拌，机械剪切力切断面筋网络，面团失去弹性、发黏渗水，产品体积大幅缩减。'},
  {id:8,g:'A',src:'2022真题',q:'新鲜酵母、活性干酵母、即发干酵母的换算比例，何者正确？',opts:{A:'新鲜:活性干:即发干 = 3:2:1',B:'新鲜:活性干:即发干 = 1:0.5:0.33',C:'新鲜:活性干:即发干 = 2:1:0.5',D:'三者相等可直接替换'},ans:'B',exp:'换算黄金比例：新鲜酵母3g ≈ 活性干酵母1.5g ≈ 即发干酵母1g。即 1:0.5:0.33。即发干效力最强。'},
  {id:9,g:'A',src:'2022真题',q:'面包体积比（Specific Volume）是指什么？',opts:{A:'面包体积 ÷ 面包重量',B:'面包重量 ÷ 面包体积',C:'面包体积 ÷ 面团重量',D:'面团重量 ÷ 面包体积'},ans:'A',exp:'体积比 = 面包体积（cm³）÷ 面包重量（g）。标准吐司约 6~7 cm³/g，越高表示组织越松软。'},
  {id:10,g:'A',src:'2022真题',q:'制作面包时盐量加倍，发酵后会产生哪种情形？',opts:{A:'产品高度变高',B:'产品高度变低',C:'产品会容易烧焦',D:'产品表面出现裂痕'},ans:'B',exp:'食盐高渗透压抑制酵母活性，盐加倍则酵母产气量大幅减少，面团发酵不足，产品高度明显偏低。'},
  {id:11,g:'A',src:'2021高频',q:'制作派皮或奶酥底，配方内应用哪种油脂最合适？',opts:{A:'沙拉油',B:'无水奶油或精制猪油',C:'玛琪琳',D:'棉籽油'},ans:'B',exp:'无水奶油或猪油固态脂肪含量高，提供最佳起酥性（Shortening Effect）与层次感。玛琪琳含水，沙拉油为液态。'},
  {id:12,g:'A',src:'2021高频',q:'以下哪项正确描述三大乳沫类蛋糕的区别？',opts:{A:'三者皆使用全蛋打发法',B:'海绵全蛋打发，戚风分蛋打发，天使纯蛋白打发',C:'戚风和天使皆不含油脂',D:'天使蛋糕含大量蛋黄'},ans:'B',exp:'海绵=全蛋+糖打发；戚风=分蛋打发+沙拉油；天使=纯蛋白+塔塔粉，不含蛋黄与任何油脂。'},
  {id:13,g:'A',src:'2021高频',q:'面糊比重（Specific Gravity）的正确定义是？',opts:{A:'比重越高，打发程度越好',B:'面糊重量 ÷ 同体积水的重量',C:'比重大于1说明充气良好',D:'海绵蛋糕标准比重约0.9~1.0'},ans:'B',exp:'比重 = 等体积面糊重量 ÷ 等体积水重量。比重越低（接近0），充气越多、打发越好。海绵蛋糕标准约 0.45~0.55。'},
  {id:14,g:'A',src:'2020真题',q:'烘焙食品要安全贮藏，应放置在怎样的地方？',opts:{A:'阴冷、潮湿',B:'阴冷、干燥',C:'高温、潮湿',D:'高温、阳光直射'},ans:'B',exp:'「阴冷干燥」：低温减缓细菌繁殖与脂肪氧化；干燥防止吸潮受潮、霉菌生长。'},
  {id:15,g:'A',src:'2020真题',q:'800g带盖吐司在200℃下，烘焙时间约需多久？',opts:{A:'15~20分钟',B:'35~40分钟',C:'55~60分钟',D:'1小时以上'},ans:'B',exp:'800g 带盖吐司在 200℃ 标准条件下需 35~40 分钟。重量越大、含糖量越高须适当延长时间并降低炉温。'},
  {id:16,g:'A',src:'2024高频',q:'烘焙产品形成金黄色泽与焦香风味，主要由于哪种反应？',opts:{A:'焦糖化反应（Caramelization）',B:'美拉德反应（Maillard Reaction）',C:'水解反应（Hydrolysis）',D:'皂化反应（Saponification）'},ans:'B',exp:'美拉德反应：还原糖与氨基酸在约110℃以上发生非酶促褐变，产生芳香化合物与褐色素——是面包烤色与焦香的主要来源。'},
  {id:17,g:'A',src:'2023真题',q:'制作马卡龙的烘焙温度应控制在约多少℃？',opts:{A:'200℃',B:'180℃',C:'160℃',D:'120℃'},ans:'C',exp:'马卡龙低温慢烤约 140~165℃，12~15 分钟。过高开裂变色，过低成品潮湿。低温烤保持外脆内软及花边（Pied）。'},
  {id:18,g:'A',src:'2022真题',q:'哪种蛋白霜最不易消泡，最适合挤花装饰？',opts:{A:'法式蛋白霜（French）',B:'瑞士蛋白霜（Swiss）',C:'意式蛋白霜（Italian）',D:'三种稳定性相同'},ans:'C',exp:'意式蛋白霜（Italian Meringue）：将118~121℃热糖浆倒入打发蛋白，热糖浆使蛋白质变性固定，形成极稳定的光泽蛋白霜。'},
  {id:19,g:'A',src:'2021真题',q:'法式道纳司（French Doughnut）使用哪种面糊制作？',opts:{A:'泡芙面糊（Pâte à Choux）',B:'千层酥皮（Puff Pastry）',C:'小西饼面团（Cookies）',D:'派皮（Pie Dough）'},ans:'A',exp:'法式道纳司使用泡芙面糊（Choux Pastry），将面糊挤圈入油锅，靠蒸汽膨胀（非酵母发酵）炸至金黄膨松。'},
  {id:20,g:'A',src:'2020高频',q:'食品用具煮沸杀菌法，正确操作条件是什么？',opts:{A:'90℃加热半分钟',B:'90℃加热1分钟',C:'100℃加热半分钟',D:'100℃加热1分钟'},ans:'D',exp:'标准煮沸杀菌法：100℃沸腾清水中持续至少1分钟，可消灭大部分非孢子型致病细菌。'},
  {id:21,g:'A',src:'2023高频',q:'下列关于海绵蛋糕出炉后收缩，哪项叙述有误？',opts:{A:'面粉筋度过高',B:'烘焙时间太短',C:'蛋打发过度或不足',D:'出炉后立刻脱模表面朝下'},ans:'D',exp:'出炉后立刻脱模表面朝下是戚风蛋糕的正确操作。海绵蛋糕收缩原因：筋度过高、时间不足、打发异常、出炉后震动。'},
  {id:22,g:'A',src:'2024高频',q:'烘烤泡芙体积膨胀不足的原因包括哪些？\nⅠ蛋温太低或不新鲜 Ⅱ加蛋时面糊超过65℃ Ⅲ油水面粉未拌合均匀',opts:{A:'Ⅰ、Ⅱ',B:'Ⅰ、Ⅲ',C:'Ⅱ、Ⅲ',D:'Ⅰ、Ⅱ、Ⅲ'},ans:'D',exp:'三项均是：①蛋温低→乳化差；②面糊过热→蛋白质过早凝固；③油水分离→面糊不稳定，三者皆导致体积不足。'},
  {id:23,g:'A',src:'2022高频',q:'先将面粉与油脂拌至蓬松，再依序加入其他原料，此搅拌方法是？',opts:{A:'糖油拌合法',B:'粉油拌合法',C:'直接拌合法',D:'二步拌合法'},ans:'B',exp:'粉油拌合法（Flour-Batter Method）：油脂裹覆面粉阻断面筋，产品细腻柔软油润，适用于高油脂磅蛋糕。'},
  {id:24,g:'A',src:'2021真题',q:'吉利丁（Gelatin）是从何种来源提取制成？',opts:{A:'海藻',B:'山药',C:'动物骨骼与皮肤胶原蛋白',D:'树脂'},ans:'C',exp:'吉利丁是动物骨骼、皮肤、结缔组织中的胶原蛋白水解而成。海藻→琼脂；植物→果胶。冷水泡软后加热至60℃融化使用。'},
  {id:25,g:'A',src:'2020高频',q:'以下哪种烘焙产品不需使用酵母？',opts:{A:'法国面包（Baguette）',B:'美式甜面包（Soft Roll）',C:'马卡龙（Macaron）',D:'丹麦面包（Danish）'},ans:'C',exp:'马卡龙由蛋白霜+杏仁粉+糖粉组成，靠打发蛋白霜气泡膨胀，完全不使用酵母。其他三种均为发酵面团产品。'},
  {id:26,g:'A',src:'2023真题',q:'下列何者为化学膨大剂？',opts:{A:'酵母（Yeast）',B:'吉利丁（Gelatin）',C:'塔塔粉（Cream of Tartar）',D:'泡打粉（Baking Powder）'},ans:'D',exp:'泡打粉由碳酸氢钠＋酸性盐＋淀粉组成，遇水或加热产生CO₂，不依赖微生物。塔塔粉为酸性调节剂；酵母为生物膨大剂。'},
  {id:27,g:'A',src:'2024高频',q:'小麦麸皮与胚芽中的矿物质成分（镁、钾、磷、铁等）称为？',opts:{A:'灰分（Ash Content）',B:'脂肪',C:'葡萄糖',D:'胡萝卜素'},ans:'A',exp:'灰分是面粉高温灼烧后残留矿物质，来自麸皮与胚芽。灰分越高→精白度越低，全麦粉灰分高，高精白粉灰分约0.3~0.5%。'},
  {id:28,g:'A',src:'2022高频',q:'油炸用油的发烟点（Smoke Point）应达多少以上？',opts:{A:'150~160℃',B:'160~170℃',C:'170~180℃',D:'200℃以上'},ans:'D',exp:'油炸操作温度约170~190℃，发烟点须高于200℃以避免油脂在操作温度下分解产生有害醛类物质。'},
  {id:29,g:'A',src:'2023高频',q:'下列关于烤炉烤面包，哪项不正确？',opts:{A:'瓦斯炉炉温上升较慢',B:'蒸汽炉烤硬式面包表皮较脆薄',C:'隧道炉可连续生产产量较大',D:'热风炉烤吐司颜色较均匀'},ans:'A',exp:'瓦斯炉加热速度实际取决于设备型号与火力，不一定较慢。蒸汽炉（B）确能形成薄脆外壳；隧道炉（C）与热风炉（D）叙述均正确。'},
  {id:30,g:'A',src:'2020真题',q:'比萨（Pizza）的意大利发面饼，属于哪项产品分类？',opts:{A:'面包类',B:'饼干类',C:'中点类',D:'西点类'},ans:'A',exp:'比萨饼底使用酵母发酵面团制作，属「面包类」产品分类。那不勒斯传统比萨使用高水分面团，讲究弹性与延展性。'},
  {id:31,g:'A',src:'2022高频',q:'制作苹果派馅，通常用哪种胶冻原料增稠？',opts:{A:'玉米淀粉',B:'吉利丁',C:'洋菜粉（琼脂）',D:'甘薯粉'},ans:'A',exp:'玉米淀粉在95℃加热迅速糊化，冷却后透明有光泽，质地滑顺不凝固成固体，适合派馅。吉利丁室温可能融化，琼脂口感硬脆。'},
  {id:32,g:'A',src:'2021高频',q:'小麦面粉中两种主要蛋白质，形成面筋网络（Gluten）的是？',opts:{A:'白蛋白与球蛋白',B:'麦谷蛋白（Glutenin）与醇溶谷蛋白（Gliadin）',C:'胶原蛋白与弹性蛋白',D:'酪蛋白与乳清蛋白'},ans:'B',exp:'麦谷蛋白（Glutenin）提供弹性；醇溶谷蛋白（Gliadin）提供延展性。两者加水搅拌形成立体面筋网络。'},
  {id:33,g:'A',src:'2024高频',q:'马卡龙面糊挤出后需静置结皮才烤，其目的是？',opts:{A:'防止面糊流散变形',B:'表面干燥，烘烤时蒸汽从底部冲出形成花边（Pied）',C:'增加面糊含糖量',D:'使酵母在室温发酵'},ans:'B',exp:'静置结皮（Resting）：表面形成薄外壳，烘烤时内部蒸汽无法从顶部逸出，转而从底部边缘冲出，形成马卡龙标志性花边。'},
  {id:34,g:'A',src:'2022真题',q:'以下哪一烘焙原料组合是错误的？',opts:{A:'蛋白霜＋甜点醋 = 舒芙蕾',B:'面包面团＋起酥油 = 可颂',C:'焦糖＋全蛋 = 焦糖布丁',D:'面糊类＋乳沫类 = 戚风蛋糕'},ans:'A',exp:'舒芙蕾搭配的是卡士达酱（Crème Pâtissière）或巧克力糊，并非甜点醋。醋仅是蛋白霜打发时的辅助稳定剂，不是主配对。'},
  {id:35,g:'A',src:'2021高频',q:'派皮从模型中取出时容易破碎，最主要原因是？',opts:{A:'取出时过热',B:'配方中油脂含量太少',C:'松弛时间不足',D:'烘焙不足'},ans:'B',exp:'油脂润滑作用减少面筋形成，使派皮有适当酥脆感。油脂过少→面筋过强→派皮太脆，受力即破碎。'},
  {id:36,g:'A',src:'2023真题',q:'派馅中牛奶布丁质地太坚韧，最可能的原因是？',opts:{A:'浓皮太厚',B:'烘焙时间太长',C:'馅料温度太低',D:'胶凝程度不够'},ans:'B',exp:'烘焙时间过长→蛋白质过度变性凝固→质地橡皮状坚韧。标准应烤至中心微晃（果冻感）即出炉，余热完成凝固。'},
  {id:37,g:'A',src:'2020高频',q:'以下哪种水果含天然果胶，具有胶凝特性？',opts:{A:'黄梨（菠萝）',B:'香蕉',C:'西瓜',D:'奇异果'},ans:'A',exp:'黄梨（菠萝）含天然果胶（Pectin），加热加糖可产生胶凝效果。注意：新鲜菠萝含蛋白酶（Bromelain）会分解吉利丁，需先煮熟灭酶再用。'},
  {id:38,g:'A',src:'2022高频',q:'打发蛋白霜时，以下哪种材料不能替代塔塔粉（Cream of Tartar）？',opts:{A:'盐',B:'白醋',C:'发粉（Baking Powder）',D:'柠檬汁'},ans:'C',exp:'发粉含碳酸氢钠（碱性），会提高蛋白pH值，破坏泡沫结构。白醋、柠檬汁（酸性）、少量盐均可稳定蛋白泡沫。'},
  {id:39,g:'A',src:'2025高频',q:'蛋糕包装时，为延长保存时间，常放置什么材料？',opts:{A:'抗氧化剂',B:'防腐剂',C:'干燥剂',D:'防腐剂与干燥剂'},ans:'C',exp:'干燥剂（硅胶）吸收包装内多余水分，维持干燥环境，防止霉菌生长与淀粉老化（Staling）。'},
  {id:40,g:'A',src:'2024真题',q:'奶粉重量2.2磅（lbs），相当于多少公制重量？',opts:{A:'半公斤',B:'1公斤',C:'1.5公斤',D:'4.4公斤'},ans:'B',exp:'1磅≈453.6g，2.2磅≈997.9g≈1公斤。记忆口诀：1公斤≈2.2磅，因此2.2磅倒推约等于1公斤。'},

  // ── WESTERN CUISINE Q41-50 ──
  {id:41,g:'B',src:'2024真题',q:'法式五大母酱中，由「白色高汤＋白色面糊（White Roux）」制成的是？',opts:{A:'荷兰酱（Hollandaise）',B:'白酱（Béchamel）',C:'褐酱（Espagnole）',D:'金黄酱（Velouté）'},ans:'D',exp:'Velouté = White Stock＋White/Blonde Roux；Béchamel = Milk＋White Roux；Espagnole = Brown Stock＋Brown Roux；Hollandaise = 澄清黄油＋蛋黄。'},
  {id:42,g:'B',src:'2024真题',q:'荷兰酱（Hollandaise Sauce）的主要油脂应使用什么？',opts:{A:'普通黄油（Whole Butter）',B:'玛琪琳',C:'澄清黄油（Clarified Butter）',D:'沙拉油'},ans:'C',exp:'澄清黄油（Clarified Butter）去除水分与蛋白质，纯净脂肪乳化效果最稳定，发烟点更高，是荷兰酱的专用油脂。'},
  {id:43,g:'B',src:'2025真题',q:'法式料理中，「Roux（面糊）」最主要的功能是什么？',opts:{A:'增加食物味道',B:'增加食物颜色',C:'增加食物营养',D:'增加食物浓稠度'},ans:'D',exp:'Roux = 等量黄油＋面粉加热翻炒，主要功能是增稠（Thickening）——淀粉糊化使酱汁形成浓稠顺滑质地。'},
  {id:44,g:'B',src:'2023真题',q:'法式洋葱汤呈现深棕色，洋葱在烹调时经历的专业术语是？',opts:{A:'酶促褐变',B:'焦糖化反应（Caramelization）',C:'美拉德反应',D:'氧化反应'},ans:'B',exp:'洋葱在150~180℃低温长时间翻炒，天然糖分发生焦糖化反应（Caramelize Onions），产生深棕色素与甜香，需约30~45分钟以上。'},
  {id:45,g:'B',src:'2024真题',q:'水波煮（Poaching）的烹调温度约为摄氏几度？',opts:{A:'100℃',B:'85~95℃',C:'65~80℃',D:'50℃以下'},ans:'C',exp:'水波煮约65~80℃微沸（可见细小气泡，液体不翻滚），适合娇嫩食材（水波蛋、鱼片、家禽胸肉），防止破碎保持嫩度。'},
  {id:46,g:'B',src:'2025真题',q:'西餐术语「al dente」指的是什么？',opts:{A:'放工时间',B:'准备工作',C:'饭的粘稠度',D:'面食的嚼劲度'},ans:'D',exp:'al dente 是意大利文「to the tooth」，形容意大利面食外层软熟、内心略带嚼劲的最佳熟度状态，是专业西餐面食的黄金标准。'},
  {id:47,g:'B',src:'2023真题',q:'储存高汤或酱料，以下哪些原则正确？\nⅠ FIFO先进先出 Ⅱ 必须标上贮藏日期 Ⅲ 贮藏前必须搅拌 Ⅳ 重新加热',opts:{A:'Ⅰ、Ⅱ',B:'Ⅰ、Ⅱ、Ⅲ',C:'Ⅱ、Ⅲ、Ⅳ',D:'Ⅰ、Ⅱ、Ⅲ、Ⅳ'},ans:'A',exp:'正确原则：FIFO先进先出＋标注日期。贮藏前搅拌可能引入污染；重新加热须在使用时进行，不适合纯贮藏操作。'},
  {id:48,g:'B',src:'2022真题',q:'Palette knife 的别称是什么？',opts:{A:'Chef knife（主厨刀）',B:'Metal spatula（金属抹刀）',C:'Butcher knife（屠宰刀）',D:'Filleting knife（去骨刀）'},ans:'B',exp:'Palette knife 刀刃宽平柔软，无切割功能，专用于涂抹蛋糕奶油、铺平酱料，学名别称为 Metal spatula。'},
  {id:49,g:'B',src:'2025真题',q:'将食物切成不规则形状的极细末，西餐中称为什么？',opts:{A:'Mince（碎末）',B:'Chop（粗切）',C:'Dice（方丁）',D:'Shred（细丝）'},ans:'A',exp:'Mince = 极细小不规则碎末（约1~2mm），常用于蒜末、洋葱末、香草末。Chop为粗切；Dice为标准方形；Shred为细丝。'},
  {id:50,g:'B',src:'2022真题',q:'欲使食材表面焗烤（Gratin）上色，应使用哪个厨具？',opts:{A:'煎炉（Grill）',B:'烤箱（Oven）',C:'炉灶（Stove Top）',D:'萨拉曼德烤炉（Salamander）'},ans:'D',exp:'Salamander 是顶部加热的专业开放式烤炉，热源从上方直接辐射，极短时间使表面上色，常用于焗烤芝士、法式洋葱汤表面。'},

  // ── ASIAN CUISINE Q51-60 ──
  {id:51,g:'C',src:'2024真题',q:'下列刀工尺寸关系，何者正确？',opts:{A:'丝 比 条 粗',B:'丁 比 粒 大',C:'条 比 丝 细',D:'粒 比 丁 小'},ans:'D',exp:'正确关系：丝（细）< 条（粗）；粒（小）< 丁（大）。所以「粒比丁小」正确。常考陷阱：选项B「丁比粒大」也正确，但D的表述更精确。'},
  {id:52,g:'C',src:'2022真题',q:'制作「炖」的菜肴，应使用什么火候？',opts:{A:'大火',B:'文火（小火）',C:'武火',D:'旺火'},ans:'B',exp:'炖以文火（80~95℃）长时间缓慢加热，使胶原蛋白充分溶出，汤汁醇厚，肉质软烂入味。旺火/大火不适合长时间炖制。'},
  {id:53,g:'C',src:'2025真题',q:'铁氟龙（Teflon）不粘锅，应搭配哪种器具以免损伤涂层？',opts:{A:'铁铲',B:'木制铲',C:'不锈钢铲',D:'不锈铜炒瓢'},ans:'B',exp:'铁氟龙（PTFE）涂层极脆弱，金属器具会划破涂层。应用木制铲或硅胶铲——柔软无金属，保护涂层完整性。'},
  {id:54,g:'C',src:'2023真题',q:'下列干货库房管理原则，哪项正确？',opts:{A:'尽可能日光直射以维持干燥',B:'最适宜温度20~25℃',C:'相对湿度控制在30~50%',D:'食物以先进后出为原则'},ans:'C',exp:'干货库房：温度10~21℃；湿度30~60%（C正确）；避免日光直射；应遵循FIFO先进先出（D错误：先进后出是错的）。'},
  {id:55,g:'C',src:'2022真题',q:'勾芡要达到「明油亮芡」的效果，应如何操作？',opts:{A:'用面粉来勾芡',B:'芡粉中添加小苏打',C:'用炒瓢不停地搅拌',D:'勾芡时用炒瓢往同一方向推拌'},ans:'D',exp:'明油亮芡关键：水淀粉沿锅边缓缓淋入，同一固定方向均匀推拌，使淀粉均匀糊化包裹食材。乱搅会破坏芡汁稳定性。'},
  {id:56,g:'C',src:'2023真题',q:'擅长烹煮海鲜、口味极清淡、强调原料本味的，是哪个地区特色菜？',opts:{A:'江苏菜',B:'浙江菜',C:'福建菜',D:'东北菜'},ans:'B',exp:'浙菜以「清鲜秀美、注重本味」著称，尤善水产海鲜。代表菜：西湖醋鱼、龙井虾仁。江苏偏甜；福建擅长糟味；东北偏重口。'},
  {id:57,g:'C',src:'2024真题',q:'下列哪种细菌性食物中毒最容易发生于禽肉类？',opts:{A:'肉毒杆菌',B:'肠炎弧菌',C:'沙门氏杆菌（Salmonella）',D:'金黄色葡萄球菌'},ans:'C',exp:'沙门氏杆菌（Salmonella）常见于禽类肠道，屠宰时可能污染肉品。症状：发烧、腹泻、呕吐。肠炎弧菌来自海鲜；金黄色葡萄球菌来自手部伤口。'},
  {id:58,g:'C',src:'2022真题',q:'水拔拔丝的正确四个阶段顺序是？',opts:{A:'熔化→稀薄→浓稠→出丝',B:'熔化→浓稠→出丝→稀薄',C:'熔化→浓稠→稀薄→出丝',D:'浓稠→熔化→稀薄→出丝'},ans:'A',exp:'水拔拔丝：①熔化（糖晶体融化）→②稀薄（水分多，流动性强）→③浓稠（水分蒸发，约145~155℃）→④出丝（约155~165℃，可拉出细糖丝）。'},
  {id:59,g:'C',src:'2025真题',q:'糖醋排骨中，芡汁浓度的作用不包含哪一项？',opts:{A:'让食物更亮丽',B:'让食物更酥脆',C:'让调味料沾在食物表面',D:'让芡汁水分暂时不渗进排骨'},ans:'B',exp:'芡汁功能：①增亮美化；②调味附着；③隔水保温。「使食物更酥脆」不是芡汁功能——芡汁含水分，反而会软化炸物外壳。'},
  {id:60,g:'C',src:'2023真题',q:'刀与食材呈40度角切割，食材受热后卷曲成花状，是哪种花刀？',opts:{A:'麦穗花刀',B:'松球花刀',C:'菊花花刀',D:'鱼鳃花刀'},ans:'D',exp:'鱼鳃花刀：刀与食材成40°角斜切，每刀切入约2/3深度，热处理后食材沿切口翻卷展开如鱼鳃，常用于鱿鱼、腰花。'},
];

// ═══════════════════════════════════════════════
// EXAM DATA — PAPER B (2026 Prediction Questions)
// ═══════════════════════════════════════════════
const paperB_mcq = [
  // ── BAKERY Q1-40 (均衡版) ──
  {id:1,g:'A',src:'2026预测',q:'天然酸种酵母（Sourdough Starter）的主要膨胀原理是？',opts:{A:'商业酵母快速产生二氧化碳气体膨胀',B:'化学泡打粉遇水受热释放二氧化碳',C:'野生酵母与乳酸菌共生发酵产酸产气',D:'面团内部水分受热气化形成高压蒸汽'},ans:'C',exp:'天然酸种酵母（Sourdough）靠野生酵母菌（Saccharomyces）与乳酸菌（Lactobacillus）共生发酵：酵母产CO₂使面包膨胀，乳酸菌产乳酸与醋酸赋予独特酸味与复杂风味。'},
  {id:2,g:'A',src:'2026预测',q:'低温慢煮（Sous-Vide）在烘焙与甜品领域的主要应用是？',opts:{A:'快速高温烘烤欧包形成焦脆厚硬外壳',B:'真空密封后以恒温水浴精准熟化内馅',C:'急速冷冻面团以抑制酵母细胞的活性',D:'利用高压蒸汽喷射使面糊瞬间受热膨胀'},ans:'B',exp:'Sous-Vide（真空低温慢煮）：食材真空封袋后浸于精确控温水浴（如63℃/2小时），保留水分与营养，质地精准一致。常用于甜品中的布丁、乳酪蛋糕、卡士达酱的无人为温度误差制作。'},
  {id:3,g:'A',src:'2026预测',q:'对流蒸汽烤炉（Combi Oven）与普通热风炉的最主要区别是？',opts:{A:'仅能使用单一微波辐射进行快速加热',B:'依靠纯导热铁板自下而上单向传递热量',C:'炉腔内保持绝对干燥状态无法注入水分',D:'结合热风与蒸汽可精准调控温度与湿度'},ans:'D',exp:'万能蒸烤炉（Combi Oven）结合干热（热风）与湿热（蒸汽）两种加热模式，可单独或同时使用，精准控制温度（30~300℃）与湿度（0~100%），适用范围极广：面包、糕点、肉类、蔬菜等均可处理。'},
  {id:4,g:'A',src:'2026预测',q:'「折叠面团（Laminated Dough）」中裹入油脂后的折叠层数，决定了产品的哪个特性？',opts:{A:'烘烤成品的酥脆层次质感与膨胀高度',B:'酵母在面团内部进行无氧发酵的速率',C:'面团在常温搅拌过程中的最终含水量',D:'焦糖化反应在表皮所呈现的深浅色泽'},ans:'A',exp:'折叠面团（如可颂、丹麦酥）通过多次折叠裹入黄油（每折叠三次产生3倍层数），烘烤时黄油层间水分汽化产生蒸汽，将面团层层撑开，产生数十至数百层的酥脆分层效果。'},
  {id:5,g:'A',src:'2026预测',q:'糖（Sugar）在面包发酵过程中的主要功能是？',opts:{A:'完全作为结构支撑原料以增加面筋韧性',B:'降低面团黏度并防止油脂在发酵中氧化',C:'提供酵母发酵碳源并促进烘烤褐变着色',D:'抑制杂菌繁殖且彻底阻断淀粉的水化过程'},ans:'C',exp:'糖在面包中的多重功能：①酵母食物（Carbon Source）——提供可发酵糖促进CO₂产生；②上色（Maillard与焦糖化反应）；③保湿（吸湿性延长保鲜）；④甜味与香气；⑤高浓度时（>5%）则抑制酵母（渗透压）。'},
  {id:6,g:'A',src:'2026预测',q:'以下关于奶油（Butter）在饼干（Cookies）中的功能，哪项错误？',opts:{A:'阻断面筋网络形成赋予饼干酥脆口感',B:'充当主要膨大剂促使饼干体积剧烈膨胀',C:'烘烤时散发浓郁奶香并增进成品的风味',D:'打发充入空气使面团具有良好的延展性'},ans:'B',exp:'奶油在饼干中：①风味香气；②起酥性（阻断面筋）；③增脆（固态脂肪片状晶体）；④延展性（打发时充入空气使饼干稍有蓬松感）。使饼干体积「大幅膨胀」是化学膨大剂或蛋白打发的功能，不是奶油的主要作用。'},
  {id:7,g:'A',src:'2026预测',q:'黑麦（Rye）面包与小麦面包最主要的面筋差异是？',opts:{A:'缺乏醇溶谷蛋白无法形成连续网状面筋',B:'含有极高活性面筋蛋白导致弹性特别强',C:'面筋完全无法吸收水分形成均质的面团',D:'加热后蛋白质迅速溶解失去保气支撑力'},ans:'A',exp:'黑麦（Rye）含有戊聚糖（Pentosans）而非典型面筋蛋白，无法形成小麦面粉那样的连续弹性面筋网络。黑麦面团依靠戊聚糖的持水性维持结构，质地致密黏稠，面包组织孔洞粗大，需酸种（Sourdough）帮助其稳定结构。'},
  {id:8,g:'A',src:'2026预测',q:'制作可颂（Croissant）时，裹入黄油的理想温度范围是？',opts:{A:'0℃～4℃（刚出冷藏库质地坚硬）',B:'8℃～10℃（略带微凉且韧性较足）',C:'26℃～28℃（室温偏软极易渗出）',D:'16℃～18℃（可塑性适中与面相近）'},ans:'D',exp:'裹入黄油须与面团温度相近（约16~18℃），两者可塑性相当，折叠时黄油不会因太硬而碎裂刺穿面层，也不因太软融化失去层次。过硬→折裂；过软→融合→层次消失。'},
  {id:9,g:'A',src:'2026预测',q:'食品安全危险温度带（Danger Zone）的正确温度范围是？',opts:{A:'0℃～30℃之间',B:'5℃～60℃之间',C:'10℃～70℃之间',D:'15℃～50℃之间'},ans:'B',exp:'危险温度带（Danger Zone）：5~60℃——此温度范围内大多数致病细菌繁殖最为活跃（理想繁殖温度约35~37℃）。食品不应在此温度带停留超过2小时（高风险食品不超过1小时）。'},
  {id:10,g:'A',src:'2026预测',q:'天使蛋糕（Angel Food Cake）中必须加入塔塔粉的原因是？',opts:{A:'降低酸碱度以稳定蛋白泡沫并保持纯白',B:'充当化学膨大剂受热释放大量二氧化碳',C:'代替部分低筋面粉提供坚固的支撑骨架',D:'分解多余油脂以防止面糊产生消泡离析'},ans:'A',exp:'塔塔粉（酒石酸氢钾，酸性）加入蛋白中的作用：①降低pH值→蛋白质等电点接近→打发更稳定；②中和蛋黄中残余碱性色素→天使蛋糕保持洁白；③增强泡沫网络结构防止塌陷。'},
  {id:11,g:'A',src:'2026预测',q:'巧克力调温（Tempering）的目的是什么？',opts:{A:'彻底蒸发可可豆残余水分以防止发霉',B:'促使糖粉完全溶解以提高成品的甜度',C:'诱导可可脂形成稳定的第五型晶体结构',D:'破坏可可脂结晶使巧克力保持常温液态'},ans:'C',exp:'巧克力调温（Tempering）：通过精确控温（融化→降温→升温）步骤，引导可可脂形成稳定的β-5晶型（熔点约34℃），使成品巧克力：①表面光亮；②折断声脆（snap）；③不起白霜（Bloom）；④脱模容易。'},
  {id:12,g:'A',src:'2026预测',q:'酵母发酵面团中「基本发酵」与「最终发酵」的主要区别是？',opts:{A:'基本发酵需高温高湿，最终发酵需低温干燥',B:'基本发酵完全不产气，最终发酵才开始膨胀',C:'基本发酵由细菌主导，最终发酵由酵母完成',D:'基本发酵在分割前进行，最终发酵在整型后'},ans:'D',exp:'面包发酵流程：搅拌→基本发酵（Bulk Fermentation，面团整体发酵）→分割滚圆→中间发酵→整型→最终发酵（Final Proof，整型后入炉前发酵）→烘烤。两个发酵阶段目的不同：基本发酵建立风味，最终发酵决定体积。'},
  {id:13,g:'A',src:'2026预测',q:'「自解（Autolyse）」在面包制作中的意义是？',opts:{A:'仅混合粉水静置促使淀粉水化与面筋自然形成',B:'将面粉在干锅中翻炒至金黄微焦以激发麦香',C:'加入大量商业干酵母置于温室快速催生酒香',D:'成品出炉后倒扣在铁网架上利用余温慢慢自熟'},ans:'A',exp:'自解（Autolyse）：面粉与水混合（不加盐、酵母）静置20~60分钟，让面粉充分吸水：①面筋自然排列延展→减少机械搅拌时间；②改善面团延展性；③面包孔洞更大更均匀，是开放孔洞酸种面包的关键技法。'},
  {id:14,g:'A',src:'2026预测',q:'以下关于蛋清（Egg White）的打发，哪项正确？',opts:{A:'容器内残留少量油脂完全不影响打发效率',B:'必须先将生蛋白加热至沸腾方可形成泡沫',C:'铜质器皿释放的铜离子能显著稳定蛋白霜',D:'混入少许富含卵磷脂的蛋黄利于起泡膨胀'},ans:'C',exp:'铜碗打发蛋清：铜离子（Cu²⁺）与蛋清中的卵铁传递蛋白结合，形成更稳定的蛋白质—铜络合物，使泡沫更细腻、稳定、不易消泡，是传统法式甜点的秘诀。油脂和蛋黄（含油脂）会破坏蛋清起泡性。'},
  {id:15,g:'A',src:'2026预测',q:'「直接法（Straight Dough Method）」与「中种法（Sponge and Dough Method）」的主要区别是？',opts:{A:'直接法需添加酸种酵头，中种法仅用化学膨松剂',B:'直接法材料一次性拌匀，中种法分两次发酵搅拌',C:'直接法需经历三天冷藏，中种法可在半小时出炉',D:'直接法成品柔软抗老化，中种法组织紧密易掉渣'},ans:'B',exp:'直接法（Straight Dough）：一次将所有原料（面粉、水、酵母、盐、糖、油）混合搅拌，适合快速生产。中种法（Sponge & Dough）：先将部分面粉+水+酵母制成中种发酵3~4小时，再加入剩余材料搅拌，面包风味更丰富、保存期更长。'},
  {id:16,g:'A',src:'2026预测',q:'「水合（Hydration）」在面包配方中指的是什么？',opts:{A:'面团从搅拌完成到烘烤出炉的蒸发水分比例',B:'出炉面包表皮与面包心之间的相对水分梯度',C:'面团吸收空气中环境相对湿度的最大饱和度',D:'配方中总加水量占面粉总重量的烘焙百分比'},ans:'D',exp:'水合率（Hydration）= 水重量 ÷ 面粉重量 × 100%。低水合（50~60%）→面团较硬，适合造型饼干；标准（60~70%）→吐司、甜面包；高水合（70~80%+）→开放孔洞酸种面包（Ciabatta、Sourdough）。'},
  {id:17,g:'A',src:'2026预测',q:'卡士达酱（Crème Pâtissière）的主要蛋黄成分作用是？',opts:{A:'提供天然卵磷脂乳化增稠并在受热变性后定型',B:'完全分解面粉中的直链淀粉以保持透明质感',C:'使酱料质地呈透明胶状并大幅度降低热量值',D:'充当天然化学膨大剂在冷藏时释放微小气泡'},ans:'A',exp:'蛋黄在卡士达酱中的双重功能：①卵磷脂（Lecithin）作为乳化剂，稳定水油相界面；②蛋黄蛋白质在约75~80℃加热时变性凝固，与淀粉共同提供卡士达酱特有的柔嫩浓稠结构与金黄色泽。'},
  {id:18,g:'A',src:'2026预测',q:'下列哪种蛋糕属于「油脂蛋糕类（Shortened Cake）」？',opts:{A:'天使蛋糕（Angel Food Cake）',B:'重奶油磅蛋糕（Pound Cake）',C:'日式轻乳酪（Soufflé Cheese）',D:'分蛋戚风蛋糕（Chiffon Cake）'},ans:'B',exp:'油脂蛋糕类（Shortened Cake）：配方中油脂占主导（固态黄油/猪油），依靠糖油打发充入空气，代表：磅蛋糕（Pound Cake）、奶油蛋糕（Butter Cake）。乳沫类蛋糕（Foam Cake）：天使、海绵、戚风——依靠蛋白打发气泡膨胀。'},
  {id:19,g:'A',src:'2026预测',q:'吐司面包的「拉丝」口感，主要来自面团的哪个特性？',opts:{A:'配方中添加了过量未融化的固态起酥油脂',B:'内部淀粉在烘烤中未充分糊化保留生粉性',C:'充分扩展的面筋薄膜网络经定向延展定向排列',D:'由于多次冷冻复温导致的蛋白质水分子脱离'},ans:'C',exp:'吐司拉丝感来自：完全扩展阶段形成的充分面筋网络（Gluten Network）——连续薄膜状面筋在烘烤时被CO₂气泡撑开，形成细腻拉丝状内部组织。同时，糖与蛋提供的柔软湿润感也是关键因素。'},
  {id:20,g:'A',src:'2026预测',q:'开心果粉（Pistachio）在现代西式糕点中的主要应用是？',opts:{A:'替代面粉中的强力面筋以支撑戚风蛋糕骨架',B:'充当天然酸味中和剂以稳定新鲜水果的酸度',C:'在甘纳许中作为强效吸油剂防止可可脂析出',D:'赋予马卡龙或内馅独特的天然绿色与醇厚坚果香'},ans:'D',exp:'开心果粉是现代精品糕点的高级食材，可替代杏仁粉（Almond Meal）制作马卡龙、达克瓦兹等，提供天然翠绿色泽（无需色素）与独特浓郁坚果甜香，是2026年高档糕点的流行元素。'},
  {id:21,g:'A',src:'2026预测',q:'「冻干草莓粉（Freeze-Dried Strawberry Powder）」与普通果粉的最大优势是？',opts:{A:'低温升华脱水完整保留天然果香、色泽与热敏营养',B:'含有极高比例的自由水分能直接替代配方中的鲜奶',C:'经过高温瞬间焦糖化后具备天然的焦糖烘烤香气',D:'在面团中能产生类似酵母的持续发酵产气膨胀功能'},ans:'A',exp:'冻干（Freeze-Drying / 升华干燥）在低温真空条件下将水分升华去除，避免高温破坏水溶性营养素（维生素C）、天然色素（花青素）和挥发性香气成分，是保留最完整果粉品质的先进技术。'},
  {id:22,g:'A',src:'2026预测',q:'制作千层酥（Puff Pastry / Feuilletage）时，层次的形成原理是？',opts:{A:'配方中添加了高比例的双重反应型化学泡打粉',B:'黄油层间水分受热急剧汽化产生高压蒸汽顶开面层',C:'耐高糖活性干酵母在高温下进行超高速爆裂产气',D:'面粉中高筋蛋白在遇热收缩时产生强烈反弹推力'},ans:'B',exp:'千层酥（Puff Pastry）属「物理膨胀」：无酵母、无化学膨大剂，纯靠多次折叠（通常6次三折=3⁶=729层理论层数）裹入黄油层，烘烤时黄油层间水分（约14%）急速汽化膨胀，将酥皮层层撑起。'},
  {id:23,g:'A',src:'2026预测',q:'「甘纳许（Ganache）」的基本配方组合是？',opts:{A:'无盐黄油搭配高细度白砂糖粉',B:'打发蛋白霜混合无糖纯可可粉',C:'煮沸液体鲜奶油与优质纯巧克力',D:'脱脂纯牛奶与高熔点氢化植物油'},ans:'C',exp:'甘纳许（Ganache）= 热鲜奶油 ＋ 切碎巧克力。鲜奶油的热量融化巧克力并与可可脂乳化，形成细腻顺滑的乳化甘纳许。比例决定用途：1:1（软甘纳许/淋面）；1:2（较硬/球状松露）；2:1（较软/镜面光泽用）。'},
  {id:24,g:'A',src:'2026预测',q:'「冰淇淋（Ice Cream）」中加入乳化剂（卵磷脂/卵黄）与稳定剂的主要目的是？',opts:{A:'大幅提高成品的甜度以降低糖的用量',B:'彻底杀灭原料乳中可能存留的嗜冷细菌',C:'在冷冻过程中加速冰晶的快速聚集粗化',D:'结合游离水抑制粗大冰晶生成并延缓融化'},ans:'D',exp:'冰淇淋中乳化剂（Emulsifier）与稳定剂（Stabilizer）的功能：①乳化——使脂肪球稳定均匀分布；②稳定——减少冰晶重结晶（大冰晶使口感粗糙）；③保形——减缓融化；④改善搅拌（Overrun）效果，使成品体积蓬松。'},
  {id:25,g:'A',src:'2026预测',q:'Couscous（古斯米）源自于哪个地区的食物？',opts:{A:'北非地区，以硬质杜兰小麦粗粒粉加水搓粒蒸制',B:'意大利北部，以软质低筋白面粉加鲜蛋揉捏成团',C:'东南亚地区，以长粒籼米蒸熟后经日光自然晒干',D:'南美洲山区，以去皮印第安马铃薯经捣泥烘干制成'},ans:'A',exp:'Couscous（古斯米）源自北非（摩洛哥、阿尔及利亚、突尼斯），由硬质小麦粗粉（Semolina）滚粒蒸制而成，是北非传统主食与宴席主角，搭配炖肉蔬菜塔吉锅（Tagine）享用。'},
  {id:26,g:'A',src:'2026预测',q:'「松露巧克力（Chocolate Truffle）」的名称来源是？',opts:{A:'制作配方中必须浸泡昂贵的法国黑松露菌切片',B:'外形凹凸且滚满可可粉酷似出土的新鲜黑松露',C:'最早由盛产名贵菌类的法国南部松露猎人发明',D:'入口带有浓烈的天然林地泥土气味与菌菇芳香'},ans:'B',exp:'松露巧克力（Chocolate Truffle）名字来自其外形：圆形甘纳许球裹覆可可粉后，外观酷似珍贵的黑松露菌（Black Truffle）——凹凸不平的深褐色球状。传统配方为甘纳许内芯＋可可粉外衣。'},
  {id:27,g:'A',src:'2026预测',q:'「Mille-feuille（拿破仑千层派）」的法文字面意思是？',opts:{A:'拿破仑皇帝在战地常备的特制口粮',B:'蕴含着一千种馥郁风味的经典甜品',C:'由如同层叠千片轻盈树叶构成的酥皮',D:'经过一千次手工反复捶打折叠的面团'},ans:'C',exp:'Mille-feuille = Mille（一千）＋ Feuille（叶子/片）= 一千片叶子，形容千层酥皮无数薄层叠叠的外观。经典版本：三层酥皮＋两层卡士达酱，表面撒糖粉或做镜面糖浆装饰。'},
  {id:28,g:'A',src:'2026预测',q:'下列关于可可豆（Cacao/Cocoa）处理步骤，正确顺序是？',opts:{A:'烘焙→发酵→干燥→研磨→去壳',B:'研磨→去壳→发酵→烘焙→干燥',C:'去壳→干燥→研磨→发酵→烘焙',D:'发酵→干燥→烘焙→去壳→研磨'},ans:'D',exp:'可可豆完整处理流程：①采摘→②发酵（5~7天，发展风味前体物质）→③干燥→④烘焙（Roasting，150~170℃发展巧克力风味）→⑤去壳（Winnowing）→⑥研磨（Grinding成可可液块）→⑦精炼（Conching）→⑧调温→⑨成型。'},
  {id:29,g:'A',src:'2026预测',q:'制作布丁（Pudding）时，蒸烤法（Bain-Marie / Water Bath）的目的是？',opts:{A:'利用水温恒定温和传热防止蛋液过热沸腾产生蜂窝孔洞',B:'使烤箱内部充满水蒸气以大幅度加速模具内蛋液凝固',C:'稀释模具内部糖液浓度以防止布丁底部焦糖过快焦黑',D:'促使布丁表面迅速结皮形成类似法式脆皮的厚硬外壳'},ans:'A',exp:'水浴法（Bain-Marie）：布丁模型放入热水中烘烤，水的最高温度为100℃（沸点），可缓冲并控制布丁受热温度，防止超过80℃以上蛋白质过度变性产生「橡皮感」与「气泡孔洞」，确保成品细腻嫩滑。'},
  {id:30,g:'A',src:'2026预测',q:'「帕夫洛娃蛋糕（Pavlova）」的特点是？',opts:{A:'底层为坚硬黄油挞皮，中间填入浓稠酸甜柠檬乳酪酱',B:'外壳酥脆内部如棉花糖般轻柔的蛋白霜顶覆新鲜水果',C:'层层相间的多层巧克力海绵蛋糕刷满樱桃利口酒糖浆',D:'以大量焦化黄油与未打发蛋白烤制的金黄色长条小点'},ans:'B',exp:'帕夫洛娃（Pavlova）：以大量蛋白霜（法式/瑞士式）烘烤而成，外壳轻盈酥脆，内部因含少量玉米淀粉与白醋保持棉软湿润，顶部铺鲜奶油（Chantilly）与时令水果（奇异果、草莓、百香果）装饰，是澳新（澳大利亚/新西兰）国民甜点。'},
  {id:31,g:'A',src:'2026预测',q:'以下关于「糖」在饼干中的功能，哪项正确？',opts:{A:'白砂糖在常温搅拌过程中极易氧化导致面筋过快硬化',B:'糖粉能够完全抑制油脂融合促使饼干产生极厚酥脆层',C:'粗砂糖未完全溶解形成脆裂晶体，糖粉溶解度高质地细腻',D:'细砂糖遇热分解出大量天然水分使饼干变得湿润且绵软'},ans:'C',exp:'糖的粒径影响饼干质感：细砂糖（较粗）在搅拌时无法完全溶解，部分晶体保留→饼干烘烤后更脆；糖粉（极细）完全溶解→面团更均匀细腻→饼干更松软细腻（如法式手指饼干、雪球饼干的质感）。'},
  {id:32,g:'A',src:'2026预测',q:'「乳化（Emulsification）」在烘焙中的重要性是？',opts:{A:'彻底排空面团内部多余空气以增强烘烤成品的紧实密度',B:'促使蛋白质快速水解成单体氨基酸以提升面团的柔软度',C:'降低面糊整体温度防止黄油中的天然乳脂过早发生融化',D:'借助表面活性剂使互不相溶的水相与油相形成均质分散系'},ans:'D',exp:'乳化（Emulsification）：通过乳化剂（如蛋黄卵磷脂、大豆卵磷脂）使水相与油相稳定混合，防止油水分离。在烘焙中应用广泛：蛋糕面糊（更细腻均匀）→气泡更稳定→体积更大、质地更软；面包（面筋网络更延展）→柔软。'},
  {id:33,g:'A',src:'2026预测',q:'「啤酒酵母（Baker's Yeast）」与「野生酸种（Wild Sourdough Starter）」相比，最主要的区别是？',opts:{A:'单一纯种酿酒酵母产气迅速稳定，酸种含共生菌群发酵慢风味繁复',B:'商业酵母发酵需要添加大量醋酸，酸种酵头完全依赖天然中性发酵',C:'商业酵母仅能在真空环境中产气，酸种酵头可在有氧常压自由呼吸',D:'商业酵母烘烤后具有强烈麦香，酸种酵头成品则完全没有酸味特征'},ans:'A',exp:'商业酵母（Commercial Yeast）：单一菌株（Saccharomyces cerevisiae），发酵速度快（约1~2小时基本发酵），风味较简单；天然酸种（Sourdough）：含数十种野生酵母菌＋多种乳酸菌，发酵慢（4~20小时），产生乳酸、醋酸、酯类等数百种风味物质，风味极其复杂。'},
  {id:34,g:'A',src:'2026预测',q:'制作卷形蛋糕时，海绵蛋糕出炉后为何需要趁热卷起？',opts:{A:'趁热快速卷起可以最大程度加速蛋糕中心热量向外散逸',B:'温热状态下淀粉与面筋结构柔韧延展性好，冷却硬化后易断裂',C:'高温能使内馅涂抹的打发纯鲜奶油保持高度稳定不发生融化',D:'趁热受力能迫使表皮毛孔完全闭合防止蛋糕内部的水分散失'},ans:'B',exp:'海绵蛋糕趁热卷卷（Roll）的科学原理：高温时淀粉链尚未完全老化（Retrogradation），面筋与淀粉结构具有最大延展性，此时卷起蛋糕不会开裂；待冷却后淀粉老化、结构变硬，再卷即会断裂。'},
  {id:35,g:'A',src:'2026预测',q:'「蛋黄酥（Dan Huang Su）」的饼皮使用何种传统配方？',opts:{A:'纯粹依赖法式冷藏裹入黄油进行多次四折的开酥手法',B:'将水油面团油炸熟透后再包入豆沙蛋黄馅进行二次烘烤',C:'以具延展性的水油皮包裹纯油酥经擀卷形成明暗交替酥层',D:'面粉中加入大量重碳酸氢铵在高温烘烤下剧烈崩解分层'},ans:'C',exp:'蛋黄酥使用中式传统「明酥」技术：外层为水油皮（低筋面粉＋猪油＋热水，具延展性）＋内层油酥（低筋面粉＋猪油，纯油酥性），两者包覆折叠，烘烤时形成清晰可见的白色层次（明酥），包裹豆沙＋咸蛋黄馅。'},
  {id:36,g:'A',src:'2026预测',q:'「糖浆浸渍（Simple Syrup Soaking）」在蛋糕制作中的主要功能是？',opts:{A:'增加蛋糕胚体湿润度防止在冷藏陈列中失水变干',B:'增添酒香或果香提升甜品整体层次丰富的风味',C:'降低局部水分活度在一定程度上延缓微生物滋生',D:'充当天然化学膨大剂使蛋糕在冷藏期间继续膨胀'},ans:'D',exp:'糖浆浸渍（Imbibing Syrup）：蛋糕体脱模后刷上热糖浆（可加香草精、朗姆酒、咖啡等），功能：①补充水分防止蛋糕干燥；②增添额外风味层次；③糖浓度降低水分活度，延缓微生物生长延长保鲜。'},
  {id:37,g:'A',src:'2026预测',q:'「费南雪（Financier）」蛋糕的特征原料是？',opts:{A:'焦化榛果黄油与大量杏仁粉及未经打发的纯蛋白',B:'全蛋高速打发至浓稠羽毛状后拌入高筋强韧面粉',C:'新鲜重质酸奶油混合大量融化纯白巧克力与蛋黄',D:'发酵面种加入大量黑麦粉与浸泡朗姆酒的葡萄干'},ans:'A',exp:'费南雪（Financier）法式小烤蛋糕的特征：①蛋白（非蛋黄，不打发）——只用蛋白；②杏仁粉——提供坚果香与湿润质地；③焦化黄油（Beurre Noisette，榛子黄油）——黄油加热至焦化产生坚果香是灵魂所在；④高温快烤（约200℃/8~12min）形成焦脆外壳、湿润内芯。'},
  {id:38,g:'A',src:'2026预测',q:'下列关于「奶酪（Cheese）」与烘焙的搭配，哪项错误？',opts:{A:'奶油乳酪（Cream Cheese）是重芝士蛋糕主体原料',B:'里科塔乳酪（Ricotta）是制作传统可颂的开酥油脂',C:'马斯卡彭（Mascarpone）是传统提拉米苏的核心基底',D:'帕玛森乳酪（Parmesan）常用于法式咸味泡芙调香'},ans:'B',exp:'里科塔（Ricotta）是由乳清再加热制成的新鲜软质奶酪，常用于意大利千层面（Lasagna）、甜点馅料（Cannoli、Cheesecake变体），但不是可颂（Croissant）的材料。可颂使用的是高质量无盐黄油（Unsalted Butter）。'},
  {id:39,g:'A',src:'2026预测',q:'以下哪项是「百香果（Passion Fruit）」在现代法式糕点中的主要应用？',opts:{A:'富含极强油脂成分能直接替代配方中的固体可可脂',B:'其籽粒提取物具有强效防腐杀菌功能延长保质期',C:'高酸度与强烈热带芳香能完美平衡甘纳许与奶油甜腻',D:'在面糊中充当纯天然膨松剂以促使蛋糕体积膨胀'},ans:'C',exp:'百香果（Passion Fruit）以其独特热带酸甜香气，是现代法式精品糕点的热门食材：①百香果慕斯（Mousse）；②百香果镜面果冻（Miroir）；③百香果挞（代替柠檬挞中的柠檬凝乳）；④百香果甘纳许。其高浓度天然酸香可平衡甜腻感。'},
  {id:40,g:'A',src:'2026预测',q:'在烘焙百分比中，已知低筋面粉312g，细砂糖百分比为100%，鸡蛋百分比为167%，泡打粉1%。鸡蛋实际用量是多少？',opts:{A:'187g',B:'312g',C:'468g',D:'521g'},ans:'D',exp:'鸡蛋实际用量 = 面粉重量 × 鸡蛋百分比 = 312g × 167% = 312 × 1.67 ≈ 521g。（烘焙百分比计算：各原料重量 = 面粉重量 × 该原料百分比）'},
  // ── WESTERN Q41-50 (均衡版) ──
  {id:41,g:'B',src:'2026预测',q:'「Mise en Place」在法式厨房中的含义是？',opts:{A:'每位厨师必须在出餐结束后彻底清点冷库的所有剩余存货',B:'严格按照欧洲古典宫廷菜肴标准进行毫无改动的传统复刻',C:'使用标准电子秤严格称量并精确计算每道菜品的食材成本',D:'在正式烹调开单前将所有工器具与食材预先处理定位就绪'},ans:'D',exp:'Mise en Place（法文：所有一切准备就绪）是法式厨房的核心工作哲学，指烹饪开始前将所有食材处理、量取、切割、准备好放置到位，确保烹饪过程流畅高效，减少操作中的混乱与错误。'},
  {id:42,g:'B',src:'2026预测',q:'「真空低温慢煮（Sous-Vide）」牛排的核心优势是？',opts:{A:'精准水浴使肉质内外均匀达到目标熟度再快煎上色',B:'完全省略高温煎烤步骤从真空袋取出即可直接切盘',C:'通过超高压蒸气使结缔组织在数分钟之内彻底融化',D:'能在零下低温环境中彻底杀灭肉品表面的一切细菌'},ans:'A',exp:'Sous-Vide牛排：真空封袋于精确温度水浴（如Medium Rare = 54~57℃）数小时，全体均匀熟化。取出后大火（铁锅/炭火）快速煎制30~60秒形成美拉德焦香外壳——结合两种烹调方法的最佳效果：内部精准熟度 ＋ 外部焦香。'},
  {id:43,g:'B',src:'2026预测',q:'经典法国马赛鱼汤（Bouillabaisse）的代表食材组合是？',opts:{A:'北西洋大西洋鲑鱼搭配浓厚重奶油及马铃薯炖煮',B:'鲜活澳洲龙虾搭配黑松露菌片及意大利红酒焖烧',C:'多种地中海杂鱼贝类加番红花、茴香与番茄慢熬成汤',D:'高档牛里脊肉块搭配洋葱头、西芹与白葡萄酒清炖'},ans:'C',exp:'马赛鱼汤（Bouillabaisse）是法国普罗旺斯马赛港的地标性名菜：使用多种当地地中海鱼（Rascasse、圣皮耶尔鱼等）与海鲜，加入番茄、橙皮、番红花（Saffron）、茴香、大蒜等香料慢炖，搭配蒜味蛋黄酱（Rouille）与烤面包片享用。'},
  {id:44,g:'B',src:'2026预测',q:'「Tenderloin（菲力）」部位的肉质特点与最适合的烹调方法是？',opts:{A:'结缔组织极其粗硬耐嚼，必须通过长时间文火砂锅炖煮',B:'肌肉运动极少纤维最嫩脂肪低，适宜高温快煎或快烤',C:'肌间脂肪雪花密布油分极重，最适宜长时间烟熏脱脂',D:'富含大量骨胶原蛋白，只适合切块用于慢炖浓稠高汤'},ans:'B',exp:'Tenderloin（腰内肉/里脊）：位于脊柱内侧，几乎不承受肌肉运动，因此肌肉纤维最细嫩、脂肪（Marbling）最少，是最嫩的牛肉部位。最适合快速高温烹调（Pan-Fry、Grill、Roast），保留嫩度；炖煮（Stew）会使其质地变老失去优势。'},
  {id:45,g:'B',src:'2026预测',q:'「Paella（西班牙烩饭）」的灵魂食材与传统烹调容器是？',opts:{A:'高吸水短粒米（Bomba）与专用浅底双耳宽口平底铁锅',B:'细长型印度香米（Basmati）与高深度带盖圆形砂锅',C:'意大利长粒高淀粉米与传统厚底带柄不锈钢深口炒锅',D:'泰国茉莉香米与带有密集小孔的传统竹制圆形蒸笼'},ans:'A',exp:'Paella（西班牙巴伦西亚）灵魂要素：①Bomba/Calasparra短粒米——高吸水性，充分吸收汤汁风味不糊烂；②浅底宽口专用铁锅（Paellera）——大接触面使米饭均匀受热，形成底层焦脆锅巴（Socarrat），是评价Paella质量的关键指标。'},
  {id:46,g:'B',src:'2026预测',q:'「French Toast（法式吐司）」的正确制作顺序是？',opts:{A:'先在热干锅中两面烤焦再迅速淋入冰镇未打散的生全蛋液',B:'面包单面沾裹纯牛奶后立刻放入高温深油锅中炸至金黄',C:'将厚切面包充分浸泡蛋奶香草混合液再用黄油双面温煎',D:'先将面包均匀滚满干面包糠后再浸入高浓度纯枫糖浆中'},ans:'C',exp:'法式吐司（French Toast）正确工序：先将面包浸泡于混合液（牛奶＋蛋液＋糖＋香草）中让液体充分渗入面包内部，吸收均匀；再放入锅中用黄油煎制两面金黄。若先沾蛋液则外层已凝固，内部难以吸收牛奶，口感干燥。'},
  {id:47,g:'B',src:'2026预测',q:'「塔塔牛排（Steak Tartare）」的制作特点是？',opts:{A:'整块牛排用喷枪炙烤至三分熟后切成厚片冷藏上桌',B:'新鲜极嫩牛肉细致手切拌入生蛋黄酸豆洋葱全生食用',C:'牛肉末用红酒与香草腌渍入味后置于烤箱中烤至全熟',D:'将牛绞肉煮熟挤干水分后再加入大量美乃滋搅拌冷食'},ans:'B',exp:'Steak Tartare（塔塔牛排）是法式经典冷前菜：选用极新鲜牛里脊（Tenderloin）或腿肉，细手切（Mince）后与生蛋黄、续随子（Capers）、洋葱末、芥末、Worcestershire酱等调味混合，完全生食（Raw）。食材新鲜度与卫生是关键安全要素。'},
  {id:48,g:'B',src:'2026预测',q:'「Crème Brûlée（法式焦糖布丁）」表面焦糖化处理，最专业的工具是？',opts:{A:'微波炉高火转动加热十秒钟',B:'家用热风电吹风持续近距离强吹',C:'炉灶高压大火直接熏烤碗体外部',D:'手持专业喷枪或顶部上火焗炉'},ans:'D',exp:'Crème Brûlée 表面焦糖化：在已凝固的卡士达布丁表面撒薄层细砂糖，用①厨用喷枪（Blowtorch）——最精准直接，专业常用；②Salamander（顶部加热）——商业厨房使用，热力均匀。目标：糖层完全焦糖化、薄脆如玻璃，而布丁本体保持冰凉。'},
  {id:49,g:'B',src:'2026预测',q:'「Confit」烹调技法的定义是？',opts:{A:'腌渍肉类完全浸入自身油脂中低温慢烹熟化并隔绝空气保存',B:'将生鲜食材置于高温深油锅中瞬间炸至外壳金黄酥脆脱水',C:'将肉类表面刷满植物油后挂在炭火上方利用冷烟长时间慢熏',D:'利用饱和纯水蒸气在密闭压力舱内将禽肉完全蒸至软烂脱骨'},ans:'A',exp:'Confit（腌渍油封）：法式传统保存技法，食材（如鸭腿、鹅腿）先以盐和香料腌制，再浸入自身脂肪中以极低温度（约80~90℃）缓慢烹调数小时，使结缔组织分解、肉质极嫩，然后密封于脂肪层中冷藏保存（传统可保存数月）。'},
  {id:50,g:'B',src:'2026预测',q:'「Charcuterie（熟肉制品）」在西餐中常见的产品类型包括哪些？',opts:{A:'仅包括未经过任何发酵处理的纯深海生鱼片与贝类',B:'仅包括纯蔬菜类经天然乳酸发酵脱水制成的酸渍泡菜',C:'风干香肠、肉酱、肉冻、生火腿等腌制或风干熟肉制品',D:'仅涵盖经过高温烘烤后立即切片食用的全熟热牛排拼盘'},ans:'C',exp:'Charcuterie（法式熟肉制品专卖/产品）涵盖：Saucisson（法式干香肠）、Pâté（肉酱）、Rillettes（肉泥）、Terrine（肉冻）、Prosciutto（意大利生火腿）、Salami（萨拉米）、Jambon（熟火腿）等多种腌制、发酵、风干、烟熏肉类加工品。'},
  // ── ASIAN Q51-60 (均衡版) ──
  {id:51,g:'C',src:'2026预测',q:'中餐「滑油」技法的定义与目的是？',opts:{A:'用八成热烈油使食材外皮瞬间炸脆焦黄并完全收干肉汁',B:'使上浆原料在三至四成温油中划散定型并锁住内部水分',C:'彻底排出原料内部所吸收的油脂以降低菜品的总热量',D:'利用高温油脂瞬间杀灭食材深处可能潜伏的致病细菌'},ans:'B',exp:'滑油（Velvet / Oil Blanching）：上浆（挂糊）后的食材投入100~120℃温油中划散至外层定型呈半熟状（约60~70%熟度），捞出控油。目的：浆粉在低温油中糊化包裹食材，锁住水分，确保成品极度嫩滑。是炒肉片、炒虾仁等滑炒菜肴的核心技法。'},
  {id:52,g:'C',src:'2026预测',q:'「挂糊（Batter Coating）」与「上浆（Velveting）」的主要区别是？',opts:{A:'挂糊专门用于低温水煮菜肴，上浆专门用于明火炭烤菜肴',B:'挂糊仅适用于淡水活鱼，上浆则严格限制于禽肉与红肉类',C:'两者配料完全一样，仅因不同地域方言产生叫法上的差异',D:'挂糊浆层较厚常用于炸熘，上浆浆层极薄多用于滑炒水汆'},ans:'D',exp:'挂糊（Batter）：较厚的粉浆包裹食材，油炸后形成酥脆厚实外壳（如糖醋排骨、各式炸物）。上浆（Velveting）：薄层淀粉（生粉＋蛋白/蛋黄＋油脂）包裹食材，滑油/滑水后保持食材嫩滑水润（如嫩炒肉片）。'},
  {id:53,g:'C',src:'2026预测',q:'川菜「七滋」的完整内容是？',opts:{A:'酸、甜、苦、辣、咸、鲜、香',B:'麻、辣、酸、甜、鲜、苦、涩',C:'咸、鲜、焦、香、甜、酸、辣',D:'麻、香、咸、淡、苦、滑、脆'},ans:'A',exp:'川菜七滋（7 Tastes of Sichuan Cuisine）：酸、甜、苦、辣、咸、鲜、香——川菜讲究复合调味，一道菜常同时呈现多种滋味，形成层次丰富的复合口感。「麻（Numbing）」是川菜的第八种独特感官体验（来自花椒），有时单独列出。'},
  {id:54,g:'C',src:'2026预测',q:'「东坡肉」的烹调工艺与发源地是？',opts:{A:'猪瘦肉经裹糊油炸后浇淋酸甜糖醋芡汁，发源于北京',B:'带皮五花肉块加黄酒酱油冰糖文火慢焖，发源于杭州',C:'整只猪肘经高压大火清炖后淋上麻辣红油，发源于成都',D:'排骨经长时间炭火烤制后刷上甜面酱汁，发源于广州'},ans:'B',exp:'东坡肉（由北宋文人苏东坡（苏轼）以杭州太守身份推广创制）：选用猪五花肉（三层肉）切大方块，以绍兴黄酒、生抽、冰糖、葱姜为主料，文火慢焖（红烧）约2~3小时，成品红亮软烂、肥而不腻。浙菜代表名作。'},
  {id:55,g:'C',src:'2026预测',q:'「佛跳墙」是哪个地区的顶级名菜，主要食材包含哪些？',opts:{A:'以新鲜活鱼头搭配老豆腐文火快熬成奶白色汤羹',B:'以整只填鸭经挂炉果木烘烤后片皮搭配甜面酱卷饼',C:'鲍参翅肚等名贵干货汇聚坛中加绍酒高汤文火慢煨',D:'选用优质牛羊杂碎投入麻辣牛油锅底中长时间翻滚'},ans:'C',exp:'佛跳墙（福建福州地标菜）：相传香气太诱人连佛祖也要「跳墙」而出品尝。选用鱼翅、鲍鱼、干贝、蹄筋、花胶、瑶柱等数十种珍贵食材，以绍兴酒坛密封，隔水蒸炖约8~10小时，汤汁浓醇馥郁，是闽菜最高境界代表。'},
  {id:56,g:'C',src:'2026预测',q:'马来西亚叻沙（Laksa）大致分为四种，其中「亚参叻沙」的特点是？',opts:{A:'以大量浓厚新鲜椰浆为底，色泽金黄温润且微辣',B:'以醇厚牛骨高汤为底，加入大量沙茶酱与花生碎',C:'以清甜鸡汤为底，仅用白胡椒粉与新鲜豆芽调味',D:'以鲜鱼熬汤加罗望子调酸，不加椰奶呈现酸辣鲜爽'},ans:'D',exp:'亚参叻沙（Asam Laksa）：以沙丁鱼/竹鱼熬成的鱼汤为底，加入亚参（罗望子/Tamarind）调出独特酸味，不加椰奶，汤色深红，酸辣鲜爽，搭配河粉、叻沙叶（Daun kesom）、花生末、黄瓜丝等配料，是槟城名物。'},
  {id:57,g:'C',src:'2026预测',q:'中餐上浆技法中，「水粉浆」的主要成分是？',opts:{A:'淀粉与适量清水（常配合少许精盐与料酒）',B:'全蛋液与优质细面包糠（常搭配辣椒粉）',C:'高筋面粉与双效泡打粉（需常温发酵两小时）',D:'纯蛋黄与大量熟猪油（需隔水完全加热乳化）'},ans:'A',exp:'水粉浆（最简单的上浆）= 生粉（淀粉）＋清水（有时加盐），浓稠度较低，适用于简单滑炒或汆水处理。蛋清浆（蛋白＋生粉）更细腻适合高档嫩炒；脆浆（面粉＋泡打粉＋水）用于酥炸类。'},
  {id:58,g:'C',src:'2026预测',q:'「清蒸」烹调法的烹调温度与适用食材特点是？',opts:{A:'利用低温干燥热风长久烘烤，适宜油脂丰腴的整禽',B:'利用纯饱和水蒸气温和加热，适宜新鲜质嫩的原汁食材',C:'利用沸腾红油翻滚浸炸，适宜筋膜粗壮的红肉块',D:'利用冷水浸泡慢炖，适宜坚硬耐煮的草本根茎干货'},ans:'B',exp:'清蒸（Steaming）：约100℃饱和水蒸气加热，特点：①温和均匀加热；②保留食材天然水分与营养；③不添加油脂，保持清淡原味。最适合：新鲜鱼类（如清蒸石斑）、蒸蛋、鲜虾、豆腐等娇嫩食材，是粤菜「鲜」的精髓技法。'},
  {id:59,g:'C',src:'2026预测',q:'「酱油（Soy Sauce）」的酿造过程中，负责产生鲜味（Umami）的主要物质是？',opts:{A:'氯化钠晶体在水溶液中电离出的大量纯钠离子',B:'烘炒小麦粉在高温焦糖化过程中产生的焦糖色素',C:'大豆蛋白质在酶解中释放出的游离谷氨酸及氨基酸',D:'醋酸菌在有氧呼吸发酵过程中所代谢产生的高浓度乙酸'},ans:'C',exp:'酱油鲜味来源：大豆（黄豆）在霉菌（Aspergillus oryzae）作用下发酵，大豆蛋白水解为谷氨酸（Glutamic Acid）、天冬氨酸等游离氨基酸——谷氨酸是「鲜味（Umami）」的核心物质，与人工鲜味剂味精（MSG，谷氨酸钠）的原理相同。'},
  {id:60,g:'C',src:'2026预测',q:'「满汉全席」的代表标志不包含以下哪项？',opts:{A:'汇聚南北珍馐百味的海量佳肴品类',B:'融合满汉传统烹调精华的高超烹饪技艺',C:'讲究金银玉石与景泰蓝搭配的精致器皿',D:'故意拖延用餐节奏的虚伪繁复繁文缛节'},ans:'D',exp:'满汉全席（清朝宫廷宴席顶峰，结合满族与汉族饮食精华）的代表标志：①佳肴繁多（108~196道菜）；②厨艺高超（精细烹调工艺）；③器皿精致（金银玉石餐具）。「繁文缛节（繁复的礼仪节奏）」不是其代表标志——满汉全席强调的是菜肴品质与器皿规格。'},
];

// ═══════════════════════════════════════════════
// WRITTEN QUESTIONS — PAPER A
// ═══════════════════════════════════════════════
const paperA_written = [
  {
    id:'A-W1', type:'mandatory', label:'甲组·必答题（10%）—— 1题必答',
    stem:'1. 已知戚风蛋糕配方的烘焙百分比如下表，低筋面粉重量为 250g。',
    subqs:[
      {label:'(a)', text:'重抄下表并计算各材料的实际重量（g）。（7%）',
       table:[
         {m:'低筋面粉',p:'100%',w:'250g'},
         {m:'细砂糖',p:'80%',w:'___'},
         {m:'鸡蛋（全蛋）',p:'160%',w:'___'},
         {m:'沙拉油',p:'40%',w:'___'},
         {m:'牛奶',p:'40%',w:'___'},
         {m:'泡打粉',p:'2%',w:'___'},
         {m:'塔塔粉',p:'1%',w:'___'},
         {m:'合计',p:'423%',w:'___'},
       ]},
      {label:'(b)', text:'写出烘焙百分比的计算公式。（3%）'}
    ],
    answer:'(a) 计算方法：各原料重量 = 面粉重量（250g）× 该原料百分比\n• 细砂糖：250g × 80% = 200g\n• 鸡蛋：250g × 160% = 400g\n• 沙拉油：250g × 40% = 100g\n• 牛奶：250g × 40% = 100g\n• 泡打粉：250g × 2% = 5g\n• 塔塔粉：250g × 1% = 2.5g\n• 合计：250+200+400+100+100+5+2.5 = 1057.5g\n\n(b) 烘焙百分比公式：\n某原料百分比（%）= 该原料重量 ÷ 面粉总重量 × 100%\n该原料实际重量 = 面粉重量 × 该原料百分比（以小数表示）\n面粉永远设定为 100% 基准值。'
  },
  {
    id:'A-W2', type:'optional', label:'乙组·选答题（30%）—— 7题选答3题',
    questions:[
      {id:2, stem:'2. 搅拌机（Mixer）是烘焙作业中不可缺少的设备。\n(a) 试写出搅拌机中三种不同拌打器的名称及其主要功能。（6%）\n(b) 试列举面包面团搅拌的六个主要阶段，并简述「完全扩展阶段」的面团特征。（4%）',
       answer:'(a) 三种拌打器：\n① 钩状拌打器（Dough Hook）——专门搅拌高筋面团（面包、比萨），模拟手工揉面，充分发展面筋网络；\n② 桨状拌打器（Flat Beater / Paddle）——拌合蛋糕面糊、饼干面团、奶油霜，适合中等硬度材料；\n③ 球状拌打器（Wire Whip / Balloon Whisk）——打发鸡蛋、鲜奶油、蛋白霜，充入大量空气。\n\n(b) 六阶段：①原料混合→②拾起→③卷起→④扩展→⑤完全扩展→⑥断筋（过度）\n【完全扩展阶段】：面团极光滑有光泽；可拉出极薄均匀的透明薄膜，破口平滑圆弧（无锯齿）；弹性与延伸性达最佳平衡。适合制作吐司、软式甜面包。'},
      {id:3, stem:'3. 法式料理对西餐的发展影响深远。\n(a)① 经典法式洋葱汤用什么高汤做汤底？（2%）② 若因宗教因素，可用什么高汤替代？（1%）\n(b) 为什么法式洋葱汤呈深色？洋葱在烹调时的专用术语是什么？（2%＋1%）\n(c) 试列出维希冷汤（Vichyssoise）的主材料及基本烹调方式。（4%）',
       answer:'(a)① 牛肉褐色高汤（Brown Beef Stock）或小牛高汤（Veal Stock）\n  ② 蔬菜高汤（Vegetable Stock）作素食/宗教替代\n\n(b) 深色原因：洋葱在低温长时间（150~180℃约30~45分钟）翻炒下，天然糖分发生【焦糖化反应（Caramelization）】产生深棕色素与浓郁甜香。专用术语：「焦糖化洋葱（Caramelize the Onions）」\n\n(c) 维希冷汤（Vichyssoise）：主材料：韭葱（Leek）、马铃薯（Potato）、洋葱（Onion）、鸡汤、鲜奶油。\n烹调：韭葱洋葱炒软→加马铃薯与鸡汤煮至软烂→打成细腻浓汤→过滤加鲜奶油→冷藏冰镇后盛盘，顶部以葱末或鱼子酱装饰。'},
      {id:4, stem:'4. 不同烹调方法影响菜肴品质。\n(a)① 水波煮（Poaching）温度？② 蒸气烹（Steaming）温度？③ 荷兰酱的主要油脂？④ 褐高汤褐色来源？⑤ Roux功效？（各1%）\n(b) 如何定义一个好的炸物？（5%）',
       answer:'(a)① 约65~80℃（微沸状态，液体不翻滚）\n② 约100℃（饱和水蒸气）\n③ 澄清黄油（Clarified Butter）\n④ 骨头与肉类先高温烘烤至深褐色（美拉德反应），产生深色素融入高汤\n⑤ Roux功效：作为酱汁增稠剂（Thickening Agent），淀粉糊化使液体浓稠顺滑\n\n(b) 优质炸物评定标准：\n① 色泽金黄均匀——无过焦或过淡区域；② 外脆内嫩——外壳酥脆，内部食材水嫩熟透；③ 含油量低——表面不油腻；④ 无异味——油质新鲜，无哈喇味；⑤ 形状完整——裹粉均匀，大小一致便于均匀受热。'},
      {id:5, stem:'5. 牛肉是西餐重要食材。\n(a) 说明四种牛排生熟度（Medium Rare、Medium、Medium Well、Well Done）。（4%）\n(b) 说明「休息时间（Resting Time）」的目的。（2%）\n(c) 列举5种常见西餐香草（中英对照）。（4%）',
       answer:'(a) • Medium Rare（三分熟）55~57℃：内约50%粉红/红色，汁液丰富\n• Medium（五分熟）60~63℃：内约25%粉红色，软嫩多汁\n• Medium Well（七分熟）65~68℃：少量粉红痕迹，肉质开始较坚实\n• Well Done（全熟）70℃以上：全部熟透呈灰褐色，质地坚实汁液少\n\n(b) 休息时间（Resting）：牛排离火后静置3~5分钟。高温时肌肉纤维收缩将汁液挤向中心，静置后肌肉松弛，汁液重新均匀分布，防止切开时大量汁液流失。\n\n(c) 5种西餐香草：① 罗勒 Basil ② 百里香 Thyme ③ 迷迭香 Rosemary ④ 欧芹 Parsley ⑤ 月桂叶 Bay Leaf'},
      {id:6, stem:'6. 中餐刀工是核心技能。\n(a) 简述下列切割法适用材料并各举一例：① 直切 ② 推切 ③ 拉切 ④ 推拉切 ⑤ 滚刀切。（5%）\n(b) 列举中国八大菜系中任意5个，并各举一道代表菜。（5%）',
       answer:'(a) 切割法：\n① 直切——脆硬蔬菜（胡萝卜、萝卜），刀垂直向下。例：切萝卜片\n② 推切——软嫩食材（熟肉、豆腐），刀由后向前推。例：切熟猪肝\n③ 拉切——韧性纤维食材（生肉），刀由前向后拉。例：切鸡胸肉\n④ 推拉切——有弹性食材（火腿），推拉结合。例：切火腿薄片\n⑤ 滚刀切——圆柱形蔬菜（茄子），边切边转食材。例：切滚刀茄子块\n\n(b) 菜系代表（任5个）：\n① 川菜→麻婆豆腐 ② 粤菜→清蒸石斑 ③ 鲁菜→葱烧海参 ④ 苏菜→松鼠桂鱼 ⑤ 浙菜→西湖醋鱼 ⑥ 闽菜→佛跳墙 ⑦ 湘菜→剁椒鱼头 ⑧ 徽菜→红烧臭鳜鱼'},
      {id:7, stem:'7. 厨房安全卫生是基本守则。\n(a) 按顺序写出厨房餐具的洗涤流程。（4%）\n(b) 写出厨房卫生管理中的四大原则。（4%）\n(c) 说明四色砧板管理制度。（2%）',
       answer:'(a) 餐具洗涤流程（5步）：\n① 刮除残渣→② 预浸/冲洗→③ 洗涤（热水＋洗洁精刷洗）→④ 漂清（流水清洗去除洗洁精）→⑤ 消毒（煮沸100℃/1分钟，或化学消毒，或高温烘干）\n\n(b) 四大卫生原则：\n① 清洁（Clean）—定时清洗接触食品的表面与设备\n② 隔离（Separate）—生熟分开，防止交叉污染\n③ 烹煮（Cook）—确保食物达到安全内部温度\n④ 控温（Chill）—冷藏4℃以下，热食60℃以上\n\n(c) 四色砧板：红色→生红肉（猪牛羊）；黄色→生禽肉（鸡鸭）；蓝色→生海鲜（鱼虾贝）；绿色→新鲜蔬果；白色→熟食'},
      {id:8, stem:'8. 粮食制品是以粮食为原料制作的成品或半成品。\n(a) 列出粮食制品的三大种类。（3%）\n(b) 说明以下食品的储存方法：① 蛋类 ② 豆类 ③ 豆腐类 ④ 油脂类。（4%）\n(c) 列举三种中餐调味料并说明其作用。（3%）',
       answer:'(a) 三大种类：\n① 谷类制品（面粉、大米、玉米粉）\n② 豆类制品（豆腐、豆浆、腐竹）\n③ 薯类制品（淀粉、粉丝、粉条）\n\n(b) 储存：\n① 蛋类：冷藏（4℃以下），尖端朝下，不水洗后储存\n② 豆类（干燥）：阴凉干燥密封，10~15℃，湿度50%以下\n③ 豆腐：冷藏（0~4℃），泡清水每日换水，1~2天内用完\n④ 油脂：密封避光储存，防氧化酸败，冷藏延长保质期\n\n(c) 调味料：\n① 酱油——咸味、增色（焦糖色素）、增鲜（氨基酸）\n② 米酒——去腥解腻、增香、软化肉质\n③ 香醋——酸味、增进食欲、软化食材、防腐'}
    ]
  }
];

// ═══════════════════════════════════════════════
// WRITTEN QUESTIONS — PAPER B
// ═══════════════════════════════════════════════
const paperB_written = [
  {
    id:'B-W1', type:'mandatory', label:'甲组·必答题（10%）—— 1题必答',
    stem:'1. 以下为一款布朗尼（Brownie）蛋糕的配方。已知低筋面粉重量为 200g，巧克力百分比为150%，无盐黄油百分比为125%，细砂糖百分比为150%，鸡蛋百分比为125%，可可粉百分比为25%。',
    subqs:[
      {label:'(a)', text:'重抄下表并计算各材料的实际重量（g）。（7%）',
       table:[
         {m:'低筋面粉',p:'100%',w:'200g'},
         {m:'黑巧克力',p:'150%',w:'___'},
         {m:'无盐黄油',p:'125%',w:'___'},
         {m:'细砂糖',p:'150%',w:'___'},
         {m:'鸡蛋',p:'125%',w:'___'},
         {m:'可可粉',p:'25%',w:'___'},
         {m:'合计',p:'675%',w:'___'},
       ]},
      {label:'(b)', text:'说明布朗尼蛋糕中「巧克力」的烘焙功能（至少三点）。（3%）'}
    ],
    answer:'(a) 计算（各原料重量 = 面粉200g × 百分比）：\n• 黑巧克力：200 × 150% = 300g\n• 无盐黄油：200 × 125% = 250g\n• 细砂糖：200 × 150% = 300g\n• 鸡蛋：200 × 125% = 250g\n• 可可粉：200 × 25% = 50g\n• 合计：200+300+250+300+250+50 = 1350g\n\n(b) 巧克力的烘焙功能：\n① 提供浓郁巧克力风味与香气（可可脂与可可固形物）\n② 提供脂肪：可可脂替代部分黄油，产生湿润浓稠的质地\n③ 提供天然乳化性：可可脂的结晶特性有助于面糊稳定\n④ 增添深棕色泽（可可固形物中的棕色素）\n⑤ 调节甜度平衡：苦巧克力的苦味平衡配方中大量糖分'
  },
  {
    id:'B-W2', type:'optional', label:'乙组·选答题（30%）—— 7题选答3题',
    questions:[
      {id:2, stem:'2. 天然酸种面包（Sourdough Bread）近年来在精品烘焙界极为盛行。\n(a) 解释天然酸种酵母（Sourdough Starter）的发酵原理及其给面包带来的独特特征。（5%）\n(b) 说明「自解（Autolyse）」技法的操作步骤及目的。（3%）\n(c) 为何酸种面包的保质期比商业酵母面包更长？（2%）',
       answer:'(a) 酸种发酵原理：天然酸种由捕获自空气与面粉中的【野生酵母菌（Wild Yeast，如Saccharomyces cerevisiae变种）】与【乳酸菌（Lactobacillus）】共生培育。酵母菌分解糖分产生CO₂使面包膨胀；乳酸菌产生乳酸（温和酸感）与醋酸（强烈酸感），赋予复杂风味。独特特征：①复杂酸香风味（无法用商业酵母复制）；②外壳更酥脆坚实；③内部大不规则孔洞；④保存期更长（有机酸抑菌）。\n\n(b) 自解（Autolyse）：将面粉与水混合（不加盐、酵母）静置20~60分钟，让淀粉充分吸水、面筋自然排列延展。目的：①减少机械搅拌时间→降低面团温度；②改善面团延展性→更易整型；③改善最终成品孔洞结构→更开放大孔。\n\n(c) 保质期更长原因：乳酸菌产生的【乳酸与醋酸】降低面团pH值（约pH3.5~4.5），酸性环境抑制霉菌、杂菌生长繁殖，同时乳酸本身具有一定抗微生物活性，因此酸种面包可在室温保存3~5天而不发霉。'},
      {id:3, stem:'3. 现代西式糕点中，「慕斯（Mousse）」是精品蛋糕的灵魂。\n(a) 慕斯的基本结构组成（Base + Aeration + Setting Agent）各包含什么？（4%）\n(b) 制作镜面果冻（Mirror Glaze / Nappage）时，需注意哪些关键操作？（3%）\n(c) 列出制作提拉米苏（Tiramisu）的主要材料及制作要点。（3%）',
       answer:'(a) 慕斯三层结构：\n① 基底（Base）——主风味来源：巧克力甘纳许、水果泥（果泥+糖浆）、卡士达酱等；\n② 充气（Aeration）——提供轻盈质感：打发鲜奶油（Whipped Cream）或意式蛋白霜（Italian Meringue）；\n③ 凝固剂（Setting Agent）——使慕斯定型：吉利丁（Gelatin，最常用）或琼脂（Agar，素食用）。\n\n(b) 镜面果冻关键操作：\n①温度控制：镜面须在30~35℃（接近体温）时淋覆，太热会融化慕斯，太冷则凝固太快无法均匀流动；②慕斯须冷冻至-18℃以下，淋面时温差使镜面快速凝固；③一次从中心均匀淋下，不要来回涂抹；④避免气泡（可提前过筛）。\n\n(c) 提拉米苏（Tiramisu）：主材料：马斯卡彭奶酪（Mascarpone）、蛋黄、细砂糖、鲜奶油、手指饼干（Ladyfinger/Savoiardi）、浓缩咖啡（Espresso）、可可粉。制作要点：蛋黄+糖隔水打发→拌入Mascarpone→拌入打发鲜奶油→手指饼干快速浸咖啡液（不泡软）→层叠→冷藏4小时→撒可可粉。'},
      {id:4, stem:'4. 食品安全是厨艺专业的基本守则。\n(a) 解释HACCP系统的七大原则。（7%）\n(b) 说明「危险温度带（Danger Zone）」并列举两种高风险食品。（3%）',
       answer:'(a) HACCP七大原则：\n① 危害分析（Hazard Analysis）——识别潜在生物/化学/物理危害；\n② 确定关键控制点（CCPs）——找出可控制危害的关键工艺步骤；\n③ 建立关键限制值（Critical Limits）——每个CCP的安全参数（如温度、时间）；\n④ 建立监控程序——定期监测CCP参数是否在控制范围内；\n⑤ 建立纠偏措施——当CCP超出限制时的应急处理程序；\n⑥ 建立验证程序——定期验证HACCP系统有效性（如微生物检测）；\n⑦ 建立记录保存系统——完整记录所有监控数据与操作记录，便于追溯。\n\n(b) 危险温度带：5~60℃。此范围内大多数致病细菌（如沙门氏菌、大肠杆菌、金黄色葡萄球菌）繁殖最活跃，食品不应在此温度带停留超过2小时。\n高风险食品：①禽肉类（鸡、鸭）——沙门氏菌风险；②海鲜（鱼、虾、贝类）——肠炎弧菌风险。'},
      {id:5, stem:'5. 马来西亚是多元文化美食的天堂，有丰富的亚洲烹调传统。\n(a) 试描述马来西亚四种叻沙（Laksa）的特点与区别。（4%）\n(b) 说明「亚参（Asam / Tamarind）」在马来西亚烹调中的主要应用。（3%）\n(c) 列举马来西亚三道国菜或代表性美食并简述其特色。（3%）',
       answer:'(a) 四种叻沙：\n① 咖喱叻沙（Curry Laksa）——以椰浆＋咖喱为汤底，浓郁微辣，配米粉或面，槟城/吉隆坡常见；\n② 亚参叻沙（Asam Laksa）——以鱼汤＋罗望子调酸，不加椰奶，酸辣鲜，槟城名物；\n③ 砂劳越叻沙（Sarawak Laksa）——以采用砂捞越特制参巴酱为底，加椰浆，配粗米粉、鸡肉、虾；\n④ 东海岸叻沙（East Coast Laksa）——偏甜，以鱼高汤为底，配宽粗米粉，吉兰丹/登嘉楼风格。\n\n(b) 亚参（Tamarind/罗望子）应用：亚参果肉含丰富有机酸（酒石酸、柠檬酸），主要应用：①调酸（替代醋）用于鱼类、虾类烹调去腥增酸；②制作亚参虾（Udang Masak Asam）；③亚参叻沙汤底；④亚参甜酸酱；⑤嫩化肉类（酸性软化肌肉纤维）。\n\n(c) 马来西亚代表美食（任3道）：\n① 椰浆饭（Nasi Lemak）——以椰浆与香兰叶煮饭，搭配参巴辣酱、炸花生、凤尾鱼、水煮蛋，是国民早餐；\n② 肉骨茶（Bak Kut Teh）——猪肋骨以中药香料长时间熬炖，汤底清鲜药香；\n③ 炒贵刁（Char Kway Teow）——宽粁条以猪油大火爆炒，加虾、蛤蜊、豆芽、韭黄，焦香四溢。'},
      {id:6, stem:'6. 中餐烹调技法丰富多彩，各有其科学原理。\n(a) 解释「焰(Yan)」「煨(Wei)」「扒(Pa)」三种烹调方法的定义与特点。（3%）\n(b) 试列出中餐12大热菜烹调技法中的任意8种，并各举一例代表菜。（4%）\n(c) 说明中餐「上浆」处理肉类的科学原理及其效果。（3%）',
       answer:'(a) 三种烹调法：\n① 焰——将腌制好的食材以明火（炭火）直接烧烤，外焦香脆，内鲜嫩，如北京烤鸭（挂炉焰烤）；\n② 煨——食材与汤汁一同置于密封容器（砂锅/瓦罐）中，文火长时间缓慢加热，汤汁浓缩醇厚，如煨猪蹄；\n③ 扒——将原料整齐排列，加酱汁原汁小火慢煮至熟，大翻炒瓢成型保持形态，整体上盘，如扒整鸡。\n\n(b) 12大技法（任8种）：\n① 炒（清炒虾仁）② 滑（滑炒肉片）③ 爆（葱爆羊肉）④ 炖（清炖排骨汤）⑤ 蒸（清蒸石斑）⑥ 炸（糖醋里脊）⑦ 煎（煎饺子）⑧ 烤（叉烧肉）⑨ 溜（糖醋咕噜肉）⑩ 煨（煨牛腩）⑪ 扒（扒整鸡）⑫ 腌（腌酱牛肉）\n\n(c) 上浆科学原理：\n上浆（Velveting）= 生粉（淀粉）＋蛋白/蛋黄＋少量油，包裹在肉类表面。\n①淀粉糊化形成保护膜，锁住肉类天然水分；\n②低温滑油时（100~120℃），浆粉迅速糊化固化在肉表面；\n③阻断高温与肉类蛋白质直接接触，防止急速收缩失水；\n④效果：肉质保持极度嫩滑，口感顺滑有弹性，无干柴感。'},
      {id:7, stem:'7. 现代烘焙融合了传统工艺与科技创新。\n(a) 解释「低温慢煮（Sous-Vide）」在布丁/焦糖布丁制作中的应用与优势。（4%）\n(b) 说明「万能蒸烤炉（Combi Oven）」的三种基本工作模式及各自适用场景。（3%）\n(c) 试列出「天然发酵酸种（Sourdough）」面包与「商业酵母面包」在口感、风味、外壳、保存期」方面的主要区别。（3%）',
       answer:'(a) Sous-Vide布丁应用：\n布丁食材（如Crème Brûlée原料：蛋黄、鲜奶油、糖、香草）混合后，以真空袋密封或置于密封容器，放入精确控温水浴（约80~82℃）中烹调45~60分钟。\n优势：①温度精确——蛋白质在80℃温和变性凝固，避免超过100℃产生气泡孔洞；②全体均匀受热——水浴四面导热，无烤箱热梯度差异；③质地极为细腻——没有过度凝固或橡皮感的风险；④可批量标准化生产，品质稳定一致。\n\n(b) Combi Oven三种模式：\n① 纯热风模式（Convection Mode）——循环热风干热烘烤，适合：饼干、酥皮类、焦糖布丁表面上色；\n② 纯蒸汽模式（Steam Mode）——100%蒸汽，适合：蔬菜、海鲜保鲜蒸制、布丁制作；\n③ 混合模式（Combi Mode）——热风＋蒸汽同时，适合：硬式面包（初期蒸汽促膨胀，后期热风上色成脆皮）、禽肉（外脆内嫩）。\n\n(c) 酸种vs商业酵母面包对比：\n• 口感：酸种→内部大不规则气孔，嚼劲有深度；商业→气孔均匀细腻，柔软\n• 风味：酸种→复杂酸香（乳酸＋醋酸）＋坚果麦香；商业→简单酵母香，风味较单一\n• 外壳：酸种→极厚实酥脆，噼啪声响；商业→外壳较薄软\n• 保存期：酸种→3~5天室温（有机酸抑菌）；商业→1~2天（易变霉）'}
    ]
  }
];

// ═══════════════════════════════════════════════
// STATE & TIMER
// ═══════════════════════════════════════════════
const state = {
  A: { mode:'practice', answers:{}, timerInterval:null, timeLeft:80*60, submitted:false },
  B: { mode:'practice', answers:{}, timerInterval:null, timeLeft:80*60, submitted:false }
};

// ── FREQUENCY CHART DATA ──
const freqData = [
  { label:'搅拌六阶段', count:6, max:6 },
  { label:'酵母换算比例', count:5, max:6 },
  { label:'五大母酱', count:5, max:6 },
  { label:'蛋糕三大分类', count:5, max:6 },
  { label:'中餐刀工', count:4, max:6 },
  { label:'食品安全HACCP', count:4, max:6 },
  { label:'烘焙材料特性', count:4, max:6 },
  { label:'马卡龙', count:3, max:6 },
  { label:'烘焙百分比', count:4, max:6 },
  { label:'牛排熟度', count:3, max:6 },
];

function buildFreqChart() {
  const container = document.getElementById('freqChart');
  freqData.forEach((d, i) => {
    const pct = Math.round(d.count / d.max * 100);
    const rankClass = i === 0 ? 'rank1' : (i < 3 ? 'rank2' : (i < 5 ? 'rank3' : ''));
    const row = document.createElement('div');
    row.className = 'freq-row';
    row.innerHTML = `
      <div class="freq-label">${d.label}</div>
      <div class="freq-bar-wrap">
        <div class="freq-bar ${rankClass}" style="width:0%" data-target="${pct}%">
          <span>${d.count}/6年</span>
        </div>
      </div>`;
    container.appendChild(row);
  });
  // Animate
  setTimeout(() => {
    document.querySelectorAll('.freq-bar[data-target]').forEach(bar => {
      bar.style.width = bar.dataset.target;
    });
  }, 300);
}

// ═══════════════════════════════════════════════
// BUILD MCQ CARDS
// ═══════════════════════════════════════════════
function buildMCQ(paperKey, mcqData) {
  const g1 = document.getElementById(`${paperKey}-mcq-group1`);
  const g2 = document.getElementById(`${paperKey}-mcq-group2`);
  const g3 = document.getElementById(`${paperKey}-mcq-group3`);

  mcqData.forEach(q => {
    const container = q.g === 'A' ? g1 : (q.g === 'B' ? g2 : g3);
    const srcClass = q.src.includes('预测') ? 'src-predict' : (q.src.includes('2025') || q.src.includes('2024') ? 'src-A' : 'src-B');

    const card = document.createElement('div');
    card.className = 'q-card';
    card.id = `${paperKey}-q${q.id}`;

    const optionsHtml = Object.entries(q.opts).map(([k, v]) => `
      <div class="q-opt" id="${paperKey}-q${q.id}-opt${k}" onclick="selectOpt('${paperKey}',${q.id},'${k}')">
        <div class="opt-letter">${k}</div>
        <div>${v}</div>
      </div>`).join('');

    card.innerHTML = `
      <div class="q-header">
        <div class="q-num" id="${paperKey}-q${q.id}-num">${q.id}</div>
        <div style="flex:1">
          <div class="q-meta-row">
            <span class="q-source-tag ${srcClass}">【${q.src}】</span>
            <span class="q-source-tag" style="background:rgba(${q.g==='A'?'139,58,26':q.g==='B'?'26,74,107':'26,90,42'},0.2)">
              ${q.g==='A'?'甲组·烘焙':q.g==='B'?'乙组·西餐':'丙组·亚洲'}
            </span>
          </div>
        </div>
      </div>
      <div class="q-stem">${q.q}</div>
      <div class="q-options">${optionsHtml}</div>
      <div class="q-explain" id="${paperKey}-q${q.id}-exp">
        <div class="explain-title">💡 统考考点解析</div>
        ${q.exp}
      </div>`;
    container.appendChild(card);
  });
}

// ═══════════════════════════════════════════════
// SELECT OPTION HANDLER
// ═══════════════════════════════════════════════
function selectOpt(paper, qid, optKey) {
  const s = state[paper];
  if (s.submitted) return;
  const q = (paper==='A'?paperA_mcq:paperB_mcq).find(x=>x.id===qid);
  if (!q) return;

  if (s.mode === 'practice') {
    // Immediate reveal
    const correct = q.ans;
    s.answers[qid] = optKey;

    ['A','B','C','D'].forEach(k => {
      const el = document.getElementById(`${paper}-q${qid}-opt${k}`);
      if (!el) return;
      el.classList.remove('selected','correct-opt','wrong-opt');
      el.classList.add('disabled');
      if (k === correct) el.classList.add('correct-opt');
      else if (k === optKey && optKey !== correct) el.classList.add('wrong-opt');
    });

    const card = document.getElementById(`${paper}-q${qid}`);
    const numEl = document.getElementById(`${paper}-q${qid}-num`);
    card.classList.remove('answered-correct','answered-wrong');
    if (optKey === correct) { card.classList.add('answered-correct'); numEl.classList.add('correct-num'); }
    else { card.classList.add('answered-wrong'); numEl.classList.add('wrong-num'); }

    document.getElementById(`${paper}-q${qid}-exp`).classList.add('visible');
    updateProgress(paper);
  } else {
    // Exam mode: just mark selection
    const prev = s.answers[qid];
    if (prev) {
      const prevEl = document.getElementById(`${paper}-q${qid}-opt${prev}`);
      if (prevEl) prevEl.classList.remove('selected');
    }
    s.answers[qid] = optKey;
    const el = document.getElementById(`${paper}-q${qid}-opt${optKey}`);
    if (el) el.classList.add('selected');
    updateProgress(paper);
  }
}

// ═══════════════════════════════════════════════
// PROGRESS
// ═══════════════════════════════════════════════
function updateProgress(paper) {
  const s = state[paper];
  const total = 60;
  const answered = Object.keys(s.answers).length;
  const pct = Math.round(answered / total * 100);
  document.getElementById(`progress${paper}`).style.width = pct + '%';
  document.getElementById(`progressLabel${paper}`).textContent = `答题进度：${answered} / ${total}`;
}

// ═══════════════════════════════════════════════
// MODE TOGGLE
// ═══════════════════════════════════════════════
function setMode(paper, mode) {
  const s = state[paper];
  s.mode = mode;
  s.answers = {};
  s.submitted = false;

  // Reset UI
  ['A','B','C','D'].forEach(k => {
    const mcq = paper==='A'?paperA_mcq:paperB_mcq;
    mcq.forEach(q => {
      const opt = document.getElementById(`${paper}-q${q.id}-opt${k}`);
      if (opt) { opt.classList.remove('selected','correct-opt','wrong-opt','disabled'); }
    });
    (paper==='A'?paperA_mcq:paperB_mcq).forEach(q => {
      const card = document.getElementById(`${paper}-q${q.id}`);
      if (card) { card.classList.remove('answered-correct','answered-wrong'); }
      const num = document.getElementById(`${paper}-q${q.id}-num`);
      if (num) { num.classList.remove('correct-num','wrong-num'); }
      const exp = document.getElementById(`${paper}-q${q.id}-exp`);
      if (exp) { exp.classList.remove('visible'); }
    });
  });

  updateProgress(paper);
  document.getElementById(`scoreBoard${paper}`).classList.remove('visible');

  const practiceBtn = document.getElementById(`mode${paper}-practice`);
  const examBtn = document.getElementById(`mode${paper}-exam`);
  const submitBtn = document.getElementById(`submit${paper}`);
  const timerEl = document.getElementById(`timer${paper}`);

  practiceBtn.classList.toggle('active', mode==='practice');
  examBtn.classList.toggle('active', mode==='exam');
  submitBtn.style.display = mode==='exam' ? 'block' : 'none';

  if (s.timerInterval) { clearInterval(s.timerInterval); s.timerInterval = null; }

  if (mode === 'exam') {
    s.timeLeft = 80*60;
    timerEl.classList.add('active');
    updateTimerDisplay(paper);
    s.timerInterval = setInterval(() => {
      s.timeLeft--;
      updateTimerDisplay(paper);
      if (s.timeLeft <= 0) { clearInterval(s.timerInterval); submitPaper(paper); }
      if (s.timeLeft <= 300) timerEl.classList.add('urgent');
    }, 1000);
  } else {
    timerEl.classList.remove('active','urgent');
  }
}

function updateTimerDisplay(paper) {
  const t = state[paper].timeLeft;
  const m = Math.floor(t/60).toString().padStart(2,'0');
  const s2 = (t%60).toString().padStart(2,'0');
  document.getElementById(`timer${paper}-text`).textContent = `${m}:${s2}`;
}

// ═══════════════════════════════════════════════
// SUBMIT PAPER (EXAM MODE)
// ═══════════════════════════════════════════════
function submitPaper(paper) {
  const s = state[paper];
  if (s.submitted) return;
  s.submitted = true;

  if (s.timerInterval) { clearInterval(s.timerInterval); s.timerInterval=null; }
  document.getElementById(`timer${paper}`).classList.remove('active','urgent');
  document.getElementById(`submit${paper}`).style.display = 'none';

  const mcq = paper==='A'?paperA_mcq:paperB_mcq;
  let totalScore=0, g1=0, g2=0, g3=0;

  mcq.forEach(q => {
    const userAns = s.answers[q.id];
    const correct = q.ans;
    const isCorrect = userAns === correct;
    if (isCorrect) {
      totalScore++;
      if (q.g==='A') g1++;
      else if (q.g==='B') g2++;
      else g3++;
    }

    // Reveal answers
    ['A','B','C','D'].forEach(k => {
      const el = document.getElementById(`${paper}-q${q.id}-opt${k}`);
      if (!el) return;
      el.classList.remove('selected');
      el.classList.add('disabled');
      if (k===correct) el.classList.add('correct-opt');
      else if (k===userAns && userAns!==correct) el.classList.add('wrong-opt');
    });
    const card = document.getElementById(`${paper}-q${q.id}`);
    const num = document.getElementById(`${paper}-q${q.id}-num`);
    if (card) card.classList.add(isCorrect?'answered-correct':'answered-wrong');
    if (num) num.classList.add(isCorrect?'correct-num':'wrong-num');
    const exp = document.getElementById(`${paper}-q${q.id}-exp`);
    if (exp) exp.classList.add('visible');
  });

  // Show scores
  const board = document.getElementById(`scoreBoard${paper}`);
  board.classList.add('visible');
  document.getElementById(`totalScore${paper}`).textContent = totalScore;
  document.getElementById(`score${paper}-g1`).textContent = g1;
  document.getElementById(`score${paper}-g2`).textContent = g2;
  document.getElementById(`score${paper}-g3`).textContent = g3;
  board.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ═══════════════════════════════════════════════
// BUILD WRITTEN QUESTIONS
// ═══════════════════════════════════════════════
function buildWritten(paperId, writtenData) {
  const container = document.getElementById(`${paperId}-written`);

  writtenData.forEach(section => {
    const sectionEl = document.createElement('div');
    sectionEl.style.marginBottom = '24px';

    if (section.type === 'mandatory') {
      const card = buildWrittenCard(section, paperId);
      sectionEl.appendChild(card);
    } else {
      // Optional group header
      const grpHeader = document.createElement('div');
      grpHeader.className = 'exam-section-hdr';
      grpHeader.style.background = 'rgba(80,40,10,0.1)';
      grpHeader.style.borderColor = '#6a4010';
      grpHeader.style.color = '#c0a060';
      grpHeader.innerHTML = `${section.label} <span class="section-tag" style="color:#c0a060">请选答3题</span>`;
      sectionEl.appendChild(grpHeader);

      section.questions.forEach(q => {
        const card = buildWrittenCard(q, paperId, true);
        sectionEl.appendChild(card);
      });
    }

    container.appendChild(sectionEl);
  });
}

function buildWrittenCard(q, paperId, isOptional=false) {
  const card = document.createElement('div');
  card.className = 'written-section';
  card.id = `${paperId}-written-${q.id}`;

  const optLabel = isOptional ? `<span style="font-size:11px;color:#c0a060;margin-left:8px;">[选答]</span>` : `<span style="font-size:11px;color:#e8a030;margin-left:8px;">[必答]</span>`;

  let bodyHtml = `<div class="written-stem">${q.stem}</div>`;

  // Subquestions if any
  if (q.subqs) {
    q.subqs.forEach(sub => {
      bodyHtml += `<div class="written-sub">
        <div class="sub-label">${sub.label}</div>
        <div class="sub-text">${sub.text}</div>`;
      if (sub.table) {
        bodyHtml += `<table class="baking-table">
          <thead><tr><th>材料名称</th><th>烘焙百分比 (%)</th><th>重量 (g)</th></tr></thead>
          <tbody>`;
        sub.table.forEach(row => {
          const isTot = row.m === '合计';
          bodyHtml += `<tr${isTot?' class="total"':''}><td>${row.m}</td><td>${row.p}</td><td>${row.w}</td></tr>`;
        });
        bodyHtml += `</tbody></table>`;
      }
      bodyHtml += `</div>`;
    });
  }

  // Answer reveal
  const answerId = `${paperId}-ans-${q.id}`;
  bodyHtml += `
    <button class="reveal-btn" onclick="revealAnswer('${answerId}')">
      🔍 点击查看参考答案
    </button>
    <div class="answer-box" id="${answerId}">
      <span class="answer-label">✅ 参考答案与评分要点</span>
      ${(q.answer||'').replace(/\n/g,'<br>')}
    </div>`;

  card.innerHTML = `
    <div class="written-header">
      题目 ${q.id || ''}${optLabel}
    </div>
    <div class="written-body">${bodyHtml}</div>`;

  return card;
}

function revealAnswer(id) {
  const el = document.getElementById(id);
  if (!el) return;
  el.classList.toggle('visible');
  const btn = el.previousElementSibling;
  if (btn) btn.textContent = el.classList.contains('visible') ? '🔒 收起参考答案' : '🔍 点击查看参考答案';
}

// ═══════════════════════════════════════════════
// TAB SWITCH
// ═══════════════════════════════════════════════
function switchTab(paper) {
  document.getElementById('panelA').classList.remove('active');
  document.getElementById('panelB').classList.remove('active');
  document.getElementById(`panel${paper}`).classList.add('active');

  document.querySelectorAll('.paper-tab').forEach(t => {
    t.classList.remove('active-A','active-B');
  });
  const tabs = document.querySelectorAll('.paper-tab');
  if (paper==='A') tabs[0].classList.add('active-A');
  else tabs[1].classList.add('active-B');
}

// ═══════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  buildFreqChart();
  buildMCQ('A', paperA_mcq);
  buildMCQ('B', paperB_mcq);
  buildWritten('A', paperA_written);
  buildWritten('B', paperB_written);
});
</script>
</body>
</html>"""

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"SUCCESS: HTML file written to:")
print(OUTPUT_FILE)
import os
size = os.path.getsize(OUTPUT_FILE)
print(f"File size: {size:,} bytes ({size//1024} KB)")
