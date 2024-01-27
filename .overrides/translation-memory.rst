:orphan:

=======================
 Memoria de traducción
=======================


Esta página contiene la Memoria de Traducción, con todos los términos dudosos que hemos ido
resolviendo, coordinandonos en cuál era la mejor traducción dado el contexto.

También incluye una serie de reglas de estilo extraídas de fuentes reconocidas.

Si quieres ver cómo se ha utilizado un término anteriormente, puedes utilizar la herramienta
``find_in_po.py`` que muestra dónde se usó ese término: original y traducción lado a lado:

.. code-block:: text

   $ python scripts/find_in_po.py docstring
   ╒════════════════════════════════════════════════════════════════════════════════════════════════╤═══════════════════════════════════════════════════════════════════════════════════════════════╕
   │ The first statement of the function body can optionally be a string literal; this string       │ La primera sentencia del cuerpo de la función puede ser opcionalmente una cadena de texto     │
   │ literal is the function's documentation string, or :dfn:`docstring`. (More about docstrings    │ literal; esta es la cadena de texto de documentación de la función, o :dfn:`docstring`.       │
   │ can be found in the section :ref:`tut-docstrings`.) There are tools which use docstrings to    │ (Puedes encontrar más acerca de docstrings en la sección :ref:`tut-docstrings`.). Existen     │
   │ automatically produce online or printed documentation, or to let the user interactively browse │ herramientas que usan las ``docstrings`` para producir documentación imprimible o disponible  │
   │ through code; it's good practice to include docstrings in code that you write, so make a habit │ en línea, o para dejar que los usuarios busquen interactivamente a través del código; es una  │
   │ of it.                                                                                         │ buena práctica incluir ``docstrings`` en el código que escribes, y hacerlo un buen hábito.    │
   ├────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
   │ Here is an example of a multi-line docstring::                                                 │ Este es un ejemplo de un ``docstring`` multi-línea::                                          │
   ├────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
   │ Use docstrings.                                                                                │ Usar ``docstrings``.                                                                          │
   ├────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤

Para términos que aún no han sido resueltos, se lista a continuación las fuentes consultadas más
habituales y con cierta referencialidad en el mundo hispanohablante o de la traducción:

Fuentes recomendadas
====================

  :Diccionario Panhispánico de dudas:

  https://www.rae.es/dpd/

  Obra orientada a resolver dudas en diferentes áreas de la lengua española: ortografía, sintaxis,
  gramática ...

  :Wordreference:

  https://www.wordreference.com/

  Diccionario y traductor multilingue

  :Linguee.es:

  https://www.linguee.es/

  Diccionario y traductor multilíngue con millones de traducciones indexadas. De los creadores
  de DeepL

  :Fundéu BBVA - Fundación para el español urgente:

  https://www.fundeu.es/

  Fundación dedicada a la resolución de dudas. Creada originalmente por la agencia estatal
  española de noticias EFE, a partir de su departamento y libro de estilo.

  :IATE - European Union terminology:

  https://iate.europa.eu/home

  Base de datos de las traducciones oficiales de la Unión Europea. Permite búsqueda por término
  y sector.



Términos y bigramas
===================

Dividimos esta sección en dos partes, los términos que se traducen y los que mantenemos el original.
Éstas son las palabras que hemos coordinado hasta el momento:


   auditing event
     evento de auditoría ``library/tempfile`` and many others
     
   array
     arreglo

   awaitable
     aguardable ``glossary``

   slash and backslash
     barra y barra invertida ``c-api``, ``tutorial``, ``library/functions.po``

   built-in
     incorporada ``glossary.po``

   built-in exceptions
     excepciones predefinidas ``tutorial/errors.po``

   bytecodes
     queda igual ``glossary.po``

   callback
     retrollamada ``glossary.po``

   callable
     invocable ``glossary.po``, ``library/functions.po``

     Nota: en ocasiones es mejora mantener callable, especialmente cuando se refiere directamente
     a la anotación de typing Callable.

   checksum
     suma de comprobación ``howto/clinic.po``

   code object
     objeto código ``c-api``, ``library/functions.po``

   context manager
     gestor de contexto

   deallocated
     desalojable ``glossary.po``

   docstring
     docstring. ``library/idle.po``

   floor division
     división entera a la baja
     En este `issue`_ más información al respecto.

   key
     clave

   keyword argument
     argumento por palabra clave / argumento de palabra clave

     host
       host  ``library/smtplib.po``
       Significado: máquina conectada a una red que provee de servicios

     hostname
       hostname  ``library/smtplib.po``
       Significado: nombre de la máquina conectada a una red que provee de servicios

     i. e.
       en otras palabras. ``library/sqlite3.po``
     handler
       gestor ``tutorial/errors.po``

   handle exception
     gestionar [una] excepción. ``tutorial/inputoutput.po``
     gestionar excepciones

   i. e.
     en otras palabras. ``library/sqlite3.po``

   in-place, in place
     in situ. Aunque estrictamente no es español, su uso es generalizado.

   library
     biblioteca. ``library/sqlite3.po``

   list comprehension / list comprehensions
     lista por comprensión / listas por comprensión.

   locale
     Configuración regional. ``library/functions.po`` and others

   helper function
     función auxiliar  ``library/typing.po``

   loop
     bucle ``tutorial/controlflow.po``

   mapping
     mapeo ``glossary.po``

   named tuple.
     tupla nombrada ``glossary.po``

   overload, overloading
     sobrecargar, sobrecarga

   override, overriding
     sobreescribir, sobreescritura

   path
     ruta ``glossary.po``

   pythonic
     *pythónico*

     idiomático

     Estes dos términos son próximos en el contexto que se usan, utilizar complementariamente
     según el contexto. Referencia: https://docs.python-guide.org/writing/style/

   raise
     lanzar, lanza. (referido a excepciones)  ``library/functions.po``, ``c-api``

   release
     version ``HOWTO``

   return / returns
     retorna / retornar ``library/sqlite3.po``

   return type
     tipo de retorno ``library/typing.po``
     tipo retornado
     tipo devuelto
     Nota: en algunos contextos es mejor usar el participio (retornado/devuelto), se prefiere
     retornado por semejanza con el original inglés "return".

   runtime
     tiempo de ejecución ``tutorial/classes.po``

   slice
    segmento ``datamodel.po``

   slicing
    segmentación ``datamodel.po``

   statement
    sentencia ``smtplib.po``

   static type checker
    Validador estático de tipos
    Notas: mantener la mayúscula, usar validación cuando se refiera a la acción y no al agente.

   string
    cadena de caracteres ``datamodel.po``

   strings
    cadenas de caracteres ``datamodel.po``

   third-party
     de terceros ``library/typing.po``

   thread
     hilos ``library/threading.po``

   timeout
     timeout  ``library/smtplib.po``
     Significado: tiempo de espera para establecer/reintentar una conexión de red

   type hint
     indicador de tipo ``library/typing.po``

   type annotation
     anotación de tipo ``library/typing.po``
     Nota: úsese como sinónimo de *type hint*, aunque en el texto se sobreentiende que anotación
     es algo accesorio, un comentario, y type hint implica que el Validador hará comprobaciones

   underscore
     guión bajo ``glossary.po``

   widget
     widget ``library/tkinter``


Términos que no se traducen
---------------------------

En general, estos términos no se traducen, con las excepciones donde una traducción menos literal
hace omitir o substituír el término. Al ser extranjerismos deben estar en cursiva (rodeados con
asterísticos).

     bytes
     bytecodes
     docstring
     script
     token
     unicode

Puedes revisar los términos no traducidos usando la siguiente regex en tu IDE:

    ``\*[^*]+\*``

Si quieres buscar esos términos sólo en el texto traducido en el archivo dado en input, puedes emplear el siguiente comando:

    ``msgexec --input library/datetime.po grep -E --regexp="\*[^*]+\*"``


Reglas de estilo
================

Estas son las reglas de estilo que hemos convenido hasta el momento:

* En títulos [de sección] sólo se usará mayúscula en la primera palabra salvo nombre propios,
  en contraste con el inglés, que lo hace en todas las palabras principales (conectores no).

  Referencia: https://www.rae.es/dpd/may%C3%BAsculas 4.17

  Ejemplo: ``tutorial/errors.po``
  `en`: Predefined Clean-up Actions
  `es`: Acciones de limpieza predefinidas


* Se priorizará la segunda persona del singular no formal (tu/vos) frente al formal (usted).
  Sin embargo, allí donde sea posible, se usarán formas impersonales (con se), ya que son comunes a
  todas las variantes del español.

  Referencia: https://www.rae.es/dpd/se punto 2

  Ejemplo: ``tutorial/errors.po``
  `en`: Look at the following example, [...]
  `es`: Véase el siguiente ejemplo, [...]


* En general se evitará la traducción literal de la voz pasiva del original en inglés y se usará
  el impersonal (pasiva refleja) en la traducción al español.

  Referencia: https://www.rae.es/dpd/se punto 2

  Ejemplo: ``tutorial/errors.po``
  `en`: [...] where the error was detected.
  `es`: [...] donde se detectó el error.
  Nota cf. "fue detectado"


* Al incluír voces latinas (in situ, a priori ...) se recomienda el uso de *cursiva* salvo en
  aquellas expresiones más habituales como etcetera o viceversa, por ser considerados
  extranjerismos.

  Referencia: https://www.fundeu.es/recomendacion/locuciones-latinas-latinismos-errores-frecuentes-621/


.. _issue: https://github.com/python/python-docs-es/issues/2754
