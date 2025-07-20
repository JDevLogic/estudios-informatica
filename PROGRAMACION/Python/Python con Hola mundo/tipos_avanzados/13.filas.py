from collections import deque

fila = deque([1,2])

# fila.append(3)                      # Agrega un elemento al final de la fila
# fila.append(4)
# fila.append(5)

print(fila)                         # Imprime la fila

fila.popleft()                      # Elimina el primer elemento de la fila
fila.popleft()

print(fila)                         # Imprime la fila

if not fila:                        # Verifica si la fila está vacía
    print("fila está vacía")
