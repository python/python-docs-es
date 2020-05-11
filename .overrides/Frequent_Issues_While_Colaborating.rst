:orphan:

General
=====================================

Preguntas frecuentes en Mac
=====================================

¿Cómo puedo instalar y configurar el chequeo con pospell?
*********************************************************
Uno de los chequeos que realiza nuestro servidor de github cada vez que hacemos un pull de request es un test de corrección ortográfico usando la herramienta pospell. Pospell puede ser instalada en tu entorno de Python empleando pip (https://pypi.org/project/pospell/)::

    pip install pospell 

Una vez instalado, para chequear el fichero .po sobre el que estás trabajando, ejecuta:


pospell emplea la herramienta de diccionarios hunspell. Si pospell falla dando como error que no tiene hunspell instalado, lo puedes instalar empleando brew (https://formulae.brew.sh/formula/hunspell)::


    brew install hunspell
    
Este comando instala hunspell, pero puede que todavía necesites los diccionarios. Los diccionarios de Hunspell (\*.aff y \*.dic) en Mac deben estar en la carpeta ~/Library/Spelling/ o /Library/Spelling/. Puedes encontrar diccionarios de español en las webs de open office, mozilla y otros open source projects (ejemplo: https://wiki.openoffice.org/wiki/Dictionaries) .
  

Preguntas frecuentes en Windows
=====================================
