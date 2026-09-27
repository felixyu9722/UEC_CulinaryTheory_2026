$word = New-Object -ComObject Word.Application
$word.Visible = $false

$ws = (Get-Item .).FullName
$dirs = Get-ChildItem -Directory -Path $ws
$targetDir = $null
foreach ($d in $dirs) {
    if ($d.Name -notlike "*0*" -and $d.Name -notlike "*AI*" -and $d.Name -notlike "*work*" -and $d.Name -notlike "*backup*" -and $d.Name -notlike "*yu*") {
        $targetDir = $d.FullName
        break
    }
}

Write-Host ("Target Dir: " + $targetDir)
$files = Get-ChildItem -File -Path $targetDir -Filter "*.docx"
foreach ($f in $files) {
    Write-Host ("Opening: " + $f.Name)
    $doc = $word.Documents.Open($f.FullName)
    $txt = $doc.Content.Text
    $doc.Close($false)
    
    $outPath = Join-Path "work" ("exam_" + $f.BaseName + ".txt")
    [System.IO.File]::WriteAllText($outPath, $txt, [System.Text.Encoding]::UTF8)
    Write-Host ("Saved to: " + $outPath + " Length: " + $txt.Length)
}

$word.Quit()
