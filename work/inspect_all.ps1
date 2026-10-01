$outPath = Join-Path $PSScriptRoot "oct_scan_output.txt"
$word = New-Object -ComObject Word.Application
$word.Visible = $false

$sb = New-Object System.Text.StringBuilder

try {
    $dir = Get-ChildItem -Directory | Where-Object { $_.Name -like "*OCT*" }
    [void]$sb.AppendLine("Target folder: " + $dir.FullName)
    $files = Get-ChildItem -Path $dir.FullName -Recurse -File | Where-Object { $_.Extension -match "\.docx?$" }
    [void]$sb.AppendLine("Total doc/docx files: " + $files.Count)
    
    foreach ($f in $files) {
        [void]$sb.AppendLine("`n========================================================")
        [void]$sb.AppendLine("FILE: " + $f.FullName)
        [void]$sb.AppendLine("SIZE: " + $f.Length)
        try {
            $doc = $word.Documents.Open($f.FullName, $false, $true)
            $text = $doc.Content.Text
            $doc.Close()
            [void]$sb.AppendLine("CHAR COUNT: " + $text.Length)
            $preview = $text.Substring(0, [Math]::Min(1200, $text.Length))
            [void]$sb.AppendLine("CONTENT PREVIEW:`n" + $preview)
        } catch {
            [void]$sb.AppendLine("ERROR: " + $_.Exception.Message)
        }
    }
} finally {
    $word.Quit()
}

[System.IO.File]::WriteAllText($outPath, $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "Done writing output to $outPath"
