$baseUrl = "https://oaoadna-1313.github.io/yessong/"
$excelPath = "c:\2026_歌SONG臺北\【閱思龍門】歌SONG單元_全網站網頁對照總覽表.xlsx"

if (Test-Path $excelPath) {
    Remove-Item $excelPath -Force
}

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false

$workbook = $excel.Workbooks.Add()
$sheet = $workbook.Worksheets.Item(1)
$sheet.Name = "歌SONG全系列網頁對照表"

# Colors (BGR hex or RGB int)
# Purple Theme: RGB(49, 46, 129) = 0x312E81 -> BGR: 0x812E31 = 8465969
$hdrBgColor = 8465969
$hdrTextColor = 16777215 # White
$zebraColor = 16514043   # Slate-50: RGB(248, 250, 252) -> BGR: 0xFCFAF8 = 16579320

# 1. Title Banner (Row 1)
$sheet.Range("A1:L1").Merge()
$titleCell = $sheet.Range("A1")
$titleCell.Value2 = "【閱思龍門】歌SONG單元・音樂地誌互動教學平台 全網站網頁對照總覽表"
$titleCell.Font.Name = "微軟正黑體"
$titleCell.Font.Size = 16
$titleCell.Font.Bold = $true
$titleCell.Font.Color = 16777215
$titleCell.Interior.Color = 4337220 # Dark Purple / Slate: RGB(67, 56, 202) -> BGR: 0xCA3843 = 13252675
$titleCell.HorizontalAlignment = -4108 # xlCenter
$titleCell.VerticalAlignment = -4108   # xlCenter
$sheet.Rows.Item(1).RowHeight = 40

# 2. Subtitle / Metadata (Row 2)
$sheet.Range("A2:L2").Merge()
$subCell = $sheet.Range("A2")
$subCell.Value2 = "🌐 線上發布總入口：https://oaoadna-1313.github.io/yessong/   |   本網頁由黃于珊老師利用 Google antigravity 2.0 生成製作，僅供教學使用。   |   全系列共 6 大學期單元、22 首文學歌曲、34 頁互動教學網頁"
$subCell.Font.Name = "微軟正黑體"
$subCell.Font.Size = 10
$subCell.Font.Color = 4473924
$subCell.Interior.Color = 15921906 # Light purple-gray
$subCell.HorizontalAlignment = -4108
$subCell.VerticalAlignment = -4108
$sheet.Rows.Item(2).RowHeight = 24

# 3. Column Headers (Row 3)
$headers = @(
    "序號",
    "學期／冊別",
    "單元名稱",
    "單元主題意境標語",
    "頁面類型",
    "歌曲／頁面名稱",
    "演唱歌手／主講",
    "作詞／作曲／年代",
    "教學亮點與特色標籤",
    "本地相對路徑",
    "GitHub Pages 線上完整網址",
    "點擊開啟線上網頁"
)

for ($i = 0; $i -lt $headers.Count; $i++) {
    $col = $i + 1
    $cell = $sheet.Cells.Item(3, $col)
    $cell.Value2 = $headers[$i]
    $cell.Font.Name = "微軟正黑體"
    $cell.Font.Size = 11
    $cell.Font.Bold = $true
    $cell.Font.Color = 16777215
    $cell.Interior.Color = 7092823 # Indigo
    $cell.HorizontalAlignment = -4108
    $cell.VerticalAlignment = -4108
}
$sheet.Rows.Item(3).RowHeight = 28

# 4. Data Rows
$pages = @(
    @{ Grade = "全學程總覽"; Unit = "全學程總目錄"; Theme = "認識龍門 → 遇見大安 → 探索臺北 → 看見臺灣 → 放眼世界 → 思考未來"; PageType = "總目錄導覽首頁"; Title = "【閱思龍門】歌SONG系列 目錄總覽"; Artist = "學思軒・全體師生"; Creator = "黃于珊老師利用 Google antigravity 2.0 製作"; Tag = "六大單元導覽・年級篩選・即時搜尋・學習地圖・校本課程願景"; Path = "index.html" },
    @{ Grade = "七年級上學期"; Unit = "歌SONG龍門"; Theme = "詠唱校園心聲・穿梭青春韶光與龍門記憶"; PageType = "單元主頁"; Title = "【7上認識龍門】歌SONG龍門 教學首頁"; Artist = "五月天 / 龍門師生"; Creator = "跨時代校園青春金曲"; Tag = "黑膠唱盤・三首曲目切換・填空測驗・心得探究"; Path = "longmen/index.html" },
    @{ Grade = "七年級上學期"; Unit = "歌SONG龍門"; Theme = "詠唱校園心聲・穿梭青春韶光與龍門記憶"; PageType = "單曲互動學習單"; Title = "龍門國中校歌"; Artist = "龍門國中全體師生"; Creator = "詞：賈生海、潘水波 / 曲：黃友棣"; Tag = "七星仙境・魚躍龍門・生詞田字格注音（鰲峰、遐邇、韶光、化育）"; Path = "longmen/school-anthem.html" },
    @{ Grade = "七年級上學期"; Unit = "歌SONG龍門"; Theme = "詠唱校園心聲・穿梭青春韶光與龍門記憶"; PageType = "單曲互動學習單"; Title = "三個傻瓜"; Artist = "五月天"; Creator = "詞：阿信 / 曲：怪獸"; Tag = "告別盲從・追求理想・生詞田字格注音（分數、盲目、束縛）"; Path = "longmen/three-idiots.html" },
    @{ Grade = "七年級上學期"; Unit = "歌SONG龍門"; Theme = "詠唱校園心聲・穿梭青春韶光與龍門記憶"; PageType = "單曲互動學習單"; Title = "人生有限公司"; Artist = "五月天"; Creator = "詞：阿信 / 曲：怪獸"; Tag = "青春自傳起跑・韶光珍惜・生詞田字格注音（一期一會、有限公司）"; Path = "longmen/life-co-ltd.html" },
    @{ Grade = "七年級下學期"; Unit = "歌SONG大安"; Theme = "遇見大安森呼吸・穿梭校園林蔭與流行金曲記憶"; PageType = "單元主頁"; Title = "【7下遇見大安】歌SONG大安 教學首頁"; Artist = "蘇打綠 / 吳青峰"; Creator = "大安森林公園綠意生態巡禮"; Tag = "大安生態絮語・中英對照・黑膠播放器・生詞田字格"; Path = "daan/index.html" },
    @{ Grade = "七年級下學期"; Unit = "歌SONG大安"; Theme = "遇見大安森呼吸・穿梭校園林蔭與流行金曲記憶"; PageType = "單曲互動學習單"; Title = "從一片落葉開始"; Artist = "蘇打綠"; Creator = "詞：吳青峰 / 曲：吳青峰"; Tag = "落葉奇境・自然絮語・生詞注音（秋天、旋律、凋零）"; Path = "daan/fallen-leaf.html" },
    @{ Grade = "七年級下學期"; Unit = "歌SONG大安"; Theme = "遇見大安森呼吸・穿梭校園林蔭與流行金曲記憶"; PageType = "單曲互動學習單"; Title = "請聽"; Artist = "吳青峰"; Creator = "詞：吳青峰 / 曲：吳青峰"; Tag = "側耳傾聽大自然心跳・城市綠洲靈感・田字格注音"; Path = "daan/listen.html" },
    @{ Grade = "七年級下學期"; Unit = "歌SONG大安"; Theme = "遇見大安森呼吸・穿梭校園林蔭與流行金曲記憶"; PageType = "單曲互動學習單 (英文版)"; Title = "It Began With A Fallen Leaf"; Artist = "蘇打綠 ft. Przemysław Wójcicki"; Creator = "詞曲：吳青峰 / 英文詮釋"; Tag = "國際雙語共鳴・英文歌詞挖洞・跨國合作"; Path = "daan/fallen-leaf-en.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單元主頁"; Title = "【8上探索臺北】歌SONG臺北 教學首頁"; Artist = "跨世代都會歌手群"; Creator = "臺北都會意象與歷史變遷"; Tag = "7首經典收錄・臺語臺羅對照・時代思辨・都會萬象"; Path = "taipei/index.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單"; Title = "台北天晴"; Artist = "嚴正嵐"; Creator = "詞：嚴正嵐 / 曲：嚴正嵐"; Tag = "治癒系・雨後臺北・遍體鱗傷・雨過天晴"; Path = "taipei/taipei-sunny.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單"; Title = "台北調"; Artist = "南西樂團"; Creator = "詞：南西樂團 / 曲：南西樂團"; Tag = "律動感・都會節奏・捷運蕭邦圓舞曲・手舞足蹈"; Path = "taipei/taipei-tune.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單"; Title = "台北的天空"; Artist = "王芷蕾 / 李翊君"; Creator = "詞：陳克華 / 曲：陳復明"; Tag = "時代金曲・溫暖鄉愁・離人歸宿・年少青春"; Path = "taipei/taipei-sky.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單 (臺羅漢羅)"; Title = "向前走"; Artist = "林強"; Creator = "詞：林強 / 曲：林強"; Tag = "臺語新浪潮・臺北車站拼搏精神・臺羅拼音對齊・啥咪攏毋驚"; Path = "taipei/moving-forward.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單"; Title = "臺北沉睡了"; Artist = "炎亞綸"; Creator = "詞：陳信延 / 曲：張簡君偉"; Tag = "深夜街景・寂靜情思・都會寂寞"; Path = "taipei/taipei-crash.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單"; Title = "台北某個地方"; Artist = "陳綺貞"; Creator = "詞：陳綺貞 / 曲：陳綺貞"; Tag = "文青詩意・角落漫遊・城市記憶與追尋"; Path = "taipei/taipei-person.html" },
    @{ Grade = "八年級上學期"; Unit = "歌SONG臺北"; Theme = "穿梭臺北十二行政區與文學地誌的文青漫遊"; PageType = "單曲互動學習單"; Title = "鹿港小鎮"; Artist = "羅大佑"; Creator = "詞：羅大佑 / 曲：羅大佑"; Tag = "時代巨作・傳統與工業文明反思・台北不是我的家"; Path = "taipei/lukang-town.html" },
    @{ Grade = "八年級下學期"; Unit = "歌SONG臺灣"; Theme = "側耳傾聽土地心跳・連結臺灣鄉土情懷與希望之聲"; PageType = "單元主頁"; Title = "【8下看見臺灣】歌SONG臺灣 教學首頁"; Artist = "蔡依林 / 李英宏 / 滅火器"; Creator = "鄉土文化與土地情感之歌"; Tag = "土地心跳・台語文學台羅標記・常民生活采風"; Path = "taiwan/index.html" },
    @{ Grade = "八年級下學期"; Unit = "歌SONG臺灣"; Theme = "側耳傾聽土地心跳・連結臺灣鄉土情懷與希望之聲"; PageType = "單曲互動學習單"; Title = "台灣的心跳聲"; Artist = "蔡依林 (Rap: 寇家瑞)"; Creator = "詞：方文山 / 曲：林邁可"; Tag = "2010上海世博台灣館主題曲・嘉南平原・八家將・雲門狂草・平溪天燈"; Path = "taiwan/taiwan-heartbeat.html" },
    @{ Grade = "八年級下學期"; Unit = "歌SONG臺灣"; Theme = "側耳傾聽土地心跳・連結臺灣鄉土情懷與希望之聲"; PageType = "單曲互動學習單"; Title = "在路上"; Artist = "李英宏"; Creator = "詞：李英宏 / 曲：李英宏"; Tag = "公路旅行・島嶼漫遊・沿途風土與自由馳騁"; Path = "taiwan/on-the-road.html" },
    @{ Grade = "八年級下學期"; Unit = "歌SONG臺灣"; Theme = "側耳傾聽土地心跳・連結臺灣鄉土情懷與希望之聲"; PageType = "單曲互動學習單 (台羅漢羅)"; Title = "晚安台灣"; Artist = "滅火器"; Creator = "詞：楊大正 / 曲：楊大正"; Tag = "金曲溫柔禱詞・守護家園力量・全台羅拼音逐行對齊・願你順遂"; Path = "taiwan/goodnight-taiwan.html" },
    @{ Grade = "九年級上學期"; Unit = "歌SONG世界"; Theme = "唱遊寰宇五大洲・擁抱多元文化與國際視野"; PageType = "單元主頁"; Title = "【9上放眼世界】歌SONG世界 教學首頁"; Artist = "Yakko / 旺福 / I-WANT星勢力"; Creator = "寰宇五大洲與多元族群"; Tag = "地理狂想・地圖亮點・原民吟唱・世大運金曲"; Path = "world/index.html" },
    @{ Grade = "九年級上學期"; Unit = "歌SONG世界"; Theme = "唱遊寰宇五大洲・擁抱多元文化與國際視野"; PageType = "單曲互動學習單"; Title = "一首歌帶你唱遍全世界"; Artist = "Animaniacs (Yakko)"; Creator = "詞曲：Randy Rogel / 墨西哥帽子舞"; Tag = "Yakko's World・五大洲各國巡禮・影片4:59臺灣亮點現身"; Path = "world/sing-the-world.html" },
    @{ Grade = "九年級上學期"; Unit = "歌SONG世界"; Theme = "唱遊寰宇五大洲・擁抱多元文化與國際視野"; PageType = "單曲互動學習單"; Title = "環遊世界"; Artist = "旺福"; Creator = "詞：小民 / 曲：小民"; Tag = "復古陽光搖滾・巴黎鐵塔・東京鐵塔・比薩斜塔・雷峰塔"; Path = "world/travel-the-world.html" },
    @{ Grade = "九年級上學期"; Unit = "歌SONG世界"; Theme = "唱遊寰宇五大洲・擁抱多元文化與國際視野"; PageType = "單曲互動學習單"; Title = "擁抱世界擁抱你"; Artist = "I-WANT 星勢力"; Creator = "詞：舞炯恩 / 曲：舞炯恩"; Tag = "2017臺北世大運主題曲・排灣族傳統吟唱 i u giugi・國際友誼"; Path = "world/embrace-the-world.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "單元主頁"; Title = "【9下思考未來】歌SONG未來 教學首頁"; Artist = "五月天 / 蘇打綠 / 張雨生 / 茄子蛋"; Creator = "青春告別與未來夢想宣言"; Tag = "會考與畢業展望・多版本歌曲對照・自傳詩意哲思"; Path = "future/index.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "單曲互動學習單 (五月天原版)"; Title = "後青春期的詩"; Artist = "五月天"; Creator = "詞：阿信 / 曲：阿信"; Tag = "五月天原版MV・告別突然・自傳如詩・生命彼岸"; Path = "future/post-adolescence.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "單曲互動學習單 (詩意朗讀版)"; Title = "後青春期的詩 (詩意版)"; Artist = "五月天"; Creator = "詞：阿信 / 曲：阿信"; Tag = "文字詩意朗讀賞析・字詞詮釋・畢業感懷"; Path = "future/post-youth-poem.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "單曲互動學習單"; Title = "近未來"; Artist = "蘇打綠"; Creator = "詞：吳青峰 / 曲：吳青峰"; Tag = "晨曦破曉・夏／狂熱壓軸・生命裂縫中的陽光"; Path = "future/near-future.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "單曲互動學習單 (三版本總覽)"; Title = "我的未來不是夢 (綜合版)"; Artist = "張雨生 / 茄子蛋 / 蘇打綠"; Creator = "詞：陳家麗 / 曲：翁孝良"; Tag = "原版昂揚 vs 搖滾狂熱 vs 溫柔民謠 三合一切換"; Path = "future/future-dream.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "單曲互動學習單"; Title = "我的未來不是夢 (特輯版)"; Artist = "張雨生 / 茄子蛋 / 蘇打綠"; Creator = "詞：陳家麗 / 曲：翁孝良"; Tag = "認真過每一分鐘・對自己的承諾"; Path = "future/my-future-is-not-a-dream.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "版本子頁 (張雨生原版)"; Title = "我的未來不是夢 (張雨生 原唱)"; Artist = "張雨生 (1988)"; Creator = "詞：陳家麗 / 曲：翁孝良"; Tag = "1988時代經典原聲・高亢嗓音與堅毅信念"; Path = "future/future-dream-chang.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "版本子頁 (茄子蛋搖滾版)"; Title = "我的未來不是夢 (茄子蛋 搖滾)"; Artist = "茄子蛋 (2020)"; Creator = "詞：陳家麗 / 改編搖滾"; Tag = "現代爆裂搖滾風格・MV影像結合"; Path = "future/future-dream-eggbant.html" },
    @{ Grade = "九年級下學期"; Unit = "歌SONG未來"; Theme = "迎向晨曦與未知・寫下青春彼岸燦爛自傳"; PageType = "版本子頁 (蘇打綠抒情版)"; Title = "我的未來不是夢 (蘇打綠 抒情)"; Artist = "蘇打綠 (2006)"; Creator = "詞：陳家麗 / 現場抒情"; Tag = "青峰清澈嗓音・木吉他溫柔撫慰低語"; Path = "future/future-dream-sodagreen.html" }
)

$startRow = 4
for ($idx = 0; $idx -lt $pages.Count; $idx++) {
    $row = $startRow + $idx
    $p = $pages[$idx]
    $fullUrl = if ($p.Path -eq "index.html") { $baseUrl } else { "$baseUrl$($p.Path)" }

    $sheet.Cells.Item($row, 1).Value2 = "$($idx + 1)"
    $sheet.Cells.Item($row, 2).Value2 = $p.Grade
    $sheet.Cells.Item($row, 3).Value2 = $p.Unit
    $sheet.Cells.Item($row, 4).Value2 = $p.Theme
    $sheet.Cells.Item($row, 5).Value2 = $p.PageType
    $sheet.Cells.Item($row, 6).Value2 = $p.Title
    $sheet.Cells.Item($row, 7).Value2 = $p.Artist
    $sheet.Cells.Item($row, 8).Value2 = $p.Creator
    $sheet.Cells.Item($row, 9).Value2 = $p.Tag
    $sheet.Cells.Item($row, 10).Value2 = $p.Path
    $sheet.Cells.Item($row, 11).Value2 = $fullUrl
    
    # Formula for clickable hyperlink
    $sheet.Cells.Item($row, 12).Formula = "=HYPERLINK(`"$fullUrl`", `"🌐 開啟網頁`")"

    # Font & formatting
    $rowRange = $sheet.Range("A$row`:L$row")
    $rowRange.Font.Name = "微軟正黑體"
    $rowRange.Font.Size = 10
    $sheet.Rows.Item($row).RowHeight = 22

    # Alignments
    $sheet.Cells.Item($row, 1).HorizontalAlignment = -4108 # Center
    $sheet.Cells.Item($row, 2).HorizontalAlignment = -4108 # Center
    $sheet.Cells.Item($row, 3).HorizontalAlignment = -4108 # Center
    $sheet.Cells.Item($row, 5).HorizontalAlignment = -4108 # Center
    $sheet.Cells.Item($row, 12).HorizontalAlignment = -4108 # Center
    
    # Hyperlink blue & underline
    $sheet.Cells.Item($row, 12).Font.Color = 16737794 # Blue
    $sheet.Cells.Item($row, 12).Font.Underline = 2

    # Zebra stripes
    if ($idx % 2 -eq 1) {
        $rowRange.Interior.Color = 16579320 # Slate-50
    }
}

# 5. Borders & Auto-filter
$totalRows = $startRow + $pages.Count - 1
$tableRange = $sheet.Range("A3:L$totalRows")
$tableRange.Borders.LineStyle = 1 # xlContinuous
$tableRange.Borders.Weight = 2    # xlThin
$tableRange.Borders.Color = 14540253 # Slate-300

# Auto-fit columns with safety margins
$sheet.Columns.Item(1).ColumnWidth = 6   # 序號
$sheet.Columns.Item(2).ColumnWidth = 14  # 冊別
$sheet.Columns.Item(3).ColumnWidth = 14  # 單元
$sheet.Columns.Item(4).ColumnWidth = 32  # 意境標語
$sheet.Columns.Item(5).ColumnWidth = 18  # 類型
$sheet.Columns.Item(6).ColumnWidth = 26  # 名稱
$sheet.Columns.Item(7).ColumnWidth = 20  # 歌手
$sheet.Columns.Item(8).ColumnWidth = 24  # 作詞作曲
$sheet.Columns.Item(9).ColumnWidth = 38  # 教學亮點
$sheet.Columns.Item(10).ColumnWidth = 25 # 本地路徑
$sheet.Columns.Item(11).ColumnWidth = 46 # 線上網址
$sheet.Columns.Item(12).ColumnWidth = 15 # 超連結

# Enable AutoFilter on header row
$sheet.Range("A3:L3").AutoFilter() | Out-Null

# Freeze panes at A4
$sheet.Range("A4").Select() | Out-Null
$excel.ActiveWindow.FreezePanes = $true

# Save & Clean up
$workbook.SaveAs($excelPath, 51) # 51 = xlOpenXMLWorkbook (.xlsx)
$workbook.Close($true)
$excel.Quit()

[System.Runtime.Interopservices.Marshal]::ReleaseComObject($sheet) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($workbook) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

Write-Host "SUCCESS: Generated Excel file at $excelPath"
