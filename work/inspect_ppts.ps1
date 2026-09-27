# Inspect PPTX files in root
$ppts = Get-ChildItem -Filter "*.pptx" | Sort-Object Name
Write-Host "=== Root PPTX Files ($($ppts.Count)) ==="
foreach ($p in $ppts) {
    Write-Host "$($p.Name) (Size: $([math]::Round($p.Length/1KB, 1)) KB)"
}
