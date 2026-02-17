import time

def menu():
    while True:
        try:
            print("bienvenido al sistema")
            print("que desea hacer: ")
            print("1. crear un nuevo usuario")
            print("2. añadir un familiar")
            print("3. eliminar informacion de un familiar")
            print("4. actualizar informacion de un familiar")
            print("5. salir")
            opcion=int(input("ingrese su opcion: "))
            if opcion==1:
                pass
            if opcion==2:
                pass
            if opcion==3:
                pass
            if opcion==4:
                pass
            if opcion==5:
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

menu()