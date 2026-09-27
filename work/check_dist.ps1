$files = Get-ChildItem "work\data\chapter*.json" | Sort-Object Name
foreach ($f in $files) {
    $json = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $data = $json | ConvertFrom-Json
    $groups = $data.questions | Group-Object answer | Sort-Object Name
    $dist = ($groups | ForEach-Object { "$($_.Name): $($_.Count)" }) -join ", "
    Write-Host "$($f.Name) (Total: $($data.questions.Count)) -> $dist"
}
