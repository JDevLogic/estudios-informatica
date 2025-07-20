# Las listas son colecciones ordenadas de elementos.
# Pueden contener cualquier tipo de dato: strings, enteros, floats, booleanos, incluso otras listas.
# Se crean usando corchetes [] y separando los elementos con comas.


mis_datos = ["Jonathan",1.73,21,True]               # Aqui creamos la lista con el nombre de la lista y dentro entre [] se ponen los datos

print(mis_datos[1:3])                               # slicing te permite cortar y mostrar partes especificas de la lista en este caso imprime desde la posicion 1 hasta 2 (la 3 no se incluye)        
print(mis_datos[:3])                                # Este seria el orden (el primer numero por donde inicia : el segundo por donde acaba pero no se cuenta el que pones si pones 3 sera hasta el 2)
print(mis_datos[2:])                                # Este caso ponemos el inicio pero no el final asi que sera hasta el final de la lista

print(mis_datos[::2])                               # Imprime desde el principio saltando de 2 en 2 la estructura es lista [inicio:fin:step] step son los saltos que da en la lista en este caso 2
print(mis_datos[1::2])                              # Empieza en la posicion 1 y va saltando de 2 en 2 
print(mis_datos[::-1])                              # Al poner -1 recorre hacia atras la lista entonces lo que se imprimira la lista al reves 

mis_datos.append ("Desarrollador Backed")           # Para añadir un dato a la lista debes poner la lista y .append y lo que quieres agregar entre ()
mis_datos.insert (1, "Hombre")                      # Si quieres insertar un dato en una posicion en especifico debes poner entre (la posicion, el dato)
mis_datos.pop()                                     # Con .pop elimina el ultimo dato si no le pones la posicion entre ()
mis_datos.remove("Jonathan")                        # Si quieres borrar un dato en especifico pones .remove y entre () el dato que quieres eliminar

mis_datos[0] = "Desarrollador"                      # Para modificar un dato en especifico pones la posicion del dato despues = y el dato ya modificado
mis_datos[3] = False                                # Sirve para todo antes era True se puede modificar a False

for dato in mis_datos:                              # Hacemos for creamos un variable dato y recorra la lista de mis datos 
    print(dato)                                     # Aqui lo imprime uno a uno


print(mis_datos)                                    # Esto es para que imprima la lista

print(mis_datos[3])                                 # Para que imprima un dato en especifico se pone entre[] el numero del dato que quieres imprimir 
print(mis_datos[2])                           
print(mis_datos[1]) 
print(mis_datos[0])                                 # Recuerda que las listas empiezan por 0 que tambien cuenta como numero entonces 0 es el primer dato

print(mis_datos[-1])                                # Si la lista es muy larga y quieres que imprima el ultimo dato de la lista solo debes poner [-1]
