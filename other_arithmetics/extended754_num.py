from .extended754 import Extended754
from arithmetic_math.arithmetic_math import ArithmeticMath
from typing import Union


class Extended754Num(ArithmeticMath):
    def __init__(self, base: int, exponent: int, mantissa: int, round_nearest: bool = True, repr_base: int = 10,
                 char_map: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", repr_len: Union[int, None] = None):
        self.__extended = Extended754(base, exponent, mantissa, round_nearest, repr_base, char_map, repr_len)

    def __call__(self, number: Union[str, float], input_base: int = 0):
        return self.__extended(number, input_base)

    def number1(self):
        return self.__extended(1)

    def number0(self):
        return self.__extended(0)

    def float_to_number(self, number: float):
        return self.__extended(number)

    def number_to_int(self, number):
        return int(str(number).split('.')[0])