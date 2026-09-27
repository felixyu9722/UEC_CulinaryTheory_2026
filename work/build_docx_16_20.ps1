$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$strFile = Join-Path $dataDir 'doc_strings_16_20.json'

$strRaw = [System.IO.File]::ReadAllText($strFile, [System.Text.Encoding]::UTF8)
$S = $strRaw | ConvertFrom-Json

$workspaceRoot = Split-Path -Parent $scriptDir
$outDir = Join-Path $workspaceRoot $S.outFolderName
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

function Generate-Doc($titleText, $introText, $questions, $outPath) {
    Write-Host ("Writing docx: " + (Split-Path -Leaf $outPath))
    $doc = $word.Documents.Add()
    
    $section = $doc.Sections.Item(1)
    $section.PageSetup.PaperSize = 2 # Letter / A4
    $section.PageSetup.TopMargin = $word.InchesToPoints(0.75)
    $section.PageSetup.BottomMargin = $word.InchesToPoints(0.75)
    $section.PageSetup.LeftMargin = $word.InchesToPoints(0.75)
    $section.PageSetup.RightMargin = $word.InchesToPoints(0.75)
    
    $sel = $word.Selection
    
    # Title
    $sel.Font.NameFarEast = 'Microsoft JhengHei'
    $sel.Font.Name = 'Calibri'
    $sel.Font.Size = 18
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x8B3A1A
    $sel.ParagraphFormat.Alignment = 1
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($titleText + "`n")
    
    # Subtitle
    $sel.Font.Size = 10.5
    $sel.Font.Bold = $false
    $sel.Font.Color = 0x555555
    $sel.ParagraphFormat.Alignment = 1
    $sel.ParagraphFormat.SpaceAfter = 12
    $sel.TypeText($S.subtitle)
    
    # Note callout
    $sel.Font.Size = 9.5
    $sel.Font.Italic = $true
    $sel.Font.Color = 0x333333
    $sel.ParagraphFormat.Alignment = 0
    $sel.ParagraphFormat.SpaceAfter = 14
    $sel.TypeText($S.note)
    $sel.Font.Italic = $false

    # Questions Section
    $sel.Font.Size = 13
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x003366
    $sel.ParagraphFormat.SpaceBefore = 8
    $sel.ParagraphFormat.SpaceAfter = 6
    $sel.TypeText($S.part1)
    
    foreach ($q in $questions) {
        $sel.Font.Size = 10.5
        $sel.Font.Bold = $true
        $sel.Font.Color = 0x000000
        $sel.ParagraphFormat.Alignment = 0
        $sel.ParagraphFormat.SpaceBefore = 6
        $sel.ParagraphFormat.SpaceAfter = 3
        
        $diffTag = ""
        if ($q.difficulty -eq "easy") { $diffTag = $S.diffEasy }
        elseif ($q.difficulty -eq "medium") { $diffTag = $S.diffMedium }
        elseif ($q.difficulty -eq "hard") { $diffTag = $S.diffHard }
        
        $sel.TypeText([string]$q.id + ". " + $diffTag + $q.question + "`n")
        
        $sel.Font.Bold = $false
        $sel.ParagraphFormat.SpaceBefore = 1
        $sel.ParagraphFormat.SpaceAfter = 1
        $sel.ParagraphFormat.LeftIndent = $word.InchesToPoints(0.2)
        $sel.TypeText("A. " + $q.options.A + "`n")
        $sel.TypeText("B. " + $q.options.B + "`n")
        $sel.TypeText("C. " + $q.options.C + "`n")
        $sel.TypeText("D. " + $q.options.D + "`n")
        $sel.ParagraphFormat.LeftIndent = 0
    }
    
    # Page Break for Answers
    $sel.InsertBreak(7) # wdPageBreak
    
    # Answers & Explanations
    $sel.Font.Size = 16
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x8B3A1A
    $sel.ParagraphFormat.Alignment = 1
    $sel.ParagraphFormat.SpaceBefore = 12
    $sel.ParagraphFormat.SpaceAfter = 14
    $sel.TypeText($S.ansTitle)
    
    # Quick Key Table
    $sel.Font.Size = 11.5
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x003366
    $sel.ParagraphFormat.Alignment = 0
    $sel.ParagraphFormat.SpaceBefore = 8
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($S.ansQuickTitle)
    
    $sel.Font.Size = 10
    $sel.Font.Bold = $false
    $sel.Font.Color = 0x111111
    $sel.ParagraphFormat.SpaceAfter = 4
    
    # Format quick table (rows of 10)
    for ($row = 0; $row -lt 4; $row++) {
        $lineItems = @()
        for ($col = 1; $col -le 10; $col++) {
            $idx = $row * 10 + $col
            $qItem = $questions | Where-Object { $_.id -eq $idx }
            if ($qItem) {
                $lineItems += ("$idx. " + $qItem.answer)
            }
        }
        $sel.TypeText("  " + ($lineItems -join "   |   ") + "`n")
    }
    
    $sel.Font.Italic = $true
    $sel.Font.Color = 0x555555
    $sel.ParagraphFormat.SpaceBefore = 4
    $sel.ParagraphFormat.SpaceAfter = 14
    $sel.TypeText($S.ansQuickNote)
    $sel.Font.Italic = $false

    # Detailed Explanations
    $sel.Font.Size = 11.5
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x003366
    $sel.ParagraphFormat.SpaceBefore = 8
    $sel.ParagraphFormat.SpaceAfter = 6
    $sel.TypeText($S.ansDetailTitle)
    
    foreach ($q in $questions) {
        $sel.Font.Size = 10
        $sel.Font.Bold = $true
        $sel.Font.Color = 0x000000
        $sel.ParagraphFormat.SpaceBefore = 4
        $sel.ParagraphFormat.SpaceAfter = 2
        $sel.TypeText($S.qPrefix + [string]$q.id + $S.qMid + $q.answer + $S.qTail)
        
        $sel.Font.Bold = $false
        $sel.Font.Color = 0x222222
        $sel.ParagraphFormat.LeftIndent = $word.InchesToPoints(0.15)
        $sel.ParagraphFormat.SpaceAfter = 6
        $sel.TypeText($S.ansPrefix + "`n" + $q.explanation + "`n")
        $sel.ParagraphFormat.LeftIndent = 0
    }
    
    $doc.SaveAs2([string]$outPath, 16) # 16 = wdFormatDocumentDefault (docx)
    $doc.Close($false)
}

try {
    # Generate 5 single-chapter docs
    for ($ch = 16; $ch -le 20; $ch++) {
        $chStr = [string]$ch
        $jsonPath = Join-Path $dataDir ("chapter$ch.json")
        $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
        $chData = $raw | ConvertFrom-Json
        
        $cName = $S.nameMap.$chStr
        $outName = $S.filePrefix + [string]$ch + $S.fileSuffix + $cName + $S.fileTail
        $outPath = Join-Path $outDir $outName
        
        Generate-Doc $chData.chapter_title $chData.intro $chData.questions $outPath
    }
    
    # Generate Combined Doc (all 200 questions)
    Write-Host "Generating combined 200 questions docx..."
    $allQuestions = @()
    $qCounter = 1
    
    for ($ch = 16; $ch -le 20; $ch++) {
        $chStr = [string]$ch
        $cName = $S.nameMap.$chStr
        $jsonPath = Join-Path $dataDir ("chapter$ch.json")
        $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
        $chData = $raw | ConvertFrom-Json
        
        foreach ($q in $chData.questions) {
            $clone = $q | Select-Object *
            $clone.id = $qCounter
            $clone.question = $S.chapterTagPrefix + [string]$ch + $S.chapterTagMid + $cName + $S.chapterTagSuffix + $q.question
            $allQuestions += $clone
            $qCounter++
        }
    }
    
    $combinedOutPath = Join-Path $outDir $S.combinedFile
    Generate-Doc $S.combinedTitle $S.combinedIntro $allQuestions $combinedOutPath
    
    Write-Host "SUCCESS: All Word documents for Chapters 16-20 generated!"
}
finally {
    $word.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
