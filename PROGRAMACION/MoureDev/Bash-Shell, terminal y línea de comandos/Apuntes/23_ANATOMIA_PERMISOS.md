# ADMINISTRACIÓN DEL SISTEMA

## Anatomía de los permisos

### Modo simbólico:

`-rwxrwxrwx`

Está formado por cuatro bloques: `[-][rwx][rwx][rwx]`

De izquierda a derecha:

* `-` tipo de archivo
* `rwx` permisos de usuario
* `rwx` permisos de grupo
* `rwx` permisos para otros usuarios

`rwx` está indicando que ese bloque tiene permisos de lectura (`r`), escritura (`w`) y ejecución (`x`).

> [!WARNING]  
> 
> La ausencia de un permiso (permiso no otorgado) se representa con `-`.
> 
> Ejemplos: `r--` indicaría que sólo tiene permisos de lectura, en cambio, `r-x` indicaría que tiene permisos de lectura y ejecución. Siempre se conserva el orden `rwx`.

### Modo octal:

`777`

* Está formado por 3 dígitos, representando de izquierda a derecha los bloques de `[usuario][grupo][otros]`.
* Cada número es el resultado de sumar el valor asociado al tipo de permiso:
	* `7` = 4 + 2 + 1 (lectura + escritura + ejecución) [`rwx`]
	* `6` = 4 + 2 (lectura + escritura) [`rw-`]
	* `5` = 4 + 1 (lectura + ejecución) [`r-x`]
	* `4` (lectura) [`r--`]
	* `3` = 2 + 1 (escritura + ejecución) [`-wx`]
	* `2` (escritura) [`-w-`]
	* `1` (ejecución) [`--x`]

Por lo tanto, `777` quiere decir que todos los usuarios tienen permisos de lectura, escritura y ejecución.

`764` significaría que el *propietario* tiene todos los permisos (4 + 2 + 1 = 7), el *grupo* tendría de lectura y escritura (4 + 2 = 6), y *otros* únicamente de lectura (4).

### Tipos de archivos más habituales

* `-` archivo
* `d` directorio
* `l` enlace simbólico
* `b` dispositivo de bloque
* `c` dispositivo de carácter
* `s` socket
* `p` pipe