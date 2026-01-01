# GESTIÓN DE ARCHIVOS

## Listados avanzados

* `tree` Muestra un árbol de directorios y archivos.
	* `tree -a` Muestra también los directorios y archivos ocultos.
* `find . -name "nombre"` Encuentra archivos por nombre en el directorio actual.
	* `find dir -name "*.log"` Encuentra archivos por criterio de búsqueda (todos los *log*, por ejemplo) en el directorio especificado.

> [!NOTE]
>
> El comando `tree` no está instalado por defecto. Ten en cuenta cómo hacerlo según tu sistema operativo y el gestor de paquetes empleado (por ejemplo *apt* o *homebrew*, entre otros).