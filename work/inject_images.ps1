$token = 'ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbvXZ9ai'
$headers = @{
    'Authorization' = 'Bearer ' + $token
    'Notion-Version' = '2022-06-28'
    'Content-Type'   = 'application/json'
}
$resp = Invoke-RestMethod -Uri 'https://api.notion.com/v1/users/me' -Method Get -Headers $headers
Write-Host 'TTEST OK: ' $resp.name