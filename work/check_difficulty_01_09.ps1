$files = Get-ChildItem "work\data\chapter0[1-9].json" | Sort-Object Name
foreach ($f in $files) {
    $data = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
    $groups = $data.questions | Group-Object difficulty | Sort-Object Name
    $str = ($groups | ForEach-Object { "$($_.Name): $($_.Count)" }) -join ", "
    $combos = ($data.questions | Where-Object { $_.type -eq 'combination' }).Count
    Write-Host "$($f.Name) (Total: $($data.questions.Count), Combos: $combos) -> $str"
}
