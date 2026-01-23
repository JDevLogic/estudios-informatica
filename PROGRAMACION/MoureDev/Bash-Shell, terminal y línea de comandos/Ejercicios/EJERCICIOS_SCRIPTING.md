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

#!/bin/bash
read -p "¿Cual es tu nombre? " nombre
echo "Tu nombre es $nombre"

# Para poder ejecutar el script
chmod +x read_nombre_script.sh
./read_nombre_script.sh
```
6. Crea un script que pida dos números al usuario y muestre su suma.
```bash
touch suma_script.sh
nano suma_script.sh

#!/bin/bash
read -p "Introduce el primer numero: " num1
read -p "Introduce el segundo numero: " num2

sum=$((num1 + num2))
echo "La respuesta de la suma es $sum"

# Para poder ejecutar el script
chmod +x suma_script.sh
./suma_script.sh
```
7. Crea un script con tres argumentos que muestre el primero y el tercero.
```bash
touch argumentos_script.sh
nano argumentos_script.sh

#!/bin/bash
echo "El primero argumento es: $1"
echo "El tercer argumento es: $3"

# Para poder ejecutar el script
chmod +x argumentos_script.sh

# Los argumentos se pasan al ejecutar el script desde la terminal
./argumentos_script.sh A B C
```
8. Crea un script con argumentos que muestre el número total.
```bash
touch numero_total_script.sh
nano numero_total_script.sh

#!/bin/bash
echo "Numero de parametros: $#"

# Para poder ejecutar el script
chmod +x numero_total_script.sh

# Los argumentos se pasan al ejecutar el script desde la terminal
./numero_total_script.sh A B C
```
9. Crea un script que reciba dos números como argumentos y muestre su suma, resta, multiplicación y división.
```bash
touch dos_numeros_script.sh
nano dos_numeros_script.sh

#!/bin/bash
sum=$(($1 + $2))
rest=$(($1 - $2))
mult=$(($1 * $2))
div=$(($1 / $2))

echo "El resultado de la suma es: $sum"
echo "El resultado de la resta es: $rest"
echo "El resultado de la multiplicacion es: $mult"
echo "El resultado de la divison es: $div"

# Para poder ejecutar el script
chmod +x dos_numeros_script.sh

# Los argumentos se pasan al ejecutar el script desde la terminal
./dos_numeros_script.sh 10 5

```
10. Crea un script que cree un archivo de texto y guarde tu nombre en su interior.
```bash
touch archivo_nombre_script.sh
nano archivo_nombre_script.sh

#!/bin/bash
read -p "Introduce tu nombre completo: " nombre
echo "Tu nombre completo es: $nombre" > archivo_nombre.txt
```