Guía para contribuir en la traducción
=====================================

¡Muchas gracias por tu interés en participar de la traducción de la documentación oficial de Python al Español!
Necesitamos *mucho* de tu ayuda para poder seguir adelante con este proyecto.

.. note::

   Si tienes cualquier duda, puedes enviarnos un email a docs-es@python.org.


#. Crea un fork del repositorio_.

   .. note::

      Puedes consular la `ayuda oficial de GitHub`_, si lo deseas.

#. Clona el fork del repositorio que acabas de crear::

     git clone git@github.com:<TU-USUARIO>/python-docs-es.git

#. Ingresa en la carpeta que `git clone` creó en tu computadora::

     cd python-docs-es/

#. Agrega el repositorio original como "upstream"::

     git remote add upstream https://github.com/pycampes/python-docs-es.git

#. Crea una branch nueva en base al artículo en el que vayas a trabajar.
   Por ejemplo, si vas a trabajar en el archivo ``glosario.po``, usa un nombre similar a::

     git checkout -b traduccion-glosario

#. Una vez que hayas elegido el archivo, lo puedes abrir con el editor poedit_ y empezar a traducir.

#. Cuando hayas terminado tu sesión, debes guardar tus cambios y enviarlos a GitHub de nuevo::

     git commit -am 'Traducido archivo {nombre de archivo}'
     git push origin traduccion-glosario

#. No olvides añadir tu nombre al archivo ``TRANSLATORS`` si no lo has hecho todavía.
   Los nombres se encuentran ordenados alfabéticamente por apellido.

#. Luego ve a tu página de GitHub y propone hacer un Pull Request.

   .. note::

      Puedes consultar la `ayuda oficial de GitHub para crear un Pull Request`_ si lo deseas.


¿Qué archivo traducir?
----------------------

Tenemos una `lista de issues en GitHub`_ en dónde vamos coordinando el trabajo realizado para no traducir dos veces lo mismo.
El proceso para traducir un archivo es el siguiente:


#. Elige cualquier de los que *no están asignados* a otra persona.
#. Deja un comentario en el issue diciendo que quieres trabajar en él.
#. Espera a que un administrador te asigne el issue.
#. ¡Empieza a traducir!



A tener en cuenta
-----------------

* No debes traducir el contenido de ``:ref:...`` y ``:term:...``.
* Si tienes que palabras en inglés, debes ponerlas en *italics* (rodeadas por asteristicos)
* Si traduces un título que es un link, por favor traduce el link también (por ejemplo un artículo a Wikipedia).
  En caso de que no haya una traducción del artículo en Wikipedia, deja el título sin traducir.
* Tenemos una `Memoria de Traducción`_, que usamos para tener consistencia con algunos términos.



.. note::

   También puedes unirte a `nuestro canal de Telegram`_ si necesitas ayuda.



Previsualizar los cambios
-------------------------

Hay dos formas de visualizar, junto con el resultado final de la documentación, los cambios que has hecho.

Read the Docs
`````````````

Una vez que hayas hecho un Pull Request en GitHub, este mostrará al final de página una sección de "check".
Ahí, debería haber uno que diga ``docs/readthedocs.org:python-docs-es``, y al lado un link de "Details".
Haciendo click en ese link, deberías poder ver una versión de la documentación con tus cambios.

Construcción local
``````````````````

Desde el mismo directorio ``python-docs-es/`` que se creó cuando hiciste ``git clone``, puedes ejecutar::

  make build

Este comando demorará unos minutos y generará toda la documentación en formato HTML en tu computadora.
Puedes ver el con tu navegador de internet (Firefox, Chrome, etc) ejecutando::

  make serve

Y luego accediendo a http://localhost:8000/


.. _repositorio: https://github.com/PyCampES/python-docs-es
.. _ayuda oficial de GitHub: https://help.github.com/es/github/getting-started-with-github/fork-a-repo
.. _ayuda oficial de GitHub para crear un Pull Request: https://help.github.com/es/github/collaborating-with-issues-and-pull-requests/about-pull-requests
.. _poedit: https://poedit.net/

.. _nuestro canal de Telegram: https://t.me/python_docs_es
.. _Memoria de traducción: https://python-docs-es.readthedocs.io/es/3.7/translation-memory.html
.. _lista de issues en GitHub: https://github.com/PyCampES/python-docs-es/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc
