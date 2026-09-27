$ErrorActionPreference = 'Stop'

$source = 'C:\Users\GOH\Desktop\2026年统考厨艺理论\03_Notion教学讲义\原创图解上传清单.md'
$output = 'C:\Users\GOH\Desktop\2026年统考厨艺理论\03_Notion教学讲义\原创图解上传清单.docx'
$pdfQa = 'C:\Users\GOH\Desktop\2026年统考厨艺理论\work\原创图解上传清单-QA.pdf'

if (-not (Test-Path -LiteralPath $source)) { throw "找不到来源文件：$source" }

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    $doc = $word.Documents.Add()
    $section = $doc.Sections.Item(1)
    $section.PageSetup.PaperSize = 2 # wdPaperLetter
    $section.PageSetup.TopMargin = $word.InchesToPoints(0.78)
    $section.PageSetup.BottomMargin = $word.InchesToPoints(0.72)
    $section.PageSetup.LeftMargin = $word.InchesToPoints(0.82)
    $section.PageSetup.RightMargin = $word.InchesToPoints(0.82)
    $section.PageSetup.HeaderDistance = $word.InchesToPoints(0.35)
    $section.PageSetup.FooterDistance = $word.InchesToPoints(0.35)

    $styles = $doc.Styles
    $normal = $styles.Item('Normal')
    $normal.Font.NameFarEast = 'Microsoft JhengHei'
    $normal.Font.Name = 'Calibri'
    $normal.Font.Size = 10.5
    $normal.ParagraphFormat.SpaceAfter = 5
    $normal.ParagraphFormat.LineSpacingRule = 5 # multiple
    $normal.ParagraphFormat.LineSpacing = 14

    foreach ($styleName in @('Title','Heading 1','Heading 2')) {
        $s = $styles.Item($styleName)
        $s.Font.NameFarEast = 'Microsoft JhengHei'
        $s.Font.Name = 'Calibri'
    }
    $styles.Item('Title').Font.Size = 24
    $styles.Item('Title').Font.Bold = $true
    $styles.Item('Title').Font.Color = 0x783F1F
    $styles.Item('Title').ParagraphFormat.SpaceAfter = 5
    $styles.Item('Heading 1').Font.Size = 15
    $styles.Item('Heading 1').Font.Bold = $true
    $styles.Item('Heading 1').Font.Color = 0xB57420
    $styles.Item('Heading 1').ParagraphFormat.SpaceBefore = 12
    $styles.Item('Heading 1').ParagraphFormat.SpaceAfter = 6
    $styles.Item('Heading 2').Font.Size = 12
    $styles.Item('Heading 2').Font.Bold = $true
    $styles.Item('Heading 2').Font.Color = 0x5A5A5A
    $styles.Item('Heading 2').ParagraphFormat.SpaceBefore = 8
    $styles.Item('Heading 2').ParagraphFormat.SpaceAfter = 4

    $header = $section.Headers.Item(1).Range
    $header.Text = '2026 高中厨艺（烘焙理论）｜原创教学图解'
    $header.Font.NameFarEast = 'Microsoft JhengHei'
    $header.Font.Size = 8.5
    $header.Font.Color = 0x777777
    $header.ParagraphFormat.Alignment = 2

    $footer = $section.Footers.Item(1).Range
    $footer.ParagraphFormat.Alignment = 1
    $footer.Font.NameFarEast = 'Microsoft JhengHei'
    $footer.Font.Size = 8.5
    $footer.Font.Color = 0x777777
    $footer.Text = '教师工作清单｜'
    $footer.Collapse(0)
    $footer.Fields.Add($footer, 33) | Out-Null # wdFieldPage

    function Add-Para([string]$text, [string]$style = 'Normal', [bool]$keepNext = $false) {
        $insert = $doc.Range($doc.Content.End - 1, $doc.Content.End - 1)
        $p = $doc.Paragraphs.Add($insert)
        $p.Range.Text = $text
        $p.Range.Style = $styles.Item($style)
        $p.Format.KeepWithNext = $keepNext
        $p.Range.InsertParagraphAfter()
        return $p
    }

    function Add-Check([string]$text) {
        $p = Add-Para "☐  $text"
        $p.Format.LeftIndent = $word.InchesToPoints(0.18)
        $p.Format.FirstLineIndent = 0
        $p.Format.SpaceAfter = 4
        return $p
    }

    $title = Add-Para '原创图解上传清单' 'Title' $true
    $sub = Add-Para '2026 高中厨艺（烘焙理论）｜Notion 人工上传与复核用'
    $sub.Range.Font.NameFarEast = 'Microsoft JhengHei'
    $sub.Range.Font.Size = 11
    $sub.Range.Font.Color = 0x666666
    $sub.Format.SpaceAfter = 11

    $note = Add-Para '使用说明：11张图片均已完成内容审核。请把原尺寸 PNG 拖入指定 Notion 课页，上传后补上替代文字（Alt text），并以手机和课堂投影检查可读性。'
    $note.Range.Shading.BackgroundPatternColor = 0xEAF4FB
    $note.Range.ParagraphFormat.LeftIndent = $word.InchesToPoints(0.16)
    $note.Range.ParagraphFormat.RightIndent = $word.InchesToPoints(0.16)
    $note.Range.ParagraphFormat.SpaceBefore = 6
    $note.Range.ParagraphFormat.SpaceAfter = 10

    Add-Para '一、上传清单' 'Heading 1' $true | Out-Null
    $items = @(
        '01｜烘焙过程总览 v2 → 高一第1课｜烘焙概论',
        '02｜烘焙原料功能关系图 → 高一第9课',
        '03｜面筋形成与面团搅拌阶段图 → 高一第10课；高二第7单元',
        '04｜酵母发酵三阶段与产气关系图 → 高一第15课；高二第8单元',
        '05｜蛋白霜四种状态与失败判断图 → 高一第13课；高二第2单元',
        '06｜乳化成功、分离与修复关系图 → 高一第17课；高二第4单元',
        '07｜蛋糕面糊比重测量步骤图 → 高二第3单元',
        '08｜巧克力结晶与调温关系图 → 补充专题A',
        '09｜泡芙空腔形成剖面时间线 → 高三第4单元',
        '10｜多阶段损耗倒推计算图 → 高二第10单元；公式与计算训练',
        '11｜生熟分区与冷藏架位图 → 高二第14单元；食品安全教学补充'
    )
    foreach ($item in $items) { Add-Check $item | Out-Null }

    Add-Para '二、上传后检查' 'Heading 1' $true | Out-Null
    $checks = @(
        '使用图片文件夹中的原尺寸 PNG，不使用聊天截图。',
        '图片放在相关概念或步骤之后，不集中堆在页面末端。',
        '加入各课页已经登记的替代文字（Alt text）。',
        '手机预览可辨认标题、阶段名称和警告框。',
        '教室投影时最小文字仍可读。',
        '数学图重新检查公式、数字、单位和取整。',
        '食品安全图对照学校 SOP；若学校规定更严格，以学校规定为准。',
        '图片下方注明“原创教学图解｜2026课程”。',
        '完成后把 Notion 媒体页状态改为“已上传并复核”。'
    )
    foreach ($item in $checks) { Add-Check $item | Out-Null }

    Add-Para '三、文件位置与规格' 'Heading 1' $true | Out-Null
    Add-Para '正式图片文件夹：03_Notion教学讲义/图片/（共11张正式 PNG）' | Out-Null
    Add-Para '16:9：01-v2、02、03、05。' | Out-Null
    Add-Para '3:2：04、06、07、08、09、10、11。' | Out-Null
    Add-Para '尺寸：1536×1024 至 1672×941；单张约 1.5–2.3 MB。' | Out-Null

    Add-Para '四、旧稿说明' 'Heading 1' $true | Out-Null
    $old = Add-Para '旧稿位置：03_Notion教学讲义/图片/旧稿/01-烘焙过程总览.png。此图只留档，不再使用。正式上传 01-烘焙过程总览-v2.png；v2 已明确区分真实炉内画面与“剖面示意”。'
    $old.Range.Shading.BackgroundPatternColor = 0xE6F0FF

    Add-Para '五、完成记录' 'Heading 1' $true | Out-Null
    Add-Check '11张图片均已上传至对应 Notion 课页。' | Out-Null
    Add-Check '所有图片均已补上替代文字（Alt text）。' | Out-Null
    Add-Check '已完成手机预览与教室投影检查。' | Out-Null
    Add-Para '完成日期：__________________    检查人：__________________' | Out-Null

    $doc.SaveAs2($output, 16) # wdFormatDocumentDefault (.docx)
    $doc.ExportAsFixedFormat($pdfQa, 17) # wdExportFormatPDF
    $doc.Close($false)
}
finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

Get-Item -LiteralPath $output, $pdfQa | Select-Object FullName, Length, LastWriteTime
