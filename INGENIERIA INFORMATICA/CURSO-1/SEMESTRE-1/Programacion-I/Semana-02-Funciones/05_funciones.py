# Las funciones sirven para organizar y reutilizar codigo 

def saludar (nombre):                         # Creamos una funcion para saludar dependiendo del nombre
    print("Hola",nombre)                      # Ponemos el mensaje que hara al saludar

saludar("Jonathan")                           # Llamada de la funcion de saludar y el nombre entre ""


# EJERCICIOS DEL DIA

# 1. Una función saludar(nombre) que imprima un saludo personalizado.

def saludo(nombre):
    print(f"Hola {nombre}, encantado de conocerte.")

saludar("Lucia")


# 2. Una función calcular_cuadrado(numero) que devuelva el cuadrado del número.

def calcular_cuadrado(a):
    return a * a

print (calcular_cuadrado(7))


# 3.  Una función es_par(numero) que devuelva True si el número es par y False si es impar.

def es_par(a):
    return a % 2 == 0

print(es_par(3))


# 4. Una función presentacion(nombre, edad) que devuelva un mensaje como:

def presentacion(nombre,edad):
    return(f"Me llamo {nombre}, tengo {edad} años, un placer.")

print(presentacion("Jonathan",22))