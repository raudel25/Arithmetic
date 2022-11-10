from big_num.numbers import Numbers


def constant_e(precision: int, number1, number0_precision):
    """
    Aproximacion de e
    :param precision: cantidad de iteraciones
    :param number1: numero 1 en el formato especifico
    :param number0_precision: numero 0 en el formato especifico con la cantidad de decimales especificada
    :return: resultado
    """
    e = number0_precision
    fact: 'Numbers' = number1
    index = number0_precision

    # Formula de taylor e^x
    # https://es.wikipedia.org/wiki/Serie_de_Taylor
    for i in range(precision):
        if i != 0:
            fact *= index
        e += number1 / fact
        index += number1

    return e
