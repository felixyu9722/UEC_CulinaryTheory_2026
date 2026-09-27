param([string]$file)
$json = Get-Content $file -Raw -Encoding UTF8 | ConvertFrom-Json
$groups = $json.questions | Group-Object answer | Select-Object Name, Count
Write-Host "File: $file (Total: $($json.questions.Count))"
$groups | ForEach-Object { Write-Host "$($_.Name): $($_.Count)" }
