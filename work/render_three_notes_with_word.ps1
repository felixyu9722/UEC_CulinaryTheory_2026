$ErrorActionPreference='Stop'
$base='C:\Users\GOH\Desktop\2026年统考厨艺理论'
$items=@(
 @{Doc=(Join-Path $base '04_学生笔记重点收藏\高一_学生笔记重点收藏.docx'); Pdf=(Join-Path $base 'work\qa_word\高一.pdf')},
 @{Doc=(Join-Path $base '04_学生笔记重点收藏\高二_学生笔记重点收藏.docx'); Pdf=(Join-Path $base 'work\qa_word\高二.pdf')},
 @{Doc=(Join-Path $base '04_学生笔记重点收藏\高三_学生笔记重点收藏.docx'); Pdf=(Join-Path $base 'work\qa_word\高三.pdf')}
)
New-Item -ItemType Directory -Path (Join-Path $base 'work\qa_word') -Force | Out-Null
foreach($i in $items){
 $word=New-Object -ComObject Word.Application
 $word.Visible=$false; $word.DisplayAlerts=0
 try {
  $d=$word.Documents.Open($i.Doc,$false,$true,$false)
  $d.ExportAsFixedFormat($i.Pdf,17)
  $d.Close($false)
 } finally {
  $word.Quit()
  [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word)|Out-Null
  [GC]::Collect(); [GC]::WaitForPendingFinalizers()
 }
}
Get-Item ($items.Pdf) | Select-Object FullName,Length
