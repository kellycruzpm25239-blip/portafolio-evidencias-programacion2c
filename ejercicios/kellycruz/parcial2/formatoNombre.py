def formato_nombre(name,lastName):
    """
    Devuelve el nombre de usuario en el formato Apellido, Nombre.

    Argumentos:
        name (str): Primer nombre del usuario
        lastName (str): Apellidopaterno de el usuario

    Retorno: 
        (str): El nombre completo en formato Apellido,Nombre.
    """
    return f"{lastName}, {name}"

#funcion main para la ejecucion del codigo. 
def main():
    _name = input("introduce tu primer nombre: ")
    _lastName = input("introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastName))

