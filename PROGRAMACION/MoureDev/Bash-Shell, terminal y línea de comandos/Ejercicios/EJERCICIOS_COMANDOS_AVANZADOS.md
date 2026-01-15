# COMANDOS AVANZADOS

## Ejercicios

<br>
1. Muestra todo el contenido de un archivo.

```
cat prueba.txt
```

<br>
2. Muestra el contenido paginado de un archivo.

```
less prueba.txt
```

<br>
3. Muestra las 15 primeras líneas de un archivo.

```
head -n 15 prueba.txt
```

<br>
4. Muestra las 15 últimas líneas de un archivo.

```
tail -n 15 prueba.txt
```

<br>
5. Busca una palabra en un archivo.

```
grep "test" prueba.txt
```

<br>
6. Cuenta las líneas de un archivo.

```
wc -l prueba.txt
```

<br>
7. Redirige una salida y guárdala en un archivo.

```
echo "log" > prueba.txt
```

<br>
8. Añade una nueva salida al archivo anterior.

```
echo "log2" >> prueba.txt
```

<br>
9. Encadena 3 comandos.

```
cat pruebas.txt | grep "log" | wc -w 
```

<br>
10. Crea una variable local y muéstrala.

```
nombre="Jonathan"
echo $nombre
```

