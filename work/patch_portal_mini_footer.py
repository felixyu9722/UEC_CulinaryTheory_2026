import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add CSS for portal-mini-footer
mini_css = """
    /* Portal Mini Footer (Clean, Small, Elegant) */
    .portal-mini-footer {
      margin-top: 26px;
      padding-top: 18px;
      border-top: 1px solid #E2E8F0;
      text-align: center;
      color: #64748B;
      font-size: 0.8rem;
      line-height: 1.6;
    }
    .mini-copy-text {
      font-weight: 600;
      color: #334155;
      margin-bottom: 4px;
      font-size: 0.82rem;
    }
    .mini-sub-text {
      color: #64748B;
      font-size: 0.76rem;
      margin-bottom: 10px;
      opacity: 0.9;
    }
    .mini-version-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 6px;
      font-size: 0.72rem;
    }
    .mini-pill {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: 12px;
      background: #F1F5F9;
      color: #475569;
      font-weight: 500;
      border: 1px solid #E2E8F0;
    }
"""

if '.portal-mini-footer' not in text:
    text = text.replace('.portal-card {', mini_css + '\n    .portal-card {')

# 2. Add mini-footer right after the grades-grid closing div inside portal-card
portal_mini_html = """
      <!-- 首页开头底部·简短小字版权与版本条 -->
      <div class="portal-mini-footer">
        <div class="mini-copy-text">
          ⚖️ <strong>版权保护声明</strong>：© 2026 尤老师 ｜ 亚罗士打新民独中 ｜ 互动答题总系统
        </div>
        <div class="mini-sub-text">
          欢迎分享本网页链接供学习使用；未经许可，不得复制、转载网页内的文字、题目及答案，不得公开发布于其他网站，亦不得用于商业销售。
        </div>
        <div class="mini-version-pills">
          <span class="mini-pill">🏷️ v2026.10-Build.01</span>
          <span class="mini-pill">📅 2026年10月统考真题对齐版</span>
          <span class="mini-pill">💾 手机离线进度自动保存</span>
        </div>
      </div>
"""

# Target insertion: right after </div> that closes grades-grid
# Look for:
#           <button class="grade-action-btn btn-secondary">进入高三专属题库</button>
#         </div>
#       </div>

target_anchor = '<button class="grade-action-btn btn-secondary">进入高三专属题库</button>\n        </div>\n      </div>'

if 'portal-mini-footer' not in text:
    if target_anchor in text:
        text = text.replace(target_anchor, target_anchor + '\n' + portal_mini_html)
        print("Inserted via target_anchor!")
    else:
        # Regex replacement
        pattern = r'(<button class="grade-action-btn btn-secondary">进入高三专属题库</button>\s*</div>\s*</div>)'
        text = re.sub(pattern, r'\1' + '\n' + portal_mini_html, text)
        print("Inserted via regex!")

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Template updated with Portal Mini Footer!")
