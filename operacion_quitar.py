def quitar_persona(personas):
    print("\n--- Quitar persona del árbol ---")
    try:
        id_str = input("Ingrese el ID de la persona a eliminar: ")
        id_eliminar = int(id_str)
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return

    persona = """buscar_persona_por_id """(personas, id_eliminar)

    if persona is None:
        print(f"No se encontró ninguna persona con ID {id_eliminar}.")
        return

    # Confirmación
    print(f"Se encontró: {persona['nombre']}")
    confirmar = input("¿Está seguro que desea eliminarla? (s/n): ").lower()

    if confirmar == "s":
        # Eliminar de la lista
        personas.remove(persona)
        print("Persona eliminada correctamente.")
    else:
        print("Operación cancelada.")