# Ejercicio 1: Generar un ticket de compra

# Descripción: El objetivo de este ejercicio es crear un programa que genere e imprima un ticket de compra a partir de una lista de productos.
# Cada producto esta representado por un diccionario con un nombre y un precio. El programa debe calcular la cantidad de cada producto,
# el subtotal de cada uno y el total de la compra.

# Entrada:Una lista de diccionarios con las claves:

# • nombre(str): El nombre del producto. 

# • precio (float): El precio del producto.


productos = [   {'nombre': 'Manzana', 'precio': 0.5},
              
                {'nombre': 'Manzana', 'precio': 0.5},   

                {'nombre': 'Pan', 'precio': 1.0},  

                {'nombre': 'Leche', 'precio': 1.5}

]

def genera_ticket(productos):
    """
    
    Esta función recibe una lista de diccionarios y devuelve un ticket de compra.

    """
    
    contador_de_productos = {}
    
    total = 0

    for producto in productos:
        
        nombre = producto["nombre"]
        
        if nombre in contador_de_productos:
            contador_de_productos[nombre]['cantidad'] += 1
        
        else:
            contador_de_productos[nombre] = {'precio': producto["precio"], 'cantidad': 1}

    print ("-----------------------")

    print ("Ticket de compra")

    print ("-----------------------")

    for nombre, info in contador_de_productos.items():
        
        precio = info['precio']
        
        cantidad = info['cantidad']
        
        subtotal = precio * cantidad
        
        total += subtotal
        
        print (f"{nombre}: x {cantidad} - {precio}€ = {subtotal}€")
    
    print ("-----------------------")

    print (f"Total: {total:.2f}€")

    print ("-----------------------")

genera_ticket(productos)