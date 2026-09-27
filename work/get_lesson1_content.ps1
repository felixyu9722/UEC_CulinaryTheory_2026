[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$pageId = "3cb138c5-b398-81fc-92c6-f806c25914b1"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$blocks = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children?page_size=100" -Headers $headers -Method Get
Write-Host "第1课 内容总块数: $($blocks.results.Count)"
foreach ($b in $blocks.results) {
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
