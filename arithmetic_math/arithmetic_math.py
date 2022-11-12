from abc import ABC, abstractmethod
from .trigonometry import sin_cos, atan_method, asin_method, constant_pi
from .constant_e import constant_e
from .logarithm import ln_method, log_method
from .pow_sqrt import algorithm_sqrt


class ArithmeticMath(ABC):
    @abstractmethod
    def number1(self):
        pass

    @abstractmethod
    def number0(self):
        pass

    @abstractmethod
    def number2(self):
        pass

    @abstractmethod
    def number05(self):
        pass

    @abstractmethod
    def number6(self):
        pass

    def sin(self, x: 'ArithmeticMath', precision=40):
        """
        Seno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return sin_cos(x, True, precision, self.number1(), self.number0())

    def cos(self, x: 'ArithmeticMath', precision=40):
        """
        Coseno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return sin_cos(x, False, precision, self.number1(), self.number0())

    def tan(self, x: 'ArithmeticMath', precision: int = 40):
        """
        Tangente
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return self.sin(x, precision) / self.cos(x, precision)

    def cot(self, x: 'ArithmeticMath', precision: int):
        """
        Cotangente
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return self.cos(x, precision) / self.sin(x, precision)

    def atan(self, x: 'ArithmeticMath', precision: int = 500):
        """
        Arctan
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        number_pi = self.pi()
        return atan_method(x, precision, number_pi, self.number1(), self.number0())

    def acot(self, x: 'ArithmeticMath', precision: int = 500):
        """
        Arcotangente
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        number_pi = self.pi()
        return self.pi() - atan_method(x, precision, number_pi, self.number1(), self.number0())

    def asin(self, x: 'ArithmeticMath', precision: int = 100):
        """
        Arcoseno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return asin_method(x, precision, self.number1(), self.number0())

    def acos(self, x: 'ArithmeticMath', precision: int = 100):
        """
        Arcocoseno
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return self.pi() / self.number2() - asin_method(x, precision, self.number1(), self.number0())

    def pi(self, precision: int = 100):
        """
        Numero pi
        :param precision:  precision
        :return: resultado
        """
        return constant_pi(precision, self.number6(), self.number05(), self.number1(), self.number0())

    def e(self, precision: int = 30):
        """
        Numero e
        :param precision:  precision
        :return: resultado
        """
        return constant_e(precision, self.number1(), self.number0())

    def ln(self, x: 'ArithmeticMath', precision=100):
        """
        Logaritmo en base e
        :param x: numero
        :param precision: presicion de decimales
        :return: resultado
        """
        return ln_method(x, precision, self.number1(), self.number0())

    def log(self, x: 'ArithmeticMath', y: 'ArithmeticMath', precision=100):
        """
        Logaritmo
        :param x: numero
        :param y: base
        :param precision: presicion de decimales
        :return: resultado
        """
        return log_method(x, y, precision, self.number1(), self.number0())

    # def pow_value(x: 'ArithmeticMath', y: 'ArithmeticMath'):
    #     """
    #     Potencia
    #     :param x: base
    #     :param y: exponente
    #     :return: resultado
    #     """
    #     if y == ArithmeticMath(0):
    #         return ArithmeticMath(1)
    # 
    #     numerator: int = y.numerator
    #     denominator: int = y.denominator
    #     gcd: int = math.gcd(numerator, denominator)
    # 
    #     result = sqrt(x, ArithmeticMath(denominator // gcd))
    #     result = result ** (numerator // gcd)
    # 
    #     return result if y >= ArithmeticMath(0) else ArithmeticMath(1) / result
    # 
    # def sqrt(x: 'ArithmeticMath', z: 'ArithmeticMath'):
    #     """
    #     Determina la raiz n-esima de un numero
    #     :param x: numero
    #     :param z: indice
    #     :return: resultado
    #     """
    #     y: int = z.numerator
    #     print(y)
    # 
    #     if y == 1:
    #         return x
    #     if x == ArithmeticMath(0):
    #         return ArithmeticMath(0)
    # 
    #     parity: bool = y & 1 == 0
    #     positive: bool = parity or x >= ArithmeticMath(0)
    # 
    #     if parity and not x >= ArithmeticMath(0):
    #         raise Exception("Operacion Invalida (el resultado no es real)")
    # 
    #     result = algorithm_sqrt(abs(x), abs(y), ArithmeticMath(abs(y)), 40, ArithmeticMath(10), ArithmeticMath(1))
    # 
    #     if not positive:
    #         result = ArithmeticMath(0) - result
    # 
    #     return result if y > 0 else ArithmeticMath(1) / result
