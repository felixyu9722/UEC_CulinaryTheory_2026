$jsonPath = Join-Path $PSScriptRoot "search_keywords.json"
$cfg = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
$keywords = $cfg.keywords

$lines = [System.IO.File]::ReadAllLines((Join-Path $PSScriptRoot "oct_scan_fast.txt"), [System.Text.Encoding]::UTF8)

$sb = New-Object System.Text.StringBuilder
$curFile = ""
$matched = $false

for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]
    if ($line.StartsWith("FILE: ")) {
        $curFile = $line.Substring(6)
        $matched = $false
        foreach ($kw in $keywords) {
            if ($curFile.IndexOf($kw, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                $matched = $true
                break
            }
        }
        if ($matched) {
            [void]$sb.AppendLine("==================================================")
            [void]$sb.AppendLine("FILE: " + $curFile)
        }
    } elseif ($matched -and $line.StartsWith("PREVIEW:")) {
        for ($j = $i; $j -lt [Math]::Min($i + 40, $lines.Length); $j++) {
            if ($lines[$j].StartsWith("========================================================")) { break }
            [void]$sb.AppendLine($lines[$j])
        }
    }
}

$outPath = Join-Path $PSScriptRoot "filtered_exam_summary.txt"
[System.IO.File]::WriteAllText($outPath, $sb.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "Output written to $outPath"
