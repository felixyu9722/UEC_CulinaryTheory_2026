$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $files = @(
        'OCT 2026 资料增加\统考厨艺理论\烘焙课程资料\计算（损耗倍数）\试卷1(烘焙).docx',
        'OCT 2026 资料增加\统考厨艺理论\烘焙课程资料\计算（损耗倍数）\试卷2(烘焙).docx',
        'OCT 2026 资料增加\统考厨艺理论\烘焙课程资料\new班用 S1 BAKERY 笔作业2024\S1烘焙作答2024.docx',
        'OCT 2026 资料增加\统考厨艺理论\烘焙课程资料\new班用S2 txt +笔练习2024 done\S2作答2024done.docx',
        'OCT 2026 资料增加\统考厨艺理论\烘焙课程资料\烘焙班课纲\亚罗士打新民独中~高中厨艺（烘焙理论）课钢.docx',
        'OCT 2026 资料增加\统考厨艺理论\烘焙课程资料\new班用 S1 BAKERY 笔作业2024\烘作答Q&A(exam 参考）done\S3作答要整理2024蛋糕.docx'
    )
    foreach ($f in $files) {
        $full = Join-Path 'C:\Users\GOH\Desktop\2026年统考厨艺理论' $f
        if (Test-Path $full) {
            Write-Host "================== FILE: $f =================="
            $doc = $word.Documents.Open($full, $false, $true)
            $txt = $doc.Content.Text
            $doc.Close()
            $len = [Math]::Min(1200, $txt.Length)
            Write-Host $txt.Substring(0, $len)
        }
    }
} finally {
    $word.Quit()
}
