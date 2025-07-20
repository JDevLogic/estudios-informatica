punto = {"x": 10, "y": 20}

print (punto)
print (punto["x"])                              # Al no ser un set ni lista se accede a los elementos por su clave
print (punto["y"])                  

punto["z"] = 30                                 # Se pueden agregar elementos al diccionario
print (punto)

#print (punto, punto["lala"])                    # Si no existe la clave, se genera un error

if "lala" in punto:                             # Se puede comprobar si existe la clave 
    print("Encontre lala", punto["lala"])       # Ponemos punto "lala" para que imprima el valor

print(punto.get("x"))                           # Con el método get se puede acceder a la clave sin que genere error 
print(punto.get("lala"))                        # Si no existe la clave, devuelve None

del punto["x"]                                  # Se puede eliminar un elemento del diccionario

del (punto["y"])                                # Son formas de eliminar un elemento

print (punto)

punto["x"] = 10                                 # Se puede volver a agregar el elemento

for valor in punto:                             # Se puede recorrer el diccionario
    print(valor, punto[valor])                  # Se puede acceder al valor y a la clave

for valor in punto.items():              # Se puede recorrer el diccionario con clave y valor
    print (valor)                         # Se puede acceder al valor y a la clave


for llave, valor in punto.items(): 
    print (llave, valor)

usuarios = [                                # Se puede crear una lista de diccionarios  
                                            # El id debe de ser único
{"id": 1, "nombre": "Chanchito"},
{"id": 2, "nombre": "Feliz"},
{"id": 3, "nombre": "Nicolas"},
{"id": 4, "nombre": "Felipe"},

]

for usuario in usuarios:
    print (usuario["nombre"])                # Se puede acceder al valor de la clave nombre