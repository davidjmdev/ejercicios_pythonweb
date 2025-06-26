from __future__ import annotations
import random


class Personaje:
    def __init__(self, nombre: str, vida: int, ataque: int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self, objetivo: Personaje):
        acertar = random.choice([True, False])
        if acertar:
            print(f"{self.nombre} fue certero en el ataque.")
            objetivo.defender(self.ataque)
        else:
            print(f"{self.nombre} lanzó un ataque pero falló.")


    def defender(self, daño_recibido: int):
        print(f"{self.nombre} ha recibido {daño_recibido} de daño")
        self.vida -= daño_recibido
        if self.vida <= 0:
            print(f"{self.nombre} ha perdido.")
    
    def estado(self) -> str:
        return f"{self.nombre} tiene {self.vida} de vida"

class Mago(Personaje):
    def hechizar(self, objetivo: Personaje):
        acertar = random.choice([True, False])
        if acertar:
            print(f"{self.nombre} fue certero con el hechizo.")
            objetivo.defender(self.ataque * 2)
        else:
            print(f"{self.nombre} lanzó un hechizo pero falló.")

class Medico(Personaje):
    def __init__(self, nombre: str, vida: int, ataque:int, sanacion:int):
        super().__init__(nombre, vida, ataque)
        self.sanacion = sanacion
    
    def sanar(self, paciente:Personaje):
        paciente.vida += self.sanacion
        print(f"{self.nombre} sanó {self.sanacion} de vida a {paciente.nombre}")



superman = Personaje("Superman", 1000, 100)
rompetechos = Personaje("Rompetechos", 2000, 200)
dumbledore = Mago("Dumbledore", 300, 300)
sprout = Medico("Sprout", 200, 100, 200)

print(rompetechos.estado())

superman.atacar(rompetechos)

print(rompetechos.estado())

dumbledore.hechizar(rompetechos)

print(rompetechos.estado())

sprout.sanar(rompetechos)

print(rompetechos.estado())
