def validar_cui(cui):
    if not isinstance(cui, str):
        return False
    return len(cui) == 13 and cui.isdigit()


def validar_edad(edad):
    if not isinstance(edad, int):
        return False
    return 3 <= edad <= 100


def validar_sexo(sexo):
    return isinstance(sexo, str) and sexo.upper() in ["M", "F"]


def validar_codigo(codigo):
    return isinstance(codigo, str) and len(codigo) > 0


def validar_grado(grado):
    return isinstance(grado, int) and 1 <= grado <= 6
