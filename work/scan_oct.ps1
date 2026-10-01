$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $allFiles = Get-ChildItem -Path "OCT 2026*" -Recurse -File -Include *.docx, *.doc
    foreach ($item in $allFiles) {
        $p = $item.FullName
        # Filter for interesting ones
        if ($p -match "作答|试卷|课钢|课纲|题库|中餐|西餐|餐饮") {
            Write-Host "================== FILE: $($item.Name) =================="
            Write-Host "PATH: $p"
            try {
                $doc = $word.Documents.Open($p, $false, $true)
                $txt = $doc.Content.Text
                $doc.Close()
                $len = [Math]::Min(1000, $txt.Length)
                Write-Host $txt.Substring(0, $len)
                Write-Host "`n------------------------------------------------`n"
            } catch {
                Write-Host "Error opening: $_"
            }
        }
    }
} finally {
    $word.Quit()
}
