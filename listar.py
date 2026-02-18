import json

def listado():
    print("\n[FORMATO JSON]")
    try:
        with open("parientes.json","r", encoding="utf-8") as archivo_json:
            datos = json.load(archivo_json)
            for contact in datos:
                print(f"""
                      =====================================
                      Nombre: {contact['nombre']}
                      Parentesco: {contact['parentesco']}
                      Edad: {contact['edad']}
                      =====================================
                      """)
    except FileNotFoundError:
        print("El archivo JSON aun no existe.")
    except Exception as e:
        print(f"Error inesperado en lectura de JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al leer el archivo JSON: {e}")