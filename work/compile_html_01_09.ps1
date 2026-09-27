$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$templateFile = Join-Path $scriptDir 'template.html'
$strFile = Join-Path $dataDir 'doc_strings_01_09.json'

$strRaw = [System.IO.File]::ReadAllText($strFile, [System.Text.Encoding]::UTF8)
$S = $strRaw | ConvertFrom-Json

$workspaceRoot = Split-Path -Parent $scriptDir
$outDir = Join-Path $workspaceRoot $S.outFolderName
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$chapters = @()
for ($ch = 1; $ch -le 9; $ch++) {
    $chPad = ("0" + [string]$ch).Substring(("0" + [string]$ch).Length - 2)
    $jsonPath = Join-Path $dataDir ('chapter' + $chPad + '.json')
    $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
    $data = $raw | ConvertFrom-Json
    $chapters += $data
}

$allJsonString = $chapters | ConvertTo-Json -Depth 10

$templateContent = [System.IO.File]::ReadAllText($templateFile, [System.Text.Encoding]::UTF8)

# Replace placeholders and custom headers from JSON
$html = $templateContent.Replace('__QUESTIONS_DATA_PLACEHOLDER__', $allJsonString)

$R = $S.htmlReplacements
$html = $html.Replace($R.oldTitle, $R.newTitle)
$html = $html.Replace($R.oldBadge, $R.newBadge)
$html = $html.Replace($R.oldSub, $R.newSub)
$html = $html.Replace("0 / " + $R.oldCount, "0 / " + $R.newCount)
$html = $html.Replace("totalQuestions = " + $R.oldCount, "totalQuestions = " + $R.newCount)

$outHtmlPath = Join-Path $outDir $S.htmlFileName
[System.IO.File]::WriteAllText($outHtmlPath, $html, [System.Text.Encoding]::UTF8)

Write-Host ('Interactive HTML generated at: ' + $outHtmlPath)
