from modelos.persona import Persona
from modelos.profesor import Profesor
from modelos.estudiante import Estudiante
from modelos.clase import Clase
from estructuras.cola import Cola


class Gestion:
    def __init__(self):
        self._cola_admision = Cola()
        self._estudiantes = []
        self._profesores = []
        self._aulas = []
        self._contador_estudiantes = 0
        self._contador_profesores = 0

    @property
    def cola_admision(self):
        return self._cola_admision

    @property
    def estudiantes(self):
        return self._estudiantes

    @property
    def profesores(self):
        return self._profesores

    @property
    def aulas(self):
        return self._aulas

    def recibir_solicitud(self, persona):
        pass

    def admitir_siguiente(self, grado, aula_asignada):
        pass

    def crear_profesor(self, persona, codigo_aula):
        pass

    def crear_aula(self, codigo_clase, codigo_aula, capacidad):
        pass

    def asignar_profesor_aula(self, codigo_profesor, codigo_aula):
        pass

    def asignar_estudiante_aula(self, codigo_estudiante, codigo_aula):
        pass

    def dar_de_baja(self, codigo_estudiante):
        pass

    def buscar_estudiante(self, codigo_estudiante):
        pass

    def buscar_profesor(self, codigo_profesor):
        pass

    def buscar_aula(self, codigo_aula):
        pass

    def listar_estudiantes_activos(self):
        pass

    def listar_estudiantes_por_grado(self, grado):
        pass

    def _existe_aula(self, codigo_aula):
        pass

    def _buscar_aula_obj(self, codigo_aula):
        pass

    def _cui_ya_registrado(self, cui):
        pass
