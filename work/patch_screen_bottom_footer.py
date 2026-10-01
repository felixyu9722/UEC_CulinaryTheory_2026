import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove any previous mini-footer placed inside grade-card or elsewhere
pattern_remove_old = r'<div class="portal-mini-footer">.*?</div>\s*</div>'
text = re.sub(pattern_remove_old, '</div>', text, flags=re.DOTALL)

# Also check for any standalone portal-mini-footer
pattern_standalone = r'<div class="portal-mini-footer">.*?</div>\s*'
text = re.sub(pattern_standalone, '', text, flags=re.DOTALL)

# 2. Add ultra-tiny, centered, italic CSS for screen-level footer
ultra_tiny_css = """
    /* Ultra-tiny Screen Level Footer (Centered, Super Small, Italic, Minimalist) */
    .portal-screen-footer {
      text-align: center;
      margin-top: 36px;
      padding-top: 14px;
      border-top: 1px dashed rgba(148, 163, 184, 0.35);
      color: #94A3B8;
      font-size: 0.60rem;
      font-style: italic;
      line-height: 1.6;
      user-select: none;
    }
    .portal-screen-footer .tiny-line-1 {
      font-size: 0.62rem;
      color: #64748B;
      margin-bottom: 2px;
    }
    .portal-screen-footer .tiny-line-2 {
      font-size: 0.58rem;
      color: #94A3B8;
      opacity: 0.9;
    }
    .portal-screen-footer .tiny-ver {
      font-style: normal;
      color: #3B82F6;
      font-weight: 600;
      margin-left: 6px;
      background: rgba(59, 130, 246, 0.08);
      padding: 0 5px;
      border-radius: 6px;
    }
"""

# Replace old .portal-mini-footer CSS
old_css_pattern = r'/\* Portal Mini Footer.*?\n    \.portal-card \{'
if re.search(old_css_pattern, text, re.DOTALL):
    text = re.sub(old_css_pattern, ultra_tiny_css + '\n    .portal-card {', text, flags=re.DOTALL)
else:
    text = text.replace('.portal-container {', ultra_tiny_css + '\n    .portal-container {')

# 3. Add the ultra-tiny footer right after </div> of grade-cards-grid inside portal-container
footer_ultra_tiny_html = """
      <!-- 整个画面的底部中间·极小字斜体版权条 -->
      <div class="portal-screen-footer">
        <div class="tiny-line-1">
          ⚖️ 版权保护声明：© 2026 尤老师 ｜ 亚罗士打新民独中 ｜ 互动答题总系统
          <span class="tiny-ver">v2026.10-Build.01</span>
        </div>
        <div class="tiny-line-2">
          欢迎分享本网页链接供学习使用；未经许可，不得复制、转载网页内的文字、题目及答案，不得公开发布于其他网站，亦不得用于商业销售。
        </div>
      </div>
"""

# Look for the end of grade-cards-grid:
# Look for </button>\s*</div>\s*</div>\s*</div>\s*</div>\s*<header>
# Or locate <button class="grade-action-btn btn-secondary">进入高三专属题库</button>
target_end_anchor = """<button class="grade-action-btn btn-secondary">进入高三专属题库</button>
        </div>
      </div>"""

if target_end_anchor in text:
    text = text.replace(target_end_anchor, target_end_anchor + '\n' + footer_ultra_tiny_html)
    print("Inserted ultra-tiny footer right after grade-cards-grid!")
else:
    # Try regex
    pattern_cards_end = r'(<button class="grade-action-btn btn-secondary">进入高三专属题库</button>\s*</div>\s*</div>)'
    text = re.sub(pattern_cards_end, r'\1\n' + footer_ultra_tiny_html, text)
    print("Inserted ultra-tiny footer via regex!")

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Template updated successfully with Ultra-Tiny, Centered, Italic Screen-Bottom Footer!")
