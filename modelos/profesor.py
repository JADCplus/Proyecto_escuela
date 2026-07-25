from modelos.persona import Persona


class Profesor(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_aula, codigo_profesor):
        super().__init__(cui, nombre, edad, sexo)
        self.codigo_aula = codigo_aula
        self.codigo_profesor = codigo_profesor

    def ver_info(self):
        print(
            f"Codigo de Profesor: {self.codigo_profesor} | CUI: {self.cui} | Nombre: {self.nombre} | Edad: {self.get_edad()} | Sexo: {self.sexo} | Aula: {self.codigo_aula}"
        )
