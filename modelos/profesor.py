from collections import deque
from modelos.persona import Persona
from modelos.asistencia import Asistencia


class Profesor(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_profesor, codigo_aula):
        super().__init__(cui, nombre, edad, sexo)
        self._codigo_profesor = codigo_profesor
        self._codigo_aula = codigo_aula
        self.asistencia = deque()

    @property
    def codigo_profesor(self):
        return self._codigo_profesor

    @property
    def codigo_aula(self):
        return self._codigo_aula

    @codigo_aula.setter
    def codigo_aula(self, valor):
        self._codigo_aula = valor

    def registrar_asistencia_estudiante(self, clase, estudiante):
        return clase.marcar_entrada(estudiante)

    def registrar_asistencia(self, gestion):
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
            estado_input = input(
                f"Estado de {estudiante.nombre} (P=Presente/A=Ausente): "
            ).upper()
            estado = "Presente" if estado_input == "P" else "Ausente"

            registro = Asistencia(
                codigo_aula,
                estudiante.codigo_estudiante,
                estudiante.nombre,
                estado,
            )

            self.asistencia.append(registro)
            if estado == "Presente":
                aula.marcar_entrada(estudiante)
            else:
                for i, est in enumerate(aula._asistencia_sesion):
                    if est.codigo_estudiante == estudiante.codigo_estudiante:
                        aula._asistencia_sesion.pop(i)
                        break

        print("Asistencia registrada exitosamente")

    def deshacer_marcacion(self, clase):
        return clase.deshacer_ultima_marcacion()

    def ver_asistencias_por_aula(self, codigo_aula):
        asistencias_aula = [a for a in self.asistencia if a.codigo_aula == codigo_aula]

        if not asistencias_aula:
            print(f"No hay asistencias registradas para el aula {codigo_aula}")
            return []

        print(f"====ASISTENCIAS DEL AULA {codigo_aula}====")
        for asistencia in asistencias_aula:
            print(asistencia)

        return asistencias_aula

    def ver_info(self):
        print(
            f"Codigo de Profesor: {self._codigo_profesor} | CUI: {self.cui} | "
            f"Nombre: {self.nombre} | Edad: {self.edad} | "
            f"Sexo: {self.sexo} | Aula: {self._codigo_aula}"
        )

    def rol(self):
        return "Profesor"

    def __str__(self):
        return (
            f"Código: {self._codigo_profesor} | Nombre: {self.nombre} | "
            f"CUI: {self.cui} | Aula: {self._codigo_aula}"
        )
