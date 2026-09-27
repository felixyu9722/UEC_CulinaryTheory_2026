[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$lessonsInfo = @(
    @{ Num = 2;  Id = "3cb138c5-b398-813e-804c-e44f0ead6f66" },
    @{ Num = 3;  Id = "3cb138c5-b398-81e2-972a-dad536ab71c9" },
    @{ Num = 4;  Id = "3cb138c5-b398-8189-b418-ecd7679a0979" },
    @{ Num = 5;  Id = "3cb138c5-b398-8107-bd8e-cb1a46718e47" },
    @{ Num = 6;  Id = "3cb138c5-b398-81a5-b06e-fe7117fdc31d" },
    @{ Num = 7;  Id = "3cb138c5-b398-81f7-ab0f-f8fdc8108e45" },
    @{ Num = 8;  Id = "3cb138c5-b398-8180-9a3a-d36130a4a9d1" },
    @{ Num = 9;  Id = "3cb138c5-b398-812b-a0f0-e53d1feaee39" },
    @{ Num = 10; Id = "3cb138c5-b398-812c-a2e8-c2d8ce439fef" },
    @{ Num = 11; Id = "3cb138c5-b398-817d-84f5-eb9d84a95290" },
    @{ Num = 12; Id = "3cb138c5-b398-818c-919a-ef492341aa52" },
    @{ Num = 13; Id = "3cb138c5-b398-817c-9e86-dc30068a706a" },
    @{ Num = 14; Id = "3cb138c5-b398-81e8-b89e-decd7a93ab73" },
    @{ Num = 15; Id = "3cb138c5-b398-81ee-afd5-dfc4b7faba00" },
    @{ Num = 16; Id = "3cb138c5-b398-81d4-bd30-de9f3b7366c6" },
    @{ Num = 17; Id = "3cb138c5-b398-81af-8730-d742c831983b" },
    @{ Num = 18; Id = "3cb138c5-b398-81b7-9e9d-e2a5895c2bf6" },
    @{ Num = 19; Id = "3cb138c5-b398-8140-ae0f-cae1d861d162" },
    @{ Num = 20; Id = "3cb138c5-b398-8103-94f0-e8d0e35e97ed" }
)

$allNotionLessons = @()

foreach ($info in $lessonsInfo) {
    $num = $info.Num
    $id = $info.Id
    Write-Host "Fetching Lesson $($num) - $id..."

    try {
        # 1. Fetch Page Title
        $pageObj = Invoke-RestMethod -Uri "https://api.notion.com/v1/pages/$id" -Headers $headers -Method Get
        $titleText = ""
        if ($pageObj.properties.title.title) {
            $titleText = ($pageObj.properties.title.title | ForEach-Object { $_.plain_text }) -join ""
        }

        # 2. Fetch Blocks
        $blocks = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$id/children?page_size=100" -Headers $headers -Method Get
        
        $textSections = @()
        foreach ($b in $blocks.results) {
            $t = $b.type
            $txt = ""
            if ($b.$t.rich_text) {
                $txt = ($b.$t.rich_text | ForEach-Object { $_.plain_text }) -join ""
            }
            if ($txt.Trim().Length -gt 0) {
                $textSections += @{ Type = $t; Text = $txt }
            }
        }

        $allNotionLessons += @{
            Num = $num
            Id = $id
            Title = $titleText
            BlockCount = $blocks.results.Count
            Sections = $textSections
        }
        Write-Host "  -> Done! Blocks: $($blocks.results.Count) | Title: $titleText"
    } catch {
        Write-Host "  -> Error fetching Lesson $($num): $($_.Exception.Message)"
    }
}

$outPath = "work\notion_g1_lessons.json"
$allNotionLessons | ConvertTo-Json -Depth 6 | Set-Content -Path $outPath -Encoding UTF8
Write-Host "All Notion Lessons saved to $outPath successfully!"
