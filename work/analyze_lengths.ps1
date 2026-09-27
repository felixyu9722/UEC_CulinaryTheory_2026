$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'

$files = Get-ChildItem (Join-Path $dataDir "chapter*.json") | Sort-Object Name
foreach ($f in $files) {
    $data = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8) | ConvertFrom-Json
    $ch = $data.chapter_id
    
    $correctIsLongest = 0
    $hugeDiffCount = 0
    $details = @()
    
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
            $correctIsLongest++
            $details += "Q$($q.id) (Ans: $($q.answer), diff: $diff, A:$($lens.A), B:$($lens.B), C:$($lens.C), D:$($lens.D))"
        }
        if ($diff -ge 20) {
            $hugeDiffCount++
        }
    }
    Write-Host "Chapter $ch : $correctIsLongest questions where correct answer is longest by >=12 chars. $hugeDiffCount questions with diff >= 20 chars."
    if ($details.Count -gt 0) {
        Write-Host "  Examples: " ($details[0..([Math]::Min(3, $details.Count - 1))] -join "; ")
    }
}
