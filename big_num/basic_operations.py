from .aux_operations import add_zeros_right_value, equal_zeros_left_value


def sum_number(x: list, y: list, base10: int) -> list:
    (x, y) = equal_zeros_left_value(x, y)
    result = []
    drag = 0

    for i in range(len(x)):
        n = x[i] + y[i]

        n = n + drag
        drag = n // (10 ** base10)
        result.append(n % (10 ** base10))

    result.append(drag)

    return result


def sub_number(x: list, y: list, base10: int) -> list:
    (x, y) = equal_zeros_left_value(x, y)
    sub = []
    drag = 0
    s = len(x)

    for i in range(s):
        n = x[i] - y[i]

        n = n - drag
        drag = 1 if n < 0 else 0
        n = n + 10 ** base10 if n < 0 else n
        sub.append(n)

    return sub


def karatsuba_algorithm(x: list, y: list, base10: int) -> list:
    """
    Algoritmo de karatsuba
    :param base10: indice de la base
    :param x: factor
    :param y: factor
    :return: producto
    """
    (x, y) = equal_zeros_left_value(x, y)

    zeros = [0 for _ in x]
    if x == zeros or y == zeros:
        return zeros

    if len(x) == 1:
        return [x[0] * y[0] % (10 ** base10), x[0] * y[0] // (10 ** base10)]

    # Algortimo de Karatsuba
    # https: // es.wikipedia.org/wiki/Algoritmo_de_Karatsuba

    n: int = len(x) // 2

    x0 = x[:n]
    x1 = x[n: len(x)]
    y0 = y[:n]
    y1 = y[n: len(y)]

    z2 = add_zeros_right_value(karatsuba_algorithm(x1, y1, base10), 2 * n)
    z11 = add_zeros_right_value(karatsuba_algorithm(x1, y0, base10), n)
    z12 = add_zeros_right_value(karatsuba_algorithm(y1, x0, base10), n)
    z1 = sum_number(z11, z12, base10)
    z0 = karatsuba_algorithm(x0, y0, base10)

    return sum_number(z2, sum_number(z1, z0, base10), base10)


def division_algorithm(x: list, y: list, precision: int, base10: int):
    """
    Algoritmo para la division
    :param x: dividendo
    :param y: divisor
    :param precision: precision de los decimales
    :return: cociente
    """
    result = []
    rest = []
    x = x.copy()
    x.reverse()
    for t in x:
        (aux, rest) = division_immediate([t] + rest, y, base10)
        result.append(aux)

    for _ in range(precision):
        (aux, rest) = division_immediate([0] + rest, y, base10)
        result.append(aux)

    result.reverse()
    return result


def division_immediate(div: list, divisor: list, base10: int) -> tuple:
    aux: list = []
    result = 0

    for j in range(10 ** base10 - 1, -1, -1):
        aux = karatsuba_algorithm([j], divisor, base10)

        if compare_list(div, aux) != -1:
            result = j
            break

    return result, sub_number(div, aux, base10)


def compare_list(x: list, y: list) -> int:
    (x, y) = equal_zeros_left_value(x, y)

    for i in range(len(x) - 1, -1, -1):
        if x[i] > y[i]:
            return 1
        if y[i] > x[i]:
            return -1

    return 0
