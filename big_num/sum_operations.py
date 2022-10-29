from .numbers import Numbers
from .aux_operations import eliminate_zeros_left, eliminate_zeros_right, add_zeros_left, add_zeros_right, equal_zeros_left, equal_zeros_right


def sum(x: 'Numbers', y: 'Numbers') -> 'Numbers':
    if x == 0:
        return y
    if y == 0:
        return x
    if x.sign == y.sign:
        return sum_operation(x, y, True, x.positive)
    compare = x.abs.compare_to(y.abs)
    if compare == 0:
        return 0
    if compare == 1:
        return sum_operation(x.abs, y.abs, False, x.positive)
    return sum_operation(y.abs, x.abs, False, y.positive)


def sum_operation(x: str, y: str, sum_or_sub: bool, positive: bool) -> 'Numbers':
    x_sum_decimal, y_sum_decimal = x.part_decimal, y.part_decimal
    x_sum_number, y_sum_number = x.part_number, y.part_number

    mayor_decimal, x_sum_decimal, y_sum_decimal = equal_zeros_right(
        x_sum_decimal, y_sum_decimal)
    mayor_number, x_sum_number, y_sum_number = equal_zeros_left(
        x_sum_number, y_sum_number)

    result = sum_str(x_sum_number + x_sum_decimal, y_sum_number +
                     y_sum_decimal) if sum_or_sub else sub_str(x_sum_number + x_sum_decimal, y_sum_number + y_sum_decimal)
    print(result)

    partDecimal = result[mayor_number:len(result)] if len(
        result) == mayor_decimal + mayor_number else result[mayor_decimal+1:len(result)]
    partNumber = result[:mayor_number] if len(
        result) == mayor_decimal + mayor_number else result[:mayor_number+1]

    print(partDecimal, partNumber)

    return Numbers(eliminate_zeros_left(partNumber), eliminate_zeros_right(partDecimal), positive, max(x.presicion, y.presicion))


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
