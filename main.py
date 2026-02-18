import time
import json
from registro import registrar, login
from cierre_sesion import cerrar_sesion
from operacion_actualizar import actualizar_persona
from operacion_quitar import quitar_persona
from parientes_info import agregar_usuario, cargar_usuarios
from listar import listado
from info_rama import listar_info_arbol

def login():
    while True:
        CorreoElectronico = input("Ingrese su direccion de correo electronico: ")
        contrasena = input("Ingrese su contrasena: ")

        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:
                emails = json.load(f)

            for u in emails:
                if u["CorreoElectronico"] == CorreoElectronico and u["contrasena"] == contrasena:
                    return u
            
            print("Usuario o contrasena incorrectos\n")
            return None
            
        except FileNotFoundError:
            print("No existe el archivo de usuarios")
            return None
        
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            return None

def menu(usuario):
    while usuario is not None:
        try:
            print("\n" + "="*50)
            print("Bienvenido al sistema")
            print("="*50)
            print("Que desea hacer: ")
            print("1. Crear un nuevo usuario")
            print("2. Anadir un familiar")
            print("3. Eliminar un familiar")
            print("4. Actualizar informacion de un familiar")
            print("5. Listar los familiares registrados")
            print("6. Ver informacion detallada de familiar")
            print("7. Salir")
            print("="*50)
            
            opcion = int(input("Ingrese su opcion: "))
            
            if opcion == 1:
                registrar()
            elif opcion == 2:
                agregar_usuario()
            elif opcion == 3:
                familiares = cargar_usuarios()
                quitar_persona(familiares)
            elif opcion == 4:
                familiares = cargar_usuarios()
                actualizar_persona(familiares)
            elif opcion == 5:
                listado()
            elif opcion == 6:
                listar_info_arbol()
            elif opcion == 7:
                cerrar_sesion()
                time.sleep(2)
                break
            else:
                print("Opcion invalida, intente de nuevo")
                
        except KeyboardInterrupt:
            print("\nSe cerro el programa forzosamente")
            print("Saliendo del programa...")
            time.sleep(2)
            break
        except ValueError:
            print("Se introdujo un valor invalido, intente de nuevo") 
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

def main():
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE ARBOL GENEALOGICO")
        print("="*50)
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesion")
        print("3. Salir")
        print("="*50)
        
        try:
            opcion = input("Seleccione una opcion: ")
            
            if opcion == "1":
                registrar()
            elif opcion == "2":
                usuario = login()
                if usuario is not None:
                    print("\nInicio de sesion exitoso\n")
                    try:
                        menu(usuario)
                    except Exception as e:
                        print(f"Se produjo un error en el menu: {e}")
                    break
            elif opcion == "3":
                print("\nSaliendo del programa...")
                time.sleep(2)
                break
            else:
                print("Opcion invalida")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()