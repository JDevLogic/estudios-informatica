# Retorno múltiple de funciones
# -----------------------------

# En Python, una función puede devolver varios valores (tupla).

# Ejemplo conceptual:
#   def dividir(a, b):
#       # devuelve cociente y resto
#       return cociente, resto
# Uso:
#   q, r = dividir(10, 3)

# Buenas prácticas:
# - Documentar con docstring el significado de cada valor.

# EJERCICIOS DEL DÍA
# 1) Crear una función 'estadisticas(lista_numeros)' que devuelva:
#    - mínimo, máximo y promedio (en ese orden).
#    - Si la lista está vacía, devolver (None, None, None).
#    - Pruébala con varias listas y desempaca los valores.

def estadisticas(lista_numeros):
    if not lista_numeros:
        return None, None, None
    
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    promedio = sum(lista_numeros) / len(lista_numeros)
    
    return minimo, maximo, promedio

print(estadisticas([4,8,11]))
print(estadisticas([4]))
print(estadisticas([]))


# 2) Crear una función 'dividir(a, b)' que devuelva:
#    - (True, cociente, resto) si b != 0
#    - (False, "División por cero") si b == 0
#    - Demuestra el uso con desempaquetado y con ignorar valores que no uses.

def dividir(a,b):
    if b == 0:
        return False, None, "Division por cero"
    else:
        return True ,a // b , a % b 
    
verificacion, cociente, resto = dividir(10,0)
print(verificacion, cociente , resto)


# 3) Crear una función 'buscar_usuario(usuarios, username)' donde 'usuarios' sea
#    una lista de diccionarios {'user': '...', 'edad': 22}.
#    - Si existe, devolver (True, usuario_dict)
#    - Si no, devolver (False, "No encontrado")
#    - Pruébala y maneja las dos ramas (éxito/error).

def buscar_usuario(usuarios,username):
    for usuario in usuarios:
        if usuario ["user"] == username:
            return True, usuario
    return False, "No encontrado"

usuarios = [
    {"user": "Jonathan", "edad": 22},
    {"user": "Bryan", "edad": 12},
    {"user": "Miriam", "edad": 49}
]

print(buscar_usuario(usuarios, "Jonathan"))
print(buscar_usuario(usuarios, "Bryan"))
print(buscar_usuario(usuarios, "Miriam"))
print(buscar_usuario(usuarios, "Manuel"))


# 4) (Opcional) 'normalizar_vector(x, y)':
#    - Devuelve (magnitud, x_norm, y_norm)
#    - Si la magnitud es 0, devolver (0.0, 0.0, 0.0)
#    - Úsalo para practicar retorno múltiple + guard clause.

import math

def normalizar_vector(x, y):

    magnitud = math.sqrt(x**2 +y**2)

# ------ Guard clause ------
    if magnitud == 0:
        return 0.0, 0.0, 0.0
# -----------------------------

    x_norm = x / magnitud
    y_norm = y / magnitud

    return magnitud, x_norm, y_norm
    
print(normalizar_vector(3,4))

