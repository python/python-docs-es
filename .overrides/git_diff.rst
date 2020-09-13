:orphan:

=========================
Simplificar el `git diff`
=========================

El comando `git diff` tiene datos que pueden llegar a ser inútiles como por ejemplo:

.. code-block:: diff

    -#: ../Doc/library/signal.rst:406
    +#: ../Doc/library/signal.rst:408

Para ellos debemos instalar brew. Si no lo tienes instalado puedes seguir el instructivo de instalación Brew_.

.. tabs::

   .. tab:: Mac

      Para instalar brew en Mac ejecutar el siguiente comando::

         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Una vez instalado brew, hay que instalar podiff, para ellos ejectar el siguiente comando:

.. code-block:: bash
   
   brew install podiff

Luego abrir el archivo de configuración del respositorio local y escribir al final:

.. code-block:: bash

   [diff "podiff"]
   command = $(brew --prefix)/bin/podiff -D--minimal

Luego, si no existiese el archivo `.gitatributes` en la carpeta dónde se encuentran los 
archivos .po con los que se van a trabajar, crealo, y luego,  agregar la siguiente línea 

.. code-block:: bash

    *.po diff=podiff

Para las distribuciones de Linux se pueden utilizar algunas herramientas, como por ejemplo podiff_ y
potools_, que son compatibles con Python 2. Se puede utilizar `pip` para instalarlas.

.. code-block:: bash
   pip install podiff
   # o
   pip install potools

.. _Brew: https://docs.brew.sh/Installation
.. _podiff: https://pypi.org/project/podiff/
.. _potools: https://pypi.org/project/potools/