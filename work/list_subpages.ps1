[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$pageId = "3cb138c5b39880fe8b37e6ed03e1be79"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$blocks = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children?page_size=100" -Headers $headers -Method Get
Write-Host "✅ 成功连通 Notion API！主页面子页面列表及 Block ID："
foreach ($b in $blocks.results) {
    if ($b.type -eq "child_page") {
        Write-Host ("- [" + $b.id + "] " + $b.child_page.title)
    }
}
