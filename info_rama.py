import os
import json

def listar_info_arbol():
    print("\n================================")
    print("  INFORMACION DETALLADA")
    print("================================")
    
    if not os.path.exists("parientes.json"):
        print("No se encontro el archivo. No hay familiares registrados.")
        return
    
    try:
        with open("parientes.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            
            if not data:
                print("No hay familiares registrados")
                return
            
            try:
                id_buscar = int(input("\nIngrese el ID del familiar: "))
            except ValueError:
                print("ID invalido")
                return
            
            familiar_encontrado = None
            for familiar in data:
                if familiar.get('id') == id_buscar:
                    familiar_encontrado = familiar
                    break
            
            if not familiar_encontrado:
                print(f"No se encontro familiar con ID: {id_buscar}")
                return
            
            print(f"""
            ================================
            
            ID: {familiar_encontrado.get('id', 'N/A')}
            Nombre: {familiar_encontrado.get('nombre', 'N/A')}
            Edad: {familiar_encontrado.get('edad', 'N/A')}
            Parentesco: {familiar_encontrado.get('parentesco', 'N/A')}
            
            --- Documentos ---
            """)
            
            if 'info' in familiar_encontrado:
                info = familiar_encontrado['info']
                print(f"Certificado de matrimonio: {info.get('certificado de matrimonio', 'No registrado')}")
                print(f"Certificado de muerte: {info.get('certificado de muerte', 'No registrado')}")
                print(f"Registros parroquiales: {info.get('registros parroquiales', 'No registrado')}")
                print(f"Censos: {info.get('censos', 'No registrado')}")
            
            print("================================")
            
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON")
    except Exception as e:
        print(f"Error: {e}")