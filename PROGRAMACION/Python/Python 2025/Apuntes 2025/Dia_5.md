# 📓 Apuntes Día 5 - Python (26 de marzo de 2025)

## 📌 Listas

Las listas son colecciones ordenadas de elementos.

* Pueden contener cualquier tipo de dato: strings, enteros, floats, booleanos, incluso otras listas.
* Se crean usando corchetes `[]` y separando los elementos con comas.

### Acceder a datos de una lista

* `lista[0]` → Primer dato.  
* `lista[-1]` → Último dato.  
* Las listas empiezan en la posición 0.

### Modificar una lista

* `lista[0] = "Nuevo valor"` → Modifica el valor en la posición 0.  
* `lista.append("dato")` → Añade un dato al final.  
* `lista.insert(1, "dato")` → Inserta en la posición 1 el dato indicado.  
* `lista.pop()` → Elimina el último dato.  
* `lista.remove("dato")` → Elimina un valor específico.

### Recorrer una lista con for

```python
for dato in lista:
    print(dato)
```

---

## 📌 Slicing (corte de listas)

Permite mostrar partes específicas de una lista:

| Ejemplo         | Significado                                  |
|-----------------|-----------------------------------------------|
| `lista[1:3]`    | Desde la posición 1 hasta la 2 (la 3 no entra) |
| `lista[:3]`     | Desde el inicio hasta la posición 2           |
| `lista[2:]`     | Desde la posición 2 hasta el final            |
| `lista[::-1]`   | Invierte la lista                             |

---

## 📌 Tuplas

* Son similares a las listas, pero **inmutables** (no se pueden modificar).
* Se crean con paréntesis `()` en vez de corchetes `[]`.
* Se accede igual que una lista: `tupla[0]`.
* Se pueden recorrer con `for` igual que una lista.

---

## 📌 Diccionarios

Colección de datos donde cada elemento tiene una **clave (key)** y un **valor (value)**.

* Se crean usando llaves `{}` y los pares clave-valor se separan por `:`.

### Ejemplo básico

```python
persona = {
    "nombre": "Jonathan",
    "edad": 21,
    "altura": 1.73,
    "es programador": True
}
```

### Operaciones básicas

* Acceder: `persona["edad"]`  
* Modificar: `persona["edad"] = 22`  
* Añadir: `persona["profesion"] = "Backend"`  
* Eliminar: `del persona["altura"]`

### Recorrer un diccionario

```python
for clave, valor in persona.items():
    print(clave, ":", valor)
```

---

## 📌 Condicionales + Diccionarios

Creamos un pequeño sistema de inventario que permite al usuario buscar productos:

```python
inventario = {
    "manzana": 0.5,
    "pan": 1.2,
    "leche": 0.9,
    "huevo": 0.2
}

producto = input("Introduce el nombre del producto: ").lower()

if producto in inventario:
    precio = inventario[producto]
    print(f"El producto {producto} está disponible y cuesta {precio} €")
else:
    print("El producto no está disponible")
```

---

## 📌 Resumen Final del Día 5

Aprendimos:

* **Listas**: acceso, modificación, slicing, recorrido.  
* **Tuplas**: inmutables, se acceden igual que listas.  
* **Diccionarios**: claves y valores, acceso, modificación y bucles.  
* Combinamos **diccionarios con condicionales** para buscar productos.  
* Consolidamos la base de **estructuras de datos** en Python.


