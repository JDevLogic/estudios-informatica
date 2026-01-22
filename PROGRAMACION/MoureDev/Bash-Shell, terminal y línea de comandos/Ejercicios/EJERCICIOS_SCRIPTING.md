# SCRIPTING

## Ejercicios

1. Crea un script que imprima en pantalla: Hola mundo desde Bash.
``` bash
touch hola_script.sh
nano hola_script.sh

#!/bin/bash
echo "Hola mundo desde mi primer script"
```
2. Crea un script que muestre la fecha y el directorio actual.
```bash
touch fecha_pwd_script.sh
nano fecha_pwd_script.sh

#!/bin/bash
echo "Fecha: $(date)"
echo "Directorio actual: $(pwd)"

# Para poder ejecutar el script
chmod +x fecha_pwd_script.sh
./fecha_pwd_script.sh
```
3. Crea un script que guarde tu nombre en una variable y lo muestre en pantalla.
```bash
touch nombre_script.sh
nano nombre_script.sh

#!/bin/bash
nombre="Jonathan"
echo "Hola, $nombre"

# Para poder ejecutar el script
chmod +x nombre_script.sh
./nombre_script.sh
```
4. Crea un script que declare dos variables numéricas, las sume, reste y multiplique, mostrando el resultado de cada operación.
```bash
touch numeros_script.sh
nano numeros_script.sh

#!/bin/bash
a=10
b=3
sum=$((a + b))
rest=$((a - b))
multi=$((a * b))

echo "La suma es $sum"
echo "La resta es $rest"
echo "La multiplicacion es $multi"

# Para poder ejecutar el script
chmod +x numeros_script.sh
./numeros_script.sh
```

5. Crea un script que pida tu nombre con read y lo muestre.
```bash
touch read_nombre_script.sh
nano read_nombre_script.sh

read -p "¿Cual es tu nombre? " nombre
echo "Tu nombre es $nombre"

# Para poder ejecutar el script
chmod +x read_nombre_script.sh
./read_nombre_script.sh
```
6. Crea un script que pida dos números al usuario y muestre su suma.

7. Crea un script con tres argumentos que muestre el primero y el tercero.

8. Crea un script con argumentos que muestre el número total.

9. Crea un script que reciba dos números como argumentos y muestre su suma, resta, multiplicación y división.

10. Crea un script que cree un archivo de texto y guarde tu nombre en su interior.