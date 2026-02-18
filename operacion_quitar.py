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

def quitar_persona(personas):
    print("\n--- Quitar persona del arbol ---")
    
    if not personas:
        print("No hay personas registradas")
        return
    
    try:
        id_str = input("Ingrese el ID de la persona a eliminar: ")
        id_eliminar = int(id_str)
    except ValueError:
        print("ID invalido. Debe ser un numero.")
        return

    persona = buscar_persona_por_id(personas, id_eliminar)

    if persona is None:
        print(f"No se encontro ninguna persona con ID {id_eliminar}.")
        return

    print(f"\nSe encontro: {persona['nombre']}")
    print(f"Parentesco: {persona.get('parentesco', 'N/A')}")
    print(f"Edad: {persona.get('edad', 'N/A')}")
    
    confirmar = input("\nEsta seguro que desea eliminarla? (s/n): ").lower()

    if confirmar == "s":
        personas.remove(persona)
        guardar_usuarios(personas)
        print("Persona eliminada correctamente.")
    else:
        print("Operacion cancelada.")