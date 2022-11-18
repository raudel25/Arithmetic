def scalate_one(x, number10, number1) -> tuple:
    """
    Llevar un numer fraccionario a entero
    :param x: numero
    :param number10: numero 10
    :param number1: numero 1
    :return: numero transformado y la cantidad de lugares decimales modificados
    """
    cant: int = 0

    while x < number1:
        x *= number10
        cant += 1

    return x, cant
