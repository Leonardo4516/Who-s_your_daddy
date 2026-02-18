import json
import os
from id import generar_id

ARCHIVO = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def registrar():
    print("\n=== REGISTRO ===")
    nombre = input("Nombre completo: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio")
        return
    
    correo = input("Correo electronico: ").strip()
    if not correo:
        print("El correo no puede estar vacio")
        return
    
    contrasena = input("Contrasena: ").strip()
    if not contrasena:
        print("La contrasena no puede estar vacia")
        return
    
    usuarios = cargar_usuarios()
    
    for usuario in usuarios:
        if usuario.get("CorreoElectronico") == correo:
            print("Ese correo ya esta registrado")
            return
    
    nuevo_usuario = {
        "id": generar_id(usuarios),
        "nombre": nombre,
        "CorreoElectronico": correo,
        "contrasena": contrasena
    }
    
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print(f"Usuario registrado con exito. ID: {nuevo_usuario['id']}\n")

def login():
    usuarios = cargar_usuarios()
    print("\n=== INICIO DE SESION ===")
    correo = input("Correo electronico: ").strip()
    contrasena = input("Contrasena: ").strip()
    
    for usuario in usuarios:
        if usuario.get("CorreoElectronico") == correo and usuario.get("contrasena") == contrasena:
            print("Bienvenido", usuario["nombre"])
            return usuario
    
    print("Datos incorrectos")
    return None