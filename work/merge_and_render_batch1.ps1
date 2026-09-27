$ErrorActionPreference = 'Stop'

$root = (Get-Location).Path
$outDir = (Get-ChildItem -Directory -Filter "08_*").FullName

$filesToLoad = @(
    (Join-Path $root "work\quiz_data_batch1.json"),
    (Join-Path $root "work\lesson3.json"),
    (Join-Path $root "work\lesson4.json"),
    (Join-Path $root "work\lesson5.json")
)

$allLessons = @()

# Load Lesson 2 from quiz_data_batch1.json
$raw2 = [System.IO.File]::ReadAllText($filesToLoad[0], [System.Text.Encoding]::UTF8)
$json2 = $raw2 | ConvertFrom-Json
$allLessons += $json2.lessons[0]

# Load Lessons 3, 4, 5
for ($i = 1; $i -lt $filesToLoad.Count; $i++) {
    $raw = [System.IO.File]::ReadAllText($filesToLoad[$i], [System.Text.Encoding]::UTF8)
    $allLessons += ($raw | ConvertFrom-Json)
}

Write-Host "Loaded $($allLessons.Count) lessons successfully!"

# Write markdown prompt specs
foreach ($les in $allLessons) {
    $mdFileName = $les.paths.file1.Replace(".docx", ".md")
    $mdPath = Join-Path $outDir $mdFileName
    $mdContent = "# " + $les.promptSpec.title + "`r`n`r`n" +
                 "> " + $les.promptSpec.meta.Replace("`n", "`r`n> ") + "`r`n`r`n---`r`n`r`n" +
                 "## " + $les.promptSpec.promptTitle + "`r`n`r`n```markdown`r`n" +
                 $les.promptSpec.promptBody + "`r`n````r`n`r`n---`r`n`r`n" +
                 "## " + $les.promptSpec.designTitle + "`r`n`r`n" +
                 $les.promptSpec.designBody + "`r`n"

    [System.IO.File]::WriteAllText($mdPath, $mdContent, [System.Text.Encoding]::UTF8)
    Write-Host "Wrote MD Prompt Spec: $mdPath"
}

# Start Word COM Automation
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

function Write-SectionHeader($sel, $title) {
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

try {
    foreach ($les in $allLessons) {
        $lNum = $les.lessonNum
        Write-Host "=================================================="
        Write-Host ">>> Processing Lesson $lNum : $($les.lessonTitle)"
        Write-Host "=================================================="

        $f1 = Join-Path $outDir $les.paths.file1
        $f2 = Join-Path $outDir $les.paths.file2
        $f3 = Join-Path $outDir $les.paths.file3
        $imgPathMcq = Join-Path $root $les.paths.imgMcq
        $imgPathCase = Join-Path $root $les.paths.imgCase

        # ----------------------------------------------------------------------
        # Doc 1: Prompt Spec Docx
        # ----------------------------------------------------------------------
        Write-Host "  -> Rendering Doc 1: $f1"
        $doc1 = $word.Documents.Add()
        Setup-Page $doc1 $les.promptSpec.header $les.promptSpec.footer
        $sel = $word.Selection
        $sel.EndKey(6) | Out-Null

        $sel.Font.NameFarEast = "Microsoft YaHei"
        $sel.Font.Name = "Calibri"
        $sel.Font.Size = 18
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.promptSpec.title + "`n`n")

        $sel.Font.Size = 10
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorDark
        $sel.TypeText($les.promptSpec.meta + "`n`n")

        $sel.Font.Size = 13
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorTeal
        $sel.TypeText($les.promptSpec.promptTitle + "`n")

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
        $cP.Text = $les.promptSpec.promptBody
        $sel.EndKey(6) | Out-Null
        $sel.TypeText("`n`n")

        $sel.Font.Size = 13
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorTeal
        $sel.TypeText($les.promptSpec.designTitle + "`n")

        $sel.Font.Size = 10
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorDark
        $sel.TypeText($les.promptSpec.designBody + "`n")

        $doc1.SaveAs([string]$f1)
        $doc1.Close()

        # ----------------------------------------------------------------------
        # Doc 2: Student Quiz Docx
        # ----------------------------------------------------------------------
        Write-Host "  -> Rendering Doc 2: $f2"
        $doc2 = $word.Documents.Add()
        Setup-Page $doc2 $les.studentQuiz.header $les.studentQuiz.footer
        $sel = $word.Selection
        $sel.EndKey(6) | Out-Null

        $sel.ParagraphFormat.Alignment = 1 # Center
        $sel.Font.NameFarEast = "Microsoft YaHei"
        $sel.Font.Name = "Calibri"
        $sel.Font.Size = 16
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.studentQuiz.title + "`n")

        $sel.Font.Size = 14
        $sel.Font.Color = $colorTeal
        $sel.TypeText($les.studentQuiz.subTitle + "`n")

        $sel.Font.Size = 9.5
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorGray
        $sel.TypeText($les.studentQuiz.meta + "`n`n")
        $sel.ParagraphFormat.Alignment = 0 # Left

        # Score Table
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
            $c.Text = $les.studentQuiz.headers[$col-1]
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
        $sel.TypeText("`n" + $les.studentQuiz.infoText + "`n`n")

        # Sec 1: MCQs (All not bold)
        Write-SectionHeader $sel $les.studentQuiz.sec1
        foreach ($m in $les.studentQuiz.mcqs) {
            $sel.Font.Bold = $false
            $sel.Font.Size = 10
            $sel.TypeText($m.q + "`n")

            if ($m.hasImg -and (Test-Path $imgPathMcq)) {
                $shape = $sel.InlineShapes.AddPicture($imgPathMcq)
                $shape.Width = 340
                $sel.TypeText("`n")
            }

            $sel.TypeText("   " + $m.a.PadRight(24) + $m.b + "`n")
            $sel.TypeText("   " + $m.c.PadRight(24) + $m.d + "`n`n")
        }

        # Sec 2: Combos (Aligned Romans, All not bold)
        Write-SectionHeader $sel $les.studentQuiz.sec2
        foreach ($cb in $les.studentQuiz.combos) {
            $sel.Font.Bold = $false
            $sel.Font.Size = 10
            $sel.TypeText($cb.stem + "`n")

            foreach ($r in $cb.romans) {
                $sel.TypeText("   " + $r + "`n")
            }

            $sel.TypeText("   " + $cb.a.PadRight(24) + $cb.b + "`n")
            $sel.TypeText("   " + $cb.c.PadRight(24) + $cb.d + "`n`n")
        }

        # Sec 3: Fills (All not bold)
        Write-SectionHeader $sel $les.studentQuiz.sec3
        foreach ($f in $les.studentQuiz.fills) {
            $sel.Font.Bold = $false
            $sel.Font.Size = 10
            $sel.TypeText($f + "`n`n")
        }

        # Sec 4: Long Questions (All not bold, no answer line, clean blank space)
        Write-SectionHeader $sel $les.studentQuiz.sec4
        foreach ($lq in $les.studentQuiz.longQuestions) {
            $sel.Font.Bold = $false
            $sel.Font.Size = 10
            $sel.TypeText($lq.title + "`n")

            if ($lq.hasImg -and (Test-Path $imgPathCase)) {
                $shape = $sel.InlineShapes.AddPicture($imgPathCase)
                $shape.Width = 330
                $sel.TypeText("`n")
            }

            for ($i = 1; $i -le $lq.blankLines; $i++) {
                $sel.TypeText("`n")
            }
        }

        $doc2.SaveAs([string]$f2)
        $doc2.Close()

        # ----------------------------------------------------------------------
        # Doc 3: Teacher Answer Docx
        # ----------------------------------------------------------------------
        Write-Host "  -> Rendering Doc 3: $f3"
        $doc3 = $word.Documents.Add()
        Setup-Page $doc3 $les.teacherDoc.header $les.teacherDoc.footer
        $sel = $word.Selection
        $sel.EndKey(6) | Out-Null

        $sel.ParagraphFormat.Alignment = 1 # Center
        $sel.Font.NameFarEast = "Microsoft YaHei"
        $sel.Font.Name = "Calibri"
        $sel.Font.Size = 16
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.teacherDoc.title + "`n")

        $sel.Font.Size = 14
        $sel.Font.Color = $colorTeal
        $sel.TypeText($les.teacherDoc.subTitle + "`n")

        $sel.Font.Size = 9.5
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorGray
        $sel.TypeText($les.teacherDoc.meta + "`n`n")
        $sel.ParagraphFormat.Alignment = 0 # Left

        # Quick Answer Table
        $sel.Font.NameFarEast = "Microsoft YaHei"
        $sel.Font.Size = 12
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.teacherDoc.sec1 + "`n")
        $sel.Font.Bold = $false

        $tblAns = $doc3.Tables.Add($sel.Range, 4, 8)
        $tblAns.Borders.Enable = 1
        $tblAns.Borders.OutsideColor = $colorTeal
        $tblAns.Borders.InsideColor = $colorTeal
        $tblAns.Rows.Alignment = 1

        for ($c = 1; $c -le 8; $c++) {
            $tblAns.Cell(1, $c).Range.Text = $les.teacherDoc.tableRow1[$c-1]
            $tblAns.Cell(1, $c).Range.Font.Bold = $true
            $tblAns.Cell(1, $c).Shading.BackgroundPatternColor = $colorLightGray
            $tblAns.Cell(2, $c).Range.Text = $les.teacherDoc.tableRow2[$c-1]
            $tblAns.Cell(2, $c).Range.Font.Bold = $true
            $tblAns.Cell(2, $c).Range.Font.Color = $colorTeal

            $tblAns.Cell(3, $c).Range.Text = $les.teacherDoc.tableRow3[$c-1]
            $tblAns.Cell(3, $c).Range.Font.Bold = $true
            $tblAns.Cell(3, $c).Shading.BackgroundPatternColor = $colorLightGray
            $tblAns.Cell(4, $c).Range.Text = $les.teacherDoc.tableRow4[$c-1]
            $tblAns.Cell(4, $c).Range.Font.Bold = $true
            $tblAns.Cell(4, $c).Range.Font.Color = $colorTeal
        }
        $sel.EndKey(6) | Out-Null
        $sel.Font.Size = 9.5
        $sel.TypeText("`n" + $les.teacherDoc.q15Note + "`n`n")

        # Combos summary
        $sel.Font.Bold = $true
        $sel.Font.Size = 10
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.teacherDoc.combosTitle + "`n")
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorDark
        foreach ($cs in $les.teacherDoc.combosSummary) {
            $sel.TypeText("  " + $cs + "`n")
        }
        $sel.TypeText("`n")

        # Fills summary
        $sel.Font.Bold = $true
        $sel.Font.Size = 10
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.teacherDoc.fillsTitle + "`n")
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorDark
        foreach ($fs in $les.teacherDoc.fillsSummary) {
            $sel.TypeText("  " + $fs + "`n")
        }
        $sel.TypeText("`n")

        # Rubrics
        $sel.Font.NameFarEast = "Microsoft YaHei"
        $sel.Font.Size = 12
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorNavy
        $sel.TypeText($les.teacherDoc.sec2 + "`n`n")

        foreach ($rb in $les.teacherDoc.rubrics) {
            $sel.Font.Bold = $true
            $sel.Font.Size = 11
            $sel.Font.Color = $colorTeal
            $sel.TypeText($rb.num + "`n")
            $sel.Font.Bold = $false
            $sel.Font.Size = 9.5
            $sel.Font.Color = $colorDark
            $sel.TypeText($rb.answer + "`n`n")
        }

        $doc3.SaveAs([string]$f3)
        $doc3.Close()
        Write-Host "  -> Saved all 3 docs for Lesson $lNum successfully!"
    }
} finally {
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}

Write-Host "All Batch 1 lessons (2, 3, 4, 5) generated completely!"
