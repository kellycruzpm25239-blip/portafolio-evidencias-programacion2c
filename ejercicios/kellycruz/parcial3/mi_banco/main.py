from banco import Banco
from cuenta import Cuenta


def main():

    banco = Banco()

    while True:

        print("""
MENU DE PROGRAMA MI BANCO

1. Apertura nueva cuenta
2. Ver clientes
3. Depositar a cuenta
4. Retirar de una cuenta
5. Transferencia entre cuentas
6. Buscar cuenta
7. Eliminar una cuenta
8. Salir del programa
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pass

        elif opcion == "2":
            pass

        elif opcion == "3":
            pass

        elif opcion == "4":
            pass

        elif opcion == "5":
            pass

        elif opcion == "6":
            pass

        elif opcion == "7":
            pass

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__== "_main_":
    main()