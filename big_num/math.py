from .numbers import Numbers
from .trigonometry import sin_cos, atan_method, asin_method, constant_pi
from .constant_e import constant_e
from .logarithm import ln_method, log_method


def sin(x: 'Numbers', precision=40):
    return sin_cos(x, True, precision)


def cos(x: 'Numbers', precision=40):
    return sin_cos(x, False, precision)


def tan(x: 'Numbers'):
    return sin(x) / cos(x)


def cot(x: 'Numbers'):
    return cos(x) / sin(x)


def atan(x: 'Numbers', precision: int = 500):
    return atan_method(x, precision)


def acot(x: 'Numbers', precision: int = 500):
    return constant_pi(precision, x.precision) / Numbers("2", "0") - atan_method(x, precision)


def asin(x: 'Numbers', precision: int = 100):
    return asin_method(x, precision)


def acos(x: 'Numbers', precision: int = 100):
    return constant_pi(precision, x.precision) / Numbers("2", "0") - atan_method(x, precision)


def pi(precision_decimal=20, precision: int = 100):
    return constant_pi(precision, precision_decimal)


def e(precision_decimal=20, precision: int = 30):
    return constant_e(precision, precision_decimal)


def ln(x: 'Numbers', precision=100):
    return ln_method(x, precision)


def log(x: 'Numbers', y: 'Numbers', precision=100):
    return log_method(x, y, precision)
