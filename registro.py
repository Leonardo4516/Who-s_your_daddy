
import json
import os

ARCHIVO = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w") as f:
        json.dump(usuarios, f)

usuarios = cargar_usuarios()

def registrar():
    global usuarios
    print("=== REGISTRO ===")
    user = input("Usuario: ")
    if user in usuarios:
        print("Ese usuario ya existe")
        return
    password = input("Contraseña: ")
    usuarios[user] = password
    guardar_usuarios(usuarios)
    print("Usuario registrado con éxito\n")

def login():
    print("=== INICIO DE SESIÓN ===")
    user = input("Usuario: ")
    password = input("Contraseña: ")
    
    if user in usuarios and usuarios[user] == password:
        print("Bienvenido", user)
    else:
        print("Datos incorrectos")

while True:
    print("\n1. Registrar")
    print("2. Iniciar sesión")
    print("3. Salir")
    
    opcion = input("Elige opción: ")
    
    if opcion == "1":
        registrar()
    elif opcion == "2":
        login()
    elif opcion == "3":
        break
