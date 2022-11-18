from decimal import Decimal
from arithmetic_math.arithmetic_math import ArithmeticMath


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
