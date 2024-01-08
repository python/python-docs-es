:orphan:

===========================
 Progreso de la traducción
===========================

Aquí puedes ver a la lista de todos los archivo de la documentación,
con sus respectivos porcentajes de lo traducido, los párrafos marcados como ``fuzzy``,
y otras estadísticas.

.. note::

   Estas listas se actualiza automáticamente cuando Pull Requests se *mergean* a la rama ``3.12``.


En progreso
-----------

Muestra los porcentajes completados por directorio y solo los archivos que no están al 100%.

.. runblock:: console

    $ potodo --path .


Completados
-----------

Lista todos los archivos con un porcentaje de traducción mayor al 90% (para contemplar los que tienen fuzzy).


.. runblock:: console

   $ python scripts/completed_files.py
