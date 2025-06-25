import dataclasses

class Coche:
    def __init__(self, marca:str, modelo:str, color:str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.conductor = None

    def mostrar_nombre_conductor(self):
        if self.conductor == None:
            print("No hay nadie al volante")
        else:
            print(f"El {self.marca} {self.modelo} lo conduce {self.conductor.nombre}")

@dataclasses.dataclass
class Conductor:
    nombre: str
    edad : int
    carnet: bool

    def conducir(self, coche:Coche):
        if self.carnet == True:
            coche.conductor = self
        else:
            print("No puedes conducir sin carnet")


Ibiza = Coche("Seat", "Ibiza", "Amarillo")
Pedro = Conductor("Pedro", edad=20, carnet=True)

Pedro.conducir(Ibiza)

Ibiza.mostrar_nombre_conductor()