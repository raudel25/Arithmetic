from decimal import Decimal
from arithmetic_math.arithmetic_math import ArithmeticMath


class DecimalNum(ArithmeticMath):
    def number1(self):
        return Decimal(1)

    def number0(self):
        return Decimal(0)

    def number2(self):
        return Decimal(2)

    def number05(self):
        return Decimal(0.5)

    def number6(self):
        return Decimal(6)
