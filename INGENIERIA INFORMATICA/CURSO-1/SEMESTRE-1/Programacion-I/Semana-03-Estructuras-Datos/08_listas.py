# LISTAS(Fundamentos)
# ===============================

# Una lista es una estructura de datos que permite almacenar
# múltiples valores en una sola variable.

# Características principales:
# - Es ordenada (tiene posiciones / índices)
# - Es mutable (se puede modificar)
# - Puede contener distintos tipos de datos

# Ejemplo de lista:

numeros = [1, 2, 3, 4]

nombres = ["Ana", "Luis", "Marta"]

print(numeros)
print(nombres)

# Acceso por índice (empieza en 0)

print(numeros[0])
print(nombres[1])

# Las listas son mutables

numeros[2] = 10
print(numeros)

# Longitud de una lista

print(len(numeros))
print(len(nombres))


# =========================
# EJERCICIOS DEL DÍA
# =========================

# 1) Crear una lista con 5 números y mostrar:
#    - el primer elemento
#    - el último elemento

num = [0,2,3,4,5]

print(num[0])
print(num[4])


# 2) Cambiar el valor del tercer elemento de la lista

num[2] = 67

print(num)


# 3) Mostrar la longitud de la lista

print(len(num))


# 4) Crear una lista vacía y comprobar su longitud

vacio = []

print(len(vacio))


# ================================
# OPERACIONES BÁSICAS CON LISTAS
# ================================

# Añadir elementos
# append()

# Eliminar elementos
# remove() y pop()

# Comprobar si un elemento existe
# in

# Añadir elementos a una lista 

num1 = [1,2,4]

num1.append(3)

print(num1)


# Eliminar elementos de una lista

num1.remove(1)
print(num1)

num1.pop()
print(num1)


# Comprobar si un elemento existe en la lista

names = ["JDevlogic", "Kayder","Bryan"]

print("JDevlogic" in names)
print("Isaias" in names)


# ================================
# EJERCICIOS DEL DÍA
# ================================

# 5) Crear una lista vacía y añadir 3 elementos usando append()

vacio1 = []

vacio1.append(9)
vacio1.append(8)
vacio1.append(7)

print(vacio1)


# 6) Eliminar un elemento concreto de una lista

vacio1.remove(8)
print(vacio1)


# 7) Comprobar si un número está dentro de una lista

names1 = ["Jonathan", "Gorka","Juan"]

print("Gorka" in names1)
print("Bryan" in names1)


# =========================
# Recorrer listas con for
# =========================

names2 = ["Ana", "Luis", "Marta"]

for nombre in names2:
    print(nombre)

for nombre in names2:
    print("Hola", nombre)


# ===========================
# Recorrer listas de números
# ===========================

numeros2 = [5, 10, 15, 20]

for numero in numeros2:
    print(numero)


# =======================
# for + if (condiciones)
# =======================

numeros3 = [1, 4, 7, 10, 13, 20]

for numero in numeros3:
    if numero > 10:
        print(numero, "es mayor que 10")


# =========================
# Acumuladores
# =========================

numeros4 = [5, 10, 15, 20]

suma = 0

for numero in numeros4:
    suma = suma + numero

print("La suma total es:", suma)


# =========================
# Contadores
# =========================

contador = 0

for numero in numeros4:
    if numero > 10:
        contador = contador + 1

print("Hay", contador, "numeros mayores que 10")


# =========================
# Recorrer listas con índice (enumerate)
# =========================

names3 = ["Ana", "Luis", "Marta"]

for indice, nombre in enumerate(names3):
    print(indice, nombre)


# =========================
# Listas + funciones
# =========================

def mostrar_lista(lista):
    for elemento in lista:
        print(elemento)

nombres_funcion = ["Miriam","Chanchito","Miguel"]

mostrar_lista(nombres_funcion)


def sumar_lista(lista):
  
    suma = 0

    for numero in lista:
        suma = suma + numero
    
    return suma

numeros_funcion = [10,66,55]

resultado = sumar_lista(numeros_funcion)

print("La suma de todos los numeros es",resultado)