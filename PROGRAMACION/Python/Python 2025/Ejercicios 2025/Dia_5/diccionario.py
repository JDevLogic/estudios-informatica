# Es una colección de datos donde cada dato tiene una clave (key) y un valor (value) 
# Permite acceder rápido al dato usando la clave

persona = {                                       # Creamos una variable donde estaran las claves y valores se ponen "{" al principio y al final "}"

    "nombre" : "Jonathan",                        # En este caso haremos los datos de una persona 
    "edad" : 21,                                  # IMPORTANTE al cada clave y valor dentro del diccionario debe ir separado por comas
    "altura" : 1.73,
    "es programador" : True
}

persona["edad"] = 22                                               # Para modificar se pone la variable donde esta el dato que queremos modificar, entre [] donde esta el valor que queremos modificar = y el dato modificado 

persona ["profesion"] = "Desarrollador Backed"                     # Al igual que en las listas para añadir algo pones entre [] lo nuevo despues el valor 

del persona ["altura"]                                             # Para borrar alguna clave se pone del el nombre de la variable donde esta y entre [] lo que queremos borrar


print (persona["nombre"])                                          # Esto es para imprimir cualquier clave entre () la variable donde esta y entre [] la clave que quieres imprimir 
print (persona["edad"])

 
for dato,detalle in persona.items():         # Para que recorra todo los datos se debera poner el nombre y seguido .items () que lo que hace es recorrer clave y valor a la vez es lo mas efectivo y los () para que se pueda ejecutar
    print(dato,":",detalle)                  # Poner nombre claro a las variables para evitar confusiones al poner . items ya sabe que clave es lo primero y el valor segundo 
