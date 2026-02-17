import os
import json

a = ""

def listar_info_arbol():

    if os.path.exists("arbol.json"):
        with open("arbol.json", "r") as file:
            data = json.load(file)
            for a in data:
                print(f"""
                ================================
    
                Nombre: {a}
    
                Certificado de matimonio: {a}
    
                Difunto: {a}
    
                Registros parroquiales: {a}
    
                Censos: {a}  
    
                ================================
                """)
    else:
        data = {}
        print("No se encontró el archivo .json, se creará uno nuevo.")


#Yo como usuario, quiero poder agregar certificado de matrimonio,
#muerte, registros parroquiales y censos si lo aplica, para poder
#tener información más detallada.