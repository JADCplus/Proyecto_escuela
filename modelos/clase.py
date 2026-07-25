from estructuras.pila import Pila


class Clase:
    def __init__(self, codigo_clase, codigo_aula, capacidad_maxima=40):
        self._codigo_clase = codigo_clase
        self._codigo_aula = codigo_aula
        self._capacidad_maxima = capacidad_maxima
        self._estudiantes = []
        self._profesor = None
        self._pila_marcaciones = Pila()
        self._asistencia_sesion = []

    @property
    def codigo_clase(self):
        return self._codigo_clase

    @property
    def codigo_aula(self):
        return self._codigo_aula

    @property
    def capacidad_maxima(self):
        return self._capacidad_maxima

    @property
    def profesor(self):
        return self._profesor

    @property
    def estudiantes(self):
        return self._estudiantes

    @property
    def asistencia_sesion(self):
        return self._asistencia_sesion

    def asignar_profesor(self, profesor):
        self._profesor = profesor

    def remover_profesor(self):
        anterior = self._profesor
        self._profesor = None
        return anterior

    def agregar_estudiante(self, estudiante):
        for est in self._estudiantes:
            if est.codigo_estudiante == estudiante.codigo_estudiante:
                return False
        if len(self._estudiantes) < self._capacidad_maxima:
            self._estudiantes.append(estudiante)
            return True
        return False

    def remover_estudiante(self, codigo_estudiante):
        for i, est in enumerate(self._estudiantes):
            if est.codigo_estudiante == codigo_estudiante:
                self._estudiantes.pop(i)
                return True
        return False

    def marcar_entrada(self, estudiante):
        if len(self._asistencia_sesion) >= self._capacidad_maxima:
            return False, "Aula llena, no se puede registrar más asistencia"

        for est in self._asistencia_sesion:
            if est.codigo_estudiante == estudiante.codigo_estudiante:
                return (
                    False,
                    f"El estudiante {estudiante.nombre} ya tiene asistencia registrada",
                )

        self._pila_marcaciones.apilar(estudiante)
        self._asistencia_sesion.append(estudiante)
        return True, f"Asistencia marcada para {estudiante.nombre}"

    def deshacer_ultima_marcacion(self):
        if self._pila_marcaciones.esta_vacia():
            return False, "No hay marcaciones recientes para deshacer"

        estudiante = self._pila_marcaciones.desapilar()

        for i, est in enumerate(self._asistencia_sesion):
            if est.codigo_estudiante == estudiante.codigo_estudiante:
                self._asistencia_sesion.pop(i)
                break

        return True, f"Se deshizo la marcación de {estudiante.nombre}"

    def ver_asistencia_sesion(self):
        if not self._asistencia_sesion:
            return "No hay asistencias registradas en esta sesión"
        resultado = (
            f"Asistencia de la sesión ({len(self._asistencia_sesion)} presentes):\n"
        )
        for est in self._asistencia_sesion:
            resultado += f"  - {est.nombre} (CUI: {est.cui})\n"
        return resultado

    def ver_tope_pila(self):
        tope = self._pila_marcaciones.ver_tope()
        if tope is None:
            return "La pila de marcaciones está vacía"
        return f"Tope de la pila: {tope.nombre}"

    def iniciar_nueva_sesion(self):
        self._pila_marcaciones = Pila()
        self._asistencia_sesion = []

    def __str__(self):
        profesor_info = self._profesor.nombre if self._profesor else "Sin asignar"
        return (
            f"Clase: {self._codigo_clase} | Aula: {self._codigo_aula} | "
            f"Profesor: {profesor_info} | "
            f"Estudiantes: {len(self._estudiantes)}/{self._capacidad_maxima}"
        )
