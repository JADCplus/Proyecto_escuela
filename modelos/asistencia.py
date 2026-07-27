class Asistencia:
    def __init__(self,codigo_aula, codigo_estudiante, nombre_estudiante, estado):
        self._codigo_aula = codigo_aula
        self._codigo_estudiante = codigo_estudiante
        self._nombre_estudiante = nombre_estudiante
        self._estado = estado

    def ver_asistencia(self):
        print(f"Codigo de aula: {self._codigo_aula}  | Codigo de estudiante: {self._codigo_estudiante}  | Nombre: {self._nombre_estudiante}  | Estado: {self._estado}")

    def __str__(self):
        return f"Aula: {self._codigo_aula} | Estudiante: {self._nombre_estudiante} ({self._codigo_estudiante}) | Estado: {self._estado}"

