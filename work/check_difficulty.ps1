$files = Get-ChildItem "work\data\chapter1[6-9].json", "work\data\chapter20.json" | Sort-Object Name
foreach ($f in $files) {
    $data = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
    $groups = $data.questions | Group-Object difficulty | Sort-Object Name
    $str = ($groups | ForEach-Object { "$($_.Name): $($_.Count)" }) -join ", "
    Write-Host "$($f.Name) (Total: $($data.questions.Count)) -> $str"
}
