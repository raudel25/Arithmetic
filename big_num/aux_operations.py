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

    return ind, add_zeros_left(x, ind - len(x)), add_zeros_right(y, ind - len(y))


def equal_zeros_right(x: str, y: str) -> tuple:
    ind: int = max(len(x), len(y))

    return ind, add_zeros_right(x, ind - len(x)), add_zeros_right(y, ind - len(y))
