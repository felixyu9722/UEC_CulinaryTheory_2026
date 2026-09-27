$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$expDir = Join-Path $scriptDir 'data_expansion'

$hardSlots = @(3, 7, 11, 15, 19, 23, 27, 31, 35, 39)
$romanSlots = @(5, 13, 21, 29, 37)
$singleSlots = @(1..40 | Where-Object { $hardSlots -notcontains $_ -and $romanSlots -notcontains $_ })

Write-Host "Single slots count: $($singleSlots.Count)"
Write-Host "Hard slots count: $($hardSlots.Count)"
Write-Host "Roman slots count: $($romanSlots.Count)"

for ($ch = 10; $ch -le 15; $ch++) {
    $basePath = Join-Path $dataDir ("chapter$ch.json")
    $expPath = Join-Path $expDir ("expansion_ch$ch.json")

    $baseRaw = [System.IO.File]::ReadAllText($basePath, [System.Text.Encoding]::UTF8)
    $baseData = $baseRaw | ConvertFrom-Json

    $expRaw = [System.IO.File]::ReadAllText($expPath, [System.Text.Encoding]::UTF8)
    $expData = $expRaw | ConvertFrom-Json

    $hardQs = @($expData)
    $romanQs = @($baseData.questions | Where-Object { $_.type -eq 'roman' })
    $singleQs = @($baseData.questions | Where-Object { $_.type -ne 'roman' })

    if ($hardQs.Count -ne 10) { throw "Chapter $ch hard questions count is $($hardQs.Count), expected 10" }
    if ($romanQs.Count -ne 5) { throw "Chapter $ch roman questions count is $($romanQs.Count), expected 5" }
    if ($singleQs.Count -ne 25) { throw "Chapter $ch single questions count is $($singleQs.Count), expected 25" }

    $targetArray = New-Object object[] 40

    for ($i = 0; $i -lt 10; $i++) {
        $idx = $hardSlots[$i] - 1
        $targetArray[$idx] = $hardQs[$i]
    }

    for ($i = 0; $i -lt 5; $i++) {
        $idx = $romanSlots[$i] - 1
        $targetArray[$idx] = $romanQs[$i]
    }

    for ($i = 0; $i -lt 25; $i++) {
        $idx = $singleSlots[$i] - 1
        $targetArray[$idx] = $singleQs[$i]
    }

    $finalQuestions = @()
    for ($i = 0; $i -lt 40; $i++) {
        $q = $targetArray[$i]
        $q | Add-Member -MemberType NoteProperty -Name 'id' -Value ($i + 1) -Force
        $finalQuestions += $q
    }

    $baseData.questions = $finalQuestions

    $counts = @{ A = 0; B = 0; C = 0; D = 0 }
    foreach ($q in $finalQuestions) {
        $ans = $q.answer.Trim()
        $counts[$ans]++
    }

    Write-Host "Chapter $ch Answer Distribution: A=$($counts['A']), B=$($counts['B']), C=$($counts['C']), D=$($counts['D']), Total=$($finalQuestions.Count)"
    if ($counts['A'] -ne 10 -or $counts['B'] -ne 10 -or $counts['C'] -ne 10 -or $counts['D'] -ne 10) {
        throw "Chapter $ch answers not balanced! Expected 10/10/10/10."
    }

    $outJson = $baseData | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($basePath, $outJson, [System.Text.Encoding]::UTF8)
    Write-Host "Successfully merged and saved Chapter $ch (40 questions, shuffled difficulty)."
}
Write-Host "ALL 6 CHAPTERS MERGED PERFECTLY!"
