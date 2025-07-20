numeros = [523, 329, 323, 231, 455, 666]

#numeros.sort(reverse = True)                             # Ordena la lista de menor a mayor
numeros2 = sorted(numeros, reverse = True)                # Ordena la lista de menor a mayor
print(numeros)                                            # Imprime la lista original
print(numeros2)                                           # Imprime la lista modificada con shorted ya que no modifica la original


usuarios = [
    ["Chanchito",4],
    ["Felipe",1],
    ["Pulga",5]
]


usuarios.sort(key=lambda el: el[1] , reverse= True)                        
print(usuarios)                                           