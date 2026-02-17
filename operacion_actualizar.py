def actualizar_persona(personas):
    print("\n--- Actualizar información de una persona ---")
    try:
        id_str = input("Ingrese el ID de la persona a actualizar: ")
        id_actualizar = int(id_str)
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return

    persona = """buscar_persona_por_id"""(personas, id_actualizar)

    if persona is None:
        print(f"No se encontró ninguna persona con ID {id_actualizar}.")
        return

    print(f"Editando a: {persona['nombre']}")
    print("Si no desea cambiar un campo, déjelo vacío y presione Enter.\n")

    nuevo_nombre = input(f"Nuevo nombre (actual: {persona['nombre']}): ")
    nueva_fecha = input(f"Nueva fecha de nacimiento (actual: {persona.get('fecha_nacimiento', 'N/A')}): ")
    nuevos_certificados = input(f"Nuevos certificados separados por coma (actual: {', '.join(persona.get('certificados', []))}): ")

    # Actualizar solo si el usuario escribió algo
    if nuevo_nombre.strip() != "":
        persona["nombre"] = nuevo_nombre.strip()

    if nueva_fecha.strip() != "":
        persona["fecha_nacimiento"] = nueva_fecha.strip()

    if nuevos_certificados.strip() != "":
        lista_certificados = [c.strip() for c in nuevos_certificados.split(",") if c.strip() != ""]
        persona["certificados"] = lista_certificados

    print("Información actualizada correctamente.")