[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

function List-Subblocks($id, $label) {
    Write-Host "`n=== Subblocks for $label ($id) ==="
    try {
        $res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$id/children?page_size=50" -Headers $headers -Method Get
        foreach ($b in $res.results) {
            $t = $b.type
            $txt = ""
            if ($b.child_page) {
                $txt = ">> CHILD PAGE: " + $b.child_page.title + " (ID: " + $b.id + ")"
            } elseif ($b.$t.rich_text) {
                $txt = ($b.$t.rich_text | ForEach-Object { $_.plain_text }) -join ""
            }
            if ($txt.Length -gt 0) {
                Write-Host "[$t] $txt"
            }
        }
    } catch {
        Write-Host "Error: $($_.Exception.Message)"
    }
}

List-Subblocks "3cb138c5-b398-8122-85f8-f90f7b3663e7" "02 Grade 2"
List-Subblocks "3cb138c5-b398-819c-8a1b-fa6c71598108" "03 Grade 3"
List-Subblocks "3cb138c5-b398-81ff-9dfa-d959e22066d3" "04 Calculation"
List-Subblocks "3d4138c5-b398-81a1-baf5-d415a319bfbf" "11 Practical Exam"
