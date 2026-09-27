$word = New-Object -ComObject Word.Application
$word.Visible = $false

$ws = (Get-Item .).FullName
$examFolder = Get-ChildItem -Directory -Path $ws | Where-Object { $_.Name -like "*校内*" } | Select-Object -First 1

$docxFiles = Get-ChildItem -File -Path $examFolder.FullName -Filter "*.docx"
foreach ($f in $docxFiles) {
    Write-Host ("Opening: " + $f.Name)
    $doc = $word.Documents.Open($f.FullName)
    $txt = $doc.Content.Text
    $doc.Close($false)
    
    $outTxtPath = Join-Path "work" ($f.BaseName + ".txt")
    [System.IO.File]::WriteAllText($outTxtPath, $txt, [System.Text.Encoding]::UTF8)
    Write-Host ("Saved text: " + $outTxtPath + " Length: " + $txt.Length)
}

$word.Quit()
