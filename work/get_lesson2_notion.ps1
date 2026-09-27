[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$pageId = "3cb138c5-b398-813e-804c-e44f0ead6f66" # Lesson 2

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$blocks = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children?page_size=100" -Headers $headers -Method Get

$outPath = "work\lesson2_notion_raw.json"
$blocks | ConvertTo-Json -Depth 5 | Set-Content -Path $outPath -Encoding UTF8
Write-Host "Saved Lesson 2 Notion blocks: $($blocks.results.Count) blocks"
