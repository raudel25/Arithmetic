from .aux_operations import eliminate_zeros_left, eliminate_zeros_right, eliminate_zeros_left_value, \
    equal_zeros_left_value,add_zeros_right
from .basic_operations_true_divsion import sum_number, sub_number, karatsuba_algorithm, compare_list, division_algorithm
from arithmetic_math.pow_sqrt import pow_numbers
from arithmetic_math.arithmetic_math import ArithmeticMath


class BigNumDecimal(ArithmeticMath):
    def __init__(self, precision=20):
        self.__precision = precision

    def __call__(self, number: str | float | list, positive: bool = True):
        return NumbersDecimal(number, positive, self.__precision)

    def precision(self):
        return self.__precision

    def number1(self):
        return NumbersDecimal('1', True, self.__precision)

    def number0(self):
        return NumbersDecimal('0', True, self.__precision)

    def float_to_number(self, number: float):
        return NumbersDecimal(abs(number), number >= 0, self.__precision)

    def number_to_int(self, number):
        return int(str(number).split('.')[0])

    def number_to_fraction(self, number):
        s = str(number).split('.')

        return int(s[0] + s[1]), int(add_zeros_right('1', len(s[1])))


class NumbersDecimal:
    def __init__(self, number: str | float | list, positive: bool, precision: int):
        self.__precision: int = precision
        self.__number_value: list = []

        if type(number) is not list:
            str_number: str = str(number)
            (part_int, part_decimal) = NumbersDecimal.__int_and_decimal(str_number)
            (part_int, part_decimal) = (eliminate_zeros_left(part_int), eliminate_zeros_right(part_decimal))
            self.__number_value = self.__create_value_number(part_int, part_decimal)
        else:
            self.__number_value = eliminate_zeros_left_value(number, precision)

        if self.__check_zero():
            positive = True

        self.__sign = '+' if positive else '-'
        self.__abs = self if positive else NumbersDecimal(number, True, precision)

    @property
    def sign(self):
        return self.__sign

    def real1(self):
        """
        Numero 1
        :return: Numero 1
        """
        return NumbersDecimal('1', True, self.__precision)

    def real0(self):
        """
        Numero 0
        :return: Numero 0
        """
        return NumbersDecimal('0', True, self.__precision)

    @property
    def positive(self) -> bool:
        """
        Determina si el numero es positivo
        :return: si es numero es positivo
        """
        return self.__sign == "+"

    @property
    def precision(self) -> int:
        """
        Determina la precision de decimales
        :return: precision de decimales
        """
        return self.__precision

    @property
    def abs(self) -> 'NumbersDecimal':
        """
        Determina el modulo de un numero
        :return: modulo del numero
        """
        return self.__abs

    @staticmethod
    def __int_and_decimal(s: str) -> tuple:
        """
        Determina si el string es correcto para un numero decimal
        :param s: string
        :return: si el string es correcto
        """
        part: list = s.split('.')

        return part[0], part[1] if len(part) == 2 else '0'

    def __create_value_number(self, part_int: str, part_decimal: str):
        """
        Representacion del numero
        :param part_int: parte entera
        :param part_decimal: parte decimal
        """
        number_value: list = [0 for _ in range(self.__precision + 1)]

        for i in range(len(part_decimal)):
            number_value[-i - 2] = int(part_decimal[i])

            if i + 1 == self.precision:
                break

        number_value[-1] = int(part_int[-1])

        for i in range(1, len(part_int)):
            number_value.append(int(part_int[-1 - i]))

        return number_value

    def __check_zero(self) -> bool:
        for i in self.__number_value:
            if i != 0:
                return False

        return True

    def compare_to(self, n: 'NumbersDecimal') -> int:
        """
        Compara el actual numero con otro
        :param n: numero para comparar
        :return: 1 si el numero introducido es menor, 0 si es igual y -1 si es mayor
        """
        if n is None:
            raise Exception("El valor introducido no es correcto")

        if self.__sign == n.__sign:
            if self.__sign == '+':
                return compare_list(self.__number_value, n.__number_value)
            return compare_list(n.__number_value, self.__number_value)

        if self.__sign == '+':
            return 1
        return -1

    def __eq__(self, obj):
        if type(obj) is not NumbersDecimal:
            return False

        return obj.__number_value == self.__number_value and obj.__sign == self.__sign

    def __str__(self) -> str:
        sign_str: str = "-" if self.__sign == "-" else ""

        part_decimal: str = ''
        part_int: str = ''

        for i in range(self.__precision):
            part_decimal = f'{str(self.__number_value[i])}{part_decimal}'
        for i in range(self.__precision, len(self.__number_value)):
            part_int = f'{str(self.__number_value[i])}{part_int}'

        part_decimal = eliminate_zeros_right(part_decimal)

        return f"{sign_str}{part_int}.{part_decimal}"

    def __add__(self, o: 'NumbersDecimal') -> 'NumbersDecimal':
        """
        Determina la suma
        :param o: sumando
        :return: resultado
        """
        x: 'NumbersDecimal' = self
        y: 'NumbersDecimal' = o

        if x == 0:
            return y
        if y == 0:
            return x

        (lx, ly) = (x.__number_value, y.__number_value)

        if x.sign == y.sign:
            return NumbersDecimal(sum_number(lx, ly), x.positive, self.__precision)
        compare = x.abs.compare_to(y.abs)
        if compare == 0:
            return self.real0()
        if compare == 1:
            return NumbersDecimal(sub_number(lx, ly), x.positive, self.__precision)

        return NumbersDecimal(sub_number(ly, lx), y.positive, self.__precision)

    def __sub__(self, o: 'NumbersDecimal') -> 'NumbersDecimal':
        return self + (-o)

    def __neg__(self) -> 'NumbersDecimal':
        return NumbersDecimal(self.__number_value, not self.positive, self.__precision)

    def __mul__(self, o: 'NumbersDecimal'):
        """
        Determina la multiplicacion
        :param o: factor
        :return: producto
        """
        x: 'NumbersDecimal' = self
        y: 'NumbersDecimal' = o

        positive = x.sign == y.sign

        if x.abs == self.real1():
            return NumbersDecimal(y.__number_value, positive, y.__precision)
        if y.abs == self.real1():
            return NumbersDecimal(x.__number_value, positive, x.__precision)

        (lx, ly) = equal_zeros_left_value(x.__number_value, y.__number_value)

        return NumbersDecimal(karatsuba_algorithm(lx, ly)[self.__precision:], positive, self.__precision)

    def __truediv__(self, o: 'NumbersDecimal'):
        """
        Determina la division
        :param o: divison
        :return: cociente
        """
        x: 'NumbersDecimal' = self
        y: 'NumbersDecimal' = o

        positive = x.sign == y.sign

        if y == self.real0():
            raise Exception("Operacion Invalida (division por 0)")
        if y.abs == self.real1():
            return NumbersDecimal(x.__number_value, positive, self.__precision)

        return NumbersDecimal(division_algorithm(x.__number_value, y.__number_value, self.__precision), positive,
                                   self.__precision)

    def __pow__(self, o: int):
        """
        Determina la potencia
        :param o: indice
        :return: potencia
        """
        return pow_numbers(self, o, self.real1())

    def __le__(self, o: 'NumbersDecimal'):
        return self.compare_to(o) != 1

    def __ge__(self, o: 'NumbersDecimal'):
        return self.compare_to(o) != -1

    def __lt__(self, o: 'NumbersDecimal'):
        return self.compare_to(o) == -1

    def __gt__(self, o: 'NumbersDecimal'):
        return self.compare_to(o) == 1
