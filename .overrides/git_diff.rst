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

   .. tab:: Linux

      Para instalar brew en Linux ejecutar

         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

      Luego ejecutar los siguientes comandos::

         test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
         test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
         test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
         echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

      Ten en cuenta que si usas un sistema Debian/Ubunut se utiliza el archivo `~/.profile` mientras que
      para sistemas CentOS/Fedora/RedHat se utiliza `~/.bash_profile`

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

.. _Brew: https://docs.brew.sh/Installation
