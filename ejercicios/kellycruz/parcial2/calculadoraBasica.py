#funciones basicas
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b 

def multi(a,b):
    return a * b 

def div(a,b):
    return a / b
#menu de opciones
opcion=0 
while(opcion != 5):
    print("----menu de opciones----")
    print("1.sumar 2 valores")
    print("2.restar 2")
    print("3.multiplicar 2 valores")
    print("4.dividir programa")
    print("5.terminar programa")
    opcion=int(input("\nselecciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #suma de dos numeros
        n1 = float(input("/nIngresa el primer numero a sumar: "))
        n2 = float(input("ingresa el segundo numero a sumar: "))
        print(f"resultado se la suma: {suma(n1)}")
    elif opcion == 2:
        #resta de dos numeros
        n1 = float(input("/nIngresa el primer minuendo: "))
        n2 = float(input("ingresa el segundo sustraendo: "))
        print(f"cociente de la resta {resta(n1,n2)}")
    elif opcion == 3:
        #multiplicacion de dos numeros
        n1 = float(input("/nIngresa el primer factor: "))
        n2 = float(input("ingresa el segundo fsctor: "))
        print(f"producto resultante: {multi(n1,n2,)}")
    elif opcion == 4:
        #division de dos numeros
        n1 = float(input("/nIngresa el dividendo: "))
        n2 = float(input("ingresa el divisor: "))
        print(f"cociente resultante: {div(n1,n2)}")
    elif opcion == 5:
        #finalizacin del programa
        print("programa finalizado...")
    else:
        #mensaje de error por opcion no valida
        print("opcion seleccionada no valida,intenta nuevamente!")