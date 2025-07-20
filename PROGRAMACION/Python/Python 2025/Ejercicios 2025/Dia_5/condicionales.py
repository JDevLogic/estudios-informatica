# Repaso y ampliación de condicionales (vistos en Día 2)

inventario = {                    # Creamos un diccionario con el inventario no olvidarse de los {} y de las comas al final de cada clave
    "manzana" : 0.5,
    "pan" : 1.2,
    "leche" : 0.9,
    "huevo" : 0.2,
}

producto = input("Introduce el nombre del producto: ").lower()                        # Aqui creamos una variable que producto sea lo que escriba el usuario y luego buscarlo se pone .lower() para que no haya problemas con mayus lower lo pone todo en minus lo que escriba 

if producto in inventario:                                                            # Creamos una condicion para que busque el producto en el inventario 
    precio = inventario[producto]
    print (f"El producto {producto} esta disponible y cuesta {precio}€")              # Este es el mensaje que sera si esta disponible y su valor se pone inventario[producto] para saber el precio del producto que se pidio solo devuelve el valor
                                                                                      # Mejora para que se vea mas claro puse que inventario[producto] se llame precio asi se sabe que es 

else:
    print ("El producto no esta disponible")                                          # Un else por si el producto introducido no este saldra este mensaje 
