lista1 = [1,2,3,4]

# print (1,2,3,4)                   # imprime la lista

# print(*lista)                     # imprime los elementos de la lista 

lista2 = [5,6]

combinada = [*lista1, *lista2]

print(combinada)                    # imprime la lista combinada

# Con los diccionarios se puede hacer lo mismo pero con doble asterisco

punto1 = {"x": 19, "y": "hola"}     # No imprime el "y" porque se sobrescribe con el segundo diccionario
punto2 = {"y": 15}

nuevoPunto = {**punto1, **punto2}

print(nuevoPunto)                   # imprime el nuevo punto