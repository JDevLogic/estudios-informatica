# COMANDOS AVANZADOS

## Redirecciones y pipes

### Redirecciones

* `>` Redirige la salida y sobrescribe el archivo.
* `>>` Redirige la salida y añade al final del archivo.
* `<` Toma la entrada desde un archivo.

Ejemplos:

* `echo "texto" > archivo.txt` Sobrescribe el contenido del archivo con la salida del comando (en este caso, imprimir un texto).
* `echo "texto" >> archivo.txt` Añade al contenido del archivo la salida del comando (en este caso, imprimir un texto).
* `sort < archivo.txt` Usa el archivo como entrada y ejecuta el comando con su contenido (en este caso, ordenar).

### Pipes

* `|` Encadena comandos.

Ejemplo:

* `cat nombre_archivo | grep "texto a buscar" | wc -w` Muestra el contenido de un archivo, busca un texto en ese contenido y realiza el recuento de palabras resultantes de la búsqueda.