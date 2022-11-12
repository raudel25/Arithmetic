from .aux_operations import add_zeros_right_value, equal_zeros_left_value


def sum_number(x: list, y: list) -> list:
    (x, y) = equal_zeros_left_value(x, y)
    result = []
    drag = 0

    for i in range(len(x)):
        n = x[i] + y[i]

        n = n + drag
        drag = n // 10
        result.append(n % 10)

    result.append(drag)

    return result


def sub_number(x: list, y: list) -> list:
    (x, y) = equal_zeros_left_value(x, y)
    sub = []
    drag = 0
    s = len(x)

    for i in range(s):
        n = x[i] - y[i]

        n = n - drag
        drag = 1 if n < 0 else 0
        n = n + 10 if n < 0 else n
        sub.append(n)

    return sub


def karatsuba_algorithm(x: list, y: list) -> list:
    """
    Algoritmo de karatsuba
    :param x: factor
    :param y: factor
    :return: producto
    """
    (x, y) = equal_zeros_left_value(x, y)

    zeros = [0 for _ in x]
    if x == zeros or y == zeros:
        return zeros

    if len(x) == 1:
        return [x[0] * y[0] % 10, x[0] * y[0] // 10]

    # Algortimo de Karatsuba
    # https: // es.wikipedia.org/wiki/Algoritmo_de_Karatsuba

    n: int = len(x) // 2
    m: int = len(x)

    x0 = x[:n]
    x1 = x[n: len(x)]
    y0 = y[:n]
    y1 = y[n: len(y)]

    z2 = add_zeros_right_value(karatsuba_algorithm(x1, y1), 2 * n)
    z11 = add_zeros_right_value(karatsuba_algorithm(x1, y0), n)
    z12 = add_zeros_right_value(karatsuba_algorithm(y1, x0), n)
    z1 = sum_number(z11, z12)
    z0 = karatsuba_algorithm(x0, y0)

    return sum_number(z2, sum_number(z1, z0))


def division_algorithm(x: list, y: list, precision):
    """
    Algoritmo para la division
    :param x: dividendo
    :param y: divisor
    :param precision: precision de los decimales
    :return: cociente
    """
    cant_decimal = 0
    result = []
    rest = []
    x=x.copy()
    x.reverse()
    for t in x:
        (aux, rest) = division_immediate([t] + rest, y)
        result.append(aux)

    for _ in range(precision):
        (aux, rest) = division_immediate([0] + rest, y)
        result.append(aux)

    result.reverse()
    return result


def division_immediate(div: list, divisor: list) -> tuple:
    aux: list = []
    result = 0
    # print(div)
    for j in range(9, -1, -1):
        aux = karatsuba_algorithm([j], divisor)
        # print(div,aux)
        # print(compare_list(div, aux))

        if compare_list(div, aux) != -1:
            result = j
            break


    return result, sub_number(div, aux)


#
#
def compare_list(x: list, y: list) -> int:
    (x, y) = equal_zeros_left_value(x, y)

    for i in range(len(x) - 1, -1, -1):
        if x[i] > y[i]:
            return 1
        if y[i] > x[i]:
            return -1

    return 0
