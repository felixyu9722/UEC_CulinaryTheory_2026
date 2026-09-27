# Pure ASCII PowerShell script to render Batch 5 (Lessons 18, 19, 20)
$ErrorActionPreference = 'Stop'
$lessons = @("work\quiz_data_lesson18.json", "work\quiz_data_lesson19.json", "work\quiz_data_lesson20.json")

foreach ($jf in $lessons) {
    Write-Host "=========================================================="
    Write-Host "Rendering $jf..."
    & powershell -ExecutionPolicy Bypass -File "work\render_lesson_suite.ps1" -JsonFile $jf
}
Write-Host "Batch 5 rendering completed successfully!"
