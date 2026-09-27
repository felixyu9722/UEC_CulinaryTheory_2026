# Pure ASCII PowerShell script to render Batch 3 (Lessons 10, 11, 12, 13)
$ErrorActionPreference = 'Stop'
$lessons = @("work\quiz_data_lesson10.json", "work\quiz_data_lesson11.json", "work\quiz_data_lesson12.json", "work\quiz_data_lesson13.json")

foreach ($jf in $lessons) {
    Write-Host "=========================================================="
    Write-Host "Rendering $jf..."
    & powershell -ExecutionPolicy Bypass -File "work\render_lesson_suite.ps1" -JsonFile $jf
}
Write-Host "Batch 3 rendering completed successfully!"
