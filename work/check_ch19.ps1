$data = [System.IO.File]::ReadAllText("work\data\chapter19.json", [System.Text.Encoding]::UTF8) | ConvertFrom-Json
foreach ($q in $data.questions) {
    $la = $q.options.A.Length
    $lb = $q.options.B.Length
    $lc = $q.options.C.Length
    $ld = $q.options.D.Length
    $lens = @($la, $lb, $lc, $ld)
    $max = ($lens | Measure-Object -Maximum).Maximum
    $min = ($lens | Measure-Object -Minimum).Minimum
    $diff = $max - $min
    if ($diff -ge 12) {
        Write-Host "Q$($q.id): diff=$diff (A=$la, B=$lb, C=$lc, D=$ld)"
    }
}
