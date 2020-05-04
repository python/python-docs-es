Guía para contribuir en la traducción
=====================================

¡Muchas gracias por tu interés en participar de la traducción de la documentación oficial de Python al Español!
Necesitamos *mucho* de tu ayuda para poder seguir adelante con este proyecto.

Actualmente se puede colaborar utilizando una de las dos siguientes formas que:

#. Utilizando el repositorio de GitHub y el editor poedit_
#. Realizando traducciones directamente en Transifex


.. note::

   Si tienes cualquier duda, puedes enviarnos un email a docs-es@python.org.


Desde GitHub
------------

#. Crea un fork del repositorio_.

.. _repositorio: https://github.com/PyCampES/python-docs-es

   .. note::

      Puedes consular la `ayuda oficial de GitHub`_, si lo deseas.

      .. _ayuda oficial de GitHub: https://help.github.com/es/github/getting-started-with-github/fork-a-repo

#. Clona el repositorio::

    git clone git@github.com:<TU-USUARIO>/python-docs-es.git

#. Ingresa en la carpeta que `git clone` creó en tu computadora::

    cd python-docs-es/

#. Agrega el repositorio original como "upstream"::

    git remote add upstream https://github.com/pycampes/python-docs-es.git

#. Mira que archivo necesita ser traducido. El siguiente comando te mostrará una lista de archivos y los porcentajes traducidos.
   Elige uno que no esté completo::

     make progress

#. Una vez que hayas elegido el archivo, lo puedes abrir con el editor poedit_ y empezar a traducir.

#. Cuando hayas terminado tu sesión, debes guardar tus cambios y enviarlos a GitHub de nuevo::

    git commit -am 'Traducido archivo {nombre de archivo}'
    git push origin update-translation

#. Luego ve a tu página de GitHub y propone hacer un Pull Request

   .. note::

      Puedes consultar la `ayuda oficial de GitHub para crear un Pull Request`_ si lo deseas.

      .. _ayuda oficial de GitHub para crear un Pull Request: https://help.github.com/es/github/collaborating-with-issues-and-pull-requests/about-pull-requests


.. _poedit: https://poedit.net/



Previsualizar los cambios
~~~~~~~~~~~~~~~~~~~~~~~~~

Hay dos formas de visualizar, junto con el resultado final de la documentación, los cambios que has hecho.

Read the Docs
`````````````

Una vez que hayas hecho un Pull Request en GitHub, este mostrará al final de página una sección de "check".
Ahí, debería haber uno que diga `docs/readthedocs.org:python-docs-es`, y al lado un link de "Details".
Haciendo click en ese link, deberías poder ver una versión de la documentación con tus cambios.

Construcción local
``````````````````

Desde el mismo directorio `python-docs-es/` que se creó cuando hiciste `git clone`, puedes ejecutar::

  make build

Este comando demorará unos minutos y generará toda la documentación en formato HTML en tu computadora.
Puedes ver el con tu navegador de internet (Firefox, Chrome, etc) ejecutando::

  make serve

Y luego accediendo a http://localhost:8000/


Utilizando Transifex
--------------------

ToDo.
