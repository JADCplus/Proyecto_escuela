import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gestion.gestion import Gestion
from modelos.persona import Persona
from utils.validaciones import validar_cui, validar_edad, validar_sexo, validar_codigo, validar_grado


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input("\nPresione Enter para continuar...")


def mostrar_titulo():
    print("=" * 60)
    print("  SISTEMA DE ASISTENCIA Y ADMISIÓN PARA ESCUELAS")
    print("=" * 60)


def solicitar_datos_persona():
    print("\n--- Ingrese los datos de la persona ---")
    nombre = input("Nombre completo: ").strip()
    if not nombre:
        return None

    while True:
        try:
            edad = int(input("Edad: "))
            if validar_edad(edad):
                break
            print("Edad inválida. Debe estar entre 3 y 100 años.")
        except ValueError:
            print("Ingrese un número válido para la edad.")

    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if validar_sexo(sexo):
            break
        print("Sexo inválido. Ingrese M o F.")

    while True:
        cui = input("CUI (13 dígitos numéricos): ").strip()
        if validar_cui(cui):
            break
        print("CUI inválido. Debe tener exactamente 13 dígitos numéricos.")

    return Persona(cui, nombre, edad, sexo)


def menu_admision(gestion):
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("      MÓDULO DE ADMISIÓN")
        print("=" * 50)
        print("1. Registrar solicitud de admisión")
        print("2. Ver cola de admisión")
        print("3. Admitir siguiente solicitud")
        print("4. Volver al menú principal")
        print("=" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            while True:
                persona = solicitar_datos_persona()
                if not persona:
                    print("Datos Invalidos, no se registro la solicitud")
                    break
                resultado,mensaje=gestion.recibir_solicitud(persona)
                print(f"{mensaje}")
                if resultado:
                    break
            pausar()

        elif opcion == "2":
            cola = gestion.cola_admision
            if cola.esta_vacia():
                print("\nLa cola de admisión está vacía.")
            else:
                print(f"\nCola de admisión ({cola.tamano()} solicitudes pendientes):")
                for i, persona in enumerate(cola.mostrar(), 1):
                    print(f"  {i}. {persona.nombre} (CUI: {persona.cui})")
            pausar()

        elif opcion == "3":
            if gestion.cola_admision.esta_vacia():
                print("\nNo hay solicitudes pendientes para admitir.")
            else:
                print("\nSiguiente en la cola:")
                frente = gestion.cola_admision.ver_frente()
                print(f"  {frente.nombre} (CUI: {frente.cui})")

                while True:
                    try:
                        grado = int(input("Grado a asignar (1-6): "))
                        if validar_grado(grado):
                            break
                        print("Grado inválido. Debe estar entre 1 y 6.")
                    except ValueError:
                        print("Ingrese un número válido.")

                aula = input("Código de aula a asignar: ").strip()
                if not validar_codigo(aula):
                    print("Código de aula inválido.")
                else:
                    resultado, mensaje = gestion.admitir_siguiente(grado, aula)
                    print(f"\n{mensaje}")
            pausar()

        elif opcion == "4":
            break
        else:
            print("\nOpción no válida.")
            pausar()


def menu_gestion(gestion):
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("      MÓDULO DE GESTIÓN")
        print("=" * 50)
        print("1. Crear profesor")
        print("2. Crear aula")
        print("3. Asignar profesor a aula")
        print("4. Asignar estudiante a aula")
        print("5. Dar de baja estudiante")
        print("6. Listar estudiantes activos")
        print("7. Listar profesores")
        print("8. Listar aulas")
        print("9. Volver al menú principal")
        print("=" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            persona = solicitar_datos_persona()
            if persona:
                while True:
                    codigo_aula = input("Código de aula a asignar: ").strip()
                    if not validar_codigo(codigo_aula):
                        print("\nCódigo de aula inválido. Intente de nuevo.")
                        continue
                    resultado, mensaje = gestion.crear_profesor(persona, codigo_aula)
                    print(f"\n{mensaje}")
                    if resultado:
                        break
            else:
                print("\nDatos inválidos.")
            pausar()

        elif opcion == "2":
            codigo_clase = input("Código de clase: ").strip()
            codigo_aula = input("Código de aula: ").strip()
            try:
                capacidad = int(input("Capacidad máxima (default 40): ") or "40")
            except ValueError:
                capacidad = 40

            if validar_codigo(codigo_clase) and validar_codigo(codigo_aula):
                resultado, mensaje = gestion.crear_aula(codigo_clase, codigo_aula, capacidad)
                print(f"\n{mensaje}")
            else:
                print("\nCódigos inválidos.")
            pausar()

        elif opcion == "3":
            codigo_profesor = input("Código del profesor: ").strip()
            codigo_aula = input("Código del aula: ").strip()
            if validar_codigo(codigo_profesor) and validar_codigo(codigo_aula):
                resultado, mensaje = gestion.asignar_profesor_aula(codigo_profesor, codigo_aula)
                print(f"\n{mensaje}")
            else:
                print("\nCódigos inválidos.")
            pausar()

        elif opcion == "4":
            codigo_estudiante = input("Código del estudiante: ").strip()
            codigo_aula = input("Código del aula: ").strip()
            if validar_codigo(codigo_estudiante) and validar_codigo(codigo_aula):
                resultado, mensaje = gestion.asignar_estudiante_aula(codigo_estudiante, codigo_aula)
                print(f"\n{mensaje}")
            else:
                print("\nCódigos inválidos.")
            pausar()

        elif opcion == "5":
            codigo_estudiante = input("Código del estudiante a dar de baja: ").strip()
            if validar_codigo(codigo_estudiante):
                resultado, mensaje = gestion.dar_de_baja(codigo_estudiante)
                print(f"\n{mensaje}")
            else:
                print("\nCódigo inválido.")
            pausar()

        elif opcion == "6":
            activos = gestion.listar_estudiantes_activos()
            if not activos:
                print("\nNo hay estudiantes activos en el sistema.")
            else:
                print(f"\nEstudiantes activos ({len(activos)}):")
                for est in activos:
                    print(f"  - {est}")
            pausar()

        elif opcion == "7":
            if not gestion.profesores:
                print("\nNo hay profesores registrados.")
            else:
                print(f"\nProfesores ({len(gestion.profesores)}):")
                for prof in gestion.profesores:
                    print(f"  - {prof}")
            pausar()

        elif opcion == "8":
            if not gestion.aulas:
                print("\nNo hay aulas registradas.")
            else:
                print(f"\nAulas ({len(gestion.aulas)}):")
                for aula in gestion.aulas:
                    print(f"  - {aula}")
            pausar()

        elif opcion == "9":
            break
        else:
            print("\nOpción no válida.")
            pausar()


def menu_asistencia(gestion):
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("      MÓDULO DE ASISTENCIA")
        print("=" * 50)
        print("1. Seleccionar clase para asistencia")
        print("2. Volver al menú principal")
        print("=" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not gestion.aulas:
                print("\nNo hay aulas registradas. Cree un aula primero.")
                pausar()
                continue

            print("\nAulas disponibles:")
            for i, aula in enumerate(gestion.aulas, 1):
                print(f"  {i}. {aula}")

            try:
                idx = int(input("\nSeleccione el número de aula: ")) - 1
                if 0 <= idx < len(gestion.aulas):
                    aula_seleccionada = gestion.aulas[idx]
                    submenu_asistencia(gestion, aula_seleccionada)
                else:
                    print("\nSelección inválida.")
                    pausar()
            except ValueError:
                print("\nIngrese un número válido.")
                pausar()

        elif opcion == "2":
            break
        else:
            print("\nOpción no válida.")
            pausar()


def submenu_asistencia(gestion, clase):
    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print(f"  ASISTENCIA - {clase.codigo_clase} ({clase.codigo_aula})")
        if clase.profesor:
            print(f"  Profesor: {clase.profesor.nombre}")
        print("=" * 50)
        print("1. Marcar entrada de estudiante")
        print("2. Deshacer última marcación")
        print("3. Ver asistencia de la sesión")
        print("4. Ver tope de la pila")
        print("5. Ver estudiantes de la clase")
        print("6. Iniciar nueva sesión")
        print("7. Registrar asistencia masiva (profesor)")
        print("8. Ver asistencias del profesor en esta aula")
        print("9. Volver")
        print("=" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            if not clase.estudiantes:
                print("\nNo hay estudiantes asignados a esta clase.")
                pausar()
                continue

            print("\nEstudiantes de la clase:")
            for i, est in enumerate(clase.estudiantes, 1):
                estado = "✓" if est in clase.asistencia_sesion else " "
                print(f"  {i}. [{estado}] {est.nombre} (CUI: {est.cui})")

            try:
                idx = int(input("\nSeleccione el número del estudiante: ")) - 1
                if 0 <= idx < len(clase.estudiantes):
                    estudiante = clase.estudiantes[idx]
                    if clase.profesor:
                        resultado, mensaje = clase.profesor.registrar_asistencia_estudiante(clase, estudiante)
                    else:
                        resultado, mensaje = clase.marcar_entrada(estudiante)
                    print(f"\n{mensaje}")
                else:
                    print("\nSelección inválida.")
            except ValueError:
                print("\nIngrese un número válido.")
            pausar()

        elif opcion == "2":
            if clase.profesor:
                resultado, mensaje = clase.profesor.deshacer_marcacion(clase)
            else:
                resultado, mensaje = clase.deshacer_ultima_marcacion()
            print(f"\n{mensaje}")
            pausar()

        elif opcion == "3":
            print(f"\n{clase.ver_asistencia_sesion()}")
            pausar()

        elif opcion == "4":
            print(f"\n{clase.ver_tope_pila()}")
            pausar()

        elif opcion == "5":
            if not clase.estudiantes:
                print("\nNo hay estudiantes asignados a esta clase.")
            else:
                print(f"\nEstudiantes de la clase ({len(clase.estudiantes)}):")
                for est in clase.estudiantes:
                    print(f"  - {est}")
            pausar()

        elif opcion == "6":
            clase.iniciar_nueva_sesion()
            print("\nNueva sesión iniciada. Pila y asistencia reiniciadas.")
            pausar()

        elif opcion == "7":
            if clase.profesor:
                clase.profesor.registrar_asistencia(gestion)
            else:
                print("\nNo hay profesor asignado a esta clase.")
            pausar()

        elif opcion == "8":
            if clase.profesor:
                clase.profesor.ver_asistencias_por_aula(clase.codigo_aula)
            else:
                print("\nNo hay profesor asignado a esta clase.")
            pausar()

        elif opcion == "9":
            break
        else:
            print("\nOpción no válida.")
            pausar()


def main():
    gestion = Gestion()

    while True:
        limpiar_pantalla()
        mostrar_titulo()
        print("\n1. Módulo de Admisión")
        print("2. Módulo de Gestión")
        print("3. Módulo de Asistencia")
        print("4. Salir")
        print("=" * 60)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_admision(gestion)
        elif opcion == "2":
            menu_gestion(gestion)
        elif opcion == "3":
            menu_asistencia(gestion)
        elif opcion == "4":
            print("\nGracias por usar el Sistema de Asistencia y Admisión.")
            print("¡Hasta luego!")
            break
        else:
            print("\nOpción no válida.")
            pausar()


if __name__ == "__main__":
    main()
