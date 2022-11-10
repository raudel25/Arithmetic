from big_num.numbers import Numbers


def ln_method(x, precision, number1, number0):
    """
    Aproximacion del logaritmo natular
    :param x: arugumento
    :param precision: cantidad de iteraciones
    :param number1: numero 1 en el formato especifico
    :param number0: numero 0 en el formato especifico
    :return: resultado
    """
    # ln(1/x)=-ln(x)
    x_abs = x if x >= number0 else number0 - x
    positive: bool = x_abs > number1
    x = number1 / x if positive else x
    x = number1 - x

    pow_value = x
    index = number1
    ln = number0

    # Serie de Taylor ln(1-x)
    # https://es.wikipedia.org/wiki/Serie_de_Taylor
    for i in range(1, precision):
        ln += pow_value / index
        pow_value *= x
        index += number1

    return ln if positive else -ln


def log_method(x, y, precision: int, number1, number0):
    pow_value = number1
    index: int = 0

    while pow_value <= y:
        if pow_value == y:
            return Numbers(str(index), '0')
        pow_value *= x
        index += 1

    return ln_method(x, precision, number1, number0) / ln_method(y, precision, number1, number0)
