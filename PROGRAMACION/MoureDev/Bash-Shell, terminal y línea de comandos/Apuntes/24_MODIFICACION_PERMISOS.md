# ADMINISTRACIÓN DEL SISTEMA

## Modificación de permisos

* Se utiliza el comando `chmod`.

### Modo simbólico:

* `chmod [tipo_usuario][+/-][permiso] nombre_archivo/directorio`
* `+` para otorgar un permiso.
* `-` para eliminar un permiso.
* Ejemplos:
	* `chmod u+x nombre_archivo/directorio`: Otorga permisos de ejecución al usuario propietario.
	* `chmod u-x nombre_archivo/directorio`: Elimina permisos de ejecución para el usuario propietario.

### Modo octal:

* `chmod [permisos_octal] nombre_archivo/directorio`
* Ejemplos:
	* `chmod 753 nombre_archivo/directorio`: u=`rwx`, g=`r-x`, o=`-wx`
	* `chmod 642 nombre_archivo/directorio`: u=`rw-`, g=`r--`, o=`-w-`

## Cambiar propietario y grupo

* `chown [usuario] nombre_archivo/directorio` para cambiar el propietario.
* `chown [usuario]:[grupo] nombre_archivo/directorio` para cambiar el propietario y el grupo.