# 🐍 Día 8 – Apuntes de Python  
## 📁 Archivos en Python: Lectura, Escritura y Añadir contenido

---

### 📝 Escribir en un archivo (`"w"` – write)

* El modo `"w"` (escritura) crea o sobrescribe el archivo.
* Si el archivo existe, se borra su contenido.
* Si no existe, lo crea.

```python
archivo = open("archivo.txt", "w")  # Modo escritura
archivo.write("¡Hola! Esto es una prueba.\n")  # Escribe una línea
archivo.close()  # Siempre cerrar el archivo
```

---

### 📖 Leer un archivo (`"r"` – read)

* El modo `"r"` abre el archivo solo para leer.
* Puedes leerlo completo o línea por línea.

```python
archivo = open("archivo.txt", "r")
print(archivo.read())  # Lee todo el contenido como cadena
archivo.close()
```

👉 También se puede usar `.readlines()` para obtener una lista de líneas:

```python
lineas = archivo.readlines()
```

---

### ➕ Añadir texto sin borrar (`"a"` – append)

* El modo `"a"` abre el archivo para agregar al final.
* No borra lo anterior.
* Ideal para añadir líneas sin sobrescribir.

```python
archivo = open("archivo.txt", "a")
archivo.write("Línea añadida desde append.\n")  # Agrega al final
archivo.close()
```

---

### 📌 Notas importantes

* Siempre cerrar el archivo con `.close()` para que los cambios se guarden.  
* Usar `\n` para que el texto se añada en una nueva línea.  
* En este día no usamos `with` todavía, ni `input()` (todo es con valores fijos).


