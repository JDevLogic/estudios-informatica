usuarios = [
    ["Chanchito",4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []                              # Lista vacia

# for usuario in usuarios:                               # Recorremos la lista de usuarios
#     nombres.append(usuario[0])                         # Agregamos el nombre a la lista de nombres

# print(nombres)                                         # Imprimimos la lista de nombres

# map
# nombres = [usuarios [0] for usuario in usuarios]                         # Crea una lista con los nombres (primer elemento) de cada usuario

# Filtrando la lista de usuarios - filter
#nombres = [usuario for usuario in usuarios if usuario[1] > 2]          

# Filtrar y transformar la lista de usuarios

#nombres = [usuario [0] for usuario in usuarios if usuario[1] > 2 ]        # Filtramos los usuarios con un valor menor a 2

# map
#nombres = list(map(lambda usuario: usuario[0], usuarios))                 # Usamos map para obtener los nombres de los usuarios

# filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))     # Filtramos los usuarios con un valor menor a 2 usando filter
print(menosUsuarios)
