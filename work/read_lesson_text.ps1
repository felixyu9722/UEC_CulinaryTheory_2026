param([int]$LessonNum)
$items = Get-Content -Path "work\notion_g1_lessons.json" -Raw -Encoding UTF8 | ConvertFrom-Json
$lesson = $items | Where-Object { [int]$_.Num -eq $LessonNum }
if (-not $lesson) {
    Write-Host "Lesson $LessonNum not found!"
    exit
}
Write-Host "=== LESSON $($lesson.Num): $($lesson.Title) ==="
foreach ($sec in $lesson.Sections) {
    Write-Host "[$($sec.Type)] $($sec.Text)"
}
