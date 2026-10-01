$lines = [System.IO.File]::ReadAllLines("work\oct_scan_fast.txt", [System.Text.Encoding]::UTF8)

$curFile = ""
$curSize = ""
$curLen = ""
$isCapturing = $false
$preview = New-Object System.Text.StringBuilder

$results = New-Object System.Text.StringBuilder

for ($i = 0; $i -lt $lines.Length; $i++) {
    $line = $lines[$i]
    if ($line.StartsWith("FILE: ")) {
        $curFile = $line.Substring(6)
    } elseif ($line.StartsWith("PREVIEW:")) {
        # Check if curFile is interesting
        if ($curFile -match "试卷|作答|题库|练习|中餐|西餐|餐饮|课钢|课纲|考试题目|报告表|损耗|原料笔记|烘焙\.docx") {
            [void]$results.AppendLine("==================================================")
            [void]$results.AppendLine("FILE: $curFile")
            # print next 30 lines
            for ($j = $i + 1; $j -lt [Math]::Min($i + 35, $lines.Length); $j++) {
                if ($lines[$j].StartsWith("========================================================")) { break }
                [void]$results.AppendLine($lines[$j])
            }
        }
    }
}

[System.IO.File]::WriteAllText("work\oct_exam_summary.txt", $results.ToString(), [System.Text.Encoding]::UTF8)
Write-Host "Done filtering exam files."
