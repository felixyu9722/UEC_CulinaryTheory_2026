$pdfFile = (Get-ChildItem -Filter "*.pdf" | Select-Object -First 1).FullName
Write-Host "Found PDF: $pdfFile"
$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $doc = $word.Documents.Open($pdfFile, $false, $true)
    $text = $doc.Content.Text
    [System.IO.File]::WriteAllText("work\pdf_syllabus_text.txt", $text, [System.Text.Encoding]::UTF8)
    Write-Host "Extracted text length: $($text.Length)"
    $doc.Close([ref]$false)
} catch {
    Write-Host "Error occurred"
} finally {
    $word.Quit()
}
