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

            opcion = int(input("Seleccione una opción: "))

            match opcion:
                case 1:
                    while True:
                        print("==== Sistema de Admision====")
                        print("1.Recibir Solicitud")
                        print("2.Admitir a Solicitante")
                        print("0. Salir")

                        try:
                            op_admision = int(input("Seleccione una opcion: "))
                            match op_admision:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    input("Regresando a menu principal, presione enter para continuar")
                                    break
                                case _:
                                    input("Opcion no valida, presione enter para continuar...")


                        except ValueError:
                            print("Opcion no valida")
                            input("Presione enter para continuar...")

                case 2:
                    while True:

                        print("==== Sistema de Gestiones====")
                        print("1.Ingresar nuevo Profesor")
                        print("2.Crear nueva Aula")
                        print("3.Asignar Profesor a un Aula")
                        print("4.Asignar Estudiante a un Aula")
                        print("5.Dar de Baja a un estudiante")
                        print("6.Buscar Estudiante")
                        print("7.Buscar Profesor")
                        print("8.Buscar Aula")
                        print("9.Listar Estudiantes")
                        print("0.Salir")

                        try:
                            op_gestion = int(input("Seleccione una opcion: "))
                            match op_gestion:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    pass
                                case 5:
                                    pass
                                case 6:
                                    pass
                                case 7:
                                    pass
                                case 8:
                                    pass
                                case 9:
                                    pass
                                case 0:
                                    input("Regresando a menu principal, presione enter para continuar")
                                    break
                                case _:
                                    input("Opcion no valida, presione enter para continuar...")


                        except ValueError:
                            print("Opcion no valida")
                            input("Presione enter para continuar...")

                case 3:
                    while True:
                        print("==== Sistema de Asistencia====")
                        print("1.Marcar Asistencia")
                        print("2.Ver asistencia")
                        print("3.Salir")

                        try:
                            op_asistencia = int(input("Seleccione una opcion: "))
                            match op_asistencia:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    input("Regresando a menu principal, presione enter para continuar")
                                    break
                                case _:
                                    input("Opcion no valida, presione enter para continuar...")


                        except ValueError:
                            print("Opcion no valida")
                            input("Presione enter para continuar...")


        except ValueError:
         pass

if __name__ == "__main__":
    main()
