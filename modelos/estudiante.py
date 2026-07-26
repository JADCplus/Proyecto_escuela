from modelos.persona import Persona


class Estudiante(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_estudiante, codigo_aula, estado):
        super().__init__(cui, nombre, edad, sexo)
        self.codigo_estudiante = codigo_estudiante
        self.codigo_aula = codigo_aula
        self.estado = estado

    def ver_info(self):
        print(
            f"Codigo de Estudiante: {self.codigo_estudiante} | CUI: {self.cui} | Nombre: {self.nombre} | Edad: {self.get_edad()} | Sexo: {self.sexo} | Aula: {self.codigo_aula} | Estado: {self.estado} "
        )


