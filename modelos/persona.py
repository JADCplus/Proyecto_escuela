from utils.validaciones import validar_cui, validar_sexo


class Persona:
    def __init__(self, cui, nombre, edad, sexo):
        self._cui = cui
        self._nombre = nombre
        self.__edad = edad
        self._sexo = sexo

    @property
    def cui(self):
        return self._cui

    @cui.setter
    def cui(self, valor):
        if not validar_cui(valor):
            raise ValueError("CUI inválido. Debe tener exactamente 13 dígitos numéricos.")
        self._cui = valor

    @property
    def nombre(self):
        return self._nombre

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        if not validar_sexo(valor):
            raise ValueError("Sexo inválido. Debe ser 'M' o 'F'.")
        self._sexo = valor.upper()

    @property
    def edad(self):
        return self.__edad

    def ver_info(self):
        pass

    def rol(self):
        return "Persona"
