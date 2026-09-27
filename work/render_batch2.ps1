# Pure ASCII PowerShell script to render Batch 2 (Lessons 6, 7, 8, 9)
$ErrorActionPreference = 'Stop'
$lessons = @("work\quiz_data_lesson6.json", "work\quiz_data_lesson7.json", "work\quiz_data_lesson8.json", "work\quiz_data_lesson9.json")

foreach ($jf in $lessons) {
    Write-Host "=========================================================="
    Write-Host "Rendering $jf..."
    & powershell -ExecutionPolicy Bypass -File "work\render_lesson_suite.ps1" -JsonFile $jf
}
Write-Host "Batch 2 rendering completed successfully!"
