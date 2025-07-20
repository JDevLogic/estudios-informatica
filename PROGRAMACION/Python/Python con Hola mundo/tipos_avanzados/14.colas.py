pila = []

pila.append(1)
pila.append(2)
pila.append(3)

print(pila)                           # Imprime la pila

ultiElemento = pila.pop()             # Elimina el último elemento
print(ultiElemento)                   # Imprime el último elemento eliminado 

print(pila)                           # Imprime la pila después de eliminar el último elemento

print(pila[-1])                       # Imprime el último elemento de la pila sin eliminarlo

pila.pop()                            # Elimina el últimos elemento
pila.pop()                            # Elimina el últimos elemento

if not pila:                          # Verifica si la pila está vacía
    print("La pila está vacía")

