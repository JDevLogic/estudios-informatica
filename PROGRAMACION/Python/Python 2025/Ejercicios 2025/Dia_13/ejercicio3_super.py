# class Personaje:
#     def __init__(self, nombre, vida, nivel):
#         self.nombre = nombre
#         self.vida = vida
#         self.nivel = nivel


# class Guerrero(Personaje):
#     def __init__(self, nombre, vida, nivel, arma):
#         self.nombre = nombre
#         self.vida = vida
#         self.nivel = nivel
#         self.arma = arma


class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def mostrar_info(self):
        print(self.nombre, self.vida, self.nivel)


class Guerrero(Personaje):
    def __init__(self, nombre, vida, nivel, arma):
        super().__init__(nombre, vida, nivel)
        self.arma = arma

    def mostrar_info(self):
        super().mostrar_info()
        print(self.arma)


class Mago(Personaje):
    def __init__(self, nombre, vida, nivel, mana):
        super().__init__(nombre, vida, nivel)
        self.mana = mana

    def mostrar_info(self):
        super().mostrar_info()
        print(self.mana)


rey_arturo = Guerrero("Paladin", 1000, 50, "Excalibur")
mago_fuego = Mago("Axel", 800, 45, 100)

rey_arturo.mostrar_info()
mago_fuego.mostrar_info()
