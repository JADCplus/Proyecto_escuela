from modelos.persona import Persona
from collections import deque
from modelos.asistencia import Asistencia


class Profesor(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_aula, codigo_profesor):
        super().__init__(cui, nombre, edad, sexo)
        self.codigo_aula = codigo_aula
        self.codigo_profesor = codigo_profesor
        self.asistencia = deque()

    def ver_info(self):
        print(
            f"Codigo de Profesor: {self.codigo_profesor} | CUI: {self.cui} | Nombre: {self.nombre} | Edad: {self.get_edad()} | Sexo: {self.sexo} | Aula: {self.codigo_aula}"
        )

    def marcar_asistencia(self, gestion):
        print("====SISTEMA DE ASISTENCIA====")
        codigo_aula = input("Ingrese codigo de aula: ")

        aula = gestion.buscar_aula(codigo_aula)
        if aula is None:
            print(f"No existe un aula con código {codigo_aula}")
            return

        if not aula.estudiantes:
            print("El aula no tiene estudiantes registrados")
            return

        for estudiante in aula.estudiantes:
            estado_input = (input(f"Estado de {estudiante.nombre} (P=Presente/A=Ausente): ").upper() )
            estado = "Presente" if estado_input == "P" else "Ausente"

            registro = Asistencia(
                codigo_aula,
                estudiante.codigo_estudiante,
                estudiante.nombre,
                estado,
            )

            self.asistencia.append(registro)

        print("Asistencia registrada exitosamente")


    def ver_asistencias_por_aula(self, codigo_aula):
        asistencias_aula = [a for a in self.asistencia if a.codigo_aula == codigo_aula]

        if not asistencias_aula:
            print(f"No hay asistencias registradas para el aula {codigo_aula}")
            return []

        print(f"====ASISTENCIAS DEL AULA {codigo_aula}====")
        for asistencia in asistencias_aula:
            print(asistencia)

        return asistencias_aula

