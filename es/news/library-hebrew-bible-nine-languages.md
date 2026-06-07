+++
title = "Biblioteca: la Biblia hebrea se lee ya en nueve idiomas"
description = "A 7 de junio de 2026, cada libro de la Biblia hebrea en la biblioteca de Wheel of Heaven dispone de texto en nueve idiomas — el ASV inglés más ocho traducciones de dominio público."
date = 2026-06-07
template = "news-page.html"

[extra]
event_date = 2026-06-07
event_type = "announcement"
claim_type = "direct"
editorial_pass = "2026-05"
summary = "La biblioteca aloja ya cada libro de la Biblia hebrea en nueve idiomas: inglés (ASV 1901) más ocho traducciones de dominio público importadas que cubren alemán, español, francés, japonés, coreano, ruso, chino simplificado y chino tradicional. Cada versículo se muestra en el idioma del sitio del lector junto a la lectura canónica en inglés, con la edición importada, el año y la licencia registrados por libro en el catálogo. La elección de edición por idioma queda documentada en una página de metodología en el sitio de documentación."
canon_links = [
    { title = "Biblia hebrea", path = "/wiki/hebrew-bible/" },
    { title = "Génesis", path = "/wiki/genesis/" },
    { title = "Elohim", path = "/wiki/elohim/" },
    { title = "Traducción de la Biblia de Dhorme", path = "/wiki/dhorme-bible-translation/" }
]
sources = [
    { title = "Traducciones importadas: programa de fuentes por idioma", url = "https://docs.wheelofheaven.world/contributing/content/imported-translations/", outlet = "Documentación de Wheel of Heaven", date = "2026-06-07" },
    { title = "Catálogo y archivos de capítulo de data-library", url = "https://github.com/wheelofheaven/data-library", outlet = "data-library de Wheel of Heaven", date = "2026-06-07" }
]
+++

## Lo que se ha entregado

A 7 de junio de 2026, la biblioteca de Wheel of Heaven aloja la Biblia hebrea completa — de Génesis a Sofonías, treinta y seis libros — en nueve idiomas. Cada capítulo presenta la línea base del ASV inglés de 1901 junto a ediciones de dominio público importadas en alemán, español, francés, japonés, coreano, ruso, chino simplificado y chino tradicional. Los lectores que consulten la biblioteca en cualquiera de los nueve idiomas del sitio ven ahora el texto en su lengua de lectura sin necesidad de pasar por el inglés.

Las ediciones importadas están identificadas con su nombre, fecha y licencia abierta. El catálogo también informa de la cobertura por idioma: cuando los desplazamientos en la versificación entre las tradiciones masorético, Vulgata o Synodal dejan un versículo sin alinear, el ASV inglés permanece como respaldo.

| Idioma | Edición | Año | Licencia |
|---|---|---|---|
| Inglés | American Standard Version (ASV) | 1901 | Dominio público |
| Alemán | Elberfelder | 1905 | Dominio público |
| Español | Reina-Valera | 1909 | Dominio público |
| Francés | Crampon (Dhorme DP para Job y Samuel donde existe) | 1923 | Dominio público |
| Japonés | 口語訳 (Kougo-yaku) | 1955 | Dominio público (derechos morales) |
| Coreano | Korean Revised Version (KRV) | 1961 | Dominio público |
| Ruso | Synodal | 1876 | Dominio público |
| Chino simplificado | Chinese Union Version (和合本) | 1919 | Dominio público |
| Chino tradicional | Chinese Union Version (和合本) | 1919 | Dominio público |

La procedencia por libro — nombre de la traducción, año, licencia, URL de origen, fecha de recuperación — se registra en `data-library/catalog.json` para cada entrada, bajo el bloque `translations.{lang}` de cada libro.

## Por qué traducciones literales

Cada edición importada en la lista anterior es, por su teoría de traducción, una traducción de **equivalencia formal** — a veces llamada de forma laxa "literal". Las ediciones elegidas se sitúan en el lado *concordante* de sus respectivas tradiciones: Elberfelder es famosa por ser la Biblia alemana más palabra por palabra de la era moderna; Reina-Valera, Crampon, la Synodal, la KRV y la Chinese Union Version pertenecen todas al mismo linaje de equivalencia formal en sus propias lenguas. 口語訳 es la modernización en japonés coloquial de la clásica 文語訳 — todavía de equivalencia formal según los estándares de la tradición, deliberadamente posicionada frente a la 新共同訳 de equivalencia dinámica (1987), que más tarde se convirtió en el estándar católico-protestante japonés.

La elección es deliberada, no nostálgica. Una traducción de equivalencia formal intenta preservar la **forma léxica y sintáctica** de la fuente — una palabra hebrea, una palabra de destino, donde las lenguas lo permitan; una cláusula hebrea, una cláusula de destino; la misma palabra en el mismo versículo fuente recibe la misma traducción a lo largo del corpus donde es posible. Una traducción de equivalencia dinámica hace lo contrario — intenta preservar el *efecto* en el lector, lo que significa que rutinariamente colapsa, parafrasea y suaviza las elecciones de la fuente en una lengua de destino idiomática.

Para una biblioteca cuya única razón para alojar ocho traducciones es comparativa — *¿qué hace cada tradición con las perícopas del nombre divino, con Génesis 1:1, con el Salmo 82, con el plural Elohim?* — la equivalencia formal es el único registro que preserva la pregunta. Una vez que una traducción ha decidido verter `יהוה` como "the LORD" porque se lee mejor en inglés, o como 主 porque se lee mejor en japonés, la elección léxica que el canon quiere rastrear ya se ha perdido. El lector ve la pulcritud del traductor, no la lectura del traductor.

El mismo razonamiento se aplica al propio referente Elohim. Elberfelder mantiene visibles "Jehova" / "Elohim" donde el hebreo los distingue; Crampon escribe "Yahweh" y "Élohim" con la misma disciplina; la Synodal preserva los pares "Господь" / "Бог" que retornan a la fuente subyacente. Una traducción de equivalencia dinámica daría al lector, en el mismo versículo, un único *Dios* indiferenciado — más fácil de leer, pero el argumento comparativo ya no tiene nada con que comparar.

## Por qué esta es la forma correcta para la biblioteca

La biblioteca siempre ha tratado la Biblia hebrea como el texto fuente operativo que el proyecto lee, no como una traducción de destino. El ASV inglés es la superficie de lectura para la audiencia principal del proyecto; el hebreo subyacente es con lo que el canon realmente se compromete. Lo que faltaba, hasta hoy, era una forma limpia de que los lectores no anglófonos consultaran la biblioteca sin convertir el inglés en una escala intermedia obligatoria.

La elección de edición por idioma sigue la disciplina del corpus en cuanto a la jerarquización de fuentes. Cada traducción importada es una edición crítica o cuasi-crítica del siglo XIX o XX — lo bastante antigua para estar en dominio público, lo bastante reciente para ser filológicamente seria. Cuando la lectura preferida del canon requeriría una edición moderna aún protegida por derechos de autor, el proyecto utiliza el subconjunto de dominio público de esa edición o señala la laguna de forma explícita. El caso más claro es el francés: la Biblia de la Pléiade de Dhorme — la edición con la que el propio Raël trabajó durante el contacto de 1973 — permanece bajo derechos de autor franceses hasta aproximadamente 2071. La biblioteca utiliza Crampon 1923 como línea base, con el Job (1929) y el Samuel (1910) anteriores de dominio público de Dhorme sustituyendo a Crampon en esos tres libros donde existen. El razonamiento completo para cada idioma — por qué Elberfelder en lugar de Luther, por qué Crampon en lugar de Darby, por qué 口語訳 en lugar de 新共同訳, por qué la KRV de 1961 en lugar de la estricta de 1938 — vive en el sitio de documentación en [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/).

El corpus lee la Biblia hebrea como un texto en capas cuyo referente Elohim es operativo en la lengua original. Las traducciones modernas son movimientos interpretativos posteriores, y qué movimiento interpretativo realiza una traducción es visible en versículos específicos — Génesis 1:1, Salmo 82, Éxodo 3:14, las perícopas del nombre divino a lo largo del texto. Alojar ocho traducciones importadas codo a codo con el ASV vuelve ordinaria esa visibilidad: el lector que quiera comparar qué hacen Elberfelder, Crampon, la Synodal y la CUV con un versículo controvertido puede ahora hacerlo sin salir de la página de la biblioteca.

## Dónde se inscribe esto en el plan más amplio

El pipeline de traducciones importadas es la mitad del mandato de la biblioteca. La otra mitad es la [Traducción de Wheel of Heaven](https://docs.wheelofheaven.world/contributing/content/source-text-translation/), que avanza actualmente por Génesis capítulo a capítulo — una nueva lectura inglesa producida desde el hebreo bajo la propia disciplina de glosario del proyecto, con un pipeline Traductor-Editor-Revisor detrás de cada capítulo. Las traducciones importadas cubren la **amplitud** (cada libro, ocho idiomas, ediciones de dominio público, entregado hoy); la traducción WoH aporta la **profundidad** (una tradición, un libro a la vez, filológicamente defendida, todavía en curso).

Ambos pipelines alimentan el mismo campo `paragraphs[].i18n[lang]` en cada archivo de capítulo, lo que significa que la plantilla de la biblioteca los renderiza a través de la misma interfaz. Cuando la traducción WoH de Génesis alcance su primera versión estable, se situará junto a estas lecturas importadas como la propia contribución del proyecto al panorama comparativo que ha venido construyendo.

## Dónde verlo

- Índice de la biblioteca: [/library/](/library/) — cada libro de la Biblia hebrea muestra ahora nueve idiomas en su matriz de disponibilidad
- Un capítulo de muestra: [/library/genesis/](/library/genesis/) (o en tu idioma de lectura: `/de/library/genesis/`, `/ja/library/genesis/`, …)
- Catálogo y procedencia por libro: [`data-library/catalog.json` en GitHub](https://github.com/wheelofheaven/data-library/blob/main/catalog.json)
- Metodología y razonamiento del programa de fuentes por idioma: [docs.wheelofheaven.world/contributing/content/imported-translations](https://docs.wheelofheaven.world/contributing/content/imported-translations/)

## Pendientes conocidos

Tres. Los marcadores de posición franceses de Dhorme para 1 Samuel, 2 Samuel y Job todavía esperan un pase OCR limpio — las exploraciones djvu subyacentes en Internet Archive intercalan el aparato hebreo y el comentario de forma demasiado agresiva para extraerlos de modo programático. El archivo del capítulo de Abdías presenta una laguna de andamiaje (solo uno de los veintiún versículos está dividido a nivel de párrafo) que el catálogo informa actualmente, de manera errónea, como cobertura completa. Y la fuente de referencia alemana de Elberfelder para 1 Crónicas (bibel-online.net) tiene una particularidad conocida de contenido duplicado en los capítulos 13, 17, 18, 22 y 28 que el catálogo recoge en `_meta.notes` pero que el pipeline de fusión aún no ha filtrado aguas abajo. Ninguno de estos puntos bloquea la legibilidad del texto importado; los tres están registrados para el próximo pase.

---

*— Archivado el 7 de junio de 2026, mesa editorial de Wheel of Heaven.*
