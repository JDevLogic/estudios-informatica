mascotas = [                                # Crear una lista de mascotas
    "Wolfgang", 
    "Pelusa",
    "Pulga",
    "Felipe" ,
    "Chanchito feliz"
]

mascotas.insert(1, "Melvin")                # Agregar un elemento en la posición 1
mascotas.append("Chanchito triste")         # Agregar un elemento al final de la lista

mascotas.remove("Pulga")                    # Eliminar un elemento por su valor
mascotas.pop(1)                             # Eliminar un elemento por su índice
del mascotas[0]                             # Otra forma de eliminar un elemento por su índice del de delete 
mascotas.clear()                            # Eliminar todos los elementos de la lista clear de limpiar

print(mascotas)                             # Imprimir la lista de mascotas   