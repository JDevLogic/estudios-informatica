# 🐍 Día 11 - Python (Funciones avanzadas, argumentos y retornos)

---

## ✅ Objetivo del día

* Aprender a crear funciones más avanzadas que:
  - Reciban **argumentos**
  - Utilicen **valores por defecto**
  - Devuelvan resultados con `return`
  - Manejen errores con condicionales (`if`, `else`)
  - Sean **reutilizables** en otros programas

---

## 📌 1. Función con argumento por defecto

```python
def saludar(idioma="es"):
    if idioma == "es":
        print("Hola")
    elif idioma == "en":
        print("Hello")
    else:
        print("Idioma no soportado")
```

* Si no se pasa argumento → usa `"es"` como valor por defecto.  
* Se puede usar así: `saludar()`, `saludar("en")`, `saludar("fr")`.

---

## 📌 2. Función que recibe un número por input y evalúa si es par o impar (multiidioma)

```python
def par_impar(idioma="es"):
    numero = int(input("Introduce un número: "))
    
    if idioma == "es":
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    elif idioma == "en":
        if numero % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
```

* Se solicitó un número desde teclado.  
* Se determinó si era par o impar.  
* El resultado se mostró en español o inglés, según el argumento pasado.

---

## 📌 3. Función con múltiples argumentos y retorno (`return`)

```python
def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "Error: División por cero"
        else:
            return num1 / num2
    else:
        return "Error: Operación no válida"
```

* Se realizaron múltiples llamadas a la función:

```text
calcular(10, 5, "+") → 15  
calcular(10, 5, "/") → 2.0  
calcular(10, 0, "/") → Error por división por cero  
calcular(10, 5, "x") → Error por operación no válida  
```

---

## 📦 Reutilización y claridad

* Se usó `return` para devolver resultados.  
* Se evitaron `print()` dentro de funciones complejas para poder reutilizar resultados.  
* Se mostraron los resultados con `print(calcular(...))`.

---

## 🧠 Conclusión del Día 11

✔️ Aprendimos a construir funciones más robustas  
✔️ Supimos manejar errores con lógica condicional  
✔️ Utilizamos funciones con argumentos, valores por defecto y retorno  
✔️ Creamos código reutilizable y bien comentado

