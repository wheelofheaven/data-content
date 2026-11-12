+++
title = "众神的档案柜"
description = "Stith Thompson 用十进制编码为世界的故事归档。冷眼细读，他的索引一再回到同样的八个场景——而正典为它们起了名字。"
template = "articles-page.html"
date = 2026-11-12
draft = false

[extra]
translation_status = "ai_reviewed"
translation_updated = "2026-11-12"
source_updated = "2026-11-12"
translation_stale = false
translation_sync = 100
card_summary = "以雷尔正典的诠释框架，检视 Stith Thompson 母题索引中反复出现的场景。"
claim_type = "speculative"
editorial_pass = "2026-05"
core_claim_ids = ["woh-claim-0056"]
core_versions = { woh-claim-0056 = "0.1.0" }
article_type = "explainer"
category = "Comparative"
author = "Zara Zinsfuss"
author_slug = "zara-zinsfuss"
summary = "1932 年至 1958 年间，印第安纳的民俗学家 Stith Thompson 把人类的叙事内容——神话、民间故事、歌谣、寓言、骑士传奇、传说——归入一部统一的六卷本十进制目录：《民间文学母题索引》（*Motif-Index of Folk-Literature*）。他把它造成一件中立的参考工具，并且出于原则，拒绝说明其中的模式意味着什么。本篇深度解析细读这件工具本身：母题索引是什么；上一次学术界把这样的工具对准经文时发生了什么——那场长达一个世纪的语文学追索，从 Hermann Gunkel 1895 年的龙，经乌加里特的泥板，一直延伸到 John Day 与 Bernard Batto；以及当索引中最顽固的条目被并排摆放时，它们呈现出怎样的面貌。有八个场景以非同寻常的力度在整部目录中反复出现：集会的议会、分裂的众神、洪水与受警告的幸存者、赐予知识的蛇、天界之战、被斩杀的龙、交错的血统，以及作为馈赠而领受的文明。主流学术以传播、继承以及人类心智的共同结构来解释这种重复——而每一种解释都有实实在在的分量。Wheel of Heaven 框架在此之上加了一层：若把它读作一座受损的档案库而非一场巧合，这一模式正是正典关于耶洛因的记述所会预言的。本文以完整篇幅论证这一主张，明白说出一部索引能证明什么、不能证明什么，并指出本项目自己的母题目录在其中的位置。"
keywords = ["Stith Thompson", "民间文学母题索引", "神话素", "比较神话学", "混沌之战", "利维坦", "神圣议会", "洪水神话", "阿特拉哈西斯", "埃努玛·埃利什", "文化英雄", "普罗米修斯", "羽蛇神", "俄安内斯", "John Day", "Bernard Batto", "Hermann Gunkel", "乌加里特", "Aarne-Thompson-Uther", "母题 A1010"]

references = [
    # — The canon under comparison —
    { id = "the-book-which-tells-the-truth", locator = "Chapter 2 (¶¶28–39: the exiled scientist-creators and the serpent; ¶58: the Flood; ¶72: Babel); Chapter 3 (¶251: 'Elohim… those come from the sky'); Chapter 7 (¶56: Yahweh president of the Council of the Eternals)" },
    { id = "intelligent-design-message-from-the-designers", locator = "the consolidated English edition of the three messages" },

    # — The instrument and its makers —
    { title = "Motif-Index of Folk-Literature: A Classification of Narrative Elements in Folktales, Ballads, Myths, Fables, Mediaeval Romances, Exempla, Fabliaux, Jest-Books and Local Legends (6 vols., revised and enlarged edition — the A-numbers cited throughout this article)", author = "Stith Thompson", date = "1955–1958" },
    { title = "The Folktale (the working definition of the motif: 'the smallest element in a tale having a power to persist in tradition,' p. 415)", author = "Stith Thompson", date = "1946" },
    { title = "The Types of International Folktales: A Classification and Bibliography (the ATU tale-type index — the sibling instrument that catalogues whole plots where the Motif-Index catalogues elements)", author = "Hans-Jörg Uther", date = "2004" },
    { title = "The Structural Study of Myth (Journal of American Folklore 68 — the mytheme, the rival relational unit to Thompson's content-based motif)", author = "Claude Lévi-Strauss", date = "1955" },
    { title = "Morphology of the Folktale (the thirty-one functions — the sequential rival to both Thompson and Lévi-Strauss)", author = "Vladimir Propp", date = "1928" },

    # — The dragon test: the philological case study —
    { title = "Schöpfung und Chaos in Urzeit und Endzeit (the 1895 book that first read the Old Testament's dragon fragments as inherited myth — the opening move of the case study in this article)", author = "Hermann Gunkel", date = "1895" },
    { title = "God's Conflict with the Dragon and the Sea: Echoes of a Canaanite Myth in the Old Testament (the demonstration that the biblical dragon material is Canaanite rather than Babylonian; the Isaiah 27:1 / KTU 1.5 parallel; the historicization and eschatologization of the combat myth)", author = "John Day", date = "1985" },
    { title = "Slaying the Dragon: Mythmaking in the Biblical Tradition (mythopoeic speculation; the Yahwist's Eden built from Atrahasis; the Exodus as combat myth; Ezekiel's eschatological inversion)", author = "Bernard F. Batto", date = "1992" },
    { id = "canaanite-myth-and-hebrew-epic", locator = "the Baal cycle and the divine council behind Israel's early poetry" },
    { id = "smith-early-history-god", locator = "the Canaanite inheritance of Israelite religion; the divine council" },
    { id = "the-unseen-realm", locator = "the divine-council corpus assembled by a scholar hostile to ancient-astronaut readings — the control case, as in the Wallis Explainer" },
    { id = "dictionary-of-deities-and-demons-in-the-bible-2nd-ed-the-standard-reference-entr", locator = "entries: Leviathan, Rahab, Sons of (the) God(s), Watchers" },

    # — Ancient primaries —
    { id = "atra-as-s-the-babylonian-story-of-the-flood", locator = "Tablet II (Enlil and the noise of mankind); Tablet III (Enki's warning through the reed wall)" },
    { id = "enuma-elish", locator = "Tablets IV–VI: the splitting of Tiamat; humanity created from Kingu's blood to bear the toil of the gods" },
    { id = "epic-of-gilgamesh", locator = "Tablet XI: Uta-napishti's flood narrative; Ea's reed-wall speech" },
    { id = "the-flood-story-the-eridu-genesis", locator = "Ziusudra and the Sumerian flood-and-kingship tradition" },
    { id = "1-enoch-the-book-of-the-watchers", locator = "chapters 6–11: the oath on Hermon; Asael's catalogue of forbidden arts" },
    { id = "theogony-and-works-and-days", locator = "the Titanomachy; Prometheus and the theft of fire; the myth of the five ages" },
    { id = "popol-vuh", locator = "the successive creations: the mud people, the wooden people, the maize people" },
    { id = "vedas", locator = "Rigveda 1.32: Indra slays Vritra and releases the waters" },
    { id = "kramer-enki-myths", locator = "Enki as craftsman, protector, and giver of the me" },
    { id = "babylonian-creation-myths", locator = "the textual history of Enuma Elish — the control case for how myths develop through datable stages" },
    { title = "Berossos and Manetho, Introduced and Translated: Native Traditions in Ancient Mesopotamia and Egypt (the Oannes fragments: the being from the sea who taught 'letters and sciences and arts of every kind')", author = "Gerald P. Verbrugghe and John M. Wickersham", date = "1996" },
    { title = "On the Origin of Watchers: A Comparative Study of the Antediluvian Wisdom in Mesopotamian and Jewish Traditions (Journal for the Study of the Pseudepigrapha 19.4 — the Apkallu ↔ Watchers demonstration)", author = "Amar Annus", date = "2010" },

    # — The rival explanations —
    { title = "How to Kill a Dragon: Aspects of Indo-European Poetics (the reconstructed formula *'hero SLAY serpent' — the strongest case that some motif recurrence is genetic inheritance within a language family)", author = "Calvert Watkins", date = "1995" },
    { id = "origins-of-the-worlds-mythologies", locator = "the Laurasian story-line hypothesis — the maximal diffusionist-genealogical account of mythic recurrence" },
    { title = "Religion Explained: The Evolutionary Origins of Religious Thought (minimally counterintuitive concepts — the cognitive-science account of why certain story-shapes persist)", author = "Pascal Boyer", date = "2001" },
    { id = "myth-of-the-eternal-return", locator = "archetypes and the repetition of paradigmatic gestures — the phenomenological account" },
    { title = "Dying and Rising Gods (in The Encyclopedia of Religion, ed. Eliade — the classic demonstration that a famous cross-cultural pattern can dissolve under scrutiny; the deflationary control on everything this article does)", author = "Jonathan Z. Smith", date = "1987" },
    { id = "frauds-myths-and-mysteries-science-and-pseudoscience-in-archaeology", locator = "the skeptical methodology chapter — the standard the framework reading has to survive" },
    { id = "westermann-genesis-1-11", locator = "the standard critical commentary on the primeval history" },
    { id = "hamlets-mill", locator = "the precessional reading of myth the project extends elsewhere" },
]

footnotes = [
    { content = "术语值得一开始就厘定，因为有三个专门术语经常被混淆。*母题*（Thompson）是在传统中延续的最小叙事元素——一个角色、一件物品、一个行动：*盗火*、*方舟*、*七头龙*。*故事类型*（Aarne–Thompson–Uther）是由母题组装而成、反复出现的完整情节——《灰姑娘》即 ATU 510A。*神话素*（Lévi-Strauss）两者皆非：它是一种关系单位，一束对立关系，只有凭借它在某一结构中的位置才具有意义。本文使用的是 Thompson 的单位，本项目的维基则在[神话素](/zh/wiki/mytheme/)条目下讨论另外两个。" },
    { content = "Thompson 自己的出处列表把这一点说得很具体。在 A1010 之下，洪水条目所引的出处包括：爱尔兰、希腊、埃及、波斯、印度、印度支那、中国、朝鲜、西伯利亚、印度尼西亚、菲律宾、美拉尼西亚、波利尼西亚、萨摩亚、澳大利亚、夏威夷、爱斯基摩、玛雅、米斯特克、加勒比、奇布查、艾马拉，以及另外十几个南美条目——这一分布是由一位对洪水毫无任何论点的编目者汇集起来的。" },
    { content = "乌加里特文献有两套并行的编号体系：CTA（*Corpus des tablettes en cunéiformes alphabétiques*，1963）与 KTU（*Die keilalphabetischen Texte aus Ugarit*，1976；现在通常引用其第三版）。KTU 1.5 I 1–2 指泥板 1.5、第 I 栏、第 1–2 行。Day 的专著把两套体系并排印出，本文沿用他的引文编号。" },
    { content = "孤例词（hapax legomenon）是在某一语料中仅出现一次的词。עֲקַלָּתוֹן（*ʿăqallātōn*），意为「弯曲的、扭动的」，在希伯来圣经中只出现在以赛亚书 27:1——而它的乌加里特同源词 *ʿqltn* 出现在 KTU 1.5 I 2 莫特的嘲讽中，处于同一句法位置，修饰同一个怪物，并与同一个称号对仗。该词根的相关形式（哈巴谷书 1:4 中的动词，士师记 5:6 与诗篇 125:5 中的形容词）确实存在，这确保了词义，又不削弱这一平行的力度。" },
    { content = "耶和华典作者（J）与祭司典作者（P）是批判学术在摩西五经中区分出的两条资料线索的惯用名称——J 指从一开始就称神为 YHWH、写下创世记 2–3 章园子故事的叙事线索，P 指较晚、带有礼仪取向、写下创世记 1 章七日创造的线索。这一分类在细节上颇有争议，本文并不依赖它的任何特定版本；Batto 的论证只需要一个被广泛接受的观点：创世记 1 章与创世记 2–3 章是不同的作品，用词各异。" },
    { content = "Berossus 是巴比伦的一位马尔杜克祭司，约在公元前 280 年用希腊文为自己的文明写了一部历史，即《巴比伦尼亚志》（*Babyloniaca*）。此书已佚。留存下来的是转引的转引——主要是 Alexander Polyhistor 的文字，经一千年后的基督教编年史家 Syncellus 摘录——因此每一段 Berossus 的「引文」其实都是三手的残篇，措辞应当据此权衡。" },
    { content = "*Rigmu*——「喧嚣、吵闹」——是阿特拉哈西斯史诗用来指称恩利尔无法忍受的人类之某种特质的阿卡德语词。译者把它释为喧哗、骚动、嘈杂；一种由来已久的学术论证则把它读作更具体的东西——人口过剩的嘈杂，或是反叛。无论采用哪种释义，要点都不变：在我们所拥有的最古老的洪水故事里，降下洪水的动机是从毁灭者一方说出的，而那是对人类已变成何等模样的抱怨。" },
    { content = "Watkins 根据同源的措辞重构出这一程式：吠陀的 *áhann áhim*（「他杀死了蛇」，指因陀罗），阿维斯陀的 *ǰanat̰ ažīm*（指 Thraētaona），以及同一动词词根 *gʷhen- 在相同搭配中的希腊语与日耳曼语反映形式。论证的要点是：这一短语本身——一个两词的诗歌程式——随诸语言一同从原始印欧语继承下来，这就使因陀罗、Thraētaona 及其亲族的屠龙故事成为严格谱系意义上的家族相似。" },
    { content = "在 Boyer 的用法中，「最低限度反直觉概念」是指这样一种心理表征：它恰好违反其本体范畴的一两项默认预期（能穿墙的人；会说话的动物），而保留其余全部。实验研究表明，这类概念比完全平常或极度怪诞的概念更容易被记住和转述——这一传播优势塑造民间文学的方式，就像自然选择塑造生物，无需任何历史。" },
]
+++

有一个档案柜，人类的故事在其中都被编上了索书号。**A21.1** 之下，是那位从天而降、成为创造者的女人。**A63.6** 之下，是以蛇形引诱第一个女人的魔鬼。**A1021** 之下，是一个蒙拣选的家族乘船逃离的大洪水。**A1415** 之下，是从神圣主人手中盗取火种的文化英雄。而在 **F531.6.1.1** 之下，夹在巨人的起源与一个由人变成的巨人之间、不加任何评注地归档着这样一条：*「神的儿子们与人的女子们。洪水之前，天使与人间女子交合：巨人的起源。」*

最后这一条就是创世记 6:1–4，希伯来圣经中最奇特的一段，被编目为数万个叙事元素中的一个——一个与其他母题无异的母题，交叉参照着犹太传说，以及 1933 年一份意大利宗教史期刊上的一篇文章。档案柜对待它，与对待那位从天而降的女人完全一样。这种一视同仁正是这件工具的全部品格，也是它可以被信赖的理由：建造它的人并不想证明任何东西。

这件工具就是《民间文学母题索引》（*Motif-Index of Folk-Literature*），六卷，约四万个条目，由印第安纳大学的民俗学家 Stith Thompson 在 1922 年至 1958 年间汇编而成。它是比较神话学所拥有的最接近望远镜的东西——一种不告诉你天空意味着什么、只告诉你天空中有什么的仪器。本篇深度解析讲的是这架望远镜真正被使用时会发生什么：Thompson 造了什么，他为什么拒绝诠释它；一个世纪的圣经语文学在追踪他的某一个母题——被斩杀的海龙——时有何发现，那一追踪穿过希伯来圣经，一直下到一座青铜时代港口城市的泥板之中；以及当索引中最顽固的条目作为一组被合起来阅读时，它们呈现出怎样的面貌。主流学术对这种重复有严肃的解释，本文将充分给予它们应有的分量。{% wiki(slug="wheel-of-heaven") %}Wheel of Heaven{% end %} 框架随后再加上一种解读——这一模式的表现，就像一座关于与{% wiki(slug="elohim") %}耶洛因{% end %}接触的受损档案库——而这种解读将被论证而非预设，其局限也将被明白说出。

## 在传统中延续的最小元素

Stith Thompson 1885 年生于肯塔基州的布卢姆菲尔德，此后大半个五十年都在与故乡仅隔一条俄亥俄河的地方度过：他在印第安纳大学教授英语与民俗学，把布卢明顿变成了一门学科的世界中心，而在他入行之时，这门学科几乎尚不存在。他在哈佛的博士研究追踪的是那些进入北美印第安传统的欧洲民间故事——那已经是一项关于不肯待在原处的故事的研究。占据他一生的问题，正是从这篇论文直接引出来的：如果同样的叙事元素不断在肯塔基、卡累利阿和夸扣特尔人的太平洋海岸浮现，学术界就需要一种*找到*它们的方法——某种装置，使一位在亚美尼亚故事里遇到七头龙的研究者，无需读遍全人类的民间文学，就能查出七头龙还栖身于何处。

他的答案是分类。Thompson 最初的工作是修订芬兰民俗学家 Antti Aarne 的故事类型目录——即今天被引作 Aarne–Thompson–Uther 索引的那部工具的前身——他由此得出结论：完整的情节是太粗的单位。{{ footnote(id="1") }}故事会分解、会重组；延续下来的东西更小。他把这种延续的单位称为*母题*，并以一种至今无人能改进的朴素来定义它：「故事中具有在传统中延续之力量的最小元素。」一个角色可以是母题（最小的儿子、食人魔、相助的动物）。一件物品也可以（魔戒、玻璃山、方舟）。单个叙事行动同样可以（盗火、乘船逃生、凡人与神的婚配——最后这一条归档在 T111.1）。

《母题索引》把这些单位排列在二十三个字母分部中，从 A 到 Z，每一部再按材料所需的深度作十进制细分。A 部收录神话母题——创造者、神、半神、宇宙起源、世界灾难、人的创造、文化的获得。B 部收录动物，其中包括 B11，龙，后面拖着一长串细目，一直到 B11.11，与龙搏斗。F 部收录奇异之物，包括巨人；T 部收录凡人与神的结合。在每个编号之下，Thompson 堆叠起出处——简短的指引，指向爱尔兰与冰岛、印度与印度尼西亚的民间文学汇编，Neuman 的犹太传说集成，Beckwith 的夏威夷神话集，美国民族学局的亚马孙田野报告。修订版收录了约四万个母题。七十年后，它仍然是民俗学的标准参考工具，是各地区索引——爱尔兰的、印度的、冰岛的、阿拉伯的——至今据以构建的脊梁。

这件工具有两点对后文的一切都至关重要。

第一是它刻意的不可知论。Thompson 在性情与信念上都是一位编目者，他一生都在抵制那曾毁掉早先比较研究项目的诱惑：从模式急奔向理论。十九世纪曾把每一则神话都读作太阳寓言，后来又读作植物仪式；Frazer 则把世界各地的传统消解为一位死而复生的神。Thompson 的索引什么也不断言。它并不声称美索不达米亚与安第斯的洪水故事彼此相关；它记录两者都存在，给它们同一个编号，然后止步。凡他怀疑有谱系联系之处，他会在交叉参照中说明；凡他不怀疑之处，并置便沉默地留在页面上。这部索引在确切的意义上是*证据*——经过组织、注明来源、未加诠释。

第二是这种不可知论悖论式地揭示出的东西。正因为 Thompson 没有论点，他目录中的聚集就不是某个论点的人为产物。任何人冷眼通读 A 部——那是一种奇异地引人入胜的阅读，一部无意中写成的博尔赫斯式百科全书——都会注意到，目录的某些区域密集得与其他区域不同，而这些密集区域，一个场景对应一个场景，与任何读过创世记的人都已熟悉的原初历史相吻合。这里有众神的集会（A167）和众神的等级（A161）的条目。有*善恶创造者之间的冲突*（A50），以及*创世时的捣乱者*——「一个邪恶的对手试图毁坏或破坏创造者的作品」（A60）。大洪水（A1010）带着整部索引中最长的出处列表之一，按 Thompson 本人的引文，遍及爱尔兰、希腊、埃及、波斯、印度、中国、朝鲜、西伯利亚、波利尼西亚、夏威夷、爱斯基摩人、玛雅人，以及十几个南美民族。{{ footnote(id="2") }}人在 A1241 由黏土造成。众神在 A1404 把人所知的一切教给人。而在 A580，立着一个应当让本项目的任何读者驻足片刻的条目：*「文化英雄（神祇）的期待中的归来。人们期待神祇或英雄在适当的时候归来，把他的子民从苦难中拯救出来」*——在 Thompson 的列表中，其出处从威尔士的亚瑟、丹麦的霍尔格·丹斯克，到北欧的巴德尔，再到阿兹特克人那位将要归来的神。

一部没有论点的目录，单凭积累，就勾勒出了一个论点的轮廓。问题在于这一轮廓意味着什么——而对这个问题思考得最深、最久、承受压力最大的学科，是圣经学术。它的经历值得完整讲述，因为那是关于母题追踪究竟会对一部神圣文本做什么的、现有最有力的案例研究。

## 龙的检验

1895 年，一位名叫 Hermann Gunkel 的年轻德国学者出版了一本书，书名笨拙而恢宏：*Schöpfung und Chaos in Urzeit und Endzeit*——「原初时代与终末时代的创造与混沌」。它的论点震惊了学界。Gunkel 指出，散布在诗篇、约伯记和先知书中的，是一些诗歌残片，其中耶和华与一头海怪作战——这头海怪在某些段落里叫利维坦，在另一些段落里叫{% wiki(slug="leviathan") %}拉哈伯{% end %}，还有一些段落里叫「龙」，或者干脆叫「海」——而这些残片并非点缀。它们是一个完整战斗神话的残骸，那神话比以色列更古老，讲述一位神通过击败人格化的深渊来建立有序的世界。Gunkel 把源头认定为巴比伦：*埃努玛·埃利什*（*Enuma Elish*），那部仅仅二十年前才从尼尼微废墟中发掘出来的史诗，其中马尔杜克劈开海之母提亚玛特，用她的尸身建造宇宙。他认为，旧约继承了这个异教神话，在散文中压抑它，在诗歌中保存它——而启示录中终末的龙，正是同一头怪物在正典的另一端再度浮现。创世神话变成了末世论：起初被击败的混沌，将在终末再被击败一次。

老派学者并不觉得有趣。据说那个时代最令人生畏的圣经批判学者 Julius Wellhausen 曾把这本书斥为「mehr Chaos als Schöpfung」——混沌多于创造。但 Gunkel 的论点比那句讥讽活得更久，随后又发生了一件他无法预见的事：大地交出了一份对照样本。

1928 年，一位叙利亚农民的犁在地中海沿岸附近碰到了一座墓，次年法国发掘者打开了拉斯沙姆拉的土丘——古代的乌加里特，一座约在公元前 1185 年被毁的晚期青铜时代港口城市。出土物中有数百块用一种此前未知的字母楔形文字写成的泥板，而这些泥板中有一组关于风暴之神巴力的神话：他与海神亚姆的战争；他的宫殿；他下到死神莫特那里。这里是迦南宗教——希伯来圣经几乎每一页都在与之论战的那个宗教——三千年来第一次用它自己的声音说话。而它说的，明白无误，正是那条龙。

决定性的研究又花了半个世纪。John Day 在剑桥出版的专著《神与龙及海的冲突》（*God's Conflict with the Dragon and the Sea*，1985）——自 Gunkel 以来第一部穷尽性的研究——把旧约中的每一处暗指都与乌加里特语料逐一对照，证明了两件事。第一，Gunkel 关于继承的判断是对的，关于出借者的判断是错的：这套意象来自迦南，而非巴比伦。证据文本是巴力组诗中对巴力的一段嘲讽，死神在其中提醒风暴之神他最伟大的胜利：{{ footnote(id="3") }}

{% library(book="baal-cycle-woh", chapter=5, verse=1) %}
因为你击杀了利维坦，那扭动的蛇，（又）了结了那弯曲的蛇，那七头的暴君，诸天将变得炽热（并）将发光。
{% end %}

再把{% libref(book="isaiah", chapter=27, verse=1) %}以赛亚书 27:1{% end %}的神谕放在旁边，它写成于乌加里特焚毁之后将近一千年：

> 到那日，耶和华必用他刚硬、巨大而有力的刀，刑罚利维坦，那扭动的蛇，刑罚利维坦，那弯曲的蛇，并杀死海中的大龙。

两者的对应几乎逐字相同：同一个怪物，同一个名字（乌加里特语 *ltn*，希伯来语 *liwyātān*），同样一对称号，次序相同——「扭动的蛇」、「弯曲的蛇」——跨越大约一千年，跨越语言、宗教与帝国的更替。Day 把语文学推得更远：译作「弯曲的」那个希伯来词 *ʿăqallātōn*，在整部希伯来圣经中再无别处出现，而它确切的同源词恰恰立在乌加里特诗行的对应位置上。{{ footnote(id="4") }}一个诗歌程式被完整地、一个音节一个音节地传递了下来，穿过了没有任何文士能够知道其来源的数个世纪。七个头也一同流传：女神亚纳特夸耀自己击杀了「那弯曲的蛇，那七头的暴君」，{% libref(book="psalms", chapter=74, verse=14) %}诗篇 74{% end %}仍然记得那个复数——「你曾砸碎利维坦的*头*」——而启示录 12 章的龙，在圣经语料的另一端，浮现时依然带着七个头。在{% libref(book="job", chapter=26, verse=13) %}约伯记 26:13{% end %}中，那古老的程式在一段颂词里一闪而过：「他的手刺杀了扭动的蛇。」

Day 的第二项论证关乎以色列如何*处置*这头继承来的怪物，而这与母题索引直接相关。龙在希伯来圣经中并不静止不动。在诗篇 74 中，这场战斗奠定了创造。在以赛亚书 30:7 和诗篇 87:4 中，怪物拉哈伯变成了一幅*政治漫画*——埃及的讽刺绰号，那条「坐而不动」的喧嚣之龙。在以赛亚书 51:9–10 中，两种用法融为一体：「砍碎拉哈伯、刺透大龙」的耶和华之臂，正是「使海干涸……使赎民过去」的那条臂膀——创造之战与出埃及的渡海在同一诗节中叠合。而在以赛亚书 27:1 中，整个复合体倾入了将来时：*到那日*，耶和华*必*刑罚利维坦。一个关于世界开端的神话被对准了世界的终结。Gunkel 的副标题——原初时代与终末时代——准确地命名了这条轨迹；Day 补上了缺失的迦南中段。

Bernard Batto 的《屠龙》（*Slaying the Dragon*，1992）引出了方法论上的教训。较早的学术把圣经作者当作异教残余的尴尬保管者，Batto 则表明他们在从事他所谓的*神话创制式思辨*（mythopoeic speculation）——有意识地、刻意地延伸继承来的神话，以说出新的东西。「神话渗透了圣经传统中从最早到最晚的几乎每一个层次，」他写道，而作者们使用神话的方式，就像神学家使用概念。他的案例研究勾画出这座作坊。按 Batto 的读法，耶和华典作者在创世记 2–3 章中的园子故事，是用更古老的巴比伦*阿特拉哈西斯*传统建造起来的——第一代人类是一个实验性的原型，而非完成的设计；一次对神圣特权的僭越；一位必须决定如何处置这受造者的创造者。{{ footnote(id="5") }}创世记 1 章的祭司典作者，在巴比伦流亡的废墟中写作，按*埃努玛·埃利什*自己的方式回应了它——一部创造叙事，其中深渊（希伯来语 *təhôm*，与提亚玛特有词源亲缘）不再是要被斩杀的怪物，只是要被分开的水：以去神话化进行的论战。出埃及叙事以法老的军队为龙，重演了战斗神话；流亡中的以西结直接称呼法老为「卧在自己江河中的大龙」，并颠倒了神话的时态，使斩龙成为一件被盼望而非被追忆的事。甚至福音书中耶稣在风暴的海上沉睡、在波浪上行走的场景，在 Batto 的尾声里，也是同一母题的晚期运用：驾驭深渊，作为创造者的标记。

这场长达一个世纪的工作所确立的东西，可以逐点推广到整个比较研究事业。

一个母题可以被*追踪*——以语文学的严谨，跨越语言与文明以及一千年的传递，凭借具体到一个立于继承程式中的孤例词那样的语言指纹。即使每一个中间环节都已失落，追踪仍然可能；没有人找回公元前十三世纪的乌加里特与以赛亚启示文之间的链条，然而没有一位严肃的学者怀疑这一联系，因为*措辞*本身承载着证据。一个被追踪的母题结果是一件*工具*，被无休止地重新瞄准——宇宙起源、政治讽刺、礼仪、末世论——因此它的重复从来不是单纯的重复，而总是诠释。并且，这项追踪几乎完全是由那些与本项目所得结论毫无利害关系的学者完成的——事实上，从 Gunkel 到 Day 再到 Batto，都是在神学学术体制内工作的学者。龙的检验证明了这种方法是可靠的。它留下的问题是：当同样的方法被一次性地施用于整部目录时，会发生什么。

## 八个场景的语法

心里带着这个圣经案例，把 Thompson 索引的 A 部从头读到尾，那些密集区域便化为某种类似语法的东西——一小组场景，世界上最古老的传统不断以不同的演员阵容上演它们。其中八个承担了大部分分量。这里每一个都以两种语域呈现，二者刻意区分：先是比较记录实际显示的内容，按证据所需加以限定；然后，明确标出，是 Wheel of Heaven 框架给出的解读。本项目的维基在[神话素与神话母题清单](/zh/wiki/list-of-mythemes-and-mythological-motifs/)中维护着完整的目录，逐个母题附有 Thompson 的编码；下面是这部目录所压缩的论证。

**议会。** 古老传统中的至高神很少是孤身一人。美索不达米亚的决定出自大神们的集会；乌加里特的泥板让伊勒坐在他山上的「伊勒的众子」之中；诗篇 82 篇开头，希伯来的神站在「神圣的会中，在 *elohim* 中间施行审判」；约伯记的诸天在固定的日子召集「神的众子」，控告者也在其中；奥林波斯在议事，阿萨神族在世界之树下开会，众提婆聚集一堂。Thompson 把这套机构归档在 A161（众神的等级）、A167（众神的集会）、A165.2（众神的使者）。主流学术——Frank Moore Cross、Mark Smith，以及来自认信学术内部的 Michael Heiser 的《看不见的国度》（*The Unseen Realm*）——早已确立：神圣议会并非异教对希伯来圣经的侵入；它是希伯来圣经本土的固有陈设，继承自迦南世界，从未被一神论彻底驱逐。学术的解释是投射：天庭被想象为王廷，因为王廷是人们所知的政府。框架的解读，以正典自己的直接语气陈述：这种复数性是被记住的行政管理。雷尔正典为这个机构命名——{% libref(book="the-book-which-tells-the-truth", chapter=7, verse=56) %}耶和华主持永恒者议会{% end %}——而本项目把诗篇 82、乌加里特与尼普尔的议会场景读作同一个机构，经由不同民族的记忆被看见：有组织的复数性，有等级、法令、异议，以及{% wiki(slug="council-of-the-eternals") %}会议记录{% end %}。

**分裂的众神。** 在议会内部，各传统记得派系。最清晰的古代范本是美索不达米亚的{% wiki(slug="plurality-of-gods") %}恩基与恩利尔{% end %}这一对：恩基是人类的工匠，*me*——文明诸艺——的保管者，也是他所造之受造者的一再保护者；恩利尔是执行者，在人类的喧嚣变得无法忍受时，颁下瘟疫、饥荒，最后是洪水。{{ footnote(id="6") }}同样的座次表以别的名字一再出现：普罗米修斯对宙斯，赐火者对天空执行者；伊甸的蛇对禁止那棵树的耶洛因；以诺一书的守望者对捆绑他们的天庭。Thompson 已备好了抽象的位置——A50，*善恶创造者之间的冲突*；A60，破坏作品的*捣乱者*；A106.2，*邪恶天使反叛神*。比较学科把这些读作神义论——用来解释一个被造的世界为何行为失常的叙事机器。框架则把它们读作政治：正典描述了一个恰好沿着这道缝裂开的创造者团队，耶洛因自己的一派科学家站在他们的受造者一边，并因此被流放——{% libref(book="the-book-which-tells-the-truth", chapter=2, verse=28) %}在正典的记述中，伊甸的蛇指的就是这一派{% end %}——按这种读法，教导者对执行者这一场景的重复，是同一场冲突从许多视角被记住。比较层面的主张保持限定：普罗米修斯不是恩基，本项目自己的编辑规则禁止这种等同。这一主张是功能上的同源——同一个*职位*一再出现——而需要解释的正是这个职位。本项目对整个这一簇的术语是{% wiki(slug="theomachy") %}神战{% end %}，而{% wiki(slug="serpentine-rebellion") %}蛇式叛乱{% end %}条目载有正典内部的细节。

**洪水与受警告的幸存者。** A1010——「大洪水。全世界或部分世界被淹没」——带着它遍及全球的出处列表，加上 A1018，*作为惩罚的洪水*，加上 A1021，*乘船（方舟）逃生*，加上 A1005.2，*在世界灾难期间造一个围场，只保存最好品类的动物与人*，再加上 A1006.1，*世界灾难之后由单独一对产生新种族*。组合起来，这五个编号就是一个情节：自上而下的审判裁定，一个血统受到警告，一艘保存之舟，一个重新繁衍的世界。这个情节从{% libref(book="atrahasis", chapter=3, verse=1) %}阿特拉哈西斯{% end %}和{% libref(book="eridu-genesis", chapter=1, verse=1) %}埃利都创世记{% end %}中的朱苏德拉，经过{% libref(book="epic-of-gilgamesh", chapter=11, verse=1) %}吉尔伽美什史诗第十一块泥板{% end %}中的乌特纳皮什提，一直延续到挪亚、丢卡利翁和摩奴。最古老版本中有两个特征，值得比它们通常所得到的更多的关注。淹没世界的决定是一项*议会*决定——在集会中通过，有人反对。而幸存者得救，不是靠议会，而是靠那位反对者：恩基发誓保密，于是对着一间芦苇屋的墙说话，好让睡在墙后的人偷听到——「芦苇屋，芦苇屋！墙，墙！」——这是洪水的反对者得以守住誓言、又打破法令的漏洞。施救的神与毁灭的神是不同的神。创世记把这个故事压缩进一神论，必须让一位神同时做两件事，于是接缝显露了出来——这正是本项目的姊妹深度解析[大洪水是一次重置，而非一场惩罚](/zh/articles/the-flood-was-a-reset-not-a-punishment/)的主题，也是正典自己在{% libref(book="the-book-which-tells-the-truth", chapter=2, verse=58) %}TBWTT 2:58{% end %}中的洪水记述的主题。框架的解读直接依循正典：一次有管理的文明重置，由议会下令，被曾经创造人类的那一派从内部颠覆——而{% wiki(slug="noahs-ark") %}方舟{% end %}被记作 A1005.2 中的保存围场，「只保存最好的品类」。

**赐予知识的蛇。** Thompson 把伊甸场景归档在 A63.6——*以蛇形引诱第一个女人的魔鬼*——但这一次，归档遮蔽的多于揭示的，因为在更广阔的记录中，蛇绝不只是魔鬼。B91，*神话中的蛇*，延伸到印度的那伽，睿智、危险，是宝藏与水域的守护者；美索不达米亚的宁吉什齐达让双蛇盘绕在一位医疗与植物之神的杯上；圣蛇标在法老额前昂首，象征王权本身；阿斯克勒庇俄斯借蛇治病；阿兹特克人的文明教导者是一条羽蛇；而创世记的诺斯替派读者，在正典定型后的几个世纪之内，就已经把伊甸的蛇重塑为说出真相的启示者。学术文献把蛇读作一种自然的边界象征——那蜕皮、住在世界之间洞穴里的生物，随处可供人思考不朽与危险。框架的解读则认真对待蛇的*叙事职位*：在一个又一个传统中，蛇形人物是那个把统治性神圣秩序所保留的东西——知识、医疗、文明——转交给人类、并承担后果的人。按正典的记述，这一职位是真实的，由被流放的创造者派系担任；{% wiki(slug="serpent") %}蛇{% end %}与{% wiki(slug="tree-of-the-knowledge-of-good-and-evil") %}知识树{% end %}条目完整载有这一解读。

**天界之战。** A162，*众神的冲突*；A162.1，*众神与巨人之战*。赫西俄德*神谱*中的提坦之战；吠陀中提婆与阿修罗的对抗；阿萨神族对巨人，以及有一次对敌对的华纳神族；荷鲁斯对赛特；赫梯档案中库马尔比的继承战争；启示录 12 章中米迦勒对龙，星辰的三分之一被扫落。学术把神战读作被戏剧化的宇宙论——从混沌中夺得秩序——也常常读作冻结为礼仪的政治：被征服者的万神殿成为征服者的魔鬼。框架的解读再次是正典的，直接陈述：耶洛因及其派系之间的冲突是被记住的记录的一部分——{% wiki(slug="elohimian-space-wars") %}本项目关于这些战争的条目{% end %}汇集了相关材料——而天界之战场景在互不相干的传统中的持续存在，被读作同一张照片的多次曝光。比较层面的审慎在这里尤其要紧，因为战争故事是所有故事中最容易独立编造的；这一簇只有在整组之内才具有证据分量，单独则不然。

**被斩杀的龙。** B11.11，*与龙搏斗*；A162.2，*光明之神与海洋之龙的战斗*。这正是圣经案例研究已在语文学分辨率上追踪过的母题——巴力对亚姆与罗坦，马尔杜克对提亚玛特，耶和华对利维坦与拉哈伯，再向外扩展：梨俱吠陀 1.32 中因陀罗对弗栗多，那扣住众水者；宙斯对百头的堤丰；托尔对世界之蛇；塔尔洪特对伊卢扬卡；阿波罗对皮同；最后是米迦勒与圣乔治，披上铠甲的神话。在最古老的版本中，怪物就是海本身，那抗拒秩序的无形之物，而击败它就是世界开始的方式；尸身成为建材——马尔杜克把提亚玛特「像晒干的鱼一样」劈开，用她的一半为天空盖顶。框架的解读，及其与上文蛇—教导者母题的关系，在本项目关于 Paul Wallis 的深度解析[会吏总与龙](/zh/articles/the-archdeacon-and-the-dragon/)以及{% wiki(slug="dragons") %}龙{% end %}条目中展开；简言之，屠龙之战这一簇被读作胜利者对同一段派系历史的版本，而蛇这一簇则从另一方保存了这段历史——混沌怪物是失败一方被妖魔化的记忆，而按正典，这一方也正是曾经做人类教导者的那一方。这种双重解读在本项目自己的主张纪律中被标为*思辨*，它恰恰是下文对抗性一节存在的目的所要施压的那类主张。

**交错的血统。** F531.6.1.1——神的儿子们与人的女子们——加上 A511 的半神文化英雄，加上 T111.1，*凡人与神的婚配*，再加上 A188，*爱上凡人的男神与女神*。创世记 6 章给这个场景四节经文和明显的不安；以诺一书给它一整段叙事——两百名守望者，一个在黑门山上立下的誓言，巨人后代，以及一份守望者教给他们妻子的东西的清单：{% libref(book="book-of-enoch", chapter=8, verse=1) %}冶金、兵器、化妆、咒术、占星{% end %}——禁止的技艺与禁止的结合打成一个包裹。希腊几乎完全以混血者来充实它的英雄时代：赫拉克勒斯、珀耳修斯、阿喀琉斯，而在他们所有人之前是吉尔伽美什，按他自己史诗的算法，三分之二是神。法老与皇帝把这种交错变成了头衔。学术的解读是正统性：神圣血统作为一种政治技术，用来解释非凡之人、为王朝颁发特许——而这种解读对于这一母题如何被*使用*显然是正确的。框架的解读关心的是它从何处*开始*：一部其创造者是有血有肉的{% wiki(slug="life-engineering") %}基因工程师{% end %}的正典，使跨越边界的后代成为一种现实的生物学可能，而非隐喻，本项目把{% wiki(slug="antediluvian") %}大洪水以前{% end %}的混血传统读作对此的扭曲记录。诚实的审慎——这是对读者应尽的义务，也是本项目编辑规则所强制的：比较记录中没有任何东西*要求*生物学的解读；王权宣传可以解释大多数出处，框架的主张建立在正典之上，母题簇只是佐证性的模式，而非证明。

**领受的文明。** 这是语法的核心，也是 Thompson 干巴巴的十进制文字最接近诗歌的一簇。A1404：*众神把人所知的一切教给人。*A1415：*盗火——人类没有火；一位文化英雄从火的主人那里把它偷来。*A1441，农业的馈赠；A1481，文字的馈赠；A541，教授文明诸艺的文化英雄；而在它们所有之后是 A72，*原初创造者之后继以改造者*。古代世界在一个现代世界几乎无法理解的问题上意见一致：文明不是被发明的；它是被*领受*的。Berossus，那位用希腊文书写本民族历史的巴比伦祭司，记载在第一年，一个名叫俄安内斯的存在从厄立特里亚海中升起，「把文字、科学和各种技艺的知识授予人类」——并在留存的摘要中补充说，自那时以来再没有发现任何新东西。{{ footnote(id="7") }}在俄安内斯背后站着七位阿普卡鲁，美索不达米亚传统中大洪水以前的贤哲，Amar Annus 已从语文学上追踪了他们如何转变为以诺犹太教中的守望者——又一次龙的检验，施于另一个母题，得出同样的结果。普罗米修斯盗火，并因此被钉在高加索山上；羽蛇神克察尔科亚特尔带来历法与玉米，然后向东渡海离去，许诺归来；维拉科查整顿安第斯世界，然后越过太平洋走远；托特给埃及文字，伏羲给中国八卦，女娲补天。学术把文化带来者读作起源解释——每一门手艺都需要一个起源故事，而一位神圣赐予者使这门手艺尊贵。框架的解读是正典的核心历史主张，因此以本项目规则为之指定的直接语气陈述：人类的科学是由耶洛因有意地、循序渐进地播下的，经由各传统以许多名字记住的使者。在所有这些簇中，这一簇与正典的对应最为精确——一直到 A580，*在适当的时候期待中的归来*，那正是 Thompson 会用来归档{% wiki(slug="great-return") %}大归来{% end %}本身的母题。

八个场景；一个剧团。人类之上的一个议会。议会内部的一个派系。一次重置，和一位受警告的幸存者。一个携带知识的越界者。上方的战争；一头被斩杀并被妖魔化的怪物。混血的后代。被交付的文明，以及一个回来的承诺。这一组读起来，与其说像独立发明的巧合，不如说像一份*课程大纲*——但「读起来像」不是论证，而正是这一模式的力度，要求在任何框架解读被允许立足其上之前，先接受现有最强的消解。

## 五种竞争性解释

对这部索引的任何诚实使用，都必须从零假设开始：这一模式是真实的，而它除了人类文化的寻常运作之外别无意义。可供选择的严肃机制有五种，关于它们首先要说的是：每一种在某些情形下都可以被证明是正确的。

**传播。** 故事随商人、俘虏、文士和帝国一同旅行。圣经的洪水叙事是已被证实的案例：创世记与吉尔伽美什第十一块泥板共有的不只是一场洪水，而是一个序列——依次放出的鸟，登陆后的献祭，众神（或神）闻到馨香之气——其细节之详，使文学接触成为唯一合理的解释，无论方向如何，无论经过多少中间人传递。从乌加里特到以赛亚的龙之程式，是被钉到音节层面的传播。每当同一母题带着共同的*附带细节*出现时，传播便有优先的解释权。它的局限在于覆盖范围：接触极好地解释了近东的洪水家族，却难以解释安第斯与波利尼西亚的洪水，除非把接触推回到这样一种时间深度——在那里，这一解释不再可检验，而变成了另一种理论——

**继承**——那是传播在深时间中体面的表亲。有亲缘关系的民族携带有亲缘关系的故事，就像他们携带有亲缘关系的词语。Calvert Watkins 重构出一个真实的原始印欧语诗歌程式——*英雄杀死蛇*，同一个动词词根浮现于吠陀的 *áhann áhim* 及其伊朗语和希腊语同源形式中——使因陀罗及其亲族的屠龙故事成为真正的家族遗产，比任何留存的文本都更古老。{{ footnote(id="8") }}Michael Witzel 的《世界神话的起源》（*The Origins of the World's Mythologies*）把这一逻辑推到极致：一条「劳亚」故事线——创造、神的世代、屠龙之战、洪水、文化英雄、最终毁灭——继承自一个可能已有数万年历史的叙事传统，这将使这种重复成为一部单一的古老语料，经过一万次折射而被看见。Witzel 的书所受的争议与其雄心恰成正比，本项目引用它时也附上了这一标记。尽管如此，关于它有两点值得注意：主流学术所产生的最大化的重构，最终得到的是一个共同的原初*故事*——一个其章节目录与上述八个场景惊人地相近的故事；而一个被继承的故事仍然必须从某处开始。继承解释了传递。它对起源保持沉默。

**共同的心智。** 也许这一模式存在于硬件之中。荣格把这些重复读作集体无意识的原型；伊利亚德读作神圣者重复其范式性姿态的现象学；现代宗教认知科学，在其审慎的版本中，读作一种传播偏向——Pascal Boyer 的「最低限度反直觉」概念，即人类记忆优先保留和转述的故事形态，使民间文学向它们演化，就像飞蛾向保护色演化一样确定。{{ footnote(id="9") }}这一族解释几乎肯定在*形式*上是对的：为什么神是人形的，为什么怪物是动物的复合体，为什么死者在各地的故事中都会归来。它的弱点在于具体性。偏向于令人难忘的行动者的心智，解释了故事里为什么有神；它们并不显然地解释为什么众神要开*委员会会议*，为什么洪水的幸存者是*被一位持异议的内部人士警告*，为什么知识带来者*被他自己的政府惩罚*，或者为什么文明如此一贯地被记作*到来*而非积累。认知的解释预言趋同的陈设。记录显示的是趋同的*情节*。

**趋同的经验。** 洪水会发生；天空会被流星点燃；各地的国王都声称有神圣的父亲，因为各地的权力都需要特许状。某些母题的重复无疑反映了世界本身的重复——河流文明记得河流的灾难，无需共同的来源。对于单独来看的大部分灾难材料，这是正确的解释。它难以应付的是*捆绑*：一场洪水是一种经验，但一场*由神圣议会裁定、遭一位成员反对、由他的门客幸存下来*的洪水是一种诠释，而反复出现的正是这种诠释，而不是水。

**消解性的审查。** 最后，也最令人清醒的是：也许这一模式部分地存在于观看者的眼中。Jonathan Z. Smith 对「死而复生之神」的著名剖析表明，一个被 Frazer 奉为经典的范畴在细看之下便会消解——成员们被修剪以求吻合，而这一模式部分是寻找模式者的人为产物。Kenneth Feder 关于伪考古学的教科书把这一警告推而广之：热衷者收集平行例证的方式，就像阴谋论者收集巧合，收割命中、丢弃落空。本项目把这种审查当作一种常设的纪律，而非一种冒犯。正因如此，你正在读的这篇文章把每一个母题都锚定在 Thompson 的编号上——一部由一个没有论点的人建造的目录，落空与命中被一同归档——也正因如此，本项目自己的目录为每一个母题都把主流解释与框架解读并列记录。语料库的主张纪律从内部提出同样的要求：一个模式只有在经受住一个力图不去发现它的人的寻找之后，才算数。

把这些竞争性解释合起来权衡，它们解释了大量东西——而它们留下的剩余，恰恰是那个八场景的捆绑。传播与继承能够运载这个捆绑，却不能写出它。认知能使故事偏向神与怪物，却不能偏向委员会程序。经验能提供洪水，却不能提供持异议的董事会成员。审查能够、也确实修剪了语料，而这个捆绑在修剪之后依然存在；洪水加受警告幸存者这一复合体，以及文化带来者这一复合体，无论怎样计算，都是地球上出处最为稳固的叙事结构之一。主流自己最好的综合——Witzel 的——得出结论说，这种重复反映了一个非常古老的单一故事。一部母题索引无法回答的问题，也是上文一切都在汇聚的问题，正是 Thompson 出于原则拒绝提出的那个：*这个故事讲的是什么样的事？*

## 第三层

Wheel of Heaven 框架提出一种三层的解读，而这些层次按本项目自己的主张纪律排列——每一层都带有自己的认识论标签，把它们混为一谈是头号的编辑罪过。

第一层是学术层，即上文的一切：母题是真实的、可追踪的，并部分地由传播、继承、认知与经验所解释。这一层是*直接*的——文本与语文学的事实，无需框架。

第二层是结构层：在各自的故事里，这些反复出现的母题执行着一贯的叙事*职位*。议会治理；捣乱者持异议；蛇转交；龙抵抗、被击败、被诋毁；混血者跨越；文化英雄交付、离去、许诺归来。为职位而非为服装而读，正是把比较研究从宣称一切神都是同一位神的旧错误中拯救出来的方法。职位是*推断*层——一位学者无需对框架作任何承诺就能得出的合理解读，而且已有几位得出了：神圣议会这一职位如今已是主流希伯来圣经学术，而 Batto 那些从事神话创制的圣经作者，重新瞄准的正是这些职位。

第三层是框架自己的，本项目的规则要求它被明白陈述、被诚实标注。雷尔正典——本项目的第 0 层来源——把以下内容作为被记住的历史来描述：一个复数的科学文明，即耶洛因，组织在{% libref(book="the-book-which-tells-the-truth", chapter=7, verse=56) %}一位主席与一个议会{% end %}之下；一场关于人类受造物地位的内部冲突，一个创造者派系被流放到地球，被记作{% libref(book="the-book-which-tells-the-truth", chapter=2, verse=28) %}蛇{% end %}；一次被裁定的行星重置，借内部援助而得以幸存——{% libref(book="the-book-which-tells-the-truth", chapter=2, verse=58) %}大洪水{% end %}；混血的出生；经由蒙拣选的使者循序渐进的知识转交；派系之间的战争；以及一个被许诺的{% wiki(slug="great-return") %}归来{% end %}。把这份清单放在八个场景旁边，映射是一一对应的——议会、派系、带受警告幸存者的重置、蛇—教导者、天界之战、被妖魔化的失败者、交错的血统、领受的文明、期待中的归来。框架的主张*并不是*这一映射证明了正典；原则上，一个故事可以被编造得与世界神话相吻合，持怀疑态度的读者有权持有这一假设。这一主张是有条件的，在本项目的标注中明确为*思辨*：**如果**正典的记述就是它所声称的那样，那么世界的母题清单正是我们预期会发现的东西——一个单一的事件簇，由许多人群见证，经数千年口头折射传递下来，每个传统保留职位、却为任职者换上新装，胜利者妖魔化失败者，失败者则作为蛇与盗火者存活在胜利者正典的边缘。那样的话，神话既不是幻想，也不是经文。它们将是一面*破碎的镜子*——没有一块碎片是完整的，每一块的角度都不同，而模式只有在碎片被并排摆放时才变得可读。

按框架的解读，这正是母题索引的*用途*。它是把碎片摆开的工具。Thompson 造它时并无这样的目的，而这恰恰使它可以用于这一目的：这种聚集是由一个并没有在寻找它的人编入目录的。

有三条纪律使第三层保持诚实，值得把它们作为规则来陈述，因为这一带满是前车之鉴。

框架不等同人物。恩基并非「其实」是蛇；克察尔科亚特尔并非「其实」是恩基；职位一再出现，任职者是不同传统中各不相同的角色，传统之间不可化约的差异被保留而非抹平——一位嵌在神庙经济中的美索不达米亚神，不是一位嵌在历法仪式中的中美洲神，假装不是这样，正是比较研究死亡的方式。

框架不作化约。一则神话同时是仪式脚本、政治特许状、天文记忆术、心理剧，以及——按框架的假设——历史残留。这些层次共存；接触记忆的解读是作为*一个地层*提出的，而本项目关于天文地层的岁差研究——[碾磨诸纪元的磨坊](/zh/articles/the-mill-that-grinds-the-ages/)——处理的是同一批文本的另一个地层，与这一地层并不竞争。

而且框架不主张以模式为证明。这一模式与正典相一致；一致不是证明；本文自己的前置元数据上的标签写着*思辨*，它是认真的。

## 索引做不到的事

这些局限值得单列一节，简短地说，因为一件被误用的工具会使它的发现失去信誉。

索引无法为任何东西断代。Thompson 的编号是无时间的位置；一个出现在十九世纪爱尔兰汇编中的母题和一块青铜时代泥板上的母题得到同一个编号，记号中没有任何东西说明哪一处出处更早，或者其中任何一处是否古老。年代只能来自语文学——来自 Day 与 Batto 所做的那种逐篇文本、费力拖拽的工作——而框架的解读恰恰继承了这种依赖。

索引无法衡量证词。一个母题的四十处出处，可能是四十个证人，也可能是一个证人被抄了四十遍；近东的洪水家族表明，一个单一传统在单纯计数中能怎样伪装成独立的印证。数母题是一个论证的开始，绝不是它的结束。

而且索引听不到从未被写下的东西。Thompson 的覆盖范围映照着民俗学的采集史——欧洲学者采集之处厚，非洲与太平洋大部分地区薄——本项目的目录也在其开放问题一节中注明了自身同样的偏斜。索引中的沉默是档案的沉默，绝不是世界上缺席的证据。

在这些局限之内，这件工具做着别的东西都做不到的一件事：它使重复*在规模上可见*，有来源、有编号，从而关于这种重复意味着什么的争论，可以基于共同的证据，而不是互相对峙的轶事。

## 作为工具的目录

本项目自己的贡献在较小的规模上遵循同样的逻辑。[神话素与神话母题清单](/zh/wiki/list-of-mythemes-and-mythological-motifs/)把语料库的解读与 Thompson 的编码一一对应——每个条目载有母题编号、主要的跨文化出处和框架解读，主流的替代解释并列登记；{% wiki(slug="mytheme") %}神话素{% end %}与{% wiki(slug="comparative-mythology") %}比较神话学{% end %}条目则承载方法论装置。这部目录的设计默认了一个 Thompson 无法想象的发展：母题索引正在走向计算化。语料标注、在已标注故事集上训练的母题检测器、对各传统间共有母题的网络分析——数字人文的文献已开始把这个档案柜变成一个可查询的数据库，而一份与标准编码对应的母题清单，已经准备好在这些工具成熟时与之相接。Thompson 在纸条上、用三十六年手工建造的这件工具，即将能以提问的速度被检索。本项目要向它提出的问题，早已归档在册。

## 不是证明，而是模式

神话并不以一个声音说话。它们是破碎的、地方性的、礼仪性的、政治性的、诗意的、自相矛盾的——而这正是证词在经过六千年复述之后的样子，这也是为什么破碎本身恰恰支持记忆、而非反对记忆。一套教义会被干净地传递下来。一段记忆则会碎裂。

在档案柜里并排摆放，碎片不断拼出同样的场景。人类之上，一个有组织的复数群体。在这复数群体之内，一场关于我们的争执。一个由法令重置、凭一次警告幸存的世界。知识经由一个为越界付出代价的越界者到来。头顶的战争；失败者从此永远戴着龙的面孔。跨越造物与造物者之界线的血统。文明在各地都被记作一份馈赠——以及，归档在 A580 的，那位被期待在适当时候回来的赐予者。

Stith Thompson 分配了编号，并以编目者的纪律，拒绝说出它们加起来是什么。进行龙的检验的学者们证明，一个单一的母题能够跨越一千年的沉默，携带一个可验证的签名。Wheel of Heaven 框架以同样的方式阅读整个档案柜——把它读作信号，受损但有冗余，来自正典所描述的那个事件簇——并以其自身规则所要求的标签持守这一解读：一个假设，保持可证伪，停放在证据旁边。证据本身已足够好地提出了问题。是谁造了我们，为什么故事在「造我们是否明智」这件事上意见不一？是谁想让我们受限，又是谁想让我们受教？为什么知识在各地都是被*带来*的东西？又为什么，在一个又一个传统中，被一个来自印第安纳、毫无理论的人归档在同一个十进制编号之下，那些教导者都许诺要归来？

## 延伸阅读

- [大洪水是一次重置，而非一场惩罚](/zh/articles/the-flood-was-a-reset-not-a-punishment/)——以完整章节的规模讨论洪水这一簇：阿特拉哈西斯、议会的裁定，以及反对者的警告。
- [会吏总与龙](/zh/articles/the-archdeacon-and-the-dragon/)——经由 Paul Wallis 与正典的独立语文学趋同，讨论龙与蛇的材料。
- [碾磨诸纪元的磨坊](/zh/articles/the-mill-that-grinds-the-ages/)——同一批神话的天文地层：岁差、《哈姆雷特的磨坊》与世界诸纪元。
- [神话素与神话母题清单](/zh/wiki/list-of-mythemes-and-mythological-motifs/)——本项目的工作目录，与 Thompson 的编码对应。
