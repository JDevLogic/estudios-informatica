numeros = (1, 2, 3,) + (4, 5, 6)                    # Tupla de numeros
print(numeros)                                      # Imprime la tupla (1, 2, 3)

punto = tuple ([1, 2])                              # Convierte una lista en una tupla 
print(punto)                                        # Imprime la tupla (1, 2)

menosNumeros = numeros[:2]                          # Crea una nueva tupla con los primeros dos elementos de la tupla numeros
print(menosNumeros)                                 # Imprime la tupla (1, 2)

primero , segundo, *otros = numeros                 # Desempaqueta la tupla numeros en tres variables
print(primero, segundo, otros)

for n in numeros:
    print(n)                                        # Imprime cada elemento de la tupla numeros

listaNumeros = list(numeros)                        # Forzamos a convertir la tupla en una lista

listaNumeros[0] = "Chanchito feliz"                 # Cambiamos el primer elemento de la lista

print(listaNumeros)                                 # Imprime la lista con el primer elemento cambiado
