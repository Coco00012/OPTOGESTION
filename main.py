
"""
==========================================================
                 SISTEMA OPTOGESTIÓN
              CENTRO DE ATENCIÓN OPTOMÉTRICA
                    PROYECTO FINAL
                     PROGRAMACIÓN I
==========================================================
"""

import json
import os


# RUTA DEL ARCHIVO JSON EN LA MISMA CARPETA DEL PROGRAMA

CARPETA_PROYECTO = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_DATOS = os.path.join(CARPETA_PROYECTO, "pacientes.json")


# ==========================================================
# 1. CARGAR Y GUARDAR PACIENTES
# ==========================================================

def cargar_pacientes():

    pacientes_ejemplo = [
        {
            "id": "P001",
            "nombre": "Maria Vanegas",
            "edad": 24,
            "sexo": "Femenino",
            "usa_correccion": True
        },
        {
            "id": "P002",
            "nombre": "Juan Mejia",
            "edad": 31,
            "sexo": "Masculino",
            "usa_correccion": False
        },
        {
            "id": "P003",
            "nombre": "Naomy Melgar",
            "edad": 19,
            "sexo": "Femenino",
            "usa_correccion": True
        },
        {
            "id": "P004",
            "nombre": "Thomas Rueda",
            "edad": 67,
            "sexo": "Masculino",
            "usa_correccion": True
        },
        {
            "id": "P005",
            "nombre": "Isabella Castro",
            "edad": 42,
            "sexo": "Femenino",
            "usa_correccion": False
        }
    ]

    if not os.path.exists(ARCHIVO_DATOS):
        guardar_pacientes(pacientes_ejemplo)
        return pacientes_ejemplo

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            if isinstance(datos, list) and len(datos) > 0:
                return datos

            guardar_pacientes(pacientes_ejemplo)
            return pacientes_ejemplo

    except (json.JSONDecodeError, OSError) as error:
        print("Error al cargar los pacientes:", error)
        return []


def guardar_pacientes(pacientes):

    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(
                pacientes,
                archivo,
                ensure_ascii=False,
                indent=4
            )

    except OSError as error:
        print("Error al guardar los pacientes:", error)


# ==========================================================
# 2. FUNCIONES PARA VALIDAR LOS DATOS
# ==========================================================

def solicitar_texto(mensaje):

    while True:
        dato = input(mensaje).strip()

        if dato:
            return dato

        print("El campo no puede quedar vacío.")


def solicitar_edad():

    while True:
        try:
            edad = int(input("Edad (1 a 120 años): "))

            if 1 <= edad <= 120:
                return edad

            print("La edad debe estar entre 1 y 120 años.")

        except ValueError:
            print("Ingrese una edad numérica válida.")


def solicitar_sexo():

    while True:
        sexo = input("Sexo (F/M/Otro): ").strip().upper()

        if sexo == "F":
            return "Femenino"

        elif sexo == "M":
            return "Masculino"

        elif sexo == "OTRO":
            return "Otro"

        else:
            print("Ingrese F, M u Otro.")


def solicitar_si_no(mensaje):

    while True:
        respuesta = input(mensaje + " (S/N): ").strip().upper()

        if respuesta in ["S", "SI", "SÍ"]:
            return True

        elif respuesta in ["N", "NO"]:
            return False

        else:
            print("Respuesta inválida. Ingrese S o N.")


# ==========================================================
# 3. REGISTRAR PACIENTE
# ==========================================================

def registrar_paciente(pacientes):

    print("\n========== REGISTRO DE PACIENTE ==========")

    identificador = solicitar_texto(
        "Identificador del paciente (Ejemplo P006): "
    ).upper()

    # Verificar que el identificador sea único

    for paciente in pacientes:

        if paciente["id"].upper() == identificador:
            print("\nYa existe un paciente con ese identificador.")
            return

    nombre = solicitar_texto("Nombre completo: ")

    edad = solicitar_edad()

    sexo = solicitar_sexo()

    usa_correccion = solicitar_si_no(
        "¿Utiliza corrección visual?"
    )

    nuevo_paciente = {
        "id": identificador,
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo,
        "usa_correccion": usa_correccion
    }

    pacientes.append(nuevo_paciente)

    guardar_pacientes(pacientes)

    print("\n==========================================")
    print("¡PACIENTE REGISTRADO CORRECTAMENTE!")
    print("Nombre:", nombre)
    print("Identificador:", identificador)
    print("==========================================")


# ==========================================================
# 4. CONSULTAR PACIENTE POR IDENTIFICADOR
# ==========================================================

def consultar_paciente(pacientes):

    print("\n========== CONSULTAR PACIENTE ==========")

    identificador = solicitar_texto(
        "Ingrese el identificador del paciente: "
    ).upper()

    for paciente in pacientes:

        if paciente["id"].strip().upper() == identificador:

            print("\n========== INFORMACIÓN DEL PACIENTE ==========")

            print("Identificador:", paciente["id"])
            print("Nombre completo:", paciente["nombre"])
            print("Edad:", paciente["edad"], "años")
            print("Sexo:", paciente["sexo"])

            if paciente["usa_correccion"]:
                print("Utiliza corrección visual: Sí")

            else:
                print("Utiliza corrección visual: No")

            print("==============================================")

            return

    print("\nNo se encontró ningún paciente con ese identificador.")


# ==========================================================
# 5. MOSTRAR TODOS LOS PACIENTES REGISTRADOS
# ==========================================================

def mostrar_pacientes(pacientes):

    print("\n========== PACIENTES REGISTRADOS ==========")

    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return

    print("-" * 60)

    for paciente in pacientes:

        print(
            "ID:", paciente["id"],
            "| Nombre:", paciente["nombre"]
        )

    print("-" * 60)

    print("Número total de pacientes:", len(pacientes))


# ==========================================================
# 6. BUSCAR PACIENTES CON CORRECCIÓN VISUAL
# ==========================================================

def buscar_con_correccion(pacientes):

    print("\n====== PACIENTES CON CORRECCIÓN VISUAL ======")

    encontrados = 0

    for paciente in pacientes:

        if paciente["usa_correccion"] == True:

            print(
                "Nombre:", paciente["nombre"],
                "| ID:", paciente["id"]
            )

            encontrados += 1

    if encontrados == 0:
        print("No hay pacientes que utilicen corrección visual.")

    else:
        print("\nTotal de pacientes encontrados:", encontrados)


# ==========================================================
# 7. GENERAR ESTADÍSTICAS DE LA JORNADA
# ==========================================================

def generar_estadisticas(pacientes):

    print("\n========== ESTADÍSTICAS DE LA JORNADA ==========")

    total = len(pacientes)

    print("Número total de pacientes:", total)

    if total == 0:
        print("No hay pacientes para calcular estadísticas.")
        print("Edad promedio: No disponible.")
        print("Pacientes con corrección visual: 0")
        return

    suma_edades = 0

    pacientes_correccion = 0

    for paciente in pacientes:

        suma_edades += paciente["edad"]

        if paciente["usa_correccion"] == True:
            pacientes_correccion += 1

    promedio = suma_edades / total

    print("Edad promedio:", round(promedio, 2), "años")

    print(
        "Pacientes que utilizan corrección visual:",
        pacientes_correccion
    )

    print(
        "Pacientes que no utilizan corrección visual:",
        total - pacientes_correccion
    )


# ==========================================================
# 8. MENÚ PRINCIPAL
# ==========================================================

def mostrar_menu():

    print("""
╔════════════════════════════════════════════════════════╗
║                                                        ║
║                  SISTEMA OPTOGESTIÓN                   ║
║                                                        ║
║              CENTRO DE ATENCIÓN OPTOMÉTRICA            ║
║                                                        ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║   1. Registrar paciente                                ║
║   2. Consultar paciente                                 ║
║   3. Mostrar pacientes registrados                      ║
║   4. Buscar pacientes con corrección visual             ║
║   5. Generar estadísticas                               ║
║   6. Salir                                              ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
""")


# ==========================================================
# 9. EJECUTAR PROGRAMA
# ==========================================================

def ejecutar_programa():

    pacientes = cargar_pacientes()

    print("Pacientes cargados:", len(pacientes))
    print("Archivo de datos:", ARCHIVO_DATOS)

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_paciente(pacientes)

        elif opcion == "2":
            consultar_paciente(pacientes)

        elif opcion == "3":
            mostrar_pacientes(pacientes)

        elif opcion == "4":
            buscar_con_correccion(pacientes)

        elif opcion == "5":
            generar_estadisticas(pacientes)

        elif opcion == "6":

            print("\n==========================================")
            print("GRACIAS POR UTILIZAR OPTOGESTIÓN")
            print("Los registros se han conservado.")
            print("Hasta pronto.")
            print("==========================================")

            break

        else:
            print("\nOpción incorrecta. Seleccione del 1 al 6.")

        input("\nPresione ENTER para regresar al menú...")


# ==========================================================
# INICIO DEL SISTEMA
# ==========================================================

if __name__ == "__main__":
    ejecutar_programa()
