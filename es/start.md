+++
title = "Empieza aquí: diez minutos"
description = "Entrada de diez minutos a Wheel of Heaven: la premisa y quién la propone, cómo se etiquetan las afirmaciones, un versículo del Génesis y la objeción más sólida."
template = "info-page.html"

[extra]
claim_type = "direct"
editorial_pass = "2026-05"
summary = "Diez minutos, cinco pasos: qué propone el proyecto y quién lo propone, cómo distinguir una fuente de una interpretación, un versículo del Génesis leído de cerca, la objeción más sólida a esa lectura y adónde ir después."
cta_title = "Sigue leyendo"
cta_text = "La cronología recorre toda la historia era por era, desde la llegada en Capricornio hasta el presente."
cta_url = "/timeline/"
cta_label = "Abrir la cronología"
+++

{% route(label="Diez minutos, cinco pasos", unit="min") %}
premise | La premisa, y quién la propone | 1
labels | Cómo distinguir una fuente de una interpretación | 2
verse | Un versículo, leído de cerca | 3
against | La objeción más sólida | 2
next | Adónde ir después | 2
{% end %}

## 1. La premisa, y quién la propone {#premise}

*Alrededor de un minuto.*

Wheel of Heaven propone que los seres a los que el Génesis llama {% wiki(slug="elohim") %}Elohim{% end %} eran una pequeña civilización humana tecnológicamente avanzada procedente de otro mundo.
Diseñaron la vida en la Tierra, incluida la humanidad, y los textos religiosos de muchas tradiciones conservan recuerdos comprimidos de su trabajo.

{% rows() %}
La fuente | Los Mensajes raelianos, publicados por Claude Vorilhon (Raël) a partir de 1974.
El método | El sitio lee el material antiguo a través de esa lente y lo dice abiertamente.
El autor | Un único autor [raeliano](/es/wiki/raelism/), bajo seudónimo y con ayuda de IA.
La condición | No es una publicación oficial del Movimiento Raeliano.
{% end %}

Las páginas [Acerca de](/es/about/) y del [autor](/es/author/zara-zinsfuss/) ofrecen los detalles.

## 2. Cómo distinguir una fuente de una interpretación {#labels}

*Alrededor de dos minutos.*

Las afirmaciones se etiquetan allí donde se hacen, como uno de cuatro tipos.
Una frase etiquetada lleva un subrayado fino del color de la etiqueta y un punto; toca el punto para ver qué significa la etiqueta.

{% rows() %}
claim:direct | Enunciada en una fuente primaria e incontrovertida.
claim:framework | Enunciada en el canon raeliano, pero no aceptada por la erudición convencional.
claim:inferred | Una lectura razonable de una fuente que la fuente no enuncia con esas palabras.
claim:speculative | Una síntesis que va más allá de cualquier fuente aislada.
{% end %}

Un ejemplo de cada una, etiquetado como lo estaría en una entrada:

- {% claim(type="direct") %}La palabra hebrea *elohim* es de forma plural.{% end %}
- {% claim(type="framework") %}Los Elohim son una civilización de seres físicos.{% end %}
- {% claim(type="inferred") %}La torre de Babel se construyó como ofrenda de paz a los creadores.{% end %}
- {% claim(type="speculative") %}Los relatos de combate divino de Grecia, Mesopotamia y Canaán recuerdan el mismo conflicto.{% end %}

Una página larga contiene afirmaciones de más de un tipo.
Las etiquetas marcan aquellas en las que se apoya un argumento; la prosa marca las demás a medida que avanza, con expresiones como «según esta lectura» o «la erudición convencional sostiene».
La página [El método](/es/method/) explica las etiquetas en su totalidad.

## 3. Un versículo, leído de cerca {#verse}

*Alrededor de tres minutos.*

{% library(book="genesis-woh", chapter=1, verse=26) %}
Y los Elohim dijeron: «Hagamos al ser humano a nuestra imagen, según nuestra semejanza; y que ellos gobiernen sobre los peces del mar, y sobre las aves de los cielos, y sobre el ganado, y sobre toda la tierra, y sobre toda cosa que se arrastra sobre la tierra».
{% end %}

**Lo que dice el hebreo.**
El hablante es *Elohim*, un sustantivo de forma plural.
El verbo *na'aseh*, «hagamos», está en primera persona del plural, y también lo están los posesivos *be-tzalmenu* («a nuestra imagen») y *ki-dmutenu* («según nuestra semejanza»).
Estas formas no están en discusión.

{% interlinear(lang="he", dir="rtl", caption="Las primeras palabras de Génesis 1:26, leídas de derecha a izquierda. Las formas marcadas son plurales.") %}
וַיֹּאמֶר | vayyomer | y dijo | verbo, singular
אֱלֹהִים | Elohim | Elohim | sustantivo, de forma plural | *
נַעֲשֶׂה | na'aseh | hagamos | verbo, plural | *
אָדָם | adam | ser humano | sustantivo, singular
בְּצַלְמֵנוּ | be-tzalmenu | a nuestra imagen | «nuestra», plural | *
כִּדְמוּתֵנוּ | ki-dmutenu | según nuestra semejanza | «nuestra», plural | *
{% end %}

**Cómo se lee habitualmente.**
Los lectores han resuelto el plural de cuatro maneras principales:

{% rows() %}
Un «nosotros» regio | Un plural mayestático: un solo hablante que usa el plural para referirse a sí mismo.
La Trinidad | Un anuncio anticipado de las tres personas del Dios cristiano.
Un consejo | Dios dirigiéndose a un consejo de seres celestiales que lo asisten. | La mayoría de los biblistas actuales
Creadores plurales | Una pluralidad literal: más de un creador. | !Wheel of Heaven
{% end %}

La mayoría de los biblistas actuales prefieren la lectura del consejo y la comparan con las asambleas celestiales del {% libref(book="psalms", chapter=82, verse=1) %}Salmo 82{% end %} y de {% libref(book="1-kings", chapter=22, verse=19) %}1 Reyes 22{% end %}.

**Lo que propone Wheel of Heaven.**
La cuarta lectura: los Elohim deliberan como grupo porque eran un grupo, un equipo de diseñadores a punto de hacer al ser humano a su propia semejanza física.
El sustantivo *tselem*, «imagen», designa ordinariamente una figura concreta, una estatua o una silueta recortada, lo que encaja mejor con una semejanza física que con una espiritual.

**Por qué.**
El habla en plural reaparece en el mismo tipo de momento: en la creación de la humanidad, después del Edén («el hombre ha llegado a ser como uno de nosotros», {% libref(book="genesis-woh", chapter=3, verse=22) %}Génesis 3:22{% end %}) y en {% wiki(slug="babel") %}Babel{% end %} ({% libref(book="genesis-woh", chapter=11, verse=7) %}Génesis 11:7{% end %}).
Cada vez, los hablantes en plural deciden algo sobre el ser humano y luego actúan en consecuencia.
Los Mensajes raelianos dan el mismo relato de la creación con independencia de la gramática.

## 4. La objeción más sólida {#against}

*Alrededor de dos minutos.*

Cuando *Elohim* nombra al Dios de Israel, suele llevar un verbo en singular.
El primer versículo de la Biblia dice *bara Elohim*, «Elohim creó», con el verbo en singular.
Para la mayoría de los lectores, eso zanja la cuestión: el sustantivo es plural en la forma y singular en el sentido, y el «nosotros» del versículo 26 se dirige a un consejo de seres subordinados.

Wheel of Heaven acepta la gramática y no basa su argumento en la forma plural.
Lo basa en los pasajes en los que el texto habla en plural y en el relato raeliano, que lee los verbos en singular como el habla de un único representante que actúa en nombre del grupo.

{% compare(left="La lectura del consejo", right="La lectura de los creadores plurales", shared="Ambas toman en serio el plural. Discrepan sobre quiénes estaban presentes.") %}
¿Quién dice «nosotros»? | Un solo Dios, a un consejo de seres subordinados | Los creadores, entre sí
Los verbos en singular | Un solo Dios actúa | Un único representante actúa en nombre del grupo
Sostenida por | La mayoría de los biblistas actuales | Los Mensajes raelianos y Wheel of Heaven
{% end %}

Nada en el hebreo por sí solo permite decidir entre ellas, y la entrada [Elohim](/es/wiki/elohim/#what-would-revise-this-reading) enumera los hallazgos que debilitarían la lectura del proyecto.

## 5. Adónde ir después {#next}

*Alrededor de dos minutos.*

{% rows() %}
Sigue la historia | La [cronología](/es/timeline/) la cuenta en doce capítulos, uno por cada era precesional. | | timeline
Consulta los términos | La entrada [Elohim](/es/wiki/elohim/) es la página más enlazada del sitio; la [enciclopedia](/es/wiki/) tiene unas 150 entradas. | | wiki
Lee las fuentes | La [biblioteca](/es/library/) reúne los libros raelianos y nuevas traducciones del Génesis y de otros textos, con la lengua original al lado y notas sobre cada palabra disputada. | | library
Mira el método en toda su extensión | [Sendy y los Mensajes raelianos](/es/articles/sendy-and-the-raelian-messages/) compara pasaje por pasaje el primer libro raeliano con la obra anterior de Jean Sendy y sopesa los argumentos de que Raël tomara prestado de Sendy. | | articles
Usa los datos | El [Índice del Consejo Divino](/datasets/divine-council-index/) enumera consejos divinos en doce tradiciones con la ubicación en las fuentes, en CSV y JSON, para que cualquiera pueda verificarlos o reutilizarlos. | | datasets
{% end %}
