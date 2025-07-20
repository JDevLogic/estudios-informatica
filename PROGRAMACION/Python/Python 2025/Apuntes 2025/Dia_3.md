# 📚 Apuntes Día 3 - Python 2025
📅 Fecha: 20 de marzo de 2025

## ✅ Tema: Bucles y Control de Bucles

---

## 🔄 1. Bucles en Python

Existen dos tipos de bucles en Python:

- **while**: Se repite mientras la condición sea verdadera.
- **for**: Se repite un número determinado de veces o sobre una secuencia (listas, rangos, etc.).

---

### 🔹 Bucle while
Se usa cuando **no sabemos cuántas veces se repetirá**.

Ejemplo:
- Creamos el contador con valor 1
- Mientras el contador sea menor o igual a 5, se ejecuta el bucle
- Se imprime el valor y se incrementa el contador

---

### 🔹 Bucle for
Se usa cuando **sabemos cuántas veces se va a repetir**.

Ejemplo:
- Se recorre un rango de números
- Imprime cada número

---

### 🔹 Bucle for con números pares
- El primer número es el inicio
- El segundo es el fin (sin incluirlo)
- El tercero es el paso
- Si el paso es 2, recorre de dos en dos, imprimiendo números pares

---

## 🚀 2. Control de Bucles: `break`, `continue`, `pass`

---

### 🔸 **break** - Rompe el bucle y termina la ejecución
- Se recorre el rango de números
- Al llegar a la condición deseada, el bucle se rompe con break
- Se imprime un mensaje de parada

---

### 🔸 **continue** - Salta la iteración actual y sigue con la siguiente
- Si la condición se cumple, imprime un mensaje y salta esa vuelta
- No se ejecuta el resto del código de esa iteración

Nota: Si el print está antes del if, se imprimirá también la condición saltada. Si está después, se omite esa vuelta.

---

### 🔸 **pass** - No hace nada
- Se utiliza como relleno para que el programa no se rompa aunque la condición esté vacía
- Permite dejar código "pendiente"

---

## 📌 3. RESUMEN DEL CONTROL DE BUCLES

| Comando   | Función                                                      |
|----------|--------------------------------------------------------------|
| `break`  | Rompe el bucle y termina                                     |
| `continue` | Salta la iteración actual y continúa con la siguiente        |
| `pass`   | No hace nada, solo evita el error de bloque vacío             |

---

✅ **Consejos**:
- `break` se usa para cortar el bucle cuando se cumple una condición.
- `continue` se usa cuando quieres **saltar** esa iteración pero continuar el bucle.
- `pass` se usa cuando el código no está listo pero no quieres que dé error.

