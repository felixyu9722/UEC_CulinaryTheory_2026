[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$pageId = "3cb138c5-b398-81fa-89ec-f56925d47295" # 高一页面

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$blocks = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children?page_size=100" -Headers $headers -Method Get
Write-Host "高一页面下 blocks:"
foreach ($b in $blocks.results) {
    if ($b.type -eq "child_page") {
        Write-Host ("- [Child Page: " + $b.id + "] " + $b.child_page.title)
    } elseif ($b.type -eq "callout") {
        $txt = ($b.callout.rich_text | ForEach-Object { $_.plain_text }) -join ""
        Write-Host ("[Callout] " + $txt.Substring(0, [Math]::Min(80, $txt.Length)))
    }
}
