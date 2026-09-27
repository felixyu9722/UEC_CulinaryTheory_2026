$text = [System.IO.File]::ReadAllText("work/notion_g1_lessons.json", [System.Text.Encoding]::UTF8)
$arr = ConvertFrom-Json $text
Write-Host "=== Current Notion G1 Lessons (Total $($arr.Count)) ==="
foreach ($item in $arr) {
    Write-Host "Notion Lesson $($item.lesson_num): $($item.title)"
}
