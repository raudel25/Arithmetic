def constant_e(precision: int, number1, number0):
    """
    Aproximacion de e
    :param precision: cantidad de iteraciones
    :param number1: numero 1 en el formato especifico
    :param number0: numero 0 en el formato especifico
    :return: resultado
    """
    e = number0
    fact = number1
    index = number0

    # Formula de taylor e^x
    # https://es.wikipedia.org/wiki/Serie_de_Taylor
    for i in range(precision):
        if i != 0:
            fact *= index
        e += number1 / fact
        index += number1

    return e
