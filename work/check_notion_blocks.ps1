[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$token = 'ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai'
$headers = @{
    'Authorization' = "Bearer $token"
    'Notion-Version' = '2022-06-28'
    'Content-Type' = 'application/json'
}

$pageId = '3cb138c5-b398-81fa-89ec-f56925d47295'
try {
    $res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children?page_size=100" -Method Get -Headers $headers
    Write-Output "Blocks count: $($res.results.Count)"
    foreach ($b in $res.results) {
        $title = ''
        if ($b.child_page) {
            $title = $b.child_page.title
        } elseif ($b.paragraph -and $b.paragraph.rich_text) {
            $title = ($b.paragraph.rich_text | ForEach-Object { $_.plain_text }) -join ''
        } elseif ($b.heading_1 -and $b.heading_1.rich_text) {
            $title = '# ' + (($b.heading_1.rich_text | ForEach-Object { $_.plain_text }) -join '')
        } elseif ($b.heading_2 -and $b.heading_2.rich_text) {
            $title = '## ' + (($b.heading_2.rich_text | ForEach-Object { $_.plain_text }) -join '')
        } elseif ($b.heading_3 -and $b.heading_3.rich_text) {
            $title = '### ' + (($b.heading_3.rich_text | ForEach-Object { $_.plain_text }) -join '')
        }
        Write-Output "[$($b.type)] $title | ID: $($b.id)"
    }
} catch {
    Write-Output "Error: $_"
    if ($_.Exception.Response) {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        Write-Output $reader.ReadToEnd()
    }
}
