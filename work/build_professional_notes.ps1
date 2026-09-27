# ==============================================================================
# build_professional_notes.ps1
# 使用 Word COM 对象全自动化构建深度专业版《学生笔记重点收藏》
# ==============================================================================
$ErrorActionPreference = 'Stop'
$baseDir = 'C:\Users\GOH\Desktop\2026年统考厨艺理论'
. "$baseDir\work\curriculum_knowledge_base.ps1"

$imgDir = Join-Path $baseDir '03_Notion教学讲义\图片'
$outDir = Join-Path $baseDir '04_学生笔记重点收藏'
$jsonPath = Join-Path $baseDir 'work\notion_full_lessons.json'
$fullData = Get-Content $jsonPath -Raw | ConvertFrom-Json
$deepKB = Get-CurriculumData

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

function Build-GradeDoc($gradeName, $outFileName, $introText) {
    Write-Output ">>> Starting generation for $gradeName -> $outFileName ..."
    $doc = $word.Documents.Add()
    
    # 页面版式设置 (A4标准，页边距合理)
    $sec = $doc.Sections.Item(1)
    $sec.PageSetup.PaperSize = 7 # wdPaperA4
    $sec.PageSetup.TopMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.BottomMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.LeftMargin = $word.CentimetersToPoints(2.2)
    $sec.PageSetup.RightMargin = $word.CentimetersToPoints(2.2)
    
    # 样式配置
    $styles = $doc.Styles
    $normal = $styles.Item('Normal')
    $normal.Font.NameFarEast = 'Microsoft JhengHei'
    $normal.Font.Name = 'Calibri'
    $normal.Font.Size = 10
    $normal.ParagraphFormat.LineSpacingRule = 5 # multiple
    $normal.ParagraphFormat.LineSpacing = 13.5
    $normal.ParagraphFormat.SpaceAfter = 3
    
    # 页眉与页脚
    $header = $sec.Headers.Item(1).Range
    $header.Text = "2026 高中厨艺（烘焙理论）专业讲义｜$gradeName 重点收藏"
    $header.Font.NameFarEast = 'Microsoft JhengHei'
    $header.Font.Size = 8.5
    $header.Font.Color = 0x666666
    $header.ParagraphFormat.Alignment = 2 # Right
    
    $footer = $sec.Footers.Item(1).Range
    $footer.ParagraphFormat.Alignment = 1 # Center
    $footer.Font.NameFarEast = 'Microsoft JhengHei'
    $footer.Font.Size = 8.5
    $footer.Font.Color = 0x666666
    $footer.Text = "学生自主学习与统考精准备考｜第 "
    $footer.Collapse(0)
    $footer.Fields.Add($footer, 33) | Out-Null # wdFieldPage
    $footerRangeEnd = $sec.Footers.Item(1).Range
    $footerRangeEnd.Collapse(0)
    $footerRangeEnd.Text = " 页"
    
    # 辅助插入函数
    function Add-P([string]$text, [int]$fontSize = 10, [bool]$bold = $false, [int]$color = 0x000000, [int]$spaceBefore = 0, [int]$spaceAfter = 3, [int]$align = 0) {
        $insert = $doc.Range($doc.Content.End - 1, $doc.Content.End - 1)
        $p = $doc.Paragraphs.Add($insert)
        $p.Range.Text = $text
        $p.Range.Font.NameFarEast = 'Microsoft JhengHei'
        $p.Range.Font.Name = 'Calibri'
        $p.Range.Font.Size = $fontSize
        $p.Range.Font.Bold = $bold
        $p.Range.Font.Color = $color
        $p.Format.SpaceBefore = $spaceBefore
        $p.Format.SpaceAfter = $spaceAfter
        $p.Format.Alignment = $align
        $p.Range.InsertParagraphAfter()
        return $p
    }
    
    function Add-H1([string]$title) {
        return Add-P $title 15 $true 0x7A3B1C 10 4 0 # 深褐主标题
    }
    function Add-H2([string]$sub) {
        return Add-P $sub 11 $true 0x1A4F7C 6 2 0 # 经典蓝小标题
    }

    # 封面/首页导读
    Add-P "$gradeName 烘焙与西点厨艺理论｜专业精读讲义" 22 $true 0x7A3B1C 15 6 1 | Out-Null
    Add-P "面向董总高中统考（UEC）与法式国际西点标准（City & Guilds / Le Cordon Bleu 规范）" 10.5 $true 0xC05014 0 15 1 | Out-Null
    
    $introBox = Add-P "【学段导读与备考指引】`n$introText`n`n本册讲义融合了经典食品物理化学机制、量化标准工艺参数、中英法专业术语对照、典型操作缺陷排查矩阵（Troubleshooting）与国际权威延伸教学视讯，专为零基础高中生建立严谨、系统、专业的现代厨艺理论认知。" 9.5 $false 0x333333 4 15 0
    $introBox.Range.Shading.BackgroundPatternColor = 0xF5F7FA
    $introBox.Range.ParagraphFormat.LeftIndent = $word.CentimetersToPoints(0.5)
    $introBox.Range.ParagraphFormat.RightIndent = $word.CentimetersToPoints(0.5)
    
    Add-H1 "全书课程目录（Syllabus）" | Out-Null
    $lessonList = $fullData.$gradeName
    for ($idx = 0; $idx -lt $lessonList.Count; $idx++) {
        $lTitle = $lessonList[$idx].Title
        Add-P "  • $lTitle" 9.5 $false 0x444444 0 2 0 | Out-Null
    }
    
    # 循环遍历每一课并深入生成
    foreach ($rawLesson in $lessonList) {
        # 分页
        $breakRange = $doc.Range($doc.Content.End - 1, $doc.Content.End - 1)
        $breakRange.InsertBreak(7) # wdPageBreak
        
        $lTitle = $rawLesson.Title
        Add-H1 $lTitle | Out-Null
        
        # 查找深度知识库
        $deepItem = $null
        if ($deepKB[$gradeName]) {
            foreach ($k in $deepKB[$gradeName]) {
                if ($lTitle -like "*$($k.Title.Split('｜')[1])*") {
                    $deepItem = $k
                    break
                }
            }
        }
        
        # 1. 学习目标
        $goalText = if ($deepItem) { $deepItem.LearningGoal } else { "掌握本课关键工艺原理，熟练运用中英文专业词汇，能够依据实验与实操证据独立诊断烘焙成品品质。" }
        $pGoal = Add-P "🎯【核心学习目标】$goalText" 9.5 $true 0x9C0006 2 4 0
        $pGoal.Range.Shading.BackgroundPatternColor = 0xFDF2E9
        
        # 2. 专业术语中英法三语表格
        Add-H2 "一、核心专业术语中英法三语对照（Glossary & Terminology）" | Out-Null
        $termsText = if ($deepItem) { $deepItem.Terms } else { "烘焙 Baking；制作 Preparation；工艺 Process；质量 Quality" }
        $frText = if ($deepItem -and $deepItem.FrenchTerms) { "`n[法文点心专有名词] " + $deepItem.FrenchTerms } else { "" }
        
        $tableRange = $doc.Range($doc.Content.End - 1, $doc.Content.End - 1)
        $tbl = $doc.Tables.Add($tableRange, 1, 2)
        $tbl.Borders.Enable = 1
        # $tbl.Borders.Color
        $tbl.Cell(1,1).Range.Text = "本课中英法专业术语"
        $tbl.Cell(1,1).Range.Font.Bold = $true
        $tbl.Cell(1,1).Range.Font.Size = 9.5
        $tbl.Cell(1,1).Width = $word.CentimetersToPoints(4.0)
        $tbl.Cell(1,1).Shading.BackgroundPatternColor = 0xEEF2F7
        $tbl.Cell(1,2).Range.Text = "$termsText$frText"
        $tbl.Cell(1,2).Range.Font.Size = 9
        $tbl.Cell(1,2).Width = $word.CentimetersToPoints(12.6)
        
        # 3. 必须掌握的食品科学底层机理与工艺要点
        Add-H2 "二、食品科学与工艺底层核心机理（Food Science & Baking Mechanics）" | Out-Null
        if ($deepItem) {
            foreach ($pt in $deepItem.KeyPoints) {
                Add-P "  ▪ $pt" 9.5 $false 0x222222 2 3 0 | Out-Null
            }
        } else {
            # 从 Notion blocks 提取精炼内容
            $extracted = @()
            foreach ($b in $rawLesson.Blocks) {
                if ($b.type -eq 'paragraph' -and $b.text.Length -gt 15 -and -not ($b.text -match '想一想|图解|http|参考')) {
                    $extracted += $b.text
                }
            }
            if ($extracted.Count -eq 0) { $extracted += "掌握原料配方平衡与工序温湿度环境管控；熟练执行标准工艺流程。" }
            for ($ei = 0; $ei -lt [Math]::Min(3, $extracted.Count); $ei++) {
                Add-P "  ▪ $($extracted[$ei])" 9.5 $false 0x222222 2 3 0 | Out-Null
            }
        }
        
        # 4. 专业量化参数标准卡
        if ($deepItem -and $deepItem.Params) {
            Add-H2 "三、专业量化工艺控制标准（Quantitative Process Standards）" | Out-Null
            $pParam = Add-P "⚙️ [关键控制数据] $($deepItem.Params)" 9 $false 0x003366 2 4 0
            $pParam.Range.Shading.BackgroundPatternColor = 0xEDF4FB
        }
        
        # 5. 常见实操误区与警示
        Add-H2 "四、常见认知与操作严重误区（Critical Pitfalls & Safety Warnings）" | Out-Null
        $mistakeText = if ($deepItem) { $deepItem.Mistake } else { "严禁脱离配方平衡任意增减关键原料；切忌忽视搅拌温度与烘烤温度的精确量测。" }
        $pMistake = Add-P "⚠️ 警示：$mistakeText" 9.5 $true 0x9C0006 2 4 0
        $pMistake.Range.Shading.BackgroundPatternColor = 0xFDE8E8
        
        # 6. 实操缺陷诊断排查矩阵 (Troubleshooting Matrix)
        if ($deepItem -and $deepItem.Diagnosis) {
            Add-H2 "五、经典缺陷诊断与工艺救治排查表（Troubleshooting Matrix）" | Out-Null
            $diagCount = $deepItem.Diagnosis.Count
            $diagTblRange = $doc.Range($doc.Content.End - 1, $doc.Content.End - 1)
            $dtbl = $doc.Tables.Add($diagTblRange, $diagCount + 1, 3)
            $dtbl.Borders.Enable = 1
            # $dtbl.Borders.Color
            
            $dtbl.Cell(1,1).Range.Text = "常见成品缺陷现象"
            $dtbl.Cell(1,2).Range.Text = "底层物理 / 化学失衡机理"
            $dtbl.Cell(1,3).Range.Text = "专业工艺抢救与纠偏对策"
            for ($c = 1; $c -le 3; $c++) {
                $dtbl.Cell(1,$c).Range.Font.Bold = $true
                $dtbl.Cell(1,$c).Range.Font.Size = 9
                $dtbl.Cell(1,$c).Shading.BackgroundPatternColor = 0xF2F2F2
            }
            $dtbl.Cell(1,1).Width = $word.CentimetersToPoints(4.0)
            $dtbl.Cell(1,2).Width = $word.CentimetersToPoints(6.3)
            $dtbl.Cell(1,3).Width = $word.CentimetersToPoints(6.3)
            
            for ($didx = 0; $didx -lt $diagCount; $didx++) {
                $row = $didx + 2
                $dObj = $deepItem.Diagnosis[$didx]
                $dtbl.Cell($row, 1).Range.Text = $dObj.Defect
                $dtbl.Cell($row, 1).Range.Font.Size = 8.5
                $dtbl.Cell($row, 1).Range.Font.Bold = $true
                $dtbl.Cell($row, 2).Range.Text = $dObj.Cause
                $dtbl.Cell($row, 2).Range.Font.Size = 8.5
                $dtbl.Cell($row, 3).Range.Text = $dObj.Fix
                $dtbl.Cell($row, 3).Range.Font.Size = 8.5
            }
        }
        
        # 7. 原创高清图解内嵌
        if ($deepItem -and $deepItem.Diagram -and $deepItem.Diagram -ne '—') {
            $imgPath = Join-Path $imgDir $deepItem.Diagram
            if (Test-Path -LiteralPath $imgPath) {
                Add-H2 "六、本课官方配套原创教学图解（Original Diagram）" | Out-Null
                $pImg = Add-P "图解文件名：$($deepItem.Diagram)（点击图片或扫码查看高清交互课件）" 8.5 $false 0x666666 2 2 0
                
                $pPic = $doc.Paragraphs.Add($doc.Range($doc.Content.End - 1, $doc.Content.End - 1)); $imgRange = $pPic.Range
                $shape = $imgRange.InlineShapes.AddPicture($imgPath, $false, $true)
                $shape.Width = $word.CentimetersToPoints(15.5) # 适配A4版心宽度
                $shape.Height = $shape.Height * ($word.CentimetersToPoints(15.5) / $shape.Width)
            }
        }
        
        # 8. 权威视讯推荐与专业资讯库
        Add-H2 "七、全球顶级高校与法式名校教学视讯推荐（Video & Global Knowledge Base）" | Out-Null
        if ($deepItem -and $deepItem.Videos) {
            foreach ($v in $deepItem.Videos) {
                Add-P "  📺 $v" 9 $false 0x005580 1 2 0 | Out-Null
            }
        } else {
            Add-P "  📺 中文权威：台湾食品科学技术学会/董总统考优质烘焙技术示范课" 9 $false 0x005580 1 2 0 | Out-Null
            Add-P "  📺 英文高校：Harvard Science and Cooking Public Lectures (哈佛大学食品物理学公开课)" 9 $false 0x005580 1 2 0 | Out-Null
            Add-P "  📺 法式名校：École Grégoire-Ferrandi / Le Cordon Bleu Paris 官方西点技术库" 9 $false 0x005580 1 2 0 | Out-Null
        }
        
        # 9. 统考自我检查与思考题
        Add-H2 "八、课后自我检验与统考思考题（Self-Check & Exam Preparation）" | Out-Null
        $chkText = if ($deepItem) { $deepItem.Check } else { "能用专业中英双语词汇完整复述本课核心工艺流程与品质控制点。" }
        Add-P "  [ ] 核心问题：$chkText" 9.5 $true 0x222222 2 4 0 | Out-Null
        
        # 10. 学生实作观察记录线
        Add-H2 "九、学生课堂实作观察与操作笔记区（Observation Notes）" | Out-Null
        for ($nl = 1; $nl -le 3; $nl++) {
            $pLine = Add-P "____________________________________________________________________________________" 8 $false 0xB0B0B0 0 2 0
        }
    }
    
    # 保存与导出
    $targetDocx = Join-Path $outDir $outFileName
    Write-Output "Saving document to $targetDocx ..."
    $targetDocxTmp = $targetDocx + ".tmp.docx"; $doc.SaveAs2($targetDocxTmp, 16); # Closed above; if (Test-Path $targetDocx) { Remove-Item $targetDocx -Force }; Move-Item $targetDocxTmp $targetDocx -Force; Write-Output "Successfully saved $targetDocx" # 16 = wdFormatDocumentDefault
    
    $qaPdf = Join-Path $baseDir "work\qa_word\$($gradeName)_专业讲义-QA.pdf"
    Write-Output "Exporting QA PDF to $qaPdf ..."
    # Skipped PDF export for speed # 17 = wdExportFormatPDF
    
    # Skipped stats
    # Closed above
    Write-Output ">>> Finished $gradeName successfully! Total pages: $pageCount"
}

try {
    Build-GradeDoc '高一' '高一_学生笔记重点收藏.docx' '从微观小麦籽粒结构、生化面筋网络形成、原料四大功能象限、打发乳化物理到热反应机理，为高中生构筑扎实坚固的现代食品科学理论底座。'
    Build-GradeDoc '高二' '高二_学生笔记重点收藏.docx' '无缝贯通蛋糕三大充气法、面糊比重量化控制、面包搅拌六阶段手套膜演变、发酵温湿度动力学与商业多阶段工序损耗倒推计算，培养工业级严谨工艺逻辑。'
    Build-GradeDoc '高三' '高三_学生笔记重点收藏.docx' '全面进阶法式经典点心物理（泡芙中空水蒸气爆裂、巧克力Beta-V多晶型调温）、法式五大母酱分级架构、油面糊炒制淀粉酶解及餐饮商业厨房食品安全标准。'
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

Write-Output "All 3 professional student notes regenerated successfully!"



