from .numbers import Numbers
from .trigonometry import sin_cos, atan_method, asin_method, constant_pi


def sin(x: 'Numbers'):
    return sin_cos(x, True)


def cos(x: 'Numbers'):
    return sin_cos(x, False)


def tan(x: 'Numbers'):
    return sin(x) / cos(x)


def cot(x: 'Numbers'):
    return cos(x) / sin(x)


def atan(x: 'Numbers'):
    return atan_method(x)


def acot(x: 'Numbers'):
    return constant_pi() / Numbers("2", "0") - atan_method(x)


def asin(x: 'Numbers'):
    return asin_method(x)


def acos(x: 'Numbers'):
    return constant_pi() / Numbers("2", "0") - atan_method(x)


def pi():
    return constant_pi()
