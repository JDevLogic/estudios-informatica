"""
Ejercicio 5 — todo junto

Crea una función hacer_pedido que reciba:

Un nombre de cliente
Cualquier cantidad de productos
Cualquier cantidad de opciones extra (direccion, descuento, urgente...) 

"""

def hacer_pedido(nombre,*productos, **opciones):
    print(f"Cliente: {nombre}")

    print(f"Productos: {', '.join(productos)}")

    print(f"Opciones:")

    for clave, valor in opciones.items():
        print(f"- {clave}: {valor}")
    
# Ejemplo de uso:
hacer_pedido("Jonathan", "camiseta", "pantalón", "zapatillas", direccion="Bilbao", descuento=10, urgente=True)