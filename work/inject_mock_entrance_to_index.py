import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS for mock-exam-portal-card before </style>
css_to_add = """
    /* Mock Exam Portal Banner Card on Portal Screen */
    .mock-exam-portal-card {
      width: 100%;
      max-width: 1060px;
      margin: 0 auto 30px auto;
      background: #FFFFFF;
      border: 2px solid #FCD34D;
      border-left: 8px solid #D97706;
      border-radius: 20px;
      padding: 24px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04);
      cursor: pointer;
      transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .mock-exam-portal-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 32px rgba(120, 53, 15, 0.12);
      border-color: #92400E;
    }
    .mep-left {
      flex: 1;
    }
    .mep-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 9999px;
      background: #FEF3C7;
      color: #92400E;
      margin-bottom: 10px;
    }
    .mep-title {
      font-size: 1.45rem;
      font-weight: 800;
      color: #1E293B;
      margin-bottom: 8px;
      line-height: 1.3;
    }
    .mep-desc {
      font-size: 0.92rem;
      color: #64748B;
      line-height: 1.6;
      margin-bottom: 12px;
    }
    .mep-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .mep-tags span {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      color: #475569;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 3px 10px;
      border-radius: 6px;
    }
    .mep-right {
      flex-shrink: 0;
    }
    .mep-action-btn {
      background: linear-gradient(135deg, #78350F, #92400E);
      color: #FFFFFF;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 14px 24px;
      border-radius: 12px;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(120, 53, 15, 0.25);
      transition: all 0.2s ease;
      cursor: pointer;
    }
    .mock-exam-portal-card:hover .mep-action-btn {
      background: linear-gradient(135deg, #92400E, #B45309);
      transform: scale(1.02);
    }
    @media (max-width: 860px) {
      .mock-exam-portal-card {
        flex-direction: column;
        align-items: flex-start;
      }
      .mep-right {
        width: 100%;
      }
      .mep-action-btn {
        width: 100%;
        justify-content: center;
      }
    }
"""

if 'mock-exam-portal-card' not in text:
    text = text.replace('</style>', css_to_add + '\n</style>', 1)

# 2. Add the mock-exam-portal-card right after </div> <!-- end of grade-cards-grid -->
card_html = """
      <!-- 历届全真模拟考场专属入口卡片 (双卷全真模考系统) -->
      <div class="mock-exam-portal-card" onclick="window.location.href='模拟考场主页.html'">
        <div class="mep-left">
          <div class="mep-badge">🔥 2026 统考冲刺首选 · 历届全真模考系统</div>
          <h2 class="mep-title">🏛️ 历届全真模拟考场 · 双卷全真模考系统</h2>
          <p class="mep-desc">基于 2020~2025 年六届真实统考大数据深度剖析，提供【模拟卷 A · 历届高频真题精选卷】与【模拟卷 B · 2026前瞻预测试题卷】。配备试卷一（60题选择题即查/模考计时双模式）与试卷二（综合题参考答案及教师评分细则深度解密）。</p>
          <div class="mep-tags">
            <span>📊 历届大数据图表分析</span>
            <span>📄 模拟卷 A (60题+作答题)</span>
            <span>🔮 模拟卷 B (60题+作答题)</span>
            <span>⏱️ 80分钟全真倒计时</span>
            <span>💡 评分细则全解</span>
          </div>
        </div>
        <div class="mep-right">
          <div class="mep-action-btn">🚀 进入历届全真模拟考场 →</div>
        </div>
      </div>
"""

target_end_grid = """          <button class="grade-action-btn btn-active">🚀 进入高三练习 (320题)</button>
        </div>
      </div>
    </div>"""

if target_end_grid in text and 'mock-exam-portal-card' not in text:
    text = text.replace(target_end_grid, target_end_grid + '\n' + card_html, 1)
elif 'mock-exam-portal-card' in text and '🏛️ 历届全真模拟考场' not in text:
    # If css was added, now add HTML
    text = text.replace(target_end_grid, target_end_grid + '\n' + card_html, 1)

# 3. Add quick access in header nav-right
target_nav = '<button class="portal-switch-btn" onclick="showPortal()"'
nav_btn = '<a href="模拟考场主页.html" class="portal-switch-btn" style="text-decoration:none;background:#FEF3C7;color:#92400E;border-color:#FDE68A;" title="打开历届全真模拟考场">🏛️ 历届模考</a>\n        '
if nav_btn.strip() not in text and target_nav in text:
    text = text.replace(target_nav, nav_btn + target_nav, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Injected entrance into index.html successfully!')
