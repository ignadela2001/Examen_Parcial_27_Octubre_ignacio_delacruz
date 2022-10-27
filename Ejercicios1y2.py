#Ejercicios 1 y 2
class Alumno():
    def _init_(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def _str_(self):
        return "Nombre: {}, notas: {} ".format( self.nombre, self.notas )
    print("La clase alumno se ha creado con exito")
    def calificacion(self, notas):
        if notas >= 5:
            print("El alumno ha aprobado")
        elif notas > 10:
            print("Las notas van del 0 al 10.")
        elif notas < 0:
            print("Las notas van del 0 al 10.")
        else:
            print("El alumno ha suspendido")
Alumno("Jorge", 5)
Alumno.calificacion(5)
alumnos = (("Jorge", 5),("Alicia", 3),("Alberto", 10))
for alumno in alumnos:
    Alumno.calificacion(alumno)
for alumno in (alumno):
    Alumno(alumno)

