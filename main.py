import time
import json
from funciones import registrar, agregar_usuario, quitar_persona, actualizar_persona, cargar_usuarios, listado

def login():
    while True:
        CorreoElectronico = input("Ingrese su direccion de correo electronico: ")
        contraseña = input("Ingrese su contraseña: ")

        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:
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

def menu(usuario):
    while usuario is not None:
        try:
            print("bienvenido al sistema")
            print("que desea hacer: ")
            print("1. crear un nuevo usuario")
            print("2. añadir un familiar")
            print("3. eliminar un familiar")
            print("4. actualizar informacion de un familiar")
            print("5. listar los usuarios registrados")
            print("6. listar los familiares registrados")
            print("7. salir")
            opcion=int(input("ingrese su opcion: "))
            if opcion==1:
                funciones.registrar()
            if opcion==2:
                funciones.agregar_usuario()
            if opcion==3:
                funciones.quitar_persona()
            if opcion==4:
                funciones.actualizar_persona()
            if opcion==5:
                funciones.cargar_usuarios()
            if opcion==6:
                funciones.listado()
            if opcion==7:
                print("saliendo del programa...")
                time.sleep(3)
                break
            else:
                print("opcion invalida, intente de nuevo")
        except KeyboardInterrupt:
            print("se cerro el programa forzozamente")
            print("saliendo del programa...")
            time.sleep(3)
        except ValueError:
            print("se introdujo un valor invalido intente de nuevo") 
        except Exception as e:
            print(f"ocurrio un error inesperado: {e}")

def main():
    while True:
        usuario = login()

        if usuario is None:
            print("Usuario o contraseña incorrectos\n")
            continue  # vuelve a pedir credenciales

        print("\nInicio de sesión exitoso\n")

        try:
            menu(usuario)
        except Exception as e:
            print(f"Se produjo un error en el menú: {e}")

        break  # termina el programa cuando el usuario sale del menú

if __name__ == "__main__":
    main()

