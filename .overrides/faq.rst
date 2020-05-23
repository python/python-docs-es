:orphan:

Preguntas frecuentes
====================


Estoy bloqueado y no puedo resolver un problema, ¿qué hago?
-----------------------------------------------------------

Pregunta, |:smile:|.
Tenemos un `grupo de Telegram`_ en el que hay mucha gente que te puede ayudar.

.. _grupo de Telegram: https://t.me/python_docs_es


¿Cómo puedo instalar y configurar el chequeo con pospell?
---------------------------------------------------------

Uno de los chequeos que realiza nuestro servidor de github cada vez que hacemos
un pull de request es un test de corrección ortográfico usando la herramienta
pospell. Pospell puede ser instalada en tu entorno de Python empleando pip
(https://pypi.org/project/pospell/)::

    pip install pospell

Una vez instalado, para chequear el fichero .po sobre el que estás trabajando,
ejecuta desde el directorio principal del repo::

    pospell -p dict -l es_AR -l es_ES path/tu_fichero.po

pospell emplea la herramienta de diccionarios hunspell. Si pospell falla dando
como error que no tiene hunspell instalado, lo puedes instalar así:


.. tabs::

   .. tab:: Mac

      Utilizando ``brew`` (https://formulae.brew.sh/formula/hunspell)::

        brew install hunspell

      Este comando instala hunspell, pero puede que todavía necesites los diccionarios.
      Los diccionarios de Hunspell (``*.aff`` y ``*.dic``) en Mac deben estar en la
      carpeta ``~/Library/Spelling/`` o ``/Library/Spelling/``. Puedes encontrar
      diccionarios de español en las webs de Open Office, Mozilla y otros proyectos
      open source (ejemplo: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/).

   .. tab:: Linux

      # Arch Linux
      yay -S hunspell-es_any

      # Ubuntu Linux
      apt install hunspell-es


Estamos trabajando para unificar el uso de un mismo set de diccionarios de español,
pero por el momento el chequeo que hacemos es con los diccionarios es_AR y es_ES.


¿Cómo puedo configurar git para manejar correctamente los finales de línea en Windows?
--------------------------------------------------------------------------------------

En la ayuda de git puedes encontrar información sobre este problema frecuente:
https://help.github.com/es/github/using-git/configuring-git-to-handle-line-endings


¿Cómo hago en Mac para utilizar las comillas correctas?
-------------------------------------------------------

Cuando uses ``poedit`` en Mac, es muy probable que te cambie las comillas comunes que debemos utilizar
por comillas *Smart Quotes* automáticamente. Debes desactivar este comportamiento para usar el que necesitamos.

Puedes hacerlo haciendo

#. click derecho con el mouse en el texto que estás editando
#. *Substitutions*
#. *Smart Quotes*

y repetir el proceso para *Smart Dashes*.

.. figure:: mac-smartquotes.jpg
   :width: 85%
   :align: center

   Desactivar "Smart Quotes" y "Smart Dashes"


¿Qué parte de ``:ref:`` debo traducir?
--------------------------------------

Cuando veas el ``:ref:`` usado así,

.. code-block:: rst

   In the :ref:`article` you can find more examples.

**No debes traducir** *article*, ya que es una referencia a otro lugar de la documentación.
En la traducción al Español se mostrará el título de ese artículo en Español --no te preocupes.

Si en cambio lo ves usado así,

.. code-block:: rst

   In the section :ref:`how to redirect to a file <how-to-redirect-to-file>` from the logging HOWTO guide.

**Sí debes traducir** la parte que dice *how to redirect to a file*,
pero **no debes traducir** ``how-to-redirect-to-file``.

.. note::

   Pueder leer más sobre el rol ``:ref:`` de Sphinx en su `documentación oficial`_ para entender mejor como funcionan las referencias,
   aunque no es necesario que lo sepas para la traducción.

.. _documentación oficial: https://www.sphinx-doc.org/en/stable/usage/restructuredtext/roles.html#role-ref


¿Cómo configuro ``pre-commit``?
-------------------------------

.. warning::

   Requiere un poco de conocimiento de Python (para crear un entorno virtual) e instalar un paquete del sistema operativo.

Para utilizar ``pre-commit`` y así ejecutar unos pequeños tests antes de hacer un commit y enviar tus cambios a tu Pull Request,
debes seguir estos pasos:

#. Instalar ``pre-commit``::

   pip install pre-commit

#. Configurar ``pre-commit`` en el repositorio de ``python-docs-es``::

   cd python-docs-es/
   pre-commit install

#. Instalar ``hunspell``::

   # Arch Linux
   yay -S hunspell-es_any

   # Ubuntu Linux
   apt install hunspell-es

Luego, cada vez que realices un commit se ejecutará ``pre-commit`` y validará tus archivos.

.. note::

   Si por cualquier motivo no está funcionando ``pre-commit`` y no te deja hacer *push* de tus cambios,
   lo puedes desinstalar simplemente mediante: ``pre-commit uninstall``.
