import math

from abc import ABC, abstractmethod
from .trigonometry import sin_cos, atan_method, asin_method, constant_pi
from .constant_e import constant_e
from .logarithm import ln_method, log_method
from .pow_sqrt import algorithm_sqrt
from .aux import scalate_one
from big_num.aux_operations import add_zeros_right


class ArithmeticMath(ABC):
    @abstractmethod
    def number1(self):
        pass

    @abstractmethod
    def number0(self):
        pass

    @abstractmethod
    def float_to_number(self, number: float):
        """
        Conbertir de float al formato de la aritmetica
        :param number: float
        :return: numero en formato de la aritmetica
        """
        pass

    @abstractmethod
    def number_to_int(self, number):
        """
        Convertir a entero
        :param number: numero en forrmato de la aritmetica
        :return: numero entero
        """
        pass

    def number_to_fraction(self, number):
        """
        Convertir del formato de la aritmetica a fraccion
        :param number: numero en forrmato de la aritmetica
        :return: fraccion
        """
        s = str(number).split('.')

        if len(s) == 1:
            return int(s[0]), 1

        return int(s[0] + s[1]), int(add_zeros_right('1', len(s[1])))

    def sin(self, x, precision=50):
        """
        Seno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return sin_cos(x, True, precision, self.number1(), self.number0())

    def cos(self, x, precision=50):
        """
        Coseno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return sin_cos(x, False, precision, self.number1(), self.number0())

    def tan(self, x, precision: int = 40):
        """
        Tangente
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return self.sin(x, precision) / self.cos(x, precision)

    def cot(self, x, precision: int):
        """
        Cotangente
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return self.cos(x, precision) / self.sin(x, precision)

    def atan(self, x, precision: int = 1000):
        """
        Arctan
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        number_pi = self.pi()
        return atan_method(x, precision, number_pi, self.number1(), self.number0())

    def acot(self, x, precision: int = 1000):
        """
        Arcotangente
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        number_pi = self.pi()
        return self.pi() - atan_method(x, precision, number_pi, self.number1(), self.number0())

    def asin(self, x, precision: int = 200):
        """
        Arcoseno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return asin_method(x, precision, self.number1(), self.number0())

    def acos(self, x, precision: int = 200):
        """
        Arcocoseno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return self.pi() / self.float_to_number(2) - asin_method(x, precision, self.number1(), self.number0())

    def pi(self, precision: int = 200):
        """
        Numero pi
        :param precision:  precision
        :return: resultado
        """
        return constant_pi(precision, self.float_to_number(6), self.float_to_number(0.5), self.number1(),
                           self.number0())

    def e(self, precision: int = 40):
        """
        Numero e
        :param precision:  precision
        :return: resultado
        """
        return constant_e(precision, self.number1(), self.number0())

    def ln(self, x, precision=150):
        """
        Logaritmo en base e
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return ln_method(x, precision, self.number1(), self.number0())

    def log(self, x, y, precision=150):
        """
        Logaritmo
        :param x: numero
        :param y: base
        :param precision: presicion de decimales
        :return: resultado
        """
        return log_method(x, y, precision, self.number1(), self.number0())

    def pow_value(self, x, y):
        """
        Potencia
        :param x: base
        :param y: exponente
        :return: resultado
        """
        if y == self.number0():
            return self.number1()

        (numerator, denominator) = self.number_to_fraction(y)

        gcd: int = math.gcd(numerator, denominator)

        result = self.sqrt(x, denominator // gcd)
        result = result ** (numerator // gcd)

        return result if y >= self.number0() else self.number1() / result

    def sqrt(self, x, y: int, precision: int = 50):
        """
        Determina la raiz n-esima de un numero
        :param x: numero
        :param y: indice
        :param precision: presicion de decimales
        :return: resultado
        """

        if y == 1:
            return x
        if x == self.number0():
            return self.number0()

        parity: bool = y & 1 == 0
        positive: bool = parity or x >= self.number0()

        x = x if x >= self.number0() else -x

        number10 = self.float_to_number(10)
        (aux, ind) = scalate_one(x, number10, self.number1())
        if ind!=0:
            aux *= number10 ** (y - ind % y)

        if parity and not x >= self.number0():
            raise Exception("Operacion Invalida (el resultado no es real)")

        result = algorithm_sqrt(aux, y, self.float_to_number(y), precision, self.float_to_number(10), self.number1())

        result /= (number10 ** ((ind + y - ind % y) // y))

        if not positive:
            result = -result

        return result if y > 0 else self.number1() / result
