[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$pageId = "3cb138c5b39880fe8b37e6ed03e1be79"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

Write-Host "=== Testing Page Info ==="
try {
    $res = Invoke-RestMethod -Uri "https://api.notion.com/v1/pages/$pageId" -Headers $headers -Method Get
    Write-Host "Page Status: OK"
    Write-Host "Properties:"
    $res.properties | ConvertTo-Json -Depth 3 | Write-Host
} catch {
    Write-Host "Page Fetch Error: $($_.Exception.Message)"
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host "Details: $($reader.ReadToEnd())"
    }
}

Write-Host "`n=== Testing Blocks (Children) ==="
try {
    $blocks = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children?page_size=30" -Headers $headers -Method Get
    Write-Host "Blocks Status: OK. Count = $($blocks.results.Count)"
    foreach ($b in $blocks.results) {
        $t = $b.type
        $txt = ""
        if ($b.$t.rich_text) {
            $txt = ($b.$t.rich_text | ForEach-Object { $_.plain_text }) -join ""
        } elseif ($b.$t.title) {
            $txt = $b.$t.title
        }
        Write-Host "[$t] $txt"
    }
} catch {
    Write-Host "Blocks Fetch Error: $($_.Exception.Message)"
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Host "Details: $($reader.ReadToEnd())"
    }
}
