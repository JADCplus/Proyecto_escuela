class Persona:
    def __init__(self, cui, nombre, edad, sexo):
        self.cui = cui
        self.nombre = nombre
        self.__edad = edad
        self.sexo = sexo

    @property
    def edad(self):
        return self.__edad

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
