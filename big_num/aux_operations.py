def add_zeros_left(s: str, cant: int) -> str:
    return ''.join(['0' for _ in range(cant)]) + s


def add_zeros_right(s: str, cant: int) -> str:
    return s + ''.join(['0' for _ in range(cant)])


def eliminate_zeros_left(s: str) -> str:
    ind: int = -1

    for i in range(len(s)):
        if s[i] != '0':
            ind = i
            break

    if ind == -1:
        return '0'

    return s[ind:len(s)]


def eliminate_zeros_right(s: str) -> str:
    ind: int = -1

    for i in range(len(s) - 1, -1, -1):
        if s[i] != '0':
            ind = i
            break

    if ind == -1:
        return '0'

    return s[0:ind + 1]


def equal_zeros_left(x: str, y: str) -> tuple:
    ind: int = max(len(x), len(y))

    return ind, add_zeros_left(x, ind - len(x)), add_zeros_left(y, ind - len(y))


def equal_zeros_right(x: str, y: str) -> tuple:
    ind: int = max(len(x), len(y))

    return ind, add_zeros_right(x, ind - len(x)), add_zeros_right(y, ind - len(y))


def eliminate_zeros_left_value(numer_value: list, precision: int) -> list:
    l: list = []
    act: bool = False

    for i in range(len(numer_value) - 1, -1, -1):
        if numer_value[i] != 0 or i == precision:
            act = True

        if act:
            l.append(numer_value[i])

    l.reverse()
    return l


def add_zeros_left_value(numer_value: list, cant: int) -> list:
    l: list = [x for x in numer_value]

    for _ in range(cant):
        l.append(0)

    return l


def add_zeros_right_value(numer_value: list, cant: int) -> list:
    l: list = [0 for _ in range(cant)]

    return l + numer_value


def equal_zeros_left_value(x: list, y: list) -> tuple:
    lx: list = add_zeros_left_value(x, max(len(x), len(y)) - len(x))
    ly: list = add_zeros_left_value(y, max(len(x), len(y)) - len(y))

    return lx, ly
