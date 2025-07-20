# Las tuplas son igual que las listas pueden contener cualquier tipo de dato 
# La unica diferencia e importante es que son inmutables
# Se crean entre () en vez de [] como las listas

mi_tupla = ("Jonathan",1.73,21,True)              # Los datos de la tupla no se pueden modificar de ninguna manera 

print(mi_tupla)                                   # Para imprimir los datos al igual que una lista se hace entre () y el nombre de la tupla
print(mi_tupla[0])                                # Al igual que con las listas para imprimir un dato en especifico se pone entre []
print(mi_tupla[1])

#mi_tupla[0] = "JOSE"                             # Prueba de que las tuplas son inmutables 

for dato in mi_tupla:                             # Al igual que con las listas para que salgan uno a uno el dato se hace con for
    print(dato)

