+++
title = "图书馆：希伯来圣经现支持九种语言阅读"
description = "截至2026年6月7日，Wheel of Heaven 图书馆中的每一卷希伯来圣经均提供九种语言文本——英语 ASV 加上八种导入的公有领域译本。"
date = 2026-06-07
template = "news-page.html"

[extra]
event_date = 2026-06-07
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "图书馆现以九种语言收录全部希伯来圣经书卷：英语（ASV 1901）加上覆盖德语、西班牙语、法语、日语、韩语、俄语、简体中文与繁体中文的八种导入公有领域译本。每节经文在读者站点语言中与英语正典文本并行呈现，每卷书在目录中均记录其导入版本、年份与许可。各语种版本的选定理由在文档站点上有专门的方法论页面说明。"
canon_links = [
    { title = "希伯来圣经", path = "/wiki/hebrew-bible/" },
    { title = "创世记", path = "/wiki/genesis/" },
    { title = "耶洛因", path = "/wiki/elohim/" },
    { title = "多尔姆圣经译本", path = "/wiki/dhorme-bible-translation/" }
]
sources = [
    { title = "导入译本：分语种源头计划", url = "https://docs.wheelofheaven.world/contributing/content/imported-translations/", outlet = "Wheel of Heaven docs", date = "2026-06-07" },
    { title = "data-library 目录与章节文件", url = "https://github.com/wheelofheaven/data-library", outlet = "Wheel of Heaven data-library", date = "2026-06-07" }
]
+++

## 已发布的内容

截至2026年6月7日，Wheel of Heaven 图书馆收录了完整的希伯来圣经——从创世记到西番雅书，共三十六卷——并提供九种语言。每一章都在英语 ASV 1901 基准之外，并列呈现德语、西班牙语、法语、日语、韩语、俄语、简体中文与繁体中文的导入公有领域版本。以九种站点语言中任何一种查阅图书馆的读者，现在都可以直接以其阅读语言看到文本，无需再绕道英语。

导入的版本均标注了名称、年份与公开许可。目录还报告了各语种的覆盖情况：当马所拉传统与武加大或大公会议传统之间的经节编号差异导致某节经文未能对齐时，英语 ASV 仍作为后备保留。

| 语言 | 版本 | 年份 | 许可 |
|---|---|---|---|
| 英语 | American Standard Version (ASV) | 1901 | 公有领域 |
| 德语 | Elberfelder | 1905 | 公有领域 |
| 西班牙语 | Reina-Valera | 1909 | 公有领域 |
| 法语 | Crampon（约伯记、撒母耳记现存部分使用公有领域 Dhorme） | 1923 | 公有领域 |
| 日语 | 口語訳 (Kougo-yaku) | 1955 | 公有领域（保留人格权） |
| 韩语 | Korean Revised Version (KRV) | 1961 | 公有领域 |
| 俄语 | Synodal | 1876 | 公有领域 |
| 简体中文 | Chinese Union Version (和合本) | 1919 | 公有领域 |
| 繁体中文 | Chinese Union Version (和合本) | 1919 | 公有领域 |

每卷书的来源信息——译本名称、年份、许可、源 URL、检索日期——记录在每个条目的 `data-library/catalog.json` 中，置于该书 `translations.{lang}` 区块之下。

## 为何选用直译本

上述所列每个导入版本，按其翻译理论，均为**形式对等**译本——有时也被笼统地称为"直译"。所选版本在各自传统中均位于*一致性*的一端：Elberfelder 是公认的现代以来最逐字逐句的德语圣经；Reina-Valera、Crampon、Synodal、KRV 与 Chinese Union Version 在各自语言中也都属于同一形式对等谱系。口語訳 是古典文語訳 的口语化日语现代化版本——按该传统的标准仍为形式对等，刻意定位为对抗后来成为日本天主教与新教共同标准的动态对等 新共同訳（1987）。

这一选择是经过深思熟虑的，并非怀旧。形式对等译本试图保留来源的**词汇与句法形态**——只要语言允许，一个希伯来词对应一个目标词；一个希伯来分句对应一个目标分句；同一来源经节中的同一词，在整个语料中尽量得到同样的翻译。动态对等译本则反其道而行——它试图保留对读者所产生的*效果*，这意味着它惯常地压缩、改述、并将来源的选择平整化为目标语言的习惯表达。

对于一座以比较为唯一存在理由而托管八种译本的图书馆而言——*每个传统如何处理神圣之名的经文段落？如何处理创世记 1:1？如何处理诗篇 82？如何处理 Elohim 的复数形式？*——形式对等是唯一能保留这个问题的语域。一旦某译本决定将 `יהוה` 译为"the LORD"只因这样更符合英语读感、或译为"主"只因这样更符合日语读感，那么语料想要追踪的词汇选择便已消失。读者所见的是译者的修整，而非译者的解读。

同样的推理也适用于 Elohim 这一指称本身。Elberfelder 在希伯来文区分两词之处保留"Jehova" / "Elohim" 的可见性；Crampon 以同样的严谨写作"Yahweh"与"Élohim"；Synodal 保留与底层来源对应的"Господь" / "Бог"配对。动态对等译本会在同一节经文中只给读者一个未加区分的*神*——读起来更顺，但比较性论证已无对象可比。

## 为何此形态适合图书馆

图书馆始终将希伯来圣经视为本项目所读取的运作性源文，而非作为目标译本。英语 ASV 是项目主要读者群的阅读界面；底层希伯来文才是语料实际所接触的对象。今天之前所缺失的，是一条让非英语读者无需以英语为强制中介即可查阅图书馆的整洁路径。

各语种版本的选定遵循语料的源头分级原则。每个导入译本都是十九或二十世纪的批判性或近批判性版本——足够久远以进入公有领域，又足够晚近以保有语文学严肃性。当语料偏好的读法需要仍在版权保护下的现代版本时，项目要么使用该版本的公有领域子集，要么明确标注其缺口。最清楚的例子是法语：Dhorme 七星文库圣经——也就是 Raël 在1973年接触期间所参考的版本——在法国版权法下大约要到2071年才进入公有领域。图书馆以 Crampon 1923 为基准，并以 Dhorme 较早期的公有领域约伯记（1929）与撒母耳记（1910）在这三卷书可用之处替换 Crampon。各语种完整的选定推理——为何选 Elberfelder 而非路德版，为何选 Crampon 而非 Darby，为何选 口語訳 而非 新共同訳，为何选1961年 KRV 而非更严格的1938年版——见文档站点 [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)。

语料将希伯来圣经读作一部分层文本，其 Elohim 指称在原文语言中具有运作性。现代译本是下游的诠释性举动，而某译本所作的诠释举动在特定经节中清晰可见——创世记 1:1、诗篇 82、出埃及记 3:14、以及散见全书的神圣之名段落。将八种导入译本与 ASV 并列托管，使这种可见性成为常态：想要比较 Elberfelder、Crampon、Synodal 与 CUV 各自如何处理某节争议经文的读者，现在无需离开图书馆页面便可做到。

## 这在更长远的计划中的位置

导入译本管线是图书馆使命的一半。另一半是[Wheel of Heaven 翻译](https://docs.wheelofheaven.world/contributing/content/source-text-translation/)，目前正逐章推进创世记——一份在项目自身术语表纪律下，从希伯来文产出的新鲜英语读本，每章背后均有翻译者-编辑者-审阅者管线。导入译本提供**广度**（覆盖每卷书、八种语言、公有领域版本，今日发布）；Wheel of Heaven 翻译提供**深度**（一个传统、一次一卷书、语文学上有所辩护，仍在进行中）。

两条管线都灌注到每个章节文件相同的 `paragraphs[].i18n[lang]` 字段中，这意味着图书馆模板通过同一界面来呈现两者。当 Wheel of Heaven 翻译的创世记达到首个稳定版本时，它将作为项目自身对所建构的比较图景的贡献，与这些导入读本并列。

## 何处可见

- 图书馆索引：[/library/](/library/)——每卷希伯来圣经现在其可用性矩阵中列出九种语言
- 章节样例：[/library/genesis/](/library/genesis/)（或以您的阅读语言：`/de/library/genesis/`、`/ja/library/genesis/`……）
- 每卷书的目录与来源信息：[GitHub 上的 `data-library/catalog.json`](https://github.com/wheelofheaven/data-library/blob/main/catalog.json)
- 方法论与分语种源头计划推理：[docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)

## 已知待办事项

三项。法语 Dhorme 在撒母耳记上、撒母耳记下与约伯记的占位文本仍待一次干净的 OCR 处理——互联网档案馆上的底层 djvu 扫描件将希伯来文校勘装置与注释交织得过于密集，无法以程序方式提取。俄巴底亚书章节文件存在脚手架缺口（二十一节经文中只有一节按段落层级拆分），目录目前误报为完整覆盖。1历代志德语 Elberfelder 的源头记录（bibel-online.net）在第13、17、18、22、28章中存在已知的内容重复异常，目录已在 `_meta.notes` 中标注，但合并管线尚未在下游过滤。这三项均不影响导入文本的可读性；全部列入下一轮处理。

---

*——2026年6月7日发自 Wheel of Heaven 编辑部。*
