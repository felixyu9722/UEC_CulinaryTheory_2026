[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Stop'

$jsonPath = Join-Path $PSScriptRoot "data\prompt_doc_strings.json"
$jsonRaw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
$data = ConvertFrom-Json $jsonRaw

$rootDir = Split-Path -Parent $PSScriptRoot
$outFiles = @()
foreach ($rel in $data.outFiles) {
    $outFiles += (Join-Path $rootDir $rel)
}

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$colorNavy  = 0x5D361A  # Deep Navy #1A365D
$colorTeal  = 0x88940D  # Teal #0D9488
$colorGray  = 0x707070  # Subtext
$colorDark  = 0x222222  # Body text
$colorBgBox = 0xF9F9F8  # Light box bg

try {
    $doc = $word.Documents.Add()

    # Page Setup
    $sec = $doc.Sections.Item(1)
    $sec.PageSetup.PaperSize = 9 # wdPaperA4
    $sec.PageSetup.TopMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.BottomMargin = $word.CentimetersToPoints(2.0)
    $sec.PageSetup.LeftMargin = $word.CentimetersToPoints(2.2)
    $sec.PageSetup.RightMargin = $word.CentimetersToPoints(2.2)

    # Header & Footer
    $hdr = $sec.Headers.Item(1).Range
    $hdr.Text = $data.docHeader
    $hdr.Font.NameFarEast = "Microsoft YaHei"
    $hdr.Font.Name = "Calibri"
    $hdr.Font.Size = 9
    $hdr.Font.Color = $colorGray
    $hdr.ParagraphFormat.Alignment = 2 # Right

    $ftr = $sec.Footers.Item(1).Range
    $ftr.Text = $data.docFooter
    $ftr.Font.NameFarEast = "Microsoft YaHei"
    $ftr.Font.Name = "Calibri"
    $ftr.Font.Size = 8.5
    $ftr.Font.Color = $colorGray
    $ftr.ParagraphFormat.Alignment = 1 # Center

    $sel = $word.Selection
    $sel.EndKey(6) | Out-Null

    # Main Document Title
    $sel.Font.NameFarEast = "Microsoft YaHei"
    $sel.Font.Name = "Calibri"
    $sel.Font.Size = 18
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.ParagraphFormat.Alignment = 0 # Left
    $sel.ParagraphFormat.SpaceAfter = 6
    $sel.TypeText($data.docTitle + "`n")

    # Metadata Box
    $tblMeta = $doc.Tables.Add($sel.Range, 1, 1)
    $tblMeta.Borders.Enable = 1
    try { $tblMeta.Borders.OutsideColor = $colorTeal } catch {}
    $tblMeta.Shading.BackgroundPatternColor = 0xF4FBF7
    $cMeta = $tblMeta.Cell(1, 1).Range
    $cMeta.Font.NameFarEast = "Microsoft YaHei"
    $cMeta.Font.Name = "Calibri"
    $cMeta.Font.Size = 9.5
    $cMeta.Font.Color = $colorDark
    $cMeta.Text = $data.metaInfo
    $sel.EndKey(6) | Out-Null
    $sel.TypeParagraph()

    # Section 1: Exam analysis
    $sel.Font.Size = 14
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.ParagraphFormat.SpaceBefore = 8
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($data.sec1Title + "`n")

    $sel.Font.Size = 10.5
    $sel.Font.Bold = $false
    $sel.Font.Color = $colorDark
    $sel.ParagraphFormat.SpaceBefore = 0
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($data.sec1P1 + "`n`n")

    # 4 Features
    $features = @(
        @{ Title = $data.feature1Title; Content = $data.feature1Content },
        @{ Title = $data.feature2Title; Content = $data.feature2Content },
        @{ Title = $data.feature3Title; Content = $data.feature3Content },
        @{ Title = $data.feature4Title; Content = $data.feature4Content }
    )

    foreach ($f in $features) {
        $sel.Font.Size = 11.5
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorTeal
        $sel.ParagraphFormat.SpaceBefore = 6
        $sel.ParagraphFormat.SpaceAfter = 2
        $sel.TypeText([char]0x25C6 + " " + $f.Title + "`n")

        $sel.Font.Size = 10
        $sel.Font.Bold = $false
        $sel.Font.Color = $colorDark
        $sel.ParagraphFormat.SpaceBefore = 0
        $sel.ParagraphFormat.SpaceAfter = 6
        $sel.TypeText($f.Content + "`n`n")
    }

    # Section 2: Prompts
    $sel.Font.Size = 14
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.ParagraphFormat.SpaceBefore = 10
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($data.sec2Title + "`n")

    $sel.Font.Size = 10.5
    $sel.Font.Bold = $false
    $sel.Font.Color = $colorDark
    $sel.ParagraphFormat.SpaceBefore = 0
    $sel.ParagraphFormat.SpaceAfter = 6
    $sel.TypeText($data.sec2P1 + "`n`n")

    $prompts = @(
        @{ Title = $data.prompt1Title; Code = $data.prompt1Code },
        @{ Title = $data.prompt2Title; Code = $data.prompt2Code },
        @{ Title = $data.prompt3Title; Code = $data.prompt3Code },
        @{ Title = $data.prompt4Title; Code = $data.prompt4Code },
        @{ Title = $data.prompt5Title; Code = $data.prompt5Code }
    )

    foreach ($p in $prompts) {
        $sel.Font.Size = 11.5
        $sel.Font.Bold = $true
        $sel.Font.Color = $colorTeal
        $sel.ParagraphFormat.SpaceBefore = 8
        $sel.ParagraphFormat.SpaceAfter = 3
        $sel.TypeText($p.Title + "`n")

        $tblP = $doc.Tables.Add($sel.Range, 1, 1)
        $tblP.Borders.Enable = 1
        try { $tblP.Borders.OutsideColor = $colorTeal } catch {}
        $tblP.Shading.BackgroundPatternColor = $colorBgBox
        $cP = $tblP.Cell(1, 1).Range
        $cP.Font.NameFarEast = "Microsoft YaHei"
        $cP.Font.Name = "Consolas"
        $cP.Font.Size = 9
        $cP.Font.Color = $colorDark
        $cP.Text = $p.Code
        $sel.EndKey(6) | Out-Null
        $sel.TypeParagraph()
    }

    # Section 3: Notion guidelines
    $sel.Font.Size = 14
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.ParagraphFormat.SpaceBefore = 10
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($data.sec3Title + "`n")

    $sel.Font.Size = 10
    $sel.Font.Bold = $false
    $sel.Font.Color = $colorDark
    $sel.ParagraphFormat.SpaceBefore = 0
    $sel.ParagraphFormat.SpaceAfter = 6
    $sel.TypeText($data.sec3P1 + "`n`n")

    # Section 4: Roadmap & Strategy
    $sel.Font.Size = 14
    $sel.Font.Bold = $true
    $sel.Font.Color = $colorNavy
    $sel.ParagraphFormat.SpaceBefore = 10
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($data.sec4Title + "`n")

    $tblAdv = $doc.Tables.Add($sel.Range, 1, 1)
    $tblAdv.Borders.Enable = 1
    try { $tblAdv.Borders.OutsideColor = 0x228B22 } catch {}
    $tblAdv.Shading.BackgroundPatternColor = 0xF4FAF4 # Pale green bg
    $cAdv = $tblAdv.Cell(1, 1).Range
    $cAdv.Font.NameFarEast = "Microsoft YaHei"
    $cAdv.Font.Name = "Calibri"
    $cAdv.Font.Size = 10
    $cAdv.Font.Color = $colorDark
    $cAdv.Text = $data.sec4Advice
    $sel.EndKey(6) | Out-Null
    $sel.TypeParagraph()

    # Save to all target locations
    foreach ($outP in $outFiles) {
        Write-Host "Saving to $outP ..."
        $doc.SaveAs2([string]$outP, 16) # 16 = wdFormatDocumentDefault (docx)
    }

    $doc.Close($false)
    Write-Host "SUCCESS: Generated all Word documents!"
} finally {
    $word.Quit()
}
