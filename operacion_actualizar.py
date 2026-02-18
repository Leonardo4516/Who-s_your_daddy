import json
import os

ARCHIVO = "parientes.json"

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

def buscar_persona_por_id(personas, persona_id):
    for persona in personas:
        if persona.get('id') == persona_id:
            return persona
    return None

def actualizar_persona(personas):
    print("\n--- Actualizar informacion de una persona ---")
    
    if not personas:
        print("No hay personas registradas")
        return
    
    try:
        id_str = input("Ingrese el ID de la persona a actualizar: ")
        id_actualizar = int(id_str)
    except ValueError:
        print("ID invalido. Debe ser un numero.")
        return

    persona = buscar_persona_por_id(personas, id_actualizar)

    if persona is None:
        print(f"No se encontro ninguna persona con ID {id_actualizar}.")
        return

    print(f"\nEditando a: {persona['nombre']}")
    print("Si no desea cambiar un campo, dejelo vacio y presione Enter.\n")

    nuevo_nombre = input(f"Nuevo nombre (actual: {persona['nombre']}): ")
    nueva_edad = input(f"Nueva edad (actual: {persona.get('edad', 'N/A')}): ")
    nuevo_parentesco = input(f"Nuevo parentesco (actual: {persona.get('parentesco', 'N/A')}): ")

    if nuevo_nombre.strip() != "":
        persona["nombre"] = nuevo_nombre.strip()

    if nueva_edad.strip() != "":
        try:
            persona["edad"] = int(nueva_edad.strip())
        except ValueError:
            print("Edad invalida, no se actualizo")

    if nuevo_parentesco.strip() != "":
        persona["parentesco"] = nuevo_parentesco.strip()

    guardar_usuarios(personas)
    print("\nInformacion actualizada correctamente.")