# Pure ASCII PowerShell script to render Batch 4 (Lessons 14, 15, 16, 17)
$ErrorActionPreference = 'Stop'
$lessons = @("work\quiz_data_lesson14.json", "work\quiz_data_lesson15.json", "work\quiz_data_lesson16.json", "work\quiz_data_lesson17.json")

foreach ($jf in $lessons) {
    Write-Host "=========================================================="
    Write-Host "Rendering $jf..."
    & powershell -ExecutionPolicy Bypass -File "work\render_lesson_suite.ps1" -JsonFile $jf
}
Write-Host "Batch 4 rendering completed successfully!"
