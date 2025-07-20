# 📚 Apuntes Día 1 - Python 2025

📅 **Fecha:** 16 de marzo de 2025


## ✅ 1. Variables y Tipos de Datos

String (texto): "Hola" Entero (número entero): 21 Decimal (número flotante): 1.73 Booleano (Verdadero o Falso): True / False

nombre = "Jonathan"
edad = 21
altura = 1.73
es_estudiante = True


## ✅ 2. Mostrar Tipo de Dato

print(type(nombre))  # str
print(type(edad))    # int
print(type(altura))  # float
print(type(es_estudiante))  # bool


## ✅ 3. Conversión de Tipos

🔄 Texto a número entero:

edad_numero = int("21")

🔄 Texto decimal a número:

altura_numero = float("1.75")

🔄 Número a texto:

edad_texto = str(edad_numero)

🔄 Número a booleano:

es_mayor = bool(edad_numero)


## ✅ 4. Entrada y Salida de Datos

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura = float(input("Introduce tu altura en metros: "))

print(f"Hola, {nombre}. Tienes {edad} años y mides {altura} metros.")


## ✅ 5. Operadores Aritméticos
Operador	  Significado  	                 Ejemplo
"+"                    Suma 	                       a + b
"-"                     Resta	                           a - b
"x"                Multiplicación	               a * b
/	                     División	                       a / b
//	                División entera	               a // b
%	                    Módulo	                       a % b
**	                 Potencia	                    a ** b 

## ✅ 6. Operadores de Comparación

a = 10
b = 5

print(a == b)  # Igual
print(a != b)  # Distinto
print(a > b)   # Mayor
print(a < b)   # Menor
print(a >= b)  # Mayor o igual
print(a <= b)  # Menor o igual

## ✅ 7. Operadores Lógicos

a = 10
b = 5
c = 3

AND (ambas condiciones deben ser TRUE)
print(a > b and b > c)

OR (al menos una condición debe ser TRUE)
print(a < b or b > c)

NOT (niega el resultado)
print(not (a > b))

## ✅ 8. Ejercicio Extra - Verificar positivos y negativos

primer_numero = int  (input("Introduce el primer número: "))
segundo_numero = int  (input("Introduce el segundo número: "))

print("¿Ambos son números positivos?", primer_numero > 0 and segundo_numero > 0)
print("¿Al menos uno es negativo?", primer_numero < 0 or segundo_numero < 0)

## ✅ Resumen Día 1

✔ Aprendí variables, tipos de datos y conversiones.
✔ Practiqué entrada y salida de datos.
✔ Usé operadores aritméticos, de comparación y lógicos (and, or, not).
✔ Terminé con un ejercicio extra comprobando positivos y negativos.
