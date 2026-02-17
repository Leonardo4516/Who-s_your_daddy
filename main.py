import json

def login():
    while True:
        CorreoElectronico = input("Ingrese su direccion de correo electronico: ")
        contraseña = input("Ingrese su contraseña: ")

        try:
            with open("emails.json", "r", encoding="utf-8") as f:
                emails = json.load(f)

            for u in emails:
                if u["CorreoElectronico"] == CorreoElectronico and u["contraseña"] == contraseña:
                    return u   # ← DEVUELVE EL USUARIO COMPLETO
                    break

            return None  # no encontrado
            continue
        except FileNotFoundError:
            print("No existe el archivo de usuarios")
            return None
        
        except Exception:
            print("se produjo un error inesperado")
