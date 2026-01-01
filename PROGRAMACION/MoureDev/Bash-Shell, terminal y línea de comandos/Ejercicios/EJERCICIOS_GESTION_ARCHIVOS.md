# GESTIÓN DE ARCHIVOS

## Ejercicios

<br>
1. Crea un directorio.

```
mkdir pruebas
```

<br>
2. Elimina el directorio que acabas de crear.

```
rmdir pruebas
```

<br>
3. Copia un archivo en el directorio actual y fuera de éste.

```
cp texto1.txt pruebas/
```

<br>
4. Mueve un archivo del directorio actual.

```
mv texto2.txt pruebas/
```

<br>
5. Cambia el nombre del archivo que acabas de mover.

```
mv texto2.txt textodos.txt
```

<br>
6. Lista todos los archivos de un tipo usando un comodín.

```
ls *.txt
```

<br>
7. Elimina un directorio de manera recursiva (cuidado con lo que vas a borrar).

```
rm -r pruebas
```

<br>
8. Elimina todos los archivos de un mismo tipo (cuidado con lo que vas a borrar).

```
rm -i *txt
```

<br>
9. Utiliza el comando tree.

```
tree
tree -a         # Para ver tambien los ocultos
```

<br>
10. Busca un archivo concreto en el directorio actual utilizando find.

```
find texto?.txt
```