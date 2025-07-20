# 📚 Apuntes Día 2 - Python 2025

📅 **Fecha:** 19 de marzo de 2025  
## ✅ Tema principal: Condicionales en Python

---

## 🔎 ¿Qué son las condicionales?
Las condicionales permiten **tomar decisiones** en el código según se cumpla o no una condición.

**Estructura básica:**

``` python
if condición:
    # Código si la condición es verdadera
elif otra_condición:
    # Código si la otra condición es verdadera
else:
    # Código si ninguna condición se cumple

🔢 Ejemplo 1 - Positivo, Negativo o Cero

numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

✅ Probado con varios valores y funcionando correctamente.
🔢 Ejemplo 2 - Verificar mayoría de edad

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 0:
    print("Eres menor de edad")
else:
    print("Número no válido")

✅ Probado con varias edades:

    Mayor de edad ✅
    Menor de edad ✅
    Número negativo (inválido) ✅

📝 Resumen del Día 2:

✔️ Aprendí a usar if, elif y else.
✔️ Probé con varios ejemplos y valores.
✔️ Comenté el código con mis propias palabras.
✔️ Entendí cómo las condicionales toman decisiones en el programa.