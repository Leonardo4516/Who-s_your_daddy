import json
import os

ARCHIVO = "parientes.json"

def cargar_usuarios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def agregar_usuario():
    print("======================================")
    nombre = input("Ingrese el nombre del pariente: ")
    edad = int(input("Ingrese la edad del pariente: "))
    parentesco = input("Ingrese el parentesco del pariente: ")
    censos = input("Ingrese información sobre censos (si aplica): ")
    matrinonio = input("Ingrese información sobre certificado de matrimonio (si aplica): ")
    muerte = input("Ingrese información sobre certificado de muerte (si aplica): ")
    parroquiales = input("Ingrese información sobre registros parroquiales (si aplica): ")
    usuarios = cargar_usuarios()
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "parentesco": parentesco,
        "info" : {
            "censos" : censos,
            "certificado de matrimonio" : matrinonio,
            "certificado de muerte" : muerte,
            "registros parroquiales" : parroquiales
        }
    }
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    print("Pariente agregado exitosamente.")

agregar_usuario()
