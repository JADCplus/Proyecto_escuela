from modelos.persona import Persona


class Estudiante(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_estudiante, codigo_aula, grado):
        super().__init__(cui, nombre, edad, sexo)
        self._codigo_estudiante = codigo_estudiante
        self._codigo_aula = codigo_aula
        self._grado = grado
        self._activo = True

    @property
    def codigo_estudiante(self):
        return self._codigo_estudiante

    @property
    def codigo_aula(self):
        return self._codigo_aula

    @codigo_aula.setter
    def codigo_aula(self, valor):
        self._codigo_aula = valor

    @property
    def grado(self):
        return self._grado

    @property
    def activo(self):
        return self._activo

    def darse_de_baja(self):
        self._activo = False
        return True

    def ver_info(self):
        estado = "Activo" if self._activo else "Inactivo"
        print(
            f"Codigo de Estudiante: {self._codigo_estudiante} | CUI: {self.cui} | "
            f"Nombre: {self.nombre} | Edad: {self.get_edad()} | "
            f"Sexo: {self.sexo} | Aula: {self._codigo_aula} | Estado: {estado}"
        )

    def __str__(self):
        estado = "Activo" if self._activo else "Inactivo"
        return (
            f"Código: {self._codigo_estudiante} | Nombre: {self.nombre} | "
            f"CUI: {self.cui} | Grado: {self._grado} | "
            f"Aula: {self._codigo_aula} | Estado: {estado}"
        )
