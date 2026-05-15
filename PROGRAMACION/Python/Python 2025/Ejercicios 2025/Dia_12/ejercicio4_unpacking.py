""" 

Ejercicio 4 — unpacking al llamar funciones 

"""

def calcular_total(*precios):
    total = 0 
    for precio in precios:
        total += precio

    return total

precios = [10, 5, 3, 8]
print (calcular_total(*precios))



def mostrar_datos(**detalles_dato):

    for clave, valor in detalles_dato.items():
        print (f"   {clave}: {valor}")

datos = {"nombre": "Camiseta", "precio": 15.99, "color": "negro"}
mostrar_datos(**datos)