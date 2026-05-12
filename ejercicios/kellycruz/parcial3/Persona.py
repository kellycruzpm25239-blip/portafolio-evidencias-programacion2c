"""
crea una clase Persona con los siguientes atributos:nombre,edad,genero y nacionalidad.
Agrega un metodo para imprimir los datos de la persona y otro metodo para calcular el 
año de nacimiento de la pesona.
Crea un objeto de la clase Persona y uiliza los metodos para mostrar su informacion y
calcular su año de nacimiento. 
"""
import datetime

class Persona:

    def __init__(self,nombre,edad,genero,nacionalidad = "mexico"):
        self.nombre =nombre
        self.edad =edad
        self.genero = genero
        self.nacionalidad = nacionalidad

    def informacion(self):
        print("---- informacion----")
        print(f"{self.nombre} ({self.genero})")
        print(f"edad: {self.edad} años")
        print(f"nacionalidad: {self.nacionalidad}")

    def calcularNacimiento(self):
        year = datetime.date.today().year
        return year - self.edad

def main():
    objPersona = Persona("kelly cruz", 17,"femenino")
    objPersona.informacion()
    print(f"año de nacimiento: {objPersona.calcularNacimiento()}")
if __name__ == "__main__":
    main()