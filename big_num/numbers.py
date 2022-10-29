from .aux_operations import eliminate_zeros_left, eliminate_zeros_right


class Numbers:
    def __init__(self, part_number: str, part_decimal: str, positive: bool = True, precision: int = 20):
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
    def positive(self) -> bool:
        return self.__sign == "+"

    @property
    def presicion(self) -> int:
        return self.__precision

    @property
    def part_number(self) -> str:
        return self.__part_number

    @property
    def part_decimal(self) -> str:
        return self.__part_decimal

    @property
    def abs(self) -> 'Numbers':
        return self.__abs

    @property
    def sign(self) -> str:
        return self.__sign

    @staticmethod
    def check(s: str) -> bool:
        part: list = s.split('.')

        if len(part) > 2:
            return False

        for number in part:
            if not Numbers.__check_zero(number):
                return False

        return True

    @staticmethod
    def check_number(number: str) -> bool:
        for i in number:
            if i < '0' or i > '9':
                return False

        return True

    def determinate_precision(self, s: str) -> str:
        return s[0:self.__precision] if len(s) >= self.__precision else s

    def check_zero(self) -> bool:
        return self.__part_number == '0' and self.__part_decimal == '0'

    def compare_to(self, n: 'Numbers') -> int:
        if n is None:
            raise Exception("El valor introducido no es correcto")

        if self.__sign == n.__sign:
            if self.__sign == '+':
                return self.compare_number(self, n)
            return self.compare_number(n, self)

        if self.__sign == '+':
            return 1
        return -1

    def __eq__(self, obj):
        if type(obj) is not Numbers:
            return False

        return obj.__part_number == self.__part_number and obj.__part_decimal == self.__part_decimal and obj.__sign == self.__sign

    def compare_number(self, m: 'Numbers', n: 'Numbers') -> int:
        if len(m.__part_number) > len(n.__part_number):
            return 1
        if len(m.__part_number) < len(n.__part_number):
            return -1

        for i in range(len(m.part_number)):
            x = ord(m.__part_number[i]) - 48
            y = ord(n.__part_number[i]) - 48

            if x > y:
                return 1
            if x < y:
                return -1

        for i in range(min(len(m.__part_decimal), len(n.__part_decimal))):
            x = ord(m.__part_decimal[i]) - 48
            y = ord(n.__part_decimal[i]) - 48

            if x > y:
                return 1
            if x < y:
                return -1

        if len(m.__part_decimal) > len(n.__part_decimal):
            return -1
        if len(m.__part_decimal) < len(n.__part_decimal):
            return 1

        return 0

    def __str__(self) -> str:
        sign = "-" if self.__sign == "-" else ""
        part_decimal = f".{self.__part_decimal}" if self.__part_decimal != "0" else ""

        return f"{sign}{self.__part_number}{part_decimal}"
