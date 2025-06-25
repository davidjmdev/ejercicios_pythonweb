class Coche:
    def __init__(self, marca:str, modelo:str, color:str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.conductor = None

class Conductor:
    def __init__(self, nombre:str, edad:int, carnet:bool):
        self.nombre = nombre
        self.edad = edad
        self.carnet = carnet

    def conducir(self, coche:Coche):
        if self.carnet == True:
            coche.conductor = self
        else:
            print("No puedes conducir sin carnet")



Ibiza = Coche("Seat", "Ibiza", "Amarillo")
Pedro = Conductor("Pedro", 20, True)

Pedro.conducir(Ibiza)

print(Ibiza.conductor.nombre)