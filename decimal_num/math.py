import fractions

from math_operations.trigonometry import sin_cos, atan_method, asin_method, constant_pi
from math_operations.constant_e import constant_e
from math_operations.logarithm import ln_method, log_method
from math_operations.pow_sqrt import algorithm_sqrt
import math
from decimal import *


def sin(x: 'Decimal', precision=40):
    """
    Seno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, True, precision, Decimal(1), Decimal(0))


def cos(x: 'Decimal', precision=40):
    """
    Coseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, False, precision, Decimal(1), Decimal(0))


def tan(x: 'Decimal', precision: int = 40):
    """
    Tangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin(x, precision) / cos(x, precision)


def cot(x: 'Decimal', precision: int):
    """
    Cotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return cos(x, precision) / sin(x, precision)


def atan(x: 'Decimal', precision: int = 500):
    """
    Arctan
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    number_pi = pi()
    return atan_method(x, precision, number_pi, Decimal(1), Decimal(0))


def acot(x: 'Decimal', precision: int = 500):
    """
    Arcotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    number_pi = pi()
    return pi() - atan_method(x, precision, number_pi, Decimal(1), Decimal(0))


def asin(x: 'Decimal', precision: int = 100):
    """
    Arcoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return asin_method(x, precision, Decimal(1), Decimal(0))


def acos(x: 'Decimal', precision: int = 100):
    """
    Arcocoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return pi() / Decimal(2) - asin_method(x, precision, Decimal(1), Decimal(0))


def pi(precision: int = 100):
    """
    Numero pi
    :param precision:  precision
    :return: resultado
    """
    return constant_pi(precision, Decimal(0.5), Decimal(1), Decimal(0))


def e(precision: int = 30):
    """
    Numero e
    :param precision:  precision
    :return: resultado
    """
    return constant_e(precision, Decimal(1), Decimal(0))


def ln(x: 'Decimal', precision=100):
    """
    Logaritmo en base e
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return ln_method(x, precision, Decimal(1), Decimal(0))


def log(x: 'Decimal', y: 'Decimal', precision=100):
    """
    Logaritmo
    :param x: numero
    :param y: base
    :param precision: presicion de decimales
    :return: resultado
    """
    return log_method(x, y, precision, Decimal(1), Decimal(0))


def pow_value(x: 'Decimal', y: 'Decimal'):
    """
    Potencia
    :param x: base
    :param y: exponente
    :return: resultado
    """
    if y == Decimal(0):
        return Decimal(1)

    f=fractions.Fraction(y)
    numerator: int = f.numerator
    denominator: int = f.denominator
    gcd: int = math.gcd(numerator, denominator)

    result = sqrt(x, Decimal(denominator // gcd))
    result = result ** (numerator // gcd)

    return result if y >= Decimal(0) else Decimal(1) / result


def sqrt(x: 'Decimal', z: 'Decimal'):
    """
    Determina la raiz n-esima de un numero
    :param x: numero
    :param z: indice
    :return: resultado
    """
    y: int = int(z)
    print(y)

    if y == 1:
        return x
    if x == Decimal(0):
        return Decimal(0)

    parity: bool = y & 1 == 0
    positive: bool = parity or x >= Decimal(0)

    if parity and not x >= Decimal(0):
        raise Exception("Operacion Invalida (el resultado no es real)")

    result = algorithm_sqrt(abs(x), abs(y), Decimal(abs(y)), 40, Decimal(10), Decimal(1))

    if not positive:
        result = Decimal(0) - result

    return result if y > 0 else Decimal(1) / result
