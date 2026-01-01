# GESTIÓN DE ARCHIVOS

## Manipulación

### Creación de un archivo:

* `touch nombre_archivo` Crea un nuevo archivo en el directorio actual.

### Creación de un directorio:

* `mkdir nombre_carpeta` Crea un nuevo directorio en el directorio actual.
* `mkdir dir/nombre_carpeta` Crea un nuevo directorio en el directorio seleccionado.

### Eliminación de un directorio vacío:

* `rmdir nombre_carpeta` Elimina un directorio vacío (sólo funciona si la carpeta está vacía).

### Copia de un archivo o directorio:

* `cp nombre_archivo copia_archivo` Copia un archivo a otro en el directorio (como siempre, puede definirse otro directorio de destino).
	* `cp -r nombre_carpeta nombre_carpeta_copia` Copia recursiva de todos los archivos y subdirectorios (no preserva atributos especiales como permisos, propietarios, marcas de tiempo o enlaces simbólicos). Se usa cuando sólo quieres el contenido, no una copia exacta.
	* `cp -a nombre_carpeta nombre_carpeta_copia` Copia recursiva exacta.

### Movimiento o renombramiento de un archivo o directorio:
	
* `mv nombre_archivo dir` Mueve un archivo a un directorio.
* `mv nombre_carpeta dir` Mueve un directorio a otro.
* `mv nombre_carpeta_o_archivo nuevo_nombre` Renombra el directorio o archivo.

### Eliminación de archivos o directorios:

* `rm nombre_archivo` Elimina un archivo. 
* `rm -r nombre_carpeta` Elimina un directorio y todo su contenido de manera recursiva.
* `rm -ri nombre_carpeta` Modo de eliminación recursiva con confirmación interactiva.

> [!CAUTION]
>
> ⚠️ El comando `rm` No se envía a la papelera. Cuidado con lo que se borra.
> 
> ✋ La opción `f` (force) en `rm -rf` es muy peligrosa ya que no pide confirmación ni muestra errores si el directorio no existe.