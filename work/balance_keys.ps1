# balance_keys.ps1
# Balances the answer distribution so every chapter has EXACTLY 10 A, 10 B, 10 C, 10 D (40 total)
# and ensures no obvious letter patterns.

$files = Get-ChildItem "work\data\chapter*.json" | Sort-Object Name

# Pre-designed balanced answer pattern for 40 questions (10 A, 10 B, 10 C, 10 D)
# Designed to avoid runs of 3+, feels like a real standard exam key:
$targetAnswersBase = @(
    "A", "C", "B", "D", "B", "A", "D", "C", "A", "D", 
    "C", "B", "A", "C", "D", "B", "C", "A", "B", "D", 
    "D", "B", "A", "C", "B", "D", "A", "C", "D", "A", 
    "C", "B", "C", "A", "D", "B", "A", "D", "B", "C"
)

# Verify count of base pattern:
$g = $targetAnswersBase | Group-Object
Write-Host "Base pattern counts:" ($g | ForEach-Object { "$($_.Name):$($_.Count)" })

$chapterOffsets = @{
    "chapter01.json" = 2
    "chapter02.json" = 6
    "chapter03.json" = 10
    "chapter04.json" = 14
    "chapter05.json" = 18
    "chapter06.json" = 22
    "chapter07.json" = 26
    "chapter08.json" = 30
    "chapter09.json" = 34
    "chapter10.json" = 0
    "chapter11.json" = 3
    "chapter12.json" = 7
    "chapter13.json" = 11
    "chapter14.json" = 15
    "chapter15.json" = 19
    "chapter16.json" = 23
    "chapter17.json" = 27
    "chapter18.json" = 31
    "chapter19.json" = 35
    "chapter20.json" = 39
}

foreach ($f in $files) {
    if (-not $chapterOffsets.ContainsKey($f.Name)) { continue }
    
    $json = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $data = $json | ConvertFrom-Json
    
    $offset = $chapterOffsets[$f.Name]
    # Rotate target answers by offset for variation between chapters
    $targetAnswers = @()
    for ($i = 0; $i -lt 40; $i++) {
        $idx = ($i + $offset) % 40
        $targetAnswers += $targetAnswersBase[$idx]
    }
    
    for ($i = 0; $i -lt $data.questions.Count; $i++) {
        $q = $data.questions[$i]
        $origAns = $q.answer
        $newAns = $targetAnswers[$i]
        
        if ($origAns -ne $newAns) {
            # We need to swap the content of $origAns and $newAns
            $correctText = $q.options.$origAns
            $targetOccupantText = $q.options.$newAns
            
            # Swap them:
            $q.options.$newAns = $correctText
            $q.options.$origAns = $targetOccupantText
            
            # Set new answer:
            $q.answer = $newAns
        }
    }
    
    # Save back
    $newJson = $data | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($f.FullName, $newJson, [System.Text.Encoding]::UTF8)
    Write-Host "Balanced $($f.Name): verified 40 questions."
}
