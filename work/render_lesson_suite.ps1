# Pure ASCII PowerShell script to render Word documents and Markdown for any lesson
param(
    [string]$JsonFile
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path $JsonFile)) {
    throw "JSON file not found: $JsonFile"
}

$rawJson = [System.IO.File]::ReadAllText($JsonFile, [System.Text.Encoding]::UTF8)
$lessonData = $rawJson | ConvertFrom-Json

$root = (Get-Location).Path
$outDir = Join-Path $root $lessonData.paths.outDir
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$file1Docx = Join-Path $outDir $lessonData.paths.file1Docx
$file1Md   = Join-Path $outDir $lessonData.paths.file1Md
$file2Docx = Join-Path $outDir $lessonData.paths.file2Docx
$file3Docx = Join-Path $outDir $lessonData.paths.file3Docx

$imgQ10 = Join-Path $root $lessonData.paths.imgQ10
$imgQ35 = Join-Path $root $lessonData.paths.imgQ35

# 1. Output Markdown Prompt Spec File
Write-Host ">>> Writing Markdown Prompt Spec: $file1Md"
[System.IO.File]::WriteAllText($file1Md, $lessonData.promptMdContent, [System.Text.Encoding]::UTF8)

# 2. Start Word COM
Write-Host ">>> Starting Word COM Automation..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$colorNavy      = 0x5D361A  # Deep Navy
$colorTeal      = 0x88940D  # Teal Accent
$colorGray      = 0x666666  # Gray
$colorDark      = 0x222222  # Body text
$colorLight     = 0xF5F2EF  # Light background
$colorLightGray = 0xF8FAFC  # Soft table header background

function Setup-DocPage($doc, $headerText, $footerText) {
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
    $hdr.ParagraphFormat.Alignment = 2 # Right

    $ftr = $sec.Footers.Item(1).Range
    $ftr.Text = $footerText
    $ftr.Font.NameFarEast = "Microsoft YaHei"
    $ftr.Font.Name = "Calibri"
    $ftr.Font.Size = 8.5
    $ftr.Font.Color = $colorGray
    $ftr.ParagraphFormat.Alignment = 1 # Center
}

# ==============================================================================
# DOC 1: PROMPT SPEC DOCX
# ==============================================================================
Write-Host ">>> Generating Doc 1: Prompt Spec Docx..."
$doc1 = $word.Documents.Add()
Setup-DocPage $doc1 $lessonData.promptSpec.header $lessonData.promptSpec.footer

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 18
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.promptSpec.title + "`n`n")

$sel.Font.Size = 10
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText($lessonData.promptSpec.meta + "`n`n")

$sel.Font.Size = 13
$sel.Font.Bold = $true
$sel.Font.Color = $colorTeal
$sel.TypeText($lessonData.promptSpec.promptTitle + "`n")

$tblP = $doc1.Tables.Add($sel.Range, 1, 1)
$tblP.Borders.Enable = 1
$tblP.Borders.OutsideColor = $colorTeal
$tblP.Borders.InsideColor = $colorTeal
$tblP.Shading.BackgroundPatternColor = $colorLight
$cP = $tblP.Cell(1, 1).Range
$cP.Font.NameFarEast = "Microsoft YaHei"
$cP.Font.Name = "Calibri"
$cP.Font.Size = 9.5
$cP.Font.Color = $colorDark
$cP.Text = $lessonData.promptSpec.promptBody

$sel.EndKey(6) | Out-Null
$sel.Font.Size = 13
$sel.Font.Bold = $true
$sel.Font.Color = $colorTeal
$sel.TypeText("`n`n" + $lessonData.promptSpec.specTitle + "`n")

$tblS = $doc1.Tables.Add($sel.Range, 1, 1)
$tblS.Borders.Enable = 1
$tblS.Borders.OutsideColor = $colorNavy
$tblS.Borders.InsideColor = $colorNavy
$tblS.Shading.BackgroundPatternColor = $colorLightGray
$cS = $tblS.Cell(1, 1).Range
$cS.Font.NameFarEast = "Microsoft YaHei"
$cS.Font.Name = "Calibri"
$cS.Font.Size = 9.5
$cS.Font.Color = $colorDark
$cS.Text = $lessonData.promptSpec.specBody

$doc1.SaveAs([string]$file1Docx)
$doc1.Close()
Write-Host "  -> Saved: $file1Docx"

# ==============================================================================
# DOC 2: STUDENT QUIZ DOCX
# ==============================================================================
Write-Host ">>> Generating Doc 2: Student Quiz Docx..."
$doc2 = $word.Documents.Add()
Setup-DocPage $doc2 $lessonData.studentQuiz.header $lessonData.studentQuiz.footer

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

# School and Exam Header
$sel.ParagraphFormat.Alignment = 1 # Center
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 16
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.studentQuiz.title + "`n")

$sel.Font.Size = 14
$sel.Font.Color = $colorTeal
$sel.TypeText($lessonData.studentQuiz.subTitle + "`n")

$sel.Font.Size = 10
$sel.Font.Bold = $false
$sel.Font.Color = $colorGray
$sel.TypeText($lessonData.studentQuiz.metaInfo + "`n`n")
$sel.ParagraphFormat.Alignment = 0 # Left

# Student Info Table
$tblInfo = $doc2.Tables.Add($sel.Range, 1, 4)
$tblInfo.Borders.Enable = 1
$tblInfo.Borders.OutsideColor = $colorTeal
$tblInfo.Borders.InsideColor = $colorTeal
$tblInfo.Rows.Alignment = 1

$tblInfo.Cell(1, 1).Range.Text = $lessonData.studentQuiz.infoLabel1
$tblInfo.Cell(1, 1).Range.Font.Bold = $true
$tblInfo.Cell(1, 2).Range.Text = ""
$tblInfo.Cell(1, 3).Range.Text = $lessonData.studentQuiz.infoLabel2
$tblInfo.Cell(1, 3).Range.Font.Bold = $true
$tblInfo.Cell(1, 4).Range.Text = ""

$sel.EndKey(6) | Out-Null
$sel.TypeText("`n")

function Write-SectionHeader($secTitle) {
    $sel.Font.NameFarEast = "Microsoft YaHei"
    $sel.Font.Name = "Calibri"
    $sel.Font.Size = 11.5
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.TypeText("`n" + $secTitle + "`n`n")
    $sel.Font.Bold = $false
    $sel.Font.Color = $colorDark
}

# Section 1: Single Choice (15 MCQs, UNBOLDED)
Write-SectionHeader $lessonData.studentQuiz.sec1
foreach ($m in $lessonData.studentQuiz.mcqs) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($m.stem + "`n")

    if ($m.hasImg -and (Test-Path $imgQ10)) {
        $shape = $sel.InlineShapes.AddPicture($imgQ10)
        $shape.Width = 320
        $sel.TypeText("`n")
    }

    $sel.TypeText("   " + $m.a.PadRight(24) + $m.b + "`n")
    $sel.TypeText("   " + $m.c.PadRight(24) + $m.d + "`n`n")
}

# Section 2: Combos (5 Combo Questions, UNBOLDED, Aligned Roman Statements)
Write-SectionHeader $lessonData.studentQuiz.sec2
foreach ($cb in $lessonData.studentQuiz.combos) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($cb.stem + "`n")

    foreach ($r in $cb.romans) {
        $sel.TypeText("   " + $r + "`n")
    }

    $sel.TypeText("   " + $cb.a.PadRight(24) + $cb.b + "`n")
    $sel.TypeText("   " + $cb.c.PadRight(24) + $cb.d + "`n`n")
}

# Section 3: Fills (10 Fills, UNBOLDED)
Write-SectionHeader $lessonData.studentQuiz.sec3
foreach ($f in $lessonData.studentQuiz.fills) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($f + "`n`n")
}

# Section 4: Long Questions (5 Questions, UNBOLDED, Clean Blank Lines)
Write-SectionHeader $lessonData.studentQuiz.sec4
foreach ($lq in $lessonData.studentQuiz.longQuestions) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($lq.title + "`n")

    if ($lq.hasImg -and (Test-Path $imgQ35)) {
        $shape = $sel.InlineShapes.AddPicture($imgQ35)
        $shape.Width = 330
        $sel.TypeText("`n")
    }

    for ($i = 1; $i -le $lq.blankLines; $i++) {
        $sel.TypeText("_______________________________________________________________________________`n")
    }
    $sel.TypeText("`n")
}

$doc2.SaveAs([string]$file2Docx)
$doc2.Close()
Write-Host "  -> Saved: $file2Docx"

# ==============================================================================
# DOC 3: TEACHER ANSWER AND RUBRICS DOCX
# ==============================================================================
Write-Host ">>> Generating Doc 3: Teacher Key and Rubrics..."
$doc3 = $word.Documents.Add()
Setup-DocPage $doc3 $lessonData.teacherDoc.header $lessonData.teacherDoc.footer

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

$sel.ParagraphFormat.Alignment = 1 # Center
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 16
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.teacherDoc.title + "`n")

$sel.Font.Size = 14
$sel.Font.Color = $colorTeal
$sel.TypeText($lessonData.teacherDoc.subTitle + "`n")

$sel.Font.Size = 9.5
$sel.Font.Bold = $false
$sel.Font.Color = $colorGray
$sel.TypeText($lessonData.teacherDoc.meta + "`n`n")
$sel.ParagraphFormat.Alignment = 0 # Left

# Section 1: Answer Key Grid
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Size = 12
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.teacherDoc.sec1 + "`n")
$sel.Font.Bold = $false

$tblAns = $doc3.Tables.Add($sel.Range, 4, 8)
$tblAns.Borders.Enable = 1
$tblAns.Borders.OutsideColor = $colorTeal
$tblAns.Borders.InsideColor = $colorTeal
$tblAns.Rows.Alignment = 1

for ($c = 1; $c -le 8; $c++) {
    $tblAns.Cell(1, $c).Range.Text = $lessonData.teacherDoc.tableRow1[$c-1]
    $tblAns.Cell(1, $c).Range.Font.Bold = $true
    $tblAns.Cell(1, $c).Shading.BackgroundPatternColor = $colorLightGray
    $tblAns.Cell(2, $c).Range.Text = $lessonData.teacherDoc.tableRow2[$c-1]
    $tblAns.Cell(2, $c).Range.Font.Bold = $true
    $tblAns.Cell(2, $c).Range.Font.Color = $colorTeal

    $tblAns.Cell(3, $c).Range.Text = $lessonData.teacherDoc.tableRow3[$c-1]
    $tblAns.Cell(3, $c).Range.Font.Bold = $true
    $tblAns.Cell(3, $c).Shading.BackgroundPatternColor = $colorLightGray
    $tblAns.Cell(4, $c).Range.Text = $lessonData.teacherDoc.tableRow4[$c-1]
    $tblAns.Cell(4, $c).Range.Font.Bold = $true
    $tblAns.Cell(4, $c).Range.Font.Color = $colorTeal
}
$sel.EndKey(6) | Out-Null
$sel.Font.Size = 9.5
$sel.TypeText("`n" + $lessonData.teacherDoc.q15Note + "`n`n")

# Combos Summary
$sel.Font.Bold = $true
$sel.Font.Size = 10
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.teacherDoc.combosTitle + "`n")
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
foreach ($cs in $lessonData.teacherDoc.combosSummary) {
    $sel.TypeText("  " + $cs + "`n")
}
$sel.TypeText("`n")

# Fills Summary
$sel.Font.Bold = $true
$sel.Font.Size = 10
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.teacherDoc.fillsTitle + "`n")
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
foreach ($fs in $lessonData.teacherDoc.fillsSummary) {
    $sel.TypeText("  " + $fs + "`n")
}
$sel.TypeText("`n")

# Section 2: Rubrics
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Size = 12
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($lessonData.teacherDoc.sec2 + "`n`n")

foreach ($rb in $lessonData.teacherDoc.rubrics) {
    $sel.Font.Bold = $true
    $sel.Font.Size = 11
    $sel.Font.Color = $colorTeal
    $sel.TypeText($rb.num + "`n")
    $sel.Font.Bold = $false
    $sel.Font.Size = 9.5
    $sel.Font.Color = $colorDark
    $sel.TypeText($rb.answer + "`n`n")
}

$doc3.SaveAs([string]$file3Docx)
$doc3.Close()
Write-Host "  -> Saved: $file3Docx"

$word.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
Write-Host "All documents generated successfully for $($lessonData.promptSpec.title)!"
