$items = Get-Content -Path "work\notion_g1_lessons.json" -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($item in $items) {
    Write-Host ("Lesson " + $item.Num + " : " + $item.Title + " (Sections: " + $item.Sections.Count + ")")
    # print first 3 sections
    for ($i = 0; $i -lt [Math]::Min(3, $item.Sections.Count); $i++) {
        $s = $item.Sections[$i]
        Write-Host ("   [" + $s.Type + "] " + $s.Text.Substring(0, [Math]::Min(50, $s.Text.Length)))
    }
}
