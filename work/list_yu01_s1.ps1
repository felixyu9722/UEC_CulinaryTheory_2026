$yu = Get-ChildItem -Directory | Where-Object { $_.Name -like "yu 01*" }
$files = Get-ChildItem -Path $yu.FullName -Recurse -File | Where-Object { $_.Name -notlike "~$*" }
Write-Host "Total files in yu 01: $($files.Count)"
$s1Files = $files | Where-Object { $_.FullName -like "*S1*" }
Write-Host "S1 specific files: $($s1Files.Count)"
foreach ($f in $s1Files) {
    Write-Host $f.FullName.Substring($yu.FullName.Length + 1)
}
