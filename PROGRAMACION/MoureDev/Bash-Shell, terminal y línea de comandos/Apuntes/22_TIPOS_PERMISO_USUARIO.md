# ADMINISTRACIÓN DEL SISTEMA

> [!NOTE]  
> 
> En Unix/Linux, cada archivo o directorio tiene permisos para controlar quién puede **leer**, **escribir** o **ejecutarlo**.

## Tipos de permiso

### Modo simbólico:

* `r` lectura
* `w` escritura
* `x` ejecución

### Modo octal:

* `4` (`r`) lectura
* `2` (`w`) escritura
* `1` (`x`) ejecución

## Tipos de usuario

* `u` usuario propietario
* `g` grupo de usuarios
* `o` otros
* `a` todos

## Ver permisos

* En archivos: `ls -l nombre_archivo`
* En carpetas: `ls -ld nombre_directorio`