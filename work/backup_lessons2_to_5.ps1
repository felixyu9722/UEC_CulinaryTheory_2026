$root = (Get-Location).Path
$sourceDir = (Get-ChildItem -Directory -Filter "08_*").FullName
$backupDir = Join-Path $root "backup_lessons_2_to_5"

$files = Get-ChildItem -Path $sourceDir -File
foreach ($f in $files) {
    if ($f.Name -match "01_.*[2-5]") {
        Move-Item -Path $f.FullName -Destination $backupDir -Force
        Write-Host "Moved: $($f.Name)"
    }
}
Write-Host "Done"
