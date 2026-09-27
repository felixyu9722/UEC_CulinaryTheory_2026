$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$fixFile = Join-Path $scriptDir 'parallel_fixes.json'

$fixesRaw = [System.IO.File]::ReadAllText($fixFile, [System.Text.Encoding]::UTF8)
$fixes = $fixesRaw | ConvertFrom-Json

$groups = $fixes | Group-Object ch
foreach ($g in $groups) {
    $targetPath = Join-Path $dataDir $g.Name
    $json = [System.IO.File]::ReadAllText($targetPath, [System.Text.Encoding]::UTF8)
    $data = $json | ConvertFrom-Json
    
    foreach ($item in $g.Group) {
        $q = $data.questions | Where-Object { $_.id -eq $item.id }
        if ($q) {
            if ($item.A) { $q.options.A = $item.A }
            if ($item.B) { $q.options.B = $item.B }
            if ($item.C) { $q.options.C = $item.C }
            if ($item.D) { $q.options.D = $item.D }
        }
    }
    
    $newJson = $data | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($targetPath, $newJson, [System.Text.Encoding]::UTF8)
    Write-Host ("Applied fixes to " + $g.Name)
}
