
# 🐍 Día 10 – Apuntes de Python  
## 📌 Módulos personalizados en Python

---

### 📦 ¿Qué es un módulo?

* Un módulo es cualquier archivo `.py` que contiene funciones y que puedes reutilizar en otros archivos.
* Se usa para **organizar el código** y **evitar repeticiones**.

### 🧩 Importar funciones desde un módulo

```python
from nombre_modulo import funcion1, funcion2
```

---

### ✅ Crear un módulo (`utilidades.py`)

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2
```

---

### 📌 Usar funciones importadas desde otro archivo

Creamos otro archivo (por ejemplo, `usar_utilidades.py`) y usamos las funciones definidas anteriormente:

```python
from utilidades import saludar, sumar, restar
```

---

### 🔄 Menú interactivo con funciones de un módulo

* Creamos un menú con `while True` que permite al usuario elegir entre varias opciones.  
* Reutilizamos las funciones desde otro archivo importado.  
* Podemos importar librerías externas como `datetime` y usarlas junto a nuestras funciones.

---

## 🧪 Proyecto final del día: Calculadora Modular

### 🎯 Menú interactivo con opciones:

* **Sumar** → usa `sumar()` del módulo  
* **Restar** → usa `restar()` del módulo  
* **Saludar** → usa `saludar()` del módulo  
* **Mostrar fecha y hora actual** → usa `datetime.now()`  
* **Salir del programa**

---

### ✅ Lo aprendido:

* Separación de **lógica (funciones)** y **control (menú)**  
* Importación correcta entre archivos  
* Uso combinado de módulos **propios y estándar**  
* Buenas prácticas: claridad, estructura y comentarios útiles

