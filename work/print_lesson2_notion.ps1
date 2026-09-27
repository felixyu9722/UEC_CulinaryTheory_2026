$raw = Get-Content -Path "work\lesson2_notion_raw.json" -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($b in $raw.results) {
    $t = $b.type
    $txt = ""
    if ($b.$t.rich_text) {
        $txt = ($b.$t.rich_text | ForEach-Object { $_.plain_text }) -join ""
    }
    if ($t -like "heading*") {
        Write-Host "[$t] $txt"
    } elseif ($t -eq "callout") {
        Write-Host "[callout] $txt"
    } elseif ($txt.Length -gt 0) {
        Write-Host "  - $txt"
    }
}
