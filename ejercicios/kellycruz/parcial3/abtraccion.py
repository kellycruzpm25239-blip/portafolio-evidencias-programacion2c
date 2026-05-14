class Cafetera:
    def preparar_cafe(self):
        self._hervir_agua()
        self._moler_cafe()
        print("cafe listo!")

        def __hervir_agua(self):
            print("hirviendo el agua")

        def __moleer_cafe(self):
            print("moliendo cafe")

def main():
    cafetera = Cafetera()
    cafetera.preparar_cafe()

if __name__ == "__main__":
    main()