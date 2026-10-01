[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$id = "3cb138c5-b398-8168-87db-e011f8d96405"
$res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$id/children?page_size=50" -Headers $headers -Method Get
Write-Host "Total blocks in Asian Cuisine (G3 Unit 7): $($res.results.Count)"
foreach ($b in $res.results) {
    $t = $b.type
    $txt = ""
    if ($b.$t.rich_text) {
        $txt = ($b.$t.rich_text | ForEach-Object { $_.plain_text }) -join ""
    }
    Write-Host "[$t] $txt"
}
