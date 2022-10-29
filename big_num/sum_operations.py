def sum_str(x: str, y: str) -> str:
    result = ''
    drag = False
    s = len(x)

    for i in range(0, s):
        n = int(x[s - 1 - i]) + int(y[s - 1 - i])

        n = n + 1 if drag else n
        drag = n >= 10
        result = str(n % 10) + result

    if drag:
        result = '1' + result

    return result


def sub_str(x: str, y: str) -> str:
    sub = ''
    drag = False
    s = len(x)

    for i in range(s):
        n = int(x[s - 1 - i]) - 48 - (int(y[s - 1 - i]) - 48)

        n = n - 1 if drag else n
        drag = n < 0
        n = n + 10 if n < 0 else n
        sub = str(n) + sub

    return sub
