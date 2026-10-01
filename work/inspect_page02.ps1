[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

function Show-Page($id, $name) {
    Write-Host "`n================ $name ================"
    $res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$id/children?page_size=30" -Headers $headers -Method Get
    foreach ($b in $res.results) {
        $t = $b.type
        $txt = ""
        if ($b.child_page) {
            $txt = "PAGE: " + $b.child_page.title + " (ID: " + $b.id + ")"
        } elseif ($b.$t.rich_text) {
            $txt = ($b.$t.rich_text | ForEach-Object { $_.plain_text }) -join ""
        }
        Write-Host "[$t] $txt"
    }
}

Show-Page "3cb138c5-b398-8122-85f8-f90f7b3663e7" "Page 02 - Grade 2"
Show-Page "3cb138c5-b398-819c-8a1b-fa6c71598108" "Page 03 - Grade 3"
