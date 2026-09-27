$ErrorActionPreference = 'Stop'

$root = (Get-Location).Path
$jsonPath = Join-Path $root "work\quiz_data_lesson1.json"

if (-not (Test-Path $jsonPath)) {
    throw "Cannot find json data file at $jsonPath"
}

$rawJson = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
$data = $rawJson | ConvertFrom-Json

$outDir = Join-Path $root $data.paths.outDir
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$file1 = Join-Path $outDir $data.paths.file1
$file2 = Join-Path $outDir $data.paths.file2
$file3 = Join-Path $outDir $data.paths.file3

$imgTherm = Join-Path $root $data.paths.imgTherm
$imgDefect = Join-Path $root $data.paths.imgDefect

Write-Host "Data and paths loaded successfully!"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$colorNavy  = 0x5D361A  # #1A365D Deep Navy
$colorTeal  = 0x88940D  # #0D9488 Teal Accent
$colorGray  = 0x666666  # Gray
$colorDark  = 0x222222  # Body text
$colorLight = 0xF5F2EF  # Light background #EFFAF2
$colorLightGray = 0xF8FAFC

function Setup-Page($doc, $headerText, $footerText) {
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
    $ftr.Text = $footerText
    $ftr.Font.NameFarEast = "Microsoft YaHei"
    $ftr.Font.Name = "Calibri"
    $ftr.Font.Size = 8.5
    $ftr.Font.Color = $colorGray
    $ftr.ParagraphFormat.Alignment = 1
}

# ==============================================================================
# Doc 1: Prompt Spec
# ==============================================================================
Write-Host ">>> Generating Doc 1: Prompt Spec..."
$doc1 = $word.Documents.Add()
Setup-Page $doc1 $data.promptSpec.header $data.promptSpec.footer

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 18
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($data.promptSpec.title + "`n`n")

$sel.Font.Size = 10
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText($data.promptSpec.meta + "`n`n")

$sel.Font.Size = 13
$sel.Font.Bold = $true
$sel.Font.Color = $colorTeal
$sel.TypeText($data.promptSpec.promptTitle + "`n")

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
$cP.Text = $data.promptSpec.promptBody
$sel.EndKey(6) | Out-Null
$sel.TypeText("`n`n")

$sel.Font.Size = 13
$sel.Font.Bold = $true
$sel.Font.Color = $colorTeal
$sel.TypeText($data.promptSpec.designTitle + "`n")

$sel.Font.Size = 10
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
$sel.TypeText($data.promptSpec.designBody + "`n")

$doc1.SaveAs([string]$file1)
$doc1.Close()
Write-Host "  -> Saved: $file1"

# ==============================================================================
# Doc 2: Student Quiz
# ==============================================================================
Write-Host ">>> Generating Doc 2: Student Quiz..."
$doc2 = $word.Documents.Add()
Setup-Page $doc2 $data.studentQuiz.header $data.studentQuiz.footer

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

$sel.ParagraphFormat.Alignment = 1 # Center
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 16
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($data.studentQuiz.title + "`n")

$sel.Font.Size = 14
$sel.Font.Color = $colorTeal
$sel.TypeText($data.studentQuiz.subTitle + "`n")

$sel.Font.Size = 9.5
$sel.Font.Bold = $false
$sel.Font.Color = $colorGray
$sel.TypeText($data.studentQuiz.meta + "`n`n")
$sel.ParagraphFormat.Alignment = 0 # Left

# Table for Scores
$tblScore = $doc2.Tables.Add($sel.Range, 2, 5)
$tblScore.Borders.Enable = 1
$tblScore.Borders.OutsideColor = $colorTeal
$tblScore.Borders.InsideColor = $colorTeal
$tblScore.Rows.Alignment = 1
for ($col = 1; $col -le 5; $col++) {
    $c = $tblScore.Cell(1, $col).Range
    $c.Font.NameFarEast = "Microsoft YaHei"
    $c.Font.Size = 9
    $c.Font.Bold = $true
    $c.Font.Color = $colorNavy
    $c.Text = $data.studentQuiz.headers[$col-1]
    $c.ParagraphFormat.Alignment = 1
    $tblScore.Cell(1, $col).Shading.BackgroundPatternColor = $colorLightGray

    $c2 = $tblScore.Cell(2, $col).Range
    $c2.Font.NameFarEast = "Microsoft YaHei"
    $c2.Font.Size = 11
    $c2.Text = " "
    $c2.ParagraphFormat.Alignment = 1
}
$sel.EndKey(6) | Out-Null

$sel.Font.Size = 10
$sel.Font.Color = $colorDark
$sel.TypeText("`n" + $data.studentQuiz.infoText + "`n`n")

function Write-Section($title) {
    $sel.Font.NameFarEast = "Microsoft YaHei"
    $sel.Font.Size = 11
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.TypeText("----------------------------------------------------------------------------------------------------`n")
    $sel.TypeText("$title`n")
    $sel.TypeText("----------------------------------------------------------------------------------------------------`n")
    $sel.Font.Bold = $false
    $sel.Font.Color = $colorDark
}

# Section 1: MCQs (All questions not bold)
Write-Section $data.studentQuiz.sec1
foreach ($m in $data.studentQuiz.mcqs) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($m.q + "`n")

    if ($m.hasImg -and (Test-Path $imgTherm)) {
        $shape = $sel.InlineShapes.AddPicture($imgTherm)
        $shape.Width = 340
        $sel.TypeText("`n")
    }

    $sel.TypeText("   " + $m.a.PadRight(24) + $m.b + "`n")
    $sel.TypeText("   " + $m.c.PadRight(24) + $m.d + "`n`n")
}

# Section 2: Combos (Neatly aligned roman statements, all not bold)
Write-Section $data.studentQuiz.sec2
foreach ($cb in $data.studentQuiz.combos) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($cb.stem + "`n")

    # Each Roman numeral on its own indented line for perfect alignment
    foreach ($r in $cb.romans) {
        $sel.TypeText("   " + $r + "`n")
    }

    $sel.TypeText("   " + $cb.a.PadRight(24) + $cb.b + "`n")
    $sel.TypeText("   " + $cb.c.PadRight(24) + $cb.d + "`n`n")
}

# Section 3: Fills (All not bold)
Write-Section $data.studentQuiz.sec3
foreach ($f in $data.studentQuiz.fills) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($f + "`n`n")
}

# Section 4: Long Questions (All not bold, no answer lines, clean blank space)
Write-Section $data.studentQuiz.sec4
foreach ($lq in $data.studentQuiz.longQuestions) {
    $sel.Font.Bold = $false
    $sel.Font.Size = 10
    $sel.TypeText($lq.title + "`n")

    if ($lq.hasImg -and (Test-Path $imgDefect)) {
        $shape = $sel.InlineShapes.AddPicture($imgDefect)
        $shape.Width = 330
        $sel.TypeText("`n")
    }

    # Clean empty space for student writing without "答：____"
    for ($i = 1; $i -le $lq.blankLines; $i++) {
        $sel.TypeText("`n")
    }
}

$doc2.SaveAs([string]$file2)
$doc2.Close()
Write-Host "  -> Saved: $file2"

# ==============================================================================
# Doc 3: Teacher Answer Docx
# ==============================================================================
Write-Host ">>> Generating Doc 3: Teacher Key..."
$doc3 = $word.Documents.Add()
Setup-Page $doc3 $data.teacherDoc.header $data.teacherDoc.footer

$sel = $word.Selection
$sel.EndKey(6) | Out-Null

$sel.ParagraphFormat.Alignment = 1 # Center
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Name = "Calibri"
$sel.Font.Size = 16
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($data.teacherDoc.title + "`n")

$sel.Font.Size = 14
$sel.Font.Color = $colorTeal
$sel.TypeText($data.teacherDoc.subTitle + "`n")

$sel.Font.Size = 9.5
$sel.Font.Bold = $false
$sel.Font.Color = $colorGray
$sel.TypeText($data.teacherDoc.meta + "`n`n")
$sel.ParagraphFormat.Alignment = 0 # Left

# Section 1: Objective Answer Table
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Size = 12
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($data.teacherDoc.sec1 + "`n")
$sel.Font.Bold = $false

$tblAns = $doc3.Tables.Add($sel.Range, 4, 8)
$tblAns.Borders.Enable = 1
$tblAns.Borders.OutsideColor = $colorTeal
$tblAns.Borders.InsideColor = $colorTeal
$tblAns.Rows.Alignment = 1

for ($c = 1; $c -le 8; $c++) {
    $tblAns.Cell(1, $c).Range.Text = $data.teacherDoc.tableRow1[$c-1]
    $tblAns.Cell(1, $c).Range.Font.Bold = $true
    $tblAns.Cell(1, $c).Shading.BackgroundPatternColor = $colorLightGray
    $tblAns.Cell(2, $c).Range.Text = $data.teacherDoc.tableRow2[$c-1]
    $tblAns.Cell(2, $c).Range.Font.Bold = $true
    $tblAns.Cell(2, $c).Range.Font.Color = $colorTeal

    $tblAns.Cell(3, $c).Range.Text = $data.teacherDoc.tableRow3[$c-1]
    $tblAns.Cell(3, $c).Range.Font.Bold = $true
    $tblAns.Cell(3, $c).Shading.BackgroundPatternColor = $colorLightGray
    $tblAns.Cell(4, $c).Range.Text = $data.teacherDoc.tableRow4[$c-1]
    $tblAns.Cell(4, $c).Range.Font.Bold = $true
    $tblAns.Cell(4, $c).Range.Font.Color = $colorTeal
}
$sel.EndKey(6) | Out-Null
$sel.Font.Size = 9.5
$sel.TypeText("`n" + $data.teacherDoc.q15Note + "`n`n")

# Combos
$sel.Font.Bold = $true
$sel.Font.Size = 10
$sel.Font.Color = $colorNavy
$sel.TypeText($data.teacherDoc.combosTitle + "`n")
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
foreach ($cs in $data.teacherDoc.combosSummary) {
    $sel.TypeText("  " + $cs + "`n")
}
$sel.TypeText("`n")

# Fills
$sel.Font.Bold = $true
$sel.Font.Size = 10
$sel.Font.Color = $colorNavy
$sel.TypeText($data.teacherDoc.fillsTitle + "`n")
$sel.Font.Bold = $false
$sel.Font.Color = $colorDark
foreach ($fs in $data.teacherDoc.fillsSummary) {
    $sel.TypeText("  " + $fs + "`n")
}
$sel.TypeText("`n")

# Section 2: Rubrics
$sel.Font.NameFarEast = "Microsoft YaHei"
$sel.Font.Size = 12
$sel.Font.Bold = $true
$sel.Font.Color = $colorNavy
$sel.TypeText($data.teacherDoc.sec2 + "`n`n")

foreach ($rb in $data.teacherDoc.rubrics) {
    $sel.Font.Bold = $true
    $sel.Font.Size = 11
    $sel.Font.Color = $colorTeal
    $sel.TypeText($rb.num + "`n")
    $sel.Font.Bold = $false
    $sel.Font.Size = 9.5
    $sel.Font.Color = $colorDark
    $sel.TypeText($rb.answer + "`n`n")
}

$doc3.SaveAs([string]$file3)
$doc3.Close()
Write-Host "  -> Saved: $file3"

$word.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
Write-Host "All 3 Word documents generated successfully!"
