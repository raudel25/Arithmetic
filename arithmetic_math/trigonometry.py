def sin_cos(x, sin: bool, precision, number1, number0):
    """
    Calcular seno o coseno
    :param x: numero
    :param sin: determina si se calcula seno o coseno
    :param precision: cantidad de iteraciones
    :param number1: numero 1 en el formato especifico
    :param number0: numero 0 en el formato especifico
    :return: resultado
    """
    filter1 = (lambda a: (a & 1) == 0) if sin else (lambda a: (a & 1) != 0)
    filter2 = (lambda a: a % 4 == 1) if sin else (lambda a: a % 4 == 0)

    result = number0
    pow_value = number1
    fact = number1
    index = number0

    # Serie de taylor sen x cos x
    # https: // es.wikipedia.org / wiki / Serie_de_Taylor
    for i in range(precision):
        if i != 0:
            fact *= index
        if i != 0:
            pow_value *= x

        index += number1

        if filter1(i):
            continue

        result = result + pow_value / fact if filter2(i) else result - pow_value / fact

    return result


def atan_method(x, precision, pi, number1, number0):
    """
    Calcular el arcotangente
    :param x: numero
    :param precision: cantidad de iteraciones
    :param pi:numero pi en el formato establecido
    :param number1: numero 1 en el formato especifico
    :param number0: numero 0 en el formato especifico
    :return: resultado
    """
    # arctan(x)+arctan(1/x)=pi/2
    # arctan(1/x)=arccot(x)

    number2 = number1 + number1

    x_abs = x if x >= number0 else number0 - x

    if x_abs > number1:
        return pi - atan_method(number1 / x, precision, pi, number1, number0)

    pow_value = x
    index = number1
    arctan = number0
    xx = x * x

    for i in range(1, 2 * precision, 2):
        arctan = arctan + pow_value / index if i % 4 == 1 else arctan - pow_value / index
        pow_value *= xx
        index += number2

    return arctan


def asin_method(x, precision, number1, number0):
    """
    Calcular el arcoseno
    :param x: numero
    :param precision: cantidad de iteraciones
    :param number1: numero 1 en el formato especifico
    :param number0: numero 0 en el formato especifico
    :return: resultado
    """
    x_abs = x if x >= number0 else number0 - x
    if x_abs > number1:
        raise Exception("Operacion Invalida (arcsin recive valores entre 1 y -1)")

    index = number1
    even = number1
    odd = number1
    pow_value = number1
    arcsin = number0

    for i in range(1, precision):
        pow_value *= x

        if (i & 1) == 0:
            even *= index

        if (i & 1) == 1:
            arcsin += (odd * pow_value) / (even * index)
            odd *= index

        index += number1

    return arcsin


def constant_pi(precision,number6, number05, number1, number0):
    return asin_method(number05, precision, number1, number0) * number6
