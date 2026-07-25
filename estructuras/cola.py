class Cola:
    def __init__(self):
        self._elementos = []

    def encolar(self, elemento):
        self._elementos.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self._elementos.pop(0)

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self._elementos[0]

    def esta_vacia(self):
        return len(self._elementos) == 0

    def tamano(self):
        return len(self._elementos)

    def mostrar(self):
        return list(self._elementos)
