# 🐍 Día 9 – Apuntes de Python

---

## 📌 Uso del `with open(...)` para archivos

### ✅ ¿Qué es `with`?

* Es una forma más segura de abrir archivos.
* **Cierra automáticamente** el archivo cuando terminas de usarlo, incluso si hay errores.
* Reemplaza el uso de `open()` + `close()`.

### 🧱 Sintaxis:

```python
with open("ruta/del/archivo.txt", "modo") as archivo:
    # trabajar con el archivo
    archivo.write("texto\n")
```

### ✔️ Ventajas:

* Limpia y clara  
* Evita olvidarse de cerrar archivos  
* Recomendado siempre para lectura/escritura  

---

## 📦 Módulos incorporados de Python

Un módulo es una librería de funciones que se puede importar para no escribir todo desde cero.

### 📘 Tipos:

* **Incorporados**: vienen con Python (`math`, `random`, `datetime`)  
* **Externos**: se instalan con `pip`  
* **Personalizados**: los creas tú mismo  

---

### 🔢 Módulo `math` – Operaciones matemáticas

```python
import math

print(math.sqrt(64))       # Raíz cuadrada
print(math.pow(2, 3))      # Potencia: 2^3
print(math.pi)             # Valor de pi
```

---

### 🎲 Módulo `random` – Valores aleatorios

```python
import random

print(random.randint(1, 10))  # Número aleatorio entre 1 y 10

nombres = ["Jonathan", "Lucía", "Bryan", "Carlos"]
print(random.choice(nombres))  # Nombre aleatorio
```

---

### 🕒 Módulo `datetime` – Fechas y horas

```python
import datetime

ahora = datetime.datetime.now()

print("Fecha y hora actuales:", ahora)
print("Solo la fecha:", ahora.strftime("%d/%m/%Y"))
print("Solo la hora:", ahora.strftime("%H:%M:%S"))
```

### 🧠 Códigos `strftime` útiles

| Código | Significado    | Ejemplo |
|--------|----------------|---------|
| %d     | Día (2 dígitos) | 10      |
| %m     | Mes (2 dígitos) | 04      |
| %Y     | Año completo    | 2025    |
| %H     | Hora (24h)      | 13      |
| %M     | Minutos         | 45      |
| %S     | Segundos        | 09      |

---

### 🧩 Módulos personalizados (definidos por el usuario)

#### 📁 Archivo 1: `mis_funciones.py`

```python
def saludar():
    print("¡Hola desde un módulo!")

def sumar(a, b):
    return a + b
```

#### 📁 Archivo 2: `usar_mis_funciones.py`

```python
import mis_funciones

mis_funciones.saludar()
print(mis_funciones.sumar(3, 5))

