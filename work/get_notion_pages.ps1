[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$parentId = "3cb138c5b39880fe8b37e6ed03e1be79"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$parentId/children?page_size=50" -Headers $headers -Method Get
$subpages = @()

foreach ($b in $res.results) {
    if ($b.type -eq "child_page") {
        $subpages += [PSCustomObject]@{
            Title = $b.child_page.title
            Id    = $b.id
        }
    }
}

$jsonPath = Join-Path $PSScriptRoot "data\notion_subpages_manifest.json"
$subpages | ConvertTo-Json -Depth 3 | Set-Content -Path $jsonPath -Encoding UTF8
Write-Host "Discovered $($subpages.Count) subpages. Saved to $jsonPath"
$subpages | Format-Table -AutoSize
