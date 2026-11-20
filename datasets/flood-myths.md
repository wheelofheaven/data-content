+++
title = "Flood-Myth Concordance"
description = "Compare eleven flood accounts through 88 cited observations, named editions and explicit uncertainty. Read the sources and download the data as CSV or JSON."
template = "dataset-page.html"

[extra]
core_claim_ids = ["woh-claim-0010", "woh-claim-0060"]
core_versions = { woh-claim-0010 = "0.1.0", woh-claim-0060 = "0.1.0" }
claim_type = "inferred"
dataset_name = "Wheel of Heaven Flood-Myth Concordance"
dataset_version = "1.2"
license = "CC0-1.0"
license_url = "https://creativecommons.org/publicdomain/zero/1.0/"
updated = "2026-11-20"
keywords = ["flood myth dataset", "deluge", "comparative mythology data", "Atrahasis", "Gilgamesh", "Genesis flood", "digital humanities", "open data", "CC0 download"]
api_url = "https://api.wheelofheaven.world/v1/datasets/flood-myths.json"

stats = [
    { label = "Accounts", value = "11" },
    { label = "Cited observations", value = "88" },
    { label = "Version", value = "1.2" },
    { label = "License", value = "CC0-1.0" },
]

downloads = [
    { label = "Observations · CSV", url = "/datasets/flood-myths-observations.csv", format = "text/csv", note = "88 observations with evidence states, edition citations and notes." },
    { label = "Complete record · JSON", url = "/datasets/flood-myths.json", format = "application/json", note = "Accounts, observations, source register, relationships and chronology." },
    { label = "Account table · CSV", url = "/datasets/flood-myths.csv", format = "text/csv", note = "One row per account; original columns followed by evidence metadata." },
    { label = "Chronology · CSV", url = "/datasets/flood-myths-chronology.csv", format = "text/csv", note = "Composition, surviving witness and internal dates kept separate." },
]

citation_text = "Zinsfuss, Zara. Wheel of Heaven Flood-Myth Concordance, version 1.2. Wheel of Heaven, 2026. CC0-1.0. https://www.wheelofheaven.world/datasets/flood-myths/"
citation_bibtex = '''@misc{woh-flood-myths,
  title  = {Wheel of Heaven Flood-Myth Concordance},
  author = {Zinsfuss, Zara},
  year   = {2026},
  note   = {Version 1.2; CC0-1.0 public domain},
  url    = {https://www.wheelofheaven.world/datasets/flood-myths/}
}'''
+++

This concordance compares eleven textual accounts of a flood: who survives,
who decides and warns, what causes it, the vessel, any birds released, the
landing place and the aftermath. Each observation names the edition and
passage inspected. Open an account below to follow its sources and see where
the text leaves a question unresolved.

## Reading the evidence

**Attested** means that the selected representation states the feature; it
does not establish that the event happened. **Not stated** means silence
within the inspected passage. **Damaged text** means that gaps obstruct the
question. **Uncertain** preserves a disputed translation or attribution.
These states travel with the downloads. An empty observation value is never
an instruction to count a feature as absent.

A warning is distinct from a decree. A later promise is distinct from an oath
before the flood. The table keeps these differences visible even where a
broad comparison might make the accounts look alike.

## Browse the accounts

The selection includes the Sumerian Flood Story; *Atrahasis*; *Gilgamesh* XI;
*Genesis*; Qur’an 11; Apollodorus; Berossus as preserved through Syncellus;
the *Śatapatha Brāhmaṇa*; *Leyenda de los Soles*; Molina's Andean account;
and Snorri's *Prose Edda*. Each row has a bounded scope. Molina's account
stands separately from Betanzos, and Snorri's quoted verse has not been
counted as another independently inspected witness.

<!-- flood-concordance:start -->
<div data-ai-concordance="flood-myths">
<details class="dataset__account" id="account-sumerian-ziusudra">
<summary><strong>Sumerian</strong> · Sumerian Flood Story, selected surviving lines</summary>
<p><strong>Inspected scope:</strong> Jacobsen/Livius 81′–185′; ETCSL composite gap structure C–E; Kramer 1963 pp. 163–164</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Ziusudra, king and purification priest</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 86′–91′; 175′–185′</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The divine assembly; the order of An and Enlil</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 92′–101′</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Uncertain</em></dt>
<dd data-evidence-state="uncertain">
<p>An unnamed warning voice in the selected lines; Enki is a qualified scholarly identification</p>
<p>Livius names Enki in a heading. Kramer explicitly treats the identification as probable; this supports retaining uncertainty, not converting the heading into a preserved speaker name.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 81′–85′; 92′–101′</a>; <a href="https://isac.uchicago.edu/publications/sumerians-their-history-culture-and-character">The Sumerians: Their History, Culture, and Character — p. 163 (PDF leaf 193)</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>A decision to destroy is reported; its motive is not stated in these surviving lines. The page introduction’s noise explanation is not a translated line.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 81′–101′</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A large boat</p>
<p>Construction instructions fall in a lacuna; their reconstruction is not encoded as attested.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 132′–140′</a>; <a href="https://etcsl.orinst.ox.ac.uk/section1/c174.htm">The Flood story, ETCSL 1.7.4, composite text — gap of approximately 38 lines after C 28, before D 1</a>; <a href="https://isac.uchicago.edu/publications/sumerians-their-history-culture-and-character">The Sumerians: Their History, Culture, and Character — p. 163, missing construction instructions</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Undetermined: damaged text</em></dt>
<dd data-evidence-state="text_damaged">
<p>No release episode survives in the excerpt. Gaps prevent coding absence.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — lacunae before 132′ and 175′</a>; <a href="https://etcsl.orinst.ox.ac.uk/section1/c174.htm">The Flood story, ETCSL 1.7.4, composite text — gaps between C/D and D/E; damaged D 12–17</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Undetermined: damaged text</em></dt>
<dd data-evidence-state="text_damaged">
<p>Dilmun is a subsequent residence; it is not explicitly the boat’s landing place.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 132′–185′ and intervening lacuna</a>; <a href="https://etcsl.orinst.ox.ac.uk/section1/c174.htm">The Flood story, ETCSL 1.7.4, composite text — D 12–17 and gap of approximately 33 lines before E 1</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Sacrifice to Utu; An and Enlil grant enduring life and settle Ziusudra in Dilmun</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Sumerian Flood Story / Eridu Genesis — 137′–145′; 175′–185′</a></small></p></dd>
</dl>
<p><strong>Witness:</strong> CBS10673 (+ CBS10867), approximately 1650 BCE (Penn Museum catalogue). A date for the Nippur tablet, not the composition; the catalogue also describes seventeenth-century BCE script. No claim of earliest witness.</p>
<p><small>Penn Museum collection catalogue, object 97591, consulted 20 November 2026: Date Made; Description; Other Number (https://collections.penn.museum/collections/object/97591)</small></p>
</details>
<details class="dataset__account" id="account-babylonian-atrahasis">
<summary><strong>Babylonian (Akkadian)</strong> · Atra-hasis, Sippar Tablet III with synoptic motivation passages</summary>
<p><strong>Inspected scope:</strong> SEAL III C1 (+) C2, displayed translation i–viii; I 351–363; II A 1–20, E 56–78, G 16–97 and H 1–28</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Atrahasis; his family is brought aboard</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C2 i 11′–24′; C1 ii 40″–52″; vi 5–19</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The great Anunnaki decide together on oath; Enlil is blamed for bringing the flood</p>
<p>The collective decision is recalled after the flood. This does not turn a later blame statement into a separately preserved pre-flood council scene.</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C1 iii 36′–43′; v 41″–45″; vi 5–10</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Enki, addressing the reed wall and instructing Atrahasis</p>
<p>The speaker name at i 15′ is restored; vi 13–15 explicitly identifies Enki with the disclosure.</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C2 i 13′–24′; C1 i 36′–38′; vi 11–19</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Human multiplication and noise provoke successive divine attempts to reduce the population; the sequence escalates to the flood</p>
<p>Narrative sequence summarized across the synoptic edition: the first noise complaint prompts disease, then deprivation of food and water. The explicit flood oath at II G 49q–u comes from Middle Babylonian X-MB. Tablet III retrospectively links the destruction decision to the people’s noise; the causal sequence is not a verbatim single-line explanation.</p>
<p><small><a href="https://seal.huji.ac.il/index.php/node/1515">Atraḫasis I (all periods), SEAL 1515 — I 351–363</a>; <a href="https://seal.huji.ac.il/index.php/node/39732?tid=339">Atraḫasis II (all periods), SEAL 39732 — A 1–20; E 60–78; G 27–49u; H 9–25</a>; <a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C1 iii 36′–43′</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A roofed boat strengthened with bitumen; its door is closed with bitumen</p>
<p>The damaged dimensions are not reconstructed; a reed-worker’s participation does not establish an exclusively reed hull.</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C2 i 22′–26′; C1 i 29′–33′; ii 51″–54″</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Undetermined: damaged text</em></dt>
<dd data-evidence-state="text_damaged">
<p>Birds are loaded aboard, but no test-release scene survives in this witness’s displayed translation. The gap around the flood’s ending prevents an absence claim.</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C1 ii 34″–35″; iv 24′–27′ and following gap; v 1–31″</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Undetermined: damaged text</em></dt>
<dd data-evidence-state="text_damaged">
<p>The transition from storm to sacrifice is substantially missing; no landing location is preserved in the inspected translation.</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C1 iv 24′–27′ and following gap; v 1–31″</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Sacrifice; Enki addresses Nintu, followed by provisions for women who cannot bear, infant deaths and priestly restrictions on childbirth</p>
<p>Enlil calls for Enki and Nintu to confer; Enki’s name is restored in vi 45′. The preceding assignment of Death in vi 47′–49′ is substantially restored, so it is not presented as an unqualified preserved clause.</p>
<p><small><a href="https://seal.huji.ac.il/node/1517?tid=80">Atraḫasis OB III (Sippar), SEAL 1517 — C1 v 30″–35″; vi 41′–51′; vii 1–11</a></small></p></dd>
</dl>
<p><strong>Witness:</strong> Sippar Tablet III, Ammī-ṣadūqa year 12. SEAL identifies Ammī-ṣadūqa year 12 from a partly restored colophon formula. An absolute BCE conversion and a composition date are not inferred from it; the synoptic I–II witnesses have different dates.</p>
<p><small>SEAL edition credited to Nathan Wasserman, 8 September 2020; indexing/commentary Yulia Tulaikova, 1 July 2021. Bibliography identifies Wasserman 2020, pp. 19–37, and Lambert/Millard 1969: C2 viii 26′–31′, colophon (siglum from transliteration) (https://seal.huji.ac.il/node/1517?tid=80)</small></p>
</details>
<details class="dataset__account" id="account-babylonian-utnapishtim">
<summary><strong>Babylonian (Akkadian)</strong> · Epic of Gilgamesh, Standard Babylonian Tablet XI</summary>
<p><strong>Inspected scope:</strong> Kovacs/Livius XI.1–205</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Utnapishtim, with family, craftsmen and other living beings aboard</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.80–86; 198–205</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The great gods; Enlil is subsequently held responsible</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.14–20; 165–175</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Ea, addressing the reed house and wall</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.19–31</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>The decision is stated without its initiating motive. Later blame is not a supplied original cause.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.14–20</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Equal-sided boat with six decks making seven levels, divided into compartments</p>
<p>Replaces seven-decked with the selected translation’s distinction between decks and levels. Bitumen is listed among construction supplies; a specific sealing use is not asserted here.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.28–31; 54–66</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Dove, swallow, raven; the first two return, the raven does not</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.146–155</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Mount Nimuš</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.141–145</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Sacrifice, divine dispute, and godlike life for Utnapishtim and his wife</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Epic of Gilgamesh, Standard Babylonian Tablet XI — XI.156–205</a></small></p></dd>
</dl>
</details>
<details class="dataset__account" id="account-hebrew-noah">
<summary><strong>Hebrew / Biblical</strong> · Genesis 6–9</summary>
<p><strong>Inspected scope:</strong> Genesis 6, 8 and 9, JPS/Mechon-Mamre</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Noah, his wife, his sons and their wives</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0106.htm">Genesis 6 — 6:18</a>; <a href="https://mechon-mamre.org/p/pt/pt0108.htm">Genesis 8 — 8:18</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>YHWH at 6:5–7; Elohim at 6:13,17</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0106.htm">Genesis 6 — 6:5–7,13,17</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Elohim gives Noah instructions</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0106.htm">Genesis 6 — 6:13–22</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Human wickedness, corruption and violence</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0106.htm">Genesis 6 — 6:5–7,11–13</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Ark of gopher wood, pitched inside and out, with three levels</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0106.htm">Genesis 6 — 6:14–16</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A raven; then three sendings of a dove, which finally stays away</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0108.htm">Genesis 8 — 8:6–12</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The mountains of Ararat</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0108.htm">Genesis 8 — 8:4</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Burnt offerings and a covenant with the bow as sign against another destroying flood</p>
<p><small><a href="https://mechon-mamre.org/p/pt/pt0108.htm">Genesis 8 — 8:20–22</a>; <a href="https://mechon-mamre.org/p/pt/pt0109.htm">Genesis 9 — 9:8–17</a></small></p></dd>
</dl>
</details>
<details class="dataset__account" id="account-islamic-nuh">
<summary><strong>Islamic</strong> · Qur’an 11:25–49</summary>
<p><strong>Inspected scope:</strong> Shakir/Livius 11:25–49</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Nuh, the believers and family except those excluded</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:40–43</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Allah</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:33–40</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Allah’s revelation to Nuh</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:36–37</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Rejection of Nuh and injustice</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:25–39</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>An ark built under divine direction</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:37–41</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:25–49</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Al-Judi (al-Gudi in the inspected transcription)</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:44</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Nuh’s son drowns; the water recedes; Nuh descends with peace and blessings</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Qur’an, Surah 11 — 11:42–48</a></small></p></dd>
</dl>
</details>
<details class="dataset__account" id="account-greek-deucalion">
<summary><strong>Greek</strong> · Apollodorus, Library 1.7.2</summary>
<p><strong>Inspected scope:</strong> Frazer 1921, 1.7.2</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Deucalion and Pyrrha; a few others escape to high mountains</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Zeus</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Prometheus advises Deucalion</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Zeus intends to destroy the Bronze Age people; no further motive is given</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A chest stocked with provisions</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Parnassus, after nine days and nights afloat</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Sacrifice to Zeus; at Zeus’s instruction stones thrown by the couple become people</p>
<p>The legacy phrase about a mother’s bones is not in this passage and is removed. Its source has not been established in this audit.</p>
<p><small><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Apollodorus, Library 1.7.2 — 1.7.2</a></small></p></dd>
</dl>
</details>
<details class="dataset__account" id="account-berossus-xisuthros">
<summary><strong>Greco-Babylonian</strong> · Berossus flood fragment preserved in Syncellus</summary>
<p><strong>Inspected scope:</strong> Chronological Excerpts 53–56, Verbrugghe/Wickersham adaptation</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Xisuthrus with family and friends; other passengers survive his disappearance</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 54–56</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>Cronus foretells the event, but is not explicitly said to decree it.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 54–56</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Cronus, in a dream</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 54</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>A coming destruction is predicted; no initiating motive is stated.</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 54–56</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Boat five stades long and two broad</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 54</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Three releases: return; muddy claws; no return</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 54</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A mountain in Armenia; the remains are located in the Gordyenian mountains</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 55</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Sacrifice; Xisuthrus, wife, daughter and pilot join the gods; remaining passengers recover writings at Sippar</p>
<p><small><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Berossus fragment in Syncellus — 55–56</a></small></p></dd>
</dl>
</details>
<details class="dataset__account" id="account-vedic-manu">
<summary><strong>Vedic / Hindu</strong> · Śatapatha Brāhmaṇa, Mādhyandina 1.8.1.1–11</summary>
<p><strong>Inspected scope:</strong> Eggeling 1882; TITUS 1–6 and Sacred Texts 7–11</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Manu alone</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.6</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.1–6</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A fish raised and protected by Manu</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.1–5</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.1–6</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Ship tied to the fish’s horn; the fish instructs Manu to fasten it to a tree</p>
<p>Section 5 narrates attachment to the horn; section 6 gives the tree-fastening instruction without separately narrating its completion.</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.4–6</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.1–6</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A northern mountain; the descent is called Manu’s descent</p>
<p><small><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1 — 1.8.1.5–6</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Offerings produce a woman identified with Ida; through her and ritual Manu generates his race</p>
<p><small><a href="https://sacred-texts.com/book/the-satapatha-brahmana-part-i/story-of-the-flood-of-manu">Śatapatha Brāhmaṇa, Mādhyandina 1.8.1, ritual aftermath — 1.8.1.7–11</a></small></p></dd>
</dl>
</details>
<details class="dataset__account" id="account-aztec-tata-nena">
<summary><strong>Aztec / Nahua</strong> · Leyenda de los Soles, water-sun and Tata/Nene episodes</summary>
<p><strong>Inspected scope:</strong> Velázquez 1992, pp. 119–120</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Tata and Nene</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — p. 120, end of section I</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>The passage describes destruction and warning without a separately stated decree by Tezcatlipoca.</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — pp. 119–120, water-sun episode</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Titlacahuan, subsequently named Tezcatlipoca</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — p. 120, sections I–II</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The water-sun age ends with inundation and the sinking sky; no further motive is stated</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — pp. 119–120</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A hollowed ahuehuetl, closed over the pair</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — p. 120, section I</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — pp. 119–120</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>The water diminishes and the wood stops moving; no place is named.</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — p. 120</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>They cook fish; the smoke provokes the gods; Tezcatlipoca transforms them into dogs</p>
<p><small><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Leyenda de los Soles — p. 120, section II</a></small></p></dd>
</dl>
<p><strong>Internal Date:</strong> 22 May 1558. The text dates its narration; this does not independently date the surviving manuscript or the narrated flood.</p>
<p><small>Primo Feliciano Velázquez, Códice Chimalpopoca, 3rd ed., UNAM, 1992; digital publication 2019: p. 119, opening paragraph (https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf)</small></p>
</details>
<details class="dataset__account" id="account-inca-viracocha">
<summary><strong>Andean / Inca</strong> · Molina, An Account of the Fables and Rites of the Yncas</summary>
<p><strong>Inspected scope:</strong> Markham 1873, pp. 4–5</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>An unnamed man and woman in this account</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — p. 4</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>The Creator acts after the flood; a flood decree is not stated in this passage.</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — pp. 4–5</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — pp. 4–5</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>The nearby account of people turned to stone for disobedience must not be substituted for a stated cause of this flood.</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — pp. 4–5</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>A box</p>
<p>The inspected English says box, without specifying that it was sealed.</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — p. 4</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — pp. 4–5</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Huanaco in the text, identified as Tia-huanacu in Markham’s footnote 3</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — p. 4 and footnote 3</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The Creator forms representatives of nations from clay, gives them life and sends them to their places of emergence</p>
<p>Clay replaces the legacy stone formulation for this witness. Other survival accounts are reported on p. 5.</p>
<p><small><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Cristóbal de Molina, An Account of the Fables and Rites of the Yncas — pp. 4–5</a></small></p></dd>
</dl>
<p><strong>Composition:</strong> Between 1570 and 1584, according to Markham’s introduction. A bounded report of this 1873 editor’s dating argument, not an adjudication of modern scholarship. The legacy 1557–1575 span mixed Molina with Betanzos.</p>
<p><small>Clements R. Markham, Narratives of the Rites and Laws of the Yncas, Hakluyt Society, 1873: Introduction p. vii (PDF leaf 13) (https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up)</small></p>
</details>
<details class="dataset__account" id="account-norse-bergelmir">
<summary><strong>Norse</strong> · Snorri, Gylfaginning VII, including its quoted verse</summary>
<p><strong>Inspected scope:</strong> Brodeur 1916, p. 19</p>
<dl>
<dt><strong>Survivor</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Bergelmir and his wife; the prose also mentions his household</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
<dt><strong>Flood decreed by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>The sons of Borr kill Ymir; a separate decision to send a flood is not narrated.</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
<dt><strong>Warned by</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
<dt><strong>Cause</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>Blood from Ymir after his killing drowns the frost giants</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
<dt><strong>Vessel</strong> · <em>Uncertain</em></dt>
<dd data-evidence-state="uncertain">
<p>Brodeur renders the object as a ship, while his footnote gives mill-bench or mortar</p>
<p>The legacy hollowed-tree-trunk gloss is not supported by the inspected edition. Preserve the translation issue instead of selecting a material.</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19 and footnote 1</a></small></p></dd>
<dt><strong>Birds released</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
<dt><strong>Landing place</strong> · <em>Not stated in the inspected passage</em></dt>
<dd data-evidence-state="not_stated">
<p>No statement of this feature in the inspected scope.</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
<dt><strong>Aftermath</strong> · <em>Attested</em></dt>
<dd data-evidence-state="attested">
<p>The surviving pair become ancestors of the frost giants</p>
<p><small><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Snorri Sturluson, Gylfaginning VII — Gylfaginning VII, p. 19</a></small></p></dd>
</dl>
<p><strong>Witness:</strong> Codex Upsaliensis around 1300; Regius early fourteenth century; Wormianus fourteenth century, as reported by Brodeur. Dates reported by the selected 1916 editor, not a current manuscript census, direct manuscript inspection, or an independent date for the quoted poem.</p>
<p><small>Arthur Gilchrist Brodeur, The Prose Edda, 1916: Introduction p. xv (PDF leaf 25) (https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf)</small></p>
</details>
</div>

### Editions and access

These are the representations used for the observations. Several are adapted excerpts; their limits remain part of each citation.

<details class="dataset__source" id="source-sum-jacobsen-livius">
<summary>Sumerian Flood Story / Eridu Genesis</summary>
<p>Livius adaptation attributed to Thorkild Jacobsen; underlying edition not specified on page</p>
<p><strong>Read:</strong> Displayed translation, lines 81′–185′ and marked lacunae</p>
<p>An adapted excerpt, not manuscript collation. Editorial headings and bracketed reconstructions are not preserved ancient lines. The page introduction supplies a noise motive not present in its displayed text. Oxford ETCSL direct retrieval failed; its edition is not claimed as inspected here.</p>
<p><a href="https://www.livius.org/articles/misc/great-flood/flood2-t/">Open source</a></p>
</details>
<details class="dataset__source" id="source-gil-kovacs-livius">
<summary>Epic of Gilgamesh, Standard Babylonian Tablet XI</summary>
<p>Maureen Gallery Kovacs translation, adapted by Livius via AncientTexts.org</p>
<p><strong>Read:</strong> Tablet XI, displayed lines 1–209</p>
<p>Adapted translation; line labels are those printed on this page. Original-language collation and manuscript dating not performed.</p>
<p><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-gilgamesh/">Open source</a></p>
</details>
<details class="dataset__source" id="source-gen6-jps">
<summary>Genesis 6</summary>
<p>JPS 1917 English alongside Hebrew, Mechon-Mamre</p>
<p><strong>Read:</strong> Chapter 6</p>
<p>Reading of displayed text and English translation; no manuscript or redaction-critical collation.</p>
<p><a href="https://mechon-mamre.org/p/pt/pt0106.htm">Open source</a></p>
</details>
<details class="dataset__source" id="source-gen8-jps">
<summary>Genesis 8</summary>
<p>JPS 1917 English alongside Hebrew, Mechon-Mamre</p>
<p><strong>Read:</strong> Chapter 8</p>
<p>Reading of displayed text and English translation; no manuscript or redaction-critical collation.</p>
<p><a href="https://mechon-mamre.org/p/pt/pt0108.htm">Open source</a></p>
</details>
<details class="dataset__source" id="source-gen9-jps">
<summary>Genesis 9</summary>
<p>JPS 1917 English alongside Hebrew, Mechon-Mamre</p>
<p><strong>Read:</strong> Chapter 9</p>
<p>Reading of displayed text and English translation; no manuscript or redaction-critical collation.</p>
<p><a href="https://mechon-mamre.org/p/pt/pt0109.htm">Open source</a></p>
</details>
<details class="dataset__source" id="source-quran11-shakir">
<summary>Qur’an, Surah 11</summary>
<p>M. H. Shakir translation as reproduced by Livius</p>
<p><strong>Read:</strong> 11:25–49</p>
<p>This revision narrows the row to the inspected passage; it does not claim a census of all Qur’anic flood passages or independent verification of Arabic.</p>
<p><a href="https://www.livius.org/articles/misc/great-flood/flood1-t-quran_a/">Open source</a></p>
</details>
<details class="dataset__source" id="source-apollodorus-frazer">
<summary>Apollodorus, Library 1.7.2</summary>
<p>J. G. Frazer, The Library, 1921; Perseus text reproduced by Alpheios</p>
<p><strong>Read:</strong> 1.7.2, complete displayed Greek and English passage</p>
<p>Observations use Frazer’s English; no fresh Greek translation. Other Deucalion versions are not merged into this witness.</p>
<p><a href="https://alpheios.net/alpheios-texts/Perseus.text.1999.01.0021/book1_card1.7.2.html">Open source</a></p>
</details>
<details class="dataset__source" id="source-berossus-vw-livius">
<summary>Berossus fragment in Syncellus</summary>
<p>G. P. Verbrugghe and J. M. Wickersham translation, adapted by Livius</p>
<p><strong>Read:</strong> Syncellus, Chronological Excerpts 53–56, as labelled on the page</p>
<p>Indirect preservation. Translator/editor identifications of Cronus with Enki are not words of the surviving excerpt. Full transmission history not independently collated.</p>
<p><a href="https://www.livius.org/articles/misc/great-flood/flood3_t-berossus/">Open source</a></p>
</details>
<details class="dataset__source" id="source-satapatha-eggeling-titus">
<summary>Śatapatha Brāhmaṇa, Mādhyandina 1.8.1</summary>
<p>Julius Eggeling, Sacred Books of the East 12, 1882, excerpt on TITUS, Frankfurt</p>
<p><strong>Read:</strong> 1.8.1.1–6</p>
<p>Source translation inspected on the web. The fish is unnamed in this passage; subsequent identifications are not imported.</p>
<p><a href="https://titus.uni-frankfurt.de/didact/idg/indi/sbbeispn.htm">Open source</a></p>
</details>
<details class="dataset__source" id="source-satapatha-eggeling-ritual">
<summary>Śatapatha Brāhmaṇa, Mādhyandina 1.8.1, ritual aftermath</summary>
<p>Julius Eggeling, Sacred Books of the East 12, 1882, transcription at Sacred Texts</p>
<p><strong>Read:</strong> 1.8.1.7–11, printed pp. 218–219 in the displayed transcription</p>
<p>Only the numbered source transcription was used, inspected online. Site-generated summaries are not evidence.</p>
<p><a href="https://sacred-texts.com/book/the-satapatha-brahmana-part-i/story-of-the-flood-of-manu">Open source</a></p>
</details>
<details class="dataset__source" id="source-soles-velazquez">
<summary>Leyenda de los Soles</summary>
<p>Primo Feliciano Velázquez, Códice Chimalpopoca, 3rd ed., UNAM, 1992; digital publication 2019</p>
<p><strong>Read:</strong> Printed pp. 119–120; PDF leaves 2–3; p. 120 visually checked</p>
<p>Spanish translation inspected, not an independent Nahuatl reading. The text’s 1558 date is not automatically the date of the surviving manuscript.</p>
<p><a href="https://historicas.unam.mx/publicaciones/publicadigital/libros/000/000_04_03_LeyendaSoles.pdf">Open source</a></p>
</details>
<details class="dataset__source" id="source-molina-markham">
<summary>Cristóbal de Molina, An Account of the Fables and Rites of the Yncas</summary>
<p>Clements R. Markham, Narratives of the Rites and Laws of the Yncas, Hakluyt Society, 1873</p>
<p><strong>Read:</strong> Printed pp. 4–5; p. 4 (PDF leaf 30) visually checked; Introduction p. vii (PDF leaf 13)</p>
<p>A colonial author’s report in a nineteenth-century English translation. Betanzos has not been inspected and contributes no revised cells.</p>
<p><a href="https://archive.org/details/narrativesofrite00markiala/page/4/mode/2up">Open source</a></p>
</details>
<details class="dataset__source" id="source-edda-brodeur">
<summary>Snorri Sturluson, Gylfaginning VII</summary>
<p>Arthur Gilchrist Brodeur, The Prose Edda, 1916</p>
<p><strong>Read:</strong> Printed p. 19 (PDF leaf 51), text and footnote visually checked; Introduction p. xv (PDF leaf 25)</p>
<p>Snorri’s prose and quoted verse are one inspected witness here. Vafþrúðnismál has not been separately collated. The English ship rendering has a qualifying footnote.</p>
<p><a href="https://upload.wikimedia.org/wikipedia/commons/f/fd/The_Prose_Edda_%281916_translation_by_Arthur_Gilchrist_Brodeur%29.pdf">Open source</a></p>
</details>
<details class="dataset__source" id="source-atra-seal-i">
<summary>Atraḫasis I (all periods), SEAL 1515</summary>
<p>Nathan Wasserman and Michael P. Streck, SEAL edition, translation and commentary, revision 29 December 2024</p>
<p><strong>Read:</strong> Translation I 351–363 and revision history</p>
<p>A synoptic edition combining manuscripts from different periods. Brackets and sigla are significant; not a single continuously preserved Old Babylonian witness.</p>
<p><a href="https://seal.huji.ac.il/index.php/node/1515">Open source</a></p>
</details>
<details class="dataset__source" id="source-atra-seal-ii">
<summary>Atraḫasis II (all periods), SEAL 39732</summary>
<p>SEAL synoptic edition; revision history credits Nathan Wasserman, 10–11 August 2026</p>
<p><strong>Read:</strong> Translation segments A 1–20, E 56–78, G 16–97, H 1–28; commentary H 16–25 and I 7f–i; revision history</p>
<p>Combines Old, Middle and Neo-Assyrian/Babylonian witnesses. G 49q–u is supplied through Middle Babylonian X-MB; do not present it as preserved in the Sippar Tablet II.</p>
<p><a href="https://seal.huji.ac.il/index.php/node/39732?tid=339">Open source</a></p>
</details>
<details class="dataset__source" id="source-atra-seal-iii">
<summary>Atraḫasis OB III (Sippar), SEAL 1517</summary>
<p>SEAL edition credited to Nathan Wasserman, 8 September 2020; indexing/commentary Yulia Tulaikova, 1 July 2021. Bibliography identifies Wasserman 2020, pp. 19–37, and Lambert/Millard 1969</p>
<p><strong>Read:</strong> Displayed translation of C1 (+) C2, columns i–viii, including colophon; catalogue and revision history</p>
<p>Witnesses BM 78942+78971+80385 (+) MAH 16064. Restored names and words are bracketed; substantial passages are missing. The regnal date belongs to this copy, not the composition.</p>
<p><a href="https://seal.huji.ac.il/node/1517?tid=80">Open source</a></p>
</details>
<details class="dataset__source" id="source-sum-etcsl-composite">
<summary>The Flood story, ETCSL 1.7.4, composite text</summary>
<p>Oxford ETCSL, static composite text, revisions through 1999; header reformatted 2001</p>
<p><strong>Read:</strong> Segments A–E, line labels and explicitly marked gaps; bibliography at https://etcsl.orinst.ox.ac.uk/section1/b174.htm</p>
<p>Used to check the edition’s gap structure, not to supply a new English translation. The Oxford English translation could not be retrieved and was not inspected for this review.</p>
<p><a href="https://etcsl.orinst.ox.ac.uk/section1/c174.htm">Open source</a></p>
</details>
<details class="dataset__source" id="source-sum-kramer-1963">
<summary>The Sumerians: Their History, Culture, and Character</summary>
<p>Samuel Noah Kramer, University of Chicago Press, 1963, pp. 163–164; scan hosted by UChicago ISAC</p>
<p><strong>Read:</strong> Flood-story discussion pp. 163–164; printed p. 163 visually checked (PDF leaf 193)</p>
<p>Scholarly synopsis, not a line-by-line critical edition. Used for the expressly tentative identification of the warning deity and the missing construction scene; its 1963 inventory of known tablets is not a current census.</p>
<p><a href="https://isac.uchicago.edu/publications/sumerians-their-history-culture-and-character">Open source</a></p>
</details>
<details class="dataset__source" id="source-sum-penn-cbs10673">
<summary>Flood Tablet / Deluge Tablet, CBS10673</summary>
<p>Penn Museum collection catalogue, object 97591, consulted 20 November 2026</p>
<p><strong>Read:</strong> Object details: period, Date Made, description, joins and CDLI identifier</p>
<p>Museum’s approximate date for a physical witness; not a composition date or earliest-attestation claim. The dating was not independently reassessed palaeographically.</p>
<p><a href="https://collections.penn.museum/collections/object/97591">Open source</a></p>
</details>
<!-- flood-concordance:end -->

## How the comparison was made

{% claim(type="inferred", id="woh-claim-0060") %}Each row registers a textual account against named sources. Related accounts do not become independent evidence because they occupy separate rows, and the number of rows is not an argument for a shared event.{% end %}

The sample was curated around comparable narrative features. It does not
estimate how common those features are among all flood traditions. This
revision checks the eleven existing accounts rather than expanding the
sample. Several sources are translated excerpts or adaptations; the edition
notes above specify what was inspected. These are observations about those
representations, not new translations or a manuscript collation.

Source review covered all 88 observations. The review corrected, among other
things, the number of decks in the selected *Gilgamesh* translation, an
unattributed phrase in the Apollodorus summary, and details previously merged
into the Molina and Snorri rows. The Atrahasis entries now cite SEAL's editions
and distinguish a synopsis assembled from several manuscripts from a single
surviving tablet.

### Dates and textual relationships

Composition, the surviving copy, a date stated within a text and the date of
a narrated event answer different questions. The chronology download keeps
these fields separate. Five positive date entries have bounded source
support; most fields remain unresolved or unassigned. No historical date is
assigned to a flood, and the inherited composition estimates are not treated
as verified chronology.

The JSON records the inherited Mesopotamian–Biblical textual-stream grouping
and marks it as not independently reassessed by this audit. It also records
Berossus's indirect preservation and the verse quoted within Snorri's prose.
An unrecorded relationship does not establish independence.

## How Wheel of Heaven reads it

{% claim(type="framework", id="woh-claim-0010") %}Within the Raëlian canon, the Flood is a deliberate reset of the antediluvian project, with genetic stock preserved aboard a craft and the human remnant re-established afterwards.{% end %}

The comparative question is how far the accounts support a shared decision
procedure: assembly, oath, dissent, warning and preservation. The table lets
readers inspect individual features and divergences. It does not demonstrate
that the complete procedure occurs in every row or establish a shared
historical event. Literary dependence is the strongest alternative explanation
for similarities within the Mesopotamian–Biblical stream. Judgment theology,
local floods and the possibility of imposing the canonical reading on older
texts remain relevant alternatives.

The interpretation is developed in [The Flood Was a Reset, Not a Punishment](/articles/the-flood-was-a-reset-not-a-punishment/)
and the [Great Flood](/wiki/great-flood/) entry. The [Myth Index](/datasets/myth-index/)
places this comparison alongside other narrative families.

## Downloads and version history

**Version 1.2** retains the eleven account IDs and the original table columns,
then adds source scopes, evidence states, references and notes. The account
CSV encodes its structured chronology as JSON in one column; the separate
chronology CSV is easier to filter. The observations CSV is the simplest
starting point for comparing a single feature across accounts.

The older `approx_date` column now contains a qualified composition estimate
or an explicit unresolved label. The JSON preserves the former mixed date
strings in `legacy_date` for reconciliation; they are not endorsed dates.
Unknown textual observations have explicit display labels in the account
table and null values with evidence states in the structured JSON.
Version 1.0 contained eight accounts; version 1.1 expanded the selection to
eleven. The descriptions and qualifications in 1.2 supersede those summaries.

The site's downloads and the [API copy](https://api.wheelofheaven.world/v1/datasets/flood-myths.json)
are generated from the same reviewed record. The compiled observations are
CC0. Linked source editions retain their own terms; their full texts are not
included in the downloads.

The [Hugging Face](https://huggingface.co/datasets/wheelofheaven/flood-myths)
and [Kaggle](https://www.kaggle.com/datasets/zarazinsfuss/flood-myths) mirrors
are updated separately. Check their version labels before combining copies.
