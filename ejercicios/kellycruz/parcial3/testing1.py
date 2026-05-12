def calcular_media(*args):
   # if len(args) == 0:
    #    return 0
    """Devuelve el valor de la media o promedio de un conjunto de datos numericos
     

    Args:
       *args (int):un numero variable de argumentos que representan los datos numericos
    Returns:
        (float):el valor de la media o promedio de las
    """
    return (sum(*args)/len(*args))

assert(calcular_media([3,5,4]) == 4.0)
assert(calcular_media([10,,20,30]) == 20.0)
assert(calcular_media([1,2,3,4,5]) ==)
