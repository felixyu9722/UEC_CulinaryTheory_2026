Add-Type -AssemblyName System.IO.Compression.FileSystem

$outPath = Join-Path $PSScriptRoot "oct_scan_fast.txt"
$sb = New-Object System.Text.StringBuilder

function Get-DocxText($path) {
    try {
        $zip = [System.IO.Compression.ZipFile]::OpenRead($path)
        $entry = $zip.GetEntry('word/document.xml')
        if ($entry) {
            $stream = $entry.Open()
            $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::UTF8)
            $xmlText = $reader.ReadToEnd()
            $reader.Close()
            $stream.Close()
            $zip.Dispose()
            
            # Simple regex to strip XML tags and extract text
            $txt = [System.Text.RegularExpressions.Regex]::Replace($xmlText, "<[^>]+>", " ")
            $txt = [System.Text.RegularExpressions.Regex]::Replace($txt, "\s+", " ")
            return $txt.Trim()
        }
        $zip.Dispose()
    } catch {
        return "ERROR: " + $_.Exception.Message
    }
    return ""
}

$dir = Get-ChildItem -Directory | Where-Object { $_.Name -like "*OCT*" }
$files = Get-ChildItem -Path $dir.FullName -Recurse -File | Where-Object { $_.Extension -eq ".docx" }

[void]$sb.AppendLine("Found " + $files.Count + " docx files.")

foreach ($f in $files) {
    [void]$sb.AppendLine("`n========================================================")
    [void]$sb.AppendLine("FILE: " + $f.FullName)
    [void]$sb.AppendLine("SIZE: " + $f.Length)
    $text = Get-DocxText $f.FullName
    [void]$sb.AppendLine("LENGTH: " + $text.Length)
    $preview = $text.Substring(0, [Math]::Min(1200, $text.Length))
    [void]$sb.AppendLine("PREVIEW:`n" + $preview)
}

[System.IO.File]::WriteAllText($outPath, $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "FAST SCAN COMPLETED. Total files: " $files.Count
