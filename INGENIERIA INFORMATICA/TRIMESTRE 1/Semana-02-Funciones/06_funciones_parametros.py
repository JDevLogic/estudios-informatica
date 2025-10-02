# Funciones con parámetros por defecto y valores opcionales
# Una función puede tener valores por defecto en sus parámetros.
# Si el usuario no pasa ese valor, Python usará el que hemos definido.
# Esto permite que las funciones sean más flexibles y fáciles de usar.


# Ejemplos teóricos:
def saludar(nombre="invitado"):
     return f"Hola {nombre}"

def potencia(base, exponente=2):
     return base ** exponente

# ---------------------------------------------------------
# EJERCICIOS DEL DÍA

# 1. Una función saludo(nombre="invitado") que devuelva un saludo.
#    - Si se da un nombre, lo usa.
#    - Si no se da, muestra "Hola invitado".

def saludo(nombre = "invitado"):
     return(f"Hola {nombre} .")

print (saludar("Bryan"))
print (saludar())


# 2. Una función potencia(base, exponente=2) que devuelva la base elevada al exponente.
#    - Si no se da exponente, calcula el cuadrado.

def potencias(base, exponente=2):
     return base ** exponente

print(potencias(2))
print(potencias(2,4))


# 3. Una función presentacion(nombre, edad=18, ciudad="desconocida")
#    que devuelva un mensaje como:
#    "Me llamo Jonathan, tengo 22 años y vivo en Madrid."
#    - Si no se pasa edad o ciudad, se usan los valores por defecto.

def presentacion(nombre, edad = 18, cuidad = "desconocida"):
     return (f"Me llamo {nombre}, tengo {edad} años y vivo en {cuidad}.")

print(presentacion("Lucia"))
print(presentacion("Lucia",22))
print(presentacion("Lucia",22, "Bilbao"))
