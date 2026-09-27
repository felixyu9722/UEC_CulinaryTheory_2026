$dirs = Get-ChildItem -Directory
foreach ($d in $dirs) {
    Write-Host ("DIR: " + [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($d.Name)))
    $files = Get-ChildItem -File -Path $d.FullName
    foreach ($f in $files) {
        Write-Host ("  FILE: " + [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($f.Name)))
    }
}
