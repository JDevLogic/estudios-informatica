# set significa grupo o conjunto 
primero = {1,1,2,2,3,4}

segundo = {3, 4, 5}

segundo = set (segundo)                            # Convierte la lista en un set

print( primero | segundo)                          # Esto | se llama union, une los dos sets

print( primero & segundo)                          # Esto & se llama interseccion, muestra los elementos que tienen en comun

print( primero - segundo)                          # Esto - se llama diferencia, muestra los elementos que tiene el primero y no el segundo

print( primero ^ segundo)                          # Esto ^ se llama diferencia simetrica, muestra los elementos que no tienen en comun

# Los sets estan desordenados, por lo que no se pueden acceder a los elementos por su indice

if 5 in segundo:
    print("Hola mundo")
