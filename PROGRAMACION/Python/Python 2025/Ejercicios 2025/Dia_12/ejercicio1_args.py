"""

Ejercicio 1 — *args
Crea una función calcular_total que reciba cualquier cantidad 
de precios y devuelva la suma de todos. 

"""

def calcular_total(*precios):
    total = 0 
    for precio in precios:
        total += precio

    return total

# Ejemplo de uso:
print(calcular_total(10, 5, 3))                    # → 18
print (calcular_total(100, 200, 50, 25))           # → 375
print (calcular_total(9.99))                       # → 9.99
