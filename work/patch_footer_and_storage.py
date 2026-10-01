import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Footer CSS
footer_css = """
    /* Modern Legal & Version Footer */
    .system-footer {
      margin-top: 50px;
      margin-bottom: 30px;
      padding: 24px 20px;
      background: #FFFFFF;
      border-radius: 16px;
      border: 1.5px solid #E2E8F0;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    }
    .footer-inner {
      max-width: 900px;
      margin: 0 auto;
    }
    .footer-header {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.05rem;
      font-weight: 700;
      color: #1E293B;
      padding-bottom: 12px;
      border-bottom: 1px solid #F1F5F9;
      margin-bottom: 14px;
    }
    .footer-header .shield-icon {
      font-size: 1.25rem;
    }
    .footer-header .author-tag {
      color: #2563EB;
      font-weight: 800;
    }
    .footer-body {
      font-size: 0.88rem;
      color: #475569;
      line-height: 1.7;
    }
    .footer-body p {
      margin-bottom: 8px;
    }
    .footer-body strong {
      color: #1E293B;
    }
    .footer-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px dashed #E2E8F0;
    }
    .f-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.78rem;
      padding: 4px 10px;
      border-radius: 20px;
      font-weight: 600;
      user-select: none;
    }
    .f-badge.version {
      background: #EFF6FF;
      color: #1D4ED8;
      border: 1px solid #BFDBFE;
    }
    .f-badge.date {
      background: #F0FDF4;
      color: #15803D;
      border: 1px solid #BBF7D0;
    }
    .f-badge.storage {
      background: #FAF5FF;
      color: #7E22CE;
      border: 1px solid #E9D5FF;
    }
"""

if '.system-footer' not in content:
    content = content.replace('.difficulty-filter-bar {', footer_css + '\n    .difficulty-filter-bar {')

# 2. Add Footer HTML
footer_html = """
    <!-- System Copyright, Terms & Dynamic Version Footer -->
    <footer class="system-footer">
      <div class="footer-inner">
        <div class="footer-header">
          <span class="shield-icon">⚖️</span>
          <span>版权保护声明与使用规范</span>
          <span style="color:#CBD5E1;">|</span>
          <span class="author-tag">© 2026 尤老师 ｜ 亚罗士打新民独中</span>
        </div>
        <div class="footer-body">
          <p>💡 <strong>学习授权说明</strong>：本系统专为马来西亚华文独中高中厨艺科师生设计，旨在辅助董总统考（UEC）教研与日常巩固，热烈欢迎分享本网页链接供学生自主学习使用。</p>
          <p>🚫 <strong>权利保留须知</strong>：未经原作者与所属学校许可，严禁擅自抓取、批量复制或转载网页内的文字、题目、解析注释及系统源代码；严禁公开发布于其他网站或平台，亦不得用于任何形式的商业营利与课程销售。</p>
        </div>
        <div class="footer-badges">
          <span class="f-badge version">🏷️ 系统构建版本：v2026.10-Build.01</span>
          <span class="f-badge date">📅 历届真题对齐版本：2026年10月</span>
          <span class="f-badge storage">💾 答题状态：手机/本机自动记忆已激活（随时随地断点续答）</span>
        </div>
      </div>
    </footer>
"""

if 'system-footer' not in content:
    content = content.replace('</main>', footer_html + '\n  </main>')

# 3. Add localStorage persistence in JS
# On click: save to localStorage
click_save_code = """
      userAnswers[uid] = { chosen: chosenLetter, correct: isCorrect };
      try {
        localStorage.setItem('uec_quiz_answers_' + currentGrade, JSON.stringify(userAnswers));
      } catch (e) {
        console.warn('LocalStorage save failed:', e);
      }
"""
old_click_save = "userAnswers[uid] = { chosen: chosenLetter, correct: isCorrect };"
if 'uec_quiz_answers_' not in content:
    content = content.replace(old_click_save, click_save_code)

# On reset / clear: remove from localStorage
reset_code_1 = """userAnswers = {};
      try { localStorage.removeItem('uec_quiz_answers_' + currentGrade); } catch(e){}"""
if 'localStorage.removeItem' not in content:
    content = content.replace('userAnswers = {};\n      render();', reset_code_1 + '\n      render();')

# On initialization: load from localStorage
init_load_code = """
    // Load persisted user answers from localStorage on init
    try {
      const savedAnswers = localStorage.getItem('uec_quiz_answers_' + currentGrade);
      if (savedAnswers) {
        userAnswers = JSON.parse(savedAnswers);
      }
    } catch (e) {
      console.warn('LocalStorage load failed:', e);
    }
"""

if 'savedAnswers' not in content:
    # Insert right before render() call in init
    content = content.replace('render();\n      populateChapterSelect();', init_load_code + '\n      render();\n      populateChapterSelect();')

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected Footer and LocalStorage Persistence into template.html!")
