class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con 10 de daño.")
        objetivo.recibir_daño(10)

    def curar(self):
        print(f"{self.nombre} se cura 10 puntos.")
        self.vida += 10

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} te quedaste sin vida. MORISTE.")

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        print(
            f"Subiste de nivel {self.nombre} y te curaste 20 puntos de vida adicionales."
        )


class Guerrero(Personaje):
    def atacar(self, objetivo):
        print(f"{self.nombre} golpea con la espada a {objetivo.nombre} con 25 de daño.")
        objetivo.recibir_daño(25)

    def ataque_especial(self, objetivo):
        print(
            f"{self.nombre} golpea con la espada de Excalibur a {objetivo.nombre} con 40 de daño."
        )
        objetivo.recibir_daño(40)


class Mago(Personaje):
    def atacar(self, objetivo):
        print(
            f"{self.nombre} lanza un conjuro basico a {objetivo.nombre} con 20 de daño."
        )
        objetivo.recibir_daño(20)

    def conjuro_fuego(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con 30 de daño.")
        objetivo.recibir_daño(30)


jonathan = Personaje("Jonathan", 70, 1)
paladin = Guerrero("Paladin", 1000, 50)
lucia = Personaje("Lucia", 80, 3)
mago = Mago("Mago", 500, 30)

atacantes = [jonathan, paladin, mago]

for atacante in atacantes:
    atacante.atacar(lucia)


jonathan.atacar(mago)
paladin.atacar(jonathan)
mago.atacar(paladin)

print(jonathan.nombre, jonathan.vida, jonathan.nivel)
print(paladin.nombre, paladin.vida, paladin.nivel)
print(mago.nombre, mago.vida, mago.nivel)
print(lucia.nombre, lucia.vida, lucia.nivel)
