$word = New-Object -ComObject Word.Application
$word.Visible = $false

$ws = (Get-Item .).FullName
$dirs = Get-ChildItem -Directory -Path $ws
foreach ($d in $dirs) {
    $subFiles = Get-ChildItem -File -Path $d.FullName -Filter "*.docx"
    foreach ($f in $subFiles) {
        if ($f.Name -like "*测验_01*") {
            Write-Host ("Extracting: " + $f.FullName)
            $doc = $word.Documents.Open($f.FullName)
            $txt = $doc.Content.Text
            $doc.Close($false)
            
            $outPath = Join-Path "work" ($f.BaseName + ".txt")
            [System.IO.File]::WriteAllText($outPath, $txt, [System.Text.Encoding]::UTF8)
            Write-Host ("Saved to: " + $outPath + " Length: " + $txt.Length)
        }
    }
}

$word.Quit()
