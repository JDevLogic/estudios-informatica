mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]

print(mascotas[0])
mascotas[0] = "Bicho"               # Cambia el primer elemento de la lista

print(mascotas)
print(mascotas[2:])                 # Imprime los elementos desde la posición 2 hasta el final
print(mascotas[-1])                 # Imprime el último elemento de la lista
print(mascotas[1:2:2])              # Imprime los elementos en posiciones impares


numeros = list(range(21))           # Crea una lista de números del 0 al 20

print(numeros[::2])                 # Imprime los elementos en posiciones pares
print(numeros[1::2])                # Imprime los elementos en posiciones impares