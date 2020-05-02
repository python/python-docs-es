Guía para contribuir en la documentación utilizando Github
===========================================================

Crea un fork y clona el repositorio 
----------------------------------- 

https://help.github.com/en/github/getting-started-with-github/fork-a-repo

Luego de tener un fork clonalo en tu maquina

.. code-block:: bash

    # Git clone your github fork using ssh (replace raulcd):
    # Clona el repositorio en tu maquina ejecutando
    git@github.com:<TU_USUARIO>/python-docs-es.git

    # Ingresá al nuevo directorio con el repo 
    cd python-docs-es/

    # Agregá el repositorio original como upstream.
    git remote add upstream https://github.com/raulcd/python-docs-es.git


Crear un build local 
--------------------

Hay un script para automatizar estos pasos el mismo va a:

- Crear un virtualenv dentro del directorio del repositorio e instalar en el mismo las librearias necesarias
- Clonar el repositorio oficial de cpython para construir ("biuldear") la documentación. 

.. code-block:: bash

   make build 

   # luego para poder ver la documentación ejecuta el siguiente comando y podes luego ir a http://localhost:8000 para ver la documentación 
   # recién construida.
   make serve 
