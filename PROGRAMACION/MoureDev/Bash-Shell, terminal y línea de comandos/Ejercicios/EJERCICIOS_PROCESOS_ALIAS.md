# PROCESOS Y ALIAS

## Ejercicios

<br>
1. Muestra todos los procesos del sistema.

```bash
ps aux
```

<br>
2. Muestra el monitor interactivo de procesos.

```bash
htop          
# Se debe de instalar primero
```

<br>
3. Utiliza el comando free de manera correcta.

```bash
free -h
# Muestra la memoria RAM disponible y usada en el sistema
```

<br>
4. Lanza sleep 100 en la terminal, suspéndelo, mándalo al segundo plano y tráelo al primer plano.

```bash
# Paso 1: Lanzar sleep 100
sleep 100

# Paso 2: Suspender el proceso (mientras esta ejecutandose)
# Presiona: Ctrl + Z
# Veras algo como: [1]+ Stopped sleep 100

# Paso 3: Ver trabajos suspendidos
jobs
# Mostrara¡: [1]+ Stopped sleep 100

# Paso 4: Mandar al segundo plano (background)
bg %1
# O simplemente: bg
# Veras: [1]+ sleep 100 &
# Ahora el proceso continua ejecutandose en segundo plano

# Verificar que esta en background
jobs
# Mostrara: [1]+ Running sleep 100 &

# Paso 5: Traer al primer plano (foreground)
fg %1
# O simplemente: fg
# El proceso vuelve al primer plano

# Ahora puedes:
# - Ctrl + Z para suspenderlo de nuevo
# - Ctrl + C para terminarlo
# - Dejarlo correr hasta que termine
```

<br>
5. Lanza un proceso como sleep y termínalo usando su PID.

```bash
# Paso 1: Lanzar sleep en segundo plano
sleep 200 &

# Esto mostrara algo como:
# [1] 41335
# Donde 41335 es el PID (Process ID)

jobs -l
# Mostrara: [1]+ 41335 Running sleep 200 &

# Paso 3: Terminar el proceso usando kill con el PID
kill 41335
```

<br>
6. Consulta el espacio en disco.

```bash
# Ver espacio en disco de todos los sistemas de archivos
df

# Con formato legible (KB, MB, GB)
df -h
```

<br>
7. Consulta el historial.

```bash
# Ver todo el historial de comandos
history

# Buscar en el historial
history | grep "palabra_clave"
```

<br>
8. Repite el último comando.

```bash
!!
```

<br>
9. Crea y prueba un alias.

```bash
# Crear un alias simple
alias ll='ls -la'

# Alias con multiples comandos
alias update='sudo apt-get update && sudo apt-get upgrade'

# Ver todos los alias definidos
alias
```

<br>
10. Elimina el alias que acabas de crear.

```bash
# Eliminar un alias especÃ­fico
unalias ll
```