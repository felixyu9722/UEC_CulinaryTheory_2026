import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

template_path = r'c:\Users\GOH\Desktop\2026年统考厨艺理论\work\template.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for difficulty filter bar
css_to_add = """
    /* Difficulty Filter Bar */
    .difficulty-filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 22px;
      background: #F8FAFC;
      padding: 10px 14px;
      border-radius: 14px;
      border: 1.5px solid #E2E8F0;
      align-items: center;
    }
    .diff-tab-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: 20px;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      border: 1.5px solid #CBD5E1;
      background: white;
      color: #475569;
      transition: all 0.2s ease;
      user-select: none;
    }
    .diff-tab-btn:hover {
      border-color: #94A3B8;
      background: #F1F5F9;
      transform: translateY(-1px);
    }
    .diff-tab-btn.active {
      border-color: #2563EB;
      background: #EFF6FF;
      color: #1D4ED8;
      box-shadow: 0 2px 4px rgba(37, 99, 235, 0.12);
    }
    .diff-tab-btn.easy.active {
      border-color: #16A34A;
      background: #DCFCE7;
      color: #15803D;
      box-shadow: 0 2px 4px rgba(22, 163, 74, 0.15);
    }
    .diff-tab-btn.medium.active {
      border-color: #D97706;
      background: #FEF3C7;
      color: #B45309;
      box-shadow: 0 2px 4px rgba(217, 119, 6, 0.15);
    }
    .diff-tab-btn.hard.active {
      border-color: #DC2626;
      background: #FEE2E2;
      color: #B91C1C;
      box-shadow: 0 2px 4px rgba(220, 38, 38, 0.15);
    }
    .diff-tab-btn.mistakes.active {
      border-color: #9333EA;
      background: #F3E8FF;
      color: #7E22CE;
      box-shadow: 0 2px 4px rgba(147, 51, 234, 0.15);
    }
    .diff-tab-btn .badge-pill {
      font-size: 0.78rem;
      padding: 1px 7px;
      border-radius: 10px;
      background: rgba(0,0,0,0.06);
      font-weight: 700;
    }
"""

if '.difficulty-filter-bar' not in content:
    content = content.replace('.control-panel {', css_to_add + '\n    .control-panel {')

# 2. Add HTML for difficulty filter bar right after </div class="control-panel">
bar_html = """
    <!-- Difficulty & Mistakes Fast Filter Bar -->
    <div class="difficulty-filter-bar">
      <span style="font-size:0.85rem; font-weight:700; color:#64748B; margin-right:4px;">🎯 题库模式：</span>
      <button class="diff-tab-btn active" id="tabAll" onclick="setDiffFilter('all')">
        <span>🔘 全部题目</span>
        <span class="badge-pill" id="badgeAll">800</span>
      </button>
      <button class="diff-tab-btn easy" id="tabEasy" onclick="setDiffFilter('easy')">
        <span>🟢 纯容易基础题</span>
        <span class="badge-pill" id="badgeEasy">400</span>
      </button>
      <button class="diff-tab-btn medium" id="tabMed" onclick="setDiffFilter('medium')">
        <span>🟡 中等实务应用</span>
        <span class="badge-pill" id="badgeMed">300</span>
      </button>
      <button class="diff-tab-btn hard" id="tabHard" onclick="setDiffFilter('hard')">
        <span>🔴 统考拔高变式</span>
        <span class="badge-pill" id="badgeHard">100</span>
      </button>
      <button class="diff-tab-btn mistakes" id="tabMistakes" onclick="setDiffFilter('mistakes')">
        <span>❌ 我的错题本</span>
        <span class="badge-pill" id="badgeMistakes">0</span>
      </button>
    </div>
"""

target_after_panel = '<!-- Questions Container -->'
if 'difficulty-filter-bar' not in content:
    content = content.replace(target_after_panel, bar_html + '\n    ' + target_after_panel)

# 3. Add JS state and filter logic
# Find "let currentFilter = 'all';"
js_state_old = "let currentFilter = 'all';"
js_state_new = """let currentFilter = 'all';
    let currentDifficulty = 'all'; // 'all', 'easy', 'medium', 'hard', 'mistakes'"""

if "let currentDifficulty = 'all';" not in content:
    content = content.replace(js_state_old, js_state_new)

# Update filter function inside render()
old_filter_block = """      let filtered = allQuestions.filter(q => {
        // Filter by Chapter or Mistakes
        if (currentFilter === 'mistakes') {
          const rec = userAnswers[q.uid];
          if (!rec || rec.correct) return false;
        } else if (currentFilter !== 'all') {
          if (q.chapter_id != currentFilter) return false;
        }

        // Search query
        if (searchQuery.trim() !== '') {
          const qText = (q.question + q.options.A + q.options.B + q.options.C + q.options.D + q.explanation).toLowerCase();
          if (!qText.includes(searchQuery.toLowerCase())) return false;
        }

        return true;
      });"""

new_filter_block = """      let filtered = allQuestions.filter(q => {
        // Filter by Chapter
        if (currentFilter !== 'all') {
          if (q.chapter_id != currentFilter) return false;
        }

        // Filter by Difficulty or Mistakes
        if (currentDifficulty === 'mistakes') {
          const rec = userAnswers[q.uid];
          if (!rec || rec.correct) return false;
        } else if (currentDifficulty === 'easy') {
          if (q.difficulty !== 'easy') return false;
        } else if (currentDifficulty === 'medium') {
          if (q.difficulty !== 'medium') return false;
        } else if (currentDifficulty === 'hard') {
          if (q.difficulty !== 'hard') return false;
        }

        // Search query
        if (searchQuery.trim() !== '') {
          const qText = (q.question + q.options.A + q.options.B + q.options.C + q.options.D + q.explanation).toLowerCase();
          if (!qText.includes(searchQuery.toLowerCase())) return false;
        }

        return true;
      });"""

content = content.replace(old_filter_block, new_filter_block)

# Add setDiffFilter and updateDiffCounts functions
js_diff_funcs = """
    function setDiffFilter(diff) {
      currentDifficulty = diff;
      document.querySelectorAll('.diff-tab-btn').forEach(btn => btn.classList.remove('active'));
      if (diff === 'all') document.getElementById('tabAll').classList.add('active');
      else if (diff === 'easy') document.getElementById('tabEasy').classList.add('active');
      else if (diff === 'medium') document.getElementById('tabMed').classList.add('active');
      else if (diff === 'hard') document.getElementById('tabHard').classList.add('active');
      else if (diff === 'mistakes') document.getElementById('tabMistakes').classList.add('active');
      render();
    }

    function updateDiffCounts() {
      // Base questions by current chapter filter
      let base = allQuestions;
      if (currentFilter !== 'all') {
        base = allQuestions.filter(q => q.chapter_id == currentFilter);
      }
      const countAll = base.length;
      const countEasy = base.filter(q => q.difficulty === 'easy').length;
      const countMed = base.filter(q => q.difficulty === 'medium').length;
      const countHard = base.filter(q => q.difficulty === 'hard').length;
      const countMistakes = base.filter(q => {
        const rec = userAnswers[q.uid];
        return rec && !rec.correct;
      }).length;

      const elAll = document.getElementById('badgeAll');
      const elEasy = document.getElementById('badgeEasy');
      const elMed = document.getElementById('badgeMed');
      const elHard = document.getElementById('badgeHard');
      const elMistakes = document.getElementById('badgeMistakes');

      if (elAll) elAll.textContent = countAll;
      if (elEasy) elEasy.textContent = countEasy;
      if (elMed) elMed.textContent = countMed;
      if (elHard) elHard.textContent = countHard;
      if (elMistakes) elMistakes.textContent = countMistakes;
    }
"""

if 'function setDiffFilter' not in content:
    # Insert right before render()
    content = content.replace('function render() {', js_diff_funcs + '\n    function render() {')

# Hook updateDiffCounts() into render() and init
if 'updateDiffCounts();' not in content:
    content = content.replace('updateHUD();', 'updateHUD();\n      updateDiffCounts();')

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("template.html updated successfully with Difficulty Filtering!")
