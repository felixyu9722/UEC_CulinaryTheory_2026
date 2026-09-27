$ErrorActionPreference = 'Stop'
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$dataDir = Join-Path $scriptDir 'data'
$templateFile = Join-Path $scriptDir 'template.html'
$strFile = Join-Path $dataDir 'doc_strings_all_20.json'

$strRaw = [System.IO.File]::ReadAllText($strFile, [System.Text.Encoding]::UTF8)
$S = $strRaw | ConvertFrom-Json

$workspaceRoot = Split-Path -Parent $scriptDir
$outDir = Join-Path $workspaceRoot $S.outFolderName
if (-not (Test-Path $outDir)) {
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
}

$chapters = @()
for ($ch = 1; $ch -le 20; $ch++) {
    $chPad = ("0" + [string]$ch).Substring(("0" + [string]$ch).Length - 2)
    $jsonPath = Join-Path $dataDir ('chapter' + $chPad + '.json')
    $raw = [System.IO.File]::ReadAllText($jsonPath, [System.Text.Encoding]::UTF8)
    $data = $raw | ConvertFrom-Json
    $chapters += $data
}

$allJsonString = $chapters | ConvertTo-Json -Depth 10

$templateContent = [System.IO.File]::ReadAllText($templateFile, [System.Text.Encoding]::UTF8)

# Replace placeholders and custom headers
$html = $templateContent.Replace('__QUESTIONS_DATA_PLACEHOLDER__', $allJsonString)

$R = $S.htmlReplacements
if ($R.oldTitle -and $html.Contains($R.oldTitle)) { $html = $html.Replace($R.oldTitle, $R.newTitle) }
if ($R.oldBadge -and $html.Contains($R.oldBadge)) { $html = $html.Replace($R.oldBadge, $R.newBadge) }
if ($R.oldSub -and $html.Contains($R.oldSub)) { $html = $html.Replace($R.oldSub, $R.newSub) }
if ($R.oldCount -and $html.Contains("0 / " + $R.oldCount)) { $html = $html.Replace("0 / " + $R.oldCount, "0 / " + $R.newCount) }

$outHtmlPath = Join-Path $outDir $S.htmlFileName
[System.IO.File]::WriteAllText($outHtmlPath, $html, [System.Text.Encoding]::UTF8)

$rootHtmlPath = Join-Path $workspaceRoot $S.rootHtmlFileName
[System.IO.File]::WriteAllText($rootHtmlPath, $html, [System.Text.Encoding]::UTF8)

$indexHtmlPath = Join-Path $workspaceRoot 'index.html'
[System.IO.File]::WriteAllText($indexHtmlPath, $html, [System.Text.Encoding]::UTF8)

Write-Host ('Master All-in-One 800-Question Interactive HTML generated at: ' + $outHtmlPath)
Write-Host ('Root Interactive HTML generated at: ' + $rootHtmlPath)
Write-Host ('GitHub Pages Entry HTML generated at: ' + $indexHtmlPath)
