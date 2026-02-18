import json
import os
from id import generar_id

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
    print("\n======================================")
    print("    AGREGAR FAMILIAR")
    print("======================================")
    
    nombre = input("Ingrese el nombre del pariente: ")
    
    try:
        edad = int(input("Ingrese la edad del pariente: "))
    except ValueError:
        print("Edad invalida, se establecera en 0")
        edad = 0
    
    parentesco = input("Ingrese el parentesco del pariente: ")
    censos = input("Ingrese informacion sobre censos (si aplica): ")
    matrimonio = input("Ingrese informacion sobre certificado de matrimonio (si aplica): ")
    muerte = input("Ingrese informacion sobre certificado de muerte (si aplica): ")
    parroquiales = input("Ingrese informacion sobre registros parroquiales (si aplica): ")
    
    usuarios = cargar_usuarios()
    
    usuario = {
        "id": generar_id(usuarios),
        "nombre": nombre,
        "edad": edad,
        "parentesco": parentesco,
        "info": {
            "censos": censos if censos else "No registrado",
            "certificado de matrimonio": matrimonio if matrimonio else "No registrado",
            "certificado de muerte": muerte if muerte else "No registrado",
            "registros parroquiales": parroquiales if parroquiales else "No registrado"
        }
    }
    
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    print(f"\nPariente agregado exitosamente con ID: {usuario['id']}")