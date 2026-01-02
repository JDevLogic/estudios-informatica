# COMANDOS AVANZADOS

## Variables de entorno

Puedes definir variables temporalmente (locales) o que existan en todo momento (globales).

### Variable local

Las variables locales sólo viven en la sesión actual.

* `nombre_variable="valor asociado a la variable"` Almacena el valor de un texto en una variable.
* `echo $nombre_variable ` Muestra el valor de la variable.

### Variable global

Las variables globales viven más allá de la sesión (en todos los programas lanzados desde esa terminal de la sesión).

**Algunas variables globales ya existentes:**

* `echo $HOME` Muestra la ruta del directorio home del usuario.
* `echo $PATH` Muestra una lista de rutas separadas conocidas por el sistema por defecto.

**Creación de una variable global:**

* `export NOMBRE_VARIABLE="valor asociado a la variable"`

**Creación de una variable global permanente:**

Para ello debes agregar la línea de la exportación a tu archivo de configuración de la shell. Los archivos de configuración más habituales creados en tu directorio de usuario son:

* `~/.bash_profile`
* `~/.bash_login`
* `~/.profile`
* `~/.bashrc`