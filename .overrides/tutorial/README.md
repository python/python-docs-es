README
======

Introducción
------------

Este README describe la técnica utilizada en Inkscape para generar
el logo de python-docs-es con el nombre de todos los traductores.

La tecnica se llama a veces "Text portrait" y consiste simplemente
en utilizar una imagen como mascara para un texto. Muchos tutoriales
en línea explican el proceso de forma mas o menos completa.

Los archivos `ready-centered.svg` y `ready-fullpage.svg` ya tienen
la tecnica aplicada sobre la imágen de una letra "ñ".

La lista de todos los traductores está en el archivo `./TRANSLATORS`.
Lo ideal es transformar los `\n` en espacios poder copiar y pegar.
Por ejemplo: `$ cat TRANSLATORS | tr '\n' ' ' `


Modificar la lista de traductores
---------------------------------

Si sólo se quiere modificar la lista de traductores:

0. En Inkscape abrir uno de los archivos SVG (`ready-centered.svg` o `ready-fullpage.svg`)
1. Abrir el panel de objetos (`Object`/`Objects...`).
2. Seleccionar el objeto `text`
3. Abrir el panel de texto (`Text`/`Text and fonts...` o `Shift`+`Ctrl`+`T`)
4. Elegir el tabs `Text` del panel de texto
5. Remplazar el contenido y cliquear `Apply`

Si el texto es mas corto o mas largo, para que el texto ocupe toda la imágen
puede que haya que adaptar la fuente utilizada (fuente, tamaño, espaciado, ...).


Modificar la imágen
-------------------

Si se quiere modificar la imágen utilizada:

0. En Inkscape abrir uno de los archivos SVG (`ready-centered.svg` o `ready-fullpage.svg`)
1. Abrir el panel de objetos (`Object`/`Objects...`)
2. Seleccionar el objeto `text`
3. Elegir la opción `Object`/`Mask`/`Release` para "soltar" la máscara utilizada
4. En el panel de objetos, aparece un grupo (`gXXXXX`) con la la ñ y un fondo gris
5. Eliminar u ocultar el grupo
6. Agregar la nueva imágen a utilizar (via Drag and Drop o `File`/`Import...`)
7. Aseguarse que la imágen tiene el mismo tamaño que el texto:
   a. Seleccionar el objeto texto -> `Ctrl`+`C`
   b. Seleccionar la imágen agregada -> `Edit`/`Paste Size`/`Paste Size`
8. Centrar la imágen sobre la página (panel `Object`/`Align and Distribute`)
9. En el panel de objetos, seleccionar la imágen y luego el texto
10. Setear la máscara con `Object`/`Mask`/`Set`

En las partes oscuras de la imágen aparece el texto claro y viceversa.
Puede que sea necesario ajustar la imágen para obtener un buen resultado.
