from __future__ import annotations
import os
import json
from abc import ABC, abstractmethod
from typing import Protocol, List, Dict, Optional

# ——— Interfaces / Protocolos —————————————————————————————————————————————
class IDataStore(Protocol):
    """Abstracción para persistencia de datos."""
    def load(self) -> Dict[str, dict]: ...
    def save(self, data: Dict[str, dict]) -> None: ...

# ——— Implementaciones de IDataStore ——————————————————————————————————————
class JsonDataStore(IDataStore):
    """Implementa IDataStore usando un fichero JSON."""
    def __init__(self, path: str):
        self._path = path

    def load(self) -> Dict[str, dict]:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save(self, data: Dict[str, dict]) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

# ——— Modelo de Dominio ———————————————————————————————————————————————
class Inquilino:
    def __init__(self, dni: str, nombre: str):
        self.dni = dni
        self.nombre = nombre

    def to_dict(self) -> dict:
        return {"dni": self.dni, "nombre": self.nombre}

    @staticmethod
    def from_dict(d: dict) -> Inquilino:
        return Inquilino(dni=d["dni"], nombre=d["nombre"])

class Vivienda:
    def __init__(self, num_catastro: str, ciudad: str, direccion: str):
        self.num_catastro = num_catastro
        self.ciudad = ciudad
        self.direccion = direccion
        self._inquilinos: List[Inquilino] = []

    @property
    def inquilinos(self) -> List[Inquilino]:
        return list(self._inquilinos)  # inmutable desde fuera

    def add_inquilino(self, inq: Inquilino) -> None:
        if any(i.dni == inq.dni for i in self._inquilinos):
            raise ValueError(f"Inquilino {inq.dni} ya existe.")
        self._inquilinos.append(inq)

    def remove_inquilino(self, dni: str) -> None:
        original = len(self._inquilinos)
        self._inquilinos = [i for i in self._inquilinos if i.dni != dni]
        if len(self._inquilinos) == original:
            raise KeyError(f"No existe inquilino con DNI {dni}.")

    def to_dict(self) -> dict:
        return {
            "ciudad": self.ciudad,
            "direccion": self.direccion,
            "inquilinos": [i.to_dict() for i in self._inquilinos]
        }

    @staticmethod
    def from_dict(num_catastro: str, d: dict) -> Vivienda:
        v = Vivienda(num_catastro, d["ciudad"], d["direccion"])
        for inq_d in d.get("inquilinos", []):
            v.add_inquilino(Inquilino.from_dict(inq_d))
        return v

# ——— Gestor de Negocio ——————————————————————————————————————————————
class RentalManager:
    def __init__(self, datastore: IDataStore):
        self._ds = datastore
        self._cache: Dict[str, Vivienda] = {}

    def _load_all(self) -> None:
        raw = self._ds.load()
        self._cache = {
            nc: Vivienda.from_dict(nc, d)
            for nc, d in raw.items()
        }

    def _persist(self) -> None:
        serialized = {
            nc: v.to_dict()
            for nc, v in self._cache.items()
        }
        self._ds.save(serialized)

    def list_viviendas(self) -> List[Vivienda]:
        self._load_all()
        return list(self._cache.values())

    def list_inquilinos(self, num_catastro: str) -> List[Inquilino]:
        self._load_all()
        if num_catastro not in self._cache:
            raise KeyError("Vivienda no encontrada.")
        return self._cache[num_catastro].inquilinos

    def create_vivienda(self, num_catastro: str, ciudad: str, direccion: str) -> None:
        self._load_all()
        if num_catastro in self._cache:
            raise KeyError("Ya existe esa vivienda.")
        self._cache[num_catastro] = Vivienda(num_catastro, ciudad, direccion)
        self._persist()

    def add_inquilino(self, num_catastro: str, dni: str, nombre: str) -> None:
        self._load_all()
        if num_catastro not in self._cache:
            raise KeyError("Vivienda no encontrada.")
        self._cache[num_catastro].add_inquilino(Inquilino(dni, nombre))
        self._persist()

    def remove_inquilino(self, num_catastro: str, dni: str) -> None:
        self._load_all()
        if num_catastro not in self._cache:
            raise KeyError("Vivienda no encontrada.")
        self._cache[num_catastro].remove_inquilino(dni)
        self._persist()

# ——— Interfaz de Usuario (CLI) —————————————————————————————————————————
class CLI:
    def __init__(self, manager: RentalManager):
        self.mgr = manager

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pause(self):
        input("\nPulsa Enter para continuar...")

    def run(self):
        menu = (
            "\nQué deseas hacer:\n"
            "1- Listar viviendas\n"
            "2- Mostrar inquilinos de una vivienda\n"
            "3- Añadir nueva vivienda\n"
            "4- Añadir nuevo inquilino\n"
            "5- Borrar un inquilino\n"
            "6- Salir\n"
            "Opción: "
        )
        while True:
            self.clear()
            opcion = input(menu)
            try:
                if opcion == "1":
                    for v in self.mgr.list_viviendas():
                        print(f"{v.num_catastro}: {v.ciudad}, {v.direccion}")
                elif opcion == "2":
                    nc = input("Catastro: ")
                    for i in self.mgr.list_inquilinos(nc):
                        print(f"{i.dni} — {i.nombre}")
                elif opcion == "3":
                    nc = input("Catastro: ")
                    ciudad = input("Ciudad: ")
                    direc = input("Dirección: ")
                    self.mgr.create_vivienda(nc, ciudad, direc)
                    print("Vivienda creada.")
                elif opcion == "4":
                    nc = input("Catastro: ")
                    dni = input("DNI: ")
                    nombre = input("Nombre: ")
                    self.mgr.add_inquilino(nc, dni, nombre)
                    print("Inquilino añadido.")
                elif opcion == "5":
                    nc = input("Catastro: ")
                    dni = input("DNI del inquilino a borrar: ")
                    self.mgr.remove_inquilino(nc, dni)
                    print("Inquilino borrado.")
                elif opcion == "6":
                    break
                else:
                    print("Opción no válida.")
            except Exception as e:
                print(f"¡Error! {e}")
            self.pause()

# ——— Punto de entrada —————————————————————————————————————————————————
if __name__ == "__main__":
    DB_PATH = "json_db.json"
    datastore = JsonDataStore(DB_PATH)             # ⇦ Inyección de dependencia
    manager = RentalManager(datastore)             # ⇦ Manager de negocio
    cli = CLI(manager)                             # ⇦ Capa de presentación
    cli.run()
