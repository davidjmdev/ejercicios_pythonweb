from __future__ import annotations
import os
import json

ruta_DB = "json_db.json"

class Inquilino:
    def __init__(self, DNI:str, nombre:str, vivienda:Vivienda):
        self.DNI = DNI
        self.nombre = nombre
        self.vivienda = vivienda

class Vivienda:
    def __init__(self, num_catastro:int, ciudad:str, direccion:str, inquilinos:list):
        self.num_catastro = num_catastro
        self.ciudad = ciudad
        self.direccion = direccion
        self.inquilinos = inquilinos

    def añadir_inquilino(self, inquilino:Inquilino):
        self.inquilinos.append(inquilino)
    
    def borrar_inquilino(self, inquilino:Inquilino):
        self.inquilinos.pop(inquilino)


class json_DB:
    def __init__(self, ruta:str):
        self.ruta = ruta
    
    def cargar(self) -> dict:
        try:
            with open(self.ruta, "r") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return {}

    def guardar(self, dict_json:dict):
        with open(self.ruta, "w") as archivo:
            json.dump(dict_json, archivo)



def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def nueva_vivienda(num_catastro:str, ciudad:str, direccion:str, db:json_DB):
    dict_json = db.cargar()
    dict_json[num_catastro] = {"ciudad":ciudad, "direccion":direccion, "inquilinos":[]}
    db.guardar(dict_json)

def consultar_viviendas(db:json_DB):
    dict_viviendas = db.cargar()
    limpiar_pantalla()
    print(dict_viviendas)

def consultar_inquilinos(db:json_DB):
    dict_viviendas = db.cargar()
    limpiar_pantalla()
    vivienda = int(input("Introduce el número de catastro de la vivienda que deseas consultar"))
    print(dict_viviendas[vivienda]["inquilinos"])

menu = """Qué desesas hacer:
1- Consultar las viviendas disponibles
2- Consultar los inquilinos de una vivienda
3- Añadir una nueva vivienda
4- Añadir un nuevo inquilino
5- Borrar un inquilino
6- Salir

"""

opcion = 0

while opcion != 6:
    limpiar_pantalla()
    try:
        opcion = int(input(menu))
    except ValueError:
        print("Opción no valida")
        input()
        continue
    
    if opcion == 1:
        db = json_DB(ruta_DB)
        consultar_viviendas(db)
        input()
    elif opcion == 2:
        db = json_DB(ruta_DB)
        consultar_inquilinos(db)
        input()
    elif opcion == 3:
        num_catastro = input("Introduce el número del catastro: ")
        ciudad = input("Introduce la ciudad: ")
        direccion = input("Introduce la dirección: ")

        db = json_DB(ruta_DB)
        nueva_vivienda(num_catastro, ciudad, direccion, db)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    else:
        print("Opción no valida")
        input()


