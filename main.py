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
            persona = solicitar_datos_persona()
            if persona:
                resultado, mensaje = gestion.recibir_solicitud(persona)
                print(f"\n{mensaje}")
            else:
                print("\nDatos inválidos. No se registró la solicitud.")
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
            print("\nMódulo de Gestión (próximamente)")
            pausar()
        elif opcion == "3":
            print("\nMódulo de Asistencia (próximamente)")
            pausar()
        elif opcion == "4":
            print("\nGracias por usar el Sistema de Asistencia y Admisión.")
            print("¡Hasta luego!")
            break
        else:
            print("\nOpción no válida.")
            pausar()


if __name__ == "__main__":
    main()
