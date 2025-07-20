**Apuntes sobre Python**

##    1. Introducción a las variables**

- Qué son:Las variables son espacios en la memoria que almacenan datos. En Python, no es necesario declarar el tipo de dato; el lenguaje lo infiere automáticamente.
- Declaración de variables:
  
  ```python
  nombre = "Jonathan"  # Texto (string)
  edad = 21             # Número entero (integer)
  altura = 1.73         # Número decimal (float)
  es_mayor = edad >= 18 # Booleano (True o False)
  ```
 
Uso de variables:**
- Se pueden imprimir con `print()`.
- Las variables pueden participar en operaciones lógicas, matemáticas o concatenarse con cadenas de texto.


### **2. Introducción a condicionales (if, elif, else)**

- **Estructura básica:**

  ```python
  if condicion:
      # Bloque si la condicion es verdadera
  elif otra_condicion:
      # Bloque si la primera es falsa pero esta es verdadera
  else:
      # Bloque si ninguna condicion es verdadera
  ```

- **Ejemplo:**
  ```python
  nota = float(input("Introduce tu nota (entre 0 y 10): "))

  if nota < 0 or nota > 10:
      print("Solo se aceptan numeros del 0 al 10")
  elif nota >= 9:
      print("Sobresaliente")
  elif nota >= 7:
      print("Notable")
  elif nota >= 5:
      print("Aprobado")
  else:
      print("Suspenso")
  ```

### **3. Bucles en Python**

 **While**

- **Estructura:**
  
  ```python
  contador = 1
  while contador <= 5:
      print(contador)
      contador += 1  # Incremento necesario para evitar bucles infinitos
  ```

- **Ejemplo:** Contar hacia atrás:
  ```python
  contador = 10
  while contador >= 1:
      print("Cuenta atrás:", contador)
      contador -= 1
  print("¡Despegue!")
  ```

    **For**

- **Estructura:**
  ```python
  for variable in secuencia:
      # Bloque de código
  ```

- **Ejemplo:** Recorrer letras de una palabra:
  ```python
  palabra = "Python"
  for letra in palabra:
      print(letra)
  ```

### **4. Listas y el método append()**

- **Definición de listas:**
  ```python
  lista = []  # Lista vacía
  lista.append(5)  # Agregar un elemento a la lista
  print(lista)  # Salida: [5]
  ```

- **Ejemplo para guardar números primos:**
  ```python
  limite = int(input("Introduce un número límite: "))
  primos = []

  for numero in range(2, limite + 1):
      es_primo = True
      for i in range(2, int(numero ** 0.5) + 1):
          if numero % i == 0:
              es_primo = False
              break
      if es_primo:
          primos.append(numero)

  print("Números primos:", primos)
  ```


### **5. Números perfectos**

- **Definición:** Un número perfecto es igual a la suma de sus divisores propios (excluyendo el propio número).

- **Ejemplo:**
  ```python
  numero = int(input("Introduce un número: "))
  suma_divisores = 0

  for i in range(1, numero):
      if numero % i == 0:
          suma_divisores += i

  if suma_divisores == numero:
      print(f"El número {numero} es un número perfecto.")
  else:
      print(f"El número {numero} no es un número perfecto.")
  ```


### **6. Optimizaciones usando la raíz cuadrada**

- Usar `numero ** 0.5` para reducir el rango de comprobación:

  - **Sin raíz cuadrada:** Recorre todos los números desde 2 hasta el número - 1.

  - **Con raíz cuadrada:** Solo recorre hasta `int(numero ** 0.5) + 1`, haciendo el programa más eficiente.

  **Ejemplo:** Verificar si un número es primo con raíz cuadrada:
 
  ```python
  numero = int(input("Introduce un número: "))
  es_primo = True

  for i in range(2, int(numero ** 0.5) + 1):
      if numero % i == 0:
          es_primo = False
          break

  if es_primo:
      print("El número es primo.")
  else:
      print("El número no es primo.")
  ```

### **7. Buenas prácticas aprendidas**

- **Indentación:** Es crucial en Python para definir bloques de código.

- **Uso de variables claras:** Usar nombres como `es_primo`, `suma_divisores`, o `contador` ayuda a entender el propósito del código.

- **Evitar bucles infinitos:** Asegúrate de que los contadores en los bucles se actualicen correctamente.

- **Prueba con diferentes entradas:** Probar el programa con casos extremos (como números muy grandes) ayuda a identificar problemas de rendimiento.



