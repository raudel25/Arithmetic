from .numbers import Numbers
from math_operations.trigonometry import sin_cos, atan_method, asin_method, constant_pi
from math_operations.constant_e import constant_e
from math_operations.logarithm import ln_method, log_method


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
    return atan_method(x, precision, Numbers.real1(), Numbers.real0())


def acot(x: 'Numbers', precision: int = 500):
    """
    Arcotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return constant_pi(precision, x.precision, Numbers('6'), Numbers.real1(), Numbers.real0()) / Numbers("2", "0") - \
           atan_method(x, precision, Numbers.real1(), Numbers.real0())


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
    return constant_pi(precision, x.precision, Numbers('6'), Numbers.real1(),
                       Numbers.real0()) / Numbers("2", "0") - \
           atan_method(x, precision, Numbers.real1(), Numbers.real0())


def pi(precision_decimal: int = 20, precision: int = 100):
    """
    Numero pi
    :param precision_decimal: presicion de decimales
    :param precision:  precision
    :return: resultado
    """
    return constant_pi(precision, precision_decimal, Numbers('6'), Numbers.real1(), Numbers.real0())


def e(precision_decimal: int = 20, precision: int = 30):
    """
    Numero e
    :param precision_decimal: presicion de decimales
    :param precision:  precision
    :return: resultado
    """
    return constant_e(precision, precision_decimal, Numbers.real1(), Numbers('0', '0', True, precision_decimal))


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
