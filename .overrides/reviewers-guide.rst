:orphan:

================================
Guía para revisar una traducción
================================
El costado humano
=================
Teniendo en cuenta que todes somos voluntaries en este proyecto, es importante que la forma de comunicarnos sea clara, concisa y amable. Como revisor/a, ayudarás a voluntaries de diferentes culturas y lugares del mundo para que su traducción sea lo más acertada posible y podamos acercar Python a las comunidades de habla hispana. Recuerda que del otro lado de un PR hay una persona que ha dedicado tiempo y esfuerzo; es por eso es la forma en que le des una devolución sobre su trabajo influirá en su actitud hacia el proyecto…¡y en sus ganas de seguir participando de nuestra comunidad!
Aquí te dejamos algunos *tips* para que tu devolución sea constructiva y genuina:

* Siempre deja un comentario en la PR que deje una conclusión general de tu devolución para dejarle claro a les traductores qué necesita modificación y qué no. Recuerda siempre comenzar reconociendo los aspectos positivos del trabajo de la otra persona y luego puedes agregar comentarios/sugerencias sobre la traducción.

El costado práctico
===================
La devolución deberá ser acertada para transmitir el mensaje que necesitamos que llegue; de esta forma, les traductores podrán revisar su trabajo y saber qué necesitan hacer para mejorarlo.
No olvides que esto se trata de una traducción técnica y como tal, el objetivo es que, básicamente, la persona que la lea pueda entender cómo usar Python. Es por esto que, si bien es importante que la sintaxis sea correcta, el objetivo no es hacer una revisión intensiva del uso del español, a menos que la forma en que se expresó la idea imposibilite que otre la entienda.

Para esto, Github te ofrece opciones para afrontar una PR (ver botón *Review Changes* arriba a la derecha de los archivos modificados por les traductores):

* *Comment*: Puedes dejar un comentario sin necesariamente aprobar la PR. Asegúrate de hacerlo con claridad para que quien tradujo sepa que debe modificar algunas cosas antes de que su PR sea aprobada.
* *Approve*: Dejar esta opción solo para PRs que no necesitan modificación alguna o que solo tengan pocas faltas de ortografía o errores de tipeo, o algún error que no genere un conflicto mayor en la traducción y en su integración al repositorio.
* *Request Changes*: Utiliza esta opción cuando la traducción necesita varias modificaciones que afectan su integración al repositorio. En este caso también asegúrate de que tu mensaje sea claro y amable para acompañar al traductor en el proceso de modificar y lograr que la PR se apruebe.

*Tips*
======

* PRs de más de 1000 líneas: Te sugerimos hacer un comentario al principio del PR para indicar hasta qué línea haz hecho el review y qué hay que revisar hasta ese hito. También si tú mismo vas a continuar la review, pero no puedes hacerla de una sola vez, es útil para saber donde retomar tu trabajo.
* El uso del checkbox “Needs work” en poedit genera en la línea anterior al párrafo un comentario “#fuzzy” para que el traductor revise esa línea. Se puede usar cuando la traducción necesita revisión y en ese momento no puedes sugerir una traducción alternativa. Ten en cuenta que los párrafos con esa marca no aparecerán traducidos en el build. Como revisor, también podrías incluir ese comentario tu mismo como sugerencia.
* Al igual que cuando uno traduce, en el proceso de revisión puedes consultar y emplear las herramientas que tenemos. Por ejemplo, si no estás seguro sobre la traducción de un término sobre el que puede que ya hayamos tomado una decisión consensuada, puedes consultar la memoria de traducción, usar el script find in po o incluso comentarlo en nuestro grupo de telegram.

El costado técnico
==================
Al revisar una traducción, deberás tener en cuenta ciertos aspectos propios de una traducción técnica de esta índole. Además de que debe entenderse el texto en español y que debes respetar el contenido de la documentación original (ver "A tener en cuenta" en la `Guía para contribuir en la traducción <https://python-docs-es.readthedocs.io/es/3.8/CONTRIBUTING.html>`_), contamos con herramientas en este proyecto que pueden fallar en ciertos casos, y que como revisor/a deberás tener en cuenta.

Cuatro razones por las que puede fallar el *build* de Travis:
* `powrap` falla
* `pospell` falla
* Dict está duplicado
* Sphinx falla
