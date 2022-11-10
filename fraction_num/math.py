from math_operations.trigonometry import sin_cos, atan_method, asin_method, constant_pi
from math_operations.constant_e import constant_e
from math_operations.logarithm import ln_method, log_method
from math_operations.pow_sqrt import algorithm_sqrt
import math
from fractions import Fraction


def sin(x: 'Fraction', precision=40):
    """
    Seno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, True, precision, Fraction(1), Fraction(0))


def cos(x: 'Fraction', precision=40):
    """
    Coseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, False, precision, Fraction(1), Fraction(0))


def tan(x: 'Fraction', precision: int = 40):
    """
    Tangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin(x, precision) / cos(x, precision)


def cot(x: 'Fraction', precision: int):
    """
    Cotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return cos(x, precision) / sin(x, precision)


def atan(x: 'Fraction', precision: int = 500):
    """
    Arctan
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    number_pi = pi()
    return atan_method(x, precision, number_pi, Fraction(1), Fraction(0))


def acot(x: 'Fraction', precision: int = 500):
    """
    Arcotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    number_pi = pi()
    return pi() - atan_method(x, precision, number_pi, Fraction(1), Fraction(0))


def asin(x: 'Fraction', precision: int = 100):
    """
    Arcoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return asin_method(x, precision, Fraction(1), Fraction(0))


def acos(x: 'Fraction', precision: int = 100):
    """
    Arcocoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return pi() / Fraction(2) - asin_method(x, precision, Fraction(1), Fraction(0))


def pi(precision: int = 100):
    """
    Numero pi
    :param precision:  precision
    :return: resultado
    """
    return constant_pi(precision, Fraction(1, 2), Fraction(1), Fraction(0))


def e(precision: int = 30):
    """
    Numero e
    :param precision:  precision
    :return: resultado
    """
    return constant_e(precision, Fraction(1), Fraction(0))


def ln(x: 'Fraction', precision=100):
    """
    Logaritmo en base e
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return ln_method(x, precision, Fraction(1), Fraction(0))


def log(x: 'Fraction', y: 'Fraction', precision=100):
    """
    Logaritmo
    :param x: numero
    :param y: base
    :param precision: presicion de decimales
    :return: resultado
    """
    return log_method(x, y, precision, Fraction(1), Fraction(0))


def pow_value(x: 'Fraction', y: 'Fraction'):
    """
    Potencia
    :param x: base
    :param y: exponente
    :return: resultado
    """
    if y == Fraction(0):
        return Fraction(1)

    numerator: int = y.numerator
    denominator: int = y.denominator
    gcd: int = math.gcd(numerator, denominator)

    result = sqrt(x, Fraction(denominator // gcd))
    result = result ** (numerator // gcd)

    return result if y >= Fraction(0) else Fraction(1) / result


def sqrt(x: 'Fraction', z: 'Fraction'):
    """
    Determina la raiz n-esima de un numero
    :param x: numero
    :param z: indice
    :return: resultado
    """
    y: int = z.numerator
    print(y)

    if y == 1:
        return x
    if x == Fraction(0):
        return Fraction(0)

    parity: bool = y & 1 == 0
    positive: bool = parity or x >= Fraction(0)

    if parity and not x >= Fraction(0):
        raise Exception("Operacion Invalida (el resultado no es real)")

    result = algorithm_sqrt(abs(x), abs(y), Fraction(abs(y)), 40, Fraction(10), Fraction(1))

    if not positive:
        result = Fraction(0) - result

    return result if y > 0 else Fraction(1) / result
