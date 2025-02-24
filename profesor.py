class Profesor:
    total_profesores = 0  # Contador de instancias

    def __init__(self, nombre, especialidad, cursos_asignados):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        Profesor.total_profesores += 1  # Aumenta el contador cada vez que se crea un profes# # or

    def asignar_curso(self):
        self.cursos_asignados += 1

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Especialidad: {self.especialidad}, cursos asignados: {self.cursos_asignados}")

    def __str__(self):
        return f"Nombre: {self.nombre}, Especialidad: {self.especialidad}, cursos asignados: {self.cursos_asignados}"

    def __repr__(self):
        return f"Nombre: {self.nombre}, Especialidad: {self.especialidad}, cursos asignados: {self.cursos_asignados}"

    def desde_tupla(self):
        pass

    def esta_disponible_para_nuevo_curso(self):
        pass

