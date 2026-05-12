class Perro:
    #constructor de la clase Perro
    def _init_ (self,nombre,raza,edad,especie):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.especie = especie

    #metodo para imprimir los datos del perro  
    def imprimirDatos(self):
        print("nombre: ", self.nombre)
        print("raza: ", self.raza)
        print("edad: ", self.edad)
        print("especie: ", self.especie)

def main():
    #crear un objeto de la clase Perro
    perro1 = Perro("firulais","labrador",5)
    perro1.imprimirDatos()
    perro2 = Perro("rex","pastor aleman",3)
    perro2.imprimirDatos()
    print("informacion del perro 2:",perro2.nombre, perro2.raza, perro2.edad)
    perro3 = Perro("max","bulldog",2)
    perro3.imprimirDatos()
    perro4 = Perro("Dante")
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "pastor belga"
    perro2.imprimirDatos()
    perro5 = Perro("raya","sianes",1)
    perro5.especie = "felis catus"
    perro5.imprimirDatos()

if __name__ == "_main_":
    main()
