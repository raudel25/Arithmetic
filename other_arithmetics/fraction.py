from fractions import Fraction
from arithmetic_math.arithmetic_math import ArithmeticMath


class FractionNum(ArithmeticMath):
    def __call__(self, number: str | float):
        return Fraction(number)

    def number1(self):
        return Fraction(1)

    def number0(self):
        return Fraction(0)

    def number2(self):
        return Fraction(2)

    def number05(self):
        return Fraction(1,2)

    def number6(self):
        return Fraction(6)
