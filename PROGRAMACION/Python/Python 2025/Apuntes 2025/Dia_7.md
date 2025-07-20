# 🐍 Día 7 – Apuntes de Python


## 📌 Sets (conjuntos) en Python

* Los sets se crean con llaves `{}` y **no permiten elementos duplicados**.
* No tienen un orden fijo.
* Son útiles para operaciones matemáticas como **unión**, **intersección**, **diferencia** y para comprobar **incompatibilidades**.

### ✅ Operaciones básicas:
```python
lenguajes = {"Python", "Java", "C++", "Python"}  # "Python" duplicado
print(lenguajes)  # Solo muestra una vez cada elemento
```

### 🔁 Añadir y eliminar elementos:
```python
lenguajes.add("JavaScript")
lenguajes.remove("C++")
```

### 🔗 Operaciones entre sets:
```python
backend = {"Python", "Java", "Node.js"}
frontend = {"JavaScript", "React", "Python"}

print(backend | frontend)  # Union
print(backend & frontend)  # Interseccion
print(backend - frontend)  # Diferencia (solo backend sin frontend)
```

### ⚠️ Verificar incompatibilidades con `isdisjoint()`:
```python
usadas = {"Python", "JavaScript"}
incompatibles = {"C#", "PHP"}

if usadas.isdisjoint(incompatibles):
    print("Todo bien")
else:
    print("¡Conflicto de tecnologías!")
```

---

## ⚠️ Manejo de errores en Python con `try`, `except` y `finally`

### ✅ Básico:
```python
try:
    numero = int(input("Introduce un número: "))
    print("Número válido:", numero)
except:
    print("¡Eso no es un número válido!")
```

### 🧪 Capturar errores específicos:
```python
try:
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    resultado = num1 / num2
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Debes introducir un número válido")
```

### 🔁 Validar hasta que el usuario lo haga bien:
```python
while True:
    try:
        numero = int(input("Introduce un número mayor que 0: "))
        if numero > 0:
            print("Número válido:", numero)
            break
    except ValueError:
        print("¡Eso no es un número válido! Intenta de nuevo.")
```

### 🔒 Bloque completo con `else` y `finally`
```python
while True:
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        continue
    except ValueError:
        print("Eso no es un número válido")
        continue
    else:
        print("El resultado es:", resultado)
        break
    finally:
        print("Fin del programa")
```

---

✅ ¡Con esto terminamos Python del Día 7! Listo para pasar a Inglés técnico.
