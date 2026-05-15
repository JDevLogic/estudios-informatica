# 📓 Apuntes Día 12 - Python
📅 Fecha: 15 de mayo de 2026

## ¿Qué son *args y **kwargs?

- `*args` → recibe cualquier cantidad de argumentos posicionales, los guarda en una **tupla**
- `**kwargs` → recibe cualquier cantidad de argumentos con nombre, los guarda en un **diccionario**
- El `*` y `**` son lo importante, `args` y `kwargs` son solo convención

## *args

- Se itera con `for elemento in args`
- Útil cuando no sabes cuántos valores te van a pasar

## **kwargs

- Se itera con `for clave, valor in kwargs.items()`
- Útil para opciones o configuraciones flexibles

## Orden obligatorio

def funcion(normal, *args, **kwargs)

## Unpacking al llamar funciones

- `*lista` → suelta los elementos uno a uno
- `**diccionario` → suelta los pares clave-valor

