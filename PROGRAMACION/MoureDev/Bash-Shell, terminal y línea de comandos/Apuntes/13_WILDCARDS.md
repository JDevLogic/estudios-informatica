# GESTIÓN DE ARCHIVOS

## Wildcard (comodines)

Los comodines permiten trabajar con varios archivos de forma rápida. Se pueden combinar entre ellos. Se pueden combinar con diferentes comandos.

* `*` Cero o más caracteres.
* `?` Exactamente un caracter.

### Ejemplos:

* `ls *.md` Muestra todos los archivos con la extensión *md*.
* `ls *.txt` Muestra todos los archivos con la extensión *txt*.
* `ls 03*` Muestra todos los archivos que comienzan por *03*.
* `ls 03*.txt` Muestra todos los archivos que comienzan por *03* y tienen la extensión *txt*.
* `ls ?????*` Muestra todos los archivos que tienen 5 o más caracteres.
* `rm ?.txt` Elimina todos los archivos con un nombre de un único caracter y la extensión *txt*.
* `rm a????` Elimina todos los archivos que comiencen por *a* y tengan 5 caracteres.

> [!TIP]
>
> Puedes realizar combinaciones de todo tipo con comandos y comodines.