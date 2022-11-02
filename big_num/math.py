from .numbers import Numbers
from .trigonometry import sin_cos, atan_method, asin_method, constant_pi
from .constant_e import constant_e
from .logarithm import ln_method, log_method


def sin(x: 'Numbers', precision=40):
    """
    Seno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, True, precision)


def cos(x: 'Numbers', precision=40):
    """
    Coseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return sin_cos(x, False, precision)


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
    return atan_method(x, precision)


def acot(x: 'Numbers', precision: int = 500):
    """
    Arcotangente
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return constant_pi(precision, x.precision) / Numbers("2", "0") - atan_method(x, precision)


def asin(x: 'Numbers', precision: int = 100):
    """
    Arcoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return asin_method(x, precision)


def acos(x: 'Numbers', precision: int = 100):
    """
    Arcocoseno
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return constant_pi(precision, x.precision) / Numbers("2", "0") - atan_method(x, precision)


def pi(precision_decimal: int = 20, precision: int = 100):
    """
    Numero pi
    :param precision_decimal: presicion de decimales
    :param precision:  precision
    :return: resultado
    """
    return constant_pi(precision, precision_decimal)


def e(precision_decimal: int = 20, precision: int = 30):
    """
    Numero e
    :param precision_decimal: presicion de decimales
    :param precision:  precision
    :return: resultado
    """
    return constant_e(precision, precision_decimal)


def ln(x: 'Numbers', precision=100):
    """
    Logaritmo en base e
    :param x: numero
    :param precision: presicion de decimales
    :return: resultado
    """
    return ln_method(x, precision)


def log(x: 'Numbers', y: 'Numbers', precision=100):
    """
    Logaritmo
    :param x: numero
    :param y: base
    :param precision: presicion de decimales
    :return: resultado
    """
    return log_method(x, y, precision)
