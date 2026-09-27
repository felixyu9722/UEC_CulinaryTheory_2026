# ==============================================================================
# 构建高一第1课《烘焙概论》学生测验卷与教师解析卷 Word 文件
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Stop'

$outDir = "C:\Users\GOH\Desktop\2026年统考厨艺理论\08_高一新测验题库_简易版"
$imgTherm = "C:\Users\GOH\Desktop\2026年统考厨艺理论\03_Notion教学讲义\图片\统考题库考题配图\考题配图_第1课_第10题_热化学反应区间图.png"
$imgDefect = "C:\Users\GOH\Desktop\2026年统考厨艺理论\03_Notion教学讲义\图片\统考题库考题配图\考题配图_第1课_第36题_后厨真实塌陷案例图.png"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

# 颜色常量 (BGR 格式)
$colorNavy  = 0x5D361A  # #1A365D 深藏青
$colorTeal  = 0x88940D  # #0D9488 青蓝
$colorGray  = 0x666666  # 次级文字
$colorDark  = 0x222222  # 正文
$colorLight = 0xF5F2EF  # #EFFAF2 浅色衬底
$colorLightGray = 0xF8FAFC

function Setup-Document($doc, $headerText) {
    $sec = $doc.Sections.Item(1)
    $sec.PageSetup.PaperSize = 9 # wdPaperA4
    $sec.PageSetup.TopMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.BottomMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.LeftMargin = $word.CentimetersToPoints(2.2)
    $sec.PageSetup.RightMargin = $word.CentimetersToPoints(2.2)
    $sec.PageSetup.HeaderDistance = $word.CentimetersToPoints(1.0)
    $sec.PageSetup.FooterDistance = $word.CentimetersToPoints(1.0)

    $hdr = $sec.Headers.Item(1).Range
    $hdr.Text = $headerText
    $hdr.Font.NameFarEast = "Microsoft YaHei"
    $hdr.Font.Name = "Calibri"
    $hdr.Font.Size = 9
    $hdr.Font.Color = $colorGray
    $hdr.ParagraphFormat.Alignment = 2

    $ftr = $sec.Footers.Item(1).Range
    $ftr.Text = "2026年独中统考厨艺科 · 高一烘焙理论随堂测验卷（第1课：烘焙概论）"
    $ftr.Font.NameFarEast = "Microsoft YaHei"
    $ftr.Font.Name = "Calibri"
    $ftr.Font.Size = 8.5
    $ftr.Font.Color = $colorGray
    $ftr.ParagraphFormat.Alignment = 1
}

# ==============================================================================
# 生成学生试卷：02_第1课_烘焙概论_学生测验卷（简易版）.docx
# ==============================================================================
Write-Host ">>> 正在生成 02_第1课_烘焙概论_学生测验卷（简易版）.docx ..."
$doc2 = $word.Documents.Add()
Setup-Document $doc2 "2026年马来西亚华文独中高中统考（UEC）厨艺科 · 随堂测验"

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

# 试卷主标题
$sel.ParagraphFormat.Alignment = 1 # 居中
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 16
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText("2026年马来西亚华文独中高中统考（UEC）厨艺科（烘焙理论）`n")
$sel.Font.Size = 14
$sel.Font.Color = $colorTeal
$sel.TypeText("高一 单元随堂测验卷（简易版）· 第1课 烘焙概论`n")

$sel.Font.Size = 9.5
$sel.Font.Bold = $false
$sel.Font.Color = $colorGray
$sel.TypeText("考试时量：45 分钟 ｜ 卷面满分：100 分 ｜ 命题范围：第1课 烘焙概论`n`n")
$sel.ParagraphFormat.Alignment = 0 # 靠左

# 考生信息与得分表格
$tblInfo = $doc2.Tables.Add($sel.Range, 2, 5)
$tblInfo.Borders.Enable = 1
$tblInfo.Borders.Color = $colorTeal
$tblInfo.Rows.Alignment = 1
$headers = @("第一大题(30分)", "第二大题(10分)", "第三大题(20分)", "第四大题(40分)", "总分(100分)")
for ($col = 1; $col -le 5; $col++) {
    $c = $tblInfo.Cell(1, $col).Range
    $c.Font.NameFarEast = "Microsoft YaHei"
    $c.Font.Size = 9
    $c.Font.Bold = $true
    $c.Font.Color = $colorNavy
    $c.Text = $headers[$col-1]
    $c.ParagraphFormat.Alignment = 1
    $tblInfo.Cell(1, $col).Shading.BackgroundPatternColor = $colorLightGray

    $c2 = $tblInfo.Cell(2, $col).Range
    $c2.Font.NameFarEast = "Microsoft YaHei"
    $c2.Font.Size = 11
    $c2.Text = " "
    $c2.ParagraphFormat.Alignment = 1
}
$sel.EndKey(6) | Out-Null

$sel.Font.Size = 10
$sel.Font.Color = $colorDark
$sel.TypeText("`n班级：_____________  姓名：_____________  学号：_____________  座号：____  测验日期：2026年___月___日`n`n")

# 大题样式函数
function Write-SectionHeader($title) {
    $sel.Font.NameFarEast = "Microsoft YaHei"
    $sel.Font.Size = 12
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.TypeText("========================================================================`n")
    $sel.TypeText("$title`n")
    $sel.TypeText("========================================================================`n")
    $sel.Font.Bold = $false
    $sel.Font.Color = $colorDark
}

# ----------------- 第一部分：单项选择题 -----------------
Write-SectionHeader "一、单项选择题（共15题，每题2分，共30分。在每小题给出的四个选项中，只有一项是最符合题目要求的，请将字母填入括号中）"

$mcqs = @(
    @{
        Q = "1. 烘焙加工主要依赖的加热环境是（    ）。"
        A = "A. 烤炉干热"
        B = "B. 沸水湿热"
        C = "C. 高温油炸"
        D = "D. 低温冷冻"
    },
    @{
        Q = "2. 面坯入炉初期（40℃~50℃），最先发生的物理变化是（    ）。"
        A = "A. 蛋白质完全变性"
        B = "B. 固态油脂软化熔化"
        C = "C. 淀粉开始重结晶"
        D = "D. 纯糖发生焦糖化"
    },
    @{
        Q = "3. 酵母菌在烘烤升温过程中，完全死亡灭活的温度区间是（    ）。"
        A = "A. 20℃~30℃"
        B = "B. 35℃~40℃"
        C = "C. 50℃~60℃"
        D = "D. 95℃~100℃"
    },
    @{
        Q = "4. 蛋糕在烘烤中由流动面糊转变成固定组织，主要依赖哪两种反应？（    ）"
        A = "A. 蒸发与沉降"
        B = "B. 糊化与发酵"
        C = "C. 乳化与溶解"
        D = "D. 糊化与凝固"
    },
    @{
        Q = "5. 面粉中的淀粉颗粒受热吸水膨胀破裂、形成粘稠糊状的现象称为（    ）。"
        A = "A. 淀粉糊化"
        B = "B. 淀粉老化"
        C = "C. 蛋白质水解"
        D = "D. 油脂酸败"
    },
    @{
        Q = "6. 面包金黄色的外壳与浓郁烘烤麦香，主要产生自哪种化学反应？（    ）"
        A = "A. 酒精发酵"
        B = "B. 美拉德反应"
        C = "C. 纯糖焦糖化"
        D = "D. 氧化发酸"
    },
    @{
        Q = "7. 发生美拉德反应（Maillard reaction）必须同时具备的两类原料成分是（    ）。"
        A = "A. 纯糖与油脂"
        B = "B. 淀粉与水分"
        C = "C. 还原糖与氨基酸"
        D = "D. 酵母与二氧化碳"
    },
    @{
        Q = "8. 下列哪种后厨常见西点，其表面金黄褐变主要由“纯糖焦糖化反应”形成？（    ）"
        A = "A. 烤全麦吐司"
        B = "B. 烘烤黄油曲奇"
        C = "C. 法式焦糖布丁"
        D = "D. 传统法式长棍"
    },
    @{
        Q = "9. 纯蔗糖在无氨基酸参与下，发生焦糖化反应的起始温度通常为（    ）。"
        A = "A. 60℃"
        B = "B. 100℃"
        C = "C. 120℃"
        D = "D. 160℃"
    },
    @{
        Q = "10. 【识图题】观察下方《烘焙热化学反应区间图》，美拉德反应发生最适宜的温区是（    ）。"
        A = "A. 140℃~165℃"
        B = "B. 60℃~75℃"
        C = "C. 30℃~40℃"
        D = "D. 200℃~250℃"
        Img = $imgTherm
    },
    @{
        Q = "11. 烘烤完成出炉时，测量标准面包内部中心温度，适宜的标准范围是（    ）。"
        A = "A. 60℃~70℃"
        B = "B. 93℃~98℃"
        C = "C. 120℃~130℃"
        D = "D. 150℃~160℃"
    },
    @{
        Q = "12. 面包出炉瞬间，师傅必须立即在操作台上“轻震烤盘”，主要目的是（    ）。"
        A = "A. 震散内部糖分"
        B = "B. 震落表面手粉"
        C = "C. 排出湿热废气"
        D = "D. 加快油脂凝固"
    },
    @{
        Q = "13. 刚出炉的面包或蛋糕，应立即转移到哪种器具上进行自然冷却？（    ）"
        A = "A. 密封塑料盒内"
        B = "B. 紧闭烤箱内部"
        C = "C. 实心金属托盘"
        D = "D. 通风悬空网架"
    },
    @{
        Q = "14. 为什么严禁将出炉冷却的面包存放在 4℃ 的冰箱冷藏室？（    ）"
        A = "A. 会加速淀粉老化"
        B = "B. 酵母会重新发酵"
        C = "C. 面筋蛋白会溶解"
        D = "D. 表皮颜色会褪色"
    },
    @{
        Q = "15. 若需较长时间（2周以上）保鲜已完全冷却的面包，最科学的方法是（    ）。"
        A = "A. 常温敞开摆放"
        B = "B. 密封冷冻(-18℃)"
        C = "C. 4℃冷藏避光"
        D = "D. 浸泡温水保温"
    }
)

foreach ($item in $mcqs) {
    $sel.Font.Bold = $true
    $sel.Font.Size = 10
    $sel.TypeText($item.Q + "`n")
    $sel.Font.Bold = $false

    if ($item.Img -and (Test-Path $item.Img)) {
        $shape = $sel.InlineShapes.AddPicture($item.Img)
        $shape.Width = 340 # 适合宽度
        $sel.TypeText("`n")
    }

    # 选项两列整齐排布
    $sel.TypeText("   " + $item.A.PadRight(24) + $item.B + "`n")
    $sel.TypeText("   " + $item.C.PadRight(24) + $item.D + "`n`n")
}

# ----------------- 第二部分：罗马数字组合选择题 -----------------
Write-SectionHeader "二、罗马数字组合选择题（共5题，每题2分，共10分。每小题由Ⅰ、Ⅱ、Ⅲ、Ⅳ四个表述组合而成，请选出最恰当的选项）"

$combos = @(
    @{
        Q = "16. 烘焙过程中，商用烤箱对生面坯提供的热量传递方式包括以下哪些？`n   Ⅰ. 烤箱内壁热辐射    Ⅱ. 炉内热空气对流    Ⅲ. 烤盘底部热传导    Ⅳ. 微波分子极化共振"
        A = "A. Ⅰ、Ⅱ、Ⅲ"
        B = "B. Ⅰ、Ⅱ、Ⅳ"
        C = "C. Ⅱ、Ⅲ、Ⅳ"
        D = "D. Ⅰ、Ⅲ、Ⅳ"
    },
    @{
        Q = "17. 面包烘烤受热过程中，以下哪些物理化学变化直接负责“建立并固定内部骨架结构”？`n   Ⅰ. 淀粉吸水糊化    Ⅱ. 面筋蛋白质受热凝固    Ⅲ. 酵母快速产气灭活    Ⅳ. 表面纯糖焦糖化"
        A = "A. Ⅰ、Ⅲ"
        B = "B. Ⅰ、Ⅱ"
        C = "C. Ⅱ、Ⅳ"
        D = "D. Ⅲ、Ⅳ"
    },
    @{
        Q = "18. 烘焙师傅检验成品出炉品质时，常用的“三大感官评价维度”包括以下哪些？`n   Ⅰ. 结构（膨胀饱满度）  Ⅱ. 色泽（烘烤金黄色泽）  Ⅲ. 香气（复合烘烤麦香）  Ⅳ. 包装（包装袋色彩）"
        A = "A. Ⅰ、Ⅱ、Ⅳ"
        B = "B. Ⅱ、Ⅲ、Ⅳ"
        C = "C. Ⅰ、Ⅱ、Ⅲ"
        D = "D. Ⅰ、Ⅲ、Ⅳ"
    },
    @{
        Q = "19. 面包出炉后的科学冷却操作，规范动作包括以下哪些？`n   Ⅰ. 出炉瞬间轻震烤盘排气    Ⅱ. 迅速移至悬空冷却架    Ⅲ. 严禁闷在实心金属盘中    Ⅳ. 趁热直接切片装袋密封"
        A = "A. Ⅰ、Ⅱ、Ⅳ"
        B = "B. Ⅰ、Ⅱ、Ⅲ"
        C = "C. Ⅱ、Ⅲ、Ⅳ"
        D = "D. Ⅰ、Ⅲ、Ⅳ"
    },
    @{
        Q = "20. 关于烘焙成品“淀粉老化（Staling）”的物理现象，正确的表述包括以下哪些？`n   Ⅰ. 宏观表现为面包组织发硬变干、易掉渣    Ⅱ. 在 2℃~6℃ 冷藏温度下老化速度处于最高峰`n   Ⅲ. 长期保存应密封置于 -18℃ 极速冷冻库    Ⅳ. 冷冻面包自然回温或复烤后可恢复松软"
        A = "A. Ⅰ、Ⅱ"
        B = "B. Ⅱ、Ⅲ"
        C = "C. Ⅰ、Ⅲ、Ⅳ"
        D = "D. Ⅰ、Ⅱ、Ⅲ、Ⅳ"
    }
)

foreach ($cItem in $combos) {
    $sel.Font.Bold = $true
    $sel.Font.Size = 10
    $sel.TypeText($cItem.Q + "`n")
    $sel.Font.Bold = $false
    $sel.TypeText("   " + $cItem.A.PadRight(24) + $cItem.B + "`n")
    $sel.TypeText("   " + $cItem.C.PadRight(24) + $cItem.D + "`n`n")
}

# ----------------- 第三部分：核心概念填充题 -----------------
Write-SectionHeader "三、核心概念填充题（共10题，每空2分，共20分。请在横线上填入最恰当的专业术语或关键数值）"

$fills = @(
    "21. 烘焙主要以烤炉________（填“干热”或“湿热”）为介质，使面团或面糊熟化并定型。",
    "22. 烘烤受热过程中，面粉中的淀粉吸水膨胀变稠的物理变化称为淀粉________作用。",
    "23. 蛋糕面糊中的鸡蛋与面筋在 60℃~75℃ 受热变性定型的现象称为蛋白质________作用。",
    "24. 面包外壳的金黄色泽与浓郁香气，主要是由还原糖与氨基酸发生________反应生成。",
    "25. 纯蔗糖在无蛋白质氨基酸参与时，单独加热至 160℃ 以上发生的脱水褐变反应称为________反应。",
    "26. 商用烘焙在生面坯入炉前，烤箱通常需要提前预热________至 20 分钟以确保炉温恒定。",
    "27. 面包烘烤完全成熟出炉时，测得内部中心温度的标准范围应达到 93℃ 至________℃。",
    "28. 面包出炉瞬间必须轻震烤盘，其主要目的是震破密闭气孔，排出内部积聚的________高压气体。",
    "29. 出炉后的烘焙产品严禁放入________℃ 冷藏室，因为该温区是淀粉结晶老化速度的最顶峰。",
    "30. 已完全冷却的面包若需长期保鲜数周，应密封严实后送入________℃ 极速冷冻库锁水储存。"
)

foreach ($f in $fills) {
    $sel.Font.Size = 10
    $sel.TypeText($f + "`n`n")
}

# ----------------- 第四部分：综合作答题 -----------------
Write-SectionHeader "四、综合作答题（共5题，共40分。请在每小题预留的作答区域内条理清晰作答）"

$longQuestions = @(
    @{
        Title = "31. 【概念辨析题】在烘焙生产中，“美拉德反应”与“焦糖化反应”都会产生表面金黄褐变。请简要写出两者的两项核心不同之处（从反应所需原料、代表性成品两个方面进行对比）。（本题 8 分）"
        Lines = 4
    },
    @{
        Title = "32. 【后厨实操题】请简述烘焙师傅在面包烘烤出炉后，必须立即执行的“前两项关键冷却动作”是什么？并分别说明操作目的。（本题 8 分）"
        Lines = 4
    },
    @{
        Title = "33. 【受热机理题】液态的蛋糕面糊在烤箱中受热后，转变成具有饱满高度与蜂窝气孔的松软固态蛋糕。请写出在此过程中发生的两个最核心物理/化学变化，并简述各自的作用。（本题 8 分）"
        Lines = 4
    },
    @{
        Title = "34. 【食品保鲜题】某实习学生将刚出炉放凉的面包放进后厨 4℃ 的保鲜冰箱冷藏室存放，次日发现面包变得干硬粗糙、极易掉渣。`n   (1) 请指出该学生犯下的保存错误机理是什么？（4分）`n   (2) 请写出正确的短期（2~3天）与长期（2周以上）保存方法。（4分）"
        Lines = 5
    },
    @{
        Title = "35. 【读图与缺陷排查题】观察下方后厨真实烘焙案例图片。某批次乡村欧包出炉后未震盘，且直接堆叠在实心金属烤盘中冷却，数小时后发现面包底部湿黏软烂、侧边严重“塌腰收缩”。请给出两项针对性的排查诊断与救治方案。（本题 8 分）"
        Img = $imgDefect
        Lines = 5
    }
)

foreach ($lq in $longQuestions) {
    $sel.Font.Bold = $true
    $sel.Font.Size = 10
    $sel.TypeText($lq.Title + "`n")
    $sel.Font.Bold = $false

    if ($lq.Img -and (Test-Path $lq.Img)) {
        $shape = $sel.InlineShapes.AddPicture($lq.Img)
        $shape.Width = 330
        $sel.TypeText("`n")
    }

    # 答题线
    $sel.Font.Color = $colorGray
    for ($i = 1; $i -le $lq.Lines; $i++) {
        $sel.TypeText("答：____________________________________________________________________________________`n")
    }
    $sel.Font.Color = $colorDark
    $sel.TypeText("`n")
}

$file2 = Join-Path $outDir "02_第1课_烘焙概论_学生测验卷（简易版）.docx"
$doc2.SaveAs([ref]$file2, [ref]16)
$doc2.Close()
Write-Host "  -> 已保存：$file2"


# ==============================================================================
# 生成教师答案解析卷：03_第1课_烘焙概论_教师解析与评分标准（简易版）.docx
# ==============================================================================
Write-Host ">>> 正在生成 03_第1课_烘焙概论_教师解析与评分标准（简易版）.docx ..."
$doc3 = $word.Documents.Add()
Setup-Document $doc3 "2026年马来西亚华文独中高中统考（UEC）厨艺科 · 教师专用解析与评分标准"

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

# 标题
$sel.ParagraphFormat.Alignment = 1 # 居中
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 16
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText("2026年马来西亚华文独中高中统考（UEC）厨艺科（烘焙理论）`n")
$sel.Font.Size = 14
$sel.Font.Color = $colorTeal
$sel.TypeText("高一 第1课 烘焙概论 · 教师专用答案解析与评分标准（简易版）`n")

$sel.Font.Size = 9.5
$sel.Font.Bold = $false
$sel.Font.Color = $colorGray
$sel.TypeText("【教师教学备课与评卷参考手册 · 满分 100 分 · 含采分点细则与易错题解析】`n`n")
$sel.ParagraphFormat.Alignment = 0 # 靠左

# ----------------- 快速答案速查表 -----------------
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Size = 12
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText("一、客观题快速答案核对表（共 60 分）`n")
$sel.Font.Bold = $false

# 15 单选题速查表
$tblAns1 = $doc3.Tables.Add($sel.Range, 4, 8)
$tblAns1.Borders.Enable = 1
$tblAns1.Borders.Color = $colorTeal
$tblAns1.Rows.Alignment = 1

$r1 = @("题号", "1", "2", "3", "4", "5", "6", "7")
$r2 = @("答案", "A", "B", "C", "D", "A", "B", "C")
$r3 = @("题号", "8", "9", "10", "11", "12", "13", "14")
$r4 = @("答案", "C", "D", "A", "B", "C", "D", "A")

for ($c = 1; $c -le 8; $c++) {
    $tblAns1.Cell(1, $c).Range.Text = $r1[$c-1]
    $tblAns1.Cell(1, $c).Range.Font.Bold = $true
    $tblAns1.Cell(1, $c).Shading.BackgroundPatternColor = $colorLightGray
    $tblAns1.Cell(2, $c).Range.Text = $r2[$c-1]
    $tblAns1.Cell(2, $c).Range.Font.Bold = $true
    $tblAns1.Cell(2, $c).Range.Font.Color = $colorTeal

    $tblAns1.Cell(3, $c).Range.Text = $r3[$c-1]
    $tblAns1.Cell(3, $c).Range.Font.Bold = $true
    $tblAns1.Cell(3, $c).Shading.BackgroundPatternColor = $colorLightGray
    $tblAns1.Cell(4, $c).Range.Text = $r4[$c-1]
    $tblAns1.Cell(4, $c).Range.Font.Bold = $true
    $tblAns1.Cell(4, $c).Range.Font.Color = $colorTeal
}
$sel.EndKey(6) | Out-Null
$sel.Font.Size = 9.5
$sel.TypeText("注：第15题答案为【 B 】。15题单选答案分布：A: 4题，B: 4题，C: 4题，D: 3题，分布完全均衡。`n`n")

# 5 组合题速查表
$sel.Font.Bold = $true
$sel.Font.Size = 10
$sel.Font.Color = $colorNavy
$sel.TypeText("【罗马数字组合题速查（每题2分，共10分）】`n")
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText("  • 16题：【 A 】（Ⅰ、Ⅱ、Ⅲ 辐射、对流、传导属于普通烤箱传热方式，微波不属于）`n")
$sel.TypeText("  • 17题：【 B 】（Ⅰ、Ⅱ 淀粉糊化与蛋白质凝固是建立骨架核心）`n")
$sel.TypeText("  • 18题：【 C 】（Ⅰ、Ⅱ、Ⅲ 结构、色泽、香气为三大核心感官维度）`n")
$sel.TypeText("  • 19题：【 B 】（Ⅰ、Ⅱ、Ⅲ 规范冷却动作，趁热切片装袋会导致回潮破损）`n")
$sel.TypeText("  • 20题：【 D 】（Ⅰ、Ⅱ、Ⅲ、Ⅳ 四项陈述均完全正确）`n`n")

# 10 填空题答案速查
$sel.Font.Bold = $true
$sel.Font.Size = 10
$sel.Font.Color = $colorNavy
$sel.TypeText("【核心概念填空题速查（每空2分，共20分）】`n")
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText("  • 21. 干热`n  • 22. 糊化（Gelatinisation）`n  • 23. 凝固（Coagulation）`n  • 24. 美拉德（Maillard）`n  • 25. 焦糖化（Caramelisation）`n  • 26. 15`n  • 27. 98`n  • 28. 湿热（或水汽）`n  • 29. 4（或 2~6）`n  • 30. -18`n`n")

# ----------------- 第四部分：作答题详细评分标准 -----------------
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Size = 12
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText("二、综合作答题评分细则与参考范文（共 40 分）`n`n")

$rubrics = @(
    @{
        Num = "第 31 题（8分）· 美拉德反应与焦糖化反应概念辨析"
        Answer = @"
【参考满分答案】：
1. 反应所需原料不同（4分）：
   • 美拉德反应：必须同时具备“还原糖”与“氨基酸/蛋白质”（2分）。
   • 焦糖化反应：只需“纯糖”单独受热脱水裂解，无需蛋白质参与（2分）。
2. 代表性西点成品不同（4分）：
   • 美拉德反应主导：烘烤面包的金黄外壳、黄油曲奇饼干、牛排表面焦香（答出任意一项得2分）。
   • 焦糖化反应主导：法式焦糖布丁表面的焦脆糖壳、焦糖奶油酱、拔丝苹果糖浆（答出任意一项得2分）。
【易错提示】：不可认为所有食物受热变黄变黑都是焦糖化，含有蛋白质与还原糖的面包上色主要是美拉德反应。
"@
    },
    @{
        Num = "第 32 题（8分）· 面包出炉前两项关键冷却动作与操作目的"
        Answer = @"
【参考满分答案】：
1. 动作一：出炉瞬间在工作台上“轻震烤盘”（2分）。
   • 操作目的：震破微气孔，瞬间排出面包内部聚集的高压湿热废气，平衡内外气压，防止出炉后由于中心负压导致面包塌陷、收腰或缩水（2分）。
2. 动作二：立即将面包脱模并移至“悬空网架（冷却架）”上冷却（2分）。
   • 操作目的：使面包顶部、侧面和底部全方位通风散热，防止水汽凝结在实心金属盘底形成冷凝水，避免底部表皮被彻底泡软发黏（2分）。
"@
    },
    @{
        Num = "第 33 题（8分）· 蛋糕面糊转变成固态组织的两个核心物理/化学变化"
        Answer = @"
【参考满分答案】：
1. 关键变化一：淀粉糊化（Starch gelatinisation）（2分）。
   • 核心作用：面粉中的淀粉颗粒在 55℃~65℃ 吸水膨胀破裂，形成具有黏弹性的凝胶基质，填充在气孔之间，奠定蛋糕柔软细腻的组织（2分）。
2. 关键变化二：蛋白质变性凝固（Protein coagulation）（2分）。
   • 核心作用：鸡蛋与面粉中的蛋白质分子在 60℃~75℃ 受热展开并交联形成牢固的三维立体网状骨架，锁住受热膨胀的气体，使蛋糕最终定型不塌陷（2分）。
"@
    },
    @{
        Num = "第 34 题（8分）· 面包冷藏发硬错误机理与科学保鲜方法"
        Answer = @"
【参考满分答案】：
(1) 错误保存机理（4分）：
   • 淀粉老化（Retrogradation / Staling）：受热糊化后的淀粉分子在冷却时会自发脱水重新结晶排列（2分）。
   • 危险温区：科学测定表明，在 2℃~6℃（冰箱冷藏室温度）时，淀粉分子的重结晶速度处于物理最高峰，老化速度比常温快数倍，导致面包急速变干变硬、掉渣失去弹性（2分）。
(2) 正确保存方法（4分）：
   • 短期保存（2~3天）：完全放凉后，装入保鲜袋或密封盒常温避光保存（2分）。
   • 长期保存（2周以上）：完全放凉后密封严实，直接放入 -18℃ 极速冷冻库锁住冰晶；食用前取出自然回温或用 180℃ 烤箱复烤 3~5 分钟即可完全复原松软口感（2分）。
"@
    },
    @{
        Num = "第 35 题（8分）· 读图案例缺陷诊断与救治方案"
        Answer = @"
【参考满分答案】：
1. 缺陷一：欧包底部湿黏软烂（4分）
   • 诊断原因：面包出炉后闷在实心金属烤盘中，底部散发的热蒸汽遇冷凝结为冷凝水，浸泡底皮所致（2分）。
   • 修正救治方案：烘烤完成必须在数分钟内将面包移至镂空通风的冷却网架上悬空冷却（2分）。
2. 缺陷二：欧包侧边严重塌腰收缩（4分）
   • 诊断原因：出炉未震盘排气，内部高压湿热蒸汽降温冷凝后形成内部负压，在大气压作用下被压扁收腰（2分）。
   • 修正救治方案：出炉 5 秒内必须将烤盘在台面上轻震一下，震破微孔平衡气压；同时确保烘烤时间充足，中心温度达 93℃ 以上保证结构完全成熟（2分）。
"@
    }
)

foreach ($rb in $rubrics) {
    $sel.Font.Bold = $true
    $sel.Font.Size = 11
    $sel.Font.Color = $colorTeal
    $sel.TypeText($rb.Num + "`n")
    $sel.Font.Bold = $false
    $sel.Font.Size = 9.5
    $sel.Font.Color = $colorDark
    $sel.TypeText($rb.Answer + "`n`n")
}

$file3 = Join-Path $outDir "03_第1课_烘焙概论_教师解析与评分标准（简易版）.docx"
$doc3.SaveAs([ref]$file3, [ref]16)
$doc3.Close()
Write-Host "  -> 已保存：$file3"

$word.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
Write-Host "所有 Word 文档生成完毕！"
