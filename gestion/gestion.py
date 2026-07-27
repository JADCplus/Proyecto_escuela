from estructuras.cola import Cola
from modelos.estudiante import Estudiante
from modelos.profesor import Profesor
from modelos.clase import Clase


class Gestion:
    def __init__(self):
        self._cola_admision = Cola()
        self._estudiantes = []
        self._profesores = []
        self._aulas = []
        self._contador_estudiantes = 0
        self._contador_profesores = 0

    def cola_admision(self):
        return self._cola_admision

    def estudiantes(self):
        return self._estudiantes

    def profesores(self):
        return self._profesores

    def aulas(self):
        return self._aulas

    def asistencia(self):
        return self._asistencia

    def _existe_aula(self, codigo_aula):
        for aula in self._aulas:
            if aula.codigo_aula == codigo_aula:
                return True
        return False

    def _buscar_aula_obj(self, codigo_aula):
        for aula in self._aulas:
            if aula.codigo_aula == codigo_aula:
                return aula
        return None

    def _cui_ya_registrado(self, cui):
        for est in self._estudiantes:
            if est.cui == cui:
                return True
        for prof in self._profesores:
            if prof.cui == cui:
                return True
        for persona in self._cola_admision.mostrar():
            if persona.cui == cui:
                return True
        return False

    def recibir_solicitud(self, persona):
        if not self._aulas:
            return (
                False,
                "No hay aulas registradas. Cree un aula primero antes de recibir solicitudes",
            )
        if self._cui_ya_registrado(persona.cui):
            return False, f"Ya existe una persona registrada con CUI {persona.cui}"
        self._cola_admision.encolar(persona)
        return True, f"Solicitud de {persona.nombre} recibida y encolada"

    def admitir_siguiente(self, grado, aula_asignada):
        if self._cola_admision.esta_vacia():
            return False, "No hay solicitudes pendientes en la cola de admisión"

        aula = self._buscar_aula_obj(aula_asignada)
        if aula is None:
            return False, f"No existe un aula con código {aula_asignada}"

        persona = self._cola_admision.ver_frente()

        if len(aula.estudiantes) >= aula.capacidad_maxima:
            return (
                False,
                f"El aula {aula_asignada} está llena. No se pudo admitir a {persona.nombre}",
            )

        self._cola_admision.desencolar()
        self._contador_estudiantes += 1
        codigo_estudiante = f"EST-{self._contador_estudiantes:04d}"

        estudiante = Estudiante(
            persona.cui,
            persona.nombre,
            persona.edad,
            persona.sexo,
            codigo_estudiante,
            aula_asignada,
            grado
        )

        self._estudiantes.append(estudiante)
        aula.agregar_estudiante(estudiante)
        return (
            True,
            f"Estudiante {estudiante.nombre} admitido con código {codigo_estudiante} y asignado a aula {aula_asignada}",
        )

    def crear_profesor(self, persona, codigo_aula):
        aula = self._buscar_aula_obj(codigo_aula)
        if aula is None:
            return (
                False,
                f"No existe un aula con código {codigo_aula}. Cree el aula primero",
            )

        if self._cui_ya_registrado(persona.cui):
            return False, f"Ya existe una persona registrada con CUI {persona.cui}"

        self._contador_profesores += 1
        codigo_profesor = f"PROF-{self._contador_profesores:04d}"

        profesor = Profesor(
            persona.cui,
            persona.nombre,
            persona.edad,
            persona.sexo,
            codigo_aula,
            codigo_profesor,
        )

        self._profesores.append(profesor)

        mensaje_extras = ""
        if aula.profesor is not None:
            anterior = aula.profesor
            aula.remover_profesor()
            mensaje_extras = f" (reemplaza a {anterior.nombre})"

        aula.asignar_profesor(profesor)
        return (
            True,
            f"Profesor {profesor.nombre} creado con código {codigo_profesor} y asignado a aula {codigo_aula}{mensaje_extras}",
        )

    def crear_aula(self, codigo_clase, codigo_aula, capacidad=40):
        for aula in self._aulas:
            if aula.codigo_aula == codigo_aula:
                return False, f"Ya existe un aula con código {codigo_aula}"

        nueva_aula = Clase(codigo_clase, codigo_aula, capacidad)
        self._aulas.append(nueva_aula)
        return True, f"Aula {codigo_aula} creada exitosamente"

    def asignar_profesor_aula(self, codigo_profesor, codigo_aula):
        profesor = None
        for p in self._profesores:
            if p.codigo_profesor == codigo_profesor:
                profesor = p
                break

        if profesor is None:
            return False, f"No se encontró profesor con código {codigo_profesor}"

        aula = self._buscar_aula_obj(codigo_aula)
        if aula is None:
            return False, f"No se encontró aula con código {codigo_aula}"

        mensaje_extras = ""
        if aula.profesor is not None:
            anterior = aula.profesor
            aula.remover_profesor()
            for a in self._aulas:
                if (
                    a.codigo_aula == anterior.codigo_aula
                    and a.codigo_aula != codigo_aula
                ):
                    pass
            mensaje_extras = f" (reemplaza a {anterior.nombre})"

        aula.asignar_profesor(profesor)
        return (
            True,
            f"Profesor {profesor.nombre} asignado a aula {codigo_aula}{mensaje_extras}",
        )

    def asignar_estudiante_aula(self, codigo_estudiante, codigo_aula):
        estudiante = None
        for e in self._estudiantes:
            if e.codigo_estudiante == codigo_estudiante and e.activo:
                estudiante = e
                break

        if estudiante is None:
            return (
                False,
                f"No se encontró estudiante activo con código {codigo_estudiante}",
            )

        aula = self._buscar_aula_obj(codigo_aula)
        if aula is None:
            return False, f"No se encontró aula con código {codigo_aula}"

        aula_anterior = self._buscar_aula_obj(estudiante.aula_asignada)
        if aula_anterior and aula_anterior.codigo_aula != codigo_aula:
            aula_anterior.remover_estudiante(codigo_estudiante)

        resultado = aula.agregar_estudiante(estudiante)
        if resultado:
            estudiante.aula_asignada = codigo_aula
            return True, f"Estudiante {estudiante.nombre} asignado a aula {codigo_aula}"
        return (
            False,
            f"El estudiante {estudiante.nombre} ya está en el aula {codigo_aula} o el aula está llena",
        )

    def dar_de_baja(self, codigo_estudiante):
        for est in self._estudiantes:
            if est.codigo_estudiante == codigo_estudiante and est.activo:
                est.darse_de_baja()
                aula = self._buscar_aula_obj(est.aula_asignada)
                if aula:
                    aula.remover_estudiante(codigo_estudiante)
                return True, f"Estudiante {est.nombre} dado de baja exitosamente"
        return False, f"No se encontró estudiante activo con código {codigo_estudiante}"

    def buscar_estudiante(self, codigo_estudiante):
        for est in self._estudiantes:
            if est.codigo_estudiante == codigo_estudiante:
                return est
        return None

    def buscar_profesor(self, codigo_profesor):
        for prof in self._profesores:
            if prof.codigo_profesor == codigo_profesor:
                return prof
        return None

    def buscar_aula(self, codigo_aula):
        for aula in self._aulas:
            if aula.codigo_aula == codigo_aula:
                return aula
        return None

    def listar_estudiantes_activos(self):
        return [e for e in self._estudiantes if e.activo]

    def listar_estudiantes_por_grado(self, grado):
        return [e for e in self._estudiantes if e.activo and e.grado == grado]
