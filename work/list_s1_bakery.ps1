$yu = Get-ChildItem -Directory | Where-Object { $_.Name -like "yu 01*" }
$s1 = Get-ChildItem -Path $yu.FullName -Directory | Where-Object { $_.Name -like "*S1 BAKERY*" }
Get-ChildItem -Path $s1.FullName -Recurse -Depth 2 | ForEach-Object {
    $rel = $_.FullName.Substring((Get-Location).Path.Length + 1)
    Write-Host $rel
}
