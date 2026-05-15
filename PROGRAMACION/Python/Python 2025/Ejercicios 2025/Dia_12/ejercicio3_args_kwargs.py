""" 

Ejercicio 3 — combinando *args y **kwargs

Crea una función crear_perfil que reciba un nombre, luego cualquier cantidad de hobbies,
y luego cualquier cantidad de datos extra. 

"""

def crear_perfil(nombre, *hobbies,**datos_extra):
    print(f"Nombre: {nombre}.")
    print(f"Hobbies: {', '.join(hobbies)}")
    
    print(f"Datos extra:")
    
    for clave,valor in datos_extra.items():
        print(f"-{clave}:{valor}")

# Ejemplo de uso:
crear_perfil("Jonathan", "programar", "leer", ciudad="Bilbao", edad=20)