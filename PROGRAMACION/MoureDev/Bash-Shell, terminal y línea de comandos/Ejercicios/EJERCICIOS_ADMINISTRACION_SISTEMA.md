# ADMINISTRACIÓN DEL SISTEMA

## Ejercicios

<br>
1. Crea un archivo y visualiza sus permisos.

```
touch prueba.txt
ls -l
```

<br>
2. Otorga permisos de ejecución sólo al propietario en modo simbólico.

```
chmod u+x prueba.txt
```

<br>
3. Cambia sus permisos a 644.

```
chmod 664 prueba.txt
```

<br>
4. Elimina los permisos para el grupo.

```
chmod 604 prueba.txt
```

<br>
5. Haz que sólo pueda ejecutarse por el propietario.

```
chmod 700 prueba.txt
```

<br>
6. Crea una carpeta y dale permisos para que sólo el usuario pueda acceder.

```
chmod -R 700 directorio_prueba 
```

<br>
7. Cámbiale el propietario a otro usuario de tu sistema (si existe y tienes permisos).

```
chown Jonathan pruebas.txt
```

<br>
8. Consulta la máscara de permisos actual y calcula qué permisos por defecto tendrán los nuevos archivos.

```
umask        0002    
# Archivo nuevo tendra estos permisos: -rw-rw-r--
```

<br>
9. Cambia la máscara, crea un archivo y consulta los permisos por defecto del archivo.

```
umask 022
# Archivo nuevo tendra estos permisos: rw-rw-rw-
```

<br>
10. Utiliza un comando como superusuario.

```
sudo apt update 
```

