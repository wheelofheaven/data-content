+++
title = "圖書館:希伯來聖經現以九種語言呈現"
description = "截至 2026 年 6 月 7 日,Wheel of Heaven 圖書館中每一本希伯來聖經書卷皆已配備九種語言的文本——英語 ASV 版加上八種匯入的公有領域譯本。"
date = 2026-06-07
template = "news-page.html"

[extra]
event_date = 2026-06-07
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "圖書館現以九種語言收錄每一本希伯來聖經書卷:英語(ASV 1901)加上八種匯入的公有領域譯本,涵蓋德語、西班牙語、法語、日語、韓語、俄語、簡體中文與繁體中文。每節經文皆以讀者所在的站點語言、與作為基準的英語讀本並列呈現,而所匯入之譯本版本、年份與授權,逐書記錄於目錄之中。各語言所選版本之依據,已記載於文件站上的方法論頁面。"
canon_links = [
    { title = "希伯來聖經", path = "/wiki/hebrew-bible/" },
    { title = "創世記", path = "/wiki/genesis/" },
    { title = "耶洛因", path = "/wiki/elohim/" },
    { title = "多姆聖經譯本", path = "/wiki/dhorme-bible-translation/" }
]
sources = [
    { title = "匯入譯本:各語言來源計畫", url = "https://docs.wheelofheaven.world/contributing/content/imported-translations/", outlet = "Wheel of Heaven docs", date = "2026-06-07" },
    { title = "data-library 目錄與章節檔案", url = "https://github.com/wheelofheaven/data-library", outlet = "Wheel of Heaven data-library", date = "2026-06-07" }
]
+++

## 此次上線的內容

截至 2026 年 6 月 7 日,Wheel of Heaven 圖書館已以九種語言收錄完整的希伯來聖經——自《創世記》至《西番雅書》,共三十六卷。每一章皆將英語 ASV 1901 基準版,與德語、西班牙語、法語、日語、韓語、俄語、簡體中文及繁體中文之公有領域匯入版本並列呈現。讀者以九種站點語言中之任一種瀏覽圖書館時,皆可直接以其閱讀語言檢閱文本,無須繞道英語。

所匯入之版本皆已具名、附年份、並採開放授權。目錄亦逐語言記載收錄涵蓋範圍:凡因馬索拉文本傳統與武加大或東正教教會斯拉夫(Synodal)傳統之分節方式不同,而導致某節無法對齊之處,英語 ASV 即作為備援保留。

| 語言 | 版本 | 年份 | 授權 |
|---|---|---|---|
| 英語 | American Standard Version (ASV) | 1901 | 公有領域 |
| 德語 | Elberfelder | 1905 | 公有領域 |
| 西班牙語 | Reina-Valera | 1909 | 公有領域 |
| 法語 | Crampon(《約伯記》、《撒母耳記》存世部分採公有領域 Dhorme) | 1923 | 公有領域 |
| 日語 | 口語訳(Kougo-yaku) | 1955 | 公有領域(著作人格權保留) |
| 韓語 | Korean Revised Version (KRV) | 1961 | 公有領域 |
| 俄語 | Synodal | 1876 | 公有領域 |
| 簡體中文 | Chinese Union Version(和合本) | 1919 | 公有領域 |
| 繁體中文 | Chinese Union Version(和合本) | 1919 | 公有領域 |

每一書卷之出處資訊——譯本名稱、年份、授權、來源網址、擷取日期——皆已記錄於每筆條目於 `data-library/catalog.json` 中之 `translations.{lang}` 區塊。

## 為何採用直譯本

上述每一個匯入版本,依其翻譯理論而言,皆屬於 **形式對等** 譯本——有時被寬鬆地稱為「直譯本」。所選版本皆位於各自傳統中 *較為一致對應* 的一側:Elberfelder 素以近代德語聖經中最逐字對譯而著稱;Reina-Valera、Crampon、Synodal、KRV 與和合本,在各自語言之中,亦皆屬同一形式對等血脈。口語訳是將古典 文語訳 譯為現代日常日語的版本——依該傳統之標準,仍屬形式對等;其立場上有意與後來成為日本天主教與新教共通標準的動態對等 新共同訳(1987)劃清界線。

此選擇是經過思量的,而非懷舊之舉。形式對等譯本嘗試保留源文本的 **詞彙與句法輪廓**——只要目標語言允許,即以一個目標詞對應一個希伯來詞;一個希伯來子句對應一個目標子句;同一節經文中之同一個詞,在整部語料庫中盡可能採同一個譯法。動態對等譯本則反其道而行——它嘗試保留源文本對讀者的 *效果*,而這意味著它經常會將源文本的選擇壓縮、改寫、並抹平為慣用的目標語言。

對一個以收錄八種譯本作為比較之核心理由的圖書館而言——*各個傳統如何處理神之名的相關段落?如何處理〈創世記〉1:1?如何處理〈詩篇〉82?如何處理 Elohim 的複數形?*——形式對等是唯一能保留此一問題的語體。一旦某個譯本決定將 `יהוה` 譯為「the LORD」,因為這在英語中讀來較順,或譯為「主」,因為這在日語中讀來較順,語料庫所欲追蹤之詞彙抉擇便已消失。讀者所見的,是譯者的整飾,而非譯者的解讀。

同樣的邏輯亦適用於 Elohim 此一指稱本身。Elberfelder 在希伯來文加以區分之處,保留可見的「Jehova」/「Elohim」之別;Crampon 以相同的紀律寫出「Yahweh」與「Élohim」;Synodal 則保留「Господь」/「Бог」之配對,使其得以對應到底下的源文本。動態對等譯本則會在同一節經文中,給讀者一個未加區別的 *神*——閱讀起來較容易,但比較性的論證已無物可比。

## 為何這對圖書館而言是恰當的形態

圖書館一向將希伯來聖經視為本計畫所閱讀的有效源文本,而非作為目的地的譯本。英語 ASV 是本計畫主要受眾的閱讀介面;但其下的希伯來文,才是語料庫真正所處理的對象。直至今日尚付諸闕如的,是讓非英語讀者得以在不必繞行英語的情況下,乾淨地檢閱圖書館之路徑。

各語言版本之選擇遵循語料庫之來源層級紀律。每一個匯入譯本,皆為十九或二十世紀的考據版或近考據版——年代夠久,足以進入公有領域;年代夠新,足以在語文學上嚴肅。凡語料庫所偏好之讀本需要使用仍在著作權保護期內的現代版本者,本計畫或採用該版本中之公有領域子集,或明確標註其缺漏。最清楚的案例是法語:多姆 Pléiade 聖經——亦即雷爾於 1973 年接觸時所據之版本——其法國著作權保護期延續至約 2071 年。圖書館以 Crampon 1923 為基準版,並於多姆早期公有領域之《約伯記》(1929)與《撒母耳記》(1910)存世之三卷處,以多姆取代 Crampon。各語言之完整選擇理由——為何採 Elberfelder 而非 Luther、為何採 Crampon 而非 Darby、為何採 口語訳 而非 新共同訳、為何採 1961 年 KRV 而非更嚴格的 1938 年版——均載於文件站 [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)。

本語料庫將希伯來聖經視為一個分層之文本,其 Elohim 之指稱在原文之中具有操作性。現代譯本是下游的詮釋抉擇,而某一譯本所作的詮釋抉擇,會在特定經節之中顯露出來——〈創世記〉1:1、〈詩篇〉82、〈出埃及記〉3:14,以及通篇之神之名相關段落。將八種匯入譯本與 ASV 並列呈現,使此可見性成為尋常之事:欲比較 Elberfelder、Crampon、Synodal 與和合本如何處理某一具爭議經節的讀者,如今無須離開圖書館頁面即可進行此項比較。

## 此事件在更長計畫中的位置

匯入譯本流程僅是圖書館宗旨的其中一半。另一半是 [Wheel of Heaven 翻譯計畫](https://docs.wheelofheaven.world/contributing/content/source-text-translation/),目前正逐章推進《創世記》——一份在本計畫自身之術語紀律下、由希伯來文重新產出的英語讀本,每一章背後皆有 譯者—編者—審校 之流程支持。匯入譯本所負責的是 **廣度**(每一書卷、八種語言、公有領域版本,今日全部上線);而 Wheel of Heaven 翻譯則提供 **深度**(一個傳統、一次一卷、語文學上有所辯護、目前仍在進行中)。

兩條流程皆寫入每章節檔案上同一個 `paragraphs[].i18n[lang]` 欄位,這意味著圖書館模板會透過同一套介面渲染兩者。當 Wheel of Heaven 翻譯的《創世記》達到首個穩定釋出時,它將與這些匯入讀本並列,作為本計畫對其長期構築之比較地景所貢獻之自有讀本。

## 何處可以見到此次成果

- 圖書館索引:[/library/](/library/) ——每一本希伯來聖經書卷之可用語言矩陣現已列出九種語言
- 範例章節:[/library/genesis/](/library/genesis/)(或以您的閱讀語言:`/de/library/genesis/`、`/ja/library/genesis/`、……)
- 每卷之目錄與出處:[GitHub 上之 `data-library/catalog.json`](https://github.com/wheelofheaven/data-library/blob/main/catalog.json)
- 方法論與各語言之來源計畫理由:[docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)

## 已知待辦事項

三項。法語 Dhorme 之《撒母耳記上》、《撒母耳記下》與《約伯記》之佔位內容,仍待一次乾淨的 OCR 處理——Internet Archive 上底層之 djvu 掃描,將希伯來原文之考據資料與註釋過於密集地交錯排列,難以以程式方式擷取。《俄巴底亞書》章節檔案存在一個結構性缺漏(全書二十一節中,僅有一節已於段落層級拆分),而目錄目前誤報為已完整收錄。德語 Elberfelder 之《歷代志上》來源網站(bibel-online.net)在第 13、17、18、22 與 28 章存在已知之內容重複瑕疵,目錄已於 `_meta.notes` 中註明,但合併流程尚未於下游加以過濾。以上三項皆不影響匯入文本之可讀性;均已列入下一輪處理之追蹤項目。

---

*— 2026 年 6 月 7 日撰於 Wheel of Heaven 編輯室。*
