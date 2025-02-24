class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante
    def __str__(self):
        return f'Nombre: {self.nombre}, edad: {self.edad}, cursos: {self.cursos_inscritos}'
    def __repr__(self):
        return (f'Nombre: {self.nombre}',f'edad: {self.edad}',f'cursos: {self.cursos_inscritos}')
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, edad: {self.edad}, cursos: {self.cursos_inscritos}')
    def inscribir_curso(self,curso):
        self.cursos_inscritos.append(curso)
    @classmethod
    def desde_tupla(cls, tupla):
        return cls(*tupla)
    @staticmethod
    def es_mayor_de_edad(edad):
        if edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")