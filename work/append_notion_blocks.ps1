param (
    [string]$jsonFile
)

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$raw = [System.IO.File]::ReadAllText($jsonFile, [System.Text.Encoding]::UTF8)
$data = ConvertFrom-Json $raw
$pageId = $data.pageId

$bodyObj = @{ children = $data.children }
$jsonBody = $bodyObj | ConvertTo-Json -Depth 10
$utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($jsonBody)

Write-Host "Appending blocks to Notion Page ID: $pageId ..."
$res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children" -Headers $headers -Method Patch -Body $utf8Bytes
Write-Host "SUCCESS! Added $($res.results.Count) blocks to page."
