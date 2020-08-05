:orphan:

=======================
 Memoria de traducción
=======================


Esta página contiene la Memoria de Traducción, con todos los términos que hemos ido teniendo dudas,
y coordinamos cuál era la mejor traducción dado el contexto.

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


Términos y bigramas
===================

Éstos son las palabras que hemos coordinado hasta el momento:


     awaitable
       aguardable ``glossary``

     slash and backslash
      barra y barra invertida ``c-api``,``tutorial``,``library/functions.po``

     built-in
       incorporada ``glossary.po``

     built-in exceptions
       excepciones predefinidas ``tutorial/errors.po``

     bytecodes
       queda igual ``glossary.po``

     callable
       invocable ``glossary.po``, ``library/functions.po``

     code object
       objeto código ``c-api``, ``library/functions.po``

     deallocated
       desalojable ``glossary.po``

     docstring
       docstring. ``library/idle.po``

     key
       clave
       
     keyword argument
       argumento por palabra clave / argumento de palabra clave

     handler
       gestor ``tutorial/errors.po``, ``library/functions.po``

     handle exception
       Gestionar excepción. ``tutorial/inputoutput.po``

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

     path
       ruta ``glossary.po``

     raise
       lanzar, lanza. (referido a excepciones)  ``library/functions.po``, ``c-api``

     realease
       version ``HOWTO``

     runtime
       tiempo de ejecución  ``tutorial/classes.po``

     static type checker
       Validador estático de tipos
       Notas: mantener la mayúscula, usar validación cuando se refiera a la acción y no al agente.

     third-party
       de terceros ``library/typing.po``

     type hint
       indicador de tipo  ``library/typing.po``

     type annotation  ``library/typing.po``
       anotación de tipo
       Nota: úsese como sinónimo de *type hint*

     release
      version ``HOWTO``  

     slice
      segmento ``datamodel.po``

     slicing
      segmentación ``datamodel.po``

     string
      cadena de caracteres ``datamodel.po``

     strings
      cadenas de caracteres ``datamodel.po``

     underscore
       guión bajo ``glossary.po``

     auditing event
       evento de auditoria ``library/tempfile``

     widget
       widget ``library/tkinter``

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
