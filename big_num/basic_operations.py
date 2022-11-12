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
        drag = -n if n < 0 else 0
        n = n + 10 ** base10 if n < 0 else n
        sub.append(n)

    return sub


def karatsuba_algorithm(x: list, y: list, base10: int) -> list:
    (x, y) = equal_zeros_left_value(x, y)
    """
    Algoritmo de karatsuba
    :param x: factor
    :param y: factor
    :return: producto
    """
    zeros = [0 for _ in x]
    if x == zeros or y == zeros:
        return zeros

    if len(x) == 1:
        return [x[0] * y[0] // (10 ** base10), x[0] * y[0] % (10 ** base10)]

    # Algortimo de Karatsuba
    # https: // es.wikipedia.org/wiki/Algoritmo_de_Karatsuba

    n: int = len(x) // 2
    m: int = len(x)

    x1 = x[:n]
    x0 = x[n: len(x)]
    y1 = y[:n]
    y0 = y[n: len(y)]

    z2 = add_zeros_right_value(karatsuba_algorithm(x1, y1, base10), 2 * (m - n))
    z11 = add_zeros_right_value(karatsuba_algorithm(x1, y0, base10), m - n)
    z12 = add_zeros_right_value(karatsuba_algorithm(y1, x0, base10), m - n)
    z1 = sum_number(z11, z12, base10)
    z0 = karatsuba_algorithm(x0, y0, base10)

    return sum_number(z2, sum_number(z1, z0, base10), base10)


def division_algorithm(x: list, y: list, base10: int, precision: int):
    """
    Algoritmo para la division
    :param x: dividendo
    :param y: divisor
    :param precision: precision de los decimales
    :return: cociente
    """
    cant_decimal = 0
    result = []
    rest = 0
    for t in x:
        # div = Numbers(rest.part_number + t, "0")
        (rest, aux) = division_immediate([rest, t], y, base10)

    while rest != Numbers.real0():
        div = Numbers(rest.part_number + "0", "0")
        (rest, result) = division_immediate(div, y, result)
        cant_decimal += 1
        if cant_decimal == precision:
            break
    return result, cant_decimal


def division_immediate(div: list, divisor: list, base10: int) -> tuple:
    aux: list = []
    result = 0
    for j in range(9, -1, -1):
        aux = karatsuba_algorithm([j], divisor, base10)

        if compare_list(div, aux) != -1:
            result = j
            break

    return j, sub_number(div, aux)


def compare_list(x: list, y: list) -> int:
    (x, y) = equal_zeros_left_value(x, y)

    for i in range(len(x) - 1, -1, -1):
        if x[i] > y[i]:
            return 1
        if y[i] > x[1]:
            return -1

    return 0
