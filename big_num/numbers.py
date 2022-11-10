from .aux_operations import eliminate_zeros_left, eliminate_zeros_right, equal_zeros_left, equal_zeros_right, \
    add_zeros_left, add_zeros_right
from .sum_operations import sum_str, sub_str
from math_operations.pow_sqrt import pow_numbers


class Numbers:
    def __init__(self, part_number: str, part_decimal: str = '0', positive: bool = True, precision: int = 20):
        (part_number, part_decimal) = (eliminate_zeros_left(
            part_number), eliminate_zeros_right(part_decimal))

        self.__precision = precision
        self.__part_number = part_number
        self.__part_decimal = self.determinate_precision(part_decimal)

        if self.check_zero():
            positive = True

        self.__sign = '+' if positive else '-'
        self.__abs = self if positive else Numbers(
            self.__part_number, self.__part_decimal, True, precision)

    @property
    def sign(self):
        return self.__sign

    """
    
    """

    @staticmethod
    def real1():
        """
        Numero 1
        :return: Numero 1
        """
        return Numbers("1", "0")

    @staticmethod
    def real0():
        """
        Numero 0
        :return: Numero 0
        """
        return Numbers("0", "0")

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
    def part_number(self) -> str:
        """
        Determina la parte entera
        :return: parte entera
        """
        return self.__part_number

    @property
    def part_decimal(self) -> str:
        """
        Determina la parte decimal
        :return: parte decimal
        """
        return self.__part_decimal

    @property
    def abs(self) -> 'Numbers':
        """
        Determina el modulo de un numero
        :return: modulo del numero
        """
        return self.__abs

    @staticmethod
    def check(s: str) -> bool:
        """
        Determina si el string es correcto para un numero decimal
        :param s: string
        :return: si el string es correcto
        """
        part: list = s.split('.')

        if len(part) > 2:
            return False

        for number in part:
            if not Numbers.check_zero(number):
                return False

        return True

    @staticmethod
    def check_number(number: str) -> bool:
        """
        Dado un string determina si es un numero
        :param number: string
        :return: si el string es un numero
        """
        for i in number:
            if i < '0' or i > '9':
                return False

        return True

    def determinate_precision(self, s: str) -> str:
        """
        Segun la precision trunca el numero
        :param s: numero con representacion de string
        :return: numero aproximado
        """
        return s[0:self.__precision] if len(s) >= self.__precision else s

    def check_zero(self) -> bool:
        """
        Determina si el string introducido es el 0
        :return: si el string introducido es el 0
        """
        return self.__part_number == '0' and self.__part_decimal == '0'

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
                return compare_number(self, n)
            return compare_number(n, self)

        if self.__sign == '+':
            return 1
        return -1

    def __eq__(self, obj):
        if type(obj) is not Numbers:
            return False

        return obj.__part_number == self.__part_number and obj.__part_decimal == self.__part_decimal and obj.__sign == self.__sign

    def __str__(self) -> str:
        sign_str = "-" if self.__sign == "-" else ""
        part_decimal = f".{self.__part_decimal}" if self.__part_decimal != "0" else ""

        return f"{sign_str}{self.__part_number}{part_decimal}"

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
        if x.sign == y.sign:
            return sum_operation(x, y, True, x.positive)
        compare = x.abs.compare_to(y.abs)
        if compare == 0:
            return Numbers.real0()
        if compare == 1:
            return sum_operation(x.abs, y.abs, False, x.positive)
        return sum_operation(y.abs, x.abs, False, y.positive)

    def __sub__(self, o: 'Numbers') -> 'Numbers':
        return self + (-o)

    def __neg__(self) -> 'Numbers':
        return Numbers(self.__part_number, self.__part_decimal, not self.positive, self.__precision)

    def __mul__(self, o: 'Numbers'):
        """
        Determina la multiplicacion
        :param o: factor
        :return: producto
        """
        x: 'Numbers' = self
        y: 'Numbers' = o

        positive = x.sign == y.sign
        cant_decimal = len(x.part_decimal) + len(y.part_decimal)

        if x.abs == Numbers.real1():
            return Numbers(y.part_number, y.part_decimal, positive)
        if y.abs == Numbers.real1():
            return Numbers(x.part_number, x.part_decimal, positive)

        m = Numbers(x.part_number + x.part_decimal, "0")
        n = Numbers(y.part_number + y.part_decimal, "0")

        result = karatsuba_algorithm(m, n).part_number

        if result == "0":
            return Numbers.real0()

        if len(result) < cant_decimal:
            result = add_zeros_left(
                result, cant_decimal - len(result))

        return Numbers(result[:len(result) - cant_decimal],
                       result[len(result) - cant_decimal:], positive, max(x.precision, y.precision))

    def __truediv__(self, o: 'Numbers'):
        """
        Determina la division
        :param o: divison
        :return: cociente
        """
        x: 'Numbers' = self
        y: 'Numbers' = o

        positive = x.sign == y.sign

        if y == Numbers.real0():
            raise Exception("Operacion Invalida (division por 0)")
        if y.abs == Numbers.real1():
            return Numbers(x.part_number, x.part_decimal, positive)

        (x_part_decimal, y_part_decimal) = (x.part_decimal, y.part_decimal)
        aux = equal_zeros_right(x_part_decimal, y_part_decimal)
        (x_part_decimal, y_part_decimal) = (aux[1], aux[2])

        m = Numbers(x.part_number + x_part_decimal, "0")
        n = Numbers(y.part_number + y_part_decimal, "0")

        (result, cant_decimal) = division_algorithm(
            m, n, max(x.precision, y.precision))

        if cant_decimal != 0:
            return (Numbers(result[: len(result) - cant_decimal],
                            result[len(result) - cant_decimal: len(result)], positive, max(x.precision, y.precision)))
        return Numbers(result, "0", positive)

    def __pow__(self, o: int):
        """
        Determina la potencia
        :param o: indice
        :return: potencia
        """
        return pow_numbers(self, o, Numbers.real1())

    def __le__(self, o: 'Numbers'):
        return self.compare_to(o) != 1

    def __ge__(self, o: 'Numbers'):
        return self.compare_to(o) != -1

    def __lt__(self, o: 'Numbers'):
        return self.compare_to(o) == -1

    def __gt__(self, o: 'Numbers'):
        return self.compare_to(o) == 1


# Metodos auxiliares

def compare_number(m: 'Numbers', n: 'Numbers') -> int:
    if len(m.part_number) > len(n.part_number):
        return 1
    if len(m.part_number) < len(n.part_number):
        return -1

    for i in range(len(m.part_number)):
        x = ord(m.part_number[i]) - 48
        y = ord(n.part_number[i]) - 48

        if x > y:
            return 1
        if x < y:
            return -1

    for i in range(min(len(m.part_decimal), len(n.part_decimal))):
        x = ord(m.part_decimal[i]) - 48
        y = ord(n.part_decimal[i]) - 48

        if x > y:
            return 1
        if x < y:
            return -1

    if len(m.part_decimal) > len(n.part_decimal):
        return -1
    if len(m.part_decimal) < len(n.part_decimal):
        return 1

    return 0


def sum_operation(x: 'Numbers', y: 'Numbers', sum_or_sub: bool, positive: bool):
    """
    Operacion para la suma
    :param x: sumando
    :param y: sumando
    :param sum_or_sub: determina si se debe sumar o restar
    :param positive: determina si el resultado es positivo
    :return: resultado
    """
    x_sum_decimal, y_sum_decimal = x.part_decimal, y.part_decimal
    x_sum_number, y_sum_number = x.part_number, y.part_number

    mayor_decimal, x_sum_decimal, y_sum_decimal = equal_zeros_right(
        x_sum_decimal, y_sum_decimal)
    mayor_number, x_sum_number, y_sum_number = equal_zeros_left(
        x_sum_number, y_sum_number)

    result = sum_str(x_sum_number + x_sum_decimal, y_sum_number +
                     y_sum_decimal) if sum_or_sub else sub_str(x_sum_number + x_sum_decimal,
                                                               y_sum_number + y_sum_decimal)

    part_decimal = result[mayor_number:len(result)] if len(
        result) == mayor_decimal + mayor_number else result[mayor_decimal + 1:len(result)]
    part_number = result[:mayor_number] if len(
        result) == mayor_decimal + mayor_number else result[:mayor_number + 1]

    return Numbers(eliminate_zeros_left(part_number), eliminate_zeros_right(part_decimal), positive,
                   max(x.precision, y.precision))


def karatsuba_algorithm(x: 'Numbers', y: 'Numbers') -> 'Numbers':
    """
    Algoritmo de karatsuba
    :param x: factor
    :param y: factor
    :return: producto
    """
    x_valor = x.part_number
    y_valor = y.part_number

    if x_valor == "0" or y_valor == "0":
        return Numbers.real0()
    if x_valor == "1":
        return y
    if y_valor == "1":
        return x
    if len(x_valor) == 1 and len(y_valor) == 1:
        return Numbers(str(int(x_valor) * int(y_valor)), '0')

    aux = equal_zeros_left(x_valor, y_valor)
    (x_valor, y_valor) = (aux[1], aux[2])

    # Algortimo de Karatsuba
    # https: // es.wikipedia.org/wiki/Algoritmo_de_Karatsuba

    n: int = len(x_valor) // 2
    m: int = len(x_valor)

    x1 = Numbers(x_valor[: n], "0")
    x0 = Numbers(x_valor[n: len(x_valor)], "0")
    y1 = Numbers(y_valor[:n], "0")
    y0 = Numbers(y_valor[n: len(y_valor)], "0")

    z2 = Numbers(add_zeros_right(karatsuba_algorithm(
        x1, y1).part_number, 2 * (m - n)), "0")
    z11 = Numbers(add_zeros_right(
        karatsuba_algorithm(x1, y0).part_number, m - n), "0")
    z12 = Numbers(add_zeros_right(
        karatsuba_algorithm(y1, x0).part_number, m - n), "0")
    z1 = z11 + z12
    z0 = Numbers(karatsuba_algorithm(x0, y0).part_number, "0")

    return z2 + z1 + z0


def division_algorithm(x: 'Numbers', y: 'Numbers', precision: int):
    """
    Algoritmo para la division
    :param x: dividendo
    :param y: divisor
    :param precision: precision de los decimales
    :return: cociente
    """
    cant_decimal = 0
    result = ""
    rest = Numbers.real0()
    for t in x.part_number:
        div = Numbers(rest.part_number + t, "0")
        (rest, result) = division_immediate(div, y, result)

    while rest != Numbers.real0():
        div = Numbers(rest.part_number + "0", "0")
        (rest, result) = division_immediate(div, y, result)
        cant_decimal += 1
        if cant_decimal == precision:
            break
    return result, cant_decimal


def division_immediate(div: 'Numbers', divisor: 'Numbers', result: str):
    aux: 'Numbers' = Numbers.real0()
    for j in range(9, -1, -1):
        aux = divisor * Numbers(str(j), "0")

        if aux <= div:
            result += str(j)
            break

    return div - aux, result
