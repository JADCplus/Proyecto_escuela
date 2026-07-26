from gestion.gestion import Gestion

def main():
    gestion = Gestion()

    while True:
        print("\n=== Sistema de Asistencia y Admisión para Escuelas ===")
        print("1. Admisión")
        print("2. Gestión")
        print("3. Asistencia")
        print("0. Salir")
        try:

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                pass  # Submenú de Admisión
            elif opcion == "2":
                pass  # Submenú de Gestión
            elif opcion == "3":
                pass  # Submenú de Asistencia
            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

        except ValueError:
         pass


if __name__ == "__main__":
    main()
