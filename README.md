# Sistema de Árbol Genealógico

## Descripción

Sistema interactivo desarrollado con Python para la gestión de árboles genealógicos. Permite a los usuarios registrarse, iniciar sesión y administrar información detallada de sus familiares, incluyendo documentos históricos como certificados de matrimonio, muerte, registros parroquiales y censos.

## Características Principales

- **Gestión de Usuarios**
  - Registro de nuevos usuarios con ID único automático
  - Sistema de inicio de sesión seguro
  - Almacenamiento persistente de datos

- **Gestión del Árbol Genealógico**
  - Agregar familiares con información detallada
  - Listar todos los familiares registrados
  - Ver información completa de cada familiar
  - Actualizar información de familiares existentes
  - Eliminar familiares del árbol

- **Documentación Genealógica**
  - Certificados de matrimonio
  - Certificados de muerte
  - Registros parroquiales
  - Información de censos

## Estructura del Proyecto

```
Who's_your_daddy/
│
├── main.py                    # Punto de entrada del programa
├── funciones_usuario.py       # Registro e inicio de sesión
├── funciones_arbol.py         # Agregar y listar familiares
├── operaciones.py             # Actualizar y eliminar familiares
├── utilidades.py              # Funciones auxiliares (generación de ID)
├── usuarios.json              # Base de datos de usuarios (generado automáticamente)
└── familiares.json            # Base de datos de familiares (generado automáticamente)
```

## Requisitos del Sistema

- Python 3.6 o superior
- Módulos estándar de Python (json, os, time, sys)
- No requiere instalación de dependencias externas

## Instalación

1. Clone o descargue el repositorio:
```bash
git clone <url-del-repositorio>
cd proyecto_arbol
```

2. Verifique que tiene Python instalado:
```bash
python --version
```

3. El sistema está listo para ejecutarse. No requiere instalación adicional.

## Uso

### Ejecutar el Programa

```bash
python main.py
```

### Flujo de Trabajo

#### 1. Menú Principal
Al iniciar el programa, se presenta el menú principal con tres opciones:
- Registrar nuevo usuario
- Iniciar sesión
- Salir del programa

#### 2. Registro de Usuario
Para crear una cuenta nueva:
1. Seleccione la opción "Registrar nuevo usuario"
2. Ingrese su nombre completo
3. Ingrese su correo electrónico (debe ser único)
4. Ingrese una contraseña
5. El sistema genera automáticamente un ID único

#### 3. Inicio de Sesión
Para acceder al sistema:
1. Seleccione "Iniciar sesión"
2. Ingrese su correo electrónico
3. Ingrese su contraseña
4. Si las credenciales son correctas, accederá al menú de usuario

#### 4. Menú de Usuario Autenticado
Una vez autenticado, puede:

**a) Agregar Familiar**
- Ingrese nombre, edad, parentesco
- Ingrese fecha y lugar de nacimiento
- Opcionalmente agregue documentos (matrimonio, muerte, parroquiales, censos)

**b) Listar Familiares**
- Muestra un resumen de todos los familiares registrados
- Incluye ID, nombre, parentesco y edad

**c) Ver Información Detallada**
- Ingrese el ID del familiar
- Muestra toda la información incluyendo documentos

**d) Actualizar Información**
- Ingrese el ID del familiar a actualizar
- Seleccione el campo a modificar
- Ingrese el nuevo valor

**e) Eliminar Familiar**
- Ingrese el ID del familiar a eliminar
- Confirme la eliminación
- La acción es irreversible

**f) Cerrar Sesión**
- Regresa al menú principal

## Estructura de Datos

### Usuario
```json
{
    "id": 1,
    "nombre": "Juan Pérez",
    "correo": "juan@email.com",
    "contrasena": "password123"
}
```

### Familiar
```json
{
    "id": 1,
    "usuario_id": 1,
    "nombre": "María Pérez",
    "edad": 45,
    "parentesco": "madre",
    "fecha_nacimiento": "15/03/1979",
    "lugar_nacimiento": "Bogotá, Colombia",
    "documentos": {
        "matrimonio": "Certificado MAT-001",
        "muerte": "No registrado",
        "parroquiales": "Registro parroquial PR-123",
        "censos": "Censo 1990"
    }
}
```

## Funcionalidades por Módulo

### main.py
- Orquestación del flujo del programa
- Menú principal y menú de usuario autenticado
- Manejo de excepciones globales

### funciones_usuario.py
- `registrar()`: Crea un nuevo usuario
- `login()`: Autentica un usuario
- `cargar_usuarios()`: Lee usuarios del archivo JSON
- `guardar_usuarios()`: Escribe usuarios al archivo JSON

### funciones_arbol.py
- `agregar_familiar()`: Agrega un nuevo familiar
- `listar_familiares()`: Muestra lista de familiares
- `listar_info_familiar()`: Muestra información detallada
- `cargar_familiares()`: Lee familiares del archivo JSON
- `guardar_familiares()`: Escribe familiares al archivo JSON

### operaciones.py
- `actualizar_familiar()`: Modifica información de un familiar
- `eliminar_familiar()`: Elimina un familiar del árbol
- `buscar_familiar()`: Busca un familiar por ID

### utilidades.py
- `generar_id()`: Genera IDs únicos automáticamente

## Campos Actualizables

El sistema permite actualizar los siguientes campos de un familiar:
- Nombre
- Edad
- Parentesco
- Fecha de nacimiento
- Lugar de nacimiento
- Certificado de matrimonio
- Certificado de muerte
- Registros parroquiales
- Información de censos

## Manejo de Errores

El sistema incluye manejo robusto de errores:
- Validación de entrada de datos
- Manejo de archivos inexistentes
- Captura de interrupciones de teclado (Ctrl+C)
- Validación de IDs y permisos de usuario
- Mensajes de error descriptivos

## Seguridad

- Cada usuario solo puede ver y modificar sus propios familiares
- Validación de pertenencia de familiares al usuario autenticado
- Confirmación requerida para operaciones destructivas (eliminar)
- Almacenamiento de contraseñas (Nota: en producción se recomienda hash)

## Persistencia de Datos

Los datos se almacenan en archivos JSON:
- `usuarios.json`: Información de usuarios registrados
- `familiares.json`: Información de familiares

Los archivos se crean automáticamente en la primera ejecución.

## Limitaciones Conocidas

- Las contraseñas se almacenan en texto plano (no recomendado para producción)
- No hay recuperación de contraseña
- No hay límite de intentos de inicio de sesión
- La eliminación de usuarios no está implementada


## Metodología de Desarrollo

Este proyecto fue desarrollado utilizando la metodología Scrum:
- Historias de usuario definidas
- División de tareas por funcionalidades
- Desarrollo modular
- Integración continua
- Revisión de código en equipo

## Historias de Usuario Implementadas

1. **Registro**: Usuario puede registrarse con nombre, correo y contraseña
2. **ID Automático**: El sistema genera ID único automáticamente
3. **Inicio de Sesión**: Usuario puede iniciar sesión con correo y contraseña
4. **Listar Árbol**: Usuario puede listar sus familiares registrados
5. **Ver Información**: Usuario puede ver información detallada de familiares
6. **Agregar Documentos**: Usuario puede agregar certificados y registros
7. **Eliminar**: Usuario puede eliminar familiares del árbol
8. **Actualizar**: Usuario puede actualizar información de familiares
9. **Menú de Opciones**: Sistema muestra menú con funcionalidades
10. **Cerrar Sesión**: Usuario puede cerrar sesión correctamente


