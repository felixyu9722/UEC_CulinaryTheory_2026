import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the portal-mini-footer CSS to be centered, smaller, elegant and italic
new_css = """
    /* Portal Mini Footer (Centered, Small, Italic, Elegant) */
    .portal-mini-footer {
      margin: 24px auto 6px;
      padding-top: 16px;
      border-top: 1px solid #E2E8F0;
      text-align: center;
      max-width: 860px;
      color: #64748B;
      font-style: italic;
      line-height: 1.6;
    }
    .portal-mini-footer .mini-line-1 {
      font-size: 0.76rem;
      font-weight: 500;
      color: #475569;
      margin-bottom: 4px;
    }
    .portal-mini-footer .mini-line-2 {
      font-size: 0.72rem;
      color: #94A3B8;
    }
    .portal-mini-footer .mini-ver {
      display: inline-block;
      margin-left: 8px;
      font-size: 0.70rem;
      color: #3B82F6;
      font-weight: 600;
      font-style: normal;
      background: #EFF6FF;
      padding: 1px 6px;
      border-radius: 8px;
      border: 1px solid #DBEAFE;
    }
"""

# Replace old .portal-mini-footer CSS
old_css_pattern = r'/\* Portal Mini Footer.*?\n    \.portal-card \{'
text = re.sub(old_css_pattern, new_css + '\n    .portal-card {', text, flags=re.DOTALL)

# Replace the HTML of portal-mini-footer
old_html_pattern = r'<div class="portal-mini-footer">.*?</div>\s*</div>'
new_html = """<div class="portal-mini-footer">
        <div class="mini-line-1">
          ⚖️ 版权保护声明：© 2026 尤老师 ｜ 亚罗士打新民独中 ｜ 互动答题总系统
          <span class="mini-ver">v2026.10-Build.01</span>
        </div>
        <div class="mini-line-2">
          欢迎分享本网页链接供学习使用；未经许可，不得复制、转载网页内的文字、题目及答案，不得公开发布于其他网站，亦不得用于商业销售。
        </div>
      </div>
    </div>"""

text = re.sub(old_html_pattern, new_html, text, flags=re.DOTALL)

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Template updated with Centered, Small, Italic Portal Mini Footer!")
