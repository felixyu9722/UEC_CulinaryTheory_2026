[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/3cb138c5-b398-81fa-89ec-f56925d47295/children?page_size=50" -Headers $headers -Method Get
$pages = @()
foreach ($b in $res.results) {
    if ($b.child_page) {
        $pages += [PSCustomObject]@{
            Title = $b.child_page.title
            Id    = $b.id
            Url   = "https://www.notion.so/" + ($b.id.Replace("-", ""))
        }
    }
}
$pages | Format-Table -AutoSize
$pages | ConvertTo-Json -Depth 3 | Set-Content (Join-Path $PSScriptRoot "data\notion_g1_subpages.json") -Encoding UTF8
