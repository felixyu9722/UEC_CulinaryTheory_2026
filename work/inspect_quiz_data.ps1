$raw = [System.IO.File]::ReadAllText("work\data\chapter16.json", [System.Text.Encoding]::UTF8)
$data = $raw | ConvertFrom-Json
Write-Host "chapter: $($data.chapter)"
Write-Host "title: $($data.title)"
Write-Host "chapter_id: $($data.chapter_id)"
