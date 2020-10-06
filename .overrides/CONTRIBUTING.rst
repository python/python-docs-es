:orphan:

Guía para contribuir en la traducción
=====================================

¡Muchas gracias por tu interés en participar de la traducción de la
documentación oficial de Python al Español!

Este es el grupo de trabajo para la traducción de la
documentación oficial de Python al Español, todo el contenido de la traducción
es mantenido por voluntaries que aportan su tiempo y trabajo a la comunidad.

Antes de comenzar tu primera traducción, y que sigas con esta guia de
contribución, queremos señalar algunos
:ref:`lineamientos generales <a-tener-en-cuenta>`.

.. note::

   Si tienes cualquier duda, puedes enviarnos un email a docs-es@python.org.

Antes de comenzar
-----------------

#. Para enviar una traducción, necesitas tener un **fork** del repositorio_
   oficial, haciendo click en el botón encerrado en rojo.

   .. image:: fork.png
     :alt: botón fork

   .. note::

      Puedes consular la `ayuda oficial de GitHub`_, si lo deseas.

#. Clona el fork del repositorio que acabas de crear::

     git clone git@github.com:<TU-USUARIO>/python-docs-es.git

#. Ingresa en la carpeta que `git clone` creó en tu computadora::

     cd python-docs-es/

#. Agrega el repositorio original como "upstream"::

     git remote add upstream https://github.com/python/python-docs-es.git

#. (Opcional) Crea un entorno virtual y actívalo::

     python -m venv env
     source env/bin/activate   # macOS y Linux
     env\Scripts\activate.bat  # Windows

#. (Opcional) Instala los requerimientos del proyecto::

     pip install -r requirements.txt

   .. note::

      Al tener instalado los requerimientos, podrás utilizas las herramientas
      ``powrap`` y ``pospell`` para poder verificar tus archivos traducidos,
      y también contruir la documentación localmente.

¡Comienza a traducir!
---------------------

#. Selecciona un :ref:`archivo para traducir <que-archivo-traducir>`.

#. Verifica que estás en la rama principal del repositorio, **3.8**::

     git checkout 3.8

#. Crea una rama nueva en base al artículo en el que vayas a trabajar.  Por
   ejemplo, si vas a trabajar en el archivo ``library/glosario.po``, usa un nombre
   similar a::

     git checkout -b traduccion-glosario

#. Una vez que hayas elegido el archivo, lo puedes abrir con el editor poedit_ y
   empezar a traducir.

#. Cuando hayas terminado tu sesión, debes guardar tus cambios y enviarlos a
   GitHub (No olvides añadir tu nombre al archivo ``TRANSLATORS``)::

     git add library/glosario.po
     git commit -m 'Traducido archivo library/glosario'
     git push origin traduccion-glosario

   .. note::

      Mira los mensajes que el último comando imprimirá por pantalla,
      pues encontrarás un enlace para abrir un nuevo Pull-request directamente.

      Puedes consultar la `ayuda oficial de GitHub para crear un Pull Request`_
      si lo deseas.


#. En la descripción de la *Pull Request* escribe ``Closes #<número de issue>``
   (así se cierra automáticamente cuando se hace *merge*)

   .. note::

      Si hace tiempo que venis trabajando en una traducción es importante
      :ref:`mantener actualizada <mantener-actualizada>` tu copia local antes
      de realizar el *Pull Request*.

.. _que-archivo-traducir:

¿Qué archivo traducir?
----------------------

Tenemos una `lista de issues en GitHub`_ en dónde vamos coordinando el trabajo
realizado para no traducir dos veces lo mismo.  El proceso para traducir un
archivo es el siguiente:


#. Elige cualquier de los que *no están asignados* a otra persona.
#. Deja un comentario en el issue diciendo que quieres trabajar en él.
#. Espera a que un administrador te asigne el issue.
#. ¡Empieza a traducir!


.. _a-tener-en-cuenta:

A tener en cuenta
-----------------

* Esta traducción es mantenida por **personas de todo el mundo** que hablan el
  idioma Español. No queremos atarla a ninguna región en particular y creemos
  que es un valor extra la diversidad de la misma.  Vas a encontrar secciones
  con diferentes tonalidades de países, regiones o estilos. Lo único que pedimos
  es **consistencia** dentro de un mismo módulo o sección (es decir no cambiar de
  estilo de un párrafo a otro, por ejemplo) y siempre intentar que la persona del
  otro lado pueda entender lo que estamos escribiendo (no usar lunfardo o
  regionalismos muy propios de un único lugar).

* En muchos casos el **mejor criterio** es pensar en el vocabulario que utilizamos
  cuando le explicamos a otra persona, o en el trabajo. En muchas ocasiones la
  versión en inglés o “spanglish” de la palabra es mucho mejor que decir “git
  unir” (para git merge).

* Siempre vas a tener una **revisión de lo que propongas** y en ese intercambio otras
  personas van a ayudarte a destrabar las dudas que tengas.

* Colaborar **haciendo revisiones** también es muy muy importante, así que si
  tienes un rato libre puedes comenzar por mirar los PRs pendientes de revisar.
  (mira la :doc:`Guía del revisor <reviewers-guide>`)

* La documentación es ENORME, cualquier traba que encuentres siempre puedes
  marcar el texto como **"fuzzy"** o para revisar en el futuro.
  No pierdas horas buscando la palabra perfecta.

* **No debes** traducir el contenido de ``:ref:...``, ``:term:...``, ``:dfn:...``, etc.

* Si tienes que usar palabras en inglés debes ponerlas en *cursiva* (rodeadas
  por asteriscos)

* Puedes revisar las :doc:`Preguntas Frecuentes <faq>` para leer sobre problemas conocidos.

* Si **traduces un título que es un enlace**, por favor traduce el link también (por
  ejemplo un artículo a Wikipedia). En caso de que no haya una traducción del
  artículo en Wikipedia deja el título sin traducir.

* Tenemos una :doc:`Memoria de Traducción <translation-memory>`, que usamos para tener
  consistencia con algunos términos.

* Si tienes una **duda sobre una palabra o término**, escríbelo como mejor suene
  para vos y marca ese párrafo como "Need work" / "Necesita trabajo" en
  *poedit*. Además, escribe un comentario explicando cuál es el termino en ese
  párrafo con el que no estabas segura.

* Puedes usar `la traducción al Portugués`_ para ver cómo ellos hicieron la
  traducción de alguna palabra.

* Wikipedia puede ser útil también. Busca la palabra en Inglés, y luego mira si
  tiene una traducción al Español en la barra de la izquierda. Suelen estar
  bastante bien explicados.

* Te recomendamos abrir una **Pull Request aunque sea en formato borrador** (marcada
  como draft) desde los primeros commits de la traducción de tu fichero. De esta
  forma, puedes recibir feedback desde el principio que puedes aplicar al resto
  de la traducción, y probar el build más a menudo.

* Último pero no menos importante, **divertite y contá con la ayuda de todes**. Te
  esperamos en nuestro chat en telegram. ¡Gracias!


.. note::

   También puedes unirte a `nuestro canal de Telegram`_ si necesitas ayuda.


Previsualizar los cambios
-------------------------

Una vez que hayas hecho un *Pull Request* en GitHub, este mostrará al final de página una sección de "check".
Allí debería haber uno que diga ``docs/readthedocs.org:python-docs-es`` y al lado un link de "Details".

.. figure:: readthedocs-preview.png
   :width: 85%
   :align: center

Haciendo click en ese link verás una versión de la documentación completa que incluirá todos tus cambios.
Tendrás que navegar hasta el archivo que hayas cambiado para ver cómo se visualiza luego del build.


.. _repositorio: https://github.com/python/python-docs-es
.. _ayuda oficial de GitHub:
   https://help.github.com/es/github/getting-started-with-github/fork-a-repo
.. _ayuda oficial de GitHub para crear un Pull Request:
   https://help.github.com/es/github/collaborating-with-issues-and-pull-requests/about-pull-requests
.. _poedit: https://poedit.net/

.. _nuestro canal de Telegram: https://t.me/python_docs_es
.. _la traducción al Portugués: https://docs.python.org/pt-br/3/
.. _lista de issues en GitHub:
   https://github.com/python/python-docs-es/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+no%3Aassignee+translate
