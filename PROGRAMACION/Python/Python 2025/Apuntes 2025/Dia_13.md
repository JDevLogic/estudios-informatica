# Apuntes Día 13 - Python

Fecha: 15 de mayo de 2026

## Programación orientada a objetos

La programación orientada a objetos permite organizar el código usando clases y objetos.

Una clase funciona como un molde o plantilla.

Un objeto es algo creado a partir de una clase.

Ejemplo conceptual:

```text
Clase: Personaje
Objetos: jonathan, lucia, paladin, mago
```

## Clase

Una clase define la estructura que tendrán los objetos creados a partir de ella.

En este día hemos empezado creando una clase llamada `Personaje`.

La clase `Personaje` representa una base común para diferentes tipos de personajes.

## Objeto

Un objeto es una instancia de una clase.

Ejemplo:

```python
jonathan = Personaje("Jonathan", 70, 1)
```

En este caso, `jonathan` es un objeto creado a partir de la clase `Personaje`.

## __init__

El método `__init__` se ejecuta automáticamente cuando se crea un objeto.

Sirve para inicializar los atributos del objeto.

En este caso, se usó para guardar:

* `nombre`
* `vida`
* `nivel`

Ejemplo conceptual:

```python
def __init__(self, nombre, vida, nivel):
    self.nombre = nombre
    self.vida = vida
    self.nivel = nivel
```

## self

`self` representa al propio objeto que está ejecutando el método.

Si el objeto es `jonathan`, entonces `self` representa a `jonathan`.

Si el objeto es `lucia`, entonces `self` representa a `lucia`.

Gracias a `self`, cada objeto puede tener sus propios datos.

Ejemplo:

```python
self.nombre
self.vida
self.nivel
```

## Atributos

Los atributos son características de un objeto.

En este día hemos usado estos atributos:

* `nombre`
* `vida`
* `nivel`

Cada objeto tiene sus propios valores.

Por ejemplo, `jonathan` puede tener una vida diferente a `lucia`.

## Métodos

Los métodos son funciones que están dentro de una clase.

Representan acciones que puede realizar un objeto.

En la clase `Personaje` hemos trabajado con métodos como:

* `atacar`
* `curar`
* `recibir_daño`
* `subir_nivel`

## Pasar objetos como parámetros

Un método puede recibir otro objeto como parámetro.

Ejemplo conceptual:

```python
jonathan.atacar(lucia, 25)
```

En ese caso:

* `jonathan` ejecuta el método.
* `self` representa a `jonathan`.
* `lucia` es el objetivo.
* `25` es el daño.

Esto permite que un objeto interactúe con otro.

## Modificar atributos desde métodos

Los métodos pueden modificar los atributos del propio objeto.

Por ejemplo, el método `curar` aumenta la vida del personaje.

También el método `recibir_daño` resta vida al personaje.

Esto es importante porque los objetos pueden guardar estado.

El estado de un objeto son sus datos actuales.

Ejemplo conceptual:

```text
Jonathan empieza con 70 de vida.
Recibe daño.
Su vida cambia.
El objeto recuerda ese nuevo valor.
```

## Condición de muerte

Al comprobar si un personaje se queda sin vida, es mejor usar:

```python
if self.vida <= 0:
```

Y no solo:

```python
if self.vida == 0:
```

Porque si un personaje tiene 5 de vida y recibe 20 de daño, su vida quedaría en negativo.

Aunque no sea exactamente 0, igualmente debería considerarse sin vida.

## Herencia

La herencia permite crear una clase nueva a partir de otra clase existente.

La clase original se llama clase padre.

La nueva clase se llama clase hija.

En este día hemos usado esta estructura:

```text
Personaje
├── Guerrero
└── Mago
```

`Guerrero` hereda de `Personaje`.

`Mago` hereda de `Personaje`.

Eso significa que `Guerrero` y `Mago` pueden usar lo que ya existe en `Personaje`.

## Clase padre

La clase padre contiene lo común.

En este caso, `Personaje` contiene lo que comparten todos los personajes:

* nombre
* vida
* nivel
* atacar
* curar
* recibir daño
* subir nivel

## Clases hijas

Las clases hijas heredan de la clase padre.

Ejemplo conceptual:

```python
class Guerrero(Personaje):
```

```python
class Mago(Personaje):
```

Esto significa que `Guerrero` y `Mago` parten de la base de `Personaje`.

## Métodos propios de clases hijas

Una clase hija puede tener métodos propios.

En este caso:

* `Guerrero` tiene `ataque_especial`.
* `Mago` tiene `conjuro_fuego`.

Estos métodos no existen en todas las clases.

Pertenecen solo a la clase donde fueron definidos.

## Clases hermanas

`Guerrero` y `Mago` son clases hermanas porque ambas heredan de `Personaje`.

Pero una clase hermana no hereda los métodos propios de la otra.

```text
Personaje
├── Guerrero
└── Mago
```

Esto significa:

* `Guerrero` hereda de `Personaje`.
* `Mago` hereda de `Personaje`.
* `Guerrero` no hereda de `Mago`.
* `Mago` no hereda de `Guerrero`.

Por eso:

* Un `Mago` no puede usar `ataque_especial`, porque ese método pertenece a `Guerrero`.
* Un `Guerrero` no puede usar `conjuro_fuego`, porque ese método pertenece a `Mago`.

## AttributeError

`AttributeError` aparece cuando intentamos usar un atributo o método que un objeto no tiene.

Ejemplo conceptual:

```python
paladin.conjuro_fuego(mago)
```

Esto falla porque `paladin` es un objeto de tipo `Guerrero`, y `Guerrero` no tiene un método llamado `conjuro_fuego`.

El error sería parecido a:

```text
AttributeError: 'Guerrero' object has no attribute 'conjuro_fuego'
```

Python busca el método siguiendo la cadena de herencia.

En el caso de `paladin`:

```text
paladin -> Guerrero -> Personaje
```

Si no encuentra el método en `Guerrero` ni en `Personaje`, muestra error.

## Sobrescritura de métodos

La sobrescritura de métodos ocurre cuando una clase hija define un método con el mismo nombre que un método de la clase padre.

En este día hemos visto que `Personaje` tenía un método `atacar`.

Después, `Guerrero` y `Mago` también definieron su propia versión de `atacar`.

Esto significa que:

* Si ataca un objeto de tipo `Personaje`, se usa el método `atacar` de `Personaje`.
* Si ataca un objeto de tipo `Guerrero`, se usa el método `atacar` de `Guerrero`.
* Si ataca un objeto de tipo `Mago`, se usa el método `atacar` de `Mago`.

Python busca primero el método en la clase del propio objeto.

Si lo encuentra ahí, usa ese método.

Si no lo encuentra, busca en la clase padre.

## Idea importante sobre la forma de los métodos

Aunque se puede sobrescribir un método cambiando sus parámetros, conviene tener cuidado.

Si un método se llama igual en varias clases, lo ideal es que también se use de forma parecida.

Por ejemplo, si todos tienen un método `atacar`, sería más limpio que todos se pudieran usar de una forma similar.

Esto prepara el camino para entender mejor el polimorfismo.

## Polimorfismo

El polimorfismo permite que objetos de diferentes clases puedan usarse de la misma manera si comparten métodos con el mismo nombre y la misma forma de uso.

La idea principal es:

```text
Mismo método.
Misma forma de llamarlo.
Distinto comportamiento según la clase.
```

En este ejercicio, `Personaje`, `Guerrero` y `Mago` tienen un método llamado `atacar`.

Todos se usan igual desde fuera:

```python
objeto.atacar(objetivo)
```

Pero cada clase ejecuta ese método de forma diferente.

## Diferencia con el ejercicio anterior

Antes tenía una diferencia en la forma de llamar al método `atacar`.

En `Personaje` se usaba así:

```python
jonathan.atacar(lucia, 25)
```

Pero en `Guerrero` y `Mago` se usaba así:

```python
paladin.atacar(jonathan)
mago.atacar(paladin)
```

Eso funcionaba, pero no era tan limpio porque el mismo método no se usaba igual en todas las clases.

Para aplicar mejor el polimorfismo, se cambió el método `atacar` para que todos los objetos lo usen de la misma manera:

```python
jonathan.atacar(mago)
paladin.atacar(jonathan)
mago.atacar(paladin)
```

Ahora el daño no se pasa desde fuera, sino que cada clase decide internamente cuánto daño hace.

## Ataque en cada clase

En este ejercicio:

* `Personaje` tiene un ataque básico de 10 de daño.
* `Guerrero` tiene un ataque con espada de 25 de daño.
* `Mago` tiene un ataque mágico básico de 20 de daño.

Aunque el método se llama igual en las tres clases, cada clase tiene su propia versión.

Esto significa que Python ejecuta el método correcto según el tipo real del objeto.

## Polimorfismo con listas

Una parte importante del ejercicio fue crear una lista con objetos de diferentes clases:

```python
atacantes = [jonathan, paladin, mago]
```

La lista contiene:

* `jonathan`, que es un objeto de tipo `Personaje`.
* `paladin`, que es un objeto de tipo `Guerrero`.
* `mago`, que es un objeto de tipo `Mago`.

Aunque son objetos de clases diferentes, todos tienen el método `atacar(objetivo)`.

Por eso se puede recorrer la lista con un `for`:

```python
for atacante in atacantes:
    atacante.atacar(lucia)
```

La línea:

```python
atacante.atacar(lucia)
```

se ejecuta igual para todos, pero el resultado cambia según el objeto.

Python hace esto internamente:

```text
Si atacante es Personaje -> usa Personaje.atacar()
Si atacante es Guerrero -> usa Guerrero.atacar()
Si atacante es Mago -> usa Mago.atacar()
```

## Ventaja del polimorfismo

La ventaja del polimorfismo es que no hace falta comprobar manualmente qué tipo de objeto se está usando.

No hace falta hacer algo como:

```text
Si es Guerrero, ataca de una forma.
Si es Mago, ataca de otra forma.
Si es Personaje, ataca de otra forma.
```

En su lugar, simplemente se llama al método común:

```python
atacante.atacar(lucia)
```

Y cada clase responde a su manera.

## Resultado del ejercicio

En el ejercicio, `lucia` empieza con 80 de vida.

Después recibe ataques de:

```text
Jonathan -> 10 de daño
Paladin -> 25 de daño
Mago -> 20 de daño
```

El daño total recibido es:

```text
10 + 25 + 20 = 55
```

Por eso `lucia` termina con:

```text
80 - 55 = 25
```

Resultado final:

```text
Lucia 25 3
```

También se comprobaron otros ataques individuales:

```python
jonathan.atacar(mago)
paladin.atacar(jonathan)
mago.atacar(paladin)
```

Con esto se confirmó que cada objeto ejecuta su propia versión del método `atacar`.

## Conclusión sobre polimorfismo

El polimorfismo permite trabajar con objetos diferentes de forma común.

La idea clave es:

```text
No pregunto qué tipo de objeto es.
Solo llamo al método común.
Cada clase responde a su manera.
```

En este ejercicio he aprendido que varios objetos pueden compartir el mismo método `atacar`, usarse con la misma estructura y tener comportamientos diferentes según la clase.

Esto hace que el código sea más limpio, más flexible y más fácil de ampliar.
