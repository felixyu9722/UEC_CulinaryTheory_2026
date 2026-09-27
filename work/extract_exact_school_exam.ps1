$word = New-Object -ComObject Word.Application
$word.Visible = $false

$ws = (Get-Item .).FullName
$dirName = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("6auY5LiA5qCh5YaFIC0g5rWL6aqM6aKY55uu"))
$fullDir = Join-Path $ws $dirName

$f1 = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("6auY5LiAIOeDmOeEmeWfuuehgOeQhuiuuua1i+mqjF8wMS5kb2N4"))
$doc1 = $word.Documents.Open((Join-Path $fullDir $f1))
$txt1 = $doc1.Content.Text
$doc1.Close($false)
[System.IO.File]::WriteAllText("work\school_exam_questions.txt", $txt1, [System.Text.Encoding]::UTF8)

$f2 = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("6auY5LiAIOeDmOeEmeWfuuehgOeQhuiuuua1i+mqjF8wMV/mlZnluIjlj4LogIPnrZTmoYguZG9jeA=="))
$doc2 = $word.Documents.Open((Join-Path $fullDir $f2))
$txt2 = $doc2.Content.Text
$doc2.Close($false)
[System.IO.File]::WriteAllText("work\school_exam_answers.txt", $txt2, [System.Text.Encoding]::UTF8)

$word.Quit()
Write-Host "Extracted school exam successfully!"
