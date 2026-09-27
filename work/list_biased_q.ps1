$files = Get-ChildItem "work\data\chapter0[256789].json" | Sort-Object Name
foreach ($f in $files) {
    $data = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
    foreach ($q in $data.questions) {
        $lens = @{
            A = $q.options.A.Length
            B = $q.options.B.Length
            C = $q.options.C.Length
            D = $q.options.D.Length
        }
        $maxLen = ($lens.Values | Measure-Object -Maximum).Maximum
        $minLen = ($lens.Values | Measure-Object -Minimum).Minimum
        $ansLen = $lens[$q.answer.Trim()]
        $diff = $maxLen - $minLen
        
        if ($ansLen -eq $maxLen -and $diff -ge 12) {
            Write-Host "$($f.Name) Q$($q.id) (Ans: $($q.answer), diff: $diff)"
            Write-Host "  A: $($q.options.A) ($($lens.A))"
            Write-Host "  B: $($q.options.B) ($($lens.B))"
            Write-Host "  C: $($q.options.C) ($($lens.C))"
            Write-Host "  D: $($q.options.D) ($($lens.D))`n"
        }
    }
}
