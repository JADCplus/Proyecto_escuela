class Persona:
    def __init__(self, cui, nombre, edad, sexo):
        self.cui = cui
        self.nombre = nombre
        self.__edad = edad
        self.sexo = sexo

    def ver_info(self):
        pass

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad <= 0:
            print("Dato ingresado invalido")
            return False
        else:
            self.__edad = edad
            return True


class Profesor(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_aula, codigo_profesor ):
        super().__init__(cui,nombre,edad,sexo)
        self.codigo_aula = codigo_aula
        self.codigo_profesor = codigo_profesor

    def ver_info(self):
        print(f"Codigo de Profesor: {self.codigo_profesor} | CUI: {self.cui} | Nombre: {self.nombre} | Edad: {self.get_edad()} | Sexo: {self.sexo} | Aula: {self.codigo_aula}")

class Estudiante(Persona):
    def __init__(self, cui, nombre, edad, sexo, codigo_estudiante,codigo_aula, estado):
        super().__init__(cui, nombre, edad, sexo)
        self.codigo_estudiante = codigo_estudiante
        self.codigo_aula = codigo_aula
        self.estado = estado

    def ver_info(self):
        print(f"Codigo de Estudiante: {self.codigo_estudiante} | CUI: {self.cui} | Nombre: {self.nombre} | Edad: {self.get_edad()} | Sexo: {self.sexo} | Aula: {self.codigo_aula} | Estado: {self.estado} ")

class Aula:
    def __init__(self, codigo_aula, capacidad_maxima, estudiantes, codigo_profesor):
        self.codigo_aula = codigo_aula
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = estudiantes
        self.codigo_profesor = codigo_profesor

    def ver_info_aula(self):
        print(f"Codigo de Aula: {self.codigo_aula} | Capacidad: {self.capacidad_maxima} | Codigo de Profesor: {self.codigo_profesor}")


