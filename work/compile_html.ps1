$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$templateFile = Join-Path $scriptDir 'template.html'
$strFile = Join-Path $dataDir 'doc_strings.json'

$strRaw = [System.IO.File]::ReadAllText($strFile, [System.Text.Encoding]::UTF8)
$S = $strRaw | ConvertFrom-Json

$workspaceRoot = Split-Path -Parent $scriptDir
$outDir = Join-Path $workspaceRoot $S.outFolderName
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$chapters = @()
for ($ch = 10; $ch -le 15; $ch++) {
    $jsonPath = Join-Path $dataDir ('chapter' + [string]$ch + '.json')
    $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
    $data = $raw | ConvertFrom-Json
    $chapters += $data
}

$allJsonString = $chapters | ConvertTo-Json -Depth 10

$templateContent = [System.IO.File]::ReadAllText($templateFile, [System.Text.Encoding]::UTF8)
$finalHtml = $templateContent.Replace('__QUESTIONS_DATA_PLACEHOLDER__', $allJsonString)

$outHtmlPath = Join-Path $outDir $S.htmlFileName
[System.IO.File]::WriteAllText($outHtmlPath, $finalHtml, [System.Text.Encoding]::UTF8)

Write-Host ('Interactive HTML generated at: ' + $outHtmlPath)
