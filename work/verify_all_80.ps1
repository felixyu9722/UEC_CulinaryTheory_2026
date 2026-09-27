$targetDir = (Get-ChildItem -Directory | Where-Object { $_.Name -like "*08_*" }).FullName
$files = Get-ChildItem $targetDir
Write-Host "Total files found: $($files.Count)"
$docxs = ($files | Where-Object { $_.Extension -eq ".docx" }).Count
$mds = ($files | Where-Object { $_.Extension -eq ".md" }).Count
$zeroBytes = ($files | Where-Object { $_.Length -eq 0 }).Count
Write-Host "Docx files: $docxs"
Write-Host "MD files: $mds"
Write-Host "Zero-byte files: $zeroBytes"
