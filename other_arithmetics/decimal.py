from decimal import Decimal
from arithmetic_math.arithmetic_math import ArithmeticMath
from big_num.aux_operations import add_zeros_right


class DecimalNum(ArithmeticMath):
    def __call__(self, number: str | float):
        return Decimal(number)

    def number1(self):
        return Decimal(1)

    def number0(self):
        return Decimal(0)

    def float_to_number(self, number: float):
        return Decimal(number)

    def number_to_int(self, number):
        return int(str(number).split('.')[0])

    def number_to_fraction(self, number):
        s = str(number).split('.')

        if len(s)==1:
            return int(s[0]),1

        return int(s[0] + s[1]), int(add_zeros_right('1', len(s[1])))
