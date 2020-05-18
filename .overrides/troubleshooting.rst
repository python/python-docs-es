:orphan:

General
=======

Preguntas frecuentes en Mac
===========================

¿Cómo puedo instalar y configurar el chequeo con pospell?
*********************************************************

Uno de los chequeos que realiza nuestro servidor de github cada vez que hacemos 
un pull de request es un test de corrección ortográfico usando la herramienta
pospell. Pospell puede ser instalada en tu entorno de Python empleando pip 
(https://pypi.org/project/pospell/)::

    pip install pospell 

Una vez instalado, para chequear el fichero .po sobre el que estás trabajando,
ejecuta desde el directorio principal del repo::

    pospell -p dict -l es_AR -l es_ES path/tu_fichero.po

pospell emplea la herramienta de diccionarios hunspell. Si pospell falla dando 
como error que no tiene hunspell instalado, lo puedes instalar empleando brew 
(https://formulae.brew.sh/formula/hunspell)::

    brew install hunspell
    
Este comando instala hunspell, pero puede que todavía necesites los diccionarios. 
Los diccionarios de Hunspell (``*.aff`` y ``*.dic``) en Mac deben estar en la 
carpeta ``~/Library/Spelling/`` o ``/Library/Spelling/``. Puedes encontrar 
diccionarios de español en las webs de Open Office, Mozilla y otros proyectos 
open source (ejemplo: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/).

Estamos trabajando para unificar el uso de un mismo set de diccionarios de español, 
pero por el momento el chequeo que hacemos es con los diccionarios es_AR y es_ES.
  

Preguntas frecuentes en Windows
===============================


¿Cómo puedo configurar git para manejar correctamente los finales de línea?
***************************************************************************

En la ayuda de git puedes encontrar información sobre este problema frecuente:
https://help.github.com/es/github/using-git/configuring-git-to-handle-line-endings
