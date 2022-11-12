from .aux_operations import eliminate_zeros_left, eliminate_zeros_right, eliminate_zeros_left_value, equal_zeros_left_value
from .basic_operations import sum_number, sub_number, karatsuba_algorithm, compare_list, division_algorithm
from math_operations.pow_sqrt import pow_numbers


class BigNum:
    def __init__(self, base10: int = 10, precision=20):
        self.__base10 = base10
        self.__precision = precision

    def __call__(self, number: str | float | list, positive: bool = True):
        return Numbers(number, positive, self.__precision)

    def base10(self):
        return self.__base10

    def precision(self):
        return self.__precision

    def number1(self):
        return


class Numbers:
    def __init__(self, number: str | float | list, positive: bool, precision: int):
        self.__precision: int = precision
        self.__number_value: list = []

        if type(number) is not list:
            str_number: str = str(number)
            (part_int, part_decimal) = Numbers.__int_and_decimal(str_number)
            (part_int, part_decimal) = (eliminate_zeros_left(part_int), eliminate_zeros_right(part_decimal))
            self.__number_value = self.__create_value_number(part_int, part_decimal)
        else:
            self.__number_value = eliminate_zeros_left_value(number, precision)

        if self.__check_zero():
            positive = True

        self.__sign = '+' if positive else '-'
        self.__abs = self if positive else Numbers(number, True, precision)

    @property
    def sign(self):
        return self.__sign

    def real1(self):
        """
        Numero 1
        :return: Numero 1
        """
        return Numbers('1', True, self.__precision)

    def real0(self):
        """
        Numero 0
        :return: Numero 0
        """
        return Numbers('0', True, self.__precision)

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

    # @property
    # def part_int(self) -> str:
    #     """
    #     Determina la parte entera
    #     :return: parte entera
    #     """
    #     return self.__part_int
    #
    # @property
    # def part_decimal(self) -> str:
    #     """
    #     Determina la parte decimal
    #     :return: parte decimal
    #     """
    #     return self.__part_decimal

    @property
    def abs(self) -> 'Numbers':
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

        # part_int = add_zeros_left(part_int, self.__base10 - len(part_int) % self.__base10)
        # part_decimal = add_zeros_right(part_decimal, self.__base10 - len(part_decimal) % self.__base10)

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

    def compare_to(self, n: 'Numbers') -> int:
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
        if type(obj) is not Numbers:
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

    def __add__(self, o: 'Numbers') -> 'Numbers':
        """
        Determina la suma
        :param o: sumando
        :return: resultado
        """
        x: 'Numbers' = self
        y: 'Numbers' = o

        if x == 0:
            return y
        if y == 0:
            return x

        (lx, ly) = (x.__number_value, y.__number_value)

        if x.sign == y.sign:
            return Numbers(sum_number(lx, ly), x.positive, self.__precision)
        compare = x.abs.compare_to(y.abs)
        if compare == 0:
            return self.real0()
        if compare == 1:
            return Numbers(sub_number(lx, ly), x.positive, self.__precision)

        return Numbers(sub_number(ly, lx), y.positive, self.__precision)

    def __sub__(self, o: 'Numbers') -> 'Numbers':
        return self + (-o)

    def __neg__(self) -> 'Numbers':
        return Numbers(self.__number_value, not self.positive, self.__precision)

    def __mul__(self, o: 'Numbers'):
        """
        Determina la multiplicacion
        :param o: factor
        :return: producto
        """
        x: 'Numbers' = self
        y: 'Numbers' = o

        positive = x.sign == y.sign

        if x.abs == self.real1():
            return Numbers(y.__number_value, positive, y.__precision)
        if y.abs == self.real1():
            return Numbers(x.__number_value, positive, x.__precision)

        (lx, ly) = equal_zeros_left_value(x.__number_value, y.__number_value)

        return Numbers(karatsuba_algorithm(lx, ly)[self.__precision:], positive, self.__precision)

    def __truediv__(self, o: 'Numbers'):
        """
        Determina la division
        :param o: divison
        :return: cociente
        """
        x: 'Numbers' = self
        y: 'Numbers' = o

        positive = x.sign == y.sign

        if y == self.real0():
            raise Exception("Operacion Invalida (division por 0)")
        if y.abs == self.real1():
            return Numbers(x.__number_value, positive,self.__precision)

        # (x_part_decimal, y_part_decimal) = (x.part_decimal, y.part_decimal)
        # aux = equal_zeros_right(x_part_decimal, y_part_decimal)
        # (x_part_decimal, y_part_decimal) = (aux[1], aux[2])
        #
        # m = Numbers(x.part_number + x_part_decimal, "0", True, max(x.precision, y.precision))
        # n = Numbers(y.part_number + y_part_decimal, "0", True, max(x.precision, y.precision))
        #
        # (result, cant_decimal) = division_algorithm(m, n, max(x.precision, y.precision))
        #
        # if cant_decimal != 0:
        #     return (Numbers(result[: len(result) - cant_decimal],
        #                     result[len(result) - cant_decimal: len(result)], positive, max(x.precision, y.precision)))
        return Numbers(division_algorithm(x.__number_value, y.__number_value,self.__precision), positive, self.__precision)

    def __pow__(self, o: int):
        """
        Determina la potencia
        :param o: indice
        :return: potencia
        """
        return pow_numbers(self, o, self.real1())

    def __le__(self, o: 'Numbers'):
        return self.compare_to(o) != 1

    def __ge__(self, o: 'Numbers'):
        return self.compare_to(o) != -1

    def __lt__(self, o: 'Numbers'):
        return self.compare_to(o) == -1

    def __gt__(self, o: 'Numbers'):
        return self.compare_to(o) == 1
