import math

from .aux_operations import add_zeros_right_value, equal_zeros_left_value, eliminate_zeros_left_value


def sum_number(x: list, y: list, base10: int) -> list:
    (x, y) = equal_zeros_left_value(x, y)
    result = []
    drag = 0

    for i in range(len(x)):
        n = x[i] + y[i]

        n = n + drag
        drag = n // base10
        result.append(n % base10)

    if drag != 0:
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
        n = n + base10 if n < 0 else n
        sub.append(n)

    return sub


def simple_multiplication(x: list, y: int, base10: int):
    drag = 0
    result = []

    for i in x:
        n = i * y + drag

        drag = n // base10
        result.append(n % base10)

    if drag != 0:
        result.append(drag)

    return result


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
        return [x[0] * y[0] % base10, x[0] * y[0] // base10]

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


def division_algorithm_d(x: list, y: list, precision: int, base10: int) -> list:
    """
    Algoritmo para la division
    :param base10:base
    :param x: dividendo
    :param y: divisor
    :param precision: precision de los decimales
    :return: cociente
    """
    (x, y) = equal_zeros_left_value(x, y)
    (x, y) = normalize(x, y, base10)

    result = []
    rest = x[-len(y) + 1:len(x)]

    for t in range(len(x) - len(y), -1, -1):
        (aux, rest) = division_immediate([x[t]] + rest, y, base10, precision)
        result.append(aux)

    for _ in range(precision):
        (aux, rest) = division_immediate([0] + rest, y, base10, precision)
        result.append(aux)

    result.reverse()
    return result


def normalize(x: list, y: list, base10: int) -> tuple:
    if y[-1] < base10 // 2:
        y_aux = eliminate_zeros_left_value(y, -1)
        y = add_zeros_right_value(y_aux, len(y) - len(y_aux))
        x = add_zeros_right_value(x, len(y) - len(y_aux))

        mult: int = 1
        aux = y[-1] // (base10 // 10)

        if aux == 0:
            mult = base10 // (10 ** int(math.log10(y[-1]))) // 10
            aux = y[-1] * mult // (base10 // 10)

        if aux == 1:
            mult *= 5
        elif aux == 2:
            mult *= 3
        elif aux == 3:
            mult *= 2
        elif aux == 4:
            mult *= 2

        return simple_multiplication(x, mult, base10), simple_multiplication(y, mult, base10)

    return x, y


def division_immediate(div: list, divisor: list, base10: int, precision: int) -> tuple:
    if len(div) < len(divisor):
        return 0, div

    if len(div) == len(divisor):
        result = div[-1] // divisor[-1]
    else:
        result = (div[-1] * base10 + div[-2]) // divisor[-1]

    while True:
        aux = simple_multiplication(divisor, result, base10)

        if compare_list(div, aux) != -1:
            break

        result -= 1

    return result, eliminate_zeros_left_value(sub_number(div, aux, base10), precision)


def compare_list(x: list, y: list) -> int:
    (x, y) = equal_zeros_left_value(x, y)

    for i in range(len(x) - 1, -1, -1):
        if x[i] > y[i]:
            return 1
        if y[i] > x[i]:
            return -1

    return 0
