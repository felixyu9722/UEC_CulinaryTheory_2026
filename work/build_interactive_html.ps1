$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$outDir = 'C:\Users\GOH\Desktop\2026年统考厨艺理论\09_高一_第10至15课_生活常识版选择题库'

$chapters = @()
for ($ch = 10; $ch -le 15; $ch++) {
    $jsonPath = Join-Path $dataDir ('chapter' + [string]$ch + '.json')
    $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
    $data = $raw | ConvertFrom-Json
    $chapters += $data
}

$allJsonString = $chapters | ConvertTo-Json -Depth 10

$htmlTemplate = @'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2026年统考厨艺（烘焙理论）高一第10至15课·互动答题系统</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;800&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #92400E;
      --primary-light: #FDE68A;
      --primary-dark: #78350F;
      --accent: #D97706;
      --bg: #F8FAFC;
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
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --radius: 12px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Noto Sans SC', system-ui, -apple-system, sans-serif;
      background: #FDFBF7;
      color: var(--text);
      line-height: 1.6;
      padding-bottom: 80px;
    }

    /* Header & Navigation */
    header {
      background: linear-gradient(135deg, #78350F 0%, #B45309 50%, #D97706 100%);
      color: white;
      padding: 32px 24px;
      box-shadow: var(--shadow-md);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-container {
      max-width: 1000px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .header-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }

    .badge-hero {
      display: inline-block;
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(8px);
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.5px;
    }

    h1 {
      font-size: 1.75rem;
      font-weight: 800;
      letter-spacing: -0.5px;
    }

    .header-desc {
      font-size: 0.95rem;
      opacity: 0.92;
      max-width: 750px;
    }

    /* HUD Dashboard */
    .hud-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 12px;
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(10px);
      border-radius: var(--radius);
      padding: 12px 18px;
    }

    .hud-item {
      display: flex;
      flex-direction: column;
    }

    .hud-label {
      font-size: 0.78rem;
      opacity: 0.85;
      text-transform: uppercase;
      font-weight: 600;
    }

    .hud-value {
      font-family: 'Outfit', sans-serif;
      font-size: 1.4rem;
      font-weight: 700;
    }

    /* Main Container */
    main {
      max-width: 1000px;
      margin: 28px auto;
      padding: 0 16px;
    }

    /* Chapter Filter Tabs */
    .tabs-wrapper {
      display: flex;
      overflow-x: auto;
      gap: 8px;
      padding-bottom: 12px;
      margin-bottom: 20px;
      scrollbar-width: thin;
    }

    .tab-btn {
      padding: 8px 18px;
      background: white;
      border: 1px solid var(--border);
      border-radius: 9999px;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }

    .tab-btn:hover {
      border-color: var(--accent);
      color: var(--primary);
    }

    .tab-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
      box-shadow: 0 2px 8px rgba(146, 64, 14, 0.3);
    }

    /* Search and Utility Bar */
    .utility-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    .search-box {
      flex: 1;
      min-width: 240px;
      position: relative;
    }

    .search-input {
      width: 100%;
      padding: 10px 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      font-size: 0.92rem;
      outline: none;
      transition: border-color 0.2s ease;
      background: white;
    }

    .search-input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
    }

    .action-btn {
      padding: 9px 16px;
      background: white;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }

    .action-btn:hover {
      background: #F1F5F9;
    }

    /* Question Cards */
    .question-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .question-card:hover {
      box-shadow: var(--shadow-md);
    }

    .q-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
      gap: 12px;
    }

    .q-tag {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      background: #FEF3C7;
      color: #92400E;
    }

    .q-tag.roman {
      background: #EDE9FE;
      color: #6D28D9;
    }

    .q-chapter-badge {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .q-title {
      font-size: 1.08rem;
      font-weight: 600;
      line-height: 1.55;
      color: #0F172A;
      margin-bottom: 16px;
      white-space: pre-line;
    }

    /* Options List */
    .options-grid {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .option-item {
      display: flex;
      align-items: center;
      padding: 12px 16px;
      border: 1.5px solid var(--border);
      border-radius: 10px;
      background: white;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
      position: relative;
    }

    .option-item:hover:not(.locked) {
      border-color: var(--accent);
      background: #FFFBEB;
      transform: translateX(3px);
    }

    .opt-letter {
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      background: #F1F5F9;
      font-weight: 700;
      font-size: 0.88rem;
      margin-right: 12px;
      flex-shrink: 0;
      color: var(--text-muted);
      transition: all 0.2s ease;
    }

    .opt-text {
      font-size: 0.95rem;
      flex: 1;
      color: #334155;
    }

    /* Option Selected States */
    .option-item.correct {
      border-color: var(--correct);
      background: var(--correct-bg);
    }

    .option-item.correct .opt-letter {
      background: var(--correct);
      color: white;
    }

    .option-item.wrong {
      border-color: var(--wrong);
      background: var(--wrong-bg);
    }

    .option-item.wrong .opt-letter {
      background: var(--wrong);
      color: white;
    }

    .option-item.should-have-chosen {
      border-color: var(--correct);
      border-style: dashed;
      background: #F0FDF4;
    }

    .option-item.should-have-chosen .opt-letter {
      border: 2px solid var(--correct);
      color: var(--correct);
    }

    /* Explanation Drawer */
    .explanation-box {
      margin-top: 18px;
      padding: 16px 18px;
      background: #F0F9FF;
      border-left: 4px solid #0284C7;
      border-radius: 8px;
      display: none;
      animation: fadeIn 0.3s ease;
    }

    .explanation-box.show {
      display: block;
    }

    .exp-title {
      font-size: 0.9rem;
      font-weight: 700;
      color: #0369A1;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
    }

    .exp-body {
      font-size: 0.92rem;
      color: #0C4A6E;
      line-height: 1.6;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Responsive */
    @media (max-width: 640px) {
      header { padding: 20px 16px; }
      h1 { font-size: 1.35rem; }
      .q-title { font-size: 1rem; }
      .option-item { padding: 10px 12px; }
      .opt-text { font-size: 0.88rem; }
    }
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <div class="header-top">
        <span class="badge-hero">2026 UEC 烘焙理论 · 高一强化测验</span>
        <button class="action-btn" id="resetAllBtn" style="color:white; background:rgba(255,255,255,0.2); border:none;" onclick="resetAll()">
          🔄 重新答题
        </button>
      </div>
      <div>
        <h1>高一第10至15课·烘焙生活常识互动题库</h1>
        <p class="header-desc">涵盖面粉、油脂、糖、鸡蛋、乳制品、酵母与发酵共6大核心原料，全部180题精选，点击选项即时揭示正误与生动解析！</p>
      </div>

      <div class="hud-bar">
        <div class="hud-item">
          <span class="hud-label">已答题数</span>
          <span class="hud-value" id="hudAnswered">0 / 180</span>
        </div>
        <div class="hud-item">
          <span class="hud-label">正确率</span>
          <span class="hud-value" id="hudAccuracy">0%</span>
        </div>
        <div class="hud-item">
          <span class="hud-label">做对题数</span>
          <span class="hud-value" id="hudCorrect" style="color:#A7F3D0;">0</span>
        </div>
        <div class="hud-item">
          <span class="hud-label">需复习(做错)</span>
          <span class="hud-value" id="hudWrong" style="color:#FECACA;">0</span>
        </div>
      </div>
    </div>
  </header>

  <main>
    <!-- Chapter Filter Tabs -->
    <div class="tabs-wrapper" id="chapterTabs">
      <button class="tab-btn active" data-chapter="all">🌟 全部题目 (180题)</button>
      <button class="tab-btn" data-chapter="10">第10课｜面粉 (30题)</button>
      <button class="tab-btn" data-chapter="11">第11课｜油脂 (30题)</button>
      <button class="tab-btn" data-chapter="12">第12课｜糖 (30题)</button>
      <button class="tab-btn" data-chapter="13">第13课｜鸡蛋 (30题)</button>
      <button class="tab-btn" data-chapter="14">第14课｜乳制品 (30题)</button>
      <button class="tab-btn" data-chapter="15">第15课｜酵母与发酵 (30题)</button>
      <button class="tab-btn" data-chapter="mistakes">⚠️ 错题专练</button>
    </div>

    <!-- Search & Utility -->
    <div class="utility-bar">
      <div class="search-box">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 搜索考点或关键词（如：手套膜、黄油打发、蛋白霜、发酵温水...）">
      </div>
    </div>

    <!-- Questions Container -->
    <div id="questionsContainer"></div>
  </main>

  <script>
    // Embedded Question Dataset (180 Questions)
    const rawData = __QUESTIONS_DATA_PLACEHOLDER__;

    // State
    let currentFilter = 'all';
    let searchQuery = '';
    let userAnswers = {}; // key: `ch-id`, value: { chosen: 'A', correct: true/false }

    // Flatten all questions
    let allQuestions = [];
    rawData.forEach(ch => {
      ch.questions.forEach(q => {
        allQuestions.push({
          chapter_id: ch.chapter_id,
          chapter_title: ch.chapter_title,
          uid: `${ch.chapter_id}-${q.id}`,
          ...q
        });
      });
    });

    // Render questions
    function render() {
      const container = document.getElementById('questionsContainer');
      container.innerHTML = '';

      let filtered = allQuestions.filter(q => {
        // Chapter filter
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
      });

      if (filtered.length === 0) {
        container.innerHTML = `
          <div style="text-align:center; padding: 60px 20px; background:white; border-radius:12px; border:1px solid #E2E8F0;">
            <div style="font-size: 2.5rem; margin-bottom: 12px;">🎉</div>
            <h3 style="color:#334155; margin-bottom:6px;">没有找到匹配的题目</h3>
            <p style="color:#64748B; font-size:0.92rem;">${currentFilter === 'mistakes' ? '太棒了！目前还没有做错任何题目，或者错题已被清除。' : '试试调整搜索关键词或选择其他单元课。'}</p>
          </div>
        `;
        return;
      }

      filtered.forEach((q, idx) => {
        const card = document.createElement('div');
        card.className = 'question-card';
        card.id = `card-${q.uid}`;

        const isRoman = q.type === 'roman';
        const tagText = isRoman ? '乙组·罗马组合题' : '甲组·单项选择题';
        const tagClass = isRoman ? 'q-tag roman' : 'q-tag';

        const rec = userAnswers[q.uid];
        const isAnswered = !!rec;

        let optionsHtml = '';
        ['A', 'B', 'C', 'D'].forEach(letter => {
          let itemClass = 'option-item';
          if (isAnswered) {
            itemClass += ' locked';
            if (rec.chosen === letter) {
              itemClass += rec.correct ? ' correct' : ' wrong';
            } else if (!rec.correct && q.answer === letter) {
              itemClass += ' should-have-chosen';
            }
          }

          optionsHtml += `
            <div class="${itemClass}" onclick="handleOptionClick('${q.uid}', '${letter}')">
              <span class="opt-letter">${letter}</span>
              <span class="opt-text">${q.options[letter]}</span>
            </div>
          `;
        });

        const expShowClass = isAnswered ? 'explanation-box show' : 'explanation-box';

        card.innerHTML = `
          <div class="q-header">
            <span class="${tagClass}">${tagText}</span>
            <span class="q-chapter-badge">${q.chapter_title} · 第 ${q.id} 题</span>
          </div>
          <div class="q-title">${q.question}</div>
          <div class="options-grid">
            ${optionsHtml}
          </div>
          <div class="${expShowClass}" id="exp-${q.uid}">
            <div class="exp-title">💡 生活常识与烘焙机理解析【正确答案：${q.answer}】</div>
            <div class="exp-body">${q.explanation}</div>
          </div>
        `;

        container.appendChild(card);
      });

      updateHUD();
    }

    // Handle Option Selection
    window.handleOptionClick = function(uid, chosenLetter) {
      if (userAnswers[uid]) return; // already answered

      const q = allQuestions.find(item => item.uid === uid);
      if (!q) return;

      const isCorrect = (chosenLetter === q.answer);
      userAnswers[uid] = { chosen: chosenLetter, correct: isCorrect };

      render();
    };

    // Update HUD stats
    function updateHUD() {
      const answeredKeys = Object.keys(userAnswers);
      const answeredCount = answeredKeys.length;
      let correctCount = 0;
      answeredKeys.forEach(k => {
        if (userAnswers[k].correct) correctCount++;
      });
      const wrongCount = answeredCount - correctCount;
      const acc = answeredCount > 0 ? Math.round((correctCount / answeredCount) * 100) : 0;

      document.getElementById('hudAnswered').innerText = `${answeredCount} / ${allQuestions.length}`;
      document.getElementById('hudAccuracy').innerText = `${acc}%`;
      document.getElementById('hudCorrect').innerText = correctCount;
      document.getElementById('hudWrong').innerText = wrongCount;
    }

    // Reset All
    window.resetAll = function() {
      if (confirm('确定要清空当前的做题记录重新开始吗？')) {
        userAnswers = {};
        render();
      }
    };

    // Event Listeners
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.getAttribute('data-chapter');
        render();
      });
    });

    document.getElementById('searchInput').addEventListener('input', (e) => {
      searchQuery = e.target.value;
      render();
    });

    // Initial render
    render();
  </script>
</body>
</html>
'@

$finalHtml = $htmlTemplate.Replace('__QUESTIONS_DATA_PLACEHOLDER__', $allJsonString)

$outHtmlPath = Join-Path $outDir '高一厨艺理论_第10至15课_互动答题练习系统.html'
[System.IO.File]::WriteAllText($outHtmlPath, $finalHtml, [System.Text.Encoding]::UTF8)

Write-Host "Interactive HTML successfully built: $outHtmlPath"
