$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$strFile = Join-Path $dataDir 'doc_strings_easy_400.json'

$strRaw = [System.IO.File]::ReadAllText($strFile, [System.Text.Encoding]::UTF8)
$S = $strRaw | ConvertFrom-Json

$workspaceRoot = Split-Path -Parent $scriptDir
$outDir = Join-Path $workspaceRoot $S.outFolderName
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$outDocPath = Join-Path $outDir $S.docFileName

Write-Host "Initializing Microsoft Word COM Object..."
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
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
    $sel.TypeText($S.title + "`n")
    
    # Subtitle
    $sel.Font.Size = 11
    $sel.Font.Bold = $false
    $sel.Font.Color = 0x333333
    $sel.ParagraphFormat.Alignment = 1
    $sel.ParagraphFormat.SpaceAfter = 12
    $sel.TypeText($S.subtitle + "`n")
    
    # Callout Note
    $sel.Font.Size = 9.5
    $sel.Font.Italic = $true
    $sel.Font.Color = 0x555555
    $sel.ParagraphFormat.Alignment = 0
    $sel.ParagraphFormat.SpaceAfter = 18
    $sel.TypeText($S.note + "`n")
    $sel.Font.Italic = $false

    for ($ch = 1; $ch -le 20; $ch++) {
        $chPad = ("0" + [string]$ch).Substring(("0" + [string]$ch).Length - 2)
        $jsonPath = Join-Path $dataDir ('chapter' + $chPad + '.json')
        $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
        $chData = $raw | ConvertFrom-Json
        
        $easyQs = @($chData.questions | Where-Object { $_.difficulty -eq 'easy' })
        
        Write-Host ("Adding Chapter " + $chPad + " (" + $chData.chapter_title + "): " + $easyQs.Count + " easy questions")
        
        # Chapter Heading
        $sel.Font.Size = 14
        $sel.Font.Bold = $true
        $sel.Font.Color = 0x003366
        $sel.ParagraphFormat.Alignment = 0
        $sel.ParagraphFormat.SpaceBefore = 14
        $sel.ParagraphFormat.SpaceAfter = 4
        $sel.TypeText($S.chapterPrefix + " " + $chData.chapter_title + "`n")
        
        # Section Header
        $sel.Font.Size = 11
        $sel.Font.Bold = $true
        $sel.Font.Color = 0x15803D
        $sel.ParagraphFormat.SpaceBefore = 2
        $sel.ParagraphFormat.SpaceAfter = 6
        $sel.TypeText($S.secQuestions + "`n")
        
        # Questions
        $qIdx = 1
        foreach ($q in $easyQs) {
            $sel.Font.Size = 10.5
            $sel.Font.Bold = $true
            $sel.Font.Color = 0x111111
            $sel.ParagraphFormat.SpaceBefore = 5
            $sel.ParagraphFormat.SpaceAfter = 2
            $sel.TypeText([string]$qIdx + ". " + $q.question + "`n")
            
            $sel.Font.Bold = $false
            $sel.ParagraphFormat.SpaceBefore = 1
            $sel.ParagraphFormat.SpaceAfter = 1
            $sel.ParagraphFormat.LeftIndent = $word.InchesToPoints(0.2)
            $sel.TypeText("A. " + $q.options.A + "`n")
            $sel.TypeText("B. " + $q.options.B + "`n")
            $sel.TypeText("C. " + $q.options.C + "`n")
            $sel.TypeText("D. " + $q.options.D + "`n")
            $sel.ParagraphFormat.LeftIndent = 0
            
            $qIdx++
        }
        
        # Answers section for this chapter
        $sel.Font.Size = 11
        $sel.Font.Bold = $true
        $sel.Font.Color = 0x8B3A1A
        $sel.ParagraphFormat.SpaceBefore = 8
        $sel.ParagraphFormat.SpaceAfter = 4
        $sel.TypeText($S.secAnswers + "`n")
        
        $qIdx = 1
        foreach ($q in $easyQs) {
            $sel.Font.Size = 9.5
            $sel.Font.Bold = $true
            $sel.Font.Color = 0x1D4ED8
            $sel.ParagraphFormat.SpaceBefore = 2
            $sel.ParagraphFormat.SpaceAfter = 1
            $sel.TypeText([string]$qIdx + ". " + $S.ansLabel + $q.answer + "    ")
            
            $sel.Font.Bold = $false
            $sel.Font.Color = 0x4B5563
            $sel.TypeText($S.expLabel + $q.explanation + "`n")
            
            $qIdx++
        }
        
        if ($ch -lt 20) {
            $sel.InsertBreak(7) # PageBreak between chapters
        }
    }
    
    $doc.SaveAs([string]$outDocPath)
    $doc.Close()
    Write-Host ("Successfully generated Master 400 Easy Questions Word Document at: " + $outDocPath)
} finally {
    $word.Quit()
}
