# COMANDOS AVANZADOS

## Búsqueda y recuento

Búsqueda: `grep` busca patrones dentro de archivos o de la salida de otros comandos.

* `grep "texto a buscar" nombre_archivo` Busca un texto en un archivo (retorna las filas en las que aparece el texto).
	* `grep -i "texto a buscar" nombre_archivo` Busca el texto ignorando mayúsculas/minúsculas.
	* `grep -r "texto a buscar" dir` Busca el texto recursivamente en directorios

Recuento: `wc` cuenta líneas, palabras y bytes/caracteres.

* `wc nombre_archivo` Muestra el recuento de líneas, palabras y bytes/caracteres.
	* `wc -l nombre_archivo` Muestra el recuento de líneas.
	* `wc -w nombre_archivo` Muestra el recuento de palabras.
	* `wc -c nombre_archivo` Muestra el recuento de bytes/caracteres.

Como siempre, las opciones se pueden combinar: `wc -lw nombre_archivo`.