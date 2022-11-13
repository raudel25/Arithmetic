from fractions import Fraction
from arithmetic_math.arithmetic_math import ArithmeticMath


class FractionNum(ArithmeticMath):
    def __call__(self, number: str | float):
        return Fraction(number)

    def number1(self):
        return Fraction(1)

    def number0(self):
        return Fraction(0)

    def float_to_number(self, number: float):
        return Fraction(number)

    def number_to_int(self, number):
        return number.numerator

    def number_to_fraction(self, number):
        return number.numerator,number.denominator
