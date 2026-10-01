import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

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

if '<footer class="system-footer">' not in content:
    content = content.replace('</main>', footer_html + '\n  </main>')

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer HTML successfully inserted!")
