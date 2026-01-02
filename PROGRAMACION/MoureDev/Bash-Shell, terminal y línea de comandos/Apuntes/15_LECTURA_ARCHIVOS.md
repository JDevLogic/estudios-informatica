# COMANDOS AVANZADOS

## Lectura de archivos

* `cat` Muestra todo el contenido del archivo en pantalla (útil para archivos pequeños).
* `less` Permite ver archivos largos, paginando su contenido (sales pulsando `q`).
* `more` Similar a less, pero como menos funcionalidades (por ejemplo, no puedes desplazarte hacia atrás).
* `head` Muestra las primeras 10 líneas de un archivo por defecto.
	* `head -n 20` Para especificar el número de líneas.
* `tail` Muestra las últimas 10 líneas de un archivo por defecto.
	* `tail -n 20` Para especificar el número de líneas.
	* `tail -f file.log` Muy útil para ver logs en tiempo real mientras crecen.

> [!TIP]
>
> Para desplazarte por la paginación es habitual usar flechas, barra espaciadora, scroll o PgUp/PgDown.