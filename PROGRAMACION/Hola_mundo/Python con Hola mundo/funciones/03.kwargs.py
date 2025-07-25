def get_product(**datos):                                   # Definimos la función get_product con un argumento de tipo diccionario (**kwargs)
    
    print(datos["id"], datos["nombre"])                     # Imprimimos el id y el nombre del producto se busca en el diccionario entre los []
    
get_product(id= 1, 
            nombre = "Iphone", 
            desc = "Esto es un iphone")