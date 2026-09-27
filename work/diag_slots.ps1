$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$expDir = Join-Path $scriptDir 'data_expansion'

$hardSlots = @(3, 7, 11, 15, 19, 23, 27, 31, 35, 39)
$romanSlots = @(5, 13, 21, 29, 37)
$singleSlots = @(1..40 | Where-Object { $hardSlots -notcontains $_ -and $romanSlots -notcontains $_ })

$basePath = Join-Path $dataDir "chapter10.json"
$expPath = Join-Path $expDir "expansion_ch10.json"

$baseRaw = [System.IO.File]::ReadAllText($basePath, [System.Text.Encoding]::UTF8)
$baseData = $baseRaw | ConvertFrom-Json

$expRaw = [System.IO.File]::ReadAllText($expPath, [System.Text.Encoding]::UTF8)
$expData = $expRaw | ConvertFrom-Json

$hardQs = @($expData.questions)
$romanQs = @($baseData.questions | Where-Object { $_.type -eq 'roman' })
$singleQs = @($baseData.questions | Where-Object { $_.type -ne 'roman' })

Write-Host "hardQs count: $($hardQs.Count)"
Write-Host "romanQs count: $($romanQs.Count)"
Write-Host "singleQs count: $($singleQs.Count)"

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

for ($i = 0; $i -lt 40; $i++) {
    $item = $targetArray[$i]
    $status = if ($null -eq $item) { "NULL!" } else { "OK (type=" + $item.type + ")" }
    Write-Host "Slot $($i+1): $status"
}
