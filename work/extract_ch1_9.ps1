$files = Get-ChildItem "08_*/*.md" | Where-Object { $_.Name -match "01_.*第[1-9]课" } | Sort-Object Name
foreach ($f in $files) {
    Write-Host ("=== " + $f.Name + " ===")
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $idx = $content.IndexOf("### ")
    if ($idx -ge 0) {
        $sub = $content.Substring($idx)
        $endIdx = $sub.IndexOf('```')
        if ($endIdx -gt 0) {
            Write-Host $sub.Substring(0, $endIdx)
        }
    }
}
