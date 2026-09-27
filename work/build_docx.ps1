$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$strFile = Join-Path $dataDir 'doc_strings.json'

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
        $sel.ParagraphFormat.SpaceBefore = 6
        $sel.ParagraphFormat.SpaceAfter = 2
        $sel.ParagraphFormat.LineSpacing = 13
        $sel.TypeText([string]$q.id + '. ' + $q.question + "`n")
        
        $sel.Font.Bold = $false
        $sel.Font.Color = 0x222222
        $sel.ParagraphFormat.SpaceBefore = 1
        $sel.ParagraphFormat.SpaceAfter = 1
        $sel.ParagraphFormat.LeftIndent = $word.InchesToPoints(0.2)
        $sel.TypeText('A. ' + $q.options.A + "`n")
        $sel.TypeText('B. ' + $q.options.B + "`n")
        $sel.TypeText('C. ' + $q.options.C + "`n")
        $sel.TypeText('D. ' + $q.options.D + "`n")
        $sel.ParagraphFormat.LeftIndent = 0
    }
    
    # Page break for Answers & Explanations
    $sel.InsertBreak(7)
    
    # Answer Section Header
    $sel.Font.Size = 16
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x1A5235
    $sel.ParagraphFormat.Alignment = 1
    $sel.ParagraphFormat.SpaceBefore = 10
    $sel.ParagraphFormat.SpaceAfter = 6
    $sel.TypeText($S.ansTitle)
    
    # Answer Quick Table
    $sel.Font.Size = 11
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x000000
    $sel.ParagraphFormat.Alignment = 0
    $sel.ParagraphFormat.SpaceBefore = 8
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($S.ansQuickTitle)
    
    $sel.Font.Size = 9.5
    $sel.Font.Bold = $false
    $ansList = @()
    foreach ($q in $questions) {
        $ansList += ('Q' + [string]$q.id + ': ' + $q.answer)
    }
    
    for ($i = 0; $i -lt $ansList.Count; $i += 5) {
        $maxIdx = [Math]::Min($i + 4, $ansList.Count - 1)
        $chunk = $ansList[$i..$maxIdx] -join '    |    '
        $sel.TypeText('  ' + $chunk + "`n")
    }
    
    $sel.Font.Italic = $true
    $sel.Font.Color = 0x666666
    $sel.TypeText($S.ansQuickNote)
    $sel.Font.Italic = $false
    
    # Detailed Explanations
    $sel.Font.Size = 11
    $sel.Font.Bold = $true
    $sel.Font.Color = 0x000000
    $sel.ParagraphFormat.SpaceBefore = 10
    $sel.ParagraphFormat.SpaceAfter = 4
    $sel.TypeText($S.ansDetailTitle)
    
    foreach ($q in $questions) {
        $sel.Font.Size = 10
        $sel.Font.Bold = $true
        $sel.Font.Color = 0x0B3C5D
        $sel.ParagraphFormat.SpaceBefore = 5
        $sel.ParagraphFormat.SpaceAfter = 1
        $sel.TypeText($S.qPrefix + [string]$q.id + $S.qMid + $q.answer + $S.qTail)
        
        $sel.Font.Bold = $false
        $sel.Font.Color = 0x333333
        $sel.ParagraphFormat.SpaceBefore = 0
        $sel.ParagraphFormat.SpaceAfter = 4
        $sel.ParagraphFormat.LeftIndent = $word.InchesToPoints(0.15)
        $sel.TypeText($S.ansPrefix + ' ' + $q.explanation + "`n")
        $sel.ParagraphFormat.LeftIndent = 0
    }
    
    $doc.SaveAs2([string]$outPath, 16)
    $doc.Close($false)
}

try {
    for ($ch = 10; $ch -le 15; $ch++) {
        $jsonPath = Join-Path $dataDir ('chapter' + [string]$ch + '.json')
        $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
        $data = $raw | ConvertFrom-Json
        
        $chKey = [string]$ch
        $cName = $S.nameMap.$chKey
        
        $docFileName = $S.filePrefix + [string]$ch + $S.fileSuffix + $cName + $S.fileTail
        $outDocPath = Join-Path $outDir $docFileName
        Generate-Doc $data.chapter_title $data.intro $data.questions $outDocPath
    }
    
    Write-Host 'Generating combined 240 questions docx...'
    $allQuestions = @()
    $cId = 1
    for ($ch = 10; $ch -le 15; $ch++) {
        $jsonPath = Join-Path $dataDir ('chapter' + [string]$ch + '.json')
        $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
        $data = $raw | ConvertFrom-Json
        foreach ($q in $data.questions) {
            $qCopy = $q | Select-Object *
            $qCopy | Add-Member -MemberType NoteProperty -Name 'id' -Value ($cId++) -Force
            $allQuestions += $qCopy
        }
    }
    
    $combinedPath = Join-Path $outDir $S.combinedFile
    Generate-Doc $S.combinedTitle $S.combinedIntro $allQuestions $combinedPath
    
    Write-Host 'SUCCESS: All Word documents generated!'
} finally {
    $word.Quit()
}
