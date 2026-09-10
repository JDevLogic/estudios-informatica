#=============================
# TUPLAS(Fundamentos)
# ============================

# Una tupla es una estructura de datos similar a una lista,
# pero es INMUTABLE (no se puede modificar).

numeros = (1,2,3,4)
nombres = ("Luis", "Miguel","Bryan")

print(numeros)
print(nombres)


# Esto NO se puede hacer en una tupla porque es inmutable
# numeros[0] = 10

# Acceso por índice (igual que en listas)

print(numeros[0])
print(nombres[1])


# Longitud de una tupla

print(len(numeros))
print(len(nombres))


# Recorrer una tupla con for

for numero in numeros:
    print(numero)

for nombre in nombres:
    print(nombre)


# Las tuplas se usan mucho para:
# - Retornos múltiples de funciones
# - Desempaquetado de valores
# - Datos que no deben cambiar (coordenadas, configuraciones, resultados)



# =========================
# Desempaquetado de tuplas
# =========================

coordenadas = (10, 20)

x, y = coordenadas

print(x)
print(y)


persona = ("Jonathan", 22, "Bilbao")

nombre, edad, ciudad = persona

print(nombre)
print(edad)
print(ciudad)

