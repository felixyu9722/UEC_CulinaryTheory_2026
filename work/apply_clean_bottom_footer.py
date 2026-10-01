import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean out all old system-footer CSS and old portal-screen-footer CSS
pattern_sys_footer_css = r'/\* Modern Legal & Version Footer \*/\s*\.system-footer\s*\{.*?\.\s*f-badge\.storage\s*\{[^}]*\}\s*'
text = re.sub(pattern_sys_footer_css, '', text, flags=re.DOTALL)

# Also check for any remaining .system-footer or .footer-inner CSS
text = re.sub(r'\.system-footer\s*\{[^}]*\}', '', text)
text = re.sub(r'\.footer-inner\s*\{[^}]*\}', '', text)
text = re.sub(r'\.footer-header[^{]*\{[^}]*\}', '', text)
text = re.sub(r'\.footer-body[^{]*\{[^}]*\}', '', text)
text = re.sub(r'\.footer-badges\s*\{[^}]*\}', '', text)
text = re.sub(r'\.f-badge[^{]*\{[^}]*\}', '', text)

# Remove any old portal-screen-footer CSS
pattern_old_screen_footer_css = r'/\* Ultra-tiny Screen Level Footer.*?\n    \.portal-container \{'
text = re.sub(pattern_old_screen_footer_css, '.portal-container {', text, flags=re.DOTALL)

# 2. Add brand-new Ultra-Tiny, Centered, Italic Footer CSS right before .portal-container
ultra_tiny_footer_css = """
    /* Ultra-tiny Screen Level Footer (Centered, Super Small, Italic, Minimalist) */
    .portal-screen-footer {
      width: 100%;
      text-align: center;
      margin: auto auto 0 auto;
      padding: 14px 10px 8px;
      color: #94A3B8;
      font-size: 0.50rem;
      font-style: italic;
      line-height: 1.5;
      user-select: none;
    }
    .portal-screen-footer .tiny-line-1 {
      font-size: 0.52rem;
      color: #64748B;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .portal-screen-footer .tiny-line-2 {
      font-size: 0.48rem;
      color: #94A3B8;
      letter-spacing: 0.1px;
    }
    .portal-screen-footer .tiny-ver {
      font-style: normal;
      color: #2563EB;
      font-weight: 600;
      background: rgba(37, 99, 235, 0.08);
      padding: 0 5px;
      border-radius: 4px;
    }
"""

text = text.replace('.portal-container {', ultra_tiny_footer_css + '\n    .portal-container {')

# Adjust .portal-screen to ensure flex column with space-between so footer pins to absolute bottom
portal_screen_old = """.portal-screen {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 50% 20%, #FFFDF9 0%, #F5EBE1 100%);
      z-index: 1000;
      overflow-y: auto;
      padding: 40px 20px 60px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: opacity 0.3s ease, visibility 0.3s ease;
    }"""

portal_screen_new = """.portal-screen {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at 50% 20%, #FFFDF9 0%, #F5EBE1 100%);
      z-index: 1000;
      overflow-y: auto;
      padding: 28px 20px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      transition: opacity 0.3s ease, visibility 0.3s ease;
      box-sizing: border-box;
    }"""

if portal_screen_old in text:
    text = text.replace(portal_screen_old, portal_screen_new)
else:
    # Use regex
    text = re.sub(r'\.portal-screen\s*\{[^}]*\}', portal_screen_new, text)

# Adjust .portal-container
portal_container_old = """.portal-container {
      max-width: 1160px;
      width: 100%;
      margin: 0 auto;
    }"""
portal_container_new = """.portal-container {
      max-width: 1160px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      flex: 1 0 auto;
      justify-content: center;
    }"""
text = text.replace(portal_container_old, portal_container_new)

# 3. Clean and fix the HTML of #gradePortal
portal_html_pattern = r'<div id="gradePortal" class="portal-screen">.*?<header>'
# Let's inspect what's inside
match = re.search(portal_html_pattern, text, re.DOTALL)
if match:
    # Rebuild cleanly
    # Extract the cards from match
    portal_content = match.group(0)
    cards_match = re.search(r'(<div class="grade-cards-grid">.*?</div>\s*</div>\s*</div>)', portal_content, re.DOTALL)
    
portal_clean_html = """  <!-- Grade Selection Portal Screen (登录与年段选择门户) -->
  <div id="gradePortal" class="portal-screen">
    <div class="portal-container">
      <div class="portal-hero">
        <div class="portal-badge">2026 马来西亚华文独中高中统考（UEC）</div>
        <h1 class="portal-title">高中厨艺（烘焙理论）互动答题总系统</h1>
        <p class="portal-desc">全套校内考点与统考大纲精选试题库 · 智能评分与机理解析系统</p>
      </div>

      <div class="grade-cards-grid">
        <!-- Grade 1: Senior 1 -->
        <div class="grade-card ready" onclick="selectGrade('senior1')">
          <div class="card-status-badge badge-ready">🟢 800题已就绪 · 立即练习</div>
          <div class="card-icon">🥐</div>
          <div class="grade-num">01 | 高一年级</div>
          <h2 class="grade-name">烘焙基础理论</h2>
          <div class="grade-tags">
            <span>全20课</span>
            <span>800道精选</span>
            <span>生活常识与校内测验</span>
            <span>ABCD均等分布</span>
          </div>
          <p class="grade-summary">
            覆盖烘焙概论、历史分类、器具设备、度量衡精准称量、核心原辅料（面粉/油脂/糖/蛋/乳制品/酵母）、膨大乳化作用与烘焙百分比计算。
          </p>
          <button class="grade-action-btn btn-active">🚀 进入高一练习 (800题)</button>
        </div>

        <!-- Grade 2: Senior 2 -->
        <div class="grade-card" onclick="selectGrade('senior2')">
          <div class="card-status-badge badge-pending">🟡 扩展架构已就绪 · 题库编排中</div>
          <div class="card-icon">🎂</div>
          <div class="grade-num">02 | 高二年级</div>
          <h2 class="grade-name">蛋糕、面包与西餐理论</h2>
          <div class="grade-tags">
            <span>蛋糕烘烤工艺</span>
            <span>面包发酵成型</span>
            <span>西餐基础与烹饪原理</span>
          </div>
          <p class="grade-summary">
            涵盖海绵/戚风/重油蛋糕工艺、面团直接与中种发酵法、西餐烹调法与菜肴组配标准等高二核心知识点。
          </p>
          <button class="grade-action-btn btn-secondary">进入高二专属题库</button>
        </div>

        <!-- Grade 3: Senior 3 -->
        <div class="grade-card" onclick="selectGrade('senior3')">
          <div class="card-status-badge badge-pending">🟣 扩展架构已就绪 · 题库编排中</div>
          <div class="card-icon">👨‍🍳</div>
          <div class="grade-num">03 | 高三年级</div>
          <h2 class="grade-name">西式点心、酱汁与亚洲烹调</h2>
          <div class="grade-tags">
            <span>法式点心与派塔</span>
            <span>五大经典母酱</span>
            <span>亚洲特色烹饪</span>
            <span>统考实作冲刺</span>
          </div>
          <p class="grade-summary">
            深度解析法式泡芙与酥皮折叠、经典西餐母酱调配、亚洲风味烹调工艺与独中董总总技术鉴定统考冲刺题型。
          </p>
          <button class="grade-action-btn btn-secondary">进入高三专属题库</button>
        </div>
      </div>
    </div>

    <!-- 整个画面的底部中间·极小字斜体版权条 -->
    <div class="portal-screen-footer">
      <div class="tiny-line-1">
        <span>⚖️ 版权保护声明：© 2026 尤老师 ｜ 亚罗士打新民独中 ｜ 互动答题总系统</span>
        <span class="tiny-ver">v2026.10-Build.01</span>
      </div>
      <div class="tiny-line-2">
        欢迎分享本网页链接供学习使用；未经许可，不得复制、转载网页内的文字、题目及答案，不得公开发布于其他网站，亦不得用于商业销售。
      </div>
    </div>
  </div>

  <header>"""

text = re.sub(r'<!-- Grade Selection Portal Screen.*?<header>', portal_clean_html, text, flags=re.DOTALL)

# 4. Replace .system-footer inside <main> with the exact same clean ultra-tiny italic footer
quiz_footer_html = """    <!-- 页面底部中间·极小字斜体版权条 -->
    <footer class="portal-screen-footer" style="margin: 40px auto 10px; border-top: 1px dashed rgba(148, 163, 184, 0.35); max-width: 900px;">
      <div class="tiny-line-1">
        <span>⚖️ 版权保护声明：© 2026 尤老师 ｜ 亚罗士打新民独中 ｜ 互动答题总系统</span>
        <span class="tiny-ver">v2026.10-Build.01</span>
      </div>
      <div class="tiny-line-2">
        欢迎分享本网页链接供学习使用；未经许可，不得复制、转载网页内的文字、题目及答案，不得公开发布于其他网站，亦不得用于商业销售。
      </div>
    </footer>
  </main>"""

text = re.sub(r'<!-- System Copyright.*?</footer>\s*</main>', quiz_footer_html, text, flags=re.DOTALL)

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully applied clean bottom footer to template.html!")
