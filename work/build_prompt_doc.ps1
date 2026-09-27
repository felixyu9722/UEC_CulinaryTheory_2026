# ==============================================================================
# 自动生成高一第1课《烘焙概论》测试卷 Word 文档脚本
# 生成三大文件：
# 1. 01_第1课_烘焙概论_命题提示词与规范留档.docx
# 2. 02_第1课_烘焙概论_学生测验卷（简易版）.docx
# 3. 03_第1课_烘焙概论_教师解析与评分标准（简易版）.docx
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Stop'

$outDir = "C:\Users\GOH\Desktop\2026年统考厨艺理论\08_高一新测验题库_简易版"
if (-not (Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$imgTherm = "C:\Users\GOH\Desktop\2026年统考厨艺理论\03_Notion教学讲义\图片\统考题库考题配图\考题配图_第1课_第10题_热化学反应区间图.png"
$imgDefect = "C:\Users\GOH\Desktop\2026年统考厨艺理论\03_Notion教学讲义\图片\统考题库考题配图\考题配图_第1课_第36题_后厨真实塌陷案例图.png"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

# 颜色常量定义
$colorNavy  = 0x5D361A  # BGR for #1A365D (Deep Navy)
$colorTeal  = 0x88940D  # BGR for #0D9488 (Teal Accent)
$colorGray  = 0x707070  # BGR for Subtext
$colorDark  = 0x222222  # BGR for Body
$colorLight = 0xFAF8F6  # BGR for Light gray background #F6F8FA

function Set-PageSetup($doc) {
    $sec = $doc.Sections.Item(1)
    $sec.PageSetup.PaperSize = 9 # wdPaperA4
    $sec.PageSetup.TopMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.BottomMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.LeftMargin = $word.CentimetersToPoints(2.2)
    $sec.PageSetup.RightMargin = $word.CentimetersToPoints(2.2)
    $sec.PageSetup.HeaderDistance = $word.CentimetersToPoints(1.0)
    $sec.PageSetup.FooterDistance = $word.CentimetersToPoints(1.0)
}

function Add-HeaderFooter($doc, $titleText) {
    $sec = $doc.Sections.Item(1)
    $hdr = $sec.Headers.Item(1).Range
    $hdr.Text = $titleText
    $hdr.Font.NameFarEast = "Microsoft YaHei"
    $hdr.Font.Name = "Calibri"
    $hdr.Font.Size = 9
    $hdr.Font.Color = $colorGray
    $hdr.ParagraphFormat.Alignment = 2 # Right

    $ftr = $sec.Footers.Item(1).Range
    $ftr.Text = "2026年独中统考厨艺科 · 高一烘焙理论随堂测验卷（简易版）"
    $ftr.Font.NameFarEast = "Microsoft YaHei"
    $ftr.Font.Name = "Calibri"
    $ftr.Font.Size = 8.5
    $ftr.Font.Color = $colorGray
    $ftr.ParagraphFormat.Alignment = 1 # Center
}

# ------------------------------------------------------------------------------
# 1. 生成 01_第1课_烘焙概论_命题提示词与规范留档.docx
# ------------------------------------------------------------------------------
Write-Host ">>> 正在生成 01_第1课_烘焙概论_命题提示词与规范留档.docx ..."
$doc1 = $word.Documents.Add()
Set-PageSetup $doc1
Add-HeaderFooter $doc1 "【命题规范留档】高一《烘焙基础理论》第1课：烘焙概论"

$sel = $word.Selection
$sel.EndKey(6) | Out-Null # wdStory

# 标题
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 18
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText("高一《烘焙基础理论》第1课：烘焙概论`n命题提示词与工程规范留档`n")

# 元数据表
$sel.Font.Size = 10
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText("适用对象：马来西亚华文独中高中厨艺科（高一零基础学生）`n命题依据：董总高中厨艺科课程纲要、Notion《高中厨艺（烘焙理论）2026》、后厨食品物理化学机理`n试卷定位：单元标准测试卷（简易基础版，选项短句化、ABCD均等分布、图文并茂）`n`n")

# 一、核心提示词
$sel.Font.Size = 14
$sel.Font.Bold = $true
$sel.Font.Color = $colorTeal
$sel.TypeText("一、AI 自动化命题核心提示词（Prompt Template）`n")

$tbl1 = $doc1.Tables.Add($sel.Range, 1, 1)
$tbl1.Borders.Enable = 1
$tbl1.Borders.Color = $colorTeal
$tbl1.Shading.BackgroundPatternColor = $colorLight
$c1 = $tbl1.Cell(1, 1).Range
$c1.Font.NameFarEast = "Microsoft YaHei"
$c1.Font.Name = "Calibri"
$c1.Font.Size = 9.5
$c1.Font.Color = $colorDark
$c1.Text = @"
你是一位拥有20年教学经验的马来西亚华文独中高中厨艺科高级教师，同时具备法国蓝带（Le Cordon Bleu）西点师认证。请根据以下考纲知识点与规范，为高一零基础学生编写一份《第1课：烘焙概论》的新测验题库（简易版）。

### 一、出题原则与格式约束
1. 【难度定位】：简易基础版。语言通俗严谨，紧扣核心概念与后厨实操，杜绝冗长晦涩句子。
2. 【选择题选项长度控制】：ABCD 四个选项必须为“短词或短句”（每项字数严格控制在 4~12 字以内），句式整齐。
3. 【答案均匀分布】：
   - 15 题单选题答案分布必须均衡：A 选项 4 题、B 选项 4 题、C 选项 4 题、D 选项 3 题。
   - 5 题罗马数字组合题答案分布均衡：涵盖 A、B、C、D 各项组合。
4. 【题型与分值配比】（满分 100 分）：
   - 第一部分：单项选择题（15 题，每题 2 分，共 30 分）
   - 第二部分：罗马数字组合选择题（5 题，每题 2 分，共 10 分，含 Ⅰ、Ⅱ、Ⅲ、Ⅳ 选项组合）
   - 第三部分：核心概念填充题（10 题，每题 2 分，共 20 分，标准唯一关键词挖空）
   - 第四部分：综合作答题（5 题，共 40 分，问法简明，附结构化采分点与步骤分）
5. 【配图考题融合】：结合后厨真实情境与物理化学温区图表（如出炉震盘排气、冷却架摆放、美拉德与焦糖化温区图、烤箱热传递）。

### 二、核心知识图谱与命题考点库
- 烘焙定义：主要依靠烤炉干热（辐射、对流、传导），使生面坯受热熟化形成固定体积、蜂窝结构、金黄着色与烘烤香气。
- 受热连续反应链：油脂熔化(40-50℃) → 酵母灭活(50-60℃) → 淀粉糊化(55-65℃) → 蛋白质凝固(60-75℃) → 水分汽化(100℃) → 美拉德反应(140-165℃) → 纯糖焦糖化(>160℃)。
- 关键概念辨析：美拉德反应（还原糖+氨基酸，面包外壳金黄麦香）；焦糖化反应（纯糖脱水裂解，焦糖布丁）。
- 出炉冷却守则：出炉立即震盘（排湿热气体，防塌陷收腰）；移至悬空冷却架（防底部冷凝水泡软）；严禁 4℃ 冷藏（2℃~6℃ 淀粉老化结晶速度最高峰，面包发硬掉渣）；长期保存应密封置于 -18℃ 极速冷冻。
"@
$sel.EndKey(6) | Out-Null
$sel.TypeText("`n`n")

# 二、版面视觉设计规范
$sel.Font.Size = 14
$sel.Font.Bold = $true
$sel.Font.Color = $colorTeal
$sel.TypeText("二、Word 教育版视觉设计与排版规范`n")

$sel.Font.Size = 10
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText(@"
1. 色彩规范：
   - 典雅深藏青 RGB(26, 54, 93) (#1A365D)：用于试卷总标题、大题分类条、表头背景。
   - 晨曦青蓝 RGB(13, 148, 136) (#0D9488)：用于题型分值标注、小标题重点强调。
   - 浅灰衬底 RGB(248, 250, 252) (#F8FAFC)：用于考务表格、提示框与得分栏背景。
2. 版面参数：
   - 页面规格：A4 纸张，上下边距 2.0 cm，左右边距 2.2 cm。
   - 字体配比：中文字体采用“微软雅黑 (Microsoft YaHei)”，西文字体采用“Calibri”。
   - 选项排列：单选题选项为短词短句，排成并列两栏或整齐四项，避免拥挤，阅读体验极佳。
   - 作答题空间：每题预留答题虚线或书写框，规范学生作答习惯。
"@)

$file1 = Join-Path $outDir "01_第1课_烘焙概论_命题提示词与规范留档.docx"
$doc1.SaveAs([ref]$file1, [ref]16) # wdFormatDocumentDefault
$doc1.Close()
Write-Host "  -> 已保存：$file1"

Write-Host "提示词 Word 文档生成完成！"
