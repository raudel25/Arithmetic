def pow_numbers(x, y: int, number1):
    result = number1
    for _ in range(y):
        result *= x

    return result


def algorithm_sqrt(x, y: int, number_y, precision, number10, number1):
    """
    Algoritmo para calcular la raiz n-esima
    :param x: numero
    :param y: indice
    :param precision: precision de los decimales
    :param number_y: numero (y) en el formato deseado
    :param number10:numero 10 en el formato deseado
    :param number1:numero 1 en el formato deseado
    :return: resultado en el formato deseado
    """

    (value, find) = approximate_integer(x, y, number10, number1)

    if find:
        return value

    value_y = number_y
    value_y_1 = value_y - number1

    #  https: // es.frwiki.wiki/wiki/Algorithme_de_calcul_de_la_racine_n-i % C3 % A8me
    for i in range(precision):
        aux = x / pow_numbers(value, y - 1,number1)
        value = number1 / value_y * (value_y_1 * value + aux)

    return value


def approximate_integer(x, y: int, number10, number1):
    value = number10
    while value < x:
        value *= number10

    if value > x:
        value = value / number10

    pow_value = pow_numbers(value, y,number1)

    while pow_value < x:
        value += number1
        pow_value = pow_numbers(value, y,number1)

    return (value, True) if pow_value == x else (value - number1, False)
