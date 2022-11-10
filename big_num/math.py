from .numbers import Numbers
from math_operations.trigonometry import sin_cos, atan_method, asin_method, constant_pi
from math_operations.constant_e import constant_e
from math_operations.logarithm import ln_method, log_method
from math_operations.pow_sqrt import algorithm_sqrt
import math
from .aux_operations import add_zeros_right


def sin(x: 'Numbers', precision=40):
    """
    Seno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, True, precision, Numbers.real1(), Numbers.real0())


def cos(x: 'Numbers', precision=40):
    """
    Coseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, False, precision, Numbers.real1(), Numbers.real0())


def tan(x: 'Numbers', precision: int = 40):
    """
    Tangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin(x, precision) / cos(x, precision)


def cot(x: 'Numbers', precision: int):
    """
    Cotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return cos(x, precision) / sin(x, precision)


def atan(x: 'Numbers', precision: int = 500):
    """
    Arctan
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return atan_method(x, precision, pi(), Numbers.real1(), Numbers.real0())


def acot(x: 'Numbers', precision: int = 500):
    """
    Arcotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    number_pi = pi()
    return number_pi / Numbers("2", "0") - atan_method(x, precision, number_pi, Numbers.real1(), Numbers.real0())


def asin(x: 'Numbers', precision: int = 100):
    """
    Arcoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return asin_method(x, precision, Numbers.real1(), Numbers.real0())


def acos(x: 'Numbers', precision: int = 100):
    """
    Arcocoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return pi() / Numbers("2", "0") - asin_method(x, precision, Numbers.real1(), Numbers.real0())


def pi(precision_decimal: int = 20, precision: int = 100):
    """
    Numero pi
    :param precision_decimal: presicion de decimales
    :param precision:  precision
    :return: resultado
    """
    return constant_pi(precision, Numbers('0', '5', True, precision_decimal), Numbers.real1(), Numbers.real0())


def e(precision_decimal: int = 20, precision: int = 30):
    """
    Numero e
    :param precision_decimal: presicion de decimales
    :param precision:  precision
    :return: resultado
    """
    return constant_e(precision, Numbers.real1(), Numbers('0', '0', True, precision_decimal))


def ln(x: 'Numbers', precision=100):
    """
    Logaritmo en base e
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return ln_method(x, precision, Numbers.real1(), Numbers.real0())


def log(x: 'Numbers', y: 'Numbers', precision=100):
    """
    Logaritmo
    :param x: numero
    :param y: base
    :param precision: presicion de decimales
    :return: resultado
    """
    return log_method(x, y, precision, Numbers.real1(), Numbers.real0())


def pow_value(x: 'Numbers', y: 'Numbers'):
    """
    Potencia
    :param x: base
    :param y: exponente
    :return: resultado
    """
    if y == Numbers.real0():
        return Numbers.real1()

    numerator: int = int(y.part_number + y.part_decimal)
    denominator: int = int(add_zeros_right('1', len(y.part_decimal)))
    gcd: int = math.gcd(numerator, denominator)

    result = sqrt(x, Numbers(str(denominator // gcd), '0'))
    result = result ** (numerator // gcd)

    return result if y.positive else Numbers.real1() / result


def sqrt(x: 'Numbers', z: 'Numbers'):
    """
    Determina la raiz n-esima de un numero
    :param x: numero
    :param z: indice
    :return: resultado
    """
    y = int(z.part_number)

    if y == 1:
        return x
    if x == Numbers.real0():
        return Numbers.real0()

    parity: bool = y & 1 == 0
    positive: bool = parity or x.positive

    if parity and not x.positive:
        raise Exception("Operacion Invalida (el resultado no es real)")

    result = algorithm_sqrt(x.abs, abs(y), Numbers(str(abs(y))), 40, Numbers('10'), Numbers.real1())

    return Numbers(result.part_number, result.part_decimal, positive) if y > 0 else Numbers.real1() / Numbers(
        result.part_number, result.part_decimal, positive)
