[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
$pageId = "3cb138c5-b398-8168-87db-e011f8d96405"

$headers = @{
    "Authorization" = "Bearer $token"
    "Notion-Version" = "2022-06-28"
    "Content-Type"  = "application/json; charset=utf-8"
}

$bodyObj = @{
    children = @(
        @{
            object = "block"
            type   = "heading_2"
            heading_2 = @{
                rich_text = @(
                    @{
                        type = "text"
                        text = @{ content = "五、2026统考新增核心考点：中餐八大菜系与经典名菜全景表" }
                    }
                )
            }
        },
        @{
            object = "block"
            type   = "callout"
            callout = @{
                icon = @{ emoji = "🏮" }
                rich_text = @(
                    @{
                        type = "text"
                        text = @{
                            content = "【统考教研重点：八大菜系形成、风味与名菜对应】`n" +
                                      "1. 鲁菜（山东）：历史最悠久，咸鲜浓油赤酱。代表菜：九转大肠（猪大肠）、糖醋鲤鱼。`n" +
                                      "2. 川菜（四川、重庆）：重油重盐、麻辣鲜香。代表菜：麻婆豆腐（主要调味：辣豆瓣酱）、宫保鸡丁、四川火锅。`n" +
                                      "3. 粤菜（广东）：追求原汁原味，咸鲜清淡。代表菜：脆皮乳猪、白切鸡、蜜汁叉烧。`n" +
                                      "4. 苏菜（江苏/淮扬）：清淡微甜、重黄酒味。代表菜：红烧狮子头（五花肉/绞肉）、软兜长鱼（鳝鱼）。`n" +
                                      "5. 浙菜（浙江/杭州）：酱香浓郁、清鲜爽脆。代表菜：红烧下巴（草鱼下巴，属淡水鱼）、西湖醋鱼、东坡肉、粉蒸肉（五花肉裹米粉）。`n" +
                                      "6. 闽菜（福建/福州）：南部咸甜、北部香辣。代表菜：佛跳墙（福寿全，集鲍鱼、海参、鱼翅、干贝等山珍海味于一盅）。`n" +
                                      "7. 徽菜（安徽）：重油、重盐。代表菜：红烧划水（草鱼尾部，属淡水鱼）、徽州臭鳜鱼。`n" +
                                      "8. 湘菜（湖南）：重油重辣、腌制腊味。代表菜：炒血鸭（主料：鸭肉与鸭血）、剁椒鱼头。"
                        }
                    }
                )
            }
        }
    )
}

$jsonBody = $bodyObj | ConvertTo-Json -Depth 6
$utf8Bytes = [System.Text.Encoding]::UTF8.GetBytes($jsonBody)

Write-Host "Appending blocks to page $pageId ..."
$res = Invoke-RestMethod -Uri "https://api.notion.com/v1/blocks/$pageId/children" -Headers $headers -Method Patch -Body $utf8Bytes
Write-Host "SUCCESS! Appended $($res.results.Count) blocks."
