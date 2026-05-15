""" 

Ejercicio 2 — **kwargs

Crea una función mostrar_producto que reciba el nombre del producto y 
cualquier cantidad de detalles extra (precio, stock, categoria...) 
e imprima todo por pantalla. 

"""

def mostrar_producto(nombre,**detalles_producto):
    print (f"Producto: {nombre}.")
    for clave, valor in detalles_producto.items():
        print (f"   {clave}: {valor}")

datos = {"nombre": "Camiseta", "precio": 15.99, "color": "negro"}
mostrar_producto(**datos)


#mostrar_producto("Camiseta", precio=15.99, talla="M", color="negro")
#mostrar_producto("Portátil", precio=799, marca="Lenovo", stock=5)